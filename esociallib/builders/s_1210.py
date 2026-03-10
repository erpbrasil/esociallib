"""
Builder para S-1210 — Pagamentos de Rendimentos do Trabalho.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1210 e um evento periodico que informa os pagamentos efetivamente
realizados ao trabalhador em um periodo de apuracao, referenciando os
demonstrativos de S-1200, S-1202, S-1207, S-2299 ou S-2399.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_03_00"


@register_builder("S-1210")
def build_s1210(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1210 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideEvento (T_ideEvento_folha_mensal)
            "per_apur": "2024-03",          # YYYY-MM

            # ideBenef
            "cpf_benef": "12345678901",

            # infoPgto (lista de pagamentos)
            "info_pgto": [
                {
                    "dt_pgto": "2024-03-05",
                    "tp_pgto": 1,               # 1-5, conforme evento de origem
                    "per_ref": "2024-03",        # periodo referencia
                    "ide_dm_dev": "DEM001",      # id demonstrativo
                    "vr_liq": "4500.00",         # valor liquido
                    # opcionais:
                    "pais_resid_ext": None,
                    "info_pgto_ext": None,
                },
            ],

            # infoIRComplem (opcional, lista)
            "info_ir_complem": [
                {
                    "dt_laudo": "2024-01-01",        # opcional
                    "info_dep": [...],               # opcional
                    "info_ir_cr": [...],             # opcional
                    "plan_saude": {...},             # opcional
                },
            ],
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtPgtos", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_folha_mensal)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
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

    # ideBenef
    ide_benef = sub(evt, "ideBenef")
    sub(ide_benef, "cpfBenef", str(data["cpf_benef"]))

    # infoPgto (lista de pagamentos)
    for pgto in data.get("info_pgto", []):
        _build_info_pgto(ide_benef, pgto)

    # infoIRComplem (opcional, lista)
    for ir in data.get("info_ir_complem", []):
        _build_info_ir_complem(ide_benef, ir)

    return EventoXml(root, _NAMESPACE)


def _build_info_pgto(parent, pgto: dict) -> None:
    """Constroi um grupo infoPgto."""
    info_pgto = sub(parent, "infoPgto")
    sub(info_pgto, "dtPgto", str(pgto["dt_pgto"]))
    sub(info_pgto, "tpPgto", str(pgto["tp_pgto"]))
    sub(info_pgto, "perRef", str(pgto["per_ref"]))
    sub(info_pgto, "ideDmDev", str(pgto["ide_dm_dev"]))
    sub(info_pgto, "vrLiq", str(pgto["vr_liq"]))

    if pgto.get("pais_resid_ext") is not None:
        sub(info_pgto, "paisResidExt", str(pgto["pais_resid_ext"]))

    # infoPgtoExt (opcional)
    pgto_ext = pgto.get("info_pgto_ext")
    if pgto_ext:
        _build_info_pgto_ext(info_pgto, pgto_ext)


def _build_info_pgto_ext(parent, ext: dict) -> None:
    """Constroi o grupo infoPgtoExt."""
    info_pgto_ext = sub(parent, "infoPgtoExt")
    sub(info_pgto_ext, "indNIF", str(ext["ind_nif"]))
    if ext.get("nif_benef"):
        sub(info_pgto_ext, "nifBenef", str(ext["nif_benef"]))
    sub(info_pgto_ext, "frmTribut", str(ext["frm_tribut"]))

    # endExt (opcional)
    end = ext.get("end_ext")
    if end:
        end_ext = sub(info_pgto_ext, "endExt")
        if end.get("end_dsc_lograd"):
            sub(end_ext, "endDscLograd", str(end["end_dsc_lograd"]))
        if end.get("end_nr_lograd"):
            sub(end_ext, "endNrLograd", str(end["end_nr_lograd"]))
        if end.get("end_complem"):
            sub(end_ext, "endComplem", str(end["end_complem"]))
        if end.get("end_bairro"):
            sub(end_ext, "endBairro", str(end["end_bairro"]))
        if end.get("end_cidade"):
            sub(end_ext, "endCidade", str(end["end_cidade"]))
        if end.get("end_estado"):
            sub(end_ext, "endEstado", str(end["end_estado"]))
        if end.get("end_cod_postal"):
            sub(end_ext, "endCodPostal", str(end["end_cod_postal"]))
        if end.get("telef"):
            sub(end_ext, "telef", str(end["telef"]))


def _build_info_ir_complem(parent, ir: dict) -> None:
    """Constroi o grupo infoIRComplem."""
    info_ir = sub(parent, "infoIRComplem")

    if ir.get("dt_laudo"):
        sub(info_ir, "dtLaudo", str(ir["dt_laudo"]))

    # perAnt (opcional)
    per_ant_data = ir.get("per_ant")
    if per_ant_data:
        per_ant = sub(info_ir, "perAnt")
        sub(per_ant, "perRefAjuste", str(per_ant_data["per_ref_ajuste"]))
        sub(per_ant, "nrRec1210Orig", str(per_ant_data["nr_rec_1210_orig"]))

    # infoDep (opcional, lista)
    for dep in ir.get("info_dep", []):
        _build_info_dep(info_ir, dep)

    # infoIRCR (opcional, lista)
    for cr in ir.get("info_ir_cr", []):
        _build_info_ir_cr(info_ir, cr)

    # planSaude (opcional)
    plan_saude_data = ir.get("plan_saude")
    if plan_saude_data:
        _build_plan_saude(info_ir, plan_saude_data)


def _build_info_dep(parent, dep: dict) -> None:
    """Constroi o grupo infoDep."""
    info_dep = sub(parent, "infoDep")
    sub(info_dep, "cpfDep", str(dep["cpf_dep"]))
    sub(info_dep, "dtNascto", str(dep["dt_nascto"]))
    sub(info_dep, "nome", str(dep["nome"]))
    sub(info_dep, "depIRRF", str(dep["dep_irrf"]))
    if dep.get("tp_dep") is not None:
        sub(info_dep, "tpDep", str(dep["tp_dep"]))
    if dep.get("desc_dep"):
        sub(info_dep, "descDep", str(dep["desc_dep"]))


def _build_info_ir_cr(parent, cr: dict) -> None:
    """Constroi o grupo infoIRCR."""
    info_ir_cr = sub(parent, "infoIRCR")
    sub(info_ir_cr, "tpCR", str(cr["tp_cr"]))
    sub(info_ir_cr, "vrCR", str(cr["vr_cr"]))

    # infoProcRet (opcional, lista)
    for proc in cr.get("info_proc_ret", []):
        info_proc = sub(info_ir_cr, "infoProcRet")
        sub(info_proc, "tpProcRet", str(proc["tp_proc_ret"]))
        sub(info_proc, "nrProcRet", str(proc["nr_proc_ret"]))
        sub(info_proc, "codSusp", str(proc["cod_susp"]))
        sub(info_proc, "vrNRetido", str(proc["vr_n_retido"]))

    # penAlim (opcional, lista)
    for pen in cr.get("pen_alim", []):
        pen_alim = sub(info_ir_cr, "penAlim")
        sub(pen_alim, "cpfDep", str(pen["cpf_dep"]))
        sub(pen_alim, "vlrDedPenAlim", str(pen["vlr_ded_pen_alim"]))

    # previdCompl (opcional, lista)
    for prev in cr.get("previd_compl", []):
        previd = sub(info_ir_cr, "previdCompl")
        sub(previd, "tpPrev", str(prev["tp_prev"]))
        if prev.get("cnpj_ent_previd"):
            sub(previd, "cnpjEntPrevid", str(prev["cnpj_ent_previd"]))
        sub(previd, "vlrDedPrevid", str(prev["vlr_ded_previd"]))


def _build_plan_saude(parent, plan: dict) -> None:
    """Constroi o grupo planSaude."""
    plan_saude = sub(parent, "planSaude")
    if plan.get("ind_oper_plan_saude") is not None:
        sub(plan_saude, "indOperPlanSaude", str(plan["ind_oper_plan_saude"]))
    if plan.get("cnpj_oper"):
        sub(plan_saude, "cnpjOper", str(plan["cnpj_oper"]))
    if plan.get("reg_ans"):
        sub(plan_saude, "regANS", str(plan["reg_ans"]))
    sub(plan_saude, "vlrSaudeTit", str(plan["vlr_saude_tit"]))

    for dep in plan.get("info_dep_plan", []):
        info_dep = sub(plan_saude, "infoDep")
        sub(info_dep, "cpfDep", str(dep["cpf_dep"]))
        sub(info_dep, "vlrSaudeDep", str(dep["vlr_saude_dep"]))
