"""
Builder para S-2418 — Reativacao de Beneficio - Entes Publicos.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2418 registra a reativacao de um beneficio previdenciario que
havia sido cessado em um ente publico.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtReativBen/v_S_01_03_00"


@register_builder("S-2418")
def build_s2418(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2418 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # ideBeneficio
            "cpf_benef": "12345678901",
            "nr_beneficio": "BEN001",

            # infoReativ
            "dt_efet_reativ": "2024-06-01",
            "dt_efeito": "2024-05-01",
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtReativBen", event_id, _NAMESPACE)

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

    # infoReativ
    info_reativ = sub(evt, "infoReativ")
    sub(info_reativ, "dtEfetReativ", str(data["dt_efet_reativ"]))
    sub(info_reativ, "dtEfeito", str(data["dt_efeito"]))

    return EventoXml(root, _NAMESPACE)
