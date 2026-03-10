"""
Builder para S-2190 -- Registro Preliminar de Trabalhador.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2190 e um evento nao-periodico que registra previamente a admissao
de um trabalhador antes do envio completo do S-2200, permitindo o
cumprimento do prazo legal de registro.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00"


@register_builder("S-2190")
def build_s2190(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2190 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # infoRegPrelim
            "cpf_trab": "12345678901",
            "dt_nascto": "1990-05-20",      # YYYY-MM-DD
            "dt_adm": "2024-03-01",         # YYYY-MM-DD
            "matricula": "000123",
            "cod_categ": "101",             # Codigo da categoria do trabalhador
            "nat_atividade": 1,             # 1=Normal, 2=Aprendiz (opcional)

            # infoRegCTPS (opcional - informacoes de registro e CTPS Digital)
            "cod_cbo": "252105",            # CBO relativo ao cargo (opcional)
            "vr_sal_fx": "5000.00",         # Salario fixo (opcional)
            "und_sal_fixo": 5,              # Unidade salario fixo (opcional)
            "tp_contr": 1,                  # 1=Indeterminado, 2=Determinado (opcional)
            "dt_term": None,               # Data termino contrato (opcional, se tp_contr=2)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtAdmPrelim", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab_admissao: indRetif, nrRecibo, tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # infoRegPrelim
    info_reg_prelim = sub(evt, "infoRegPrelim")
    sub(info_reg_prelim, "cpfTrab", str(data["cpf_trab"]))
    sub(info_reg_prelim, "dtNascto", str(data["dt_nascto"]))
    sub(info_reg_prelim, "dtAdm", str(data["dt_adm"]))
    sub(info_reg_prelim, "matricula", str(data["matricula"]))
    sub(info_reg_prelim, "codCateg", str(data["cod_categ"]))
    if data.get("nat_atividade") is not None:
        sub(info_reg_prelim, "natAtividade", str(data["nat_atividade"]))

    # infoRegCTPS (opcional - informacoes de registro e CTPS Digital)
    if data.get("cod_cbo"):
        info_reg_ctps = sub(info_reg_prelim, "infoRegCTPS")
        sub(info_reg_ctps, "CBOCargo", str(data["cod_cbo"]))
        sub(info_reg_ctps, "vrSalFx", str(data["vr_sal_fx"]))
        sub(info_reg_ctps, "undSalFixo", str(data["und_sal_fixo"]))
        sub(info_reg_ctps, "tpContr", str(data["tp_contr"]))
        if data.get("dt_term"):
            sub(info_reg_ctps, "dtTerm", str(data["dt_term"]))

    return EventoXml(root, _NAMESPACE)
