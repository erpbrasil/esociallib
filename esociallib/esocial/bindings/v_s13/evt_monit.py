from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtMonit/v_S_01_03_00"


class AsoResAso(Enum):
    """
    Resultado do ASO.

    :cvar VALUE_1: Apto
    :cvar VALUE_2: Inapto
    """

    VALUE_1 = 1
    VALUE_2 = 2


class ExMedOcupTpExameOcup(Enum):
    """
    Tipo do exame médico ocupacional.

    Validação: Se informado [0], não pode existir outro evento S-2220 para o mesmo contrato com
    {dtAso}(./aso_dtAso) anterior.

    :cvar VALUE_0: Exame médico admissional
    :cvar VALUE_1: Exame médico periódico, conforme Norma Regulamentadora 07 - NR-07 e/ou planejamento do
        Programa de Controle Médico de Saúde Ocupacional - PCMSO
    :cvar VALUE_2: Exame médico de retorno ao trabalho
    :cvar VALUE_3: Exame médico de mudança de função ou de mudança de risco ocupacional
    :cvar VALUE_4: Exame médico de monitoração pontual, não enquadrado nos demais casos
    :cvar VALUE_9: Exame médico demissional
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_9 = 9


class ExameIndResult(Enum):
    """
    Indicação dos resultados.

    :cvar VALUE_1: Normal
    :cvar VALUE_2: Alterado
    :cvar VALUE_3: Estável
    :cvar VALUE_4: Agravamento
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class ExameOrdExame(Enum):
    """
    Ordem do exame.

    Validação: Preenchimento obrigatório se {procRealizado}(./procRealizado) = [0281].

    :cvar VALUE_1: Inicial
    :cvar VALUE_2: Sequencial
    """

    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2220 - Monitoramento da Saúde do Trabalhador.

    :ivar evtMonit: Evento Monitoramento da Saúde do Trabalhador. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_EXT_SEM_IMPACTO_FOPAG
        REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EXISTE_EVENTO_TSV_INICIO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXISTE_VINCULO REGRA:REGRA_EXTEMP_REINTEGRACAO
        REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_RETIFICA_MESMO_VINCULO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtMonit/v_S_01_03_00"

    evtMonit: ESocial.EvtMonit = field(
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
    class EvtMonit(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar exMedOcup: Informações do exame médico ocupacional. CHAVE_GRUPO: {tpExameOcup*}
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
        ideVinculo: str = field(
            metadata={
                "type": "Element",
            }
        )
        exMedOcup: ESocial.EvtMonit.ExMedOcup = field(
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
        class ExMedOcup(CommonMixin):
            """
            :ivar tpExameOcup:
            :ivar aso: ASO DESCRICAO_COMPLETA:Detalhamento das informações do Atestado de Saúde Ocupacional -
                ASO. CHAVE_GRUPO: {dtAso*}
            :ivar respMonit: Informações sobre o médico responsável/coordenador do PCMSO. CONDICAO_GRUPO: OC
            """

            tpExameOcup: ExMedOcupTpExameOcup = field(
                metadata={
                    "type": "Element",
                }
            )
            aso: ESocial.EvtMonit.ExMedOcup.Aso = field(
                metadata={
                    "type": "Element",
                }
            )
            respMonit: None | ESocial.EvtMonit.ExMedOcup.RespMonit = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Aso(CommonMixin):
                """
                :ivar dtAso: Data de emissão do ASO. Validação: Deve ser uma data válida, igual ou anterior à
                    data atual e igual ou posterior à data de início da obrigatoriedade deste evento para o
                    empregador no eSocial. Se {tpExameOcup}(../tpExameOcup) for diferente de [0], também deve
                    ser igual ou posterior à data de admissão/exercício ou de início.
                :ivar resAso:
                :ivar exame: Avaliações clínicas e exames complementares realizados DESCRICAO_COMPLETA:Grupo que
                    detalha as avaliações clínicas e os exames complementares porventura realizados pelo
                    trabalhador em virtude do determinado nos Anexos da NR-07, além de outros solicitados pelo
                    médico e os referentes ao ASO. CHAVE_GRUPO: {dtExm}, {procRealizado}
                :ivar medico: Informações sobre o médico emitente do ASO.
                """

                dtAso: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                resAso: None | AsoResAso = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                exame: list[ESocial.EvtMonit.ExMedOcup.Aso.Exame] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 99,
                    },
                )
                medico: ESocial.EvtMonit.ExMedOcup.Aso.Medico = field(
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass(kw_only=True)
                class Exame(CommonMixin):
                    """
                    :ivar dtExm: Data do exame realizado. Validação: Deve ser uma data válida, igual ou anterior
                        à data do ASO informada em {dtAso}(../dtAso).
                    :ivar procRealizado:
                    :ivar obsProc: Observação sobre o procedimento diagnóstico realizado. Validação:
                        Preenchimento obrigatório se {procRealizado}(./procRealizado) = [0583, 0998, 0999, 1128,
                        1230, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 9999].
                    :ivar ordExame:
                    :ivar indResult:
                    """

                    dtExm: XmlDate = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    procRealizado: str = field(
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{4}",
                        }
                    )
                    obsProc: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    ordExame: None | ExameOrdExame = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    indResult: None | ExameIndResult = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class Medico(CommonMixin):
                    """
                    :ivar nmMed: Preencher com o nome do médico emitente do ASO.
                    :ivar nrCRM:
                    :ivar ufCRM: Preencher com a sigla da Unidade da Federação - UF de expedição do CRM.
                        Validação: O preenchimento do campo não é obrigatório se o endereço do trabalhador em
                        S-2200/S-2300, ou em S-2205 vigente em {dtAso}(../dtAso), for no exterior.
                    """

                    nmMed: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    nrCRM: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 10,
                            "pattern": r".*[^\s].*",
                        },
                    )
                    ufCRM: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

            @dataclass(kw_only=True)
            class RespMonit(CommonMixin):
                """
                :ivar cpfResp: Preencher com o CPF do médico responsável/coordenador do PCMSO. Validação: Se
                    informado, deve ser um CPF válido.
                :ivar nmResp: Preencher com o nome do médico responsável/coordenador do PCMSO.
                :ivar nrCRM:
                :ivar ufCRM: Preencher com a sigla da UF de expedição do CRM.
                """

                cpfResp: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                nmResp: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                nrCRM: str = field(
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 10,
                        "pattern": r".*[^\s].*",
                    }
                )
                ufCRM: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
