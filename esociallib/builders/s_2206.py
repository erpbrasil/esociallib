"""
Builder para S-2206 — Alteracao de Contrato de Trabalho/Relacao Estatutaria.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2206 e um evento nao-periodico que registra alteracoes contratuais
como mudanca de cargo, salario, jornada, lotacao, etc.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtAltContratual/v_S_01_03_00"


@register_builder("S-2206")
def build_s2206(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2206 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideVinculo
            "cpf_trab": "12345678901",
            "matricula": "000123",

            # altContratual
            "dt_alteracao": "2024-06-01",   # YYYY-MM-DD
            "dt_ef": "2024-06-01",          # Data dos efeitos remuneratorios (opcional)
            "dsc_alt": "",                  # Descricao da alteracao (opcional)

            # vinculo
            "tp_reg_prev": 1,               # 1=RGPS, 2=RPPS, 3=Nao segurado

            # infoRegimeTrab.infoCeletista (se CLT)
            "tp_reg_trab": 1,               # 1=CLT, 2=Estatutario
            "tp_reg_jor": 1,                # Tipo de regime de jornada
            "nat_atividade": 1,             # 1=Normal, 2=Aprendiz
            "cnpj_sind_categ_prof": "12345678000199",

            # infoContrato
            "cod_categ": "101",
            "cod_cbo": "252105",            # CBO (opcional)
            "nm_cargo": "Analista",         # Nome do cargo (opcional)

            # remuneracao (opcional, obrigatorio para CLT)
            "vr_sal_fx": "6000.00",
            "und_sal_fixo": 5,              # 5=Mensal

            # duracao (opcional, obrigatorio para CLT)
            "tp_contr": 1,                  # 1=Indeterminado, 2=Determinado
            "dt_term": "2025-06-01",        # Data termino (se determinado)

            # localTrabalho
            "tp_insc_local": 1,             # Tipo insc. local de trabalho
            "nr_insc_local": "12345678000199",

            # horContratual (opcional)
            "qtd_hrs_sem": "44.00",
            "tp_jornada": 2,
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtAltContratual", event_id, _NAMESPACE)

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

    # ideVinculo (T_ideVinculo)
    ide_vinculo = sub(evt, "ideVinculo")
    sub(ide_vinculo, "cpfTrab", str(data["cpf_trab"]))
    sub(ide_vinculo, "matricula", str(data["matricula"]))

    # altContratual
    alt_contratual = sub(evt, "altContratual")
    sub(alt_contratual, "dtAlteracao", str(data["dt_alteracao"]))
    if data.get("dt_ef"):
        sub(alt_contratual, "dtEf", str(data["dt_ef"]))
    if data.get("dsc_alt"):
        sub(alt_contratual, "dscAlt", str(data["dsc_alt"]))

    # altContratual.vinculo
    vinculo = sub(alt_contratual, "vinculo")
    sub(vinculo, "tpRegPrev", str(data["tp_reg_prev"]))

    # infoRegimeTrab
    tp_reg_trab = int(data.get("tp_reg_trab", 1))

    if tp_reg_trab == 1:
        # CLT - infoRegimeTrab.infoCeletista
        info_regime = sub(vinculo, "infoRegimeTrab")
        celetista = sub(info_regime, "infoCeletista")
        sub(celetista, "tpRegJor", str(data.get("tp_reg_jor", 1)))
        sub(celetista, "natAtividade", str(data["nat_atividade"]))
        if data.get("dt_base") is not None:
            sub(celetista, "dtBase", str(data["dt_base"]))
        sub(celetista, "cnpjSindCategProf", str(data["cnpj_sind_categ_prof"]))
    elif tp_reg_trab == 2 and int(data["tp_reg_prev"]) == 2:
        # Estatutario - infoRegimeTrab.infoEstatutario
        info_regime = sub(vinculo, "infoRegimeTrab")
        estatutario = sub(info_regime, "infoEstatutario")
        sub(estatutario, "tpPlanRP", str(data["tp_plan_rp"]))
        sub(estatutario, "indTetoRGPS", str(data["ind_teto_rgps"]))
        sub(estatutario, "indAbonoPerm", str(data["ind_abono_perm"]))

    # infoContrato
    info_contrato = sub(vinculo, "infoContrato")
    if data.get("nm_cargo"):
        sub(info_contrato, "nmCargo", str(data["nm_cargo"]))
    if data.get("cod_cbo"):
        sub(info_contrato, "CBOCargo", str(data["cod_cbo"]))
    if data.get("nm_funcao"):
        sub(info_contrato, "nmFuncao", str(data["nm_funcao"]))
    if data.get("cbo_funcao"):
        sub(info_contrato, "CBOFuncao", str(data["cbo_funcao"]))
    if data.get("acum_cargo"):
        sub(info_contrato, "acumCargo", str(data["acum_cargo"]))
    sub(info_contrato, "codCateg", str(data["cod_categ"]))

    # infoContrato.remuneracao (obrigatorio para CLT)
    if data.get("vr_sal_fx") is not None:
        remuneracao = sub(info_contrato, "remuneracao")
        sub(remuneracao, "vrSalFx", str(data["vr_sal_fx"]))
        sub(remuneracao, "undSalFixo", str(data["und_sal_fixo"]))
        if data.get("dsc_sal_var"):
            sub(remuneracao, "dscSalVar", str(data["dsc_sal_var"]))

    # infoContrato.duracao (obrigatorio para CLT)
    if data.get("tp_contr") is not None:
        duracao = sub(info_contrato, "duracao")
        sub(duracao, "tpContr", str(data["tp_contr"]))
        if data.get("dt_term"):
            sub(duracao, "dtTerm", str(data["dt_term"]))
        if data.get("obj_det"):
            sub(duracao, "objDet", str(data["obj_det"]))

    # infoContrato.localTrabalho
    local_trabalho = sub(info_contrato, "localTrabalho")
    if data.get("tp_insc_local") is not None:
        local_trab_geral = sub(local_trabalho, "localTrabGeral")
        sub(local_trab_geral, "tpInsc", str(data["tp_insc_local"]))
        sub(local_trab_geral, "nrInsc", str(data["nr_insc_local"]))
        if data.get("desc_comp"):
            sub(local_trab_geral, "descComp", str(data["desc_comp"]))

    # infoContrato.horContratual (opcional)
    if data.get("qtd_hrs_sem") is not None:
        hor_contratual = sub(info_contrato, "horContratual")
        sub(hor_contratual, "qtdHrsSem", str(data["qtd_hrs_sem"]))
        sub(hor_contratual, "tpJornada", str(data["tp_jornada"]))

    return EventoXml(root, _NAMESPACE)
