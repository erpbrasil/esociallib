"""Testes de integração: builder → XML → validação XSD real.

Cada builder gera XML que deve passar na validação XSD oficial,
exceto pelo elemento <Signature> (adicionado pela assinatura).
"""
import pytest
from esociallib.validators import validate_xsd


def _validate_ignoring_signature(xml: str, event_type: str) -> list[str]:
    """Valida XML contra XSD, ignorando erros de Signature ausente."""
    errors = validate_xsd(xml, event_type)
    return [e for e in errors if "Signature" not in e]


class TestS1000XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_1000 import build_s1000
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "ini_valid": "2024-01", "class_trib": "01",
            "ind_coop": 0, "ind_constr": 0, "ind_des_folha": 0,
            "ind_opt_reg_eletron": 0, "ind_ent_ed": "N", "ind_ett": "N",
            "nm_razao": "EMPRESA TESTE LTDA", "nat_jur": "2062", "ind_sit_pj": 0,
        }
        xml = build_s1000(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-1000")
        assert errors == [], f"Erros XSD: {errors}"


class TestS1010XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_1010 import build_s1010
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "ini_valid": "2024-01", "cod_rubr": "RUB001",
            "ide_tab_rubr": "TAB1", "dsc_rubr": "SALARIO BASE",
            "nat_rubr": 1000, "tp_rubr": 1,
            "cod_inc_cp": "11", "cod_inc_irrf": "11", "cod_inc_fgts": "11",
        }
        xml = build_s1010(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-1010")
        assert errors == [], f"Erros XSD: {errors}"


class TestS1020XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_1020 import build_s1020
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "ini_valid": "2024-01", "cod_lotacao": "LOT001",
            "tp_lotacao": "01", "fpas": "515", "cod_tercs": "0000",
        }
        xml = build_s1020(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-1020")
        assert errors == [], f"Erros XSD: {errors}"


class TestS2200XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_2200 import build_s2200
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "cpf_trab": "12345678901", "nm_trab": "JOAO DA SILVA",
            "sexo": "M", "raca_cor": 1, "grau_instr": "07",
            "dt_nascto": "1980-01-15", "matricula": "000123",
            "tp_reg_trab": 1, "tp_reg_prev": 1, "dt_adm": "2024-03-01",
            "nat_atividade": 1, "cnpj_sind_categ_prof": "12345678000199",
            "cod_categ": "101", "vr_sal_fx": "5000.00", "und_sal_fixo": 5,
        }
        xml = build_s2200(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-2200")
        assert errors == [], f"Erros XSD: {errors}"


class TestS1200XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_1200 import build_s1200
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "ind_apuracao": 1, "per_apur": "2024-03",
            "cpf_trab": "12345678901",
            "dm_dev": [{
                "ide_dm_dev": "DM001", "cod_categ": "101",
                "info_per_apur": {
                    "ide_estab_lot": [{
                        "tp_insc": 1, "nr_insc": "12345678000199",
                        "cod_lotacao": "LOT001",
                        "remun_per_apur": [{
                            "itens_remun": [{
                                "cod_rubr": "RUB001",
                                "ide_tab_rubr": "TAB1",
                                "vr_rubr": "5000.00",
                            }],
                        }],
                    }],
                },
            }],
        }
        xml = build_s1200(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-1200")
        assert errors == [], f"Erros XSD: {errors}"


class TestS1299XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_1299 import build_s1299
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "ind_apuracao": 1, "per_apur": "2024-03",
            "evt_remun": "S", "evt_pgtos": "N", "evt_aq_prod": "N",
            "evt_com_prod": "N", "evt_contrat_av_np": "N",
            "evt_info_compl_per": "N",
        }
        xml = build_s1299(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-1299")
        assert errors == [], f"Erros XSD: {errors}"


class TestS2206XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_2206 import build_s2206
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "cpf_trab": "12345678901", "matricula": "000123",
            "dt_alteracao": "2024-06-01", "tp_reg_trab": 1,
            "tp_reg_prev": 1, "nat_atividade": 1,
            "cnpj_sind_categ_prof": "12345678000199",
            "cod_categ": "101", "vr_sal_fx": "6000.00", "und_sal_fixo": 5,
        }
        xml = build_s2206(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-2206")
        assert errors == [], f"Erros XSD: {errors}"


class TestS2230XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_2230 import build_s2230
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "cpf_trab": "12345678901", "matricula": "000123",
            "cod_mot_afast": "01", "dt_ini_afast": "2024-04-01",
        }
        xml = build_s2230(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-2230")
        assert errors == [], f"Erros XSD: {errors}"


class TestS2299XsdValidation:
    def test_valid(self):
        from esociallib.builders.s_2299 import build_s2299
        data = {
            "tp_insc": 1, "nr_insc": "12345678000199",
            "cpf_trab": "12345678901", "matricula": "000123",
            "dt_deslig": "2024-12-31", "mtv_deslig": "02",
        }
        xml = build_s2299(data).to_xml()
        errors = _validate_ignoring_signature(xml, "S-2299")
        assert errors == [], f"Erros XSD: {errors}"
