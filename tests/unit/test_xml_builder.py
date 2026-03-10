"""Testes unitários do xml_builder e EventoXml."""
from lxml import etree

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub

NS = "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_03_00"


def test_make_esocial_creates_root_and_event():
    root, evt = make_esocial("evtAdmissao", "ID001", NS)
    assert root.tag == f"{{{NS}}}eSocial"
    assert evt.tag == f"{{{NS}}}evtAdmissao"
    assert evt.get("Id") == "ID001"


def test_sub_adds_child_with_text():
    root, evt = make_esocial("evtAdmissao", "ID001", NS)
    child = sub(evt, "cpfTrab", "12345678901")
    assert child.tag == f"{{{NS}}}cpfTrab"
    assert child.text == "12345678901"


def test_sub_adds_child_without_text():
    root, evt = make_esocial("evtAdmissao", "ID001", NS)
    child = sub(evt, "ideEvento")
    assert child.tag == f"{{{NS}}}ideEvento"
    assert child.text is None


def test_sub_inherits_parent_namespace():
    root, evt = make_esocial("evtAdmissao", "ID001", NS)
    ide = sub(evt, "ideEvento")
    sub(ide, "tpAmb", "2")
    assert etree.QName(ide[0]).namespace == NS


def test_evento_xml_to_xml_returns_string():
    root, evt = make_esocial("evtAdmissao", "ID001", NS)
    sub(evt, "test", "value")
    evento = EventoXml(root, NS)
    xml = evento.to_xml()
    assert isinstance(xml, str)
    assert "<?xml" in xml
    assert "evtAdmissao" in xml
    assert 'Id="ID001"' in xml


def test_evento_xml_to_xml_bytes_returns_bytes():
    root, evt = make_esocial("evtAdmissao", "ID001", NS)
    evento = EventoXml(root, NS)
    xml_bytes = evento.to_xml_bytes()
    assert isinstance(xml_bytes, bytes)
    assert b"evtAdmissao" in xml_bytes


def test_evento_xml_no_namespace_prefix():
    """O XML gerado não deve conter prefixos de namespace (ns0:, ns1:)."""
    root, evt = make_esocial("evtAdmissao", "ID001", NS)
    sub(evt, "campo", "valor")
    evento = EventoXml(root, NS)
    xml = evento.to_xml()
    assert "ns0:" not in xml
    assert "ns1:" not in xml
    assert "xsi:type" not in xml
