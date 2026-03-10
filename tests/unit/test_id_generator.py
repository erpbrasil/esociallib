"""Testes unitários do gerador de IDs de evento."""
import pytest
from esociallib.utils.id_generator import generate_event_id, reset_counters


@pytest.fixture(autouse=True)
def clean_counters():
    reset_counters()
    yield
    reset_counters()


def test_id_starts_with_id_prefix():
    id_ = generate_event_id(1, "12345678")
    assert id_.startswith("ID"), "Id deve começar com 'ID'"


def test_id_exact_length_36():
    id_ = generate_event_id(1, "12345678")
    assert len(id_) == 36, f"Id deve ter exatamente 36 chars, tem {len(id_)}: {id_}"


def test_id_matches_pattern():
    """ID + 34 dígitos (padrão oficial eSocial)."""
    id_ = generate_event_id(1, "12345678")
    assert id_[:2] == "ID"
    assert id_[2:].isdigit(), f"Após 'ID' deve ser só dígitos: {id_}"


def test_id_contains_tp_insc():
    id_ = generate_event_id(1, "12345678")
    assert id_[2] == "1"  # tpInsc = 1


def test_id_contains_nr_insc():
    id_ = generate_event_id(1, "12345678")
    # nrInsc padded to 14 digits at position 3..16
    assert id_[3:17] == "12345678000000"


def test_ids_are_unique():
    ids = [generate_event_id(1, "12345678") for _ in range(100)]
    assert len(set(ids)) == 100, "IDs devem ser únicos"


def test_different_inscricoes_different_ids():
    id_cnpj = generate_event_id(1, "12345678000199")
    reset_counters()
    id_cpf = generate_event_id(2, "12345678901")
    assert id_cnpj[2] == "1"
    assert id_cpf[2] == "2"
    assert id_cnpj[3:17] != id_cpf[3:17]


def test_no_special_chars():
    id_ = generate_event_id(1, "12345678")
    assert id_.isalnum(), f"Id contém caracteres inválidos: {id_!r}"
