"""
Builder para S-3000 — Exclusao de Eventos.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-3000 permite a exclusao de eventos periodicos e nao-periodicos
previamente enviados ao eSocial.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtExclusao/v_S_01_03_00"


@register_builder("S-3000")
def build_s3000(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-3000 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # infoExclusao
            "tp_evento": "S-2200",              # Tipo do evento a excluir
            "nr_rec_evt": "1.2.1234567.1234567890",  # Nr recibo do evento

            # ideTrabalhador (obrigatorio para eventos nao-periodicos e periodicos S-1200 a S-1210)
            "cpf_trab": "12345678901",          # (opcional)

            # ideFolhaPagto (obrigatorio para eventos periodicos S-1200 a S-1280/S-1300)
            "ind_apuracao": None,               # (opcional)
            "per_apur": None,                   # (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtExclusao", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_exclusao: tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador_exclusao)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # infoExclusao
    info_exclusao = sub(evt, "infoExclusao")
    sub(info_exclusao, "tpEvento", str(data["tp_evento"]))
    sub(info_exclusao, "nrRecEvt", str(data["nr_rec_evt"]))

    # ideTrabalhador (opcional - para eventos nao-periodicos e periodicos com trabalhador)
    if data.get("cpf_trab"):
        ide_trab = sub(info_exclusao, "ideTrabalhador")
        sub(ide_trab, "cpfTrab", str(data["cpf_trab"]))

    # ideFolhaPagto (opcional - para eventos periodicos)
    if data.get("per_apur"):
        ide_folha = sub(info_exclusao, "ideFolhaPagto")
        if data.get("ind_apuracao") is not None:
            sub(ide_folha, "indApuracao", str(data["ind_apuracao"]))
        sub(ide_folha, "perApur", str(data["per_apur"]))

    return EventoXml(root, _NAMESPACE)
