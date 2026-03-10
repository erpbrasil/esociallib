"""
assinatura.py — Assinatura digital de eventos eSocial.

Wrapper fino sobre erpbrasil.assinatura, configurado com os
parâmetros obrigatórios do eSocial S-1.3:
  - Algoritmo: RSA-SHA1 (governo exige SHA1, não SHA256)
  - Canonicalização: C14N 1.0
  - Reference URI: atributo Id do elemento raiz do evento
  - Posição <Signature>: último filho de <eSocial>
"""

from __future__ import annotations

from erpbrasil.assinatura import Assinatura as _Assinatura
from erpbrasil.assinatura import Certificado as _Certificado


def assinar(
    xml_str: str,
    cert_pfx: bytes,
    cert_password: str,
    raise_expirado: bool = True,
) -> str:
    """
    Assina um XML eSocial com certificado ICP-Brasil A1.

    :param xml_str: String XML do evento (saída de to_xml()).
    :param cert_pfx: Bytes do certificado PKCS#12 (.pfx / .p12) ou base64.
    :param cert_password: Senha do certificado.
    :param raise_expirado: Se True, rejeita certificado expirado.
    :returns: String XML com <Signature> inserida.
    """
    cert = _Certificado(
        arquivo=cert_pfx,
        senha=cert_password,
        raise_expirado=raise_expirado,
    )
    assinatura = _Assinatura(cert)
    # erpbrasil.assinatura espera bytes e retorna bytes
    xml_bytes = xml_str.encode("utf-8") if isinstance(xml_str, str) else xml_str
    signed_bytes = assinatura.assina_xml(xml_bytes)
    return signed_bytes.decode("utf-8") if isinstance(signed_bytes, bytes) else signed_bytes


def info_certificado(
    cert_pfx: bytes,
    cert_password: str,
    raise_expirado: bool = False,
) -> dict:
    """
    Retorna informações do certificado (validade, CN, etc).

    Útil para exibir dados do certificado no Odoo.
    """
    cert = _Certificado(
        arquivo=cert_pfx,
        senha=cert_password,
        raise_expirado=raise_expirado,
    )
    return {
        "subject": cert.proprietario or "",
        "issuer": cert.emissor or "",
        "valid_from": str(cert.inicio_validade) if cert.inicio_validade else "",
        "valid_until": str(cert.fim_validade) if cert.fim_validade else "",
        "expired": cert.expirado,
    }
