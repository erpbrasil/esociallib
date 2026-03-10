"""
Builder para S-1202 — Remuneracao de Servidor vinculado ao RPPS.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1202 e um evento periodico que informa as rubricas de remuneracao
de cada servidor vinculado ao Regime Proprio de Previdencia Social (RPPS)
em um periodo de apuracao.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v_S_01_03_00"


@register_builder("S-1202")
def build_s1202(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1202 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideEvento (T_ideEvento_folha_opp)
            "ind_apuracao": 1,              # 1=Mensal, 2=Anual (13o)
            "per_apur": "2024-03",          # YYYY-MM ou YYYY

            # ideTrabalhador
            "cpf_trab": "12345678901",

            # ideTrabalhador/infoComplem (opcional)
            "info_complem": {
                "nm_trab": "NOME DO SERVIDOR",
                "dt_nascto": "1990-01-15",
                "sucessao_vinc": {              # opcional
                    "cnpj_orgao_ant": "98765432000188",
                    "matric_ant": "ANT001",     # opcional
                    "dt_exercicio": "2020-01-01",
                    "observacao": "obs",        # opcional
                },
            },

            # dmDev (lista de demonstrativos)
            "dm_dev": [
                {
                    "ide_dm_dev": "DEM001",
                    "cod_categ": "301",
                    "info_per_apur": {
                        "ide_estab": [
                            {
                                "tp_insc": 1,
                                "nr_insc": "12345678000199",
                                "remun_per_apur": [
                                    {
                                        "matricula": "000123",
                                        "itens_remun": [
                                            {
                                                "cod_rubr": "RUBR001",
                                                "ide_tab_rubr": "TAB1",
                                                "vr_rubr": "5000.00",
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

    root, evt = make_esocial("evtRmnRPPS", event_id, _NAMESPACE)

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

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # ideTrabalhador
    ide_trabalhador = sub(evt, "ideTrabalhador")
    sub(ide_trabalhador, "cpfTrab", str(data["cpf_trab"]))

    # infoComplem (opcional)
    info_complem_data = data.get("info_complem")
    if info_complem_data:
        _build_info_complem(ide_trabalhador, info_complem_data)

    # dmDev (lista de demonstrativos)
    for dm in data.get("dm_dev", []):
        _build_dm_dev(evt, dm)

    return EventoXml(root, _NAMESPACE)


def _build_info_complem(parent, info: dict) -> None:
    """Constroi o grupo infoComplem do ideTrabalhador."""
    info_complem = sub(parent, "infoComplem")
    sub(info_complem, "nmTrab", str(info["nm_trab"]))
    sub(info_complem, "dtNascto", str(info["dt_nascto"]))

    sucess = info.get("sucessao_vinc")
    if sucess:
        sucessao = sub(info_complem, "sucessaoVinc")
        sub(sucessao, "cnpjOrgaoAnt", str(sucess["cnpj_orgao_ant"]))
        if sucess.get("matric_ant"):
            sub(sucessao, "matricAnt", str(sucess["matric_ant"]))
        sub(sucessao, "dtExercicio", str(sucess["dt_exercicio"]))
        if sucess.get("observacao"):
            sub(sucessao, "observacao", str(sucess["observacao"]))


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
        for estab in info_per_apur_data.get("ide_estab", []):
            _build_ide_estab(info_per_apur, estab, "remunPerApur")

    # infoPerAnt
    info_per_ant_data = dm.get("info_per_ant")
    if info_per_ant_data:
        info_per_ant = sub(dm_dev, "infoPerAnt")
        sub(info_per_ant, "remunOrgSuc", str(info_per_ant_data["remun_org_suc"]))
        for periodo in info_per_ant_data.get("ide_periodo", []):
            _build_ide_periodo(info_per_ant, periodo)


def _build_ide_estab(parent, estab: dict, remun_tag: str) -> None:
    """Constroi um grupo ideEstab."""
    ide_estab = sub(parent, "ideEstab")
    sub(ide_estab, "tpInsc", str(estab["tp_insc"]))
    sub(ide_estab, "nrInsc", str(estab["nr_insc"]))

    for remun in estab.get("remun_per_apur", estab.get("remun_per_ant", [])):
        _build_remun(ide_estab, remun, remun_tag)


def _build_ide_periodo(parent, periodo: dict) -> None:
    """Constroi um grupo idePeriodo dentro de infoPerAnt."""
    ide_periodo = sub(parent, "idePeriodo")
    sub(ide_periodo, "perRef", str(periodo["per_ref"]))
    for estab in periodo.get("ide_estab", []):
        _build_ide_estab(ide_periodo, estab, "remunPerAnt")


def _build_remun(parent, remun: dict, tag: str) -> None:
    """Constroi um grupo remunPerApur ou remunPerAnt."""
    remun_el = sub(parent, tag)
    if remun.get("matricula"):
        sub(remun_el, "matricula", str(remun["matricula"]))

    for item in remun.get("itens_remun", []):
        _build_item_remun(remun_el, item)


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
