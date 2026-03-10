"""Testes unitários do módulo transmissao (sem rede, tudo mockado)."""
import pytest
from unittest.mock import patch, MagicMock

from esociallib.transmissao import (
    enviar_lote,
    consultar_lote,
    LoteResult,
    EventoResult,
    MAX_EVENTOS_POR_LOTE,
    _montar_envelope_envio,
    _montar_envelope_consulta,
    _extrair_protocolo,
    _extrair_event_id,
    _parsear_resultado,
)


# ── Testes de envelope ─────────────────────────────────────────────────────────

def test_montar_envelope_envio_contains_soap_structure():
    xml = _montar_envelope_envio(["<eSocial><evt Id='ID1'/></eSocial>"], grupo=1)
    assert "soapenv:Envelope" in xml
    assert "EnviarLoteEventos" in xml
    assert 'grupo="1"' in xml


def test_montar_envelope_envio_includes_all_events():
    xmls = [
        "<eSocial><evt Id='ID1'/></eSocial>",
        "<eSocial><evt Id='ID2'/></eSocial>",
    ]
    envelope = _montar_envelope_envio(xmls, grupo=2)
    assert "ID1" in envelope
    assert "ID2" in envelope
    assert 'grupo="2"' in envelope


def test_montar_envelope_consulta_contains_protocolo():
    xml = _montar_envelope_consulta("1.2.202403.123456789")
    assert "ConsultarLoteEventos" in xml
    assert "1.2.202403.123456789" in xml


# ── Testes de parsing ──────────────────────────────────────────────────────────

def test_extrair_protocolo_from_response():
    resp = """<?xml version="1.0"?>
    <root xmlns:es="http://www.esocial.gov.br/schema/lote/eventos/envio/retornoEnvio/v1_1_1">
        <es:retornoEnvio>
            <es:protocoloEnvio>1.2.202403.000001</es:protocoloEnvio>
        </es:retornoEnvio>
    </root>"""
    assert _extrair_protocolo(resp) == "1.2.202403.000001"


def test_extrair_protocolo_raises_on_missing():
    resp = '<?xml version="1.0"?><root><nada/></root>'
    with pytest.raises(ValueError, match="protocoloEnvio não encontrado"):
        _extrair_protocolo(resp)


def test_parsear_resultado_processado():
    resp = """<?xml version="1.0"?>
    <root xmlns:es="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
        <es:retornoConsulta>
            <es:cdResposta>201</es:cdResposta>
            <es:ocorrencias>
                <es:ocorrencia>
                    <es:id>ID001</es:id>
                    <es:nrRecibo>1.2.0000001</es:nrRecibo>
                    <es:cdResposta>201</es:cdResposta>
                    <es:dscResposta>Sucesso</es:dscResposta>
                </es:ocorrencia>
            </es:ocorrencias>
        </es:retornoConsulta>
    </root>"""
    result = _parsear_resultado("PROTO001", resp)
    assert isinstance(result, LoteResult)
    assert result.status == "processado"
    assert result.protocolo == "PROTO001"
    assert len(result.eventos) == 1
    assert result.eventos[0].aceito is True
    assert result.eventos[0].nr_recibo == "1.2.0000001"


def test_parsear_resultado_em_processamento():
    resp = """<?xml version="1.0"?>
    <root xmlns:es="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
        <es:retornoConsulta>
            <es:cdResposta>101</es:cdResposta>
        </es:retornoConsulta>
    </root>"""
    result = _parsear_resultado("PROTO002", resp)
    assert result.status == "em_processamento"
    assert result.eventos == []


def test_parsear_resultado_erro():
    resp = """<?xml version="1.0"?>
    <root xmlns:es="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
        <es:retornoConsulta>
            <es:cdResposta>301</es:cdResposta>
        </es:retornoConsulta>
    </root>"""
    result = _parsear_resultado("PROTO003", resp)
    assert result.status == "erro"


# ── Testes de extração de Id ───────────────────────────────────────────────────

def test_extrair_event_id_from_xml():
    xml = '<eSocial xmlns="http://x"><evtAdmissao Id="ID12345"/></eSocial>'
    assert _extrair_event_id(xml) == "ID12345"


def test_extrair_event_id_fallback():
    assert _extrair_event_id("<broken") == "evt001"


# ── Testes de validação de lote ────────────────────────────────────────────────

def test_enviar_lote_rejects_more_than_max():
    xmls = ["<xml/>"] * (MAX_EVENTOS_POR_LOTE + 1)
    with pytest.raises(ValueError, match="excede"):
        enviar_lote(xmls, cert_pfx=b"fake", cert_password="pwd")


@patch("esociallib.transmissao.TransmissaoSOAP")
def test_enviar_lote_calls_transmissao(mock_soap_cls):
    mock_instance = MagicMock()
    mock_soap_cls.return_value = mock_instance
    mock_instance.enviar.return_value = """<?xml version="1.0"?>
    <r xmlns:es="http://www.esocial.gov.br/schema/lote/eventos/envio/retornoEnvio/v1_1_1">
        <es:protocoloEnvio>1.2.2024.001</es:protocoloEnvio>
    </r>"""

    proto = enviar_lote(
        ["<eSocial><evt Id='ID1'/></eSocial>"],
        cert_pfx=b"cert",
        cert_password="pwd",
        environment="restricted",
    )
    assert proto == "1.2.2024.001"
    mock_soap_cls.assert_called_once_with(cert_pfx=b"cert", cert_password="pwd")
    mock_instance.enviar.assert_called_once()


@patch("esociallib.transmissao.TransmissaoSOAP")
def test_consultar_lote_returns_lote_result(mock_soap_cls):
    mock_instance = MagicMock()
    mock_soap_cls.return_value = mock_instance
    mock_instance.enviar.return_value = """<?xml version="1.0"?>
    <r xmlns:es="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
        <es:cdResposta>201</es:cdResposta>
    </r>"""

    result = consultar_lote(
        "PROTO001",
        cert_pfx=b"cert",
        cert_password="pwd",
    )
    assert isinstance(result, LoteResult)
    assert result.status == "processado"


# ── Testes dos dataclasses ─────────────────────────────────────────────────────

def test_evento_result_defaults():
    er = EventoResult(event_id="ID001")
    assert er.aceito is False
    assert er.nr_recibo is None


def test_lote_result_defaults():
    lr = LoteResult(protocolo="P001", status="processado")
    assert lr.eventos == []
