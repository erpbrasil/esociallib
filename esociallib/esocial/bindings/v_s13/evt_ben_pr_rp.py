from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtBenPrRP/v_S_01_03_00"


@dataclass(kw_only=True)
class TIdeEstab(CommonMixin):
    """
    Identificação da unidade do órgão público DESCRICAO_COMPLETA:Identificação da unidade do órgão público na qual
    o beneficiário possui provento ou pensão.

    CHAVE_GRUPO: {tpInsc}, {nrInsc}.

    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição da unidade do órgão público.
    """

    class Meta:
        name = "T_ideEstab"

    tpInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBenPrRP/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBenPrRP/v_S_01_03_00",
        }
    )


@dataclass(kw_only=True)
class TItensRemunRppsPerApur(CommonMixin):
    class Meta:
        name = "T_itensRemun_rpps_perApur"

    descFolha: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBenPrRP/v_S_01_03_00",
        },
    )


@dataclass(kw_only=True)
class TIdeEstabPerAnt(TIdeEstab):
    """
    :ivar itensRemun: Itens que compõem o provento ou pensão do beneficiário DESCRICAO_COMPLETA:Rubricas que
        compõem o provento ou pensão do beneficiário.
    """

    class Meta:
        name = "T_ideEstab_perAnt"

    itensRemun: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBenPrRP/v_S_01_03_00",
            "min_occurs": 1,
            "max_occurs": 200,
        },
    )


@dataclass(kw_only=True)
class TIdeEstabPerApur(TIdeEstab):
    """
    :ivar itensRemun: Itens que compõem o provento ou pensão do beneficiário DESCRICAO_COMPLETA:Rubricas que
        compõem o provento ou pensão do beneficiário.
    """

    class Meta:
        name = "T_ideEstab_perApur"

    itensRemun: list[TItensRemunRppsPerApur] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBenPrRP/v_S_01_03_00",
            "min_occurs": 1,
            "max_occurs": 200,
        },
    )


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1207 - Benefícios - Entes Públicos.

    :ivar evtBenPrRP: Evento Benefícios - Entes Públicos. CHAVE_GRUPO: {Id} REGRA:REGRA_CONTROLE_DUPLICIDADE
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_REMUN_ANUAL_DEZEMBRO
        REGRA:REGRA_REMUN_BENEFICIO_EXISTENTE_RET REGRA:REGRA_REMUN_IND_RETIFICACAO
        REGRA:REGRA_REMUN_PERMITE_EXCLUSAO REGRA:REGRA_RUBRICA_COMPATIVEL_DECTERCEIRO
        REGRA:REGRA_RUBRICA_ECONSIGNADO REGRA:REGRA_VALIDA_EMPREGADOR REGRA:REGRA_VALIDA_PERIODO_APURACAO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtBenPrRP/v_S_01_03_00"

    evtBenPrRP: ESocial.EvtBenPrRp = field(
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
    class EvtBenPrRp(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideBenef: Identificação do beneficiário. CHAVE_GRUPO: {cpfBenef*}
        :ivar dmDev: Demonstrativo de valores devidos ao beneficiário DESCRICAO_COMPLETA:Identificação de cada
            um dos demonstrativos de valores devidos ao beneficiário. CHAVE_GRUPO: {ideDmDev}
            REGRA:REGRA_DEMONSTRATIVO
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
        ideBenef: ESocial.EvtBenPrRp.IdeBenef = field(
            metadata={
                "type": "Element",
            }
        )
        dmDev: list[ESocial.EvtBenPrRp.DmDev] = field(
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
        class IdeBenef(CommonMixin):
            """
            :ivar cpfBenef: Informar o CPF do beneficiário. Validação: Deve ser um CPF válido.
            """

            cpfBenef: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class DmDev(CommonMixin):
            """
            :ivar ideDmDev: Identificador atribuído pelo órgão público para o demonstrativo de valores devidos
                ao beneficiário. O ente público pode preencher este campo utilizando-se de um identificador
                padrão para todos os beneficiários; no entanto, havendo mais de um demonstrativo relativo a uma
                mesma competência, devem ser utilizados identificadores diferentes para cada um dos
                demonstrativos. Validação: Deve ser um identificador único dentro do mesmo
                {perApur}(1207_ideEvento_perApur) para cada um dos demonstrativos do beneficiário.
                REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar nrBeneficio: Preencher com o número do benefício.
            :ivar indRRA:
            :ivar infoRRA:
            :ivar infoPerApur: Informações relativas ao período de apuração. CONDICAO_GRUPO: O (se não existir o
                grupo {infoPerAnt}(1207_dmDev_infoPerAnt)); OC (nos demais casos)
            :ivar infoPerAnt: Informações relativas a períodos anteriores DESCRICAO_COMPLETA:Grupo destinado às
                informações relativas a períodos anteriores. Somente preencher esse grupo se houver proventos ou
                pensões retroativos. CONDICAO_GRUPO: O (se não existir o grupo
                {infoPerApur}(1207_dmDev_infoPerApur) e {indApuracao}(1207_ideEvento_indApuracao) = [1]); N (se
                {indApuracao}(1207_ideEvento_indApuracao) = [2]); OC (nos demais casos)
            """

            ideDmDev: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nrBeneficio: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indRRA: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoRRA: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoPerApur: None | ESocial.EvtBenPrRp.DmDev.InfoPerApur = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoPerAnt: None | ESocial.EvtBenPrRp.DmDev.InfoPerAnt = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class InfoPerApur(CommonMixin):
                ideEstab: list[TIdeEstabPerApur] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 500,
                    },
                )

            @dataclass(kw_only=True)
            class InfoPerAnt(CommonMixin):
                """
                :ivar idePeriodo: Identificação do período de referência do provento ou pensão
                    DESCRICAO_COMPLETA:Identificação do período ao qual se referem as diferenças de provento ou
                    pensão. CHAVE_GRUPO: {perRef}
                """

                idePeriodo: list[ESocial.EvtBenPrRp.DmDev.InfoPerAnt.IdePeriodo] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 180,
                    },
                )

                @dataclass(kw_only=True)
                class IdePeriodo(CommonMixin):
                    """
                    :ivar perRef: Informar o período ao qual se refere o complemento de provento ou pensão, no
                        formato AAAA-MM. Validação: Deve ser igual ou anterior ao período de apuração informado
                        em {perApur}(1207_ideEvento_perApur). Deve ser informado no formato AAAA-MM.
                    :ivar ideEstab:
                    """

                    perRef: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    ideEstab: list[TIdeEstabPerAnt] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 500,
                        },
                    )
