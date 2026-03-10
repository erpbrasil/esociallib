"""
Builder para S-2399 — Trabalhador Sem Vinculo - Termino.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2399 registra o termino da prestacao de servicos por trabalhadores
sem vinculo empregaticio (TSVE), incluindo opcionalmente verbas rescisorias.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtTSVTermino/v_S_01_03_00"


@register_builder("S-2399")
def build_s2399(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2399 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # ideTrabSemVinculo
            "cpf_trab": "12345678901",
            "matricula": "000123",          # (opcional)
            "cod_categ": "901",             # (opcional)

            # infoTSVTermino
            "dt_term": "2024-12-31",
            "mtv_deslig_tsv": "01",         # (opcional)
            "pens_alim": 0,                 # (opcional)
            "perc_aliment": None,           # (opcional)
            "vr_alim": None,               # (opcional)
            "nr_proc_trab": None,           # (opcional)

            # mudancaCPF (opcional - motivo 07)
            "novo_cpf": None,

            # verbasResc (opcional)
            "verbas_resc": [],

            # remunAposTerm (opcional)
            "ind_remun": None,
            "dt_fim_remun": None,
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtTSVTermino", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab_indGuia)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
    if data.get("ind_guia") is not None:
        sub(ide_evento, "indGuia", str(data["ind_guia"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # ideTrabSemVinculo (T_ideTrabSemVinculo)
    ide_trab = sub(evt, "ideTrabSemVinculo")
    sub(ide_trab, "cpfTrab", str(data["cpf_trab"]))
    if data.get("matricula"):
        sub(ide_trab, "matricula", str(data["matricula"]))
    if data.get("cod_categ"):
        sub(ide_trab, "codCateg", str(data["cod_categ"]))

    # infoTSVTermino
    info_term = sub(evt, "infoTSVTermino")
    sub(info_term, "dtTerm", str(data["dt_term"]))
    if data.get("mtv_deslig_tsv"):
        sub(info_term, "mtvDesligTSV", str(data["mtv_deslig_tsv"]))
    if data.get("pens_alim") is not None:
        sub(info_term, "pensAlim", str(data["pens_alim"]))
    if data.get("perc_aliment") is not None:
        sub(info_term, "percAliment", str(data["perc_aliment"]))
    if data.get("vr_alim") is not None:
        sub(info_term, "vrAlim", str(data["vr_alim"]))
    if data.get("nr_proc_trab"):
        sub(info_term, "nrProcTrab", str(data["nr_proc_trab"]))

    # mudancaCPF (motivo 07)
    if data.get("novo_cpf"):
        mudanca_cpf = sub(info_term, "mudancaCPF")
        sub(mudanca_cpf, "novoCPF", str(data["novo_cpf"]))

    # verbasResc (opcional)
    verbas_resc_list = data.get("verbas_resc", [])
    if verbas_resc_list:
        verbas_resc = sub(info_term, "verbasResc")
        for dm in verbas_resc_list:
            _build_dm_dev(verbas_resc, dm)

    # remunAposTerm (opcional)
    if data.get("dt_fim_remun"):
        remun_apos = sub(info_term, "remunAposTerm")
        if data.get("ind_remun") is not None:
            sub(remun_apos, "indRemun", str(data["ind_remun"]))
        sub(remun_apos, "dtFimRemun", str(data["dt_fim_remun"]))

    return EventoXml(root, _NAMESPACE)


def _build_dm_dev(parent, dm: dict) -> None:
    """Constroi um grupo dmDev (demonstrativo de valores devidos)."""
    dm_dev = sub(parent, "dmDev")
    sub(dm_dev, "ideDmDev", str(dm["ide_dm_dev"]))
    if dm.get("ind_rra"):
        sub(dm_dev, "indRRA", str(dm["ind_rra"]))

    for estab_lot in dm.get("ide_estab_lot", []):
        _build_ide_estab_lot(dm_dev, estab_lot)


def _build_ide_estab_lot(parent, estab_lot: dict) -> None:
    """Constroi um grupo ideEstabLot."""
    ide_estab_lot = sub(parent, "ideEstabLot")
    sub(ide_estab_lot, "tpInsc", str(estab_lot["tp_insc"]))
    sub(ide_estab_lot, "nrInsc", str(estab_lot["nr_insc"]))
    sub(ide_estab_lot, "codLotacao", str(estab_lot["cod_lotacao"]))

    for det in estab_lot.get("det_verbas", []):
        _build_det_verbas(ide_estab_lot, det)


def _build_det_verbas(parent, det: dict) -> None:
    """Constroi um grupo detVerbas."""
    det_verbas = sub(parent, "detVerbas")
    sub(det_verbas, "codRubr", str(det["cod_rubr"]))
    sub(det_verbas, "ideTabRubr", str(det["ide_tab_rubr"]))
    if det.get("qtd_rubr") is not None:
        sub(det_verbas, "qtdRubr", str(det["qtd_rubr"]))
    if det.get("fator_rubr") is not None:
        sub(det_verbas, "fatorRubr", str(det["fator_rubr"]))
    sub(det_verbas, "vrRubr", str(det["vr_rubr"]))
    if det.get("ind_apur_ir") is not None:
        sub(det_verbas, "indApurIR", str(det["ind_apur_ir"]))
