"""
Builder para S-2500 — Processo Trabalhista.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2500 registra informacoes de processos trabalhistas judiciais ou
demandas submetidas a CCP/NINTER, incluindo dados do trabalhador,
contrato e bases de calculo.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_03_00"


@register_builder("S-2500")
def build_s2500(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2500 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # ideResp (opcional - responsabilidade indireta)
            "ide_resp_tp_insc": None,
            "ide_resp_nr_insc": None,

            # infoProcesso
            "origem": 1,                    # 1=Judicial, 2=CCP/NINTER
            "nr_proc_trab": "12345678901234567890",
            "obs_proc_trab": None,          # (opcional)

            # dadosCompl - infoProcJud (se origem=1)
            "dt_sent": "2024-06-01",
            "uf_vara": "SP",
            "cod_munic": "3550308",
            "id_vara": 1,

            # OU dadosCompl - infoCCP (se origem=2)
            "dt_ccp": None,
            "tp_ccp": None,
            "cnpj_ccp": None,

            # ideTrab
            "cpf_trab": "12345678901",
            "nm_trab": "JOAO DA SILVA",    # (opcional se indContr=S)
            "dt_nascto": "1980-01-15",      # (opcional se indContr=S)

            # infoContr (lista)
            "info_contr": [
                {
                    "tp_contr": 1,
                    "ind_contr": "S",
                    "dt_adm_orig": None,
                    "ind_reint": "N",
                    "ind_categ": "N",
                    "ind_nat_ativ": "N",
                    "ind_mot_deslig": "N",
                    "matricula": "000123",  # (opcional)
                    "cod_categ": "101",     # (opcional)
                    "dt_inicio": None,      # (opcional)
                }
            ],
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtProcTrab", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # ideResp (opcional - responsabilidade indireta)
    if data.get("ide_resp_tp_insc") is not None:
        ide_resp = sub(ide_empregador, "ideResp")
        sub(ide_resp, "tpInsc", str(data["ide_resp_tp_insc"]))
        sub(ide_resp, "nrInsc", str(data["ide_resp_nr_insc"]))
        if data.get("dt_adm_resp_dir"):
            sub(ide_resp, "dtAdmRespDir", str(data["dt_adm_resp_dir"]))
        if data.get("mat_resp_dir"):
            sub(ide_resp, "matRespDir", str(data["mat_resp_dir"]))

    # infoProcesso
    info_proc = sub(evt, "infoProcesso")
    sub(info_proc, "origem", str(data["origem"]))
    sub(info_proc, "nrProcTrab", str(data["nr_proc_trab"]))
    if data.get("obs_proc_trab"):
        sub(info_proc, "obsProcTrab", str(data["obs_proc_trab"]))

    # dadosCompl
    dados_compl = sub(info_proc, "dadosCompl")
    if int(data["origem"]) == 1:
        # infoProcJud
        info_proc_jud = sub(dados_compl, "infoProcJud")
        sub(info_proc_jud, "dtSent", str(data["dt_sent"]))
        sub(info_proc_jud, "ufVara", str(data["uf_vara"]))
        sub(info_proc_jud, "codMunic", str(data["cod_munic"]))
        sub(info_proc_jud, "idVara", str(data["id_vara"]))
    else:
        # infoCCP
        info_ccp = sub(dados_compl, "infoCCP")
        sub(info_ccp, "dtCCP", str(data["dt_ccp"]))
        sub(info_ccp, "tpCCP", str(data["tp_ccp"]))
        if data.get("cnpj_ccp"):
            sub(info_ccp, "cnpjCCP", str(data["cnpj_ccp"]))

    # ideTrab
    ide_trab = sub(evt, "ideTrab")
    sub(ide_trab, "cpfTrab", str(data["cpf_trab"]))
    if data.get("nm_trab"):
        sub(ide_trab, "nmTrab", str(data["nm_trab"]))
    if data.get("dt_nascto"):
        sub(ide_trab, "dtNascto", str(data["dt_nascto"]))
    if data.get("ide_seq_trab") is not None:
        sub(ide_trab, "ideSeqTrab", str(data["ide_seq_trab"]))

    # infoContr (lista de contratos)
    for contr in data.get("info_contr", []):
        _build_info_contr(ide_trab, contr)

    return EventoXml(root, _NAMESPACE)


def _build_info_contr(parent, contr: dict) -> None:
    """Constroi um grupo infoContr."""
    info_contr = sub(parent, "infoContr")
    sub(info_contr, "tpContr", str(contr["tp_contr"]))
    sub(info_contr, "indContr", str(contr["ind_contr"]))
    if contr.get("dt_adm_orig"):
        sub(info_contr, "dtAdmOrig", str(contr["dt_adm_orig"]))
    if contr.get("ind_reint"):
        sub(info_contr, "indReint", str(contr["ind_reint"]))
    sub(info_contr, "indCateg", str(contr.get("ind_categ", "N")))
    sub(info_contr, "indNatAtiv", str(contr.get("ind_nat_ativ", "N")))
    sub(info_contr, "indMotDeslig", str(contr.get("ind_mot_deslig", "N")))
    if contr.get("matricula"):
        sub(info_contr, "matricula", str(contr["matricula"]))
    if contr.get("cod_categ"):
        sub(info_contr, "codCateg", str(contr["cod_categ"]))
    if contr.get("dt_inicio"):
        sub(info_contr, "dtInicio", str(contr["dt_inicio"]))
