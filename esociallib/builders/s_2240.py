"""
Builder para S-2240 -- Condicoes Ambientais do Trabalho - Agentes Nocivos.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2240 e um evento nao-periodico que registra as condicoes ambientais
de trabalho do trabalhador, indicando os agentes nocivos aos quais ele
esta exposto, informacoes sobre o ambiente de trabalho e EPCs/EPIs.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtExpRisco/v_S_01_03_00"


@register_builder("S-2240")
def build_s2240(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2240 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideVinculo (T_ideVinculo_sst)
            "cpf_trab": "12345678901",
            "matricula": "000123",          # Opcional
            "cod_categ": "101",             # Opcional (se TSVE sem matricula)

            # infoExpRisco
            "dt_ini_condicao": "2024-01-01",  # Data inicio das condicoes
            "dt_fim_condicao": None,          # Data fim das condicoes (opcional)

            # infoAmb (lista 1..9 - ambientes de trabalho)
            "info_amb": [
                {
                    "local_amb": 1,                 # 1=Proprio empregador, 2=Terceiros
                    "dsc_setor": "PRODUCAO",        # Descricao do setor
                    "tp_insc": 1,                   # 1=CNPJ, 3=CAEPF, 4=CNO
                    "nr_insc": "12345678000199",    # Nr inscricao
                }
            ],

            # infoAtiv
            "dsc_ativ_des": "Operar maquina de envase de produtos quimicos",

            # agNoc (lista 1..999 - agentes nocivos)
            "ag_noc": [
                {
                    "cod_ag_noc": "02.01.014",      # Codigo agente nocivo (Tabela 24)
                    "dsc_ag_noc": None,             # Descricao (opcional)
                    "tp_aval": 1,                   # 1=Quantitativo, 2=Qualitativo (opcional)
                    "int_conc": "85.5000",          # Intensidade/concentracao (opcional)
                    "lim_tol": "85.0000",           # Limite de tolerancia (opcional)
                    "un_med": 4,                    # Unidade de medida (opcional)
                    "tec_medicao": "NHO-01",        # Tecnica de medicao (opcional)
                    "nr_proc_jud": None,            # Nr processo judicial (opcional)

                    # epcEpi (opcional)
                    "utiliz_epc": 2,                # 0=N/A, 1=Nao implementa, 2=Implementa
                    "efic_epc": "S",                # S ou N (se utiliz_epc=2)
                    "utiliz_epi": 2,                # 0=N/A, 1=Nao utilizado, 2=Utilizado
                    "efic_epi": "S",                # S ou N (se utiliz_epi=2)

                    # epi (lista opcional, se utiliz_epi=2)
                    "epi": [
                        {"doc_aval": "CA 12345"},
                    ],

                    # epiCompl (opcional, se utiliz_epi=2)
                    "med_protecao": "S",
                    "cond_functo": "S",
                    "uso_inint": "S",
                    "prz_valid": "S",
                    "periodic_troca": "S",
                    "higienizacao": "S",
                }
            ],

            # respReg (lista 1..99 - responsaveis pelos registros ambientais)
            "resp_reg": [
                {
                    "cpf_resp": "12345678901",      # CPF do responsavel
                    "ide_oc": 4,                    # 1=CRM, 4=CREA, 9=Outros (opcional)
                    "dsc_oc": None,                 # Descricao OC (se ide_oc=9) (opcional)
                    "nr_oc": "123456",              # Nr inscricao OC (opcional)
                    "uf_oc": "SP",                  # UF do OC (opcional)
                }
            ],

            # obs (opcional)
            "obs_compl": None,              # Observacao complementar
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtExpRisco", event_id, _NAMESPACE)

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

    # infoExpRisco
    info_exp_risco = sub(evt, "infoExpRisco")
    sub(info_exp_risco, "dtIniCondicao", str(data["dt_ini_condicao"]))
    if data.get("dt_fim_condicao"):
        sub(info_exp_risco, "dtFimCondicao", str(data["dt_fim_condicao"]))

    # infoAmb (lista 1..9 - ambientes de trabalho)
    for amb in data.get("info_amb", []):
        info_amb = sub(info_exp_risco, "infoAmb")
        sub(info_amb, "localAmb", str(amb["local_amb"]))
        sub(info_amb, "dscSetor", str(amb["dsc_setor"]))
        sub(info_amb, "tpInsc", str(amb["tp_insc"]))
        sub(info_amb, "nrInsc", str(amb["nr_insc"]))

    # infoAtiv
    info_ativ = sub(info_exp_risco, "infoAtiv")
    sub(info_ativ, "dscAtivDes", str(data["dsc_ativ_des"]))

    # agNoc (lista 1..999 - agentes nocivos)
    for ag in data.get("ag_noc", []):
        _build_ag_noc(info_exp_risco, ag)

    # respReg (lista 1..99 - responsaveis)
    for resp in data.get("resp_reg", []):
        resp_reg = sub(info_exp_risco, "respReg")
        sub(resp_reg, "cpfResp", str(resp["cpf_resp"]))
        if resp.get("ide_oc") is not None:
            sub(resp_reg, "ideOC", str(resp["ide_oc"]))
        if resp.get("dsc_oc"):
            sub(resp_reg, "dscOC", str(resp["dsc_oc"]))
        if resp.get("nr_oc"):
            sub(resp_reg, "nrOC", str(resp["nr_oc"]))
        if resp.get("uf_oc"):
            sub(resp_reg, "ufOC", str(resp["uf_oc"]))

    # obs (opcional)
    if data.get("obs_compl"):
        obs = sub(info_exp_risco, "obs")
        sub(obs, "obsCompl", str(data["obs_compl"]))

    return EventoXml(root, _NAMESPACE)


def _build_ag_noc(parent, ag: dict) -> None:
    """Constroi um grupo agNoc (agente nocivo)."""
    ag_noc = sub(parent, "agNoc")
    sub(ag_noc, "codAgNoc", str(ag["cod_ag_noc"]))
    if ag.get("dsc_ag_noc"):
        sub(ag_noc, "dscAgNoc", str(ag["dsc_ag_noc"]))
    if ag.get("tp_aval") is not None:
        sub(ag_noc, "tpAval", str(ag["tp_aval"]))
    if ag.get("int_conc") is not None:
        sub(ag_noc, "intConc", str(ag["int_conc"]))
    if ag.get("lim_tol") is not None:
        sub(ag_noc, "limTol", str(ag["lim_tol"]))
    if ag.get("un_med") is not None:
        sub(ag_noc, "unMed", str(ag["un_med"]))
    if ag.get("tec_medicao"):
        sub(ag_noc, "tecMedicao", str(ag["tec_medicao"]))
    if ag.get("nr_proc_jud"):
        sub(ag_noc, "nrProcJud", str(ag["nr_proc_jud"]))

    # epcEpi (opcional)
    if ag.get("utiliz_epc") is not None:
        epc_epi = sub(ag_noc, "epcEpi")
        sub(epc_epi, "utilizEPC", str(ag["utiliz_epc"]))
        if ag.get("efic_epc") is not None:
            sub(epc_epi, "eficEpc", str(ag["efic_epc"]))
        sub(epc_epi, "utilizEPI", str(ag["utiliz_epi"]))
        if ag.get("efic_epi") is not None:
            sub(epc_epi, "eficEpi", str(ag["efic_epi"]))

        # epi (lista opcional)
        for epi_item in ag.get("epi", []):
            epi_el = sub(epc_epi, "epi")
            sub(epi_el, "docAval", str(epi_item["doc_aval"]))

        # epiCompl (opcional)
        if ag.get("med_protecao") is not None:
            epi_compl = sub(epc_epi, "epiCompl")
            sub(epi_compl, "medProtecao", str(ag["med_protecao"]))
            sub(epi_compl, "condFuncto", str(ag["cond_functo"]))
            sub(epi_compl, "usoInint", str(ag["uso_inint"]))
            sub(epi_compl, "przValid", str(ag["prz_valid"]))
            sub(epi_compl, "periodicTroca", str(ag["periodic_troca"]))
            sub(epi_compl, "higienizacao", str(ag["higienizacao"]))
