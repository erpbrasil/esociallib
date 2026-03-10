"""
CommonMixin — injetado pelo xsdata em todas as classes de binding geradas.

Não editar esta classe sem regenerar os bindings logo após.
"""

from __future__ import annotations

import importlib.resources
from pathlib import Path
from typing import TYPE_CHECKING, TypeVar

from lxml import etree
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from esociallib.exceptions import EsocialValidationError

if TYPE_CHECKING:
    pass

T = TypeVar("T", bound="CommonMixin")

_context = XmlContext()

_SERIALIZER_CONFIG = SerializerConfig(
    pretty_print=True,
    xml_declaration=True,
    encoding="UTF-8",
)


class CommonMixin:
    """
    Mixin base injetado pelo xsdata em todas as classes de binding eSocial.

    Fornece serialização/deserialização XML e validação XSD.
    Não instanciar diretamente — usar as subclasses geradas.
    """

    # Namespace do evento — sobrescrito nas subclasses geradas.
    # Ex: "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_03_00"
    _namespace: str | None = None

    # Nome do arquivo XSD correspondente (sem extensão).
    # Ex: "evtAdmissao" — usado para localizar o XSD bundled.
    _xsd_name: str | None = None

    def to_xml(self, ns_map: dict | None = None) -> str:
        """
        Serializa o objeto para string XML UTF-8.

        :param ns_map: Mapa de prefixos de namespace. Se None, usa o namespace
                       padrão do evento sem prefixo (padrão eSocial).
        :returns: String XML com declaração.
        """
        effective_ns_map = ns_map or ({None: self._namespace} if self._namespace else {})
        serializer = XmlSerializer(context=_context, config=_SERIALIZER_CONFIG)
        return serializer.render(self, ns_map=effective_ns_map)

    def to_xml_bytes(self, ns_map: dict | None = None) -> bytes:
        """Retorna XML como bytes UTF-8."""
        return self.to_xml(ns_map).encode("utf-8")

    @classmethod
    def from_xml(cls: type[T], xml: str | bytes) -> T:
        """
        Desserializa XML para a classe correspondente.

        :param xml: String ou bytes XML.
        :returns: Instância preenchida.
        :raises: xsdata.exceptions.ParserError se XML inválido.
        """
        parser = XmlParser(context=_context)
        if isinstance(xml, str):
            xml = xml.encode("utf-8")
        return parser.from_bytes(xml, cls)

    @classmethod
    def from_path(cls: type[T], path: str | Path) -> T:
        """
        Desserializa XML a partir de arquivo.

        :param path: Caminho para arquivo XML.
        :returns: Instância preenchida.
        """
        return cls.from_xml(Path(path).read_bytes())

    def validate_xsd(self) -> list[str]:
        """
        Valida o objeto contra o XSD bundled.

        :returns: Lista de erros (vazia se válido).
        :raises: ValueError se _xsd_name não estiver definido.
        """
        if not self._xsd_name:
            raise ValueError(
                f"{self.__class__.__name__} não define _xsd_name — "
                "validação XSD não disponível."
            )
        xsd_path = _get_bundled_xsd(self._xsd_name)
        schema = etree.XMLSchema(etree.parse(str(xsd_path)))
        xml_doc = etree.fromstring(self.to_xml_bytes())
        schema.validate(xml_doc)
        return [
            f"Linha {e.line}: {e.message}"
            for e in schema.error_log
        ]

    def validate_xsd_or_raise(self) -> None:
        """
        Valida contra o XSD e levanta EsocialValidationError se inválido.

        :raises: EsocialValidationError com lista de erros.
        """
        errors = self.validate_xsd()
        if errors:
            raise EsocialValidationError(
                errors=errors,
                event_type=self._xsd_name or self.__class__.__name__,
            )


def _get_bundled_xsd(xsd_name: str) -> Path:
    """
    Localiza um XSD bundled no pacote instalado.

    :param xsd_name: Nome do arquivo XSD sem extensão (ex: 'evtAdmissao').
    :returns: Path para o arquivo XSD.
    :raises: FileNotFoundError se não encontrado.
    """
    try:
        pkg = importlib.resources.files("esociallib.esocial.schemas.v_s13")
        xsd_file = pkg / f"{xsd_name}.xsd"
        path = Path(str(xsd_file))
        if not path.exists():
            raise FileNotFoundError
        return path
    except (FileNotFoundError, TypeError) as exc:
        raise FileNotFoundError(
            f"XSD '{xsd_name}.xsd' não encontrado no pacote. "
            "Certifique-se de que os XSDs S-1.3 estão em "
            "esociallib/esocial/schemas/v_s13/."
        ) from exc
