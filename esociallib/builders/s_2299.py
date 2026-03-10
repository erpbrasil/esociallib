"""
Builder para S-2299 — Desligamento.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2299 e um evento nao-periodico que registra o desligamento do vinculo
empregaticio, incluindo opcionalmente as verbas rescisorias.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00"


@register_builder("S-2299")
def build_s2299(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2299 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideVinculo
            "cpf_trab": "12345678901",
            "matricula": "000123",

            # infoDeslig
            "mtv_deslig": "02",             # Motivo do desligamento (Tabela 19)
            "dt_deslig": "2024-06-30",      # Data do desligamento (ultimo dia)
            "ind_pagto_api": "N",           # S ou N - pagou aviso previo indenizado?
            "dt_proj_fim_api": None,        # Data projetada fim API (obrigatorio se S)
            "pens_alim": 0,                 # 0=Nao, 1=%, 2=Valor, 3=% e Valor (CLT)
            "perc_aliment": None,           # Percentual pensao (se pens_alim=1 ou 3)
            "vr_alim": None,               # Valor pensao (se pens_alim=2 ou 3)

            # opcionais
            "dt_av_prv": None,              # Data concessao aviso previo (opcional)
            "nr_proc_trab": None,           # Nr processo trabalhista (opcional)

            # verbasResc (opcional - lista de demonstrativos)
            "verbas_resc": [
                {
                    "ide_dm_dev": "DEM001",     # Identificador do demonstrativo
                    "info_per_apur": {
                        "ide_estab_lot": [
                            {
                                "tp_insc": 1,
                                "nr_insc": "12345678000199",
                                "cod_lotacao": "LOT001",
                                "det_verbas": [
                                    {
                                        "cod_rubr": "RUBR001",
                                        "ide_tab_rubr": "TAB1",
                                        "vr_rubr": "5000.00",
                                        "qtd_rubr": None,
                                        "fator_rubr": None,
                                        "ind_apur_ir": 0,
                                    }
                                ],
                            }
                        ],
                    },
                }
            ],

            # sucessaoVinc (obrigatorio para motivos 11,12,13,28,29,37,43)
            "suc_tp_insc": None,            # Tipo insc. empresa sucessora
            "suc_nr_insc": None,            # Nr insc. empresa sucessora
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtDeslig", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab_indGuia: indRetif, nrRecibo, indGuia, tpAmb, procEmi, verProc)
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

    # ideVinculo (T_ideVinculo)
    ide_vinculo = sub(evt, "ideVinculo")
    sub(ide_vinculo, "cpfTrab", str(data["cpf_trab"]))
    sub(ide_vinculo, "matricula", str(data["matricula"]))

    # infoDeslig
    info_deslig = sub(evt, "infoDeslig")
    sub(info_deslig, "mtvDeslig", str(data["mtv_deslig"]))
    sub(info_deslig, "dtDeslig", str(data["dt_deslig"]))
    if data.get("dt_av_prv"):
        sub(info_deslig, "dtAvPrv", str(data["dt_av_prv"]))
    sub(info_deslig, "indPagtoAPI", str(data.get("ind_pagto_api", "N")))
    if data.get("dt_proj_fim_api"):
        sub(info_deslig, "dtProjFimAPI", str(data["dt_proj_fim_api"]))
    if data.get("pens_alim") is not None:
        sub(info_deslig, "pensAlim", str(data["pens_alim"]))
    if data.get("perc_aliment") is not None:
        sub(info_deslig, "percAliment", str(data["perc_aliment"]))
    if data.get("vr_alim") is not None:
        sub(info_deslig, "vrAlim", str(data["vr_alim"]))
    if data.get("nr_proc_trab"):
        sub(info_deslig, "nrProcTrab", str(data["nr_proc_trab"]))

    # observacoes (opcional)
    for obs in data.get("observacoes", []):
        observacoes_el = sub(info_deslig, "observacoes")
        sub(observacoes_el, "observacao", str(obs))

    # sucessaoVinc (para motivos de sucessao)
    if data.get("suc_tp_insc") is not None:
        sucessao = sub(info_deslig, "sucessaoVinc")
        sub(sucessao, "tpInsc", str(data["suc_tp_insc"]))
        sub(sucessao, "nrInsc", str(data["suc_nr_insc"]))

    # transfTit (para motivo 34 - transferencia domestico)
    if data.get("cpf_substituto"):
        transf_tit = sub(info_deslig, "transfTit")
        sub(transf_tit, "cpfSubstituto", str(data["cpf_substituto"]))
        sub(transf_tit, "dtNascto", str(data["dt_nascto_substituto"]))

    # mudancaCPF (para motivo 36)
    if data.get("novo_cpf"):
        mudanca_cpf = sub(info_deslig, "mudancaCPF")
        sub(mudanca_cpf, "novoCPF", str(data["novo_cpf"]))

    # verbasResc (lista de demonstrativos de verbas rescisorias)
    verbas_resc_list = data.get("verbas_resc", [])
    if verbas_resc_list:
        verbas_resc = sub(info_deslig, "verbasResc")
        for dm in verbas_resc_list:
            _build_dm_dev(verbas_resc, dm)

    return EventoXml(root, _NAMESPACE)


def _build_dm_dev(parent, dm: dict) -> None:
    """Constroi um grupo dmDev (demonstrativo de valores devidos) para rescisao."""
    dm_dev = sub(parent, "dmDev")
    sub(dm_dev, "ideDmDev", str(dm["ide_dm_dev"]))
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

    for det in estab_lot.get("det_verbas", []):
        _build_det_verbas(ide_estab_lot, det)


def _build_det_verbas(parent, det: dict) -> None:
    """Constroi um grupo detVerbas (itens da rescisao)."""
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
