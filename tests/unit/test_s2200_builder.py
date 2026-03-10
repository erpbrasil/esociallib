"""Testes unitários do builder S-2200."""
import pytest
from lxml import etree

from esociallib.builders.s_2200 import build_s2200


@pytest.fixture
def minimal_data():
    """Dict mínimo para gerar um S-2200 CLT válido."""
    return {
        "tp_insc": 1,
        "nr_insc": "12345678",
        "cpf_trab": "12345678901",
        "nm_trab": "JOAO DA SILVA",
        "sexo": "M",
        "raca_cor": 1,
        "grau_instr": "07",
        "dt_nascto": "1980-01-15",
        "matricula": "000123",
        "tp_reg_trab": 1,
        "tp_reg_prev": 1,
        "dt_adm": "2024-03-01",
        "nat_atividade": 1,
        "cnpj_sind_categ_prof": "12345678000199",
        "cod_categ": "101",
        "vr_sal_fx": "5000.00",
        "und_sal_fixo": 5,
    }


NS = "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_03_00"


def _parse(xml_str):
    return etree.fromstring(xml_str.encode("utf-8"))


def _find(root, xpath):
    return root.find(xpath, namespaces={"e": NS})


def test_build_s2200_returns_evento_xml(minimal_data):
    evento = build_s2200(minimal_data)
    assert hasattr(evento, "to_xml")
    xml = evento.to_xml()
    assert isinstance(xml, str)
    assert "evtAdmissao" in xml


def test_build_s2200_xml_structure(minimal_data):
    xml = build_s2200(minimal_data).to_xml()
    root = _parse(xml)

    assert root.tag == f"{{{NS}}}eSocial"
    evt = root.find(f"{{{NS}}}evtAdmissao")
    assert evt is not None
    assert evt.get("Id") is not None
    assert evt.get("Id").startswith("ID")


def test_build_s2200_ide_evento(minimal_data):
    xml = build_s2200(minimal_data, environment="restricted").to_xml()
    root = _parse(xml)
    tp_amb = root.find(f".//{{{NS}}}tpAmb")
    assert tp_amb is not None
    assert tp_amb.text == "2"


def test_build_s2200_production_environment(minimal_data):
    xml = build_s2200(minimal_data, environment="production").to_xml()
    root = _parse(xml)
    tp_amb = root.find(f".//{{{NS}}}tpAmb")
    assert tp_amb.text == "1"


def test_build_s2200_ide_empregador(minimal_data):
    xml = build_s2200(minimal_data).to_xml()
    root = _parse(xml)
    tp_insc = root.find(f".//{{{NS}}}ideEmpregador/{{{NS}}}tpInsc")
    nr_insc = root.find(f".//{{{NS}}}ideEmpregador/{{{NS}}}nrInsc")
    assert tp_insc.text == "1"
    assert nr_insc.text == "12345678"


def test_build_s2200_trabalhador(minimal_data):
    xml = build_s2200(minimal_data).to_xml()
    root = _parse(xml)
    cpf = root.find(f".//{{{NS}}}cpfTrab")
    nm = root.find(f".//{{{NS}}}nmTrab")
    assert cpf.text == "12345678901"
    assert nm.text == "JOAO DA SILVA"


def test_build_s2200_vinculo_clt(minimal_data):
    xml = build_s2200(minimal_data).to_xml()
    root = _parse(xml)
    matricula = root.find(f".//{{{NS}}}matricula")
    dt_adm = root.find(f".//{{{NS}}}dtAdm")
    assert matricula.text == "000123"
    assert dt_adm.text == "2024-03-01"


def test_build_s2200_remuneracao(minimal_data):
    xml = build_s2200(minimal_data).to_xml()
    root = _parse(xml)
    vr_sal = root.find(f".//{{{NS}}}vrSalFx")
    und_sal = root.find(f".//{{{NS}}}undSalFixo")
    assert vr_sal.text == "5000.00"
    assert und_sal.text == "5"


def test_build_s2200_no_namespace_prefix(minimal_data):
    xml = build_s2200(minimal_data).to_xml()
    assert "ns0:" not in xml
    assert "ns1:" not in xml
    assert "xsi:type" not in xml


def test_build_s2200_optional_endereco(minimal_data):
    """Sem dados de endereço, o grupo não deve aparecer."""
    xml = build_s2200(minimal_data).to_xml()
    assert "endereco" not in xml


def test_build_s2200_with_endereco(minimal_data):
    minimal_data.update({
        "dsc_lograd": "RUA DAS FLORES",
        "nr_lograd": "123",
        "bairro": "CENTRO",
        "cep": "01001000",
        "cod_munic_end": "3550308",
        "uf_end": "SP",
    })
    xml = build_s2200(minimal_data).to_xml()
    root = _parse(xml)
    lograd = root.find(f".//{{{NS}}}dscLograd")
    assert lograd is not None
    assert lograd.text == "RUA DAS FLORES"


def test_build_s2200_estatutario():
    data = {
        "tp_insc": 1,
        "nr_insc": "12345678",
        "cpf_trab": "12345678901",
        "nm_trab": "MARIA SOUZA",
        "sexo": "F",
        "raca_cor": 2,
        "grau_instr": "09",
        "dt_nascto": "1985-06-20",
        "matricula": "SRV001",
        "tp_reg_trab": 2,
        "tp_reg_prev": 2,
        "tp_prov": 1,
        "dt_exercicio": "2020-01-15",
        "cod_categ": "301",
    }
    xml = build_s2200(data, environment="restricted").to_xml()
    root = _parse(xml)
    tp_prov = root.find(f".//{{{NS}}}tpProv")
    assert tp_prov is not None
    assert tp_prov.text == "1"
    # Não deve ter infoCeletista
    assert root.find(f".//{{{NS}}}infoCeletista") is None
