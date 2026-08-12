"""
retorno_totalizadores.py — Parsing dos eventos totalizadores devolvidos pelo eSocial.

Os eventos totalizadores (S-5001, S-5002, S-5011, S-5012, S-5003, S-5013) nao sao
gerados pelo empregador: eles voltam do governo como resposta ao processamento de
um evento base (S-1200, S-1210, S-1299, ...) e sao a fonte oficial do que foi
apurado e enviado para a DCTFWeb/FGTS Digital.

Este modulo faz APENAS o parsing: recebe o XML devolvido (o envelope completo do
retorno, o grupo <tot>, ou o proprio evento totalizador isolado) e devolve
dataclasses simples. Persistencia e conferencia sao responsabilidade do
consumidor (por exemplo o modulo l10n_br_esocial do Odoo).

O parsing e agnostico de namespace: os elementos sao localizados por local-name,
porque o wrapper do retorno muda entre consulta de lote, consulta por
identificador e download de eventos, e a versao do namespace muda a cada leiaute.

Uso basico::

    from esociallib.retorno_totalizadores import parse_totalizadores

    for tot in parse_totalizadores(xml_retorno):
        print(tot.evento, tot.per_apur, tot.nr_rec_arq_base)
        for linha in tot.linhas:
            print(linha.grupo, linha.codigo, linha.valor)
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation

from lxml import etree

logger = logging.getLogger(__name__)

# Elemento-raiz de cada evento totalizador -> codigo do evento.
TOTALIZADOR_ROOTS = {
    "evtBasesTrab": "S-5001",
    "evtIrrfBenef": "S-5002",
    "evtBasesFGTS": "S-5003",
    "evtCS": "S-5011",
    "evtIrrf": "S-5012",
    "evtFGTS": "S-5013",
}

# Grupos de linha reconhecidos, por evento. Documenta o vocabulario usado em
# TotalizadorLinha.grupo (util para o consumidor montar a conferencia).
GRUPOS_LINHA = {
    "S-5001": ("info_cp_calc", "base_cs", "calc_terc", "base_pis_pasep"),
    "S-5002": ("cr_men", "cr_dia"),
    "S-5011": ("cr_contrib", "cr_estab", "base_cp", "base_cp13", "cp_seg"),
    "S-5012": ("cr_men", "cr_dia"),
}


@dataclass
class TotalizadorLinha:
    """Uma linha de valor apurado dentro de um evento totalizador.

    :param grupo: Grupo logico de origem (ver GRUPOS_LINHA).
    :param codigo: Codigo de receita (tpCR/CRMen/CRDia) ou tipo de valor
        (tpValor/ind_incid), conforme o grupo.
    :param valor: Valor monetario apurado.
    :param descricao: Nome do campo XML de origem, quando o grupo tem varios
        campos de valor no mesmo elemento (ex.: vrBcCp00, vrDescSest).
    """

    grupo: str
    codigo: str | None = None
    valor: Decimal = Decimal("0")
    descricao: str | None = None
    matricula: str | None = None
    cod_categ: str | None = None
    cod_lotacao: str | None = None
    tp_insc: str | None = None
    nr_insc: str | None = None
    ind_13: str | None = None
    per_ref: str | None = None


@dataclass
class Totalizador:
    """Um evento totalizador devolvido pelo eSocial."""

    evento: str
    nr_rec_arq_base: str | None = None
    per_apur: str | None = None
    ind_apuracao: str | None = None
    cpf_trab: str | None = None
    ind_exist_info: str | None = None
    id_evento: str | None = None
    linhas: list[TotalizadorLinha] = field(default_factory=list)
    xml: str | None = None

    @property
    def total(self) -> Decimal:
        """Soma de todas as linhas (atalho de conferencia grosseira)."""
        return sum((linha.valor for linha in self.linhas), Decimal("0"))

    def total_grupo(self, grupo: str, codigo: str | None = None) -> Decimal:
        """Soma das linhas de um grupo (opcionalmente filtrando por codigo)."""
        return sum(
            (
                linha.valor
                for linha in self.linhas
                if linha.grupo == grupo and (codigo is None or linha.codigo == codigo)
            ),
            Decimal("0"),
        )


# ── API publica ───────────────────────────────────────────────────────────────


def parse_totalizadores(xml: str | bytes) -> list[Totalizador]:
    """Extrai todos os eventos totalizadores presentes em um XML de retorno.

    Aceita o envelope completo do retorno, o grupo <tot> ou o evento
    totalizador isolado. Nunca levanta por XML malformado: devolve lista vazia
    e registra WARNING, porque um retorno ilegivel nao deve derrubar o
    processamento do lote.
    """
    root = _parse(xml)
    if root is None:
        return []

    totalizadores: list[Totalizador] = []
    for elemento in _iter_totalizador_elements(root):
        evento = TOTALIZADOR_ROOTS[_local_name(elemento)]
        parser = _PARSERS.get(evento)
        if parser is None:
            logger.info(
                "Totalizador %s reconhecido mas sem parser detalhado; "
                "devolvendo apenas a identificacao.",
                evento,
            )
            totalizadores.append(_parse_identificacao(evento, elemento))
            continue
        totalizadores.append(parser(elemento))
    return totalizadores


def parse_totalizador(xml: str | bytes) -> Totalizador | None:
    """Como parse_totalizadores, mas devolve o primeiro (ou None)."""
    totalizadores = parse_totalizadores(xml)
    return totalizadores[0] if totalizadores else None


# ── Helpers de arvore ─────────────────────────────────────────────────────────


def _parse(xml: str | bytes) -> etree._Element | None:
    if not xml:
        return None
    raw = xml.encode("utf-8") if isinstance(xml, str) else xml
    try:
        return etree.fromstring(raw)
    except (etree.XMLSyntaxError, ValueError):
        logger.warning("Retorno eSocial: XML ilegivel ao extrair totalizadores.")
        return None


def _local_name(elemento) -> str:
    tag = elemento.tag
    if not isinstance(tag, str):
        return ""
    return tag.rsplit("}", 1)[-1]


def _iter_totalizador_elements(root):
    """Itera os elementos-raiz de evento totalizador dentro da arvore."""
    if _local_name(root) in TOTALIZADOR_ROOTS:
        yield root
    for elemento in root.iter():
        if elemento is root:
            continue
        if _local_name(elemento) in TOTALIZADOR_ROOTS:
            yield elemento


def _find(parent, *path: str):
    """Busca por local-name seguindo um caminho de filhos diretos."""
    atual = parent
    for nome in path:
        encontrado = None
        for filho in atual:
            if _local_name(filho) == nome:
                encontrado = filho
                break
        if encontrado is None:
            return None
        atual = encontrado
    return atual


def _findall(parent, nome: str):
    """Filhos diretos com o local-name informado."""
    if parent is None:
        return []
    return [filho for filho in parent if _local_name(filho) == nome]


def _text(parent, nome: str) -> str | None:
    if parent is None:
        return None
    elemento = _find(parent, nome)
    if elemento is None or elemento.text is None:
        return None
    texto = elemento.text.strip()
    return texto or None


def _decimal(parent, nome: str) -> Decimal | None:
    texto = _text(parent, nome)
    if texto is None:
        return None
    try:
        return Decimal(texto.replace(",", "."))
    except InvalidOperation:
        logger.warning("Totalizador: valor nao numerico em %s: %r", nome, texto)
        return None


def _serialize(elemento) -> str:
    return etree.tostring(elemento, encoding="unicode")


def _parse_identificacao(evento: str, elemento) -> Totalizador:
    """Le apenas ideEvento/ideTrabalhador — comum a todos os totalizadores."""
    ide_evento = _find(elemento, "ideEvento")
    ide_trab = _find(elemento, "ideTrabalhador")
    # nrRecArqBase aparece em ideEvento (S-5001/S-5002) ou no grupo info*
    # (S-5011/S-5012); a busca ampla resolve os dois casos.
    nr_rec = _text(ide_evento, "nrRecArqBase")
    if nr_rec is None:
        for filho in elemento.iter():
            if _local_name(filho) == "nrRecArqBase" and filho.text:
                nr_rec = filho.text.strip()
                break
    return Totalizador(
        evento=evento,
        nr_rec_arq_base=nr_rec,
        per_apur=_text(ide_evento, "perApur"),
        ind_apuracao=_text(ide_evento, "indApuracao"),
        cpf_trab=_text(ide_trab, "cpfTrab") or _text(ide_trab, "cpfBenef"),
        id_evento=elemento.get("Id"),
        xml=_serialize(elemento),
    )


def _linha(grupo: str, valor: Decimal | None, **kwargs) -> TotalizadorLinha | None:
    if valor is None:
        return None
    return TotalizadorLinha(grupo=grupo, valor=valor, **kwargs)


def _linhas_campos(grupo: str, elemento, campos: tuple[str, ...], **comuns):
    """Uma linha por campo de valor presente no elemento (ex.: basesCp)."""
    linhas = []
    for campo in campos:
        valor = _decimal(elemento, campo)
        if valor is None:
            continue
        linhas.append(
            TotalizadorLinha(grupo=grupo, valor=valor, descricao=campo, **comuns)
        )
    return linhas


# ── S-5001 — bases e valores por trabalhador ──────────────────────────────────


def _parse_s5001(elemento) -> Totalizador:
    tot = _parse_identificacao("S-5001", elemento)

    # infoCpCalc: contribuicao previdenciaria calculada, por codigo de receita.
    for info in _findall(elemento, "infoCpCalc"):
        tp_cr = _text(info, "tpCR")
        for campo in ("vrCpSeg", "vrDescSeg"):
            linha = _linha(
                "info_cp_calc",
                _decimal(info, campo),
                codigo=tp_cr,
                descricao=campo,
            )
            if linha:
                tot.linhas.append(linha)

    info_cp = _find(elemento, "infoCp")
    for estab in _findall(info_cp, "ideEstabLot"):
        comuns_estab = {
            "tp_insc": _text(estab, "tpInsc"),
            "nr_insc": _text(estab, "nrInsc"),
            "cod_lotacao": _text(estab, "codLotacao"),
        }
        for categ in _findall(estab, "infoCategIncid"):
            comuns = dict(
                comuns_estab,
                matricula=_text(categ, "matricula"),
                cod_categ=_text(categ, "codCateg"),
            )
            for base in _findall(categ, "infoBaseCS"):
                linha = _linha(
                    "base_cs",
                    _decimal(base, "valor"),
                    codigo=_text(base, "tpValor"),
                    ind_13=_text(base, "ind13"),
                    **comuns,
                )
                if linha:
                    tot.linhas.append(linha)
            for terc in _findall(categ, "calcTerc"):
                tp_cr = _text(terc, "tpCR")
                for campo in ("vrCsSegTerc", "vrDescTerc"):
                    linha = _linha(
                        "calc_terc",
                        _decimal(terc, campo),
                        codigo=tp_cr,
                        descricao=campo,
                        **comuns,
                    )
                    if linha:
                        tot.linhas.append(linha)
            for per_ref in _findall(categ, "infoPerRef"):
                referencia = _text(per_ref, "perRef")
                for det in _findall(per_ref, "detInfoPerRef"):
                    linha = _linha(
                        "base_cs",
                        _decimal(det, "vrPerRef"),
                        codigo=_text(det, "tpVrPerRef"),
                        ind_13=_text(det, "ind13"),
                        per_ref=referencia,
                        **comuns,
                    )
                    if linha:
                        tot.linhas.append(linha)

    info_pis = _find(elemento, "infoPisPasep")
    for estab in _findall(info_pis, "ideEstab"):
        comuns_estab = {
            "tp_insc": _text(estab, "tpInsc"),
            "nr_insc": _text(estab, "nrInsc"),
        }
        for categ in _findall(estab, "infoCategPisPasep"):
            comuns = dict(
                comuns_estab,
                matricula=_text(categ, "matricula"),
                cod_categ=_text(categ, "codCateg"),
            )
            for base in _findall(categ, "infoBasePisPasep"):
                linha = _linha(
                    "base_pis_pasep",
                    _decimal(base, "valorPisPasep"),
                    codigo=_text(base, "tpValorPisPasep"),
                    ind_13=_text(base, "ind13"),
                    **comuns,
                )
                if linha:
                    tot.linhas.append(linha)

    return tot


# ── S-5011 — contribuicoes sociais consolidadas por contribuinte ──────────────

_BASES_CP_CAMPOS = (
    "vrBcCp00",
    "vrBcCp15",
    "vrBcCp20",
    "vrBcCp25",
    "vrSuspBcCp00",
    "vrSuspBcCp15",
    "vrSuspBcCp20",
    "vrSuspBcCp25",
    "vrDescSest",
    "vrCalcSest",
    "vrDescSenat",
    "vrCalcSenat",
    "vrSalFam",
    "vrSalMat",
)


def _parse_s5011(elemento) -> Totalizador:
    tot = _parse_identificacao("S-5011", elemento)
    info_cs = _find(elemento, "infoCS")
    tot.ind_exist_info = _text(info_cs, "indExistInfo")

    # infoCPSeg: INSS do segurado (descontado x calculado) do contribuinte.
    cp_seg = _find(info_cs, "infoCPSeg")
    if cp_seg is not None:
        tot.linhas.extend(
            _linhas_campos("cp_seg", cp_seg, ("vrDescCP", "vrCpSeg"))
        )

    for estab in _findall(info_cs, "ideEstab"):
        comuns_estab = {
            "tp_insc": _text(estab, "tpInsc"),
            "nr_insc": _text(estab, "nrInsc"),
        }
        for cr_estab in _findall(estab, "infoCREstab"):
            tp_cr = _text(cr_estab, "tpCR")
            for campo in ("vrCR", "vrSuspCR"):
                linha = _linha(
                    "cr_estab",
                    _decimal(cr_estab, campo),
                    codigo=tp_cr,
                    descricao=campo,
                    **comuns_estab,
                )
                if linha:
                    tot.linhas.append(linha)
        for lotacao in _findall(estab, "ideLotacao"):
            comuns = dict(comuns_estab, cod_lotacao=_text(lotacao, "codLotacao"))
            for bases in _findall(lotacao, "basesRemun"):
                comuns_bases = dict(comuns, cod_categ=_text(bases, "codCateg"))
                bases_cp = _find(bases, "basesCp")
                if bases_cp is not None:
                    tot.linhas.extend(
                        _linhas_campos(
                            "base_cp",
                            bases_cp,
                            _BASES_CP_CAMPOS,
                            codigo=_text(bases, "indIncid"),
                            **comuns_bases,
                        )
                    )
                bases_cp13 = _find(bases, "basesCp13")
                if bases_cp13 is not None:
                    tot.linhas.extend(
                        _linhas_campos(
                            "base_cp13",
                            bases_cp13,
                            _BASES_CP_CAMPOS,
                            codigo=_text(bases, "indIncid"),
                            **comuns_bases,
                        )
                    )

    # infoCRContrib: o que efetivamente vai para a DCTFWeb, por codigo de receita.
    for cr in _findall(info_cs, "infoCRContrib"):
        tp_cr = _text(cr, "tpCR")
        for campo in ("vrCR", "vrCRSusp"):
            linha = _linha(
                "cr_contrib",
                _decimal(cr, campo),
                codigo=tp_cr,
                descricao=campo,
            )
            if linha:
                tot.linhas.append(linha)

    return tot


# ── S-5002 / S-5012 — IRRF ────────────────────────────────────────────────────

_IR_CONSOLID_CAMPOS = (
    "vlrRendTrib",
    "vlrRendTrib13",
    "vlrPrevOficial",
    "vlrPrevOficial13",
    "vlrCRMen",
    "vlrCR13Men",
)


def _parse_s5002(elemento) -> Totalizador:
    tot = _parse_identificacao("S-5002", elemento)
    ide_trab = _find(elemento, "ideTrabalhador")

    # totInfoIR/consolidApurMen: consolidado do beneficiario no periodo.
    tot_info = _find(ide_trab, "totInfoIR")
    for consolid in _findall(tot_info, "consolidApurMen"):
        tot.linhas.extend(
            _linhas_campos(
                "cr_men",
                consolid,
                _IR_CONSOLID_CAMPOS,
                codigo=_text(consolid, "CRMen"),
            )
        )

    # Detalhe por demonstrativo (dmDev), quando presente.
    for dm_dev in _findall(ide_trab, "dmDev"):
        comuns = {"per_ref": _text(dm_dev, "perRef")}
        for apur in _findall(dm_dev, "totApurMen"):
            tot.linhas.extend(
                _linhas_campos(
                    "cr_men",
                    apur,
                    _IR_CONSOLID_CAMPOS,
                    codigo=_text(apur, "CRMen"),
                    **comuns,
                )
            )
        for dia in _findall(dm_dev, "totApurDia"):
            linha = _linha(
                "cr_dia",
                _decimal(dia, "vlrCRDia"),
                codigo=_text(dia, "CRDia"),
                descricao="vlrCRDia",
                **comuns,
            )
            if linha:
                tot.linhas.append(linha)

    return tot


def _parse_s5012(elemento) -> Totalizador:
    tot = _parse_identificacao("S-5012", elemento)
    info_irrf = _find(elemento, "infoIRRF")
    tot.ind_exist_info = _text(info_irrf, "indExistInfo")

    for cr_men in _findall(info_irrf, "infoCRMen"):
        linha = _linha(
            "cr_men",
            _decimal(cr_men, "vrCRMen"),
            codigo=_text(cr_men, "CRMen"),
            descricao="vrCRMen",
        )
        if linha:
            tot.linhas.append(linha)

    for cr_dia in _findall(info_irrf, "infoCRDia"):
        linha = _linha(
            "cr_dia",
            _decimal(cr_dia, "vrCRDia"),
            codigo=_text(cr_dia, "CRDia"),
            descricao="vrCRDia",
        )
        if linha:
            tot.linhas.append(linha)

    return tot


_PARSERS = {
    "S-5001": _parse_s5001,
    "S-5002": _parse_s5002,
    "S-5011": _parse_s5011,
    "S-5012": _parse_s5012,
}
