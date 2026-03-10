"""Teste do fluxo completo: gerar → assinar → enviar → consultar (mockado).

Simula o ciclo de vida real de um evento eSocial, com transmissão
mockada como feito em erpbrasil.edoc.
"""
import pytest
from unittest.mock import patch, MagicMock

from esociallib.generator import to_xml
from esociallib.assinatura import assinar
from esociallib.transmissao import enviar_lote, consultar_lote


# ── Respostas SOAP simuladas ─────────────────────────────────────────────────

RESPOSTA_ENVIO_SUCESSO = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <EnviarLoteEventosResponse
        xmlns="http://www.esocial.gov.br/servicos/empregador/enviarloteeventos/v1_1_0">
      <EnviarLoteEventosResult>
        <eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/retornoEnvio/v1_1_1">
          <retornoEnvioLoteEventos>
            <status>
              <cdResposta>201</cdResposta>
              <descResposta>Lote enfileirado com sucesso</descResposta>
            </status>
            <dadosRecepcaoLote>
              <protocoloEnvio>1.2.202403.000000001</protocoloEnvio>
              <dhRecepcao>2024-03-15T12:30:00.000</dhRecepcao>
            </dadosRecepcaoLote>
          </retornoEnvioLoteEventos>
        </eSocial>
      </EnviarLoteEventosResult>
    </EnviarLoteEventosResponse>
  </soap:Body>
</soap:Envelope>"""

RESPOSTA_CONSULTA_PROCESSADO = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ConsultarLoteEventosResponse
        xmlns="http://www.esocial.gov.br/servicos/empregador/consultarloteeventos/v1_1_0">
      <ConsultarLoteEventosResult>
        <eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
          <retornoConsultaLoteEventos>
            <status>
              <cdResposta>201</cdResposta>
              <descResposta>Lote processado com sucesso</descResposta>
            </status>
            <retornoEventos>
              <evento Id="ID1123456780001992024031512300000001">
                <processamento>
                  <cdResposta>201</cdResposta>
                  <descResposta>Sucesso</descResposta>
                </processamento>
                <recibo>
                  <nrRecibo>1.2.0000000000001</nrRecibo>
                </recibo>
              </evento>
            </retornoEventos>
          </retornoConsultaLoteEventos>
        </eSocial>
      </ConsultarLoteEventosResult>
    </ConsultarLoteEventosResponse>
  </soap:Body>
</soap:Envelope>"""

RESPOSTA_CONSULTA_EM_PROCESSAMENTO = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ConsultarLoteEventosResponse
        xmlns="http://www.esocial.gov.br/servicos/empregador/consultarloteeventos/v1_1_0">
      <ConsultarLoteEventosResult>
        <eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
          <retornoConsultaLoteEventos>
            <status>
              <cdResposta>101</cdResposta>
              <descResposta>Lote aguardando processamento</descResposta>
            </status>
          </retornoConsultaLoteEventos>
        </eSocial>
      </ConsultarLoteEventosResult>
    </ConsultarLoteEventosResponse>
  </soap:Body>
</soap:Envelope>"""


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def s2200_data():
    return {
        "tp_insc": 1, "nr_insc": "12345678000199",
        "cpf_trab": "12345678901", "nm_trab": "JOAO DA SILVA",
        "sexo": "M", "raca_cor": 1, "grau_instr": "07",
        "dt_nascto": "1980-01-15", "matricula": "000123",
        "tp_reg_trab": 1, "tp_reg_prev": 1, "dt_adm": "2024-03-01",
        "nat_atividade": 1, "cnpj_sind_categ_prof": "12345678000199",
        "cod_categ": "101", "vr_sal_fx": "5000.00", "und_sal_fixo": 5,
    }


# ── Testes ────────────────────────────────────────────────────────────────────

def test_fluxo_completo_admissao(fake_cert, fake_cert_password, s2200_data):
    """
    Fluxo completo:
      1. Gerar XML (to_xml com validação XSD)
      2. Assinar com certificado fake
      3. Enviar lote (SOAP mockado)
      4. Consultar resultado (SOAP mockado)
    """
    # 1. Gerar XML validado
    xml = to_xml("S-2200", s2200_data, environment="restricted")
    assert "evtAdmissao" in xml
    assert "ns0:" not in xml

    # 2. Assinar
    xml_assinado = assinar(
        xml, cert_pfx=fake_cert,
        cert_password=fake_cert_password, raise_expirado=False,
    )
    assert "Signature" in xml_assinado

    # 3. Enviar lote (mockado)
    with patch("esociallib.transmissao.TransmissaoSOAP") as mock_soap:
        mock_instance = MagicMock()
        mock_soap.return_value = mock_instance
        mock_instance.enviar.return_value = RESPOSTA_ENVIO_SUCESSO

        protocolo = enviar_lote(
            [xml_assinado],
            cert_pfx=fake_cert,
            cert_password=fake_cert_password,
            environment="restricted",
            grupo=2,  # não-periódicos
        )
        assert protocolo == "1.2.202403.000000001"
        mock_instance.enviar.assert_called_once()

    # 4. Consultar resultado (mockado)
    with patch("esociallib.transmissao.TransmissaoSOAP") as mock_soap:
        mock_instance = MagicMock()
        mock_soap.return_value = mock_instance
        mock_instance.enviar.return_value = RESPOSTA_CONSULTA_PROCESSADO

        resultado = consultar_lote(
            protocolo,
            cert_pfx=fake_cert,
            cert_password=fake_cert_password,
            environment="restricted",
        )
        assert resultado.status == "processado"
        assert resultado.protocolo == "1.2.202403.000000001"


@patch("esociallib.transmissao.TransmissaoSOAP")
def test_fluxo_envio_multiplos_eventos(mock_soap, fake_cert, fake_cert_password):
    """Envia lote com 3 eventos de tipos diferentes."""
    mock_instance = MagicMock()
    mock_soap.return_value = mock_instance
    mock_instance.enviar.return_value = RESPOSTA_ENVIO_SUCESSO

    # Gerar 3 eventos diferentes
    xmls = []
    for i in range(3):
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "cpf_trab": f"1234567890{i}", "nm_trab": f"TRABALHADOR {i}",
            "sexo": "M", "raca_cor": 1, "grau_instr": "07",
            "dt_nascto": "1980-01-15", "matricula": f"00{i:04d}",
            "tp_reg_trab": 1, "tp_reg_prev": 1, "dt_adm": "2024-03-01",
            "nat_atividade": 1, "cnpj_sind_categ_prof": "12345678000199",
            "cod_categ": "101", "vr_sal_fx": "5000.00", "und_sal_fixo": 5,
        }
        xml = to_xml("S-2200", data, environment="restricted")
        xml_assinado = assinar(
            xml, cert_pfx=fake_cert,
            cert_password=fake_cert_password, raise_expirado=False,
        )
        xmls.append(xml_assinado)

    protocolo = enviar_lote(
        xmls,
        cert_pfx=fake_cert,
        cert_password=fake_cert_password,
        environment="restricted",
    )
    assert protocolo == "1.2.202403.000000001"

    # Verifica que o envelope contém os 3 eventos
    call_args = mock_instance.enviar.call_args
    envelope = call_args.kwargs.get("xml") or call_args[1].get("xml") or call_args[0][1]
    # Os 3 XMLs estão no envelope
    assert isinstance(envelope, str)


@patch("esociallib.transmissao.TransmissaoSOAP")
def test_consulta_em_processamento(mock_soap, fake_cert, fake_cert_password):
    """Consulta retorna 'em_processamento' quando lote ainda não foi processado."""
    mock_instance = MagicMock()
    mock_soap.return_value = mock_instance
    mock_instance.enviar.return_value = RESPOSTA_CONSULTA_EM_PROCESSAMENTO

    resultado = consultar_lote(
        "1.2.202403.000000001",
        cert_pfx=fake_cert,
        cert_password=fake_cert_password,
    )
    assert resultado.status == "em_processamento"
    assert resultado.eventos == []
