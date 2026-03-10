from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00"


class TDadosRubricaCodIncCp(Enum):
    """
    Código de incidência tributária da rubrica para a Previdência Social.

    Validação: Para utilização de código [91, 92, 93, 94, 95, 96, 97, 98], é necessária a existência de grupo com
    informações relativas ao processo.

    :cvar VALUE_00: Não é base de cálculo
    :cvar VALUE_01: Não é base de cálculo em função de acordos internacionais de previdência social
    :cvar VALUE_11: Base de cálculo das contribuições sociais - Salário de contribuição: Mensal
    :cvar VALUE_12: 13º salário
    :cvar VALUE_13: Exclusiva do empregador - Mensal
    :cvar VALUE_14: Exclusiva do empregador - 13° salário
    :cvar VALUE_15: Exclusiva do segurado - Mensal
    :cvar VALUE_16: Exclusiva do segurado - 13° salário
    :cvar VALUE_21: Salário-maternidade mensal, pago pelo empregador
    :cvar VALUE_22: Salário-maternidade 13º salário, pago pelo empregador
    :cvar VALUE_25: Salário-maternidade mensal, pago pelo INSS
    :cvar VALUE_26: Salário-maternidade 13° salário, pago pelo INSS
    :cvar VALUE_31: Contribuição descontada do segurado sobre salário de contribuição: Mensal
    :cvar VALUE_32: 13º salário
    :cvar VALUE_34: SEST
    :cvar VALUE_35: SENAT
    :cvar VALUE_51: Outros: Salário-família
    :cvar VALUE_91: Suspensão de incidência sobre salário de contribuição em decorrência de decisão judicial:
        Mensal
    :cvar VALUE_92: 13º salário
    :cvar VALUE_93: Salário-maternidade
    :cvar VALUE_94: Salário-maternidade 13º salário
    :cvar VALUE_95: Exclusiva do empregador - Mensal
    :cvar VALUE_96: Exclusiva do empregador - 13º salário
    :cvar VALUE_97: Exclusiva do empregador - Salário-maternidade
    :cvar VALUE_98: Exclusiva do empregador - Salário-maternidade 13º salário
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_51 = "51"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"
    VALUE_94 = "94"
    VALUE_95 = "95"
    VALUE_96 = "96"
    VALUE_97 = "97"
    VALUE_98 = "98"


class TDadosRubricaCodIncCprp(Enum):
    """
    Código de incidência da rubrica para as contribuições do Regime Próprio de Previdência Social - RPPS ou do
    Sistema de Proteção Social dos Militares das Forças Armadas - SPSMFA.

    :cvar VALUE_00: Não é base de cálculo de contribuições devidas
    :cvar VALUE_11: Base de cálculo de contribuições devidas
    :cvar VALUE_12: Base de cálculo de contribuições devidas - 13º salário
    :cvar VALUE_31: Contribuição descontada do segurado ou beneficiário
    :cvar VALUE_32: Contribuição descontada do segurado ou beneficiário - 13º salário
    :cvar VALUE_91: Suspensão de incidência em decorrência de decisão judicial
    :cvar VALUE_92: Suspensão de incidência em decorrência de decisão judicial - 13º salário
    """

    VALUE_00 = "00"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_91 = "91"
    VALUE_92 = "92"


class TDadosRubricaCodIncFgts(Enum):
    """
    Código de incidência da rubrica para o Fundo de Garantia do Tempo de Serviço - FGTS.

    Validação: Para utilização de código [91, 92, 93], é necessária a existência de grupo com informações relativas
    ao processo. A utilização do código [31] é obrigatória e exclusiva quando {natRubr}(./natRubr) = [9253].

    :cvar VALUE_00: Não é base de cálculo do FGTS
    :cvar VALUE_11: Base de cálculo do FGTS mensal
    :cvar VALUE_12: Base de cálculo do FGTS 13° salário
    :cvar VALUE_21: Base de cálculo do FGTS aviso prévio indenizado
    :cvar VALUE_31: Desconto eConsignado
    :cvar VALUE_91: Incidência suspensa em decorrência de decisão judicial - FGTS mensal
    :cvar VALUE_92: Incidência suspensa em decorrência de decisão judicial - FGTS 13º salário
    :cvar VALUE_93: Incidência suspensa em decorrência de decisão judicial - FGTS aviso prévio indenizado
    """

    VALUE_00 = "00"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_21 = "21"
    VALUE_31 = "31"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"


class TDadosRubricaCodIncPisPasep(Enum):
    """
    Código de incidência da rubrica para o PIS/PASEP sobre a folha de salários a ser utilizado quando
    {}(1000_infoEmpregador_inclusao_infoCadastro_indTribFolhaPisPasep) = [S] em S-1000.

    Validação: Para utilização de código [91, 92], é necessária a existência de grupo com informações relativas ao
    processo. Caso o campo não seja informado, será presumido o valor [00].

    :cvar VALUE_00: Não é base de cálculo do PIS/PASEP
    :cvar VALUE_11: Base de cálculo do PIS/PASEP mensal
    :cvar VALUE_12: Base de cálculo do PIS/PASEP 13° salário
    :cvar VALUE_91: Incidência suspensa em decorrência de decisão judicial - PIS/PASEP mensal
    :cvar VALUE_92: Incidência suspensa em decorrência de decisão judicial - PIS/PASEP 13º salário
    """

    VALUE_00 = "00"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_91 = "91"
    VALUE_92 = "92"


class TDadosRubricaTpRubr(Enum):
    """
    Tipo de rubrica.

    Validação: Se {natRubr}(./natRubr) = [9253], deve ser preenchido com [2].

    :cvar VALUE_1: Vencimento, provento ou pensão
    :cvar VALUE_2: Desconto
    :cvar VALUE_3: Informativa
    :cvar VALUE_4: Informativa dedutora
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass(kw_only=True)
class TIdeRubrica(CommonMixin):
    """
    Identificação da rubrica e validade das informações DESCRICAO_COMPLETA:Identificação da rubrica e período de
    validade das informações.

    CHAVE_GRUPO: {codRubr*}, {ideTabRubr*}, {iniValid*}, {fimValid*}.

    :ivar codRubr: Informar o código atribuído pelo empregador que identifica a rubrica em sua folha de
        pagamento. Validação: O código não pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições.
        REGRA:REGRA_CARACTERE_ESPECIAL
    :ivar ideTabRubr: Preencher com o identificador da Tabela de Rubricas no âmbito do empregador. Validação: O
        identificador não pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições.
        REGRA:REGRA_CARACTERE_ESPECIAL
    :ivar iniValid:
    :ivar fimValid:
    """

    class Meta:
        name = "T_ideRubrica"

    codRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        }
    )
    ideTabRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        }
    )
    iniValid: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        }
    )
    fimValid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        },
    )


class IdeProcessoCpExtDecisao(Enum):
    """
    Extensão da decisão/sentença.

    :cvar VALUE_1: Contribuição previdenciária patronal
    :cvar VALUE_2: Contribuição previdenciária patronal + descontada dos segurados
    """

    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class TDadosRubrica(CommonMixin):
    """
    Detalhamento das informações da rubrica.

    :ivar dscRubr: Informar a descrição (nome) da rubrica no sistema de folha de pagamento da empresa.
    :ivar natRubr:
    :ivar tpRubr:
    :ivar codIncCP:
    :ivar codIncIRRF:
    :ivar codIncFGTS:
    :ivar codIncCPRP:
    :ivar codIncPisPasep:
    :ivar tetoRemun: Informar se a rubrica compõe o teto remuneratório específico (art. 37, XI, da CF/1988).
        Validação: Preenchimento obrigatório se a natureza jurídica do declarante for Administração Pública
        (grupo [1]).
    :ivar observacao: Observações relacionadas à rubrica ou à sua utilização.
    :ivar ideProcessoCP: Identificação de processo - Incidência de Contrib. Previdenciária
        DESCRICAO_COMPLETA:Caso a empresa possua processo administrativo ou judicial com decisão/sentença
        favorável, determinando a não incidência de contribuição previdenciária relativa à rubrica identificada
        no evento, as informações deverão ser incluídas neste grupo, e o detalhamento do processo deverá ser
        efetuado através de evento específico na Tabela de Processos (S-1070). CHAVE_GRUPO: {nrProc}
        CONDICAO_GRUPO: O (se {codIncCP}(1010_infoRubrica_inclusao_dadosRubrica_codIncCP) = [9X]); N (nos demais
        casos)
    :ivar ideProcessoIRRF: Identificação de processo - Incidência de IRRF DESCRICAO_COMPLETA:Caso a empresa
        possua processo judicial com decisão/sentença favorável, determinando a não incidência de imposto de
        renda relativo à rubrica identificada no evento, as informações deverão ser incluídas neste grupo, e o
        detalhamento do processo deverá ser efetuado através de evento específico na Tabela de Processos
        (S-1070). CHAVE_GRUPO: {nrProc} CONDICAO_GRUPO: O (se
        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) = [9X] ou [9XXX]); N (nos demais casos)
    :ivar ideProcessoFGTS: Identificação de processo - Incidência de FGTS DESCRICAO_COMPLETA:Caso a empresa
        possua processo judicial com decisão/sentença favorável, determinando a não incidência de FGTS relativo
        à rubrica identificada no evento, as informações deverão ser incluídas neste grupo, e o detalhamento do
        processo deverá ser efetuado através de evento específico na Tabela de Processos (S-1070). CHAVE_GRUPO:
        {nrProc} CONDICAO_GRUPO: O (se {codIncFGTS}(1010_infoRubrica_inclusao_dadosRubrica_codIncFGTS) = [9X]);
        N (nos demais casos)
    :ivar ideProcessoPisPasep: Identificação de processo - Incidência para o PIS/PASEP DESCRICAO_COMPLETA:Caso a
        empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de
        contribuição para o PIS/PASEP relativo à rubrica identificada no evento, as informações deverão ser
        incluídas neste grupo, e o detalhamento do processo deverá ser efetuado através de evento específico na
        Tabela de Processos (S-1070). CHAVE_GRUPO: {nrProc} CONDICAO_GRUPO: O (se
        {}(1010_infoRubrica_inclusao_dadosRubrica_codIncPisPasep) = [9X]); N (nos demais casos)
    """

    class Meta:
        name = "T_dadosRubrica"

    dscRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        }
    )
    natRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        }
    )
    tpRubr: TDadosRubricaTpRubr = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        }
    )
    codIncCP: TDadosRubricaCodIncCp = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        }
    )
    codIncIRRF: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            "pattern": r"\d{1,4}",
        }
    )
    codIncFGTS: TDadosRubricaCodIncFgts = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        }
    )
    codIncCPRP: None | TDadosRubricaCodIncCprp = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        },
    )
    codIncPisPasep: None | TDadosRubricaCodIncPisPasep = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        },
    )
    tetoRemun: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        },
    )
    observacao: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
        },
    )
    ideProcessoCP: list[TDadosRubrica.IdeProcessoCp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            "max_occurs": 99,
        },
    )
    ideProcessoIRRF: list[TDadosRubrica.IdeProcessoIrrf] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            "max_occurs": 99,
        },
    )
    ideProcessoFGTS: list[TDadosRubrica.IdeProcessoFgts] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            "max_occurs": 99,
        },
    )
    ideProcessoPisPasep: list[TDadosRubrica.IdeProcessoPisPasep] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            "max_occurs": 99,
        },
    )

    @dataclass(kw_only=True)
    class IdeProcessoCp(CommonMixin):
        """
        :ivar tpProc:
        :ivar nrProc: Informar um número de processo cadastrado através do evento S-1070, cujo
            {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) seja igual a [1]. Validação: Deve ser
            um número de processo administrativo ou judicial válido e existente na Tabela de Processos (S-1070),
            com {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) = [1].
        :ivar extDecisao:
        :ivar codSusp:
        """

        tpProc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )
        nrProc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )
        extDecisao: IdeProcessoCpExtDecisao = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )
        codSusp: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )

    @dataclass(kw_only=True)
    class IdeProcessoIrrf(CommonMixin):
        nrProc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )
        codSusp: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )

    @dataclass(kw_only=True)
    class IdeProcessoFgts(CommonMixin):
        nrProc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )

    @dataclass(kw_only=True)
    class IdeProcessoPisPasep(CommonMixin):
        nrProc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )
        codSusp: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00",
            }
        )


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1010 - Tabela de Rubricas.

    :ivar evtTabRubrica: Evento Tabela de Rubricas. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_TABGERAL_ALTERACAO_PERIODO_CONFLITANTE
        REGRA:REGRA_TABGERAL_EXISTE_REGISTRO_ALTERADO REGRA:REGRA_TABGERAL_EXISTE_REGISTRO_EXCLUIDO
        REGRA:REGRA_TABGERAL_INCLUSAO_PERIODO_CONFLITANTE REGRA:REGRA_TABRUBR_INCLUSAO
        REGRA:REGRA_TAB_PERMITE_EXCLUSAO REGRA:REGRA_VALIDA_CODINCCP_EXC_SEGURADO REGRA:REGRA_VALIDA_DT_FUTURA
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTabRubrica/v_S_01_03_00"

    evtTabRubrica: ESocial.EvtTabRubrica = field(
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
    class EvtTabRubrica(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoRubrica: Informações da rubrica DESCRICAO_COMPLETA:Identificação da operação (inclusão,
            alteração ou exclusão) e das informações da rubrica.
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
        infoRubrica: ESocial.EvtTabRubrica.InfoRubrica = field(
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
        class InfoRubrica(CommonMixin):
            """
            :ivar inclusao: Inclusão de novas informações. CONDICAO_GRUPO: OC
            :ivar alteracao: Alteração das informações. CONDICAO_GRUPO: OC
            :ivar exclusao: Exclusão das informações. CONDICAO_GRUPO: OC
            """

            inclusao: None | ESocial.EvtTabRubrica.InfoRubrica.Inclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            alteracao: None | ESocial.EvtTabRubrica.InfoRubrica.Alteracao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            exclusao: None | ESocial.EvtTabRubrica.InfoRubrica.Exclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Inclusao(CommonMixin):
                ideRubrica: TIdeRubrica = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dadosRubrica: TDadosRubrica = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Alteracao(CommonMixin):
                ideRubrica: TIdeRubrica = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dadosRubrica: TDadosRubrica = field(
                    metadata={
                        "type": "Element",
                    }
                )
                novaValidade: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Exclusao(CommonMixin):
                ideRubrica: TIdeRubrica = field(
                    metadata={
                        "type": "Element",
                    }
                )
