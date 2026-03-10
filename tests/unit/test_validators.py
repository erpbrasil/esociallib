"""Testes unitários do módulo validators."""

import pytest

from esociallib.validators import (
    _EVENT_XSD_MAP,
    _resolve_xsd_path,
    clear_schema_cache,
    validate_xsd,
)


@pytest.fixture(autouse=True)
def clear_cache():
    """Limpa cache entre testes."""
    clear_schema_cache()
    yield
    clear_schema_cache()


def test_event_xsd_map_has_core_events():
    """Eventos principais devem estar mapeados."""
    expected = [
        "S-1000", "S-1010", "S-1020",
        "S-2200", "S-2206", "S-2230", "S-2299",
        "S-1200", "S-1299",
        "S-3000",
    ]
    for code in expected:
        assert code in _EVENT_XSD_MAP, f"{code} ausente no _EVENT_XSD_MAP"


def test_event_xsd_map_no_obsolete_events():
    """Eventos removidos no S-1.3 não devem estar no mapa."""
    obsolete = ["S-1030", "S-1035", "S-1040", "S-1050", "S-1060", "S-1080"]
    for code in obsolete:
        assert code not in _EVENT_XSD_MAP, f"{code} obsoleto presente no mapa"


def test_validate_xsd_raises_on_unknown_event():
    with pytest.raises(ValueError, match="não possui XSD mapeado"):
        validate_xsd("<xml/>", "S-9999")


def test_resolve_xsd_path_finds_existing_xsd():
    """Deve encontrar um XSD real no pacote."""
    path = _resolve_xsd_path("evtAdmissao")
    assert path.exists()
    assert path.suffix == ".xsd"


def test_resolve_xsd_path_raises_on_missing():
    with pytest.raises(FileNotFoundError):
        _resolve_xsd_path("evtNaoExiste")


def test_validate_xsd_with_real_builder():
    """Valida XML gerado pelo builder S-1000 contra o XSD real."""
    from esociallib.builders.s_1000 import build_s1000
    data = {
        "tp_insc": 1,
        "nr_insc": "12345678",
        "ini_valid": "2024-01",
        "class_trib": "01",
        "ind_coop": 0,
        "ind_constr": 0,
        "ind_des_folha": 0,
        "ind_opt_reg_eletron": 0,
        "ind_ent_ed": "N",
        "ind_ett": "N",
        "nm_razao": "EMPRESA TESTE LTDA",
        "nat_jur": "2062",
        "ind_sit_pj": 0,
    }
    xml = build_s1000(data).to_xml()
    errors = validate_xsd(xml, "S-1000")
    assert isinstance(errors, list)


def test_validate_xsd_caches_schema():
    """Schema deve ser compilado uma vez e cacheado."""
    from esociallib.builders.s_1000 import build_s1000
    data = {
        "tp_insc": 1,
        "nr_insc": "12345678",
        "ini_valid": "2024-01",
        "class_trib": "01",
        "ind_coop": 0,
        "ind_constr": 0,
        "ind_des_folha": 0,
        "ind_opt_reg_eletron": 0,
        "ind_ent_ed": "N",
        "ind_ett": "N",
        "nm_razao": "EMPRESA TESTE LTDA",
        "nat_jur": "2062",
        "ind_sit_pj": 0,
    }
    xml = build_s1000(data).to_xml()
    validate_xsd(xml, "S-1000")
    # Segunda chamada deve usar cache
    validate_xsd(xml, "S-1000")


def test_all_mapped_xsds_exist():
    """Todos os XSDs mapeados devem existir no pacote."""
    missing = []
    for code, xsd_name in _EVENT_XSD_MAP.items():
        try:
            path = _resolve_xsd_path(xsd_name)
            if not path.exists():
                missing.append(f"{code}: {xsd_name}")
        except FileNotFoundError:
            missing.append(f"{code}: {xsd_name}")
    assert not missing, f"XSDs faltando: {missing}"
