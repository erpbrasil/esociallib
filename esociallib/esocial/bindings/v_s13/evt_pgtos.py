from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_03_00"


class InfoPgtoTpPgto(Enum):
    """
    Informar o evento de origem do pagamento.

    :cvar VALUE_1: Pagamento de remuneração, conforme apurado em {ideDmDev}(1200_dmDev_ideDmDev) do S-1200
    :cvar VALUE_2: Pagamento de verbas rescisórias conforme apurado em
        {ideDmDev}(2299_infoDeslig_verbasResc_dmDev_ideDmDev) do S-2299
    :cvar VALUE_3: Pagamento de verbas rescisórias conforme apurado em
        {ideDmDev}(2399_infoTSVTermino_verbasResc_dmDev_ideDmDev) do S-2399
    :cvar VALUE_4: Pagamento de remuneração conforme apurado em {ideDmDev}(1202_dmDev_ideDmDev) do S-1202
    :cvar VALUE_5: Pagamento de benefícios previdenciários, conforme apurado em {ideDmDev}(1207_dmDev_ideDmDev)
        do S-1207
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1210 - Pagamentos de Rendimentos do Trabalho.

    :ivar evtPgtos: Evento Pagamentos de Rendimentos do Trabalho. CHAVE_GRUPO: {Id}
        REGRA:REGRA_CONTROLE_DUPLICIDADE REGRA:REGRA_DESCONTO_IRRF_POSITIVO REGRA:REGRA_EMPREGADO_DOMESTICO
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVE_FOPAG_SIMPLIFICADO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_PAGTO_IND_RETIFICACAO
        REGRA:REGRA_PAGTO_PERMITE_EXCLUSAO REGRA:REGRA_VALIDA_DT_PGTO REGRA:REGRA_VALIDA_EMPREGADOR
        REGRA:REGRA_VALIDA_PER_APUR_PGTO REGRA:REGRA_VALIDA_PERANT_1210
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_03_00"

    evtPgtos: ESocial.EvtPgtos = field(
        metadata={
            "type": "Element",
        }
    )
    Signature: Signature = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )

    @dataclass(kw_only=True)
    class EvtPgtos(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideBenef: Identificação do beneficiário do pagamento. CHAVE_GRUPO: {cpfBenef*}
        :ivar Id:
        """

        ideEvento: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideBenef: ESocial.EvtPgtos.IdeBenef = field(
            metadata={
                "type": "Element",
            }
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass(kw_only=True)
        class IdeBenef(CommonMixin):
            """
            :ivar cpfBenef: Informar o CPF do beneficiário. Validação: Deve ser o mesmo CPF informado no evento
                de remuneração ou desligamento (S-1200, S-1202, S-1207, S-2299 ou S-2399).
            :ivar infoPgto: Informações dos pagamentos efetuados. CHAVE_GRUPO: {tpPgto}, {perRef}, {ideDmDev}
                CONDICAO_GRUPO: OC (se {}(1210_ideEvento_perApur) = [AAAA-01] e existir pelo menos um grupo
                {infoIRComplem/perAnt}(1210_ideBenef_infoIRComplem_perAnt)); O (nos demais casos)
            :ivar infoIRComplem: Informações relacionadas à retenção na fonte, aos rendimentos tributáveis e não
                tributáveis, deduções e/ou isenções, etc., de acordo com a legislação aplicada ao imposto de
                renda. CHAVE_GRUPO: {perAnt_perRefAjuste} CONDICAO_GRUPO: O (conforme as condições dos grupos
                {}(1210_ideBenef_infoIRComplem_infoIRCR_penAlim),
                {}(1210_ideBenef_infoIRComplem_infoIRCR_previdCompl), {}(1210_ideBenef_infoIRComplem_planSaude)
                e {}(1210_ideBenef_infoIRComplem_infoIRCR_infoProcRet)} e se {}(1210_ideEvento_perApur)
                posterior ou igual [2025-01] (início da substituição da DIRF)); F (nos demais casos)
            """

            cpfBenef: str = field(
                metadata={
                    "type": "Element",
                }
            )
            infoPgto: list[ESocial.EvtPgtos.IdeBenef.InfoPgto] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 999,
                },
            )
            infoIRComplem: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 13,
                },
            )

            @dataclass(kw_only=True)
            class InfoPgto(CommonMixin):
                """
                :ivar dtPgto: Informar a data de pagamento. Validação: A data informada deve estar compreendida
                    no período de apuração ({perApur}(1210_ideEvento_perApur)), exceto se
                    {procEmi}(1210_ideEvento_procEmi) = [2, 4, 22].
                :ivar tpPgto:
                :ivar perRef: Informar a competência declarada no campo {perApur} do evento remuneratório a que
                    se refere o pagamento, no formato AAAA-MM (ou AAAA, se for relativa à folha de 13° salário).
                    Se {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [2, 3], informar o mês/ano da data de
                    desligamento (ou de término), no formato AAAA-MM. Validação: Deve corresponder ao conteúdo
                    indicado na relação a seguir: Se {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [1],
                    {perApur}(1200_ideEvento_perApur) do S-1200; Se {tpPgto}(1210_ideBenef_infoPgto_tpPgto) =
                    [2], mês/ano de {dtDeslig}(2299_infoDeslig_dtDeslig) do S-2299 (formato AAAA-MM); Se
                    {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [3], mês/ano de
                    {dtTerm}(2399_infoTSVTermino_dtTerm) do S-2399 (formato AAAA-MM); Se
                    {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [4], {perApur}(1202_ideEvento_perApur) do S-1202;
                    Se {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [5], {perApur}(1207_ideEvento_perApur) do
                    S-1207.
                :ivar ideDmDev: Identificador atribuído pela fonte pagadora para o demonstrativo de valores
                    devidos ao trabalhador conforme definido em S-1200, S-1202, S-1207, S-2299 ou S-2399.
                    Validação: Deve ser um valor atribuído pela fonte pagadora em S-1200, S-1202, S-1207, S-2299
                    ou S-2399 no campo {ideDmDev}, obedecendo à relação: Se
                    {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [1], em S-1200; Se
                    {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [2], em S-2299; Se
                    {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [3], em S-2399; Se
                    {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [4], em S-1202; Se
                    {tpPgto}(1210_ideBenef_infoPgto_tpPgto) = [5], em S-1207.
                :ivar vrLiq: Valor líquido recebido pelo trabalhador, composto pelos vencimentos e descontos,
                    inclusive os descontos de IRRF e de pensão alimentícia (se houver). Validação: Não pode ser
                    um valor negativo.
                :ivar paisResidExt: Informar o código do país de residência para fins fiscais, quando no
                    exterior, conforme Tabela 06. Somente informar este campo caso o país de residência para
                    fins fiscais seja diferente de Brasil. Se não informado, implica que o país de residência
                    fiscal é Brasil. Validação: O campo apenas pode ser preenchido se
                    {perApur}(1210_ideEvento_perApur) &gt;= [2023-03]. Se informado, deve ser um código válido e
                    existente na Tabela 06, exceto [105].
                :ivar infoPgtoExt: Informações complementares relativas a pagamentos a residente fiscal no
                    exterior. CONDICAO_GRUPO: O (se {paisResidExt}(../paisResidExt) for informado); N (nos
                    demais casos)
                """

                dtPgto: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                tpPgto: InfoPgtoTpPgto = field(
                    metadata={
                        "type": "Element",
                    }
                )
                perRef: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                ideDmDev: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                vrLiq: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                paisResidExt: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoPgtoExt: None | ESocial.EvtPgtos.IdeBenef.InfoPgto.InfoPgtoExt = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoPgtoExt(CommonMixin):
                    """
                    :ivar indNIF:
                    :ivar nifBenef: Número de Identificação Fiscal (NIF). Validação: Preenchimento obrigatório e
                        exclusivo se {indNIF}(./indNIF) = [1].
                    :ivar frmTribut:
                    :ivar endExt: Endereço do beneficiário residente ou domiciliado no exterior. CONDICAO_GRUPO:
                        OC REGRA:REGRA_ENDERECO_EXTERIOR
                    """

                    indNIF: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    nifBenef: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    frmTribut: str = field(
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{2}",
                        }
                    )
                    endExt: None | ESocial.EvtPgtos.IdeBenef.InfoPgto.InfoPgtoExt.EndExt = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class EndExt(CommonMixin):
                        """
                        :ivar endDscLograd:
                        :ivar endNrLograd: Número do logradouro. Validação: Devem ser utilizados apenas
                            caracteres alfanuméricos com, pelo menos, um caractere numérico.
                        :ivar endComplem:
                        :ivar endBairro:
                        :ivar endCidade:
                        :ivar endEstado:
                        :ivar endCodPostal:
                        :ivar telef:
                        """

                        endDscLograd: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 80,
                                "pattern": r"[^\s]{1}[\S\s]*",
                            },
                        )
                        endNrLograd: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        endComplem: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        endBairro: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 60,
                                "pattern": r".*[^\s].*",
                            },
                        )
                        endCidade: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 40,
                                "pattern": r".*[^\s].*",
                            },
                        )
                        endEstado: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 40,
                                "pattern": r".*[^\s].*",
                            },
                        )
                        endCodPostal: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 12,
                                "pattern": r"[A-Za-z0-9]{1,12}",
                            },
                        )
                        telef: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "pattern": r"\d{8,15}",
                            },
                        )

            @dataclass(kw_only=True)
            class InfoIrcomplem(CommonMixin):
                """
                :ivar dtLaudo: Data da moléstia grave atribuída pelo laudo. Validação: Não pode ser anterior ao
                    ano de 1900. Deve ser anterior ou igual a {}(1210_ideEvento_perApur).
                :ivar perAnt: Informações complementares de períodos anteriores DESCRICAO_COMPLETA:
                    Identificação do evento S-1210 original e {}(1210_ideBenef_infoPgto_perRef) cujas
                    informações de {}(1210_ideBenef_infoIRComplem) serão alteradas. CONDICAO_GRUPO: F (se o mês
                    de {}(1210_ideEvento_perApur) = [01]); N (nos demais casos)
                :ivar infoDep: Informações de dependentes não cadastrados pelo
                    S-2200/S-2205/S-2300/S-2400/S-2405. CHAVE_GRUPO: {cpfDep} CONDICAO_GRUPO: OC
                :ivar infoIRCR: Informações de Imposto de Renda, por Código de Receita - CR. CHAVE_GRUPO: {tpCR}
                    CONDICAO_GRUPO: OC
                :ivar planSaude: Plano de saúde coletivo DESCRICAO_COMPLETA: Plano de saúde coletivo.
                    Identificação da(s) operadora(s) de plano privado coletivo empresarial de assistência à
                    saúde. CHAVE_GRUPO: {cnpjOper}, {regANS} CONDICAO_GRUPO: O (((se
                    {}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [67, 9067] ou
                    {}(1010_infoRubrica_inclusao_dadosRubrica_natRubr) em S-1010 = [9219]) e
                    {}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 = [2]) em qualquer rubrica em
                    {infoPgto}(1210_ideBenef_infoPgto), inclusive aquelas referenciadas em
                    {perAnt/nrRec1210Orig}(1210_ideBenef_infoIRComplem_perAnt_nrRec1210Orig)); OC (nos demais
                    casos)
                :ivar infoReembMed: Reembolsos de despesas médicas DESCRICAO_COMPLETA: Informações relativas a
                    reembolsos efetuados no período de apuração ({perApur}(1210_ideEvento_perApur)) pelo
                    empregador ao trabalhador referente a despesas médicas ou odontológicas pagas pelo
                    trabalhador a prestadores de serviços de saúde. CHAVE_GRUPO: {cnpjOper}, {regANS}
                    CONDICAO_GRUPO: OC
                """

                dtLaudo: None | XmlDate = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                perAnt: None | ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.PerAnt = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoDep: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoDep] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 999,
                    },
                )
                infoIRCR: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoIrcr] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                planSaude: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.PlanSaude] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                infoReembMed: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoReembMed] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )

                @dataclass(kw_only=True)
                class PerAnt(CommonMixin):
                    """
                    :ivar perRefAjuste: Informar {}(1210_ideEvento_perApur) do S-1210 cujo
                        {}(1210_ideBenef_infoIRComplem) será alterado. Validação: Deve corresponder a um mês do
                        ano anterior (ano de {}(1210_ideEvento_perApur) - 1)
                    :ivar nrRec1210Orig: Número do recibo do S-1210 original cujas informações de
                        {}(1210_ideBenef_infoIRComplem) serão alteradas. Validação: Deve corresponder ao recibo
                        de um arquivo com informações de rendimentos sujeitos a Imposto de Renda Retido na Fonte
                        - IRRF (S-1210). Validação: Deve corresponder ao recibo de um evento S-1210 válido, com
                        {}(1210_ideEvento_perApur) igual a {}(./perRefAjuste)
                    """

                    perRefAjuste: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    nrRec1210Orig: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoDep(CommonMixin):
                    """
                    :ivar cpfDep:
                    :ivar dtNascto:
                    :ivar nome:
                    :ivar depIRRF:
                    :ivar tpDep: Tipo de dependente. Validação: Preenchimento obrigatório e exclusivo se
                        {depIRRF}(./depIRRF) = [S]. Deve ser um código válido e existente na Tabela 07.
                    :ivar descrDep:
                    """

                    cpfDep: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtNascto: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    nome: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    depIRRF: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    tpDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    descrDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class InfoIrcr(CommonMixin):
                    """
                    :ivar tpCR:
                    :ivar dedDepen: Dedução do rendimento tributável relativa a dependentes. CHAVE_GRUPO:
                        {tpRend}, {cpfDep} CONDICAO_GRUPO: N (se {tpCR}(../tpCR) = [188901]); OC (nos demais
                        casos)
                    :ivar penAlim: Informação dos beneficiários da pensão alimentícia. CHAVE_GRUPO: {tpRend},
                        {cpfDep} CONDICAO_GRUPO: O ((se {}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em
                        S-1010 = [51, 52, 53, 54] e {}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010
                        = [2]) em qualquer rubrica em {infoPgto}(1210_ideBenef_infoPgto), inclusive aquelas
                        referenciadas em
                        {perAnt/nrRec1210Orig}(1210_ideBenef_infoIRComplem_perAnt_nrRec1210Orig)); OC (nos
                        demais casos)
                    :ivar previdCompl: Informações relativas a planos de previdência complementar. CHAVE_GRUPO:
                        {tpPrev}, {cnpjEntidPC} CONDICAO_GRUPO: O ((se
                        {}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [46, 47, 48, 61, 62,
                        63, 64, 65, 66] e {}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 = [2]) em
                        qualquer rubrica em {infoPgto}(1210_ideBenef_infoPgto), inclusive aquelas referenciadas
                        em {perAnt/nrRec1210Orig}(1210_ideBenef_infoIRComplem_perAnt_nrRec1210Orig)); OC (nos
                        demais casos)
                    :ivar infoProcRet: Processos relacionados a não retenção de tributos DESCRICAO_COMPLETA:
                        Informações de processos relacionados a não retenção de tributos ou a depósitos
                        judiciais. CHAVE_GRUPO: {tpProcRet}, {nrProcRet}, {codSusp} CONDICAO_GRUPO: N (se
                        {tpCR}(../tpCR) = [188901]); O (se {}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF)
                        em S-1010 = [9XXX] (exceto [9067]) com valor &gt; 0 em qualquer rubrica em
                        {infoPgto}(1210_ideBenef_infoPgto), inclusive aquelas referenciadas em
                        {perAnt/nrRec1210Orig}(1210_ideBenef_infoIRComplem_perAnt_nrRec1210Orig)); OC (nos
                        demais casos)
                    """

                    tpCR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dedDepen: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoIrcr.DedDepen] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 999,
                        },
                    )
                    penAlim: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoIrcr.PenAlim] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    previdCompl: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoIrcr.PrevidCompl] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    infoProcRet: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoIrcr.InfoProcRet] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 50,
                        },
                    )

                    @dataclass(kw_only=True)
                    class DedDepen(CommonMixin):
                        tpRend: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        cpfDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrDedDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class PenAlim(CommonMixin):
                        """
                        :ivar tpRend: Tipo de rendimento. Validação: Se {tpCR}(../tpCR) = [188901], deve ser
                            igual a [18].
                        :ivar cpfDep:
                        :ivar vlrDedPenAlim:
                        """

                        tpRend: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        cpfDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrDedPenAlim: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class PrevidCompl(CommonMixin):
                        """
                        :ivar tpPrev:
                        :ivar cnpjEntidPC: Número de inscrição da entidade de previdência complementar.
                            Validação: Deve ser um CNPJ válido no Cadastro CNPJ e não pode estar com situação
                            cadastral "baixada" (situação = 8) em data anterior ao período de apuração indicado
                            em {perApur}(1210_ideEvento_perApur) ou "nula" (situação = 1).
                        :ivar vlrDedPC: Valor da dedução mensal relativa a previdência complementar. Validação:
                            Preenchimento obrigatório se {vlrDedPC13} não for preenchido. Deve ser maior que 0
                            (zero).
                        :ivar vlrDedPC13: Valor da dedução do 13º Salário relativa a previdência complementar.
                            Validação: Preenchimento obrigatório se {vlrDedPC} não for preenchido. Deve ser
                            maior que 0 (zero).
                        :ivar vlrPatrocFunp: Valor da contribuição mensal do ente público patrocinador da
                            Fundação de Previdência Complementar do Servidor Público (Funpresp). Validação:
                            Informação permitida apenas se {tpPrev}(./tpPrev) = [3]. Deve ser maior que 0
                            (zero).
                        :ivar vlrPatrocFunp13: Valor da contribuição do 13º Salário do ente público patrocinador
                            da Fundação de Previdência Complementar do Servidor Público (Funpresp). Validação:
                            Informação permitida apenas se {tpPrev}(./tpPrev) = [3]. Deve ser maior que 0
                            (zero).
                        """

                        tpPrev: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        cnpjEntidPC: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrDedPC: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        vlrDedPC13: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        vlrPatrocFunp: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        vlrPatrocFunp13: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                    @dataclass(kw_only=True)
                    class InfoProcRet(CommonMixin):
                        """
                        :ivar tpProcRet:
                        :ivar nrProcRet:
                        :ivar codSusp:
                        :ivar infoValores: Informações de valores relacionados a não retenção de tributos ou a
                            depósitos judiciais. CHAVE_GRUPO: {indApuracao} CONDICAO_GRUPO: OC
                        """

                        tpProcRet: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        nrProcRet: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        codSusp: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        infoValores: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoIrcr.InfoProcRet.InfoValores] = (
                            field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 2,
                                },
                            )
                        )

                        @dataclass(kw_only=True)
                        class InfoValores(CommonMixin):
                            """
                            :ivar indApuracao:
                            :ivar vlrNRetido:
                            :ivar vlrDepJud:
                            :ivar vlrCmpAnoCal:
                            :ivar vlrCmpAnoAnt:
                            :ivar vlrRendSusp:
                            :ivar dedSusp: Detalhamento das deduções suspensas DESCRICAO_COMPLETA: Detalhamento
                                das deduções com exigibilidade suspensa. CHAVE_GRUPO: {indTpDeducao},
                                {cnpjEntidPC} CONDICAO_GRUPO: OC
                            """

                            indApuracao: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vlrNRetido: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vlrDepJud: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vlrCmpAnoCal: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vlrCmpAnoAnt: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vlrRendSusp: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            dedSusp: list[
                                ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoIrcr.InfoProcRet.InfoValores.DedSusp
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 25,
                                },
                            )

                            @dataclass(kw_only=True)
                            class DedSusp(CommonMixin):
                                """
                                :ivar indTpDeducao:
                                :ivar vlrDedSusp: Valor da dedução da base de cálculo do imposto de renda com
                                    exigibilidade suspensa. Validação: Se {indTpDeducao}(./indTpDeducao) = [5,
                                    7], e o grupo {benefPen}(./benefPen) for preenchido, o valor informado neste
                                    campo deve ser a soma do(s) campo(s) {vlrDepenSusp}(./benefPen_vlrDepenSusp)
                                    do grupo {benefPen}(./benefPen). Deve ser maior que 0 (zero). O não
                                    preenchimento do grupo {benefPen}(./benefPen) indica que o contribuinte
                                    declarante não possui as informações detalhadas por dependente/alimentando.
                                :ivar cnpjEntidPC: Número de inscrição da entidade de previdência complementar.
                                    Validação: Informação obrigatória e exclusiva se
                                    {indTpDeducao}(./indTpDeducao) = [2, 3, 4]. Deve ser um CNPJ válido no
                                    Cadastro CNPJ e não pode estar com situação cadastral "baixada" (situação =
                                    8) em data anterior ao período de apuração indicado em
                                    {perApur}(1210_ideEvento_perApur) ou "nula" (situação = 1).
                                :ivar vlrPatrocFunp: Valor da contribuição do ente público patrocinador da
                                    Fundação de Previdência Complementar do Servidor Público (Funpresp).
                                    Validação: Informação exclusiva se {indTpDeducao}(./indTpDeducao) = [4].
                                    Deve ser maior que 0 (zero).
                                :ivar benefPen: Deduções suspensas por dependentes e beneficiários da pensão
                                    alimentícia DESCRICAO_COMPLETA: Informação das deduções suspensas por
                                    dependentes e beneficiários da pensão alimentícia. CHAVE_GRUPO: {cpfDep}
                                    CONDICAO_GRUPO: O (se {indTpDeducao}(../indTpDeducao) = [5, 7]); N (nos
                                    demais casos)
                                """

                                indTpDeducao: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                vlrDedSusp: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                cnpjEntidPC: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                vlrPatrocFunp: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                benefPen: list[
                                    ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoIrcr.InfoProcRet.InfoValores.DedSusp.BenefPen
                                ] = field(
                                    default_factory=list,
                                    metadata={
                                        "type": "Element",
                                        "max_occurs": 99,
                                    },
                                )

                                @dataclass(kw_only=True)
                                class BenefPen(CommonMixin):
                                    """
                                    :ivar cpfDep:
                                    :ivar vlrDepenSusp: Valor da dedução relativa a dependentes ou a pensão
                                        alimentícia com exigibilidade suspensa. Validação: Deve ser maior que 0
                                        (zero).
                                    """

                                    cpfDep: str = field(
                                        metadata={
                                            "type": "Element",
                                        }
                                    )
                                    vlrDepenSusp: str = field(
                                        metadata={
                                            "type": "Element",
                                        }
                                    )

                @dataclass(kw_only=True)
                class PlanSaude(CommonMixin):
                    """
                    :ivar cnpjOper: Informar o número do CNPJ da operadora de plano privado coletivo empresarial
                        de assistência à saúde. Validação: Deve ser um CNPJ válido no Cadastro CNPJ e não pode
                        estar com situação cadastral "baixada" (situação = 8) em data anterior ao período de
                        apuração indicado em {perApur}(1210_ideEvento_perApur) ou "nula" (situação = 1). Não
                        deve ser igual ao número de inscrição das pessoas jurídicas informadas nos grupos
                        {}(1210_ideBenef_infoIRComplem_infoIRCR_previdCompl) (para
                        {}(1210_ideBenef_infoIRComplem_infoIRCR_previdCompl_tpPrev) = [2, 3]) e {ideAdv} do
                        evento remuneratório.
                    :ivar regANS:
                    :ivar vlrSaudeTit: Valor relativo à dedução do rendimento tributável correspondente a
                        pagamento a plano de saúde do titular. Validação: Deve ser maior ou igual a 0 (zero). Se
                        for igual a 0 (zero), deve haver informações em registro(s) filho(s), relativas a
                        dependentes ({infoDepSau}(./infoDepSau)).
                    :ivar infoDepSau: Informações de dependente de plano de saúde coletivo empresarial.
                        CHAVE_GRUPO: {cpfDep} CONDICAO_GRUPO: OC
                    """

                    cnpjOper: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    regANS: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    vlrSaudeTit: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoDepSau: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.PlanSaude.InfoDepSau] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoDepSau(CommonMixin):
                        """
                        :ivar cpfDep: Número de inscrição no CPF do dependente do plano de saúde. Validação:
                            Deve ser um CPF de dependente cadastrado no eSocial
                            (S-2200/S-2205/S-2300/S-2400/S-2405 ou no grupo
                            {infoDep}(1210_ideBenef_infoIRComplem_infoDep)).
                        :ivar vlrSaudeDep: Valor relativo a dedução do rendimento tributável correspondente a
                            pagamento a plano de saúde do dependente. Validação: Deve ser maior que 0 (zero).
                        """

                        cpfDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrSaudeDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                @dataclass(kw_only=True)
                class InfoReembMed(CommonMixin):
                    """
                    :ivar indOrgReemb:
                    :ivar cnpjOper: CNPJ da operadora do plano de saúde. Validação: Informação obrigatória e
                        exclusiva se {indOrgReemb}(./indOrgReemb) = [1]. Deve ser um CNPJ válido no Cadastro
                        CNPJ e não pode estar com situação cadastral "baixada" (situação = 8) em data anterior
                        ao período de apuração indicado em {}(1210_ideEvento_perApur) ou "nula" (situação = 1).
                        Não deve ser igual ao número de inscrição das pessoas jurídicas informadas nos grupos
                        {}(1210_ideBenef_infoIRComplem_infoIRCR_previdCompl) e {ideAdv} do evento remuneratório.
                    :ivar regANS:
                    :ivar detReembTit: Informação de reembolso do titular do plano de saúde. CHAVE_GRUPO:
                        {tpInsc}, {nrInsc} CONDICAO_GRUPO: OC
                    :ivar infoReembDep: Informação de reembolso do dependente do plano de saúde. CHAVE_GRUPO:
                        {cpfBenef} CONDICAO_GRUPO: OC
                    """

                    indOrgReemb: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    cnpjOper: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    regANS: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    detReembTit: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    infoReembDep: list[ESocial.EvtPgtos.IdeBenef.InfoIrcomplem.InfoReembMed.InfoReembDep] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoReembDep(CommonMixin):
                        """
                        :ivar cpfBenef: Número de inscrição no CPF do dependente. Validação: Deve ser um CPF de
                            dependente cadastrado no eSocial (S-2200/S-2205/S-2300/S-2400/S-2405 ou no grupo
                            {infoDep}(1210_ideBenef_infoIRComplem_infoDep)).
                        :ivar detReembDep: Detalhamento dos reembolsos efetuados aos dependentes
                            DESCRICAO_COMPLETA: Detalhamento dos reembolsos efetuados em
                            {perApur}(1210_ideEvento_perApur) pelo empregador ao trabalhador referente a
                            despesas médicas ou odontológicas pagas pelo trabalhador a prestadores de serviços
                            de saúde relativo a despesas de seus dependentes. CHAVE_GRUPO: {tpInsc}, {nrInsc}
                            CONDICAO_GRUPO: OC
                        """

                        cpfBenef: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        detReembDep: list[str] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 99,
                            },
                        )
