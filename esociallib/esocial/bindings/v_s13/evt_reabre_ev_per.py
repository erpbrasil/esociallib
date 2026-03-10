from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtReabreEvPer/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1298 - Reabertura dos Eventos Periódicos.

    :ivar evtReabreEvPer: Evento Reabertura dos Eventos Periódicos. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVE_FOPAG_SIMPLIFICADO REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_REABERTURA_VALIDA_PERIODO_APURACAO REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtReabreEvPer/v_S_01_03_00"

    evtReabreEvPer: ESocial.EvtReabreEvPer = field(
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
    class EvtReabreEvPer(CommonMixin):
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
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )
