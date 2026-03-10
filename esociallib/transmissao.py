"""
transmissao.py — Transmissão de lotes eSocial via SOAP 1.1.

Wrapper sobre erpbrasil.transmissao configurado com os endpoints
e envelopes SOAP específicos do eSocial S-1.3.

Fluxo assíncrono obrigatório desde 22/07/2024:
  1. enviar_lote()    → retorna protocolo
  2. consultar_lote() → retorna BatchResult (polling até processado)
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from xml.sax.saxutils import escape as xml_escape

from erpbrasil.transmissao import TransmissaoSOAP
from lxml import etree

logger = logging.getLogger(__name__)

MAX_EVENTOS_POR_LOTE = 50

_ENDPOINTS = {
    "production": {
        "envio": (
            "https://webservices.envio.esocial.gov.br"
            "/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc"
        ),
        "consulta": (
            "https://webservices.consulta.esocial.gov.br"
            "/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc"
        ),
    },
    "restricted": {
        "envio": (
            "https://webservices.producaorestrita.esocial.gov.br"
            "/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc"
        ),
        "consulta": (
            "https://webservices.producaorestrita.esocial.gov.br"
            "/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc"
        ),
    },
}

_SOAP_ACTION_ENVIO = (
    "http://www.esocial.gov.br/servicos/empregador"
    "/enviarloteeventos/EnviarLoteEventos"
)
_SOAP_ACTION_CONSULTA = (
    "http://www.esocial.gov.br/servicos/empregador"
    "/consultarloteeventos/ConsultarLoteEventos"
)


@dataclass
class EventoResult:
    event_id: str
    nr_recibo: str | None = None
    code: str | None = None
    description: str | None = None
    aceito: bool = False


@dataclass
class LoteResult:
    protocolo: str
    status: str  # "processado" | "em_processamento" | "erro"
    eventos: list[EventoResult] = field(default_factory=list)


def enviar_lote(
    xmls_assinados: list[str],
    cert_pfx: bytes,
    cert_password: str,
    environment: str = "restricted",
    grupo: int = 1,
) -> str:
    """
    Envia um lote de eventos assinados para o eSocial.

    :param xmls_assinados: Lista de XMLs assinados (máx. 50).
    :param cert_pfx: Certificado ICP-Brasil A1 em PKCS#12.
    :param cert_password: Senha do certificado.
    :param environment: 'production' ou 'restricted'.
    :param grupo: 1=tabelas, 2=não-periódicos, 3=periódicos.
    :returns: Protocolo de envio.
    :raises: ValueError se mais de 50 eventos.
    """
    if len(xmls_assinados) > MAX_EVENTOS_POR_LOTE:
        raise ValueError(
            f"Lote excede {MAX_EVENTOS_POR_LOTE} eventos. "
            f"Recebidos: {len(xmls_assinados)}."
        )

    url = _ENDPOINTS[environment]["envio"]
    envelope = _montar_envelope_envio(xmls_assinados, grupo)

    logger.info(
        "Enviando lote %d evento(s) → %s (grupo=%d)",
        len(xmls_assinados), environment, grupo,
    )

    transmissao = TransmissaoSOAP(
        cert_pfx=cert_pfx,
        cert_password=cert_password,
    )
    resposta = transmissao.enviar(
        url=url,
        xml=envelope,
        soap_action=_SOAP_ACTION_ENVIO,
    )

    protocolo = _extrair_protocolo(resposta)
    logger.info("Lote enviado. Protocolo: %s", protocolo)
    return protocolo


def consultar_lote(
    protocolo: str,
    cert_pfx: bytes,
    cert_password: str,
    environment: str = "restricted",
) -> LoteResult:
    """
    Consulta o resultado de um lote enviado.

    :param protocolo: Retornado por enviar_lote().
    :returns: LoteResult com status e lista de EventoResult.
    """
    url = _ENDPOINTS[environment]["consulta"]
    envelope = _montar_envelope_consulta(protocolo)

    logger.info("Consultando protocolo %s em %s", protocolo, environment)

    transmissao = TransmissaoSOAP(
        cert_pfx=cert_pfx,
        cert_password=cert_password,
    )
    resposta = transmissao.enviar(
        url=url,
        xml=envelope,
        soap_action=_SOAP_ACTION_CONSULTA,
    )

    return _parsear_resultado(protocolo, resposta)


# ── Helpers internos ──────────────────────────────────────────────────────────

def _montar_envelope_envio(xmls: list[str], grupo: int) -> str:
    eventos_xml = "\n".join(
        f'<evento Id="{_extrair_event_id(xml)}">{xml}</evento>'
        for xml in xmls
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:v1="http://www.esocial.gov.br/servicos/empregador/enviarloteeventos/v1_1_0">
  <soapenv:Header/>
  <soapenv:Body>
    <v1:EnviarLoteEventos>
      <v1:loteEventos>
        <eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/v1_1_1">
          <envioLoteEventos grupo="{grupo}">
            <eventos>{eventos_xml}</eventos>
          </envioLoteEventos>
        </eSocial>
      </v1:loteEventos>
    </v1:EnviarLoteEventos>
  </soapenv:Body>
</soapenv:Envelope>"""


def _montar_envelope_consulta(protocolo: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:v1="http://www.esocial.gov.br/servicos/empregador/consultarloteeventos/v1_1_0">
  <soapenv:Header/>
  <soapenv:Body>
    <v1:ConsultarLoteEventos>
      <v1:consulta>
        <eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
          <download>
            <protocoloEnvio>{xml_escape(protocolo)}</protocoloEnvio>
          </download>
        </eSocial>
      </v1:consulta>
    </v1:ConsultarLoteEventos>
  </soapenv:Body>
</soapenv:Envelope>"""


def _extrair_protocolo(resposta_xml: str) -> str:
    raw = resposta_xml.encode("utf-8") if isinstance(resposta_xml, str) else resposta_xml
    root = etree.fromstring(raw)
    ns = {"es": "http://www.esocial.gov.br/schema/lote/eventos/envio/retornoEnvio/v1_1_1"}
    el = root.find(".//es:protocoloEnvio", ns)
    if el is not None and el.text:
        return el.text.strip()
    raise ValueError(f"protocoloEnvio não encontrado na resposta:\n{resposta_xml[:300]}")


def _parsear_resultado(protocolo: str, resposta_xml: str) -> LoteResult:
    raw = resposta_xml.encode("utf-8") if isinstance(resposta_xml, str) else resposta_xml
    root = etree.fromstring(raw)
    ns = {"es": "http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1"}

    cd_el = root.find(".//es:cdResposta", ns)
    cd = cd_el.text.strip() if cd_el is not None else "000"

    if cd == "201":
        status = "processado"
    elif cd.startswith("1"):
        status = "em_processamento"
    else:
        status = "erro"

    eventos = []
    for oc in root.findall(".//es:ocorrencias/es:ocorrencia", ns):
        def _txt(tag):
            el = oc.find(f"es:{tag}", ns)
            return el.text.strip() if el is not None and el.text else None

        code = _txt("cdResposta")
        eventos.append(EventoResult(
            event_id=_txt("id") or "",
            nr_recibo=_txt("nrRecibo"),
            code=code,
            description=_txt("dscResposta"),
            aceito=(code == "201"),
        ))

    return LoteResult(protocolo=protocolo, status=status, eventos=eventos)


def _extrair_event_id(xml: str) -> str:
    try:
        root = etree.fromstring(xml.encode("utf-8"))
        for child in root:
            id_val = child.get("Id")
            if id_val:
                return id_val
    except Exception:
        logger.warning("Falha ao extrair Id do evento XML")
    logger.warning("Id não encontrado no evento, usando fallback 'evt001'")
    return "evt001"
