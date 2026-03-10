from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtReativBen/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2418 - Reativação de Benefício - Entes Públicos.

    :ivar evtReativBen: Evento Reativação de Benefício DESCRICAO_COMPLETA:Evento Reativação de Benefício - Entes
        Públicos. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EXISTE_EVENTO_BENEFICIO_TERMINO REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_EXTEMP_REATIVACAO REGRA:REGRA_REATIVACAO_EXCLUSAO_EVENTO
        REGRA:REGRA_RETIFICA_MESMO_BENEFICIO REGRA:REGRA_VALIDA_CNPJ
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtReativBen/v_S_01_03_00"

    evtReativBen: ESocial.EvtReativBen = field(
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
    class EvtReativBen(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideBeneficio:
        :ivar infoReativ: Informações da reativação do benefício. CHAVE_GRUPO: {dtEfetReativ*}
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
        ideBeneficio: str = field(
            metadata={
                "type": "Element",
            }
        )
        infoReativ: ESocial.EvtReativBen.InfoReativ = field(
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
        class InfoReativ(CommonMixin):
            """
            :ivar dtEfetReativ: Informar a data da efetiva reativação do benefício. Validação: Deve ser
                posterior à data de cessação do benefício e igual ou anterior à data atual.
            :ivar dtEfeito: Data de início dos efeitos financeiros da reativação do benefício. Validação: Deve
                ser uma data igual ou anterior à data da efetiva reativação do benefício e posterior à data de
                sua cessação.
            """

            dtEfetReativ: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtEfeito: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
