"""
Builder para S-1280 — Informacoes Complementares aos Eventos Periodicos.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1280 e um evento periodico que informa dados complementares
necessarios ao fechamento dos eventos periodicos, como substituicao
patronal (Lei 12.546/2011), atividades concomitantes (Simples Nacional)
e transformacao em sociedade de fins lucrativos (Lei 11.096/2005).
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtInfoComplPer/v_S_01_03_00"


@register_builder("S-1280")
def build_s1280(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1280 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideEvento (T_ideEvento_folha)
            "ind_apuracao": 1,              # 1=Mensal, 2=Anual (13o)
            "per_apur": "2024-03",          # YYYY-MM ou YYYY

            # infoSubstPatr (opcional — Lei 12.546/2011)
            "info_subst_patr": {
                "ind_subst_patr": 1,        # 1=Integral, 2=Parcial
                "perc_red_contrib": "0.00",
            },

            # infoSubstPatrOpPort (opcional, lista — OGMO)
            "info_subst_patr_op_port": [
                {"cod_lotacao": "LOT001"},
            ],

            # infoAtivConcom (opcional — Simples Nacional)
            "info_ativ_concom": {
                "fator_mes": "50.00",
                "fator_13": "50.00",
            },

            # infoPercTransf11096 (opcional — Lei 11.096/2005)
            "info_perc_transf_11096": {
                "perc_transf": "20.00",
            },
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtInfoComplPer", event_id, _NAMESPACE)

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

    # infoSubstPatr (opcional)
    subst_data = data.get("info_subst_patr")
    if subst_data:
        info_subst = sub(evt, "infoSubstPatr")
        sub(info_subst, "indSubstPatr", str(subst_data["ind_subst_patr"]))
        sub(info_subst, "percRedContrib", str(subst_data["perc_red_contrib"]))

    # infoSubstPatrOpPort (opcional, lista)
    for op_port in data.get("info_subst_patr_op_port", []):
        info_op = sub(evt, "infoSubstPatrOpPort")
        sub(info_op, "codLotacao", str(op_port["cod_lotacao"]))

    # infoAtivConcom (opcional)
    ativ_data = data.get("info_ativ_concom")
    if ativ_data:
        info_ativ = sub(evt, "infoAtivConcom")
        sub(info_ativ, "fatorMes", str(ativ_data["fator_mes"]))
        sub(info_ativ, "fator13", str(ativ_data["fator_13"]))

    # infoPercTransf11096 (opcional)
    transf_data = data.get("info_perc_transf_11096")
    if transf_data:
        info_transf = sub(evt, "infoPercTransf11096")
        sub(info_transf, "percTransf", str(transf_data["perc_transf"]))

    return EventoXml(root, _NAMESPACE)
