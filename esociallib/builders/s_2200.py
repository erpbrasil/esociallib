"""
Builder para S-2200 — Cadastramento Inicial do Vínculo e Admissão/Ingresso.

Este módulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serialização.

O mapper Odoo (services/mapper_s2200.py no sped_esocial) é responsável
por extrair os dados de hr.employee + hr.contract e montar o dict.
Este builder apenas traduz o dict para a estrutura XML do eSocial.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_03_00"


@register_builder("S-2200")
def build_s2200(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constrói o XML do evento S-2200 a partir do dict do mapper Odoo.

    :param data: Dicionário com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 dígitos) ou CPF

            # trabalhador
            "cpf_trab": "12345678901",
            "nm_trab": "JOAO DA SILVA",
            "sexo": "M",                    # M ou F
            "raca_cor": 1,                  # Tabela eSocial
            "grau_instr": "07",             # Tabela eSocial
            "dt_nascto": "1980-01-15",      # YYYY-MM-DD
            "pais_nascto": "105",           # Brasil
            "pais_nac": "105",

            # vinculo
            "matricula": "000123",
            "tp_reg_trab": 1,               # 1=CLT, 2=Estatutário
            "tp_reg_prev": 1,               # 1=RGPS, 2=RPPS, 3=Não segurado
            "cad_ini": "N",                 # S ou N

            # infoCeletista (se CLT)
            "dt_adm": "2024-03-01",         # YYYY-MM-DD
            "tp_admissao": 1,               # Tabela 9
            "ind_admissao": 1,              # 1=Normal, 2=Ação fiscal, 3=Judicial
            "tp_reg_jor": 1,                # 1=Submetido a horário
            "nat_atividade": 1,             # 1=Normal, 2=Aprendiz
            "cnpj_sind_categ_prof": "12345678000199",

            # infoContrato
            "cod_categ": "101",
            "cod_cbo": "252105",            # CBO (opcional)

            # remuneração
            "vr_sal_fx": "5000.00",         # Salário fixo como string Decimal
            "und_sal_fixo": 5,              # 5=mensal, 6=quinzenal, etc.

            # horário contratual (opcional)
            "qtd_hrs_sem": "44.00",
            "tp_jornada": 2,

            # duração do contrato (opcional)
            "tp_contr": 1,                  # 1=Indeterminado
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtAdmissao", event_id, _NAMESPACE)

    # ideEvento
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador
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

    # vinculo
    vinculo = sub(evt, "vinculo")
    sub(vinculo, "matricula", str(data["matricula"]))
    sub(vinculo, "tpRegTrab", str(data["tp_reg_trab"]))
    sub(vinculo, "tpRegPrev", str(data["tp_reg_prev"]))
    sub(vinculo, "cadIni", str(data.get("cad_ini", "N")))

    # vinculo.infoRegimeTrab
    info_regime = sub(vinculo, "infoRegimeTrab")

    if int(data["tp_reg_trab"]) == 1:
        # CLT
        celetista = sub(info_regime, "infoCeletista")
        sub(celetista, "dtAdm", str(data["dt_adm"]))
        sub(celetista, "tpAdmissao", str(data.get("tp_admissao", 1)))
        sub(celetista, "indAdmissao", str(data.get("ind_admissao", 1)))
        if data.get("nr_proc_trab"):
            sub(celetista, "nrProcTrab", str(data["nr_proc_trab"]))
        sub(celetista, "tpRegJor", str(data.get("tp_reg_jor", 1)))
        sub(celetista, "natAtividade", str(data["nat_atividade"]))
        if data.get("dt_base") is not None:
            sub(celetista, "dtBase", str(data["dt_base"]))
        sub(celetista, "cnpjSindCategProf", str(data["cnpj_sind_categ_prof"]))
    else:
        # Estatutário
        estatutario = sub(info_regime, "infoEstatutario")
        sub(estatutario, "tpProv", str(data["tp_prov"]))
        sub(estatutario, "dtExercicio", str(data["dt_exercicio"]))

    # vinculo.infoContrato
    info_contrato = sub(vinculo, "infoContrato")
    if data.get("nm_cargo"):
        sub(info_contrato, "nmCargo", str(data["nm_cargo"]))
    if data.get("cod_cbo"):
        sub(info_contrato, "CBOCargo", str(data["cod_cbo"]))
    sub(info_contrato, "codCateg", str(data["cod_categ"]))

    # infoContrato.remuneracao
    if data.get("vr_sal_fx") is not None:
        remuneracao = sub(info_contrato, "remuneracao")
        sub(remuneracao, "vrSalFx", str(data["vr_sal_fx"]))
        sub(remuneracao, "undSalFixo", str(data["und_sal_fixo"]))
        if data.get("dsc_sal_var"):
            sub(remuneracao, "dscSalVar", str(data["dsc_sal_var"]))

    # infoContrato.duracao
    if data.get("tp_contr") is not None:
        duracao = sub(info_contrato, "duracao")
        sub(duracao, "tpContr", str(data["tp_contr"]))
        if data.get("dt_term"):
            sub(duracao, "dtTerm", str(data["dt_term"]))
        if data.get("clau_assec"):
            sub(duracao, "clauAssec", str(data["clau_assec"]))

    # infoContrato.localTrabalho
    if data.get("tp_insc_local") is not None:
        local_trabalho = sub(info_contrato, "localTrabalho")
        local_trab_geral = sub(local_trabalho, "localTrabGeral")
        sub(local_trab_geral, "tpInsc", str(data["tp_insc_local"]))
        sub(local_trab_geral, "nrInsc", str(data["nr_insc_local"]))
        if data.get("desc_comp"):
            sub(local_trab_geral, "descComp", str(data["desc_comp"]))

    # infoContrato.horContratual
    if data.get("qtd_hrs_sem") is not None:
        hor_contratual = sub(info_contrato, "horContratual")
        sub(hor_contratual, "qtdHrsSem", str(data["qtd_hrs_sem"]))
        sub(hor_contratual, "tpJornada", str(data["tp_jornada"]))

    return EventoXml(root, _NAMESPACE)
