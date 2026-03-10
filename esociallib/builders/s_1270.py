"""
Builder para S-1270 — Contratacao de Trabalhadores Avulsos Nao Portuarios.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1270 e um evento periodico que informa a remuneracao totalizada
dos trabalhadores avulsos nao portuarios contratados.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtContratAvNP/v_S_01_03_00"


@register_builder("S-1270")
def build_s1270(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1270 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideEvento (T_ideEvento_folha_mensal)
            "per_apur": "2024-03",          # YYYY-MM

            # remunAvNP (lista)
            "remun_av_np": [
                {
                    "tp_insc": 1,
                    "nr_insc": "12345678000199",
                    "cod_lotacao": "LOT001",
                    "vr_bc_cp00": "10000.00",
                    "vr_bc_cp15": "0.00",
                    "vr_bc_cp20": "0.00",
                    "vr_bc_cp25": "0.00",
                    "vr_bc_cp13": "0.00",
                    "vr_bc_fgts": "10000.00",
                    "vr_desc_cp": "800.00",
                },
            ],
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtContratAvNP", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_folha_mensal)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
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

    # remunAvNP (lista)
    for remun in data.get("remun_av_np", []):
        _build_remun_av_np(evt, remun)

    return EventoXml(root, _NAMESPACE)


def _build_remun_av_np(parent, remun: dict) -> None:
    """Constroi um grupo remunAvNP."""
    remun_av = sub(parent, "remunAvNP")
    sub(remun_av, "tpInsc", str(remun["tp_insc"]))
    sub(remun_av, "nrInsc", str(remun["nr_insc"]))
    sub(remun_av, "codLotacao", str(remun["cod_lotacao"]))
    sub(remun_av, "vrBcCp00", str(remun["vr_bc_cp00"]))
    sub(remun_av, "vrBcCp15", str(remun["vr_bc_cp15"]))
    sub(remun_av, "vrBcCp20", str(remun["vr_bc_cp20"]))
    sub(remun_av, "vrBcCp25", str(remun["vr_bc_cp25"]))
    sub(remun_av, "vrBcCp13", str(remun["vr_bc_cp13"]))
    sub(remun_av, "vrBcFgts", str(remun["vr_bc_fgts"]))
    sub(remun_av, "vrDescCP", str(remun["vr_desc_cp"]))
