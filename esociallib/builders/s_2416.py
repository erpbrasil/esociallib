"""
Builder para S-2416 — Cadastro de Beneficio - Entes Publicos - Alteracao.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2416 registra alteracoes nos dados de um beneficio previdenciario
de regime proprio (RPPS) em entes publicos.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtCdBenAlt/v_S_01_03_00"


@register_builder("S-2416")
def build_s2416(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2416 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # ideBeneficio
            "cpf_benef": "12345678901",
            "nr_beneficio": "BEN001",

            # infoBenAlteracao
            "dt_alt_beneficio": "2024-06-01",

            # dadosBeneficio
            "tp_beneficio": "0101",
            "tp_plan_rp": 1,
            "dsc": None,                    # (opcional)
            "ind_suspensao": "N",

            # infoPenMorte (opcional)
            "tp_pen_morte": None,

            # suspensao (opcional - se indSuspensao=S)
            "mtv_suspensao": None,
            "dsc_suspensao": None,
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtCdBenAlt", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab_PJ)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador_cnpj)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # ideBeneficio (T_ideBeneficio)
    ide_beneficio = sub(evt, "ideBeneficio")
    sub(ide_beneficio, "cpfBenef", str(data["cpf_benef"]))
    sub(ide_beneficio, "nrBeneficio", str(data["nr_beneficio"]))

    # infoBenAlteracao
    info_alt = sub(evt, "infoBenAlteracao")
    sub(info_alt, "dtAltBeneficio", str(data["dt_alt_beneficio"]))

    # dadosBeneficio
    dados_ben = sub(info_alt, "dadosBeneficio")
    sub(dados_ben, "tpBeneficio", str(data["tp_beneficio"]))
    sub(dados_ben, "tpPlanRP", str(data["tp_plan_rp"]))
    if data.get("dsc"):
        sub(dados_ben, "dsc", str(data["dsc"]))
    sub(dados_ben, "indSuspensao", str(data.get("ind_suspensao", "N")))

    # infoPenMorte (opcional)
    if data.get("tp_pen_morte") is not None:
        info_pen = sub(dados_ben, "infoPenMorte")
        sub(info_pen, "tpPenMorte", str(data["tp_pen_morte"]))
        if data.get("tp_dep_inst") is not None:
            inst = sub(info_pen, "instPenMorte")
            sub(inst, "tpDepInst", str(data["tp_dep_inst"]))
            if data.get("descr_dep_inst"):
                sub(inst, "descrDepInst", str(data["descr_dep_inst"]))

    # suspensao (se indSuspensao=S)
    if data.get("mtv_suspensao"):
        suspensao = sub(dados_ben, "suspensao")
        sub(suspensao, "mtvSuspensao", str(data["mtv_suspensao"]))
        if data.get("dsc_suspensao"):
            sub(suspensao, "dscSuspensao", str(data["dsc_suspensao"]))

    return EventoXml(root, _NAMESPACE)
