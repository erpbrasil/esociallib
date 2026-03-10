"""
Builder para S-1298 — Reabertura dos Eventos Periodicos.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1298 sinaliza ao governo que o periodo de apuracao previamente
fechado pelo S-1299 sera reaberto para correcoes ou complementos.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtReabreEvPer/v_S_01_03_00"


@register_builder("S-1298")
def build_s1298(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1298 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideEvento (T_ideEvento_folha_sem_retificacao)
            "ind_apuracao": 1,              # 1=Mensal, 2=Anual (13o)
            "per_apur": "2024-03",          # YYYY-MM ou YYYY
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtReabreEvPer", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_folha_sem_retificacao)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indApuracao", str(data["ind_apuracao"]))
    sub(ide_evento, "perApur", str(data["per_apur"]))
    if data.get("ind_guia") is not None:
        sub(ide_evento, "indGuia", str(data["ind_guia"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    return EventoXml(root, _NAMESPACE)
