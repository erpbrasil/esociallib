"""Testes unitários das exceções."""
import pytest
from esociallib.exceptions import (
    EsocialValidationError,
    EsocialSignatureError,
    EsocialTransmissionError,
    EsocialBatchError,
)


def test_validation_error_formats_message():
    erros = ["Linha 5: campo obrigatório ausente", "Linha 12: valor inválido"]
    exc = EsocialValidationError(errors=erros, event_type="S-2200")
    assert "S-2200" in str(exc)
    assert "campo obrigatório ausente" in str(exc)
    assert exc.errors == erros
    assert exc.event_type == "S-2200"


def test_transmission_error_stores_status():
    exc = EsocialTransmissionError("timeout", status_code=503, response_body="<html>")
    assert exc.status_code == 503
    assert exc.response_body == "<html>"


def test_batch_error_stores_rejections():
    rejections = [{"event_id": "evt1", "code": "401", "msg": "não autorizado"}]
    exc = EsocialBatchError(protocol="1234567890", rejections=rejections)
    assert exc.protocol == "1234567890"
    assert len(exc.rejections) == 1


def test_all_errors_inherit_from_base():
    from esociallib.exceptions import EsocialError
    assert issubclass(EsocialValidationError, EsocialError)
    assert issubclass(EsocialSignatureError, EsocialError)
    assert issubclass(EsocialTransmissionError, EsocialError)
    assert issubclass(EsocialBatchError, EsocialError)
