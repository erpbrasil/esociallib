from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtConsolidContProc/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2555 - Solicitação de Consolidação das Informações de Tributos Decorrentes de Processo Trabalhista.

    :ivar evtConsolidContProc: Evento Solicitação de Consolidação das Informações de Tributos Decorrentes de
        Processo Trabalhista. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXISTE_2501 REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtConsolidContProc/v_S_01_03_00"

    evtConsolidContProc: ESocial.EvtConsolidContProc = field(
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
    class EvtConsolidContProc(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador: Informações de identificação do empregador ou do contribuinte que está prestando a
            informação. CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar ideProc: Identificação do processo. CHAVE_GRUPO: {nrProcTrab*}, {perApurPgto*}
        :ivar Id:
        """

        ideEvento: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: ESocial.EvtConsolidContProc.IdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        ideProc: ESocial.EvtConsolidContProc.IdeProc = field(
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
                Validação: Deve ser um número de processo válido.
            :ivar perApurPgto: Mês/ano em que é devida a obrigação de pagar a parcela prevista no
                acordo/sentença. Validação: Deve ser informado no formato AAAA-MM.
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
