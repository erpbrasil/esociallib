"""
Builder para S-2221 -- Exame Toxicologico do Motorista Profissional Empregado.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2221 e um evento nao-periodico que registra informacoes do exame
toxicologico do motorista profissional empregado, conforme exigido
pela legislacao trabalhista.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtToxic/v_S_01_03_00"


@register_builder("S-2221")
def build_s2221(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2221 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideVinculo
            "cpf_trab": "12345678901",
            "matricula": "000123",

            # toxicologico
            "dt_exame": "2024-03-01",       # Data do exame toxicologico
            "cnpj_lab": "12345678000199",   # CNPJ do laboratorio
            "cod_seq_exame": "AB123456789", # Codigo do exame (2 letras + 9 digitos)
            "nm_med": "DR JOAO SILVA",      # Nome do medico
            "nr_crm": "123456",             # Nr CRM (opcional)
            "uf_crm": "SP",                 # UF do CRM (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtToxic", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab_PJ_sem_simplificado: indRetif, nrRecibo, tpAmb, procEmi, verProc)
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

    # ideVinculo (cpfTrab + matricula obrigatoria)
    ide_vinculo = sub(evt, "ideVinculo")
    sub(ide_vinculo, "cpfTrab", str(data["cpf_trab"]))
    sub(ide_vinculo, "matricula", str(data["matricula"]))

    # toxicologico
    toxicologico = sub(evt, "toxicologico")
    sub(toxicologico, "dtExame", str(data["dt_exame"]))
    sub(toxicologico, "cnpjLab", str(data["cnpj_lab"]))
    sub(toxicologico, "codSeqExame", str(data["cod_seq_exame"]))
    sub(toxicologico, "nmMed", str(data["nm_med"]))
    if data.get("nr_crm"):
        sub(toxicologico, "nrCRM", str(data["nr_crm"]))
    if data.get("uf_crm"):
        sub(toxicologico, "ufCRM", str(data["uf_crm"]))

    return EventoXml(root, _NAMESPACE)
