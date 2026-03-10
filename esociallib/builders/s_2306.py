"""
Builder para S-2306 — Trabalhador Sem Vinculo - Alteracao Contratual.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2306 registra alteracoes contratuais de trabalhadores sem vinculo
empregaticio (TSVE): cargo, funcao, remuneracao, etc.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtTSVAltContr/v_S_01_03_00"


@register_builder("S-2306")
def build_s2306(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2306 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # ideTrabSemVinculo
            "cpf_trab": "12345678901",
            "matricula": "000123",          # (opcional)
            "cod_categ": "901",             # (opcional)

            # infoTSVAlteracao
            "dt_alteracao": "2024-06-01",
            "nat_atividade": 1,             # (opcional)

            # infoComplementares (opcional)
            "nm_cargo": "ESTAGIARIO",       # (opcional)
            "cod_cbo": "252105",            # (opcional)
            "vr_sal_fx": "2000.00",         # (opcional)
            "und_sal_fixo": 5,              # (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtTSVAltContr", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab)
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

    # ideTrabSemVinculo (T_ideTrabSemVinculo)
    ide_trab = sub(evt, "ideTrabSemVinculo")
    sub(ide_trab, "cpfTrab", str(data["cpf_trab"]))
    if data.get("matricula"):
        sub(ide_trab, "matricula", str(data["matricula"]))
    if data.get("cod_categ"):
        sub(ide_trab, "codCateg", str(data["cod_categ"]))

    # infoTSVAlteracao
    info_alt = sub(evt, "infoTSVAlteracao")
    sub(info_alt, "dtAlteracao", str(data["dt_alteracao"]))
    if data.get("nat_atividade") is not None:
        sub(info_alt, "natAtividade", str(data["nat_atividade"]))

    # infoComplementares (opcional)
    has_complementares = (
        data.get("nm_cargo")
        or data.get("cod_cbo")
        or data.get("vr_sal_fx") is not None
        or data.get("tp_reg_prev_dir_sind") is not None
        or data.get("tp_reg_prev_cedido") is not None
        or data.get("ind_remun_cargo_mand") is not None
        or data.get("nat_estagio")
        or data.get("tp_insc_local") is not None
    )
    if has_complementares:
        info_compl = sub(info_alt, "infoComplementares")

        # cargoFuncao (opcional)
        if data.get("nm_cargo") or data.get("cod_cbo"):
            cargo_funcao = sub(info_compl, "cargoFuncao")
            if data.get("nm_cargo"):
                sub(cargo_funcao, "nmCargo", str(data["nm_cargo"]))
            if data.get("cod_cbo"):
                sub(cargo_funcao, "CBOCargo", str(data["cod_cbo"]))
            if data.get("nm_funcao"):
                sub(cargo_funcao, "nmFuncao", str(data["nm_funcao"]))
            if data.get("cbo_funcao"):
                sub(cargo_funcao, "CBOFuncao", str(data["cbo_funcao"]))

        # remuneracao (opcional)
        if data.get("vr_sal_fx") is not None:
            remuneracao = sub(info_compl, "remuneracao")
            sub(remuneracao, "vrSalFx", str(data["vr_sal_fx"]))
            sub(remuneracao, "undSalFixo", str(data["und_sal_fixo"]))
            if data.get("dsc_sal_var"):
                sub(remuneracao, "dscSalVar", str(data["dsc_sal_var"]))

        # infoDirigenteSindical (opcional - categ 401)
        if data.get("tp_reg_prev_dir_sind") is not None:
            dir_sind = sub(info_compl, "infoDirigenteSindical")
            sub(dir_sind, "tpRegPrev", str(data["tp_reg_prev_dir_sind"]))

        # infoTrabCedido (opcional - categ 410)
        if data.get("tp_reg_prev_cedido") is not None:
            trab_cedido = sub(info_compl, "infoTrabCedido")
            sub(trab_cedido, "tpRegPrev", str(data["tp_reg_prev_cedido"]))

        # infoMandElet (opcional - categ 304)
        if data.get("ind_remun_cargo_mand") is not None or data.get(
            "tp_reg_prev_mand"
        ):
            mand_elet = sub(info_compl, "infoMandElet")
            if data.get("ind_remun_cargo_mand") is not None:
                sub(mand_elet, "indRemunCargo", str(data["ind_remun_cargo_mand"]))
            sub(mand_elet, "tpRegPrev", str(data["tp_reg_prev_mand"]))

        # infoEstagiario (opcional - categ 901, 906)
        if data.get("nat_estagio"):
            estagiario = sub(info_compl, "infoEstagiario")
            sub(estagiario, "natEstagio", str(data["nat_estagio"]))
            sub(estagiario, "nivEstagio", str(data["niv_estagio"]))
            if data.get("area_atuacao"):
                sub(estagiario, "areaAtuacao", str(data["area_atuacao"]))
            if data.get("nr_apol"):
                sub(estagiario, "nrApol", str(data["nr_apol"]))
            if data.get("dt_prev_term"):
                sub(estagiario, "dtPrevTerm", str(data["dt_prev_term"]))

        # localTrabGeral (opcional)
        if data.get("tp_insc_local") is not None:
            local_trab = sub(info_compl, "localTrabGeral")
            sub(local_trab, "tpInsc", str(data["tp_insc_local"]))
            sub(local_trab, "nrInsc", str(data["nr_insc_local"]))
            if data.get("desc_comp"):
                sub(local_trab, "descComp", str(data["desc_comp"]))

    return EventoXml(root, _NAMESPACE)
