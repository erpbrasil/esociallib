from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCdBenefAlt/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2405 - Cadastro de Beneficiário - Entes Públicos - Alteração.

    :ivar evtCdBenefAlt: Evento Cadastro de Beneficiário - Alteração DESCRICAO_COMPLETA:Evento Cadastro de
        Beneficiário - Entes Públicos - Alteração. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_EXT_SEM_IMPACTO_FOPAG REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCdBenefAlt/v_S_01_03_00"

    evtCdBenefAlt: ESocial.EvtCdBenefAlt = field(
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
    class EvtCdBenefAlt(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideBenef: Identificação do beneficiário. CHAVE_GRUPO: {cpfBenef*}
        :ivar alteracao: Alteração de dados do beneficiário. CHAVE_GRUPO: {dtAlteracao*}
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
        ideBenef: ESocial.EvtCdBenefAlt.IdeBenef = field(
            metadata={
                "type": "Element",
            }
        )
        alteracao: ESocial.EvtCdBenefAlt.Alteracao = field(
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
        class IdeBenef(CommonMixin):
            """
            :ivar cpfBenef: Informar o CPF do beneficiário. Validação: Deve ser um CPF válido e cadastrado pelo
                órgão público declarante por meio do evento S-2400.
            """

            cpfBenef: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class Alteracao(CommonMixin):
            """
            :ivar dtAlteracao: Preencher com a data de alteração. Validação: Deve ser posterior à data de início
                informada no evento S-2400 e igual ou anterior à data atual.
            :ivar dadosBenef: Dados do beneficiário.
            """

            dtAlteracao: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dadosBenef: ESocial.EvtCdBenefAlt.Alteracao.DadosBenef = field(
                metadata={
                    "type": "Element",
                }
            )

            @dataclass(kw_only=True)
            class DadosBenef(CommonMixin):
                """
                :ivar nmBenefic:
                :ivar sexo: Sexo do beneficiário.
                :ivar racaCor: Etnia e raça do beneficiário, conforme sua autoclassificação (art. 39, § 8º, da
                    Lei 12.288/2010). Validação: Se {dtAlteracao}(../dtAlteracao) for igual ou posterior a
                    [2024-04-22], não pode ser informado o valor [6].
                :ivar estCiv:
                :ivar incFisMen:
                :ivar endereco: Endereço do beneficiário. DESCRICAO_COMPLETA:Grupo de informações do endereço do
                    beneficiário.
                :ivar dependente: Informações dos dependentes. CHAVE_GRUPO: {tpDep}, {nmDep}, {dtNascto}
                    CONDICAO_GRUPO: OC
                """

                nmBenefic: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                sexo: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                racaCor: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                estCiv: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                incFisMen: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                endereco: ESocial.EvtCdBenefAlt.Alteracao.DadosBenef.Endereco = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dependente: list[ESocial.EvtCdBenefAlt.Alteracao.DadosBenef.Dependente] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )

                @dataclass(kw_only=True)
                class Endereco(CommonMixin):
                    brasil: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    exterior: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class Dependente(CommonMixin):
                    """
                    :ivar tpDep:
                    :ivar nmDep:
                    :ivar dtNascto:
                    :ivar cpfDep:
                    :ivar sexoDep: Sexo do dependente.
                    :ivar depIRRF:
                    :ivar incFisMen:
                    :ivar descrDep:
                    """

                    tpDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    nmDep: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtNascto: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    cpfDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    sexoDep: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    depIRRF: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    incFisMen: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    descrDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
