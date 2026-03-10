"""
Builder para S-2210 -- Comunicacao de Acidente de Trabalho (CAT).

Este modulo recebe o dict montado pelo mapper do sped_esocial (Odoo)
e retorna um EventoXml pronto para serializacao.

O S-2210 e um evento nao-periodico que registra a Comunicacao de
Acidente de Trabalho, incluindo informacoes sobre o acidente, local,
parte atingida, agente causador e atestado medico.
"""

from __future__ import annotations

from esociallib.builders.xml_builder import EventoXml, make_esocial, sub
from esociallib.generator import register_builder
from esociallib.utils.id_generator import generate_event_id

_NAMESPACE = "http://www.esocial.gov.br/schema/evt/evtCAT/v_S_01_03_00"


@register_builder("S-2210")
def build_s2210(data: dict, environment: str = "restricted") -> EventoXml:
    """
    Constroi o XML do evento S-2210 a partir do dict do mapper Odoo.

    :param data: Dicionario com os campos do evento. Estrutura esperada:

        {
            # ideEmpregador
            "tp_insc": 1,                   # 1=CNPJ, 2=CPF
            "nr_insc": "12345678",          # CNPJ raiz (8 digitos) ou CPF

            # ideVinculo (T_ideVinculo_sst)
            "cpf_trab": "12345678901",
            "matricula": "000123",          # Opcional (TSVE sem matricula)
            "cod_categ": "101",             # Opcional (TSVE sem matricula)

            # cat
            "dt_acid": "2024-06-15",        # Data do acidente
            "tp_acid": 1,                   # 1=Tipico, 2=Doenca, 3=Trajeto
            "hr_acid": "1430",              # Hora do acidente HHMM (opcional)
            "hrs_trab_antes_acid": "0600",  # Horas trabalhadas antes HHMM (opcional)
            "tp_cat": 1,                    # 1=Inicial, 2=Reabertura, 3=Obito
            "ind_cat_obito": "N",           # S ou N
            "dt_obito": None,               # Data do obito (se ind_cat_obito=S)
            "ind_comun_policia": "N",       # S ou N
            "cod_sit_geradora": "200004300", # Codigo situacao geradora (Tabela 15)
            "iniciat_cat": 1,               # 1=Empregador, 2=Judicial, 3=Fiscal
            "obs_cat": None,                # Observacao (opcional)
            "ult_dia_trab": None,           # Ultimo dia trabalhado (opcional)
            "houve_afast": None,            # S ou N (opcional)

            # localAcidente
            "tp_local": 1,                  # 1-6,9 Tipo de local
            "dsc_local": None,              # Especificacao do local (opcional)
            "tp_lograd": None,              # Tipo logradouro (opcional)
            "dsc_lograd": "RUA DAS FLORES", # Descricao logradouro
            "nr_lograd": "100",             # Numero logradouro
            "complemento_local": None,      # Complemento (opcional)
            "bairro_local": None,           # Bairro (opcional)
            "cep_local": "01001000",        # CEP (opcional)
            "cod_munic_local": "3550308",   # Codigo municipio (opcional)
            "uf_local": "SP",               # UF (opcional)
            "pais_local": None,             # Codigo pais (opcional, se exterior)
            "cod_postal_local": None,       # Codigo postal (opcional, se exterior)

            # ideLocalAcid (opcional)
            "tp_insc_local": None,          # Tipo inscricao local (opcional)
            "nr_insc_local": None,          # Nr inscricao local (opcional)

            # parteAtingida
            "cod_parte_ating": "753010000",  # Codigo parte atingida (Tabela 13)
            "lateralidade": 0,              # 0=N/A, 1=Esq, 2=Dir, 3=Ambas

            # agenteCausador
            "cod_agnt_causador": "302010300", # Codigo agente causador (Tabela 14)

            # atestado
            "dt_atendimento": "2024-06-15", # Data do atendimento
            "hr_atendimento": "1500",       # Hora do atendimento HHMM
            "ind_internacao": "N",          # S ou N
            "dur_trat": "15",               # Duracao tratamento em dias
            "ind_afast": "S",               # S ou N
            "dsc_lesao": "702010200",       # Natureza da lesao (Tabela 17)
            "dsc_comp_lesao": None,         # Descricao complementar (opcional)
            "diag_provavel": None,          # Diagnostico provavel (opcional)
            "cod_cid": "S610",              # Codigo CID
            "observacao_atestado": None,    # Observacao (opcional)

            # emitente
            "nm_emit": "DR JOAO",           # Nome medico/dentista
            "ide_oc": 1,                    # 1=CRM, 2=CRO, 3=RMS
            "nr_oc": "123456",              # Nr inscricao orgao classe
            "uf_oc": "SP",                  # UF orgao classe (opcional)

            # catOrigem (obrigatorio se tp_cat=2 ou 3)
            "nr_rec_cat_orig": None,        # Nr recibo CAT anterior (opcional)
        }

    :param environment: 'production' ou 'restricted'.
    :returns: EventoXml pronto para to_xml().
    """
    tp_amb = 1 if environment == "production" else 2
    event_id = generate_event_id(data["tp_insc"], data["nr_insc"])

    root, evt = make_esocial("evtCAT", event_id, _NAMESPACE)

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

    # ideVinculo (T_ideVinculo_sst: cpfTrab, matricula?, codCateg?)
    ide_vinculo = sub(evt, "ideVinculo")
    sub(ide_vinculo, "cpfTrab", str(data["cpf_trab"]))
    if data.get("matricula"):
        sub(ide_vinculo, "matricula", str(data["matricula"]))
    if data.get("cod_categ") is not None and not data.get("matricula"):
        sub(ide_vinculo, "codCateg", str(data["cod_categ"]))

    # cat
    cat = sub(evt, "cat")
    sub(cat, "dtAcid", str(data["dt_acid"]))
    sub(cat, "tpAcid", str(data["tp_acid"]))
    if data.get("hr_acid"):
        sub(cat, "hrAcid", str(data["hr_acid"]))
    if data.get("hrs_trab_antes_acid"):
        sub(cat, "hrsTrabAntesAcid", str(data["hrs_trab_antes_acid"]))
    sub(cat, "tpCat", str(data["tp_cat"]))
    sub(cat, "indCatObito", str(data["ind_cat_obito"]))
    if data.get("dt_obito"):
        sub(cat, "dtObito", str(data["dt_obito"]))
    sub(cat, "indComunPolicia", str(data["ind_comun_policia"]))
    sub(cat, "codSitGeradora", str(data["cod_sit_geradora"]))
    sub(cat, "iniciatCAT", str(data["iniciat_cat"]))
    if data.get("obs_cat"):
        sub(cat, "obsCAT", str(data["obs_cat"]))
    if data.get("ult_dia_trab"):
        sub(cat, "ultDiaTrab", str(data["ult_dia_trab"]))
    if data.get("houve_afast") is not None:
        sub(cat, "houveAfast", str(data["houve_afast"]))

    # localAcidente
    local_acidente = sub(cat, "localAcidente")
    sub(local_acidente, "tpLocal", str(data["tp_local"]))
    if data.get("dsc_local"):
        sub(local_acidente, "dscLocal", str(data["dsc_local"]))
    if data.get("tp_lograd"):
        sub(local_acidente, "tpLograd", str(data["tp_lograd"]))
    sub(local_acidente, "dscLograd", str(data["dsc_lograd"]))
    sub(local_acidente, "nrLograd", str(data["nr_lograd"]))
    if data.get("complemento_local"):
        sub(local_acidente, "complemento", str(data["complemento_local"]))
    if data.get("bairro_local"):
        sub(local_acidente, "bairro", str(data["bairro_local"]))
    if data.get("cep_local"):
        sub(local_acidente, "cep", str(data["cep_local"]))
    if data.get("cod_munic_local"):
        sub(local_acidente, "codMunic", str(data["cod_munic_local"]))
    if data.get("uf_local"):
        sub(local_acidente, "uf", str(data["uf_local"]))
    if data.get("pais_local"):
        sub(local_acidente, "pais", str(data["pais_local"]))
    if data.get("cod_postal_local"):
        sub(local_acidente, "codPostal", str(data["cod_postal_local"]))

    # ideLocalAcid (opcional)
    if data.get("tp_insc_local") is not None:
        ide_local_acid = sub(local_acidente, "ideLocalAcid")
        sub(ide_local_acid, "tpInsc", str(data["tp_insc_local"]))
        sub(ide_local_acid, "nrInsc", str(data["nr_insc_local"]))

    # parteAtingida
    parte_atingida = sub(cat, "parteAtingida")
    sub(parte_atingida, "codParteAting", str(data["cod_parte_ating"]))
    sub(parte_atingida, "lateralidade", str(data["lateralidade"]))

    # agenteCausador
    agente_causador = sub(cat, "agenteCausador")
    sub(agente_causador, "codAgntCausador", str(data["cod_agnt_causador"]))

    # atestado
    atestado = sub(cat, "atestado")
    sub(atestado, "dtAtendimento", str(data["dt_atendimento"]))
    sub(atestado, "hrAtendimento", str(data["hr_atendimento"]))
    sub(atestado, "indInternacao", str(data["ind_internacao"]))
    sub(atestado, "durTrat", str(data["dur_trat"]))
    sub(atestado, "indAfast", str(data["ind_afast"]))
    sub(atestado, "dscLesao", str(data["dsc_lesao"]))
    if data.get("dsc_comp_lesao"):
        sub(atestado, "dscCompLesao", str(data["dsc_comp_lesao"]))
    if data.get("diag_provavel"):
        sub(atestado, "diagProvavel", str(data["diag_provavel"]))
    sub(atestado, "codCID", str(data["cod_cid"]))
    if data.get("observacao_atestado"):
        sub(atestado, "observacao", str(data["observacao_atestado"]))

    # emitente
    emitente = sub(atestado, "emitente")
    sub(emitente, "nmEmit", str(data["nm_emit"]))
    sub(emitente, "ideOC", str(data["ide_oc"]))
    sub(emitente, "nrOC", str(data["nr_oc"]))
    if data.get("uf_oc"):
        sub(emitente, "ufOC", str(data["uf_oc"]))

    # catOrigem (obrigatorio se tp_cat=2 ou 3)
    if data.get("nr_rec_cat_orig"):
        cat_origem = sub(cat, "catOrigem")
        sub(cat_origem, "nrRecCatOrig", str(data["nr_rec_cat_orig"]))

    return EventoXml(root, _NAMESPACE)
