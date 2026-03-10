"""
Builder para S-3500 — Exclusao de Eventos - Processo Trabalhista.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-3500 permite a exclusao de eventos de processo trabalhista
(S-2500, S-2501, S-2555) previamente enviados ao eSocial.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtExcProcTrab/v_S_01_03_00"


@register_builder("S-3500")
def build_s3500(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-3500 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # infoExclusao
            "tp_evento": "S-2500",              # S-2500, S-2501 ou S-2555
            "nr_rec_evt": "1.2.1234567.1234567890",

            # ideProcTrab
            "nr_proc_trab": "12345678901234567890",
            "cpf_trab": "12345678901",          # (obrig. se tpEvento=S-2500)
            "per_apur_pgto": None,              # (obrig. se tpEvento=S-2501/S-2555)
            "ide_seq_proc": None,               # (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtExcProcTrab", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_exclusao_proc_trab: tpAmb, procEmi, verProc)
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

    # ideProcTrab
    ide_proc = sub(info_exclusao, "ideProcTrab")
    sub(ide_proc, "nrProcTrab", str(data["nr_proc_trab"]))
    if data.get("cpf_trab"):
        sub(ide_proc, "cpfTrab", str(data["cpf_trab"]))
    if data.get("per_apur_pgto"):
        sub(ide_proc, "perApurPgto", str(data["per_apur_pgto"]))
    if data.get("ide_seq_proc") is not None:
        sub(ide_proc, "ideSeqProc", str(data["ide_seq_proc"]))

    return EventoXml(root, _NAMESPACE)
