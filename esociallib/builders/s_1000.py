"""
Builder para S-1000 — Informacoes do Empregador/Contribuinte/Orgao Publico.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1000 e um evento de tabela com operacoes de inclusao, alteracao ou exclusao.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00"


@register_builder("S-1000")
def build_s1000(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1000 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # operacao: "inclusao", "alteracao" ou "exclusao"
            "operacao": "inclusao",

            # idePeriodo
            "ini_valid": "2024-01",         # YYYY-MM
            "fim_valid": "2099-12",         # YYYY-MM (opcional)

            # infoCadastro (obrigatorio para inclusao/alteracao)
            "class_trib": "01",             # Tabela 08 - Classificacao tributaria
            "ind_coop": 0,                  # 0=Nao e cooperativa (opcional, PJ)
            "ind_constr": 0,                # 0=Nao e construtora (opcional, PJ)
            "ind_des_folha": 0,             # 0=Nao aplicavel
            "ind_opt_reg_eletron": 0,       # 0=Nao optou

            # novaValidade (apenas para alteracao, opcional)
            "nova_ini_valid": "2024-03",    # YYYY-MM (opcional)
            "nova_fim_valid": "2099-12",    # YYYY-MM (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtInfoEmpregador", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_exclusao: tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # infoEmpregador
    info_empregador = sub(evt, "infoEmpregador")

    operacao = data.get("operacao", "inclusao")

    if operacao == "inclusao":
        inclusao = sub(info_empregador, "inclusao")

        # idePeriodo
        ide_periodo = sub(inclusao, "idePeriodo")
        sub(ide_periodo, "iniValid", str(data["ini_valid"]))
        if data.get("fim_valid"):
            sub(ide_periodo, "fimValid", str(data["fim_valid"]))

        # infoCadastro
        _build_info_cadastro(inclusao, data)

    elif operacao == "alteracao":
        alteracao = sub(info_empregador, "alteracao")

        # idePeriodo
        ide_periodo = sub(alteracao, "idePeriodo")
        sub(ide_periodo, "iniValid", str(data["ini_valid"]))
        if data.get("fim_valid"):
            sub(ide_periodo, "fimValid", str(data["fim_valid"]))

        # infoCadastro
        _build_info_cadastro(alteracao, data)

        # novaValidade (opcional)
        if data.get("nova_ini_valid"):
            nova_validade = sub(alteracao, "novaValidade")
            sub(nova_validade, "iniValid", str(data["nova_ini_valid"]))
            if data.get("nova_fim_valid"):
                sub(nova_validade, "fimValid", str(data["nova_fim_valid"]))

    elif operacao == "exclusao":
        exclusao = sub(info_empregador, "exclusao")

        # idePeriodo
        ide_periodo = sub(exclusao, "idePeriodo")
        sub(ide_periodo, "iniValid", str(data["ini_valid"]))
        if data.get("fim_valid"):
            sub(ide_periodo, "fimValid", str(data["fim_valid"]))

    return EventoXml(root, _NAMESPACE)


def _build_info_cadastro(parent, data: dict) -> None:
    """Constroi o grupo infoCadastro dentro de inclusao ou alteracao."""
    if not data.get("class_trib"):
        return

    info_cadastro = sub(parent, "infoCadastro")
    sub(info_cadastro, "classTrib", str(data["class_trib"]))
    if data.get("ind_coop") is not None:
        sub(info_cadastro, "indCoop", str(data["ind_coop"]))
    if data.get("ind_constr") is not None:
        sub(info_cadastro, "indConstr", str(data["ind_constr"]))
    sub(info_cadastro, "indDesFolha", str(data.get("ind_des_folha", 0)))
    if data.get("ind_opc_cp") is not None:
        sub(info_cadastro, "indOpcCP", str(data["ind_opc_cp"]))
    if data.get("ind_porte"):
        sub(info_cadastro, "indPorte", str(data["ind_porte"]))
    sub(info_cadastro, "indOptRegEletron", str(data.get("ind_opt_reg_eletron", 0)))
    if data.get("cnpj_efr"):
        sub(info_cadastro, "cnpjEFR", str(data["cnpj_efr"]))
    if data.get("dt_trans_11096"):
        sub(info_cadastro, "dtTrans11096", str(data["dt_trans_11096"]))
    if data.get("ind_trib_folha_pis_pasep"):
        sub(info_cadastro, "indTribFolhaPisPasep", str(data["ind_trib_folha_pis_pasep"]))
    if data.get("ind_pert_irrf"):
        sub(info_cadastro, "indPertIRRF", str(data["ind_pert_irrf"]))
