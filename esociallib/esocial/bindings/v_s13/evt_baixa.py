from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtBaixa/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-8299 - Baixa Judicial do Vínculo.

    :ivar evtBaixa: Evento Baixa Judicial do Vínculo. CHAVE_GRUPO: {Id} REGRA:REGRA_BAIXA_JUDICIAL
        REGRA:REGRA_BAIXA_TRABALHADOR_AFASTADO REGRA:REGRA_DESLIG_EXCLUI_DESLIGAMENTO_REINTEG
        REGRA:REGRA_DESLIG_EXCLUSAO_EVENTO REGRA:REGRA_DESLIG_EXISTE_EVENTO_POSTERIOR
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_VINCULO_ATIVO_NA_DTEVENTO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtBaixa/v_S_01_03_00"

    evtBaixa: ESocial.EvtBaixa = field(
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
    class EvtBaixa(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar infoBaixa: Informações relativas à baixa judicial do vínculo. CHAVE_GRUPO: {dtDeslig*}
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
        infoBaixa: ESocial.EvtBaixa.InfoBaixa = field(
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
        class InfoBaixa(CommonMixin):
            """
            :ivar mtvDeslig:
            :ivar dtDeslig: Preencher com a data de desligamento do vínculo (último dia trabalhado). Validação:
                Deve ser uma data igual ou posterior a 24/09/2019 e igual ou anterior à data atual. No caso de
                empregado reintegrado e quando não se tratar de retificação do desligamento anterior à
                reintegração, também deve ser uma data igual ou posterior a
                {dtEfetRetorno}(2298_infoReintegr_dtEfetRetorno) do evento S-2298.
            :ivar dtProjFimAPI:
            :ivar nrProcTrab: Número que identifica o processo judicial onde a baixa do vínculo foi determinada.
                Validação: Deve ser um processo judicial válido, com 20 (vinte) algarismos.
            :ivar observacao: Observação relevante sobre o desligamento do trabalhador, que não esteja
                consignada em outros campos.
            """

            mtvDeslig: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtDeslig: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtProjFimAPI: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            nrProcTrab: str = field(
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
