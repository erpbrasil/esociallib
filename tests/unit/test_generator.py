"""Testes unitários do generator (sem XSDs nem certificados)."""
from unittest.mock import MagicMock, patch

import pytest

from esociallib.exceptions import EsocialValidationError
from esociallib.generator import (
    _BUILDERS,
    generate_unsigned,
    list_supported_events,
    register_builder,
    to_xml,
)


@pytest.fixture(autouse=True)
def clean_registry():
    """Preserva o registry entre testes."""
    original = dict(_BUILDERS)
    yield
    _BUILDERS.clear()
    _BUILDERS.update(original)


def test_register_builder_adds_to_registry():
    @register_builder("S-9999")
    def fake_builder(data, environment="restricted"):
        return MagicMock()

    assert "S-9999" in _BUILDERS


def test_list_supported_events_returns_sorted():
    @register_builder("S-8888")
    def b1(data, environment="restricted"):
        return MagicMock()

    @register_builder("S-7777")
    def b2(data, environment="restricted"):
        return MagicMock()

    events = list_supported_events()
    assert "S-8888" in events
    assert "S-7777" in events
    assert events == sorted(events)


def test_generate_unsigned_raises_on_unknown_event():
    with pytest.raises(ValueError, match="Nenhum builder registrado"):
        generate_unsigned("S-9998", data={})


def test_generate_unsigned_raises_validation_error_on_bad_xml():
    mock_evento = MagicMock()
    mock_evento.to_xml.return_value = "<eSocial></eSocial>"

    @register_builder("S-9997")
    def builder(data, environment="restricted"):
        return mock_evento

    with patch("esociallib.generator.validate_xsd") as mock_validate:
        mock_validate.return_value = ["Linha 1: campo obrigatório ausente"]
        with pytest.raises(EsocialValidationError) as exc_info:
            generate_unsigned("S-9997", data={})
        assert "S-9997" in str(exc_info.value)


def test_generate_unsigned_returns_xml_on_success():
    expected_xml = "<eSocial><evtAdmissao Id='ID001'/></eSocial>"
    mock_evento = MagicMock()
    mock_evento.to_xml.return_value = expected_xml

    @register_builder("S-9996")
    def builder(data, environment="restricted"):
        return mock_evento

    with patch("esociallib.generator.validate_xsd") as mock_validate:
        mock_validate.return_value = []
        result = generate_unsigned("S-9996", data={"test": True})

    assert result == expected_xml


def test_to_xml_is_same_as_generate_unsigned():
    """to_xml e generate_unsigned devem ser a mesma função."""
    assert to_xml is generate_unsigned
