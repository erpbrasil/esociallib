"""Fixtures compartilhadas entre todos os testes."""
import pytest
from erpbrasil.assinatura.misc import create_fake_certificate_file


@pytest.fixture(scope="session")
def fake_cert():
    """Certificado PKCS#12 fake (válido) para testes de assinatura."""
    return create_fake_certificate_file(
        valid=True,
        passwd="teste123",
        issuer="ESOCIALLIB TEST CA",
        country="BR",
        subject="ESOCIALLIB TESTE:12345678000199",
    )


@pytest.fixture(scope="session")
def fake_cert_password():
    return "teste123"


@pytest.fixture(scope="session")
def fake_cert_expired():
    """Certificado fake expirado — para testar rejeição."""
    return create_fake_certificate_file(
        valid=False,
        passwd="teste123",
        issuer="ESOCIALLIB TEST CA",
        country="BR",
        subject="ESOCIALLIB TESTE EXPIRADO:12345678000199",
    )
