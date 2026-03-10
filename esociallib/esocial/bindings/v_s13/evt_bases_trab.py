from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_03_00"


class CalcTercTpCr(Enum):
    """
    Código de Receita - CR da contribuição descontada do trabalhador.

    :cvar VALUE_121802: Contribuição ao SEST, descontada do transportador autônomo
    :cvar VALUE_122102: Contribuição ao SENAT, descontada do transportador autônomo
    """

    VALUE_121802 = 121802
    VALUE_122102 = 122102


class DetInfoPerRefTpVrPerRef(Enum):
    """
    Tipo de valor que influi na apuração da contribuição devida.

    :cvar VALUE_11: Base de cálculo da contribuição previdenciária normal
    :cvar VALUE_12: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 15 anos de contribuição
    :cvar VALUE_13: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 20 anos de contribuição
    :cvar VALUE_14: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 25 anos de contribuição
    :cvar VALUE_15: Base de cálculo da contribuição previdenciária adicional normal - Exclusiva do empregador
    :cvar VALUE_16: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 15 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_17: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 20 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_18: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 25 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_19: Base de cálculo da contribuição previdenciária exclusiva do empregado
    :cvar VALUE_21: Valor total descontado do trabalhador para recolhimento à Previdência Social
    :cvar VALUE_22: Valor descontado do trabalhador para recolhimento ao SEST
    :cvar VALUE_23: Valor descontado do trabalhador para recolhimento ao SENAT
    :cvar VALUE_31: Valor pago ao trabalhador a título de salário-família
    :cvar VALUE_32: Valor pago ao trabalhador a título de salário-maternidade
    """

    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_31 = 31
    VALUE_32 = 32


class InfoBaseCsTpValor(Enum):
    """
    Tipo de valor que influi na apuração da contribuição devida.

    :cvar VALUE_11: Base de cálculo da contribuição previdenciária normal
    :cvar VALUE_12: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 15 anos de contribuição
    :cvar VALUE_13: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 20 anos de contribuição
    :cvar VALUE_14: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 25 anos de contribuição
    :cvar VALUE_15: Base de cálculo da contribuição previdenciária adicional normal - Exclusiva do empregador
    :cvar VALUE_16: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 15 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_17: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 20 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_18: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 25 anos de contribuição - Exclusiva do empregador
    :cvar VALUE_19: Base de cálculo da contribuição previdenciária exclusiva do empregado
    :cvar VALUE_21: Valor total descontado do trabalhador para recolhimento à Previdência Social
    :cvar VALUE_22: Valor descontado do trabalhador para recolhimento ao SEST
    :cvar VALUE_23: Valor descontado do trabalhador para recolhimento ao SENAT
    :cvar VALUE_31: Valor pago ao trabalhador a título de salário-família
    :cvar VALUE_32: Valor pago ao trabalhador a título de salário-maternidade
    :cvar VALUE_41: Base de cálculo da contribuição previdenciária normal - Categorias 107 e 108
    :cvar VALUE_42: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 15 anos de contribuição - Categorias 107 e 108
    :cvar VALUE_43: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 20 anos de contribuição - Categorias 107 e 108
    :cvar VALUE_44: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 25 anos de contribuição - Categorias 107 e 108
    :cvar VALUE_45: Base de cálculo da contribuição previdenciária adicional normal - Exclusiva do empregador -
        Categorias 107 e 108
    :cvar VALUE_46: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 15 anos de contribuição - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_47: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 20 anos de contribuição - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_48: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 25 anos de contribuição - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_49: Base de cálculo da contribuição previdenciária exclusiva do empregado - Categorias 107 e 108
    :cvar VALUE_51: Base de cálculo da contribuição previdenciária normal - 13º salário - Lei 14.973/2024
    :cvar VALUE_52: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 15 anos de contribuição - 13º salário - Lei 14.973/2024
    :cvar VALUE_53: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 20 anos de contribuição - 13º salário - Lei 14.973/2024
    :cvar VALUE_54: Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios
        de aposentadoria especial após 25 anos de contribuição - 13º salário - Lei 14.973/2024
    :cvar VALUE_71: Incidência suspensa em decorrência de decisão judicial - Base de cálculo - BC da
        Contribuição Previdenciária - CP normal - 13º salário - Lei 14.973/2024
    :cvar VALUE_72: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 15
        anos de trabalho - 13º salário - Lei 14.973/2024
    :cvar VALUE_73: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 20
        anos de trabalho - 13º salário - Lei 14.973/2024
    :cvar VALUE_74: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 25
        anos de trabalho - 13º salário - Lei 14.973/2024
    :cvar VALUE_81: Incidência suspensa em decorrência de decisão judicial - BC CP normal - Categorias 107 e 108
    :cvar VALUE_82: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 15
        anos de trabalho - Categorias 107 e 108
    :cvar VALUE_83: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 20
        anos de trabalho - Categorias 107 e 108
    :cvar VALUE_84: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 25
        anos de trabalho - Categorias 107 e 108
    :cvar VALUE_85: Incidência suspensa em decorrência de decisão judicial - BC CP normal - Exclusiva do
        empregador - Categorias 107 e 108
    :cvar VALUE_86: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 15
        anos de trabalho - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_87: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 20
        anos de trabalho - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_88: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 25
        anos de trabalho - Exclusiva do empregador - Categorias 107 e 108
    :cvar VALUE_91: Incidência suspensa em decorrência de decisão judicial - BC CP normal
    :cvar VALUE_92: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 15
        anos de trabalho
    :cvar VALUE_93: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 20
        anos de trabalho
    :cvar VALUE_94: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 25
        anos de trabalho
    :cvar VALUE_95: Incidência suspensa em decorrência de decisão judicial - BC CP normal - Exclusiva do
        empregador
    :cvar VALUE_96: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 15
        anos de trabalho - Exclusiva do empregador
    :cvar VALUE_97: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 20
        anos de trabalho - Exclusiva do empregador
    :cvar VALUE_98: Incidência suspensa em decorrência de decisão judicial - BC CP aposentadoria especial aos 25
        anos de trabalho - Exclusiva do empregador
    """

    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_74 = 74
    VALUE_81 = 81
    VALUE_82 = 82
    VALUE_83 = 83
    VALUE_84 = 84
    VALUE_85 = 85
    VALUE_86 = 86
    VALUE_87 = 87
    VALUE_88 = 88
    VALUE_91 = 91
    VALUE_92 = 92
    VALUE_93 = 93
    VALUE_94 = 94
    VALUE_95 = 95
    VALUE_96 = 96
    VALUE_97 = 97
    VALUE_98 = 98


class InfoBasePisPasepInd13(Enum):
    """
    Indicativo de 13° salário.

    Validação: Se {indApuracao}(/ideEvento_perApur) = [2], preencher com [1].

    :cvar VALUE_0: Mensal
    :cvar VALUE_1: 13° salário
    """

    VALUE_0 = 0
    VALUE_1 = 1


class InfoBasePisPasepTpValorPisPasep(Enum):
    """
    Tipo de valor que influi na apuração da contribuição devida.

    :cvar VALUE_11: Base de cálculo da contribuição para o PIS/PASEP
    :cvar VALUE_91: Incidência suspensa em decorrência de decisão judicial - BC PIS/PASEP
    """

    VALUE_11 = 11
    VALUE_91 = 91


class InfoCpCalcTpCr(Enum):
    """
    Código de Receita - CR da contribuição descontada do trabalhador.

    Validação: Se {indApuracao}(5001_ideEvento_indApuracao) = [2], deve ser igual a [108221, 108222, 108223,
    108224, 108225, 109921, 109922].

    :cvar VALUE_108201: Contribuição Previdenciária - CP descontada do segurado empregado/avulso
    :cvar VALUE_108202: CP descontada do segurado empregado rural curto prazo - Lei 11.718/2008
    :cvar VALUE_108203: CP descontada do segurado empregado doméstico
    :cvar VALUE_108204: CP descontada do segurado especial curto prazo - Lei 11.718/2008
    :cvar VALUE_108205: CP descontada do segurado empregado do segurado especial
    :cvar VALUE_108207: CP descontada do segurado empregado do MEI
    :cvar VALUE_108221: CP descontada do segurado empregado/avulso 13° salário
    :cvar VALUE_108222: CP descontada do segurado empregado rural curto prazo 13° salário - Lei 11.718/2008
    :cvar VALUE_108223: CP descontada do segurado empregado doméstico 13° salário
    :cvar VALUE_108224: CP descontada do segurado especial curto prazo 13° salário - Lei 11.718/2008
    :cvar VALUE_108225: CP descontada do segurado empregado do segurado especial 13° salário
    :cvar VALUE_109901: CP descontada do contribuinte individual, alíquota de 11%
    :cvar VALUE_109902: CP descontada do contribuinte individual, alíquota de 20%
    :cvar VALUE_109921: CP descontada do contribuinte individual, alíquota de 11% - 13º salário
    :cvar VALUE_109922: CP descontada do contribuinte individual, alíquota de 20% - 13º salário
    :cvar VALUE_160601: Empréstimo Consignado do Trabalhador, Lei nº 10.820/2003 (aplicável apenas ao DAE dos
        módulos simplificados)
    """

    VALUE_108201 = 108201
    VALUE_108202 = 108202
    VALUE_108203 = 108203
    VALUE_108204 = 108204
    VALUE_108205 = 108205
    VALUE_108207 = 108207
    VALUE_108221 = 108221
    VALUE_108222 = 108222
    VALUE_108223 = 108223
    VALUE_108224 = 108224
    VALUE_108225 = 108225
    VALUE_109901 = 109901
    VALUE_109902 = 109902
    VALUE_109921 = 109921
    VALUE_109922 = 109922
    VALUE_160601 = 160601


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-5001 - Informações das Contribuições Sociais por Trabalhador.

    :ivar evtBasesTrab: Evento Informações das Contribuições Sociais por Trabalhador. CHAVE_GRUPO: {Id}
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtBasesTrab/v_S_01_03_00"

    evtBasesTrab: ESocial.EvtBasesTrab = field(
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
    class EvtBasesTrab(CommonMixin):
        """
        :ivar ideEvento: Identificação do evento de retorno. CHAVE_GRUPO: {indApuracao*}, {perApur*}
        :ivar ideEmpregador:
        :ivar ideTrabalhador: Identificação do trabalhador. CHAVE_GRUPO: {cpfTrab*}
        :ivar infoCpCalc: Cálculo da contribuição previdenciária do segurado DESCRICAO_COMPLETA:Cálculo da
            contribuição previdenciária do segurado, incidente sobre a remuneração do período de apuração e de
            períodos anteriores informada nos eventos S-1200, S-2299 e S-2399. CHAVE_GRUPO: {tpCR}
            CONDICAO_GRUPO: OC
        :ivar infoCp: Informações sobre bases e valores das contribuições sociais DESCRICAO_COMPLETA:Informações
            sobre bases de cálculo, descontos e deduções de contribuições sociais devidas à Previdência Social e
            a Outras Entidades e Fundos, referentes à remuneração do período de apuração e de períodos
            anteriores informada nos eventos S-1200, S-2299 e S-2399. CONDICAO_GRUPO: OC
        :ivar infoPisPasep: Informações sobre bases de cálculo do PIS/PASEP. DESCRICAO_COMPLETA:Informações
            sobre bases de cálculo do PIS/PASEP informadas nos eventos S-1200, S-2299, S-2399 ou S-1202.
            CONDICAO_GRUPO: OC (se {}(1000_infoEmpregador_inclusao_infoCadastro_indTribFolhaPisPasep) em S-1000
            = [S], {}(5001_ideEvento_perApur) &gt;= [2025-01] e
            {ideEmpregador/tpInsc}(5001_ideEmpregador_tpInsc) = [1], exceto se
            {}(5001_infoCp_ideEstabLot_infoCategIncid_codCateg) = [5XX, 7XX, 9XX]); N (nos demais casos)
        :ivar Id:
        """

        ideEvento: ESocial.EvtBasesTrab.IdeEvento = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideTrabalhador: ESocial.EvtBasesTrab.IdeTrabalhador = field(
            metadata={
                "type": "Element",
            }
        )
        infoCpCalc: list[ESocial.EvtBasesTrab.InfoCpCalc] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 9,
            },
        )
        infoCp: None | ESocial.EvtBasesTrab.InfoCp = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        infoPisPasep: None | ESocial.EvtBasesTrab.InfoPisPasep = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass(kw_only=True)
        class IdeEvento(CommonMixin):
            """
            :ivar nrRecArqBase: Preencher com o número do recibo do arquivo que deu origem ao presente arquivo
                de retorno ao empregador. Validação: Deve ser um recibo de entrega válido, correspondente ao
                arquivo que deu origem ao presente arquivo de retorno (S-1200, S-1202, S-2299, S-2399 ou
                S-3000).
            :ivar indApuracao:
            :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência das informações, se
                {indApuracao}(./indApuracao) for igual a [1], ou apenas o ano (formato AAAA), se
                {indApuracao}(./indApuracao) for igual a [2].
            """

            nrRecArqBase: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indApuracao: str = field(
                metadata={
                    "type": "Element",
                }
            )
            perApur: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class IdeTrabalhador(CommonMixin):
            """
            :ivar cpfTrab:
            :ivar infoCompl: Informações complementares do trabalhador e do contrato. CONDICAO_GRUPO: OC
            :ivar procJudTrab: Processos judiciais do trabalhador DESCRICAO_COMPLETA:Informações sobre processos
                judiciais do trabalhador com decisão favorável quanto à não incidência ou alterações na
                incidência de contribuição previdenciária. CHAVE_GRUPO: {nrProcJud} CONDICAO_GRUPO: OC
            """

            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            infoCompl: None | ESocial.EvtBasesTrab.IdeTrabalhador.InfoCompl = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            procJudTrab: list[ESocial.EvtBasesTrab.IdeTrabalhador.ProcJudTrab] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class InfoCompl(CommonMixin):
                """
                :ivar sucessaoVinc: Grupo de informações da sucessão de vínculo trabalhista
                    DESCRICAO_COMPLETA:Grupo de informações da sucessão de vínculo trabalhista. Evento de
                    origem: S-1200. CONDICAO_GRUPO: OC
                :ivar infoInterm: Informações relativas ao trabalho intermitente DESCRICAO_COMPLETA:Informações
                    relativas ao trabalho intermitente. Evento de origem: S-1200 ou S-2299. CHAVE_GRUPO: {dia}
                    CONDICAO_GRUPO: OC
                :ivar infoComplCont: Informações complementares contratuais do trabalhador
                    DESCRICAO_COMPLETA:Informações complementares contratuais do trabalhador. Evento de origem:
                    S-1200. CHAVE_GRUPO: {codCBO}, {natAtividade}, {qtdDiasTrab} CONDICAO_GRUPO: OC
                """

                sucessaoVinc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoInterm: list[ESocial.EvtBasesTrab.IdeTrabalhador.InfoCompl.InfoInterm] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 31,
                    },
                )
                infoComplCont: list[ESocial.EvtBasesTrab.IdeTrabalhador.InfoCompl.InfoComplCont] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoInterm(CommonMixin):
                    """
                    :ivar dia: Dia do mês efetivamente trabalhado pelo empregado com contrato de trabalho
                        intermitente.
                    :ivar hrsTrab: Horas trabalhadas no dia pelo empregado com contrato de trabalho
                        intermitente, no formato HHMM.
                    """

                    dia: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    hrsTrab: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class InfoComplCont(CommonMixin):
                    """
                    :ivar codCBO: Classificação Brasileira de Ocupações - CBO.
                    :ivar natAtividade: Natureza da atividade.
                    :ivar qtdDiasTrab: Informação prestada exclusivamente pelo segurado especial em caso de
                        contratação de contribuinte individual, indicando a quantidade de dias trabalhados pelo
                        mesmo.
                    """

                    codCBO: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    natAtividade: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    qtdDiasTrab: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

            @dataclass(kw_only=True)
            class ProcJudTrab(CommonMixin):
                """
                :ivar nrProcJud: Informar o número do processo judicial. Origem: campo {nrProcJud} de S-1200,
                    S-2299 ou S-2399, se {tpTrib} no evento de origem for igual a [2].
                :ivar codSusp: Código do indicativo da suspensão, atribuído pelo empregador em S-1070. Origem:
                    campo {codSusp} de S-1200, S-2299 ou S-2399, se {tpTrib} no evento de origem for igual a
                    [2].
                """

                nrProcJud: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                codSusp: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

        @dataclass(kw_only=True)
        class InfoCpCalc(CommonMixin):
            """
            :ivar tpCR:
            :ivar vrCpSeg: Valor da contribuição do segurado, devida à Previdência Social, calculada segundo as
                regras da legislação em vigor, por CR. Validação: 1. Se {indMV} do S-1200/S-2299/S-2399 = [3],
                {vrCpSeg}(./vrCpSeg) = [0]; portanto, não há CR. 2. Se {indMV} do S-1200/S-2299/S-2399 = [1, 2],
                efetuar o somatório das ocorrências do campo {vlrRemunOE} e o somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) = [11, 12, 13, 14, 19],
                resultando em [TotalRemun]. Este procedimento visa a identificação da(s) alíquota(s)
                aplicável(eis): 2.1. Se {indMV} do S-1200/S-2299/S-2399 = [1], aplicar a(s) alíquota(s) conforme
                a categoria do segurado sobre a remuneração paga pelo declarante (somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) = [11, 12, 13, 14, 19]),
                observado o limite máximo do salário de contribuição. 2.2. Se {indMV} do S-1200/S-2299/S-2399 =
                [2]: a) Se [TotalRemun] ultrapassar o limite máximo do salário de contribuição, aplicar a(s)
                alíquota(s) conforme a categoria do segurado sobre a diferença entre o referido limite máximo e
                o somatório das ocorrências do campo {vlrRemunOE}. Para os períodos de apuração iguais ou
                posteriores a 03/2020, observar a(s) faixa(s) de remuneração já tributada(s) em outra(s)
                empresa(s) nas categorias empregado/avulso/agente público. b) Se [TotalRemun] for inferior ao
                limite máximo do salário de contribuição: b1) Para as categorias empregado/avulso/agente
                público: somar {vlrRemunOE} destas mesmas categorias com o somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) = [11, 12, 13, 14, 19] e
                aplicar a(s) alíquota(s). Para os períodos de apuração iguais ou posteriores a 03/2020, observar
                a(s) faixa(s) de remuneração já tributada(s) em outra(s) empresa(s) nas categorias
                empregado/avulso/agente público. b2) Para categoria contribuinte individual: aplicar a alíquota
                sobre a remuneração paga pelo declarante (somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) = [11, 12, 13, 14, 19]). 3.
                Se não for informado o grupo {infoMV} do S-1200/S-2299/S-2399: a) Se o trabalhador presta
                serviço para a empresa declarante em apenas uma categoria
                ({codCateg}(5001_infoCp_ideEstabLot_infoCategIncid_codCateg)), efetuar o somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) = [11, 12, 13, 14, 19] e
                aplicar a(s) alíquota(s) conforme a categoria. b) Se o trabalhador presta serviço para a empresa
                declarante em mais de uma categoria
                ({codCateg}(5001_infoCp_ideEstabLot_infoCategIncid_codCateg)): I. Efetuar o somatório de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) = [11, 12, 13, 14, 19] para
                todas as categorias de segurado empregado/avulso/agente público e aplicar a(s) alíquota(s)
                correta(s) conforme faixa salarial, observado o limite máximo do salário de contribuição. II.
                Caso o somatório do item I não tenha atingido o limite máximo do salário de contribuição,
                efetuar o somatório de {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) quando
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) = [11, 12, 13, 14, 19] para
                todas as categorias diferentes de segurado empregado e aplicar a alíquota correta conforme a
                categoria, observado o limite máximo do salário de contribuição. OBS.: a) No caso de
                {indApuracao}(5001_ideEvento_indApuracao) = [1], o cálculo deve ser efetuado separadamente para
                {infoBaseCS/ind13}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_ind13) = [0] e
                {infoBaseCS/ind13}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_ind13) = [1]. A soma de
                ambos os cálculos deve corresponder ao valor de {vrCpSeg}(./vrCpSeg). b) Aplica-se a alíquota de
                20% para o cálculo da contribuição previdenciária a ser descontada de remuneração de trabalhador
                pertencente às categorias [731, 734], quando o empregador for cooperativa de trabalho
                ({indCoop}(1000_infoEmpregador_inclusao_infoCadastro_indCoop) em S-1000 = [1]), ou pertencente
                ao grupo "Contribuinte Individual", quando o Empregador tiver {classTrib}(5001_infoCp_classTrib)
                = [04, 70, 80]; ou de trabalhador pertencente à categoria = [902] quando o tipo de lotação
                tributária ({tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) em S-1020) for igual a
                [92]. Caso o trabalhador receba remuneração da empresa em outra categoria do grupo "Contribuinte
                Individual", primeiro deve ser aplicado o desconto sobre essa categoria (7XX) e depois sobre a
                remuneração das categorias [731, 734], observado o limite máximo do salário de contribuição. c)
                {vrCpSeg}(./vrCpSeg) deve ser igual a {vrDescSeg}(./vrDescSeg) nas seguintes situações: c1) Se
                houver informações em {infoPerAnt} na composição de
                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor); c2) Se houver informação de
                {procJudTrab} com {tpTrib} = [2] nos eventos que contenham informações de remuneração (S-1200,
                S-2299 e S-2399); c3) Se houver processo do empregador informado em S-1010, contestando
                incidência de contribuição previdenciária em rubricas utilizadas na composição da remuneração do
                trabalhador; c4) Se, no período de apuração mensal, houver remuneração referente a 13º salário
                ({codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [12, 14, 16, 22, 26,
                32, 92, 94, 96, 98]). Nesse caso, o campo {vrCpSeg}(./vrCpSeg) será igual ao valor calculado
                sobre a remuneração mensal acrescido do desconto sobre a remuneração relativa a 13° salário
                informado pelo empregador; c5) Se {procEmi} do evento S-1200/S-2299/S-2399 for igual a [2, 4,
                22]; c6) Para as categorias do grupo "Contribuinte Individual" (7XX), se o campo
                {dtTrans11096}(1000_infoEmpregador_inclusao_infoCadastro_dtTrans11096) em S-1000 for informado.
                d) No caso de trabalhador categoria = [102], utilizar somente a alíquota de 8%, observado o
                limite máximo do salário de contribuição. e) No caso de empregador com
                {classTrib}(5001_infoCp_classTrib) = [21, 22, 60], não calcular para a categoria do grupo
                "Contribuinte Individual" (7XX). O valor deve ser zerado. f) Não calcular quando a categoria do
                trabalhador for [741] (MEI). O valor deve ser zerado. g) Não calcular quando a lotação
                tributária for [91]. O valor deve ser zerado.
            :ivar vrDescSeg: Valor efetivamente descontado do segurado, correspondente a
                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) = [21] do correspondente
                {infoCpCalc/tpCR}(./tpCR).
            """

            tpCR: InfoCpCalcTpCr = field(
                metadata={
                    "type": "Element",
                }
            )
            vrCpSeg: str = field(
                metadata={
                    "type": "Element",
                }
            )
            vrDescSeg: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class InfoCp(CommonMixin):
            """
            :ivar classTrib:
            :ivar ideEstabLot: Identificação do estabelecimento ou obra e da lotação tributária
                DESCRICAO_COMPLETA:Identificação do estabelecimento ou obra de construção civil e da lotação
                tributária. CHAVE_GRUPO: {tpInsc}, {nrInsc}, {codLotacao}
            """

            classTrib: str = field(
                metadata={
                    "type": "Element",
                    "pattern": r"\d{2}",
                }
            )
            ideEstabLot: list[ESocial.EvtBasesTrab.InfoCp.IdeEstabLot] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class IdeEstabLot(CommonMixin):
                """
                :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.
                    Evento de origem: S-1200, S-2299 ou S-2399.
                :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideEstabLot/tpInsc}(./tpInsc). Evento de origem: S-1200, S-2299 ou
                    S-2399.
                :ivar codLotacao: Informar o código atribuído pelo empregador para a lotação tributária. Evento
                    de origem: S-1200, S-2299 ou S-2399.
                :ivar infoCategIncid: Informações relativas à matrícula e categoria do trabalhador e tipos de
                    incidências. CHAVE_GRUPO: {matricula}, {codCateg}, {indSimples}
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
                codLotacao: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                infoCategIncid: list[ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 10,
                    },
                )

                @dataclass(kw_only=True)
                class InfoCategIncid(CommonMixin):
                    """
                    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor
                        público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão.
                        Evento de origem: S-1200, S-2299 ou S-2399.
                    :ivar codCateg: Preencher com o código da categoria do trabalhador, conforme Tabela 01.
                        Validação: Se o evento de origem for S-1200, retornar o código de categoria informado
                        nesse evento. Se o evento de origem for S-2299 ou S-2399, retornar o código de categoria
                        existente no Registro de Eventos Trabalhistas - RET.
                    :ivar indSimples: Indicador de contribuição substituída. Evento de origem: S-1200, S-2299 ou
                        S-2399.
                    :ivar infoBaseCS: Informações sobre bases de cálculo, descontos e deduções de CS
                        DESCRICAO_COMPLETA:Informações sobre bases de cálculo, descontos e deduções de
                        contribuições sociais devidas à Previdência Social e a Outras Entidades e Fundos. Evento
                        de origem: S-1200, S-2299 ou S-2399. CHAVE_GRUPO: {ind13}, {tpValor} CONDICAO_GRUPO: N
                        (se {classTrib}(5001_infoCp_classTrib) = [10] e {codCateg}(../codCateg) = [202]); O (nos
                        demais casos)
                    :ivar calcTerc: Cálculo das contribuições sociais devidas a Outras Entidades e Fundos.
                        CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC (se
                        {ideEmpregador/tpInsc}(5001_ideEmpregador_tpInsc) = [1]); N (nos demais casos)
                    :ivar infoPerRef: Informações de remuneração por período de referência. CONDICAO_GRUPO: OC
                        CHAVE_GRUPO: {perRef}
                    """

                    matricula: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    codCateg: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    indSimples: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoBaseCS: list[ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.InfoBaseCs] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    calcTerc: list[ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.CalcTerc] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 2,
                        },
                    )
                    infoPerRef: list[ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.InfoPerRef] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoBaseCs(CommonMixin):
                        """
                        :ivar ind13:
                        :ivar tpValor:
                        :ivar valor: Valor da base de cálculo, dedução ou desconto da contribuição social devida
                            à Previdência Social ou a Outras Entidades e Fundos, conforme definido no campo
                            {tpValor}(./tpValor). Validação: Deve ser maior que 0 (zero). Deve corresponder ao
                            somatório dos valores informados no campo {vrRubr} em S-1200 e S-2299 (grupos
                            {infoPerApur} e {infoPerAnt}), e também em S-2399, obedecendo ao que segue: a) Somar
                            os valores das rubricas cujo {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr)
                            em S-1010 seja igual a [1, 3] e subtrair os valores das rubricas cujo
                            {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a [2,
                            4], observando a tabela de relacionamento abaixo: {tpValor}(./tpValor) = [11]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado); {tpValor}(./tpValor) = [12]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12] e
                            {grauExp} em S-1200/S-2299 = [2]; {tpValor}(./tpValor) = [13]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12] e
                            {grauExp} em S-1200/S-2299 = [3]; {tpValor}(./tpValor) = [14]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12] e
                            {grauExp} em S-1200/S-2299 = [4]; {tpValor}(./tpValor) = [15]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado); {tpValor}(./tpValor) = [16]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14] e
                            {grauExp} em S-1200/S-2299 = [2]; {tpValor}(./tpValor) = [17]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14] e
                            {grauExp} em S-1200/S-2299 = [3]; {tpValor}(./tpValor) = [18]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14] e
                            {grauExp} em S-1200/S-2299 = [4]; {tpValor}(./tpValor) = [19],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [15, 16, 21,
                            22]; {tpValor}(./tpValor) = [31],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [51];
                            {tpValor}(./tpValor) = [32],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [21, 22] ou
                            ({natRubr}(1010_infoRubrica_inclusao_dadosRubrica_natRubr) em S-1010 = [4050, 4051]
                            com {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [9X]);
                            {tpValor}(./tpValor) = [41]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado), observado o limite para
                            {codCateg}(../codCateg) = [107, 108]; {tpValor}(./tpValor) = [42]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12] e
                            {grauExp} em S-1200/S-2299 = [2], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [43]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12] e
                            {grauExp} em S-1200/S-2299 = [3], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [44]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12] e
                            {grauExp} em S-1200/S-2299 = [4], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [45]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado), observado o limite para
                            {codCateg}(../codCateg) = [107, 108]; {tpValor}(./tpValor) = [46]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14] e
                            {grauExp} em S-1200/S-2299 = [2], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [47]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14] e
                            {grauExp} em S-1200/S-2299 = [3], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [48]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14] e
                            {grauExp} em S-1200/S-2299 = [4], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [49],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [15, 16, 21,
                            22], observado o limite para {codCateg}(../codCateg) = [107, 108];
                            {tpValor}(./tpValor) = [51]****,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [12] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado), se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]
                            para {perApur}(5001_ideEvento_perApur) entre [2025-01] e [2027-12];
                            {tpValor}(./tpValor) = [52]****,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [12] e
                            ({grauExp} em S-1200/S-2299 = [2]), se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]
                            para {perApur}(5001_ideEvento_perApur) entre [2025-01] e [2027-12];
                            {tpValor}(./tpValor) = [53]****,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [12] e
                            ({grauExp} em S-1200/S-2299 = [3]), se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]
                            para {perApur}(5001_ideEvento_perApur) entre [2025-01] e [2027-12];
                            {tpValor}(./tpValor) = [54]****,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [12] e
                            ({grauExp} em S-1200/S-2299 = [4]), se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]
                            para {perApur}(5001_ideEvento_perApur) entre [2025-01] e [2027-12];
                            {tpValor}(./tpValor) = [71]****,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [92] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado), se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]
                            para {perApur}(5001_ideEvento_perApur) entre [2025-01] e [2027-12];
                            {tpValor}(./tpValor) = [72]****,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [92] e
                            ({grauExp} em S-1200/S-2299 = [2]), se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]
                            para {perApur}(5001_ideEvento_perApur) entre [2025-01] e [2027-12];
                            {tpValor}(./tpValor) = [73]****,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [92] e
                            ({grauExp} em S-1200/S-2299 = [3]), se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]
                            para {perApur}(5001_ideEvento_perApur) entre [2025-01] e [2027-12];
                            {tpValor}(./tpValor) = [74]****,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [92] e
                            ({grauExp} em S-1200/S-2299 = [4]), se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]
                            para {perApur}(5001_ideEvento_perApur) entre [2025-01] e [2027-12];
                            {tpValor}(./tpValor) = [81]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [91, 92] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado), observado o limite para
                            {codCateg}(../codCateg) = [107, 108]; {tpValor}(./tpValor) = [82]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [91, 92] e
                            {grauExp} em S-1200/S-2299 = [2], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [83]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [91, 92] e
                            {grauExp} em S-1200/S-2299 = [3], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [84]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [91, 92] e
                            {grauExp} em S-1200/S-2299 = [4], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [85]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [95, 96] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado), observado o limite para
                            {codCateg}(../codCateg) = [107, 108]; {tpValor}(./tpValor) = [86]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [95, 96] e
                            {grauExp} em S-1200/S-2299 = [2], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [87]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [95, 96] e
                            {grauExp} em S-1200/S-2299 = [3], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [88]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [95, 96] e
                            {grauExp} em S-1200/S-2299 = [4], observado o limite para {codCateg}(../codCateg) =
                            [107, 108]; {tpValor}(./tpValor) = [91]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [91, 92] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado); {tpValor}(./tpValor) = [92]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [91, 92] e
                            {grauExp} em S-1200/S-2299 = [2]; {tpValor}(./tpValor) = [93]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [91, 92] e
                            {grauExp} em S-1200/S-2299 = [3]; {tpValor}(./tpValor) = [94]*,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [91, 92] e
                            {grauExp} em S-1200/S-2299 = [4]; {tpValor}(./tpValor) = [95]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [95, 96] e
                            ({grauExp} em S-1200/S-2299 = [1] ou não informado); {tpValor}(./tpValor) = [96]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [95, 96] e
                            {grauExp} em S-1200/S-2299 = [2]; {tpValor}(./tpValor) = [97]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [95, 96] e
                            {grauExp} em S-1200/S-2299 = [3]; {tpValor}(./tpValor) = [98]**,
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [95, 96] e
                            {grauExp} em S-1200/S-2299 = [4]. b) Somar os valores das rubricas cujo
                            {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a [2,
                            4] e subtrair os valores das rubricas cujo
                            {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a [1,
                            3], observando a tabela de relacionamento abaixo: {tpValor}(./tpValor) = [21],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [31, 32];
                            {tpValor}(./tpValor) = [22],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [34];
                            {tpValor}(./tpValor) = [23],
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [35]. * Caso
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) da rubrica em S-1010
                            seja igual a [91, 92, 93, 94] e
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) do respectivo
                            processo em S-1070 seja diferente de [90] (decisão definitiva), o valor também deve
                            ser computado na composição das bases do {tpValor}(./tpValor) = [11, 12, 13, 14, 41,
                            42, 43, 44]. Se {codCateg}(../codCateg) = [107, 108], caso {tpValor}(./tpValor) =
                            [11] seja maior que o limite do salário-base para essas categorias, então
                            {tpValor}(./tpValor) = [81] é igual a {tpValor}=[41] – ({tpValor}=[11] –
                            {tpValor}=[91]). Se {tpValor}(./tpValor) = [81] resultar negativo, informar 0
                            (zero). O mesmo se aplica para {tpValor}(./tpValor) = [82, 83, 84]. ** Caso
                            {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) da rubrica em S-1010
                            seja igual a [95, 96, 97, 98] e
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) do respectivo
                            processo em S-1070 seja diferente de [90] (decisão definitiva), o valor também deve
                            ser computado na composição das bases do {tpValor}(./tpValor) = [15, 16, 17, 18, 45,
                            46, 47, 48]. Se {codCateg}(../codCateg) = [107, 108], caso {tpValor}(./tpValor) =
                            [15] seja maior que o limite do salário-base para essas categorias, então
                            {tpValor}(./tpValor) = [85] é igual a {tpValor}=[45] – ({tpValor}=[15] –
                            {tpValor}=[95]). Se {tpValor}(./tpValor) = [85] resultar negativo, informar 0
                            (zero). O mesmo se aplica para {tpValor}(./tpValor) = [86, 87, 88]. *** Caso
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) do respectivo
                            processo em S-1070 seja igual a [90] (decisão definitiva), o valor não deve ser
                            computado. **** Caso {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) da
                            rubrica em S-1010 seja igual a [92] e
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) do respectivo
                            processo em S-1070 seja diferente de [90] (decisão definitiva), o valor de
                            {tpValor}(./tpValor) = [71, 72, 73, 74] também deve ser computado na composição das
                            bases do {tpValor}(./tpValor) = [51, 52, 53, 54].
                        """

                        ind13: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        tpValor: InfoBaseCsTpValor = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        valor: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class CalcTerc(CommonMixin):
                        """
                        :ivar tpCR:
                        :ivar vrCsSegTerc: Valor da contribuição social devida a Outras Entidades ou Fundos,
                            calculada segundo a legislação em vigor, por CR. Validação: {calcTerc/tpCR}(./tpCR)
                            = [121802] - Somatório de {valor}(../infoBaseCS_valor) quando
                            {tpValor}(../infoBaseCS_tpValor) = [11, 12, 13, 14], multiplicado pela alíquota de
                            1,5%, se {codCateg}(../codCateg) = [711, 712, 734] (transportador autônomo) e
                            {ideEmpregador/tpInsc}(5001_ideEmpregador_tpInsc) = [1]; {calcTerc/tpCR}(./tpCR) =
                            [122102] - Somatório de {valor}(../infoBaseCS_valor) quando
                            {tpValor}(../infoBaseCS_tpValor) = [11, 12, 13, 14], multiplicado pela alíquota de
                            1,0%, se {codCateg}(../codCateg) = [711, 712, 734] (transportador autônomo) e
                            {ideEmpregador/tpInsc}(5001_ideEmpregador_tpInsc) = [1]. OBS.: No período de 04/2020
                            a 06/2020, as alíquotas devem ser 0,75% para o SEST e 0,5% para o SENAT.
                        :ivar vrDescTerc: Valor efetivamente descontado do segurado, correspondente a
                            {tpValor}(../infoBaseCS_tpValor) = [22, 23], do correspondente
                            {calcTerc/tpCR}(./tpCR).
                        """

                        tpCR: CalcTercTpCr = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrCsSegTerc: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrDescTerc: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class InfoPerRef(CommonMixin):
                        """
                        :ivar perRef: Informar o período ao qual se refere a remuneração. Origem:
                            {perApur}(5001_ideEvento_perApur) ou campo {perRef} de S-1200/S-2299.
                        :ivar ideADC: Instrumento ou situação ensejadora da remuneração em períodos anteriores
                            DESCRICAO_COMPLETA:Identificação do instrumento ou situação ensejadora da
                            remuneração relativa a períodos de apuração anteriores. Evento de origem: S-1200 ou
                            S-2299 (exceto {remunSuc}(./remunSuc), cujo evento de origem somente é S-1200).
                            CHAVE_GRUPO: {dtAcConv}, {tpAcConv} CONDICAO_GRUPO: OC
                        :ivar detInfoPerRef: Detalhamento das informações de remuneração por período de
                            referência DESCRICAO_COMPLETA:Detalhamento das informações de remuneração por
                            período de referência. Deve ser preenchido com informações de {infoPerApur} e
                            {infoPerAnt} do S-1200 e S-2299, e de {dmDev} do S-2399, quando houver. CHAVE_GRUPO:
                            {ind13}, {tpVrPerRef}
                        """

                        perRef: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        ideADC: list[ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.InfoPerRef.IdeAdc] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                            },
                        )
                        detInfoPerRef: list[
                            ESocial.EvtBasesTrab.InfoCp.IdeEstabLot.InfoCategIncid.InfoPerRef.DetInfoPerRef
                        ] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 99,
                            },
                        )

                        @dataclass(kw_only=True)
                        class IdeAdc(CommonMixin):
                            """
                            :ivar dtAcConv: Data da assinatura do acordo, convenção coletiva, sentença normativa
                                ou da conversão da licença saúde em acidente de trabalho.
                            :ivar tpAcConv:
                            :ivar dsc:
                            :ivar remunSuc: Indicar se a remuneração é relativa a verbas de natureza salarial ou
                                não salarial devidas pela empresa sucessora a empregados desligados ainda na
                                sucedida.
                            """

                            dtAcConv: None | XmlDate = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            tpAcConv: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            dsc: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            remunSuc: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )

                        @dataclass(kw_only=True)
                        class DetInfoPerRef(CommonMixin):
                            """
                            :ivar ind13:
                            :ivar tpVrPerRef:
                            :ivar vrPerRef: Valor da base de cálculo, dedução ou desconto da contribuição
                                social, conforme definido no campo {tpVrPerRef}(./tpVrPerRef). Validação: Deve
                                ser maior que 0 (zero). Deve corresponder ao somatório dos valores informados no
                                campo {vrRubr} em S-1200 e S-2299 (grupos {infoPerApur} e {infoPerAnt}), e
                                também em S-2399, obedecendo ao que segue: a) Somar os valores das rubricas cujo
                                {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a
                                [1, 3] e subtrair os valores das rubricas cujo
                                {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a
                                [2, 4], observando a tabela de relacionamento abaixo: {tpVrPerRef}(./tpVrPerRef)
                                = [11]*, {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 =
                                [11, 12] e ({grauExp} em S-1200/S-2299 = [1] ou não informado);
                                {tpVrPerRef}(./tpVrPerRef) = [12]*,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12]
                                e {grauExp} em S-1200/S-2299 = [2]; {tpVrPerRef}(./tpVrPerRef) = [13]*,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12]
                                e {grauExp} em S-1200/S-2299 = [3]; {tpVrPerRef}(./tpVrPerRef) = [14]*,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [11, 12]
                                e {grauExp} em S-1200/S-2299 = [4]; {tpVrPerRef}(./tpVrPerRef) = [15]**,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14]
                                e ({grauExp} em S-1200/S-2299 = [1] ou não informado);
                                {tpVrPerRef}(./tpVrPerRef) = [16]**,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14]
                                e {grauExp} em S-1200/S-2299 = [2]; {tpVrPerRef}(./tpVrPerRef) = [17]**,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14]
                                e {grauExp} em S-1200/S-2299 = [3]; {tpVrPerRef}(./tpVrPerRef) = [18]**,
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [13, 14]
                                e {grauExp} em S-1200/S-2299 = [4]; {tpVrPerRef}(./tpVrPerRef) = [19],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [15, 16,
                                21, 22]; {tpVrPerRef}(./tpVrPerRef) = [31],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [51];
                                {tpVrPerRef}(./tpVrPerRef) = [32],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [21, 22]
                                ou ({natRubr}(1010_infoRubrica_inclusao_dadosRubrica_natRubr) em S-1010 = [4050,
                                4051] com {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010
                                = [9X]). b) Somar os valores das rubricas cujo
                                {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a
                                [2, 4] e subtrair os valores das rubricas cujo
                                {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a
                                [1, 3], observando a tabela de relacionamento abaixo: {tpVrPerRef}(./tpVrPerRef)
                                = [21], {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 =
                                [31, 32]; {tpVrPerRef}(./tpVrPerRef) = [22],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [34];
                                {tpVrPerRef}(./tpVrPerRef) = [23],
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 = [35]. *
                                Caso {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) da rubrica em
                                S-1010 seja igual a [91, 92, 93, 94] e
                                {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) do respectivo
                                processo em S-1070 seja diferente de [90] (decisão definitiva), o valor deve ser
                                computado na composição das bases do {tpVrPerRef}(./tpVrPerRef) = [11, 12, 13,
                                14]. ** Caso {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) da
                                rubrica em S-1010 seja igual a [95, 96, 97, 98] e
                                {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) do respectivo
                                processo em S-1070 seja diferente de [90] (decisão definitiva), o valor deve ser
                                computado na composição das bases do {tpVrPerRef}(./tpVrPerRef) = [15, 16, 17,
                                18]. *** Caso {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp)
                                do respectivo processo em S-1070 seja igual a [90] (decisão definitiva), o valor
                                não deve ser computado.
                            """

                            ind13: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            tpVrPerRef: DetInfoPerRefTpVrPerRef = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrPerRef: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

        @dataclass(kw_only=True)
        class InfoPisPasep(CommonMixin):
            """
            :ivar ideEstab: Identificação do estabelecimento ou obra de construção civil. CHAVE_GRUPO: {tpInsc},
                {nrInsc}
            """

            ideEstab: list[ESocial.EvtBasesTrab.InfoPisPasep.IdeEstab] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class IdeEstab(CommonMixin):
                """
                :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.
                    Evento de origem: S-1200, S-2299, S-2399 ou S-1202.
                :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideEstab/tpInsc}(./tpInsc). Evento de origem: S-1200, S-2299, S-2399 ou
                    S-1202
                :ivar infoCategPisPasep: Informações relativas à matrícula e categoria do trabalhador.
                    CHAVE_GRUPO: {matricula}, {codCateg}
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
                infoCategPisPasep: list[ESocial.EvtBasesTrab.InfoPisPasep.IdeEstab.InfoCategPisPasep] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 10,
                    },
                )

                @dataclass(kw_only=True)
                class InfoCategPisPasep(CommonMixin):
                    """
                    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor
                        público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão.
                        Evento de origem: S-1200, S-2299, S-2399 ou S-1202.
                    :ivar codCateg: Preencher com o código da categoria do trabalhador, conforme Tabela 01.
                        Validação: Se o evento de origem for S-1200 ou S-1202, retornar o código de categoria
                        informado nesse evento. Se o evento de origem for S-2299 ou S-2399, retornar o código de
                        categoria existente no Registro de Eventos Trabalhistas - RET.
                    :ivar infoBasePisPasep: Informações sobre bases de cálculo do PIS/PASEP. Evento de origem:
                        S-1200, S-2299, S-2399 ou S-1202. CHAVE_GRUPO: {ind13}, {tpValorPisPasep}
                        CONDICAO_GRUPO: N (se {classTrib}(5001_infoCp_classTrib) = [10] e
                        {codCateg}(../codCateg) = [202]); O (nos demais casos)
                    """

                    matricula: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    codCateg: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoBasePisPasep: list[
                        ESocial.EvtBasesTrab.InfoPisPasep.IdeEstab.InfoCategPisPasep.InfoBasePisPasep
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoBasePisPasep(CommonMixin):
                        """
                        :ivar ind13:
                        :ivar tpValorPisPasep:
                        :ivar valorPisPasep: Valor da base de cálculo, dedução ou desconto da contribuição
                            social devida ao PIS/PASEP, conforme definido no campo {}(./tpValorPisPasep).
                            Validação: Deve ser maior que 0 (zero). Deve corresponder ao somatório dos valores
                            informados no campo {vrRubr} em S-1200, S-1202 e S-2299 (grupos {infoPerApur} e
                            {infoPerAnt}), e também em S-2399, obedecendo ao que segue: a) Somar os valores das
                            rubricas cujo {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja
                            igual a [1, 3] e subtrair os valores das rubricas cujo
                            {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a [2,
                            4], observando a tabela de relacionamento abaixo: {}(./tpValorPisPasep) = [11]*,
                            {}(1010_infoRubrica_inclusao_dadosRubrica_codIncPisPasep) em S-1010 = [11, 12];
                            {}(./tpValorPisPasep) = [91]*,
                            {}(1010_infoRubrica_inclusao_dadosRubrica_codIncPisPasep) em S-1010 = [91, 92]; *
                            Caso {}(1010_infoRubrica_inclusao_dadosRubrica_codIncPisPasep) da rubrica em S-1010
                            seja igual a [91, 92] e
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) do respectivo
                            processo em S-1070 seja diferente de [90] (decisão definitiva), o valor também deve
                            ser computado na composição das bases do {}(./tpValorPisPasep) = [11]. *** Caso
                            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) do respectivo
                            processo em S-1070 seja igual a [90] (decisão definitiva), o valor não deve ser
                            computado.
                        """

                        ind13: InfoBasePisPasepInd13 = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        tpValorPisPasep: InfoBasePisPasepTpValorPisPasep = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        valorPisPasep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
