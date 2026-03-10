"""
Builder para S-2230 — Afastamento Temporario.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2230 e um evento nao-periodico que registra inicio e/ou termino
de afastamentos temporarios como ferias, doenca, licencas, etc.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtAfastTemp/v_S_01_03_00"


@register_builder("S-2230")
def build_s2230(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2230 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideVinculo (nota: S-2230 usa cpfTrab + matricula + codCateg)
            "cpf_trab": "12345678901",
            "matricula": "000123",          # Opcional (obrigatorio se nao for TSVE sem matricula)
            "cod_categ": "101",             # Opcional (obrigatorio se TSVE sem matricula)

            # infoAfastamento
            # -- iniAfastamento (obrigatorio se nao houver fimAfastamento)
            "dt_ini_afast": "2024-06-01",   # Data inicio do afastamento
            "cod_mot_afast": "15",          # Codigo motivo (Tabela 18): 15=ferias, 01=doenca, etc.
            "info_mesmo_mtv": None,         # S ou N (opcional, para doenca)
            "tp_acid_transito": None,       # 1,2,3 (opcional, para acidente transito)
            "observacao": None,             # Observacao (opcional)

            # -- perAquis (opcional, para ferias cod_mot_afast=15)
            "per_aquis_dt_inicio": "2023-06-01",    # Inicio periodo aquisitivo (opcional)
            "per_aquis_dt_fim": "2024-05-31",       # Fim periodo aquisitivo (opcional)

            # -- infoCessao (obrigatorio se cod_mot_afast=14)
            "cnpj_cess": None,              # CNPJ do cessionario (opcional)
            "inf_onus": None,               # 1=Cedente, 2=Cessionario, 3=Ambos (opcional)

            # -- fimAfastamento (opcional; obrigatorio se nao houver iniAfastamento)
            "dt_term_afast": None,          # Data termino do afastamento (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtAfastTemp", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_trab: indRetif, nrRecibo, tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "indRetif", str(data.get("ind_retif", 1)))
    if data.get("nr_recibo"):
        sub(ide_evento, "nrRecibo", str(data["nr_recibo"]))
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # ideVinculo (S-2230 usa cpfTrab + matricula opcional + codCateg opcional)
    ide_vinculo = sub(evt, "ideVinculo")
    sub(ide_vinculo, "cpfTrab", str(data["cpf_trab"]))
    if data.get("matricula"):
        sub(ide_vinculo, "matricula", str(data["matricula"]))
    if data.get("cod_categ") is not None and not data.get("matricula"):
        sub(ide_vinculo, "codCateg", str(data["cod_categ"]))

    # infoAfastamento
    info_afastamento = sub(evt, "infoAfastamento")

    # iniAfastamento
    if data.get("dt_ini_afast"):
        ini_afastamento = sub(info_afastamento, "iniAfastamento")
        sub(ini_afastamento, "dtIniAfast", str(data["dt_ini_afast"]))
        sub(ini_afastamento, "codMotAfast", str(data["cod_mot_afast"]))
        if data.get("info_mesmo_mtv") is not None:
            sub(ini_afastamento, "infoMesmoMtv", str(data["info_mesmo_mtv"]))
        if data.get("tp_acid_transito") is not None:
            sub(ini_afastamento, "tpAcidTransito", str(data["tp_acid_transito"]))
        if data.get("observacao"):
            sub(ini_afastamento, "observacao", str(data["observacao"]))

        # perAquis (para ferias)
        if data.get("per_aquis_dt_inicio"):
            per_aquis = sub(ini_afastamento, "perAquis")
            sub(per_aquis, "dtInicio", str(data["per_aquis_dt_inicio"]))
            if data.get("per_aquis_dt_fim"):
                sub(per_aquis, "dtFim", str(data["per_aquis_dt_fim"]))

        # infoCessao (para cessao/requisicao, codMotAfast=14)
        if data.get("cnpj_cess"):
            info_cessao = sub(ini_afastamento, "infoCessao")
            sub(info_cessao, "cnpjCess", str(data["cnpj_cess"]))
            sub(info_cessao, "infOnus", str(data["inf_onus"]))

        # infoMandSind (para mandato sindical, codMotAfast=24)
        if data.get("cnpj_sind"):
            info_mand_sind = sub(ini_afastamento, "infoMandSind")
            sub(info_mand_sind, "cnpjSind", str(data["cnpj_sind"]))
            sub(info_mand_sind, "infOnusRemun", str(data["inf_onus_remun"]))

    # fimAfastamento
    if data.get("dt_term_afast"):
        fim_afastamento = sub(info_afastamento, "fimAfastamento")
        sub(fim_afastamento, "dtTermAfast", str(data["dt_term_afast"]))

    return EventoXml(root, _NAMESPACE)
