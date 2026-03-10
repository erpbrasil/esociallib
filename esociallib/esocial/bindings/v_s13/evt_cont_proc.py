from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtContProc/v_S_01_03_00"


class DedDepenTpRend(Enum):
    """
    :cvar VALUE_11: Remuneração mensal
    :cvar VALUE_12: 13º salário
    """

    VALUE_11 = 11
    VALUE_12 = 12


class DedSuspIndTpDeducao(Enum):
    """
    :cvar VALUE_1: Previdência oficial
    :cvar VALUE_5: Pensão alimentícia
    :cvar VALUE_7: Dependentes
    """

    VALUE_1 = 1
    VALUE_5 = 5
    VALUE_7 = 7


class InfoCrirrfTpCr(Enum):
    """
    :cvar VALUE_593656: IRRF - Decisão da Justiça do Trabalho
    :cvar VALUE_056152: IRRF - CCP/NINTER
    :cvar VALUE_188951: IRRF - RRA
    """

    VALUE_593656 = 593656
    VALUE_056152 = "056152"
    VALUE_188951 = 188951


class PenAlimTpRend(Enum):
    """
    :cvar VALUE_11: Remuneração mensal
    :cvar VALUE_12: 13º salário
    :cvar VALUE_18: RRA
    :cvar VALUE_79: Rendimento isento ou não tributável
    """

    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_18 = 18
    VALUE_79 = 79


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2501 - Informações de Tributos Decorrentes de Processo Trabalhista.

    :ivar evtContProc: Evento Informações de Tributos Decorrentes de Processo Trabalhista. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EXC_RET_2501 REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_RETIFICA_IDENTIFICADOR REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtContProc/v_S_01_03_00"

    evtContProc: ESocial.EvtContProc = field(
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
    class EvtContProc(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador: Informações de identificação do empregador ou do contribuinte que está prestando a
            informação. CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar ideProc: Identificação do processo. CHAVE_GRUPO: {nrProcTrab*}, {perApurPgto*}, {ideSeqProc*}
        :ivar ideTrab: Identificação do trabalhador. CHAVE_GRUPO: {cpfTrab}
        :ivar Id:
        """

        ideEvento: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: ESocial.EvtContProc.IdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        ideProc: ESocial.EvtContProc.IdeProc = field(
            metadata={
                "type": "Element",
            }
        )
        ideTrab: list[ESocial.EvtContProc.IdeTrab] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass(kw_only=True)
        class IdeEmpregador(CommonMixin):
            """
            :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição do empregador ou
                contribuinte que está prestando a informação, conforme Tabela 05.
            :ivar nrInsc: Informar o número de inscrição do empregador ou contribuinte que está prestando a
                informação, de acordo com o tipo de inscrição indicado no campo {ideEmpregador/tpInsc}(./tpInsc)
                e conforme informado em S-1000.
            """

            tpInsc: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nrInsc: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class IdeProc(CommonMixin):
            """
            :ivar nrProcTrab: Número do processo trabalhista, da ata ou número de identificação da conciliação.
                Validação: Deve ser um número de processo válido e declarado no evento S-2500 para o(s)
                trabalhador(es) informado(s) em {cpfTrab}(2501_ideTrab_cpfTrab).
            :ivar perApurPgto: Mês/ano em que é devida a obrigação de pagar a parcela prevista no
                acordo/sentença. Validação: Deve ser um período igual ou posterior ao mês/ano de
                {dtSent}(2500_infoProcesso_dadosCompl_infoProcJud_dtSent) ou de
                {dtCCP}(2500_infoProcesso_dadosCompl_infoCCP_dtCCP) existente no evento S-2500 para o processo
                indicado em {nrProcTrab}(./nrProcTrab). Deve ser informado no formato AAAA-MM.
            :ivar ideSeqProc: Número sequencial atribuído pela empresa a cada conjunto de dados de tributos
                decorrentes de processo trabalhista, quando for necessário enviar o mesmo processo em múltiplos
                S-2501, para o mesmo {}(./perApurPgto). Validação: Deve ser um identificador único dentre os
                eventos S-2501 do empregador que tenham os mesmos {}(./nrProcTrab) e {}(./perApurPgto). Se for
                preenchido, não pode haver outro evento S-2501 com os mesmos {}(./nrProcTrab) e
                {}(./perApurPgto) e sem o campo {}(./ideSeqProc). Se não for preenchido, não pode haver outro
                evento S-2501 com os mesmos {}(./nrProcTrab) e {}(./perApurPgto). O valor [0] é reservado para
                uso interno.
            :ivar obs: Observação referente ao pagamento de parcela prevista no acordo/sentença.
            """

            nrProcTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            perApurPgto: str = field(
                metadata={
                    "type": "Element",
                }
            )
            ideSeqProc: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "pattern": r"\d{1,3}",
                },
            )
            obs: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class IdeTrab(CommonMixin):
            """
            :ivar calcTrib: Identificação do período e da base de cálculo dos tributos. CHAVE_GRUPO: {perRef}
                CONDICAO_GRUPO: OC
            :ivar infoCRIRRF: Informações de IRRF. DESCRICAO_COMPLETA:Informações de Imposto de Renda, por
                Código de Receita - CR. CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
            :ivar infoIRComplem: Informações relacionadas à retenção na fonte, aos rendimentos tributáveis e não
                tributáveis, deduções e/ou isenções, etc., de acordo com a legislação aplicada ao imposto de
                renda. CONDICAO_GRUPO: OC
            :ivar cpfTrab: Preencher com o número do CPF do trabalhador. Validação: Deve ser um CPF válido e
                informado no evento S-2500. Deve ser único dentre os eventos S-2501 do empregador que tenham os
                mesmos {}(../ideProc_nrProcTrab) e {}(../ideProc_perApurPgto).
            """

            calcTrib: list[ESocial.EvtContProc.IdeTrab.CalcTrib] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 999,
                },
            )
            infoCRIRRF: list[ESocial.EvtContProc.IdeTrab.InfoCrirrf] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                },
            )
            infoIRComplem: None | ESocial.EvtContProc.IdeTrab.InfoIrcomplem = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            cpfTrab: str = field(
                metadata={
                    "type": "Attribute",
                }
            )

            @dataclass(kw_only=True)
            class CalcTrib(CommonMixin):
                """
                :ivar infoCRContrib: Informações das contribuições sociais. DESCRICAO_COMPLETA:Informações das
                    contribuições sociais devidas à Previdência Social e Outras Entidades e Fundos, por Código
                    de Receita - CR. CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
                :ivar perRef: Informar o mês/ano (formato AAAA-MM) de referência das informações. Validação:
                    Deve ser um período existente no evento S-2500 para o trabalhador indicado em
                    {cpfTrab}(../cpfTrab) (observado o campo {}(2500_ideTrab_ideSeqTrab) de S-2500, se
                    existente) e igual ou posterior a [2008-12].
                :ivar vrBcCpMensal: Valor da base de cálculo da contribuição previdenciária sobre a remuneração
                    mensal do trabalhador. Validação: Deve ser maior ou igual a 0 (zero).
                :ivar vrBcCp13: Valor da base de cálculo da contribuição previdenciária sobre a remuneração do
                    trabalhador referente ao 13º salário. Validação: Deve ser maior ou igual a 0 (zero).
                """

                infoCRContrib: list[ESocial.EvtContProc.IdeTrab.CalcTrib.InfoCrcontrib] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                perRef: str = field(
                    metadata={
                        "type": "Attribute",
                    }
                )
                vrBcCpMensal: str = field(
                    metadata={
                        "type": "Attribute",
                    }
                )
                vrBcCp13: str = field(
                    metadata={
                        "type": "Attribute",
                    }
                )

                @dataclass(kw_only=True)
                class InfoCrcontrib(CommonMixin):
                    """
                    :ivar tpCR: Código de Receita - CR relativo a contribuições sociais devidas à Previdência
                        Social e a Outras Entidades e Fundos (Terceiros), conforme legislação em vigor na
                        competência. Validação: Deve ser um código válido e existente na Tabela 29.
                    :ivar vrCR: Valor correspondente ao Código de Receita - CR. Validação: Deve ser informado de
                        acordo com a legislação em vigor na competência. Deve ser maior que 0 (zero).
                    """

                    tpCR: str = field(
                        metadata={
                            "type": "Attribute",
                            "pattern": r"\d{6}",
                        }
                    )
                    vrCR: str = field(
                        metadata={
                            "type": "Attribute",
                        }
                    )

            @dataclass(kw_only=True)
            class InfoCrirrf(CommonMixin):
                """
                :ivar infoIR: Informações complementares, vinculadas ao
                    {infoCRIRRF/tpCR}(2501_ideTrab_infoCRIRRF_tpCR), relacionadas a rendimentos tributáveis e a
                    deduções e/ou isenções de acordo com a legislação aplicada ao imposto de renda.
                    CONDICAO_GRUPO: OC
                :ivar infoRRA: Informações complementares de RRA DESCRICAO_COMPLETA: Informações complementares
                    relativas a Rendimentos Recebidos Acumuladamente - RRA. CONDICAO_GRUPO: O (se
                    {infoCRIRRF/tpCR}(../tpCR) = [188951]); N (nos demais casos)
                :ivar dedDepen: Dedução do rendimento tributável relativa a dependentes. CHAVE_GRUPO: {tpRend},
                    {cpfDep} CONDICAO_GRUPO: N (se {infoCRIRRF/tpCR}(../tpCR) = [188951]); OC (nos demais casos)
                :ivar penAlim: Informação dos beneficiários da pensão alimentícia. CHAVE_GRUPO: {tpRend},
                    {cpfDep} CONDICAO_GRUPO: OC
                :ivar infoProcRet: Informações de processos relacionados a não retenção de tributos ou a
                    depósitos judiciais. CHAVE_GRUPO: {tpProcRet}, {nrProcRet}, {codSusp} CONDICAO_GRUPO: N (se
                    {infoCRIRRF/tpCR}(../tpCR) = [188951]); OC (nos demais casos)
                :ivar tpCR: Código de Receita - CR relativo a Imposto sobre a renda retido na fonte.
                :ivar vrCR: Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita -
                    rendimento mensal. Validação: Deve ser informado de acordo com a legislação em vigor na
                    competência. Deve ser maior ou igual a 0 (zero).
                :ivar vrCR13: Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita -
                    13º Salário. Validação: Deve ser informado de acordo com a legislação em vigor na
                    competência. Deve ser maior que 0 (zero).
                """

                infoIR: None | ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoIr = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoRRA: None | ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoRra = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                dedDepen: list[ESocial.EvtContProc.IdeTrab.InfoCrirrf.DedDepen] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 999,
                    },
                )
                penAlim: list[ESocial.EvtContProc.IdeTrab.InfoCrirrf.PenAlim] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                infoProcRet: list[ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoProcRet] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 50,
                    },
                )
                tpCR: InfoCrirrfTpCr = field(
                    metadata={
                        "type": "Attribute",
                    }
                )
                vrCR: str = field(
                    metadata={
                        "type": "Attribute",
                    }
                )
                vrCR13: None | str = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

                @dataclass(kw_only=True)
                class InfoIr(CommonMixin):
                    """
                    :ivar rendIsen0561: Rendimentos Isentos exclusivos do CR 0561. CONDICAO_GRUPO: OC (se
                        {}(../../tpCR) = [056152]); N (demais casos)
                    :ivar vrRendTrib: Valor do rendimento tributável mensal do Imposto de Renda. Validação: Deve
                        ser maior ou igual a 0 (zero).
                    :ivar vrRendTrib13: Valor do rendimento tributável do Imposto de Renda referente ao 13º
                        salário - Tributação exclusiva. Validação: Deve ser maior ou igual a 0 (zero). Não
                        informar se {infoCRIRRF/tpCR}(2501_ideTrab_infoCRIRRF_tpCR) = [188951].
                    :ivar vrRendMoleGrave: Valor do rendimento isento por ser portador de moléstia grave
                        atestada por laudo médico. Validação: Deve ser maior ou igual a 0 (zero).
                    :ivar vrRendMoleGrave13: Valor do rendimento isento por ser portador de moléstia grave
                        atestada por laudo médico - 13º salário. Validação: Deve ser maior ou igual a 0 (zero).
                    :ivar vrRendIsen65: Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou
                        mais. Validação: Deve ser maior ou igual a 0 (zero).
                    :ivar vrRendIsen65Dec: Valor de parcela isenta de aposentadoria para beneficiário de 65 anos
                        ou mais - 13º salário. Validação: Deve ser maior ou igual a 0 (zero).
                    :ivar vrJurosMora: Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração
                        por exercício de emprego, cargo ou função. Validação: Deve ser maior ou igual a 0
                        (zero).
                    :ivar vrJurosMora13: Juros de mora recebidos, devidos pelo atraso no pagamento de
                        remuneração por exercício de emprego, cargo ou função - 13º salário. Validação: Deve ser
                        maior ou igual a 0 (zero).
                    :ivar vrRendIsenNTrib: Valor de outros rendimentos isentos ou não tributáveis. Validação:
                        Deve ser maior ou igual a 0 (zero). O campo não deve ser preenchido se
                        {infoCRIRRF/tpCR}(2501_ideTrab_infoCRIRRF_tpCR) = [188951].
                    :ivar descIsenNTrib: Descrição do rendimento isento ou não tributável informado em
                        {vrRendIsenNTrib}(./vrRendIsenNTrib). Validação: Preenchimento obrigatório e exclusivo
                        se {}(./vrRendIsenNTrib) &gt; 0.
                    :ivar vrPrevOficial: Valor referente à previdência oficial. Validação: Deve ser maior ou
                        igual a 0 (zero).
                    :ivar vrPrevOficial13: Valor referente à previdência oficial - 13º salário. Validação: Deve
                        ser maior ou igual a 0 (zero).
                    """

                    rendIsen0561: None | ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoIr.RendIsen0561 = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    vrRendTrib: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrRendTrib13: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrRendMoleGrave: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrRendMoleGrave13: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrRendIsen65: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrRendIsen65Dec: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrJurosMora: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrJurosMora13: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrRendIsenNTrib: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    descIsenNTrib: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "min_length": 1,
                            "max_length": 60,
                            "pattern": r".*[^\s].*",
                        },
                    )
                    vrPrevOficial: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vrPrevOficial13: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )

                    @dataclass(kw_only=True)
                    class RendIsen0561(CommonMixin):
                        """
                        :ivar vlrDiarias: Valor relativo a diárias. Validação: Deve ser maior ou igual a 0
                            (zero).
                        :ivar vlrAjudaCusto: Valor relativo a ajuda de custo. Validação: Deve ser maior ou igual
                            a 0 (zero).
                        :ivar vlrIndResContrato: Valor relativo a indenização e rescisão de contrato, inclusive
                            a título de PDV e acidentes de trabalho. Validação: Deve ser maior ou igual a 0
                            (zero).
                        :ivar vlrAbonoPec: Valor relativo ao abono pecuniário. Validação: Deve ser maior ou
                            igual a 0 (zero).
                        :ivar vlrAuxMoradia: Valor relativo ao auxílio moradia. Validação: Deve ser maior ou
                            igual a 0 (zero).
                        """

                        vlrDiarias: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrAjudaCusto: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrIndResContrato: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrAbonoPec: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrAuxMoradia: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )

                @dataclass(kw_only=True)
                class InfoRra(CommonMixin):
                    """
                    :ivar despProcJud: Detalhamento das despesas com processo judicial. CONDICAO_GRUPO: OC
                    :ivar ideAdv: Identificação dos advogados. CHAVE_GRUPO: {tpInsc}, {nrInsc} CONDICAO_GRUPO:
                        OC (se {vlrDespAdvogados}(../despProcJud_vlrDespAdvogados) &gt; 0); N (nos demais casos)
                    :ivar descRRA: Descrição dos Rendimentos Recebidos Acumuladamente - RRA.
                    :ivar qtdMesesRRA: Número de meses relativo aos Rendimentos Recebidos Acumuladamente - RRA.
                    """

                    despProcJud: None | ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoRra.DespProcJud = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    ideAdv: list[ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoRra.IdeAdv] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    descRRA: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    qtdMesesRRA: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )

                    @dataclass(kw_only=True)
                    class DespProcJud(CommonMixin):
                        """
                        :ivar vlrDespCustas: Preencher com o valor das despesas com custas judiciais. Validação:
                            Deve ser maior ou igual a 0 (zero).
                        :ivar vlrDespAdvogados: Preencher com o valor total das despesas com advogado(s).
                            Validação: Se o grupo {}(../ideAdv) for preenchido, o valor informado neste campo
                            deve ser maior ou igual à soma do(s) campo(s) {}(../ideAdv_vlrAdv) do grupo
                            {}(../ideAdv). Deve ser maior ou igual a 0 (zero). O não preenchimento do grupo
                            {}(../ideAdv) indica que o contribuinte declarante não possui as informações
                            detalhadas por advogado.
                        """

                        vlrDespCustas: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrDespAdvogados: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )

                    @dataclass(kw_only=True)
                    class IdeAdv(CommonMixin):
                        """
                        :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme
                            Tabela 05.
                        :ivar nrInsc: Informar o número de inscrição do advogado. Validação: Deve ser um número
                            de inscrição válido, de acordo com o tipo de inscrição indicado no campo
                            {ideAdv/tpInsc}(./tpInsc), considerando as particularidades aplicadas à informação
                            de CNPJ de órgão público em S-1000. Se {ideAdv/tpInsc}(./tpInsc) = [1], deve possuir
                            14 (catorze) algarismos e, no caso de declarante pessoa jurídica, ser diferente do
                            CNPJ base do empregador (exceto se {ideEmpregador/nrInsc}(/ideEmpregador_nrInsc)
                            tiver 14 (catorze) algarismos). Se {ideAdv/tpInsc}(./tpInsc) = [2], deve possuir 11
                            (onze) algarismos e, no caso de declarante pessoa física, ser diferente do CPF do
                            empregador.
                        :ivar vlrAdv: Valor da despesa com o advogado, se houver.
                        """

                        tpInsc: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        nrInsc: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrAdv: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )

                @dataclass(kw_only=True)
                class DedDepen(CommonMixin):
                    """
                    :ivar tpRend: Tipo de rendimento.
                    :ivar cpfDep: Informar o número de inscrição do dependente no CPF. Validação: Deve ser um
                        CPF de dependente cadastrado no eSocial (S-2200/S-2205/S-2300 ou no grupo
                        {infoDep}(2501_ideTrab_infoIRComplem_infoDep)).
                    :ivar vlrDeducao: Preencher com o valor da dedução da base de cálculo. Validação: O valor
                        informado neste campo deve ser menor ou igual ao valor unitário da dedução por
                        dependente definido na legislação. Deve ser maior que 0 (zero). Em caso de
                        inconsistência na validação, o arquivo será aceito, porém com alerta ao contribuinte.
                    """

                    tpRend: None | DedDepenTpRend = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    cpfDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vlrDeducao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )

                @dataclass(kw_only=True)
                class PenAlim(CommonMixin):
                    """
                    :ivar tpRend: Tipo de rendimento. Validação: Preenchimento com valor [18] obrigatório e
                        exclusivo quando {tpCR}(../tpCR) = [188951].
                    :ivar cpfDep: Número do CPF do dependente/beneficiário da pensão alimentícia. Validação:
                        Deve ser um CPF de dependente cadastrado no eSocial (S-2200/S-2205/S-2300 ou no grupo
                        {infoDep}(2501_ideTrab_infoIRComplem_infoDep)).
                    :ivar vlrPensao: Valor relativo à dedução do rendimento tributável correspondente a
                        pagamento de pensão alimentícia. Validação: Deve ser maior que 0 (zero).
                    """

                    tpRend: None | PenAlimTpRend = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    cpfDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    vlrPensao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )

                @dataclass(kw_only=True)
                class InfoProcRet(CommonMixin):
                    """
                    :ivar infoValores: Informações de valores relacionados a não retenção de tributos ou a
                        depósitos judiciais. CHAVE_GRUPO: {indApuracao} CONDICAO_GRUPO: OC
                    :ivar tpProcRet: Preencher com o código correspondente ao tipo de processo.
                    :ivar nrProcRet: Informar o número do processo administrativo/judicial. Validação: Deve ser
                        um número de processo administrativo ou judicial válido e existente na Tabela de
                        Processos (S-1070).
                    :ivar codSusp: Código do indicativo da suspensão, atribuído pelo empregador em S-1070.
                        Validação: Preenchimento obrigatório se houver informação de
                        {codSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_codSusp) em S-1070. Se
                        informado, deve constar na Tabela de Processos (S-1070), campo
                        {codSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_codSusp), vinculado ao número do
                        processo informado em {nrProcRet}(./nrProcRet).
                    """

                    infoValores: list[ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoProcRet.InfoValores] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 2,
                        },
                    )
                    tpProcRet: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    nrProcRet: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    codSusp: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoValores(CommonMixin):
                        """
                        :ivar dedSusp: Detalhamento das deduções com exigibilidade suspensa. CHAVE_GRUPO:
                            {indTpDeducao} CONDICAO_GRUPO: OC
                        :ivar indApuracao: Indicativo de período de apuração.
                        :ivar vlrNRetido: Valor da retenção que deixou de ser efetuada em função de processo
                            administrativo ou judicial. Validação: Deve ser maior que 0 (zero).
                        :ivar vlrDepJud: Valor do depósito judicial em função de processo administrativo ou
                            judicial. Validação: Informação permitida apenas se
                            {indDeposito}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indDeposito) informado
                            em S-1070 for igual a [S]. Se informado, deve ser maior que 0 (zero).
                        :ivar vlrCmpAnoCal: Valor da compensação relativa ao ano calendário em função de
                            processo judicial. Validação: Informação permitida apenas se
                            {tpProcRet}(../tpProcRet) = [2]. Se informado, deve ser maior que 0 (zero).
                        :ivar vlrCmpAnoAnt: Valor da compensação relativa a anos anteriores em função de
                            processo judicial. Validação: Informação permitida apenas se
                            {tpProcRet}(../tpProcRet) = [2]. Se informado, deve ser maior que 0 (zero).
                        :ivar vlrRendSusp: Valor do rendimento com exigibilidade suspensa. Validação: Se
                            {indApuracao}(./indApuracao) = [1], não pode ser maior que
                            {vrRendTrib}(2501_ideTrab_infoCRIRRF_infoIR_vrRendTrib). Se
                            {indApuracao}(./indApuracao) = [2], não pode ser maior que
                            {vrRendTrib13}(2501_ideTrab_infoCRIRRF_infoIR_vrRendTrib13). Se informado, deve ser
                            maior que 0 (zero).
                        """

                        dedSusp: list[ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoProcRet.InfoValores.DedSusp] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 25,
                            },
                        )
                        indApuracao: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrNRetido: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrDepJud: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrCmpAnoCal: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrCmpAnoAnt: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )
                        vlrRendSusp: None | str = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                            },
                        )

                        @dataclass(kw_only=True)
                        class DedSusp(CommonMixin):
                            """
                            :ivar benefPen: Informação das deduções suspensas por dependentes e beneficiários da
                                pensão alimentícia CHAVE_GRUPO: {cpfDep} CONDICAO_GRUPO: OC
                            :ivar indTpDeducao: Indicativo do tipo de dedução.
                            :ivar vlrDedSusp: Valor da dedução da base de cálculo do imposto de renda com
                                exigibilidade suspensa. Validação: Informação permitida apenas se
                                {vlrRendSusp}(../vlrRendSusp) &gt; 0. Se {indTpDeducao}(./indTpDeducao) = [5,
                                7], e o grupo {benefPen}(./benefPen) for preenchido, o valor informado neste
                                campo deve ser a soma do(s) campo(s) {vlrDepenSusp}(./benefPen_vlrDepenSusp) do
                                grupo {benefPen}(./benefPen). Deve ser maior que 0 (zero). O não preenchimento
                                do grupo {benefPen}(./benefPen) indica que o contribuinte declarante não possui
                                as informações detalhadas por dependente/alimentando.
                            """

                            benefPen: list[
                                ESocial.EvtContProc.IdeTrab.InfoCrirrf.InfoProcRet.InfoValores.DedSusp.BenefPen
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 99,
                                },
                            )
                            indTpDeducao: None | DedSuspIndTpDeducao = field(
                                default=None,
                                metadata={
                                    "type": "Attribute",
                                },
                            )
                            vlrDedSusp: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Attribute",
                                },
                            )

                            @dataclass(kw_only=True)
                            class BenefPen(CommonMixin):
                                """
                                :ivar cpfDep: Número de inscrição no CPF. Validação: Deve ser um CPF de
                                    dependente cadastrado no eSocial (S-2200/S-2205/S-2300 ou no grupo
                                    {infoDep}(2501_ideTrab_infoIRComplem_infoDep)).
                                :ivar vlrDepenSusp: Valor da dedução relativa a dependentes ou a pensão
                                    alimentícia com exigibilidade suspensa. Validação: Deve ser maior que 0
                                    (zero).
                                """

                                cpfDep: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Attribute",
                                    },
                                )
                                vlrDepenSusp: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Attribute",
                                    },
                                )

            @dataclass(kw_only=True)
            class InfoIrcomplem(CommonMixin):
                """
                :ivar infoDep: Informações de dependentes não cadastrados pelo S-2200/S-2205/S-2300.
                    CHAVE_GRUPO: {cpfDep} CONDICAO_GRUPO: OC
                :ivar dtLaudo: Data da moléstia grave atribuída pelo laudo. Validação: Não pode ser anterior ao
                    ano de 1900. Deve ser menor ou igual a {}(2501_ideProc_perApurPgto).
                """

                infoDep: list[ESocial.EvtContProc.IdeTrab.InfoIrcomplem.InfoDep] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 999,
                    },
                )
                dtLaudo: None | XmlDate = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

                @dataclass(kw_only=True)
                class InfoDep(CommonMixin):
                    """
                    :ivar cpfDep: Número de inscrição no CPF. Validação: Deve ser um CPF válido e diferente do
                        CPF do declarante pessoa física ({ideEmpregador/nrInsc}(/ideEmpregador_nrInsc)) e do
                        beneficiário ({cpfTrab}(../../cpfTrab)).
                    :ivar dtNascto: Preencher com a data de nascimento. Validação: Deve ser maior ou igual que
                        01/01/1890 e menor ou igual à data atual.
                    :ivar nome: Nome do dependente.
                    :ivar depIRRF: Somente informar este campo em caso de dependente do trabalhador para fins de
                        dedução de seu rendimento tributável pelo Imposto de Renda.
                    :ivar tpDep: Tipo de dependente. Validação: Preenchimento obrigatório e exclusivo se
                        {depIRRF}(./depIRRF) = [S]. Deve ser um código válido e existente na Tabela 07.
                    :ivar descrDep: Informar a descrição da dependência. Validação: Informação obrigatória e
                        exclusiva se {tpDep}(./tpDep) = [99].
                    """

                    cpfDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    dtNascto: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    nome: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    depIRRF: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    tpDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
                    descrDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                        },
                    )
