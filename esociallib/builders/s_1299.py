"""
Builder para S-1299 — Fechamento dos Eventos Periodicos.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1299 sinaliza ao governo que todos os eventos periodicos do
periodo de apuracao ja foram enviados, disparando o processamento.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtFechaEvPer/v_S_01_03_00"


@register_builder("S-1299")
def build_s1299(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1299 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideEvento
            "ind_apuracao": 1,              # 1=Mensal, 2=Anual (13o)
            "per_apur": "2024-03",          # YYYY-MM ou YYYY

            # infoFech
            "evt_remun": "S",               # S ou N - possui eventos de remuneracao?
            "evt_pgtos": "S",               # S ou N - possui eventos de pagamentos?
            "evt_com_prod": "N",            # S ou N - possui comercializacao producao?
            "evt_contrat_av_np": "N",       # S ou N - contratou avulsos nao portuarios?
            "evt_info_compl_per": "N",      # S ou N - possui info complementar?

            # opcionais
            "ind_exc_apur_1250": None,      # "S" para excluir apuracao S-1250 (opcional)
            "trans_dctf_web": None,         # "S" para transmissao imediata DCTFWeb (opcional)
            "nao_valid": None,              # "S" ou "N" - nao validar fechamento (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtFechaEvPer", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_folha_sem_retificacao)
    ide_evento = sub(evt, "ideEvento")
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

    # infoFech
    info_fech = sub(evt, "infoFech")
    sub(info_fech, "evtRemun", str(data["evt_remun"]))
    sub(info_fech, "evtPgtos", str(data["evt_pgtos"]))
    sub(info_fech, "evtComProd", str(data["evt_com_prod"]))
    sub(info_fech, "evtContratAvNP", str(data["evt_contrat_av_np"]))
    sub(info_fech, "evtInfoComplPer", str(data["evt_info_compl_per"]))
    if data.get("ind_exc_apur_1250"):
        sub(info_fech, "indExcApur1250", str(data["ind_exc_apur_1250"]))
    if data.get("trans_dctf_web"):
        sub(info_fech, "transDCTFWeb", str(data["trans_dctf_web"]))
    if data.get("nao_valid"):
        sub(info_fech, "naoValid", str(data["nao_valid"]))

    return EventoXml(root, _NAMESPACE)
