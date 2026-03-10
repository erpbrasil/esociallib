from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtContratAvNP/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1270 - Contratação de Trabalhadores Avulsos Não Portuários.

    :ivar evtContratAvNP: Evento Contratação de Trabalhadores Avulsos Não Portuários. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVE_FOPAG_IND_RETIFICACAO
        REGRA:REGRA_EVE_FOPAG_PERMITE_EXCLUSAO REGRA:REGRA_EVE_FOPAG_SIMPLIFICADO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtContratAvNP/v_S_01_03_00"

    evtContratAvNP: ESocial.EvtContratAvNp = field(
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
    class EvtContratAvNp(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar remunAvNP: Remuneração dos trabalhadores avulsos não portuários DESCRICAO_COMPLETA:Grupo que
            apresenta a remuneração dos trabalhadores avulsos não portuários, de forma totalizada por
            estabelecimento contratante. CHAVE_GRUPO: {tpInsc}, {nrInsc}, {codLotacao}
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
        remunAvNP: list[ESocial.EvtContratAvNp.RemunAvNp] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass(kw_only=True)
        class RemunAvNp(CommonMixin):
            """
            :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.
            :ivar nrInsc: Informar o número de inscrição do estabelecimento do contribuinte de acordo com o tipo
                de inscrição indicado no campo {remunAvNP/tpInsc}(./tpInsc). Validação: Deve ser um número de
                inscrição válido e existente na Tabela de Estabelecimentos (S-1005).
            :ivar codLotacao: Informar o código atribuído pelo empregador para a lotação tributária. Validação:
                Deve ser um código válido e existente na Tabela de Lotações Tributárias (S-1020).
            :ivar vrBcCp00: Valor da base de cálculo da contribuição previdenciária sobre a remuneração dos
                trabalhadores avulsos não portuários.
            :ivar vrBcCp15: Valor da base de cálculo da contribuição adicional para o financiamento dos
                benefícios de aposentadoria especial após 15 anos de contribuição.
            :ivar vrBcCp20: Valor da base de cálculo da contribuição adicional para o financiamento dos
                benefícios de aposentadoria especial após 20 anos de contribuição.
            :ivar vrBcCp25: Valor da base de cálculo da contribuição adicional para o financiamento dos
                benefícios de aposentadoria especial após 25 anos de contribuição.
            :ivar vrBcCp13: Valor da base de cálculo da contribuição previdenciária sobre o 13° salário dos
                trabalhadores avulsos não portuários contratados.
            :ivar vrBcFgts: Valor da base de cálculo do FGTS sobre a remuneração dos trabalhadores avulsos não
                portuários contratados.
            :ivar vrDescCP: Preencher com o valor total da contribuição descontada dos trabalhadores avulsos não
                portuários.
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
            vrBcCp00: str = field(
                metadata={
                    "type": "Element",
                }
            )
            vrBcCp15: str = field(
                metadata={
                    "type": "Element",
                }
            )
            vrBcCp20: str = field(
                metadata={
                    "type": "Element",
                }
            )
            vrBcCp25: str = field(
                metadata={
                    "type": "Element",
                }
            )
            vrBcCp13: str = field(
                metadata={
                    "type": "Element",
                }
            )
            vrBcFgts: str = field(
                metadata={
                    "type": "Element",
                }
            )
            vrDescCP: str = field(
                metadata={
                    "type": "Element",
                }
            )
