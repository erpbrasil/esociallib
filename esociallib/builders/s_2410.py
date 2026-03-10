"""
Builder para S-2410 — Cadastro de Beneficio - Entes Publicos - Inicio.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2410 registra o inicio de um beneficio previdenciario de regime
proprio (RPPS) em entes publicos: aposentadoria, pensao por morte, etc.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtCdBenIn/v_S_01_03_00"


@register_builder("S-2410")
def build_s2410(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2410 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # beneficiario
            "cpf_benef": "12345678901",
            "matricula": "000123",          # (opcional)
            "cnpj_origem": None,            # (opcional)

            # infoBenInicio
            "cad_ini": "N",
            "ind_sit_benef": 1,             # (opcional)
            "nr_beneficio": "BEN001",
            "dt_ini_beneficio": "2024-01-01",
            "dt_public": None,              # (opcional)

            # dadosBeneficio
            "tp_beneficio": "0101",
            "tp_plan_rp": 1,
            "dsc": None,                    # (opcional)
            "ind_dec_jud": "N",             # (opcional)

            # infoPenMorte (opcional - grupo 06 Tab 25)
            "tp_pen_morte": None,
            "cpf_inst": None,
            "dt_inst": None,
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtCdBenIn", event_id, _NAMESPACE)

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

    # beneficiario
    beneficiario = sub(evt, "beneficiario")
    sub(beneficiario, "cpfBenef", str(data["cpf_benef"]))
    if data.get("matricula"):
        sub(beneficiario, "matricula", str(data["matricula"]))
    if data.get("cnpj_origem"):
        sub(beneficiario, "cnpjOrigem", str(data["cnpj_origem"]))

    # infoBenInicio
    info_ben = sub(evt, "infoBenInicio")
    sub(info_ben, "cadIni", str(data.get("cad_ini", "N")))
    if data.get("ind_sit_benef") is not None:
        sub(info_ben, "indSitBenef", str(data["ind_sit_benef"]))
    sub(info_ben, "nrBeneficio", str(data["nr_beneficio"]))
    sub(info_ben, "dtIniBeneficio", str(data["dt_ini_beneficio"]))
    if data.get("dt_public"):
        sub(info_ben, "dtPublic", str(data["dt_public"]))

    # dadosBeneficio
    dados_ben = sub(info_ben, "dadosBeneficio")
    sub(dados_ben, "tpBeneficio", str(data["tp_beneficio"]))
    sub(dados_ben, "tpPlanRP", str(data["tp_plan_rp"]))
    if data.get("dsc"):
        sub(dados_ben, "dsc", str(data["dsc"]))
    if data.get("ind_dec_jud"):
        sub(dados_ben, "indDecJud", str(data["ind_dec_jud"]))

    # infoPenMorte (opcional)
    if data.get("tp_pen_morte") is not None:
        info_pen = sub(dados_ben, "infoPenMorte")
        sub(info_pen, "tpPenMorte", str(data["tp_pen_morte"]))
        if data.get("cpf_inst"):
            inst = sub(info_pen, "instPenMorte")
            sub(inst, "cpfInst", str(data["cpf_inst"]))
            sub(inst, "dtInst", str(data["dt_inst"]))
            if data.get("tp_dep_inst") is not None:
                sub(inst, "tpDepInst", str(data["tp_dep_inst"]))
            if data.get("descr_dep_inst"):
                sub(inst, "descrDepInst", str(data["descr_dep_inst"]))

    # infoHomolog (opcional)
    if data.get("sit_homolog") is not None:
        info_homolog = sub(dados_ben, "infoHomolog")
        sub(info_homolog, "sitHomolog", str(data["sit_homolog"]))
        if data.get("dt_homolog"):
            sub(info_homolog, "dtHomolog", str(data["dt_homolog"]))

    # sucessaoBenef (opcional - indSitBenef=2)
    if data.get("cnpj_orgao_ant"):
        sucessao = sub(info_ben, "sucessaoBenef")
        sub(sucessao, "cnpjOrgaoAnt", str(data["cnpj_orgao_ant"]))
        sub(sucessao, "nrBeneficioAnt", str(data["nr_beneficio_ant"]))
        sub(sucessao, "dtTransf", str(data["dt_transf"]))
        if data.get("observacao_suc"):
            sub(sucessao, "observacao", str(data["observacao_suc"]))

    # mudancaCPF (opcional - indSitBenef=3)
    if data.get("cpf_ant"):
        mudanca = sub(info_ben, "mudancaCPF")
        sub(mudanca, "cpfAnt", str(data["cpf_ant"]))
        sub(mudanca, "nrBeneficioAnt", str(data["nr_beneficio_ant_cpf"]))
        sub(mudanca, "dtAltCPF", str(data["dt_alt_cpf"]))
        if data.get("observacao_cpf"):
            sub(mudanca, "observacao", str(data["observacao_cpf"]))

    # infoBenTermino (opcional - cadIni=S ou indSitBenef=2)
    if data.get("dt_term_beneficio"):
        info_term = sub(info_ben, "infoBenTermino")
        sub(info_term, "dtTermBeneficio", str(data["dt_term_beneficio"]))
        sub(info_term, "mtvTermino", str(data["mtv_termino"]))

    return EventoXml(root, _NAMESPACE)
