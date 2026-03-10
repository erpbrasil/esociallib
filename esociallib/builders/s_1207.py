"""
Builder para S-1207 — Beneficios Previdenciarios - Entes Publicos (RPPS).

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1207 e um evento periodico que informa os proventos e pensoes
pagos por entes publicos a seus beneficiarios (aposentados e pensionistas).
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtBenPrRP/v_S_01_03_00"


@register_builder("S-1207")
def build_s1207(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1207 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador (T_ideEmpregador_cnpj)
            "tp_insc": 1,                   # Sempre 1=CNPJ
            "nr_insc": "12345678",          # CNPJ raiz

            # ideEvento (T_ideEvento_folha_opp)
            "ind_apuracao": 1,              # 1=Mensal, 2=Anual (13o)
            "per_apur": "2024-03",          # YYYY-MM ou YYYY

            # ideBenef
            "cpf_benef": "12345678901",

            # dmDev (lista de demonstrativos)
            "dm_dev": [
                {
                    "ide_dm_dev": "DEM001",
                    "nr_beneficio": "BEN001",
                    "info_per_apur": {
                        "ide_estab": [
                            {
                                "tp_insc": 1,
                                "nr_insc": "12345678000199",
                                "itens_remun": [
                                    {
                                        "cod_rubr": "RUBR001",
                                        "ide_tab_rubr": "TAB1",
                                        "vr_rubr": "3000.00",
                                    }
                                ],
                            }
                        ],
                    },
                }
            ],
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtBenPrRP", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_folha_opp — sem indGuia)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
    sub(ide_evento, "indApuracao", str(data["ind_apuracao"]))
    sub(ide_evento, "perApur", str(data["per_apur"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador_cnpj)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # ideBenef
    ide_benef = sub(evt, "ideBenef")
    sub(ide_benef, "cpfBenef", str(data["cpf_benef"]))

    # dmDev (lista de demonstrativos)
    for dm in data.get("dm_dev", []):
        _build_dm_dev(evt, dm)

    return EventoXml(root, _NAMESPACE)


def _build_dm_dev(parent, dm: dict) -> None:
    """Constroi um grupo dmDev (demonstrativo de valores devidos)."""
    dm_dev = sub(parent, "dmDev")
    sub(dm_dev, "ideDmDev", str(dm["ide_dm_dev"]))
    sub(dm_dev, "nrBeneficio", str(dm["nr_beneficio"]))
    if dm.get("ind_rra"):
        sub(dm_dev, "indRRA", str(dm["ind_rra"]))

    # infoPerApur
    info_per_apur_data = dm.get("info_per_apur")
    if info_per_apur_data:
        info_per_apur = sub(dm_dev, "infoPerApur")
        for estab in info_per_apur_data.get("ide_estab", []):
            _build_ide_estab_per_apur(info_per_apur, estab)

    # infoPerAnt
    info_per_ant_data = dm.get("info_per_ant")
    if info_per_ant_data:
        info_per_ant = sub(dm_dev, "infoPerAnt")
        for periodo in info_per_ant_data.get("ide_periodo", []):
            _build_ide_periodo(info_per_ant, periodo)


def _build_ide_estab_per_apur(parent, estab: dict) -> None:
    """Constroi um grupo ideEstab para periodo de apuracao (T_ideEstab_perApur)."""
    ide_estab = sub(parent, "ideEstab")
    sub(ide_estab, "tpInsc", str(estab["tp_insc"]))
    sub(ide_estab, "nrInsc", str(estab["nr_insc"]))
    for item in estab.get("itens_remun", []):
        _build_item_remun(ide_estab, item)


def _build_ide_periodo(parent, periodo: dict) -> None:
    """Constroi um grupo idePeriodo dentro de infoPerAnt."""
    ide_periodo = sub(parent, "idePeriodo")
    sub(ide_periodo, "perRef", str(periodo["per_ref"]))
    for estab in periodo.get("ide_estab", []):
        _build_ide_estab_per_ant(ide_periodo, estab)


def _build_ide_estab_per_ant(parent, estab: dict) -> None:
    """Constroi um grupo ideEstab para periodo anterior (T_ideEstab_perAnt)."""
    ide_estab = sub(parent, "ideEstab")
    sub(ide_estab, "tpInsc", str(estab["tp_insc"]))
    sub(ide_estab, "nrInsc", str(estab["nr_insc"]))
    for item in estab.get("itens_remun", []):
        _build_item_remun(ide_estab, item)


def _build_item_remun(parent, item: dict) -> None:
    """Constroi um grupo itensRemun (T_itensRemun_rpps)."""
    itens_remun = sub(parent, "itensRemun")
    sub(itens_remun, "codRubr", str(item["cod_rubr"]))
    sub(itens_remun, "ideTabRubr", str(item["ide_tab_rubr"]))
    if item.get("qtd_rubr") is not None:
        sub(itens_remun, "qtdRubr", str(item["qtd_rubr"]))
    if item.get("fator_rubr") is not None:
        sub(itens_remun, "fatorRubr", str(item["fator_rubr"]))
    sub(itens_remun, "vrRubr", str(item["vr_rubr"]))
    if item.get("ind_apur_ir") is not None:
        sub(itens_remun, "indApurIR", str(item["ind_apur_ir"]))
