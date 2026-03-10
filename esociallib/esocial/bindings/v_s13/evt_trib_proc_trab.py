from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_03_00"


class InfoCrirrfTpCr(Enum):
    """
    Código de Receita - CR relativo a Imposto de Renda Retido na Fonte.

    :cvar VALUE_593656: IRRF - Decisão da Justiça do Trabalho
    :cvar VALUE_056152: IRRF - CCP/NINTER
    :cvar VALUE_188951: IRRF - RRA
    """

    VALUE_593656 = 593656
    VALUE_056152 = "056152"
    VALUE_188951 = 188951


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-5501 - Informações Consolidadas de Tributos Decorrentes de Processo Trabalhista.

    :ivar evtTribProcTrab: Evento Informações Consolidadas de Tributos Decorrentes de Processo Trabalhista.
        CHAVE_GRUPO: {Id}
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTribProcTrab/v_S_01_03_00"

    evtTribProcTrab: ESocial.EvtTribProcTrab = field(
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
    class EvtTribProcTrab(CommonMixin):
        """
        :ivar ideEvento: Informações de identificação do evento.
        :ivar ideEmpregador: Informações de identificação do empregador ou do contribuinte que prestou a
            informação. CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar ideProc: Identificação do processo. CHAVE_GRUPO: {nrProcTrab*}, {perApur*}
        :ivar Id:
        """

        ideEvento: ESocial.EvtTribProcTrab.IdeEvento = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: ESocial.EvtTribProcTrab.IdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        ideProc: ESocial.EvtTribProcTrab.IdeProc = field(
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
        class IdeEvento(CommonMixin):
            """
            :ivar nrRecArqBase: Preencher com o número do recibo do arquivo que deu origem ao presente arquivo
                de retorno. Validação: Deve ser um recibo de entrega válido, correspondente ao arquivo que deu
                origem ao presente arquivo de retorno (S-2501, S-2555 ou S-3500).
            """

            nrRecArqBase: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class IdeEmpregador(CommonMixin):
            """
            :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição do empregador ou
                contribuinte que prestou a informação, conforme Tabela 05.
            :ivar nrInsc: Informar o número de inscrição do empregador ou contribuinte que prestou a informação,
                de acordo com o tipo de inscrição indicado no campo {ideEmpregador/tpInsc}(./tpInsc) e conforme
                informado em S-1000.
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
                Validação: a) Se o evento de origem for S-2501 ou S-2555, retornar o campo {nrProcTrab} desse
                evento; b) Se o evento de origem for S-3500, retornar o campo {nrProcTrab} do evento S-2501 ou
                S-2555 objeto da exclusão.
            :ivar perApur: Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença.
                Validação: a) Se o evento de origem for S-2501 ou S-2555, retornar o campo {perApurPgto} desse
                evento; b) Se o evento de origem for S-3500, retornar o campo {perApurPgto} do evento S-2501 ou
                S-2555 objeto da exclusão.
            :ivar infoTributos: Identificação do período e da base de cálculo dos tributos referentes ao
                processo trabalhista. CHAVE_GRUPO: {perRef}
            :ivar infoCRIRRF: Informações de IRRF referentes ao processo trabalhista.
                DESCRICAO_COMPLETA:Informações de Imposto de Renda Retido na Fonte, consolidadas por Código de
                Receita - CR. CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
            """

            nrProcTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            perApur: str = field(
                metadata={
                    "type": "Element",
                }
            )
            infoTributos: list[ESocial.EvtTribProcTrab.IdeProc.InfoTributos] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 999,
                },
            )
            infoCRIRRF: list[ESocial.EvtTribProcTrab.IdeProc.InfoCrirrf] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class InfoTributos(CommonMixin):
                """
                :ivar perRef: Informar o mês/ano (formato AAAA-MM) de referência das informações. Validação: a)
                    Se o evento de origem for S-2501, retornar o campo {perRef}(2501_ideTrab_calcTrib_perRef)
                    desse evento; Validação: b) Se o evento de origem for S-2555, retornar o campo
                    {perRef}(2501_ideTrab_calcTrib_perRef) dos eventos S-2501 abrangidos por esse evento; c) Se
                    o evento de origem for S-3500 que exclua S-2501, retornar o campo
                    {perRef}(2501_ideTrab_calcTrib_perRef) do evento S-2501 objeto da exclusão; d) Se o evento
                    de origem for S-3500 que exclua S-2555, retornar o campo
                    {perRef}(2501_ideTrab_calcTrib_perRef) dos eventos S-2501 abrangidos pelo evento S-2555
                    objeto da exclusão.
                :ivar infoCRContrib: Informações das contribuições sociais referentes ao processo trabalhista.
                    DESCRICAO_COMPLETA:Informações das contribuições sociais devidas à Previdência Social e
                    Outras Entidades e Fundos, consolidadas por {perRef}(../perRef) e por Código de Receita -
                    CR. CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
                """

                perRef: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                infoCRContrib: list[ESocial.EvtTribProcTrab.IdeProc.InfoTributos.InfoCrcontrib] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )

                @dataclass(kw_only=True)
                class InfoCrcontrib(CommonMixin):
                    """
                    :ivar tpCR:
                    :ivar vrCR: Valor correspondente ao Código de Receita - CR. Validação: Deve ser apurado de
                        acordo com a legislação em vigor na competência. Deve ser maior que 0 (zero).
                    """

                    tpCR: str = field(
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{6}",
                        }
                    )
                    vrCR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

            @dataclass(kw_only=True)
            class InfoCrirrf(CommonMixin):
                """
                :ivar tpCR:
                :ivar vrCR: Valor correspondente ao Código de Receita - CR. Validação: Deve ser apurado de
                    acordo com a legislação em vigor na competência. Deve ser maior ou igual a 0 (zero).
                """

                tpCR: InfoCrirrfTpCr = field(
                    metadata={
                        "type": "Element",
                    }
                )
                vrCR: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
