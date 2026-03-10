from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtFechaEvPer/v_S_01_03_00"


class InfoFechIndExcApur1250(Enum):
    """
    Indicativo de exclusão de apuração das aquisições de produção rural (eventos S-1250) do período de apuração.

    Validação: Não informar se {perApur}(1299_ideEvento_perApur) &gt;= [2021-07] ou se
    {indApuracao}(1299_ideEvento_indApuracao) = [2]. Preenchimento obrigatório caso o campo tenha sido informado em
    fechamento anterior do mesmo período de apuração.

    :cvar S: Sim
    """

    S = "S"


class InfoFechTransDctfweb(Enum):
    """
    Solicitação de transmissão imediata da DCTFWeb.

    Validação: Não informar se {perApur}(1299_ideEvento_perApur) &lt; [2021-10]. Preenchimento obrigatório se
    {perApur}(1299_ideEvento_perApur) &gt;= [2021-10] e
    ({classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [04] ou
    {indGuia}(1299_ideEvento_indGuia) estiver informado).

    :cvar S: Sim
    """

    S = "S"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1299 - Fechamento dos Eventos Periódicos.

    :ivar evtFechaEvPer: Evento Fechamento dos Eventos Periódicos. CHAVE_GRUPO: {Id}
        REGRA:REGRA_CONVIVENCIA_VERSAO_PIS REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVE_FOPAG_SIMPLIFICADO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_REMUN_ANUAL_DEZEMBRO REGRA:REGRA_VALIDA_EMPREGADOR
        REGRA:REGRA_VALIDA_FECHAMENTO_FOPAG
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtFechaEvPer/v_S_01_03_00"

    evtFechaEvPer: ESocial.EvtFechaEvPer = field(
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
    class EvtFechaEvPer(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoFech: Informações do fechamento.
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
        infoFech: ESocial.EvtFechaEvPer.InfoFech = field(
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
        class InfoFech(CommonMixin):
            """
            :ivar evtRemun: Possui informações relativas a remuneração de trabalhadores ou provento/pensão de
                beneficiários no período de apuração? Validação: Se for igual a [S], deve existir evento de
                remuneração (S-1200, S-1202, S-1207, S-2299 ou S-2399) para o período de apuração, considerando
                o campo {indGuia}(1299_ideEvento_indGuia). Caso contrário, não deve existir evento de
                remuneração.
            :ivar evtPgtos: Possui informações de pagamento de rendimentos do trabalho no período de apuração?
                Validação: Se for igual a [S], deve existir o evento S-1210 para o período de apuração,
                considerando o campo {indGuia}(1299_ideEvento_indGuia). Caso contrário, não deve existir o
                evento.
            :ivar evtComProd: Possui informações de comercialização de produção? Validação: Se for igual a [S],
                deve existir o evento S-1260 para o período de apuração, considerando o campo
                {indGuia}(1299_ideEvento_indGuia). Caso contrário, não deve existir o evento.
            :ivar evtContratAvNP: Contratou, por intermédio de sindicato, serviços de trabalhadores avulsos não
                portuários? Validação: Se for igual a [S], deve existir o evento S-1270 para o período de
                apuração, considerando o campo {indGuia}(1299_ideEvento_indGuia). Caso contrário, não deve
                existir o evento.
            :ivar evtInfoComplPer: Possui informações de desoneração de folha de pagamento ou, sendo empresa
                enquadrada no Simples, possui informações sobre a receita obtida em atividades cuja contribuição
                previdenciária incidente sobre a folha de pagamento é concomitantemente substituída e não
                substituída? Validação: Se for igual a [S], deve existir o evento S-1280 para o período de
                apuração. Caso contrário, não deve existir o evento.
            :ivar indExcApur1250:
            :ivar transDCTFWeb:
            :ivar naoValid:
            """

            evtRemun: str = field(
                metadata={
                    "type": "Element",
                }
            )
            evtPgtos: str = field(
                metadata={
                    "type": "Element",
                }
            )
            evtComProd: str = field(
                metadata={
                    "type": "Element",
                }
            )
            evtContratAvNP: str = field(
                metadata={
                    "type": "Element",
                }
            )
            evtInfoComplPer: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indExcApur1250: None | InfoFechIndExcApur1250 = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            transDCTFWeb: None | InfoFechTransDctfweb = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            naoValid: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
