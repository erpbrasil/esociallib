"""
Builder para S-2420 — Cessao/Exercicio em Outro Orgao.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2420 (evtCessao) registra o inicio ou termino de cessao/exercicio
em outro orgao de servidor publico cedente.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtCessao/v_S_01_03_00"


@register_builder("S-2420")
def build_s2420(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2420 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # ideVinculo
            "cpf_trab": "12345678901",
            "matricula": "000123",

            # infoCessao - iniCessao (se inicio)
            "dt_ini_cessao": "2024-03-01",      # (preencher OU dt_term_cessao)
            "cnpj_cess": "98765432000199",
            "resp_remun": "S",

            # infoCessao - fimCessao (se termino)
            "dt_term_cessao": None,              # (preencher OU dt_ini_cessao)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtCessao", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab_PJ)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador_cnpj)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # ideVinculo (T_ideVinculo)
    ide_vinculo = sub(evt, "ideVinculo")
    sub(ide_vinculo, "cpfTrab", str(data["cpf_trab"]))
    sub(ide_vinculo, "matricula", str(data["matricula"]))

    # infoCessao
    info_cessao = sub(evt, "infoCessao")

    if data.get("dt_ini_cessao"):
        # iniCessao
        ini_cessao = sub(info_cessao, "iniCessao")
        sub(ini_cessao, "dtIniCessao", str(data["dt_ini_cessao"]))
        sub(ini_cessao, "cnpjCess", str(data["cnpj_cess"]))
        sub(ini_cessao, "respRemun", str(data.get("resp_remun", "S")))
    else:
        # fimCessao
        fim_cessao = sub(info_cessao, "fimCessao")
        sub(fim_cessao, "dtTermCessao", str(data["dt_term_cessao"]))

    return EventoXml(root, _NAMESPACE)
