"""
Builder para S-2300 — Trabalhador Sem Vinculo de Emprego/Estatutario - Inicio.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2300 registra o inicio de prestacao de servicos por trabalhadores
sem vinculo empregaticio (TSVE): diretores, estagiarios, cooperados,
dirigentes sindicais, avulsos, servidores cedidos, entre outros.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtTSVInicio/v_S_01_03_00"


@register_builder("S-2300")
def build_s2300(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2300 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # trabalhador
            "cpf_trab": "12345678901",
            "nm_trab": "JOAO DA SILVA",
            "sexo": "M",
            "raca_cor": 1,
            "grau_instr": "07",
            "dt_nascto": "1980-01-15",
            "pais_nascto": "105",
            "pais_nac": "105",

            # infoTSVInicio
            "cad_ini": "N",                # S ou N
            "cod_categ": "901",             # Tabela 01
            "dt_inicio": "2024-03-01",      # Data de inicio

            # infoComplementares (opcional)
            "nm_cargo": "ESTAGIARIO",       # (opcional)
            "cod_cbo": "252105",            # (opcional)
            "vr_sal_fx": "1500.00",         # (opcional)
            "und_sal_fixo": 5,              # (opcional)
            "nat_atividade": 1,             # (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtTSVInicio", event_id, _NAMESPACE)

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

    # trabalhador
    trabalhador = sub(evt, "trabalhador")
    sub(trabalhador, "cpfTrab", str(data["cpf_trab"]))
    sub(trabalhador, "nmTrab", str(data["nm_trab"]))
    sub(trabalhador, "sexo", str(data["sexo"]))
    sub(trabalhador, "racaCor", str(data["raca_cor"]))
    if data.get("est_civ") is not None:
        sub(trabalhador, "estCiv", str(data["est_civ"]))
    sub(trabalhador, "grauInstr", str(data["grau_instr"]))
    if data.get("nm_soc"):
        sub(trabalhador, "nmSoc", str(data["nm_soc"]))

    # trabalhador.nascimento
    nascimento = sub(trabalhador, "nascimento")
    sub(nascimento, "dtNascto", str(data["dt_nascto"]))
    if data.get("cod_munic"):
        sub(nascimento, "codMunic", str(data["cod_munic"]))
    if data.get("uf"):
        sub(nascimento, "uf", str(data["uf"]))
    sub(nascimento, "paisNascto", str(data.get("pais_nascto", "105")))
    sub(nascimento, "paisNac", str(data.get("pais_nac", "105")))

    # trabalhador.endereco (opcional)
    if data.get("tipo_logradouro") or data.get("dsc_lograd"):
        endereco = sub(trabalhador, "endereco")
        brasil = sub(endereco, "brasil")
        sub(brasil, "tpLograd", str(data.get("tipo_logradouro", "R")))
        sub(brasil, "dscLograd", str(data["dsc_lograd"]))
        sub(brasil, "nrLograd", str(data.get("nr_lograd", "S/N")))
        if data.get("complemento"):
            sub(brasil, "complemento", str(data["complemento"]))
        if data.get("bairro"):
            sub(brasil, "bairro", str(data["bairro"]))
        sub(brasil, "cep", str(data["cep"]))
        sub(brasil, "codMunic", str(data["cod_munic_end"]))
        sub(brasil, "uf", str(data["uf_end"]))

    # trabalhador.contato (opcional)
    if data.get("fone_principal") or data.get("email_principal"):
        contato = sub(trabalhador, "contato")
        if data.get("fone_principal"):
            sub(contato, "fonePrinc", str(data["fone_principal"]))
        if data.get("email_principal"):
            sub(contato, "emailPrinc", str(data["email_principal"]))

    # infoTSVInicio
    info_tsv = sub(evt, "infoTSVInicio")
    sub(info_tsv, "cadIni", str(data.get("cad_ini", "N")))
    if data.get("matricula"):
        sub(info_tsv, "matricula", str(data["matricula"]))
    sub(info_tsv, "codCateg", str(data["cod_categ"]))
    sub(info_tsv, "dtInicio", str(data["dt_inicio"]))
    if data.get("nr_proc_trab"):
        sub(info_tsv, "nrProcTrab", str(data["nr_proc_trab"]))
    if data.get("nat_atividade") is not None:
        sub(info_tsv, "natAtividade", str(data["nat_atividade"]))

    # infoComplementares (opcional)
    has_complementares = (
        data.get("nm_cargo")
        or data.get("cod_cbo")
        or data.get("vr_sal_fx") is not None
        or data.get("dt_opc_fgts")
        or data.get("categ_orig_dir_sind")
        or data.get("categ_orig_cedido")
        or data.get("categ_orig_mand_elet")
        or data.get("tp_insc_local") is not None
    )
    if has_complementares:
        info_compl = sub(info_tsv, "infoComplementares")

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

        # FGTS (opcional - categ 721)
        if data.get("dt_opc_fgts"):
            fgts = sub(info_compl, "FGTS")
            sub(fgts, "dtOpcFGTS", str(data["dt_opc_fgts"]))

        # infoDirigenteSindical (opcional - categ 401)
        if data.get("categ_orig_dir_sind"):
            dir_sind = sub(info_compl, "infoDirigenteSindical")
            sub(dir_sind, "categOrig", str(data["categ_orig_dir_sind"]))
            if data.get("tp_insc_dir_sind") is not None:
                sub(dir_sind, "tpInsc", str(data["tp_insc_dir_sind"]))
            if data.get("nr_insc_dir_sind"):
                sub(dir_sind, "nrInsc", str(data["nr_insc_dir_sind"]))
            if data.get("dt_adm_orig"):
                sub(dir_sind, "dtAdmOrig", str(data["dt_adm_orig"]))
            if data.get("matric_orig"):
                sub(dir_sind, "matricOrig", str(data["matric_orig"]))
            if data.get("tp_reg_trab_dir_sind") is not None:
                sub(dir_sind, "tpRegTrab", str(data["tp_reg_trab_dir_sind"]))
            sub(dir_sind, "tpRegPrev", str(data["tp_reg_prev_dir_sind"]))

        # infoTrabCedido (opcional - categ 305, 410)
        if data.get("categ_orig_cedido"):
            trab_cedido = sub(info_compl, "infoTrabCedido")
            sub(trab_cedido, "categOrig", str(data["categ_orig_cedido"]))
            sub(trab_cedido, "cnpjCednt", str(data["cnpj_cednt"]))
            sub(trab_cedido, "matricCed", str(data["matric_ced"]))
            sub(trab_cedido, "dtAdmCed", str(data["dt_adm_ced"]))
            sub(trab_cedido, "tpRegTrab", str(data["tp_reg_trab_cedido"]))
            sub(trab_cedido, "tpRegPrev", str(data["tp_reg_prev_cedido"]))

        # infoMandElet (opcional - categ 304)
        if data.get("categ_orig_mand_elet"):
            mand_elet = sub(info_compl, "infoMandElet")
            sub(mand_elet, "categOrig", str(data["categ_orig_mand_elet"]))
            sub(mand_elet, "cnpjOrig", str(data["cnpj_orig_mand"]))
            sub(mand_elet, "matricOrig", str(data["matric_orig_mand"]))
            sub(mand_elet, "dtExercOrig", str(data["dt_exerc_orig"]))
            if data.get("ind_remun_cargo") is not None:
                sub(mand_elet, "indRemunCargo", str(data["ind_remun_cargo"]))
            sub(mand_elet, "tpRegTrab", str(data["tp_reg_trab_mand"]))
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
            # instEstagiario (opcional)
            if data.get("cnpj_inst_ensino"):
                inst = sub(estagiario, "instEstagiario")
                sub(inst, "cnpjInstEnsino", str(data["cnpj_inst_ensino"]))
            # ageIntegracao (opcional)
            if data.get("cnpj_age_integ"):
                age = sub(estagiario, "ageIntegracao")
                sub(age, "cnpjAgntInteg", str(data["cnpj_age_integ"]))

        # localTrabGeral (opcional)
        if data.get("tp_insc_local") is not None:
            local_trab = sub(info_compl, "localTrabGeral")
            sub(local_trab, "tpInsc", str(data["tp_insc_local"]))
            sub(local_trab, "nrInsc", str(data["nr_insc_local"]))
            if data.get("desc_comp"):
                sub(local_trab, "descComp", str(data["desc_comp"]))

    return EventoXml(root, _NAMESPACE)
