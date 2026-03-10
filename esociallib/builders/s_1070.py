"""
Builder para S-1070 — Tabela de Processos Administrativos/Judiciais.

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-1070 e um evento de tabela com operacoes de inclusao, alteracao ou exclusao.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00"


@register_builder("S-1070")
def build_s1070(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-1070 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                       # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",              # CNPJ raiz (8 digitos) ou CPF

            # operacao: "inclusao", "alteracao" ou "exclusao"
            "operacao": "inclusao",

            # ideProcesso
            "tp_proc": 1,                       # 1=Administrativo, 2=Judicial, 4=FAP
            "nr_proc": "12345678901234567",     # Numero do processo
            "ini_valid": "2024-01",             # YYYY-MM
            "fim_valid": "2099-12",             # YYYY-MM (opcional)

            # dadosProc (obrigatorio para inclusao/alteracao)
            "ind_autoria": 1,                   # 1=Proprio contribuinte, 2=Outra (opcional, obrig se tpProc=2)
            "ind_mat_proc": 1,                  # 1=Tributaria, 7=FGTS
            "observacao": "Obs do processo",    # Observacao (opcional)

            # dadosProcJud (obrigatorio se tpProc=2 e indMatProc=1)
            "uf_vara": "SP",                    # UF da vara
            "cod_munic": 3550308,               # Codigo do municipio
            "id_vara": 1,                       # Codigo da vara

            # infoSusp (obrigatorio se indMatProc=1, ate 99 ocorrencias)
            "info_susp": [
                {
                    "cod_susp": "12345678901234",   # Codigo da suspensao
                    "ind_susp": "01",               # Indicativo de suspensao
                    "dt_decisao": "2024-01-15",     # Data da decisao
                    "ind_deposito": "N",            # S/N deposito montante integral
                },
            ],

            # novaValidade (apenas para alteracao, opcional)
            "nova_ini_valid": "2024-03",        # YYYY-MM (opcional)
            "nova_fim_valid": "2099-12",        # YYYY-MM (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtTabProcesso", event_id, _NAMESPACE)

    # ideEvento (T_ideEvento_evtTab: tpAmb, procEmi, verProc)
    ide_evento = sub(evt, "ideEvento")
    sub(ide_evento, "tpAmb", str(tp_amb))
    sub(ide_evento, "procEmi", str(data.get("proc_emi", 1)))
    sub(ide_evento, "verProc", data.get("ver_proc", "esociallib_1.0"))

    # ideEmpregador (T_ideEmpregador)
    ide_empregador = sub(evt, "ideEmpregador")
    sub(ide_empregador, "tpInsc", str(data["tp_insc"]))
    sub(ide_empregador, "nrInsc", str(data["nr_insc"]))

    # infoProcesso
    info_processo = sub(evt, "infoProcesso")

    operacao = data.get("operacao", "inclusao")

    if operacao == "inclusao":
        inclusao = sub(info_processo, "inclusao")
        _build_ide_processo(inclusao, data)
        _build_dados_proc(inclusao, data)

    elif operacao == "alteracao":
        alteracao = sub(info_processo, "alteracao")
        _build_ide_processo(alteracao, data)
        _build_dados_proc(alteracao, data)

        # novaValidade (opcional)
        if data.get("nova_ini_valid"):
            nova_validade = sub(alteracao, "novaValidade")
            sub(nova_validade, "iniValid", str(data["nova_ini_valid"]))
            if data.get("nova_fim_valid"):
                sub(nova_validade, "fimValid", str(data["nova_fim_valid"]))

    elif operacao == "exclusao":
        exclusao = sub(info_processo, "exclusao")
        _build_ide_processo(exclusao, data)

    return EventoXml(root, _NAMESPACE)


def _build_ide_processo(parent, data: dict) -> None:
    """Constroi o grupo ideProcesso (T_ideProcesso)."""
    ide_processo = sub(parent, "ideProcesso")
    sub(ide_processo, "tpProc", str(data["tp_proc"]))
    sub(ide_processo, "nrProc", str(data["nr_proc"]))
    sub(ide_processo, "iniValid", str(data["ini_valid"]))
    if data.get("fim_valid"):
        sub(ide_processo, "fimValid", str(data["fim_valid"]))


def _build_dados_proc(parent, data: dict) -> None:
    """Constroi o grupo dadosProc (T_dadosProc)."""
    dados_proc = sub(parent, "dadosProc")

    if data.get("ind_autoria") is not None:
        sub(dados_proc, "indAutoria", str(data["ind_autoria"]))

    sub(dados_proc, "indMatProc", str(data["ind_mat_proc"]))

    if data.get("observacao"):
        sub(dados_proc, "observacao", str(data["observacao"]))

    # dadosProcJud (obrigatorio se tpProc=2 e indMatProc=1)
    if data.get("uf_vara"):
        dados_proc_jud = sub(dados_proc, "dadosProcJud")
        sub(dados_proc_jud, "ufVara", str(data["uf_vara"]))
        sub(dados_proc_jud, "codMunic", str(data["cod_munic"]))
        sub(dados_proc_jud, "idVara", str(data["id_vara"]))

    # infoSusp (obrigatorio se indMatProc=1, ate 99 ocorrencias)
    if data.get("info_susp"):
        for susp in data["info_susp"]:
            info_susp = sub(dados_proc, "infoSusp")
            sub(info_susp, "codSusp", str(susp["cod_susp"]))
            sub(info_susp, "indSusp", str(susp["ind_susp"]))
            sub(info_susp, "dtDecisao", str(susp["dt_decisao"]))
            sub(info_susp, "indDeposito", str(susp["ind_deposito"]))
