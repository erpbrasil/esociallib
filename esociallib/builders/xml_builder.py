"""
xml_builder.py — Utilitários para construção de XML eSocial com lxml.

Os bindings xsdata gerados sofrem do problema "chameleon include":
tipos.xsd não possui targetNamespace, e os tipos compartilhados
(T_ideEmpregador, T_remuneracao etc) ficam com namespace errado
na serialização. Para contornar, os builders constroem o XML
diretamente com lxml, garantindo namespaces corretos.

Os bindings xsdata continuam úteis para DESERIALIZAÇÃO
(parsing de respostas do governo via CommonMixin.from_xml).
"""

from __future__ import annotations

from lxml import etree


class EventoXml:
    """Wrapper que encapsula lxml.etree e fornece to_xml() para o generator."""

    def __init__(self, root: etree._Element, namespace: str):
        self._root = root
        self._namespace = namespace

    def to_xml(self, ns_map: dict | None = None) -> str:
        xml_bytes = etree.tostring(
            self._root,
            encoding="UTF-8",
            xml_declaration=True,
            pretty_print=True,
        )
        return xml_bytes.decode("UTF-8")

    def to_xml_bytes(self) -> bytes:
        return etree.tostring(
            self._root,
            encoding="UTF-8",
            xml_declaration=True,
            pretty_print=True,
        )


def make_esocial(
    evento_tag: str,
    evento_id: str,
    namespace: str,
) -> tuple[etree._Element, etree._Element]:
    """
    Cria a raiz <eSocial> e o filho <evtXxx Id="...">.

    :returns: (root, evt_element)
    """
    nsmap = {None: namespace}
    root = etree.Element(f"{{{namespace}}}eSocial", nsmap=nsmap)
    evt = etree.SubElement(root, f"{{{namespace}}}{evento_tag}")
    evt.set("Id", evento_id)
    return root, evt


def sub(parent: etree._Element, tag: str, text: str | None = None) -> etree._Element:
    """Adiciona sub-elemento ao parent usando o namespace do parent."""
    ns = etree.QName(parent).namespace
    el = etree.SubElement(parent, f"{{{ns}}}{tag}")
    if text is not None:
        el.text = str(text)
    return el
