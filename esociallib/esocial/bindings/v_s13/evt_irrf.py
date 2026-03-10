from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtIrrf/v_S_01_03_00"


class InfoIrrfIndExistInfo(Enum):
    """
    Indicativo de existência de valores de bases ou de tributos.

    :cvar VALUE_1: Há informações de IRRF
    :cvar VALUE_2: Há movimento, porém não há informações de IRRF
    :cvar VALUE_3: Não há movimento no período informado em {perApur}(5012_ideEvento_perApur)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-5012 - Imposto de Renda Retido na Fonte Consolidado por Contribuinte.

    :ivar evtIrrf: Evento IRRF Consolidado por Contribuinte. DESCRICAO_COMPLETA:Evento Imposto de Renda Retido
        na Fonte Consolidado por Contribuinte. CHAVE_GRUPO: {Id}
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtIrrf/v_S_01_03_00"

    evtIrrf: ESocial.EvtIrrf = field(
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
    class EvtIrrf(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoIRRF: Informações relativas ao Imposto de Renda.
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
        infoIRRF: ESocial.EvtIrrf.InfoIrrf = field(
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
        class InfoIrrf(CommonMixin):
            """
            :ivar nrRecArqBase:
            :ivar indExistInfo:
            :ivar infoCRMen: Totalizador do IRRF por CR mensal. DESCRICAO_COMPLETA:Informações consolidadas do
                IRRF, por Código de Receita - CR mensal. Evento de origem: S-5002. CHAVE_GRUPO: {CRMen}
                CONDICAO_GRUPO: OC
            :ivar infoCRDia: Totalizador do IRRF por CR diário. DESCRICAO_COMPLETA:Informações consolidadas do
                IRRF, por Código de Receita - CR diário. Evento de origem: S-5002. CHAVE_GRUPO: {perApurDia},
                {CRDia} CONDICAO_GRUPO: OC
            """

            nrRecArqBase: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indExistInfo: InfoIrrfIndExistInfo = field(
                metadata={
                    "type": "Element",
                }
            )
            infoCRMen: list[ESocial.EvtIrrf.InfoIrrf.InfoCrmen] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 50,
                },
            )
            infoCRDia: list[ESocial.EvtIrrf.InfoIrrf.InfoCrdia] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 350,
                },
            )

            @dataclass(kw_only=True)
            class InfoCrmen(CommonMixin):
                """
                :ivar CRMen:
                :ivar vrCRMen: Valor correspondente ao Código de Receita - CR indicado em {CRMen}(./CRMen).
                """

                CRMen: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                vrCRMen: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class InfoCrdia(CommonMixin):
                """
                :ivar perApurDia: Período de apuração diário do Código de Receita - CR.
                :ivar CRDia:
                :ivar vrCRDia: Valor relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho
                    pagos a residente, para fins fiscais, no exterior.
                """

                perApurDia: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                CRDia: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                vrCRDia: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
