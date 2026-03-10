"""
validators.py — Validação XSD dos eventos eSocial.

Usa os XSDs oficiais bundled no pacote (esociallib/esocial/schemas/v_s13/).
"""

from __future__ import annotations

import importlib.resources
import logging
from pathlib import Path

from lxml import etree

logger = logging.getLogger(__name__)

# Mapa: código de evento → nome do arquivo XSD (sem extensão)
# Atualizar ao adicionar novos eventos.
_EVENT_XSD_MAP: dict[str, str] = {
    # ── Tabelas ────────────────────────────────────────────────────────────────
    "S-1000": "evtInfoEmpregador",
    "S-1005": "evtTabEstab",
    "S-1010": "evtTabRubrica",
    "S-1020": "evtTabLotacao",
    "S-1070": "evtTabProcesso",
    # ── Não-periódicos ─────────────────────────────────────────────────────────
    "S-2190": "evtAdmPrelim",
    "S-2200": "evtAdmissao",
    "S-2205": "evtAltCadastral",
    "S-2206": "evtAltContratual",
    "S-2210": "evtCAT",
    "S-2220": "evtMonit",
    "S-2221": "evtToxic",
    "S-2230": "evtAfastTemp",
    "S-2240": "evtExpRisco",
    "S-2298": "evtReintegr",
    "S-2299": "evtDeslig",
    "S-2300": "evtTSVInicio",
    "S-2306": "evtTSVAltContr",
    "S-2399": "evtTSVTermino",
    "S-2400": "evtCdBenefIn",
    "S-2405": "evtCdBenefAlt",
    "S-2410": "evtCdBenIn",
    "S-2416": "evtCdBenAlt",
    "S-2418": "evtReativBen",
    "S-2420": "evtCessao",
    "S-2500": "evtProcTrab",
    # ── Periódicos ─────────────────────────────────────────────────────────────
    "S-1200": "evtRemun",
    "S-1202": "evtRmnRPPS",
    "S-1207": "evtBenPrRP",
    "S-1210": "evtPgtos",
    "S-1260": "evtComProd",
    "S-1270": "evtContratAvNP",
    "S-1280": "evtInfoComplPer",
    "S-1298": "evtReabreEvPer",
    "S-1299": "evtFechaEvPer",
    # ── Exclusão ───────────────────────────────────────────────────────────────
    "S-3000": "evtExclusao",
    "S-3500": "evtExcProcTrab",
    # ── Totalizadores (retorno do governo — úteis para deserialização) ─────────
    "S-5001": "evtBasesTrab",
    "S-5002": "evtIrrf",
    "S-5003": "evtBasesFGTS",
    "S-5011": "evtCS",
    "S-5012": "evtIrrfBenef",
    "S-5013": "evtFGTS",
}

# Cache de schemas compilados (evita recompilar em cada chamada)
_schema_cache: dict[str, etree.XMLSchema] = {}


def validate_xsd(xml_str: str, event_type: str) -> list[str]:
    """
    Valida um XML contra o XSD oficial do evento.

    :param xml_str: String XML a validar.
    :param event_type: Código do evento (ex: 'S-2200').
    :returns: Lista de strings de erro (vazia se válido).
    :raises: ValueError se o evento não tiver XSD mapeado.
    """
    xsd_name = _EVENT_XSD_MAP.get(event_type)
    if not xsd_name:
        raise ValueError(
            f"Evento '{event_type}' não possui XSD mapeado em _EVENT_XSD_MAP. "
            "Adicione a entrada antes de validar."
        )

    schema = _get_schema(xsd_name)
    xml_doc = etree.fromstring(xml_str.encode("utf-8"))
    schema.validate(xml_doc)

    errors = [
        f"Linha {e.line}: {e.message}"
        for e in schema.error_log
    ]
    if errors:
        logger.warning(
            "Validação XSD falhou para %s (%d erro(s))", event_type, len(errors)
        )
    return errors


def _get_schema(xsd_name: str) -> etree.XMLSchema:
    """Retorna XMLSchema compilado, usando cache."""
    if xsd_name not in _schema_cache:
        xsd_path = _resolve_xsd_path(xsd_name)
        logger.debug("Compilando schema XSD: %s", xsd_path)
        _schema_cache[xsd_name] = etree.XMLSchema(etree.parse(str(xsd_path)))
    return _schema_cache[xsd_name]


def _resolve_xsd_path(xsd_name: str) -> Path:
    """Localiza o XSD no pacote instalado via importlib.resources."""
    try:
        pkg = importlib.resources.files("esociallib.esocial.schemas.v_s13")
        resource = pkg / f"{xsd_name}.xsd"
        # Usa joinpath para obter o path real — funciona tanto em editable
        # installs (path no disco) quanto em wheel/zip (extrai para temp).
        # Para editable, resource já é um Path real.
        path = Path(str(resource))
        if not path.exists():
            raise FileNotFoundError
        return path
    except (FileNotFoundError, TypeError) as exc:
        raise FileNotFoundError(
            f"XSD '{xsd_name}.xsd' não encontrado em esociallib/esocial/schemas/v_s13/. "
            "Baixe os XSDs oficiais de https://www.gov.br/esocial/pt-br/documentacao-tecnica "
            "e coloque-os nesse diretório."
        ) from exc


def clear_schema_cache() -> None:
    """Limpa o cache de schemas (útil em testes)."""
    _schema_cache.clear()
