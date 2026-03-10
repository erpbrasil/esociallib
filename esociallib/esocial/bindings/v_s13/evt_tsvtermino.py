from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTSVTermino/v_S_01_03_00"


class InfoTsvterminoMtvDesligTsv(Enum):
    """
    Motivo do término.

    Validação: Informação obrigatória se o código de categoria no Registro de Eventos Trabalhistas - RET for igual
    a [721] ou se o grupo {mudancaCPF}(2399_infoTSVTermino_mudancaCPF) estiver preenchido. Não preencher nas demais
    situações.

    :cvar VALUE_01: Exoneração do diretor não empregado sem justa causa, por deliberação da assembleia, dos
        sócios cotistas ou da autoridade competente
    :cvar VALUE_02: Término de mandato do diretor não empregado que não tenha sido reconduzido ao cargo
    :cvar VALUE_03: Exoneração a pedido de diretor não empregado
    :cvar VALUE_04: Exoneração do diretor não empregado por culpa recíproca ou força maior
    :cvar VALUE_05: Morte do diretor não empregado
    :cvar VALUE_06: Exoneração do diretor não empregado por falência, encerramento ou supressão de parte da
        empresa
    :cvar VALUE_07: Mudança de CPF
    :cvar VALUE_99: Outros
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_99 = "99"


class RemunAposTermIndRemun(Enum):
    """
    Indicativo de situação de remuneração após o término.

    Validação: Informação obrigatória se {dtTerm}(2399_infoTSVTermino_dtTerm) &gt;= [2023-01-16].

    :cvar VALUE_1: Quarentena
    :cvar VALUE_2: Término reconhecido judicialmente com data anterior a competências com remunerações já
        informadas no eSocial
    """

    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término.

    :ivar evtTSVTermino: Evento TSVE - Término DESCRICAO_COMPLETA:Evento Trabalhador Sem Vínculo de
        Emprego/Estatutário - Término. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EVE_FOPAG_SIMPLIFICADO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_MUDANCA_CPF REGRA:REGRA_REMUN_IND_RETIFICACAO REGRA:REGRA_REMUN_PERMITE_EXCLUSAO
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_RUBRICA_COMPATIVEL_CATEGORIA
        REGRA:REGRA_RUBRICA_ECONSIGNADO REGRA:REGRA_TSV_ATIVO_NA_DTEVENTO
        REGRA:REGRA_VALIDA_CODINCCP_EXC_SEGURADO REGRA:REGRA_VALIDA_EMPREGADOR
        REGRA:REGRA_VALIDA_PERIODO_APURACAO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTSVTermino/v_S_01_03_00"

    evtTSVTermino: ESocial.EvtTsvtermino = field(
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
    class EvtTsvtermino(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideTrabSemVinculo:
        :ivar infoTSVTermino: TSVE - Término. CHAVE_GRUPO: {dtTerm*}
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
        ideTrabSemVinculo: str = field(
            metadata={
                "type": "Element",
            }
        )
        infoTSVTermino: ESocial.EvtTsvtermino.InfoTsvtermino = field(
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
        class InfoTsvtermino(CommonMixin):
            """
            :ivar dtTerm: Data do término. Validação: Deve ser uma data igual ou anterior à data atual acrescida
                de 10 (dez) dias.
            :ivar mtvDesligTSV:
            :ivar pensAlim: Indicativo de pensão alimentícia para fins de retenção de FGTS. Validação:
                Informação obrigatória se o código de categoria no RET for igual a [201, 202, 721] e se
                {dtTerm}(./dtTerm) for posterior a 21/04/2019. Informação opcional se o código de categoria no
                RET for igual a [201, 202, 721] e se {dtTerm}(./dtTerm) for igual ou anterior a 21/04/2019. Não
                preencher nas demais situações.
            :ivar percAliment:
            :ivar vrAlim:
            :ivar nrProcTrab: Número que identifica o processo trabalhista, quando o término de TSVE se der por
                decisão judicial. Validação: Se preenchido, deve ser um processo judicial válido, com 20 (vinte)
                algarismos.
            :ivar mudancaCPF: Informação do novo CPF do trabalhador. CONDICAO_GRUPO: O (se
                {mtvDesligTSV}(2399_infoTSVTermino_mtvDesligTSV) = [07]); N (nos demais casos)
            :ivar verbasResc: Verbas rescisórias DESCRICAO_COMPLETA:Grupo onde são prestadas as informações
                relativas às verbas rescisórias do diretor não empregado, com FGTS. CONDICAO_GRUPO: N (se
                {mtvDesligTSV}(2399_infoTSVTermino_mtvDesligTSV) = [07] OU {dtTerm}(2399_infoTSVTermino_dtTerm)
                for anterior ao início de obrigatoriedade dos eventos periódicos para o empregador OU o código
                de categoria no RET for diferente de [721]); OC (nos demais casos)
            :ivar remunAposTerm: Informações sobre a quarentena remunerada ou outra situação de término com data
                anterior DESCRICAO_COMPLETA:Informações sobre a "quarentena" remunerada de trabalhador desligado
                ou outra situação de término com data anterior. O grupo deve ser preenchido apenas no caso do
                trabalhador que recebe remuneração após o desligamento por estar impossibilitado de exercer
                atividade remunerada ou no caso de término reconhecido judicialmente com data anterior a
                competências com remunerações já informadas no eSocial. CONDICAO_GRUPO: OC
            """

            dtTerm: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            mtvDesligTSV: None | InfoTsvterminoMtvDesligTsv = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            pensAlim: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            percAliment: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            vrAlim: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            nrProcTrab: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            mudancaCPF: None | ESocial.EvtTsvtermino.InfoTsvtermino.MudancaCpf = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            verbasResc: None | ESocial.EvtTsvtermino.InfoTsvtermino.VerbasResc = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            remunAposTerm: None | ESocial.EvtTsvtermino.InfoTsvtermino.RemunAposTerm = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class MudancaCpf(CommonMixin):
                """
                :ivar novoCPF: Preencher com o novo CPF do trabalhador. Validação: Deve ser um CPF válido e
                    diferente do CPF do empregador e do antigo CPF do trabalhador.
                """

                novoCPF: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class VerbasResc(CommonMixin):
                """
                :ivar dmDev: Demonstrativo de valores devidos ao trabalhador DESCRICAO_COMPLETA:Identificação de
                    cada um dos demonstrativos de valores devidos ao trabalhador. CHAVE_GRUPO: {ideDmDev}
                    REGRA:REGRA_DEMONSTRATIVO
                :ivar procJudTrab:
                :ivar infoMV:
                """

                dmDev: list[ESocial.EvtTsvtermino.InfoTsvtermino.VerbasResc.DmDev] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 50,
                    },
                )
                procJudTrab: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                infoMV: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class DmDev(CommonMixin):
                    """
                    :ivar ideDmDev: Identificador atribuído pela empresa para o demonstrativo de valores devidos
                        ao trabalhador relativo a verbas rescisórias. Validação: Deve ser um identificador único
                        dentro da mesma competência (mês/ano da data de término) para cada um dos demonstrativos
                        do trabalhador. REGRA:REGRA_CARACTERE_ESPECIAL
                    :ivar indRRA: Indicativo de Rendimentos Recebidos Acumuladamente - RRA. Somente preencher
                        este campo se for um demonstrativo de RRA.
                    :ivar notAFT: Número da notificação de FGTS que deu origem à confissão. Validação: Se o
                        campo for preenchido: a) O mês/ano de {}(2399_infoTSVTermino_dtTerm) deve ser igual ou
                        posterior ao início do FGTS Digital; b) Todas as rubricas de vencimento
                        ({}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 = [1]) informadas no
                        demonstrativo devem possuir {}(1010_infoRubrica_inclusao_dadosRubrica_codIncFGTS) em
                        S-1010 = [71]; c) Devem ser informados apenas caracteres alfanuméricos, com 9 (nove)
                        posições.
                    :ivar infoRRA:
                    :ivar ideEstabLot: Identificação do estabelecimento e lotação
                        DESCRICAO_COMPLETA:Identificação do estabelecimento e da lotação nos quais o trabalhador
                        possui remuneração no período de apuração. CHAVE_GRUPO: {tpInsc}, {nrInsc}, {codLotacao}
                    """

                    ideDmDev: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    indRRA: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    notAFT: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoRRA: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    ideEstabLot: list[ESocial.EvtTsvtermino.InfoTsvtermino.VerbasResc.DmDev.IdeEstabLot] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class IdeEstabLot(CommonMixin):
                        """
                        :ivar tpInsc:
                        :ivar nrInsc: Informar o número de inscrição do estabelecimento do contribuinte de
                            acordo com o tipo de inscrição indicado no campo {ideEstabLot/tpInsc}(./tpInsc).
                            Validação: A inscrição informada deve ser compatível com
                            {ideEstabLot/tpInsc}(./tpInsc).
                        :ivar codLotacao:
                        :ivar detVerbas: Detalhamento das verbas rescisórias DESCRICAO_COMPLETA:Detalhamento das
                            verbas rescisórias devidas ao trabalhador. Deve haver pelo menos uma rubrica de
                            folha, mesmo que o valor líquido a ser pago ao trabalhador seja 0 (zero) em função
                            de descontos.
                        :ivar infoSimples:
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
                        detVerbas: list[
                            ESocial.EvtTsvtermino.InfoTsvtermino.VerbasResc.DmDev.IdeEstabLot.DetVerbas
                        ] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 200,
                            },
                        )
                        infoSimples: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                        @dataclass(kw_only=True)
                        class DetVerbas(CommonMixin):
                            """
                            :ivar codRubr: Informar o código atribuído pelo empregador que identifica a rubrica
                                em sua folha de pagamento ou o código da rubrica constante da Tabela de Rubricas
                                Padrão. Validação: Não pode ser utilizada rubrica: a) cujo
                                {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) em S-1010 seja igual
                                a [25, 26, 51]; b) cuja
                                {natRubr}(1010_infoRubrica_inclusao_dadosRubrica_natRubr) em S-1010 seja igual a
                                [1801, 9220], desde que mês/ano de {dtTerm}(2399_infoTSVTermino_dtTerm) &gt;=
                                [2021-07].
                            :ivar ideTabRubr:
                            :ivar qtdRubr:
                            :ivar fatorRubr:
                            :ivar vrRubr:
                            :ivar indApurIR: Indicativo de tipo de apuração de IR. Validação: Informação
                                obrigatória e exclusiva se mês/ano de {dtTerm}(2399_infoTSVTermino_dtTerm) &gt;=
                                [2021-07].
                            :ivar descFolha: Informações de desconto do empréstimo em folha. CONDICAO_GRUPO: O
                                (se {}(1010_infoRubrica_inclusao_dadosRubrica_natRubr) em S-1010 = [9253]); N
                                (nos demais casos)
                            """

                            codRubr: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            ideTabRubr: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            qtdRubr: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            fatorRubr: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrRubr: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            indApurIR: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            descFolha: (
                                None
                                | ESocial.EvtTsvtermino.InfoTsvtermino.VerbasResc.DmDev.IdeEstabLot.DetVerbas.DescFolha
                            ) = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )

                            @dataclass(kw_only=True)
                            class DescFolha(CommonMixin):
                                """
                                :ivar tpDesc:
                                :ivar instFinanc: Código Bancário de Consignado concedente do empréstimo.
                                    Validação: Deve ser um código válido, conforme Tabela  37 do eSocial
                                    Tabelas.
                                :ivar nrDoc:
                                :ivar observacao: Outras informações do desconto.
                                """

                                tpDesc: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                instFinanc: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                nrDoc: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                observacao: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )

            @dataclass(kw_only=True)
            class RemunAposTerm(CommonMixin):
                """
                :ivar indRemun:
                :ivar dtFimRemun: Preencher com a data final da quarentena a que está sujeito o trabalhador. No
                    caso de término reconhecido judicialmente com data anterior a competências com remunerações
                    já informadas no eSocial, informar o último dia trabalhado. Validação: Deve ser uma data
                    posterior a {dtTerm}(2399_infoTSVTermino_dtTerm).
                """

                indRemun: None | RemunAposTermIndRemun = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                dtFimRemun: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
