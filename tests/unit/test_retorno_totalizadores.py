"""Testes do parsing dos eventos totalizadores (S-5001/S-5002/S-5011/S-5012)."""
from decimal import Decimal

from esociallib.retorno_totalizadores import (
    Totalizador,
    parse_totalizador,
    parse_totalizadores,
)
from esociallib.transmissao import _parsear_resultado, extrair_retornos_evento

NS_5001 = "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_03_00"
NS_5011 = "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_03_00"
NS_5002 = "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_03_00"
NS_5012 = "http://www.esocial.gov.br/schema/evt/evtIrrf/v_S_01_03_00"

S5001 = f"""<?xml version="1.0" encoding="UTF-8"?>
<eSocial xmlns="{NS_5001}">
  <evtBasesTrab Id="ID5001000000000000000000000000000001">
    <ideEvento>
      <nrRecArqBase>1.2.0000012345</nrRecArqBase>
      <indApuracao>1</indApuracao>
      <perApur>2024-03</perApur>
    </ideEvento>
    <ideEmpregador><tpInsc>1</tpInsc><nrInsc>12345678</nrInsc></ideEmpregador>
    <ideTrabalhador><cpfTrab>12345678901</cpfTrab></ideTrabalhador>
    <infoCpCalc>
      <tpCR>115601</tpCR>
      <vrCpSeg>330.00</vrCpSeg>
      <vrDescSeg>330.00</vrDescSeg>
    </infoCpCalc>
    <infoCp>
      <classTrib>01</classTrib>
      <ideEstabLot>
        <tpInsc>1</tpInsc>
        <nrInsc>12345678000199</nrInsc>
        <codLotacao>001</codLotacao>
        <infoCategIncid>
          <matricula>EMP001</matricula>
          <codCateg>101</codCateg>
          <indSimples>1</indSimples>
          <infoBaseCS>
            <ind13>0</ind13>
            <tpValor>11</tpValor>
            <valor>3000.00</valor>
          </infoBaseCS>
          <calcTerc>
            <tpCR>115801</tpCR>
            <vrCsSegTerc>172.50</vrCsSegTerc>
            <vrDescTerc>0.00</vrDescTerc>
          </calcTerc>
        </infoCategIncid>
      </ideEstabLot>
    </infoCp>
  </evtBasesTrab>
</eSocial>"""

S5011 = f"""<?xml version="1.0" encoding="UTF-8"?>
<eSocial xmlns="{NS_5011}">
  <evtCS Id="ID5011000000000000000000000000000001">
    <ideEvento><indApuracao>1</indApuracao><perApur>2024-03</perApur></ideEvento>
    <ideEmpregador><tpInsc>1</tpInsc><nrInsc>12345678</nrInsc></ideEmpregador>
    <infoCS>
      <nrRecArqBase>1.2.0000099999</nrRecArqBase>
      <indExistInfo>1</indExistInfo>
      <infoCPSeg><vrDescCP>330.00</vrDescCP><vrCpSeg>330.00</vrCpSeg></infoCPSeg>
      <ideEstab>
        <tpInsc>1</tpInsc>
        <nrInsc>12345678000199</nrInsc>
        <ideLotacao>
          <codLotacao>001</codLotacao>
          <fpas>515</fpas>
          <codTercs>0079</codTercs>
          <basesRemun>
            <indIncid>1</indIncid>
            <codCateg>101</codCateg>
            <basesCp>
              <vrBcCp00>3000.00</vrBcCp00>
              <vrSalFam>0.00</vrSalFam>
            </basesCp>
          </basesRemun>
        </ideLotacao>
        <infoCREstab>
          <tpCR>115101</tpCR>
          <vrCR>600.00</vrCR>
          <vrSuspCR>0.00</vrSuspCR>
        </infoCREstab>
      </ideEstab>
      <infoCRContrib><tpCR>115101</tpCR><vrCR>600.00</vrCR></infoCRContrib>
      <infoCRContrib><tpCR>115801</tpCR><vrCR>172.50</vrCR></infoCRContrib>
    </infoCS>
  </evtCS>
</eSocial>"""

S5002 = f"""<?xml version="1.0" encoding="UTF-8"?>
<eSocial xmlns="{NS_5002}">
  <evtIrrfBenef Id="ID5002000000000000000000000000000001">
    <ideEvento><nrRecArqBase>1.2.0000077777</nrRecArqBase><perApur>2024-03</perApur></ideEvento>
    <ideEmpregador><tpInsc>1</tpInsc><nrInsc>12345678</nrInsc></ideEmpregador>
    <ideTrabalhador>
      <cpfBenef>12345678901</cpfBenef>
      <dmDev>
        <perRef>2024-03</perRef>
        <ideDmDev>DEM000001</ideDmDev>
        <tpPgto>1</tpPgto>
        <dtPgto>2024-04-05</dtPgto>
        <codCateg>101</codCateg>
        <totApurMen>
          <CRMen>056101</CRMen>
          <vlrRendTrib>3000.00</vlrRendTrib>
          <vlrPrevOficial>330.00</vlrPrevOficial>
          <vlrCRMen>85.20</vlrCRMen>
        </totApurMen>
      </dmDev>
      <totInfoIR>
        <consolidApurMen>
          <CRMen>056101</CRMen>
          <vlrRendTrib>3000.00</vlrRendTrib>
          <vlrCRMen>85.20</vlrCRMen>
        </consolidApurMen>
      </totInfoIR>
    </ideTrabalhador>
  </evtIrrfBenef>
</eSocial>"""

S5012 = f"""<?xml version="1.0" encoding="UTF-8"?>
<eSocial xmlns="{NS_5012}">
  <evtIrrf Id="ID5012000000000000000000000000000001">
    <ideEvento><indApuracao>1</indApuracao><perApur>2024-03</perApur></ideEvento>
    <ideEmpregador><tpInsc>1</tpInsc><nrInsc>12345678</nrInsc></ideEmpregador>
    <infoIRRF>
      <nrRecArqBase>1.2.0000088888</nrRecArqBase>
      <indExistInfo>1</indExistInfo>
      <infoCRMen><CRMen>056101</CRMen><vrCRMen>85.20</vrCRMen></infoCRMen>
    </infoIRRF>
  </evtIrrf>
</eSocial>"""


# ── S-5001 ────────────────────────────────────────────────────────────────────

def test_s5001_identificacao():
    tot = parse_totalizador(S5001)
    assert isinstance(tot, Totalizador)
    assert tot.evento == "S-5001"
    assert tot.nr_rec_arq_base == "1.2.0000012345"
    assert tot.per_apur == "2024-03"
    assert tot.ind_apuracao == "1"
    assert tot.cpf_trab == "12345678901"
    assert tot.id_evento == "ID5001000000000000000000000000000001"


def test_s5001_info_cp_calc():
    tot = parse_totalizador(S5001)
    assert tot.total_grupo("info_cp_calc", "115601") == Decimal("660.00")
    descontado = [
        linha for linha in tot.linhas
        if linha.grupo == "info_cp_calc" and linha.descricao == "vrDescSeg"
    ]
    assert len(descontado) == 1
    assert descontado[0].valor == Decimal("330.00")


def test_s5001_base_cs_e_terceiros():
    tot = parse_totalizador(S5001)
    bases = [linha for linha in tot.linhas if linha.grupo == "base_cs"]
    assert len(bases) == 1
    base = bases[0]
    assert base.valor == Decimal("3000.00")
    assert base.codigo == "11"
    assert base.matricula == "EMP001"
    assert base.cod_categ == "101"
    assert base.cod_lotacao == "001"
    assert base.nr_insc == "12345678000199"
    assert tot.total_grupo("calc_terc", "115801") == Decimal("172.50")


# ── S-5011 ────────────────────────────────────────────────────────────────────

def test_s5011_cr_contrib_e_bases():
    tot = parse_totalizador(S5011)
    assert tot.evento == "S-5011"
    assert tot.nr_rec_arq_base == "1.2.0000099999"
    assert tot.ind_exist_info == "1"
    # O que vai para a DCTFWeb: soma dos códigos de receita do contribuinte.
    assert tot.total_grupo("cr_contrib") == Decimal("772.50")
    assert tot.total_grupo("cr_contrib", "115101") == Decimal("600.00")
    base_cp = [
        linha for linha in tot.linhas
        if linha.grupo == "base_cp" and linha.descricao == "vrBcCp00"
    ]
    assert len(base_cp) == 1
    assert base_cp[0].valor == Decimal("3000.00")
    assert base_cp[0].cod_lotacao == "001"
    assert tot.total_grupo("cp_seg") == Decimal("660.00")


def test_s5011_cr_estab():
    tot = parse_totalizador(S5011)
    cr_estab = [linha for linha in tot.linhas if linha.grupo == "cr_estab"]
    assert {linha.descricao for linha in cr_estab} == {"vrCR", "vrSuspCR"}
    assert all(linha.nr_insc == "12345678000199" for linha in cr_estab)


# ── S-5002 / S-5012 ───────────────────────────────────────────────────────────

def test_s5002_consolidado_e_demonstrativo():
    tot = parse_totalizador(S5002)
    assert tot.evento == "S-5002"
    assert tot.cpf_trab == "12345678901"
    # vlrCRMen aparece no consolidado e no demonstrativo: 85.20 x 2.
    crmen = [
        linha for linha in tot.linhas
        if linha.descricao == "vlrCRMen" and linha.codigo == "056101"
    ]
    assert len(crmen) == 2
    com_perref = [linha for linha in crmen if linha.per_ref == "2024-03"]
    assert len(com_perref) == 1


def test_s5012_cr_men():
    tot = parse_totalizador(S5012)
    assert tot.evento == "S-5012"
    assert tot.nr_rec_arq_base == "1.2.0000088888"
    assert tot.total_grupo("cr_men", "056101") == Decimal("85.20")


# ── Robustez ──────────────────────────────────────────────────────────────────

def test_parse_totalizadores_encontra_dentro_de_wrapper():
    """O totalizador chega embrulhado em <retornoEvento><tot>; deve ser achado."""
    wrapper = (
        '<retornoEvento xmlns="http://www.esocial.gov.br/schema/lote/eventos/'
        'envio/consulta/retornoEnvio/v1_1_1">'
        "<recibo><nrRecibo>1.2.0000012345</nrRecibo></recibo>"
        f"<tot>{S5001.split('?>', 1)[1]}</tot>"
        "</retornoEvento>"
    )
    tots = parse_totalizadores(wrapper)
    assert len(tots) == 1
    assert tots[0].evento == "S-5001"


def test_parse_totalizadores_multiplos():
    combinado = (
        "<lote>"
        + S5001.split("?>", 1)[1]
        + S5011.split("?>", 1)[1]
        + "</lote>"
    )
    tots = parse_totalizadores(combinado)
    assert [tot.evento for tot in tots] == ["S-5001", "S-5011"]


def test_parse_totalizadores_xml_invalido_nao_levanta():
    assert parse_totalizadores("nao e xml <<<") == []
    assert parse_totalizadores("") == []
    assert parse_totalizador("") is None


def test_parse_totalizadores_sem_totalizador():
    assert parse_totalizadores("<eSocial><evtRemun Id='ID1'/></eSocial>") == []


def test_valor_nao_numerico_e_ignorado():
    xml = (
        f'<eSocial xmlns="{NS_5012}"><evtIrrf Id="ID1">'
        "<ideEvento><perApur>2024-03</perApur></ideEvento>"
        "<infoIRRF><nrRecArqBase>1.2.1</nrRecArqBase>"
        "<infoCRMen><CRMen>056101</CRMen><vrCRMen>abc</vrCRMen></infoCRMen>"
        "</infoIRRF></evtIrrf></eSocial>"
    )
    tot = parse_totalizador(xml)
    assert tot.linhas == []


# ── Integração com a transmissão ──────────────────────────────────────────────

def test_extrair_retornos_evento_por_id():
    resp = (
        '<eSocial xmlns="http://www.esocial.gov.br/schema/lote/eventos/envio/'
        'consulta/retornoEnvio/v1_1_1"><retornoEventos>'
        '<evento Id="IDBASE001"><retornoEvento>'
        "<recibo><nrRecibo>1.2.0000012345</nrRecibo></recibo>"
        f"<tot>{S5001.split('?>', 1)[1]}</tot>"
        "</retornoEvento></evento>"
        "</retornoEventos></eSocial>"
    )
    retornos = extrair_retornos_evento(resp)
    assert set(retornos) == {"IDBASE001"}
    tots = parse_totalizadores(retornos["IDBASE001"])
    assert tots[0].evento == "S-5001"


def test_parsear_resultado_anexa_retorno_xml():
    resp = f"""<?xml version="1.0"?>
    <root xmlns:es="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
      <es:cdResposta>201</es:cdResposta>
      <es:ocorrencias>
        <es:ocorrencia>
          <es:id>IDBASE001</es:id>
          <es:nrRecibo>1.2.0000012345</es:nrRecibo>
          <es:cdResposta>201</es:cdResposta>
          <es:dscResposta>Sucesso</es:dscResposta>
        </es:ocorrencia>
      </es:ocorrencias>
      <es:retornoEventos>
        <es:evento Id="IDBASE001">
          <es:retornoEvento>{S5001.split("?>", 1)[1]}</es:retornoEvento>
        </es:evento>
      </es:retornoEventos>
    </root>"""
    resultado = _parsear_resultado("PROTO", resp)
    assert len(resultado.eventos) == 1
    evento = resultado.eventos[0]
    assert evento.event_id == "IDBASE001"
    assert evento.retorno_xml
    tots = parse_totalizadores(evento.retorno_xml)
    assert tots[0].nr_rec_arq_base == "1.2.0000012345"


def test_parsear_resultado_cria_evento_para_retorno_sem_ocorrencia():
    resp = f"""<?xml version="1.0"?>
    <root xmlns:es="http://www.esocial.gov.br/schema/lote/eventos/envio/consulta/retornoEnvio/v1_1_1">
      <es:cdResposta>201</es:cdResposta>
      <es:retornoEventos>
        <es:evento Id="IDBASE002">
          <es:retornoEvento>
            <es:recibo><es:nrRecibo>1.2.0000054321</es:nrRecibo></es:recibo>
            {S5011.split("?>", 1)[1]}
          </es:retornoEvento>
        </es:evento>
      </es:retornoEventos>
    </root>"""
    resultado = _parsear_resultado("PROTO", resp)
    assert len(resultado.eventos) == 1
    evento = resultado.eventos[0]
    assert evento.event_id == "IDBASE002"
    assert evento.nr_recibo == "1.2.0000054321"
    assert evento.aceito is True
    assert parse_totalizadores(evento.retorno_xml)[0].evento == "S-5011"
