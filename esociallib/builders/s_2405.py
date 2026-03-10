"""
Builder para S-2405 — Cadastro de Beneficiario - Entes Publicos - Alteracao.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2405 registra alteracoes cadastrais de beneficiarios de regime
proprio de previdencia social (RPPS) em entes publicos.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtCdBenefAlt/v_S_01_03_00"


@register_builder("S-2405")
def build_s2405(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2405 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,
            "nr_insc": "12345678",

            # ideBenef
            "cpf_benef": "12345678901",

            # alteracao
            "dt_alteracao": "2024-06-01",

            # dadosBenef
            "nm_benefic": "MARIA DA SILVA",
            "sexo": "F",
            "raca_cor": 1,
            "inc_fis_men": "N",

            # endereco
            "tipo_logradouro": "R",
            "dsc_lograd": "RUA DAS FLORES",
            "nr_lograd": "200",
            "cep": "01001000",
            "cod_munic_end": "3550308",
            "uf_end": "SP",

            # dependentes (opcional)
            "dependentes": [],
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtCdBenefAlt", event_id, _NAMESPACE)

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

    # ideBenef
    ide_benef = sub(evt, "ideBenef")
    sub(ide_benef, "cpfBenef", str(data["cpf_benef"]))

    # alteracao
    alteracao = sub(evt, "alteracao")
    sub(alteracao, "dtAlteracao", str(data["dt_alteracao"]))

    # dadosBenef
    dados_benef = sub(alteracao, "dadosBenef")
    sub(dados_benef, "nmBenefic", str(data["nm_benefic"]))
    sub(dados_benef, "sexo", str(data["sexo"]))
    sub(dados_benef, "racaCor", str(data["raca_cor"]))
    if data.get("est_civ") is not None:
        sub(dados_benef, "estCiv", str(data["est_civ"]))
    sub(dados_benef, "incFisMen", str(data.get("inc_fis_men", "N")))

    # endereco
    endereco = sub(dados_benef, "endereco")
    if data.get("pais_resid"):
        # Exterior
        exterior = sub(endereco, "exterior")
        sub(exterior, "paisResid", str(data["pais_resid"]))
        sub(exterior, "dscLograd", str(data["dsc_lograd"]))
        sub(exterior, "nrLograd", str(data.get("nr_lograd", "S/N")))
        if data.get("complemento"):
            sub(exterior, "complemento", str(data["complemento"]))
        if data.get("bairro"):
            sub(exterior, "bairro", str(data["bairro"]))
        sub(exterior, "nmCid", str(data["nm_cid"]))
        if data.get("cod_postal"):
            sub(exterior, "codPostal", str(data["cod_postal"]))
    else:
        # Brasil
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

    # dependentes (opcional)
    for dep in data.get("dependentes", []):
        dependente = sub(dados_benef, "dependente")
        if dep.get("tp_dep") is not None:
            sub(dependente, "tpDep", str(dep["tp_dep"]))
        sub(dependente, "nmDep", str(dep["nm_dep"]))
        sub(dependente, "dtNascto", str(dep["dt_nascto"]))
        if dep.get("cpf_dep"):
            sub(dependente, "cpfDep", str(dep["cpf_dep"]))
        sub(dependente, "sexoDep", str(dep["sexo_dep"]))
        sub(dependente, "depIRRF", str(dep["dep_irrf"]))
        sub(dependente, "incFisMen", str(dep.get("inc_fis_men", "N")))
        if dep.get("descr_dep"):
            sub(dependente, "descrDep", str(dep["descr_dep"]))

    return EventoXml(root, _NAMESPACE)
