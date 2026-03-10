"""Testes de integração: assinatura digital com certificado fake."""
import pytest
from lxml import etree

from esociallib.assinatura import assinar, info_certificado
from esociallib.builders.s_2200 import build_s2200
from esociallib.builders.s_1000 import build_s1000


@pytest.fixture
def s2200_xml():
    data = {
        "tp_insc": 1, "nr_insc": "12345678000199",
        "cpf_trab": "12345678901", "nm_trab": "JOAO DA SILVA",
        "sexo": "M", "raca_cor": 1, "grau_instr": "07",
        "dt_nascto": "1980-01-15", "matricula": "000123",
        "tp_reg_trab": 1, "tp_reg_prev": 1, "dt_adm": "2024-03-01",
        "nat_atividade": 1, "cnpj_sind_categ_prof": "12345678000199",
        "cod_categ": "101", "vr_sal_fx": "5000.00", "und_sal_fixo": 5,
    }
    return build_s2200(data).to_xml()


@pytest.fixture
def s1000_xml():
    data = {
        "tp_insc": 1, "nr_insc": "12345678000199",
        "ini_valid": "2024-01", "class_trib": "01",
        "ind_coop": 0, "ind_constr": 0, "ind_des_folha": 0,
        "ind_opt_reg_eletron": 0, "ind_ent_ed": "N", "ind_ett": "N",
        "nm_razao": "EMPRESA TESTE LTDA", "nat_jur": "2062", "ind_sit_pj": 0,
    }
    return build_s1000(data).to_xml()


def test_assinar_adds_signature(fake_cert, fake_cert_password, s2200_xml):
    xml_signed = assinar(
        s2200_xml, cert_pfx=fake_cert,
        cert_password=fake_cert_password, raise_expirado=False,
    )
    assert isinstance(xml_signed, str)
    assert "Signature" in xml_signed
    assert "SignatureValue" in xml_signed
    assert "DigestValue" in xml_signed


def test_assinar_preserves_event_content(fake_cert, fake_cert_password, s2200_xml):
    xml_signed = assinar(
        s2200_xml, cert_pfx=fake_cert,
        cert_password=fake_cert_password, raise_expirado=False,
    )
    root = etree.fromstring(xml_signed.encode("utf-8"))
    ns = "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_03_00"
    evt = root.find(f"{{{ns}}}evtAdmissao")
    assert evt is not None
    assert evt.get("Id") is not None
    cpf = root.find(f".//{{{ns}}}cpfTrab")
    assert cpf is not None
    assert cpf.text == "12345678901"


def test_assinar_s1000(fake_cert, fake_cert_password, s1000_xml):
    xml_signed = assinar(
        s1000_xml, cert_pfx=fake_cert,
        cert_password=fake_cert_password, raise_expirado=False,
    )
    assert "Signature" in xml_signed
    root = etree.fromstring(xml_signed.encode("utf-8"))
    ns = "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00"
    evt = root.find(f"{{{ns}}}evtInfoEmpregador")
    assert evt is not None


def test_signed_xml_validates_xsd(fake_cert, fake_cert_password, s2200_xml):
    """XML assinado deve validar contra o XSD (que exige <Signature>)."""
    from esociallib.validators import validate_xsd
    xml_signed = assinar(
        s2200_xml, cert_pfx=fake_cert,
        cert_password=fake_cert_password, raise_expirado=False,
    )
    errors = validate_xsd(xml_signed, "S-2200")
    assert errors == [], f"Erros XSD no XML assinado: {errors}"


def test_info_certificado(fake_cert, fake_cert_password):
    info = info_certificado(
        cert_pfx=fake_cert, cert_password=fake_cert_password,
        raise_expirado=False,
    )
    assert "subject" in info
    assert "valid_until" in info
    assert "expired" in info
    assert info["expired"] is False


def test_assinar_with_expired_cert_raises(fake_cert_expired, s2200_xml):
    """Certificado expirado deve levantar exceção com raise_expirado=True."""
    with pytest.raises(Exception):
        assinar(
            s2200_xml, cert_pfx=fake_cert_expired,
            cert_password="teste123", raise_expirado=True,
        )
