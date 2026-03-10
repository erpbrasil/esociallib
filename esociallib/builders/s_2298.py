"""
Builder para S-2298 -- Reintegracao/Outros Provimentos.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2298 e um evento nao-periodico que registra a reintegracao de
trabalhador previamente desligado, podendo ocorrer por decisao judicial,
anistia legal, reversao, reconducao, reinclusao ou outros motivos.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtReintegr/v_S_01_03_00"


@register_builder("S-2298")
def build_s2298(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2298 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideVinculo (T_ideVinculo)
            "cpf_trab": "12345678901",
            "matricula": "000123",

            # infoReintegr
            "tp_reint": 1,                  # 1=Judicial, 2=Anistia, 3=Reversao,
                                            # 4=Reconducao, 5=Reinclusao,
                                            # 6=Revisao reforma, 9=Outros
            "nr_proc_jud": None,            # Nr processo judicial (se tp_reint=1)
            "nr_lei_anistia": None,         # Nr lei anistia (se tp_reint=2)
            "dt_efet_retorno": "2024-07-01", # Data efetivo retorno ao trabalho
            "dt_efeito": "2024-06-15",      # Data inicio efeitos financeiros
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtReintegr", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab: indRetif, nrRecibo, tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # ideVinculo (T_ideVinculo: cpfTrab + matricula)
    ide_vinculo = sub(evt, "ideVinculo")
    sub(ide_vinculo, "cpfTrab", str(data["cpf_trab"]))
    sub(ide_vinculo, "matricula", str(data["matricula"]))

    # infoReintegr
    info_reintegr = sub(evt, "infoReintegr")
    sub(info_reintegr, "tpReint", str(data["tp_reint"]))
    if data.get("nr_proc_jud"):
        sub(info_reintegr, "nrProcJud", str(data["nr_proc_jud"]))
    if data.get("nr_lei_anistia"):
        sub(info_reintegr, "nrLeiAnistia", str(data["nr_lei_anistia"]))
    sub(info_reintegr, "dtEfetRetorno", str(data["dt_efet_retorno"]))
    sub(info_reintegr, "dtEfeito", str(data["dt_efeito"]))

    return EventoXml(root, _NAMESPACE)
