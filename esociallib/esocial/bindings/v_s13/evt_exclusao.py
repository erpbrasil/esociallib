from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtExclusao/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-3000 - Exclusão de Eventos.

    :ivar evtExclusao: Evento Exclusão DESCRICAO_COMPLETA:Evento Exclusão de Eventos. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVE_EXCLUSAO_VALIDA_NRRECIBO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXTEMP_DOMESTICO REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_VALIDA_EMPREGADOR REGRA:REGRA_VALIDA_PERANT_1210
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtExclusao/v_S_01_03_00"

    evtExclusao: ESocial.EvtExclusao = field(
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
    class EvtExclusao(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoExclusao: Informação do evento que será excluído DESCRICAO_COMPLETA:Grupo que identifica o
            evento objeto da exclusão.
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
        infoExclusao: ESocial.EvtExclusao.InfoExclusao = field(
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
        class InfoExclusao(CommonMixin):
            """
            :ivar tpEvento:
            :ivar nrRecEvt: Preencher com o número do recibo do evento que será excluído. Validação: O recibo
                deve ser relativo ao mesmo tipo de evento indicado em {tpEvento}(./tpEvento) e o respectivo
                evento não deve constar como excluído ou retificado. Além disso, no caso de exclusão de eventos
                em que existe a identificação do trabalhador, o evento que está sendo excluído deve referir-se
                ao mesmo trabalhador identificado por {cpfTrab}(./ideTrabalhador_cpfTrab).
            :ivar ideTrabalhador: Identificação do trabalhador a que se refere o evento a ser excluído
                DESCRICAO_COMPLETA:Grupo que identifica a qual trabalhador se refere o evento a ser excluído.
                CONDICAO_GRUPO: O (se {tpEvento}(../tpEvento) corresponder a um dos eventos não periódicos
                (S-2190 a S-2420, S-8200 ou S-8299) ou um dos eventos periódicos (S-1200 a S-1210); N (nos
                demais casos)
            :ivar ideFolhaPagto: Identificação do período de apuração a que se refere o evento que será excluído
                DESCRICAO_COMPLETA:Grupo que identifica a qual período de apuração pertence o evento que será
                excluído. CONDICAO_GRUPO: O (se {tpEvento}(../tpEvento) corresponder a um dos eventos periódicos
                (S-1200 a S-1280 ou S-1300)); N (nos demais casos)
            """

            tpEvento: str = field(
                metadata={
                    "type": "Element",
                    "length": 6,
                }
            )
            nrRecEvt: str = field(
                metadata={
                    "type": "Element",
                }
            )
            ideTrabalhador: None | ESocial.EvtExclusao.InfoExclusao.IdeTrabalhador = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            ideFolhaPagto: None | ESocial.EvtExclusao.InfoExclusao.IdeFolhaPagto = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class IdeTrabalhador(CommonMixin):
                """
                :ivar cpfTrab: Preencher com o número do CPF do trabalhador ou do beneficiário. Validação: O CPF
                    indicado deve existir na base de dados do RET.
                """

                cpfTrab: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class IdeFolhaPagto(CommonMixin):
                """
                :ivar indApuracao: Indicativo de período de apuração. Validação: Preenchimento obrigatório e
                    exclusivo se {tpEvento}(../tpEvento) = [S-1200, S-1202, S-1207, S-1280, S-1300].
                :ivar perApur: Informar o mês/ano (formato AAAA-MM) ou apenas o ano (formato AAAA) de referência
                    das informações. Validação: Deve ser um mês/ano ou ano válido, posterior à implementação do
                    eSocial. Somente pode ser informado ano (formato AAAA) se {indApuracao}(./indApuracao) =
                    [2].
                """

                indApuracao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                perApur: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
