"""
Builder para S-1005 — Tabela de Estabelecimentos, Obras ou Unidades de Orgaos Publicos.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1005 e um evento de tabela com operacoes de inclusao, alteracao ou exclusao.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00"


@register_builder("S-1005")
def build_s1005(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1005 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                       # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",              # CNPJ raiz (8 digitos) ou CPF

            # operacao: "inclusao", "alteracao" ou "exclusao"
            "operacao": "inclusao",

            # ideEstab
            "tp_insc_estab": 1,                 # 1=CNPJ, 3=CAEPF, 4=CNO
            "nr_insc_estab": "12345678000199",  # Numero de inscricao do estabelecimento
            "ini_valid": "2024-01",             # YYYY-MM
            "fim_valid": "2099-12",             # YYYY-MM (opcional)

            # dadosEstab (obrigatorio para inclusao/alteracao)
            "cnae_prep": "4751201",             # CNAE preponderante
            "cnpj_resp": "12345678000199",      # CNPJ responsavel (opcional, para CNO)

            # aliqGilrat (opcional)
            "aliq_rat": 1,                      # Aliquota RAT (opcional)
            "fap": "1.0000",                    # FAP (opcional)
            "proc_adm_jud_rat": {               # Processo RAT (opcional)
                "tp_proc": 1,
                "nr_proc": "12345678901234567",
                "cod_susp": "12345678901234",
            },
            "proc_adm_jud_fap": {               # Processo FAP (opcional)
                "tp_proc": 1,
                "nr_proc": "12345678901234567",
                "cod_susp": "12345678901234",
            },

            # infoCaepf (obrigatorio se tp_insc_estab=3)
            "tp_caepf": 1,                      # 1=Contrib individual, 2=Prod rural, 3=Seg especial

            # infoObra (obrigatorio se construtora e CNO)
            "ind_subst_patr_obra": 1,           # Indicativo substituicao patronal

            # infoTrab (opcional)
            "info_apr": {                       # Informacoes aprendiz (opcional)
                "nr_proc_jud": "12345678901234567890",
                "info_ent_educ": [              # Entidades educativas (opcional)
                    {"nr_insc": "12345678000199"},
                ],
            },
            "info_pcd": {                       # Informacoes PCD (opcional)
                "nr_proc_jud": "12345678901234567890",
            },

            # novaValidade (apenas para alteracao, opcional)
            "nova_ini_valid": "2024-03",        # YYYY-MM (opcional)
            "nova_fim_valid": "2099-12",        # YYYY-MM (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtTabEstab", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_evtTab_inicial: tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # infoEstab
    info_estab = sub(evt, "infoEstab")

    operacao = data.get("operacao", "inclusao")

    if operacao == "inclusao":
        inclusao = sub(info_estab, "inclusao")
        _build_ide_estab(inclusao, data)
        _build_dados_estab(inclusao, data)

    elif operacao == "alteracao":
        alteracao = sub(info_estab, "alteracao")
        _build_ide_estab(alteracao, data)
        _build_dados_estab(alteracao, data)

        # novaValidade (opcional)
        if data.get("nova_ini_valid"):
            nova_validade = sub(alteracao, "novaValidade")
            sub(nova_validade, "iniValid", str(data["nova_ini_valid"]))
            if data.get("nova_fim_valid"):
                sub(nova_validade, "fimValid", str(data["nova_fim_valid"]))

    elif operacao == "exclusao":
        exclusao = sub(info_estab, "exclusao")
        _build_ide_estab(exclusao, data)

    return EventoXml(root, _NAMESPACE)


def _build_ide_estab(parent, data: dict) -> None:
    """Constroi o grupo ideEstab (T_ideEstab)."""
    ide_estab = sub(parent, "ideEstab")
    sub(ide_estab, "tpInsc", str(data["tp_insc_estab"]))
    sub(ide_estab, "nrInsc", str(data["nr_insc_estab"]))
    sub(ide_estab, "iniValid", str(data["ini_valid"]))
    if data.get("fim_valid"):
        sub(ide_estab, "fimValid", str(data["fim_valid"]))


def _build_dados_estab(parent, data: dict) -> None:
    """Constroi o grupo dadosEstab (T_dadosEstab)."""
    dados_estab = sub(parent, "dadosEstab")
    sub(dados_estab, "cnaePrep", str(data["cnae_prep"]))

    if data.get("cnpj_resp"):
        sub(dados_estab, "cnpjResp", str(data["cnpj_resp"]))

    # aliqGilrat (opcional)
    if data.get("aliq_rat") is not None or data.get("fap") is not None or \
       data.get("proc_adm_jud_rat") or data.get("proc_adm_jud_fap"):
        aliq_gilrat = sub(dados_estab, "aliqGilrat")

        if data.get("aliq_rat") is not None:
            sub(aliq_gilrat, "aliqRat", str(data["aliq_rat"]))
        if data.get("fap") is not None:
            sub(aliq_gilrat, "fap", str(data["fap"]))

        # procAdmJudRat (opcional)
        if data.get("proc_adm_jud_rat"):
            proc = data["proc_adm_jud_rat"]
            proc_rat = sub(aliq_gilrat, "procAdmJudRat")
            sub(proc_rat, "tpProc", str(proc["tp_proc"]))
            sub(proc_rat, "nrProc", str(proc["nr_proc"]))
            sub(proc_rat, "codSusp", str(proc["cod_susp"]))

        # procAdmJudFap (opcional)
        if data.get("proc_adm_jud_fap"):
            proc = data["proc_adm_jud_fap"]
            proc_fap = sub(aliq_gilrat, "procAdmJudFap")
            sub(proc_fap, "tpProc", str(proc["tp_proc"]))
            sub(proc_fap, "nrProc", str(proc["nr_proc"]))
            sub(proc_fap, "codSusp", str(proc["cod_susp"]))

    # infoCaepf (opcional, obrigatorio se tp_insc_estab=3)
    if data.get("tp_caepf") is not None:
        info_caepf = sub(dados_estab, "infoCaepf")
        sub(info_caepf, "tpCaepf", str(data["tp_caepf"]))

    # infoObra (opcional, obrigatorio se construtora e CNO)
    if data.get("ind_subst_patr_obra") is not None:
        info_obra = sub(dados_estab, "infoObra")
        sub(info_obra, "indSubstPatrObra", str(data["ind_subst_patr_obra"]))

    # infoTrab (opcional)
    if data.get("info_apr") or data.get("info_pcd"):
        info_trab = sub(dados_estab, "infoTrab")

        # infoApr (opcional)
        if data.get("info_apr"):
            apr = data["info_apr"]
            info_apr = sub(info_trab, "infoApr")
            if apr.get("nr_proc_jud"):
                sub(info_apr, "nrProcJud", str(apr["nr_proc_jud"]))
            if apr.get("info_ent_educ"):
                for ent in apr["info_ent_educ"]:
                    info_ent_educ = sub(info_apr, "infoEntEduc")
                    sub(info_ent_educ, "nrInsc", str(ent["nr_insc"]))

        # infoPCD (opcional)
        if data.get("info_pcd"):
            pcd = data["info_pcd"]
            info_pcd = sub(info_trab, "infoPCD")
            sub(info_pcd, "nrProcJud", str(pcd["nr_proc_jud"]))
