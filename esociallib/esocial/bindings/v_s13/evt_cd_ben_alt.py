from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCdBenAlt/v_S_01_03_00"


class SuspensaoMtvSuspensao(Enum):
    """
    Motivo da suspensão do benefício.

    :cvar VALUE_01: Suspensão por não recadastramento
    :cvar VALUE_99: Outros motivos de suspensão
    """

    VALUE_01 = "01"
    VALUE_99 = "99"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2416 - Cadastro de Benefício - Entes Públicos - Alteração.

    :ivar evtCdBenAlt: Evento Cadastro de Benefício - Alteração DESCRICAO_COMPLETA:Evento Cadastro de Benefício
        - Entes Públicos - Alteração. CHAVE_GRUPO: {Id} REGRA:REGRA_ALTERA_TIPO_BENEFICIO
        REGRA:REGRA_BENEFICIO_ATIVO_NA_DTEVENTO REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXTEMP_REATIVACAO REGRA:REGRA_RETIFICA_MESMO_BENEFICIO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCdBenAlt/v_S_01_03_00"

    evtCdBenAlt: ESocial.EvtCdBenAlt = field(
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
    class EvtCdBenAlt(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideBeneficio:
        :ivar infoBenAlteracao: Informações do benefício - Alteração. CHAVE_GRUPO: {dtAltBeneficio*}
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
        infoBenAlteracao: ESocial.EvtCdBenAlt.InfoBenAlteracao = field(
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
        class InfoBenAlteracao(CommonMixin):
            """
            :ivar dtAltBeneficio: Data de alteração das informações relativas ao benefício. Validação: Deve ser
                igual ou anterior à data atual.
            :ivar dadosBeneficio: Dados relativos ao benefício.
            """

            dtAltBeneficio: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dadosBeneficio: ESocial.EvtCdBenAlt.InfoBenAlteracao.DadosBeneficio = field(
                metadata={
                    "type": "Element",
                }
            )

            @dataclass(kw_only=True)
            class DadosBeneficio(CommonMixin):
                """
                :ivar tpBeneficio: Tipo de benefício. Validação: Deve ser um código válido e existente na Tabela
                    25. Se {cadIni}(2410_infoBenInicio_cadIni) em S-2410 for igual a [N], não é permitido
                    utilizar código do grupo [08] dessa tabela.
                :ivar tpPlanRP:
                :ivar dsc: Descrição do instrumento ou situação que originou o pagamento do benefício.
                    Validação: Preenchimento obrigatório se {tpBeneficio}(./tpBeneficio) = [0909, 1001, 1009].
                :ivar indSuspensao: Indicativo de suspensão do benefício.
                :ivar infoPenMorte: Informações relativas à pensão por morte. CONDICAO_GRUPO: O (se
                    {tpBeneficio}(../tpBeneficio) pertencer ao grupo [06]); N (nos demais casos)
                :ivar suspensao: Informações referentes à suspensão do benefício. CONDICAO_GRUPO: O (se
                    {indSuspensao}(../indSuspensao) = [S]; N (se {indSuspensao}(../indSuspensao) = [N]
                """

                tpBeneficio: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                tpPlanRP: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dsc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                indSuspensao: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                infoPenMorte: None | ESocial.EvtCdBenAlt.InfoBenAlteracao.DadosBeneficio.InfoPenMorte = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                suspensao: None | ESocial.EvtCdBenAlt.InfoBenAlteracao.DadosBeneficio.Suspensao = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoPenMorte(CommonMixin):
                    """
                    :ivar tpPenMorte:
                    :ivar instPenMorte: Informações do instituidor da pensão por morte. CONDICAO_GRUPO: OC
                        Validação: Se o grupo não for informado e
                        {dtAltBeneficio}(2416_infoBenAlteracao_dtAltBeneficio) &gt;= [2025-11-24], retornar
                        alerta.
                    """

                    tpPenMorte: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    instPenMorte: (
                        None | ESocial.EvtCdBenAlt.InfoBenAlteracao.DadosBeneficio.InfoPenMorte.InstPenMorte
                    ) = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InstPenMorte(CommonMixin):
                        """
                        :ivar tpDepInst: Tipo de dependente do instituidor da pensão por morte.
                        :ivar descrDepInst:
                        """

                        tpDepInst: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        descrDepInst: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                @dataclass(kw_only=True)
                class Suspensao(CommonMixin):
                    """
                    :ivar mtvSuspensao:
                    :ivar dscSuspensao: Descrição do motivo da suspensão do benefício. Validação: Preenchimento
                        obrigatório e exclusivo se {mtvSuspensao}(./mtvSuspensao) = [99].
                    """

                    mtvSuspensao: SuspensaoMtvSuspensao = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dscSuspensao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
