"""Testes unitários dos builders de eventos eSocial."""
import pytest
from lxml import etree

from esociallib.builders.s_1000 import build_s1000
from esociallib.builders.s_1010 import build_s1010
from esociallib.builders.s_1020 import build_s1020
from esociallib.builders.s_1200 import build_s1200
from esociallib.builders.s_1299 import build_s1299
from esociallib.builders.s_2206 import build_s2206
from esociallib.builders.s_2230 import build_s2230
from esociallib.builders.s_2299 import build_s2299


def _assert_valid_esocial_xml(xml_str, evt_tag, namespace):
    """Verifica estrutura base de um XML eSocial."""
    assert isinstance(xml_str, str)
    assert "<?xml" in xml_str
    assert "ns0:" not in xml_str, "Não deve conter prefixo ns0:"
    assert "ns1:" not in xml_str, "Não deve conter prefixo ns1:"
    assert "xsi:type" not in xml_str, "Não deve conter xsi:type"

    root = etree.fromstring(xml_str.encode("utf-8"))
    assert root.tag == f"{{{namespace}}}eSocial"

    evt = root.find(f"{{{namespace}}}{evt_tag}")
    assert evt is not None, f"Elemento {evt_tag} não encontrado"
    assert evt.get("Id") is not None, "Id não encontrado"
    assert evt.get("Id").startswith("ID"), "Id deve começar com 'ID'"

    ide_evento = evt.find(f"{{{namespace}}}ideEvento")
    assert ide_evento is not None, "ideEvento não encontrado"

    ide_empregador = evt.find(f"{{{namespace}}}ideEmpregador")
    assert ide_empregador is not None, "ideEmpregador não encontrado"


# ── S-1000 ───────────────────────────────────────────────────────────────────

class TestS1000:
    NS = "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00"

    @pytest.fixture
    def data(self):
        return {
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

    def test_builds_valid_xml(self, data):
        xml = build_s1000(data).to_xml()
        _assert_valid_esocial_xml(xml, "evtInfoEmpregador", self.NS)

    def test_contains_info_cadastro(self, data):
        xml = build_s1000(data).to_xml()
        root = etree.fromstring(xml.encode())
        class_trib = root.find(f".//{{{self.NS}}}classTrib")
        assert class_trib is not None
        assert class_trib.text == "01"


# ── S-1010 ───────────────────────────────────────────────────────────────────

class TestS1010:
    NS = "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00"

    @pytest.fixture
    def data(self):
        return {
            "tp_insc": 1,
            "nr_insc": "12345678",
            "ini_valid": "2024-01",
            "cod_rubr": "RUB001",
            "ide_tab_rubr": "TAB1",
            "dsc_rubr": "SALARIO BASE",
            "nat_rubr": 1000,
            "tp_rubr": 1,
            "cod_inc_cp": "11",
            "cod_inc_irrf": "11",
            "cod_inc_fgts": "11",
        }

    def test_builds_valid_xml(self, data):
        xml = build_s1010(data).to_xml()
        _assert_valid_esocial_xml(xml, "evtTabRubrica", self.NS)

    def test_contains_rubrica(self, data):
        xml = build_s1010(data).to_xml()
        root = etree.fromstring(xml.encode())
        cod = root.find(f".//{{{self.NS}}}codRubr")
        assert cod is not None
        assert cod.text == "RUB001"


# ── S-1020 ───────────────────────────────────────────────────────────────────

class TestS1020:
    NS = "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00"

    @pytest.fixture
    def data(self):
        return {
            "tp_insc": 1,
            "nr_insc": "12345678",
            "ini_valid": "2024-01",
            "cod_lotacao": "LOT001",
            "tp_lotacao": "01",
            "fpas": "515",
            "cod_tercs": "0000",
        }

    def test_builds_valid_xml(self, data):
        xml = build_s1020(data).to_xml()
        _assert_valid_esocial_xml(xml, "evtTabLotacao", self.NS)

    def test_contains_lotacao(self, data):
        xml = build_s1020(data).to_xml()
        root = etree.fromstring(xml.encode())
        cod = root.find(f".//{{{self.NS}}}codLotacao")
        assert cod is not None
        assert cod.text == "LOT001"


# ── S-1200 ───────────────────────────────────────────────────────────────────

class TestS1200:
    NS = "http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_03_00"

    @pytest.fixture
    def data(self):
        return {
            "tp_insc": 1,
            "nr_insc": "12345678",
            "ind_apuracao": 1,
            "per_apur": "2024-03",
            "cpf_trab": "12345678901",
            "dm_dev": [
                {
                    "ide_dm_dev": "DM001",
                    "cod_categ": "101",
                    "info_per_apur": {
                        "ide_estab_lot": [
                            {
                                "tp_insc": 1,
                                "nr_insc": "12345678000199",
                                "cod_lotacao": "LOT001",
                                "remun_per_apur": [
                                    {
                                        "itens_remun": [
                                            {
                                                "cod_rubr": "RUB001",
                                                "ide_tab_rubr": "TAB1",
                                                "vr_rubr": "5000.00",
                                            }
                                        ],
                                    }
                                ],
                            }
                        ],
                    },
                }
            ],
        }

    def test_builds_valid_xml(self, data):
        xml = build_s1200(data).to_xml()
        _assert_valid_esocial_xml(xml, "evtRemun", self.NS)

    def test_contains_remuneracao(self, data):
        xml = build_s1200(data).to_xml()
        root = etree.fromstring(xml.encode())
        cpf = root.find(f".//{{{self.NS}}}cpfTrab")
        assert cpf is not None
        assert cpf.text == "12345678901"
        rubr = root.find(f".//{{{self.NS}}}codRubr")
        assert rubr is not None
        assert rubr.text == "RUB001"


# ── S-1299 ───────────────────────────────────────────────────────────────────

class TestS1299:
    NS = "http://www.esocial.gov.br/schema/evt/evtFechaEvPer/v_S_01_03_00"

    @pytest.fixture
    def data(self):
        return {
            "tp_insc": 1,
            "nr_insc": "12345678",
            "ind_apuracao": 1,
            "per_apur": "2024-03",
            "evt_remun": "S",
            "evt_pgtos": "N",
            "evt_aq_prod": "N",
            "evt_com_prod": "N",
            "evt_contrat_av_np": "N",
            "evt_info_compl_per": "N",
        }

    def test_builds_valid_xml(self, data):
        xml = build_s1299(data).to_xml()
        _assert_valid_esocial_xml(xml, "evtFechaEvPer", self.NS)


# ── S-2206 ───────────────────────────────────────────────────────────────────

class TestS2206:
    NS = "http://www.esocial.gov.br/schema/evt/evtAltContratual/v_S_01_03_00"

    @pytest.fixture
    def data(self):
        return {
            "tp_insc": 1,
            "nr_insc": "12345678",
            "cpf_trab": "12345678901",
            "matricula": "000123",
            "dt_alteracao": "2024-06-01",
            "tp_reg_trab": 1,
            "tp_reg_prev": 1,
            "nat_atividade": 1,
            "cnpj_sind_categ_prof": "12345678000199",
            "cod_categ": "101",
            "cod_cbo": "252105",
            "vr_sal_fx": "6000.00",
            "und_sal_fixo": 5,
        }

    def test_builds_valid_xml(self, data):
        xml = build_s2206(data).to_xml()
        _assert_valid_esocial_xml(xml, "evtAltContratual", self.NS)

    def test_contains_vinculo(self, data):
        xml = build_s2206(data).to_xml()
        root = etree.fromstring(xml.encode())
        matricula = root.find(f".//{{{self.NS}}}matricula")
        assert matricula is not None
        assert matricula.text == "000123"


# ── S-2230 ───────────────────────────────────────────────────────────────────

class TestS2230:
    NS = "http://www.esocial.gov.br/schema/evt/evtAfastTemp/v_S_01_03_00"

    @pytest.fixture
    def data(self):
        return {
            "tp_insc": 1,
            "nr_insc": "12345678",
            "cpf_trab": "12345678901",
            "matricula": "000123",
            "cod_mot_afast": "01",
            "dt_ini_afast": "2024-04-01",
        }

    def test_builds_valid_xml(self, data):
        xml = build_s2230(data).to_xml()
        _assert_valid_esocial_xml(xml, "evtAfastTemp", self.NS)

    def test_contains_afastamento(self, data):
        xml = build_s2230(data).to_xml()
        root = etree.fromstring(xml.encode())
        cod = root.find(f".//{{{self.NS}}}codMotAfast")
        assert cod is not None
        assert cod.text == "01"


# ── S-2299 ───────────────────────────────────────────────────────────────────

class TestS2299:
    NS = "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00"

    @pytest.fixture
    def data(self):
        return {
            "tp_insc": 1,
            "nr_insc": "12345678",
            "cpf_trab": "12345678901",
            "matricula": "000123",
            "dt_deslig": "2024-12-31",
            "mtv_deslig": "02",
        }

    def test_builds_valid_xml(self, data):
        xml = build_s2299(data).to_xml()
        _assert_valid_esocial_xml(xml, "evtDeslig", self.NS)

    def test_contains_desligamento(self, data):
        xml = build_s2299(data).to_xml()
        root = etree.fromstring(xml.encode())
        dt = root.find(f".//{{{self.NS}}}dtDeslig")
        assert dt is not None
        assert dt.text == "2024-12-31"
