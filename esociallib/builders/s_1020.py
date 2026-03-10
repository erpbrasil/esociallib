"""
Builder para S-1020 — Tabela de Lotacoes Tributarias.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1020 e um evento de tabela com operacoes de inclusao, alteracao ou exclusao
de lotacoes tributarias (agrupamento de FPAS/terceiros).
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00"


@register_builder("S-1020")
def build_s1020(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1020 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # operacao: "inclusao", "alteracao" ou "exclusao"
            "operacao": "inclusao",

            # ideLotacao
            "cod_lotacao": "LOT001",        # Codigo da lotacao
            "ini_valid": "2024-01",         # YYYY-MM
            "fim_valid": "2099-12",         # YYYY-MM (opcional)

            # dadosLotacao (obrigatorio para inclusao/alteracao)
            "tp_lotacao": "01",             # Tipo de lotacao (Tabela 10)
            "tp_insc_lotacao": 1,           # Tipo insc. da lotacao (opcional, depende tpLotacao)
            "nr_insc_lotacao": "12345678000199",  # Nr insc. da lotacao (opcional)

            # fpasLotacao
            "fpas": "515",                  # Codigo FPAS
            "cod_tercs": "0079",            # Codigo de terceiros
            "cod_tercs_susp": "0000",       # Codigo de terceiros suspenso (opcional)

            # novaValidade (apenas para alteracao, opcional)
            "nova_ini_valid": "2024-03",    # YYYY-MM (opcional)
            "nova_fim_valid": "2099-12",    # YYYY-MM (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtTabLotacao", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_evtTab: tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # infoLotacao
    info_lotacao = sub(evt, "infoLotacao")

    operacao = data.get("operacao", "inclusao")

    if operacao == "inclusao":
        inclusao = sub(info_lotacao, "inclusao")
        _build_ide_lotacao(inclusao, data)
        _build_dados_lotacao(inclusao, data)

    elif operacao == "alteracao":
        alteracao = sub(info_lotacao, "alteracao")
        _build_ide_lotacao(alteracao, data)
        _build_dados_lotacao(alteracao, data)

        # novaValidade (opcional)
        if data.get("nova_ini_valid"):
            nova_validade = sub(alteracao, "novaValidade")
            sub(nova_validade, "iniValid", str(data["nova_ini_valid"]))
            if data.get("nova_fim_valid"):
                sub(nova_validade, "fimValid", str(data["nova_fim_valid"]))

    elif operacao == "exclusao":
        exclusao = sub(info_lotacao, "exclusao")
        _build_ide_lotacao(exclusao, data)

    return EventoXml(root, _NAMESPACE)


def _build_ide_lotacao(parent, data: dict) -> None:
    """Constroi o grupo ideLotacao."""
    ide_lotacao = sub(parent, "ideLotacao")
    sub(ide_lotacao, "codLotacao", str(data["cod_lotacao"]))
    sub(ide_lotacao, "iniValid", str(data["ini_valid"]))
    if data.get("fim_valid"):
        sub(ide_lotacao, "fimValid", str(data["fim_valid"]))


def _build_dados_lotacao(parent, data: dict) -> None:
    """Constroi o grupo dadosLotacao."""
    dados_lotacao = sub(parent, "dadosLotacao")
    sub(dados_lotacao, "tpLotacao", str(data["tp_lotacao"]))
    if data.get("tp_insc_lotacao") is not None:
        sub(dados_lotacao, "tpInsc", str(data["tp_insc_lotacao"]))
    if data.get("nr_insc_lotacao"):
        sub(dados_lotacao, "nrInsc", str(data["nr_insc_lotacao"]))

    # fpasLotacao
    fpas_lotacao = sub(dados_lotacao, "fpasLotacao")
    sub(fpas_lotacao, "fpas", str(data["fpas"]))
    sub(fpas_lotacao, "codTercs", str(data["cod_tercs"]))
    if data.get("cod_tercs_susp"):
        sub(fpas_lotacao, "codTercsSusp", str(data["cod_tercs_susp"]))

    # infoEmprParcial (opcional, para tpLotacao = 02)
    if data.get("tp_insc_contrat") is not None:
        info_empr_parcial = sub(dados_lotacao, "infoEmprParcial")
        sub(info_empr_parcial, "tpInscContrat", str(data["tp_insc_contrat"]))
        sub(info_empr_parcial, "nrInscContrat", str(data["nr_insc_contrat"]))
        if data.get("tp_insc_prop") is not None:
            sub(info_empr_parcial, "tpInscProp", str(data["tp_insc_prop"]))
        if data.get("nr_insc_prop"):
            sub(info_empr_parcial, "nrInscProp", str(data["nr_insc_prop"]))

    # dadosOpPort (opcional, para tpLotacao = 08)
    if data.get("aliq_rat") is not None:
        dados_op_port = sub(dados_lotacao, "dadosOpPort")
        sub(dados_op_port, "aliqRat", str(data["aliq_rat"]))
        sub(dados_op_port, "fap", str(data["fap"]))
