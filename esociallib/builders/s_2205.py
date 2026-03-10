"""
Builder para S-2205 -- Alteracao de Dados Cadastrais do Trabalhador.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2205 e um evento nao-periodico que registra alteracoes nos dados
cadastrais do trabalhador, como nome, endereco, estado civil,
grau de instrucao, dependentes, etc.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtAltCadastral/v_S_01_03_00"


@register_builder("S-2205")
def build_s2205(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2205 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideTrabalhador
            "cpf_trab": "12345678901",

            # alteracao
            "dt_alteracao": "2024-06-01",   # Data da alteracao cadastral

            # dadosTrabalhador
            "nm_trab": "JOAO DA SILVA",
            "sexo": "M",                    # M ou F
            "raca_cor": 1,                  # Tabela eSocial
            "est_civ": None,                # Estado civil (opcional)
            "grau_instr": "07",             # Tabela eSocial
            "nm_soc": None,                 # Nome social (opcional)
            "pais_nac": "105",              # Pais de nacionalidade

            # endereco (opcional)
            "tipo_logradouro": "R",         # Tipo logradouro (opcional)
            "dsc_lograd": "RUA DAS FLORES", # Descricao logradouro
            "nr_lograd": "100",             # Numero logradouro
            "complemento": None,            # Complemento (opcional)
            "bairro": "CENTRO",             # Bairro (opcional)
            "cep": "01001000",              # CEP
            "cod_munic_end": "3550308",     # Codigo municipio
            "uf_end": "SP",                 # UF

            # trabImig (opcional - trabalhador imigrante)
            "tmp_resid": None,              # Tempo de residencia (opcional)
            "cond_ing": None,               # Condicao de ingresso (opcional)

            # infoDeficiencia (opcional)
            "def_fisica": None,             # S ou N
            "def_visual": None,
            "def_auditiva": None,
            "def_mental": None,
            "def_intelectual": None,
            "reab_readap": None,
            "info_cota": None,              # S ou N (opcional)
            "observacao_def": None,         # Observacao (opcional)

            # dependentes (opcional - lista)
            "dependentes": [
                {
                    "tp_dep": "03",         # Tipo de dependente (opcional)
                    "nm_dep": "MARIA SILVA",
                    "dt_nascto": "2010-01-01",
                    "cpf_dep": "98765432100",  # (opcional)
                    "sexo_dep": "F",           # (opcional)
                    "dep_irrf": "S",
                    "dep_sf": "S",
                    "inc_trab": "N",           # (opcional)
                    "descr_dep": None,         # (opcional)
                }
            ],

            # contato (opcional)
            "fone_principal": "11999999999",
            "email_principal": "joao@example.com",
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtAltCadastral", event_id, _NAMESPACE)

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

    # ideTrabalhador
    ide_trabalhador = sub(evt, "ideTrabalhador")
    sub(ide_trabalhador, "cpfTrab", str(data["cpf_trab"]))

    # alteracao
    alteracao = sub(evt, "alteracao")
    sub(alteracao, "dtAlteracao", str(data["dt_alteracao"]))

    # dadosTrabalhador
    dados_trab = sub(alteracao, "dadosTrabalhador")
    sub(dados_trab, "nmTrab", str(data["nm_trab"]))
    sub(dados_trab, "sexo", str(data["sexo"]))
    sub(dados_trab, "racaCor", str(data["raca_cor"]))
    if data.get("est_civ") is not None:
        sub(dados_trab, "estCiv", str(data["est_civ"]))
    sub(dados_trab, "grauInstr", str(data["grau_instr"]))
    if data.get("nm_soc"):
        sub(dados_trab, "nmSoc", str(data["nm_soc"]))
    sub(dados_trab, "paisNac", str(data.get("pais_nac", "105")))

    # endereco (opcional)
    if data.get("tipo_logradouro") or data.get("dsc_lograd"):
        endereco = sub(dados_trab, "endereco")
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

    # trabImig (opcional - trabalhador imigrante)
    if data.get("cond_ing") is not None:
        trab_imig = sub(dados_trab, "trabImig")
        if data.get("tmp_resid") is not None:
            sub(trab_imig, "tmpResid", str(data["tmp_resid"]))
        sub(trab_imig, "condIng", str(data["cond_ing"]))

    # infoDeficiencia (opcional)
    if data.get("def_fisica") is not None:
        info_def = sub(dados_trab, "infoDeficiencia")
        sub(info_def, "defFisica", str(data["def_fisica"]))
        sub(info_def, "defVisual", str(data["def_visual"]))
        sub(info_def, "defAuditiva", str(data["def_auditiva"]))
        sub(info_def, "defMental", str(data["def_mental"]))
        sub(info_def, "defIntelectual", str(data["def_intelectual"]))
        sub(info_def, "reabReadap", str(data["reab_readap"]))
        if data.get("info_cota") is not None:
            sub(info_def, "infoCota", str(data["info_cota"]))
        if data.get("observacao_def"):
            sub(info_def, "observacao", str(data["observacao_def"]))

    # dependentes (opcional - lista)
    for dep in data.get("dependentes", []):
        dependente = sub(dados_trab, "dependente")
        if dep.get("tp_dep") is not None:
            sub(dependente, "tpDep", str(dep["tp_dep"]))
        sub(dependente, "nmDep", str(dep["nm_dep"]))
        sub(dependente, "dtNascto", str(dep["dt_nascto"]))
        if dep.get("cpf_dep"):
            sub(dependente, "cpfDep", str(dep["cpf_dep"]))
        if dep.get("sexo_dep"):
            sub(dependente, "sexoDep", str(dep["sexo_dep"]))
        sub(dependente, "depIRRF", str(dep["dep_irrf"]))
        sub(dependente, "depSF", str(dep["dep_sf"]))
        if dep.get("inc_trab") is not None:
            sub(dependente, "incTrab", str(dep["inc_trab"]))
        if dep.get("descr_dep"):
            sub(dependente, "descrDep", str(dep["descr_dep"]))

    # contato (opcional)
    if data.get("fone_principal") or data.get("email_principal"):
        contato = sub(dados_trab, "contato")
        if data.get("fone_principal"):
            sub(contato, "fonePrinc", str(data["fone_principal"]))
        if data.get("email_principal"):
            sub(contato, "emailPrinc", str(data["email_principal"]))

    return EventoXml(root, _NAMESPACE)
