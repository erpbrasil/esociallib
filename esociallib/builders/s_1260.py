"""
Builder para S-1260 — Comercializacao da Producao Rural Pessoa Fisica.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1260 e um evento periodico que informa os valores da comercializacao
da producao rural por pessoa fisica.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtComProd/v_S_01_03_00"


@register_builder("S-1260")
def build_s1260(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1260 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador (tpInsc fixo=2 CPF)
            "tp_insc": 2,                   # Sempre 2=CPF (PF)
            "nr_insc": "12345678901",       # CPF do produtor rural

            # ideEvento (T_ideEvento_folha_mensal_PF)
            "per_apur": "2024-03",          # YYYY-MM

            # infoComProd
            "info_com_prod": {
                "ide_estabel": {
                    "nr_insc_estab_rural": "12345678901234",  # CAEPF 14 digitos
                    "tp_comerc": [
                        {
                            "ind_comerc": 2,              # tipo comercializacao
                            "vr_tot_com": "50000.00",     # valor total
                            "ide_adquir": [               # opcional
                                {
                                    "tp_insc": 1,
                                    "nr_insc": "98765432000100",
                                    "vr_comerc": "30000.00",
                                    "nfs": [              # opcional
                                        {
                                            "serie": "1",
                                            "nr_docto": "000123",
                                            "dt_emis_nf": "2024-03-15",
                                            "vlr_bruto": "30000.00",
                                            "vr_cp_desc_pr": "0.00",
                                            "vr_rat_desc_pr": "0.00",
                                            "vr_senar_desc": "0.00",
                                        }
                                    ],
                                }
                            ],
                            "info_proc_jud": [],          # opcional
                        }
                    ],
                },
            },
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtComProd", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_folha_mensal_PF)
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

    # ideEmpregador (tpInsc=2, CPF)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # infoComProd
    info_com_prod_data = data["info_com_prod"]
    info_com_prod = sub(evt, "infoComProd")

    # ideEstabel
    ide_estabel_data = info_com_prod_data["ide_estabel"]
    ide_estabel = sub(info_com_prod, "ideEstabel")
    sub(ide_estabel, "nrInscEstabRural", str(ide_estabel_data["nr_insc_estab_rural"]))

    for tp in ide_estabel_data.get("tp_comerc", []):
        _build_tp_comerc(ide_estabel, tp)

    return EventoXml(root, _NAMESPACE)


def _build_tp_comerc(parent, tp: dict) -> None:
    """Constroi um grupo tpComerc."""
    tp_comerc = sub(parent, "tpComerc")
    sub(tp_comerc, "indComerc", str(tp["ind_comerc"]))
    sub(tp_comerc, "vrTotCom", str(tp["vr_tot_com"]))

    for adq in tp.get("ide_adquir", []):
        _build_ide_adquir(tp_comerc, adq)

    for proc in tp.get("info_proc_jud", []):
        _build_info_proc_jud(tp_comerc, proc)


def _build_ide_adquir(parent, adq: dict) -> None:
    """Constroi um grupo ideAdquir."""
    ide_adquir = sub(parent, "ideAdquir")
    sub(ide_adquir, "tpInsc", str(adq["tp_insc"]))
    sub(ide_adquir, "nrInsc", str(adq["nr_insc"]))
    sub(ide_adquir, "vrComerc", str(adq["vr_comerc"]))

    for nf in adq.get("nfs", []):
        _build_nfs(ide_adquir, nf)


def _build_nfs(parent, nf: dict) -> None:
    """Constroi um grupo nfs."""
    nfs = sub(parent, "nfs")
    if nf.get("serie"):
        sub(nfs, "serie", str(nf["serie"]))
    sub(nfs, "nrDocto", str(nf["nr_docto"]))
    sub(nfs, "dtEmisNF", str(nf["dt_emis_nf"]))
    sub(nfs, "vlrBruto", str(nf["vlr_bruto"]))
    sub(nfs, "vrCPDescPR", str(nf["vr_cp_desc_pr"]))
    sub(nfs, "vrRatDescPR", str(nf["vr_rat_desc_pr"]))
    sub(nfs, "vrSenarDesc", str(nf["vr_senar_desc"]))


def _build_info_proc_jud(parent, proc: dict) -> None:
    """Constroi um grupo infoProcJud."""
    info_proc_jud = sub(parent, "infoProcJud")
    sub(info_proc_jud, "tpProc", str(proc["tp_proc"]))
    sub(info_proc_jud, "nrProc", str(proc["nr_proc"]))
    sub(info_proc_jud, "codSusp", str(proc["cod_susp"]))
    if proc.get("vr_cp_susp") is not None:
        sub(info_proc_jud, "vrCPSusp", str(proc["vr_cp_susp"]))
    if proc.get("vr_rat_susp") is not None:
        sub(info_proc_jud, "vrRatSusp", str(proc["vr_rat_susp"]))
    if proc.get("vr_senar_susp") is not None:
        sub(info_proc_jud, "vrSenarSusp", str(proc["vr_senar_susp"]))
