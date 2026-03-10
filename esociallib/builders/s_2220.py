"""
Builder para S-2220 -- Monitoramento da Saude do Trabalhador.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2220 e um evento nao-periodico que registra informacoes relativas
ao monitoramento da saude do trabalhador (exames medicos ocupacionais),
incluindo o ASO (Atestado de Saude Ocupacional).
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtMonit/v_S_01_03_00"


@register_builder("S-2220")
def build_s2220(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2220 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideVinculo (T_ideVinculo_sst)
            "cpf_trab": "12345678901",
            "matricula": "000123",          # Opcional
            "cod_categ": "101",             # Opcional (se TSVE sem matricula)

            # exMedOcup
            "tp_exame_ocup": 0,             # 0=Admissional, 1=Periodico, 2=Retorno,
                                            # 3=Mudanca funcao, 4=Pontual, 9=Demissional

            # aso
            "dt_aso": "2024-03-01",         # Data de emissao do ASO
            "res_aso": 1,                   # 1=Apto, 2=Inapto (opcional)

            # exames (lista de exames complementares - obrigatoria, 1..99)
            "exames": [
                {
                    "dt_exm": "2024-02-28",         # Data do exame
                    "proc_realizado": "0998",       # Codigo do procedimento (Tabela 27)
                    "obs_proc": None,               # Observacao (opcional)
                    "ord_exame": None,              # 1=Inicial, 2=Sequencial (opcional)
                    "ind_result": None,             # 1=Normal, 2=Alterado, 3=Estavel, 4=Agravamento (opcional)
                }
            ],

            # medico (informacoes do medico emitente do ASO)
            "nm_med": "DR JOAO SILVA",      # Nome do medico
            "nr_crm": "123456",             # Nr CRM (opcional)
            "uf_crm": "SP",                 # UF do CRM (opcional)

            # respMonit (opcional - medico responsavel/coordenador PCMSO)
            "cpf_resp": None,               # CPF do medico responsavel (opcional)
            "nm_resp": None,                # Nome do medico responsavel
            "nr_crm_resp": None,            # Nr CRM do responsavel
            "uf_crm_resp": None,            # UF do CRM do responsavel
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtMonit", event_id, _NAMESPACE)

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

    # ideVinculo (T_ideVinculo_sst: cpfTrab, matricula?, codCateg?)
    ide_vinculo = sub(evt, "ideVinculo")
    sub(ide_vinculo, "cpfTrab", str(data["cpf_trab"]))
    if data.get("matricula"):
        sub(ide_vinculo, "matricula", str(data["matricula"]))
    if data.get("cod_categ") is not None and not data.get("matricula"):
        sub(ide_vinculo, "codCateg", str(data["cod_categ"]))

    # exMedOcup
    ex_med_ocup = sub(evt, "exMedOcup")
    sub(ex_med_ocup, "tpExameOcup", str(data["tp_exame_ocup"]))

    # aso
    aso = sub(ex_med_ocup, "aso")
    sub(aso, "dtAso", str(data["dt_aso"]))
    if data.get("res_aso") is not None:
        sub(aso, "resAso", str(data["res_aso"]))

    # exames (lista de avaliacoes clinicas e exames complementares)
    for exame in data.get("exames", []):
        exame_el = sub(aso, "exame")
        sub(exame_el, "dtExm", str(exame["dt_exm"]))
        sub(exame_el, "procRealizado", str(exame["proc_realizado"]))
        if exame.get("obs_proc"):
            sub(exame_el, "obsProc", str(exame["obs_proc"]))
        if exame.get("ord_exame") is not None:
            sub(exame_el, "ordExame", str(exame["ord_exame"]))
        if exame.get("ind_result") is not None:
            sub(exame_el, "indResult", str(exame["ind_result"]))

    # medico (informacoes do medico emitente do ASO)
    medico = sub(aso, "medico")
    sub(medico, "nmMed", str(data["nm_med"]))
    if data.get("nr_crm"):
        sub(medico, "nrCRM", str(data["nr_crm"]))
    if data.get("uf_crm"):
        sub(medico, "ufCRM", str(data["uf_crm"]))

    # respMonit (opcional - medico responsavel/coordenador PCMSO)
    if data.get("nm_resp"):
        resp_monit = sub(ex_med_ocup, "respMonit")
        if data.get("cpf_resp"):
            sub(resp_monit, "cpfResp", str(data["cpf_resp"]))
        sub(resp_monit, "nmResp", str(data["nm_resp"]))
        sub(resp_monit, "nrCRM", str(data["nr_crm_resp"]))
        sub(resp_monit, "ufCRM", str(data["uf_crm_resp"]))

    return EventoXml(root, _NAMESPACE)
