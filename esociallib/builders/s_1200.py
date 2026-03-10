"""
Builder para S-1200 — Remuneracao de Trabalhador vinculado ao RGPS.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1200 e um evento periodico que informa as rubricas de remuneracao
de cada trabalhador em um periodo de apuracao.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_03_00"


@register_builder("S-1200")
def build_s1200(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1200 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideEvento
            "ind_apuracao": 1,              # 1=Mensal, 2=Anual (13o)
            "per_apur": "2024-03",          # YYYY-MM ou YYYY

            # ideTrabalhador
            "cpf_trab": "12345678901",

            # dmDev (lista de demonstrativos)
            "dm_dev": [
                {
                    "ide_dm_dev": "DEM001",         # Identificador do demonstrativo
                    "cod_categ": "101",             # Categoria do trabalhador
                    "info_per_apur": {
                        "ide_estab_lot": [
                            {
                                "tp_insc": 1,                   # Tipo inscricao estab.
                                "nr_insc": "12345678000199",    # CNPJ do estab.
                                "cod_lotacao": "LOT001",        # Codigo da lotacao
                                "remun_per_apur": [
                                    {
                                        "matricula": "000123",      # Matricula (opcional)
                                        "itens_remun": [
                                            {
                                                "cod_rubr": "RUBR001",
                                                "ide_tab_rubr": "TAB1",
                                                "vr_rubr": "5000.00",
                                                # opcionais:
                                                "qtd_rubr": "1.00",
                                                "fator_rubr": "1.00",
                                                "ind_apur_ir": 0,
                                            }
                                        ],
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

    root, evt = make_esocial("evtRemun", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_folha)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
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

    # ideTrabalhador
    ide_trabalhador = sub(evt, "ideTrabalhador")
    sub(ide_trabalhador, "cpfTrab", str(data["cpf_trab"]))

    # dmDev (lista de demonstrativos)
    for dm in data.get("dm_dev", []):
        _build_dm_dev(evt, dm)

    return EventoXml(root, _NAMESPACE)


def _build_dm_dev(parent, dm: dict) -> None:
    """Constroi um grupo dmDev (demonstrativo de valores devidos)."""
    dm_dev = sub(parent, "dmDev")
    sub(dm_dev, "ideDmDev", str(dm["ide_dm_dev"]))
    sub(dm_dev, "codCateg", str(dm["cod_categ"]))
    if dm.get("ind_rra"):
        sub(dm_dev, "indRRA", str(dm["ind_rra"]))

    # infoPerApur
    info_per_apur_data = dm.get("info_per_apur")
    if info_per_apur_data:
        info_per_apur = sub(dm_dev, "infoPerApur")
        for estab_lot in info_per_apur_data.get("ide_estab_lot", []):
            _build_ide_estab_lot(info_per_apur, estab_lot)


def _build_ide_estab_lot(parent, estab_lot: dict) -> None:
    """Constroi um grupo ideEstabLot."""
    ide_estab_lot = sub(parent, "ideEstabLot")
    sub(ide_estab_lot, "tpInsc", str(estab_lot["tp_insc"]))
    sub(ide_estab_lot, "nrInsc", str(estab_lot["nr_insc"]))
    sub(ide_estab_lot, "codLotacao", str(estab_lot["cod_lotacao"]))
    if estab_lot.get("qtd_dias_av") is not None:
        sub(ide_estab_lot, "qtdDiasAv", str(estab_lot["qtd_dias_av"]))

    for remun in estab_lot.get("remun_per_apur", []):
        _build_remun_per_apur(ide_estab_lot, remun)


def _build_remun_per_apur(parent, remun: dict) -> None:
    """Constroi um grupo remunPerApur."""
    remun_per_apur = sub(parent, "remunPerApur")
    if remun.get("matricula"):
        sub(remun_per_apur, "matricula", str(remun["matricula"]))
    if remun.get("ind_simples") is not None:
        sub(remun_per_apur, "indSimples", str(remun["ind_simples"]))

    for item in remun.get("itens_remun", []):
        _build_item_remun(remun_per_apur, item)


def _build_item_remun(parent, item: dict) -> None:
    """Constroi um grupo itensRemun."""
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
