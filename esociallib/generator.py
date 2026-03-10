"""
generator.py — Constrói XML de eventos eSocial a partir de dicts.

Responsabilidade única: dict (do mapper Odoo) → dataclass → XML string.
Assinatura e transmissão ficam fora desta lib (erpbrasil.assinatura/transmissao).
"""

from __future__ import annotations

import logging
from typing import Any

from esociallib.exceptions import EsocialValidationError
from esociallib.validators import validate_xsd

logger = logging.getLogger(__name__)

_BUILDERS: dict[str, Any] = {}
_builders_loaded = False


def _ensure_builders_loaded() -> None:
    """Importa builders na primeira chamada (evita circular import)."""
    global _builders_loaded
    if not _builders_loaded:
        _builders_loaded = True
        import esociallib.builders  # noqa: F401


def register_builder(event_code: str):
    """Decorador para registrar um builder de evento."""
    def decorator(func):
        _BUILDERS[event_code] = func
        return func
    return decorator


def to_xml(event_type: str, data: dict, environment: str = "restricted") -> str:
    """
    Constrói e valida o XML de um evento eSocial.

    :param event_type: Código do evento (ex: 'S-2200').
    :param data: Dict montado pelo mapper Odoo.
    :param environment: 'production' ou 'restricted'.
    :returns: String XML validada, pronta para assinar.
    :raises: EsocialValidationError se inválido.
    :raises: ValueError se event_type sem builder.
    """
    _ensure_builders_loaded()
    builder = _BUILDERS.get(event_type)
    if builder is None:
        raise ValueError(
            f"Nenhum builder registrado para '{event_type}'. "
            f"Disponíveis: {', '.join(sorted(_BUILDERS))}"
        )

    evento = builder(data, environment=environment)
    xml_str = evento.to_xml()

    errors = validate_xsd(xml_str, event_type)
    # Filtra erros de Signature — XML não assinado não terá <Signature>,
    # mas o XSD exige. A assinatura é adicionada depois por assinar().
    errors = [e for e in errors if "Signature" not in e]
    if errors:
        raise EsocialValidationError(errors=errors, event_type=event_type)

    return xml_str


def list_supported_events() -> list[str]:
    """Retorna lista de eventos com builder registrado."""
    _ensure_builders_loaded()
    return sorted(_BUILDERS.keys())


# Alias — nome descritivo usado nos testes e integração com sped_esocial
generate_unsigned = to_xml
