"""
esociallib — Biblioteca Python para eSocial S-1.3 (KMEE)
=========================================================

Responsabilidades:
  - Bindings xsdata: dataclasses geradas dos XSDs S-1.3
  - Validação XSD
  - Orquestração: montar lote → assinar → enviar → consultar

Assinatura e transmissão delegadas para:
  - erpbrasil.assinatura (ICP-Brasil A1/A3)
  - erpbrasil.transmissao (SOAP 1.1 mTLS)

Uso básico::

    from esociallib.assinatura import assinar
    from esociallib.transmissao import enviar_lote, consultar_lote
    from esociallib.validators import validate_xsd

    # 1. Montar dataclass (via builder) → gerar XML
    xml = evento.to_xml()

    # 2. Validar + assinar
    validate_xsd(xml, "S-2200")
    xml_assinado = assinar(xml, cert_pfx=pfx, cert_password="senha")

    # 3. Enviar lote
    protocolo = enviar_lote([xml_assinado], cert_pfx=pfx,
                            cert_password="senha", environment="restricted")

    # 4. Consultar resultado
    resultado = consultar_lote(protocolo, cert_pfx=pfx,
                               cert_password="senha", environment="restricted")
"""

from esociallib.validators import validate_xsd
from esociallib.generator import to_xml, generate_unsigned, list_supported_events
from esociallib.exceptions import (
    EsocialError,
    EsocialValidationError,
    EsocialSignatureError,
    EsocialTransmissionError,
    EsocialBatchError,
)

# erpbrasil wrappers — optional at import time (required at call time)
try:
    from esociallib.assinatura import assinar, info_certificado
except ImportError:
    assinar = None  # type: ignore[assignment]
    info_certificado = None  # type: ignore[assignment]

try:
    from esociallib.transmissao import enviar_lote, consultar_lote, LoteResult, EventoResult
except ImportError:
    enviar_lote = None  # type: ignore[assignment]
    consultar_lote = None  # type: ignore[assignment]
    LoteResult = None  # type: ignore[assignment]
    EventoResult = None  # type: ignore[assignment]

__version__ = "1.0.0"
__author__ = "KMEE"
__all__ = [
    "to_xml",
    "generate_unsigned",
    "list_supported_events",
    "validate_xsd",
    "assinar",
    "info_certificado",
    "enviar_lote",
    "consultar_lote",
    "LoteResult",
    "EventoResult",
    "EsocialError",
    "EsocialValidationError",
    "EsocialSignatureError",
    "EsocialTransmissionError",
    "EsocialBatchError",
]
