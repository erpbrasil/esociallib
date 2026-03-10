"""
Builder para S-1010 — Tabela de Rubricas.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1010 e um evento de tabela com operacoes de inclusao, alteracao ou exclusao
de rubricas usadas na folha de pagamento.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00"


@register_builder("S-1010")
def build_s1010(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1010 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # operacao: "inclusao", "alteracao" ou "exclusao"
            "operacao": "inclusao",

            # ideRubrica
            "cod_rubr": "RUBR001",          # Codigo da rubrica
            "ide_tab_rubr": "TAB1",         # Identificador da tabela de rubricas
            "ini_valid": "2024-01",         # YYYY-MM
            "fim_valid": "2099-12",         # YYYY-MM (opcional)

            # dadosRubrica (obrigatorio para inclusao/alteracao)
            "dsc_rubr": "Salario Base",     # Descricao da rubrica
            "nat_rubr": 1000,               # Natureza da rubrica (Tabela 03)
            "tp_rubr": 1,                   # 1=Vencimento, 2=Desconto, 3=Info, 4=Info dedutora
            "cod_inc_cp": "11",             # Incidencia CP (Tabela eSocial)
            "cod_inc_irrf": 11,             # Incidencia IRRF (Tabela 21)
            "cod_inc_fgts": "11",           # Incidencia FGTS

            # opcionais
            "cod_inc_cprp": "00",           # Incidencia RPPS (opcional)
            "cod_inc_pis_pasep": "00",      # Incidencia PIS/PASEP (opcional)
            "teto_remun": "N",              # Compoe teto remuneratorio (S/N, opcional)
            "observacao": "",               # Observacao (opcional)

            # novaValidade (apenas para alteracao, opcional)
            "nova_ini_valid": "2024-03",    # YYYY-MM (opcional)
            "nova_fim_valid": "2099-12",    # YYYY-MM (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtTabRubrica", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_evtTab: tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # infoRubrica
    info_rubrica = sub(evt, "infoRubrica")

    operacao = data.get("operacao", "inclusao")

    if operacao == "inclusao":
        inclusao = sub(info_rubrica, "inclusao")
        _build_ide_rubrica(inclusao, data)
        _build_dados_rubrica(inclusao, data)

    elif operacao == "alteracao":
        alteracao = sub(info_rubrica, "alteracao")
        _build_ide_rubrica(alteracao, data)
        _build_dados_rubrica(alteracao, data)

        # novaValidade (opcional)
        if data.get("nova_ini_valid"):
            nova_validade = sub(alteracao, "novaValidade")
            sub(nova_validade, "iniValid", str(data["nova_ini_valid"]))
            if data.get("nova_fim_valid"):
                sub(nova_validade, "fimValid", str(data["nova_fim_valid"]))

    elif operacao == "exclusao":
        exclusao = sub(info_rubrica, "exclusao")
        _build_ide_rubrica(exclusao, data)

    return EventoXml(root, _NAMESPACE)


def _build_ide_rubrica(parent, data: dict) -> None:
    """Constroi o grupo ideRubrica."""
    ide_rubrica = sub(parent, "ideRubrica")
    sub(ide_rubrica, "codRubr", str(data["cod_rubr"]))
    sub(ide_rubrica, "ideTabRubr", str(data["ide_tab_rubr"]))
    sub(ide_rubrica, "iniValid", str(data["ini_valid"]))
    if data.get("fim_valid"):
        sub(ide_rubrica, "fimValid", str(data["fim_valid"]))


def _build_dados_rubrica(parent, data: dict) -> None:
    """Constroi o grupo dadosRubrica."""
    dados_rubrica = sub(parent, "dadosRubrica")
    sub(dados_rubrica, "dscRubr", str(data["dsc_rubr"]))
    sub(dados_rubrica, "natRubr", str(data["nat_rubr"]))
    sub(dados_rubrica, "tpRubr", str(data["tp_rubr"]))
    sub(dados_rubrica, "codIncCP", str(data["cod_inc_cp"]))
    sub(dados_rubrica, "codIncIRRF", str(data["cod_inc_irrf"]))
    sub(dados_rubrica, "codIncFGTS", str(data["cod_inc_fgts"]))
    if data.get("cod_inc_cprp") is not None:
        sub(dados_rubrica, "codIncCPRP", str(data["cod_inc_cprp"]))
    if data.get("cod_inc_pis_pasep") is not None:
        sub(dados_rubrica, "codIncPisPasep", str(data["cod_inc_pis_pasep"]))
    if data.get("teto_remun"):
        sub(dados_rubrica, "tetoRemun", str(data["teto_remun"]))
    if data.get("observacao"):
        sub(dados_rubrica, "observacao", str(data["observacao"]))
