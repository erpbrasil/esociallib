from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCdBenefIn/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2400 - Cadastro de Beneficiário - Entes Públicos - Início.

    :ivar evtCdBenefIn: Evento Cadastro de Beneficiário - Início DESCRICAO_COMPLETA:Evento Cadastro de
        Beneficiário - Entes Públicos - Início. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_EXT_SEM_IMPACTO_FOPAG REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_VALIDA_CNPJ REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCdBenefIn/v_S_01_03_00"

    evtCdBenefIn: ESocial.EvtCdBenefIn = field(
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
    class EvtCdBenefIn(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador: Informações de identificação do empregador. CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar beneficiario: Grupo de informações do beneficiário. CHAVE_GRUPO: {cpfBenef*}
        :ivar Id:
        """

        ideEvento: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: ESocial.EvtCdBenefIn.IdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        beneficiario: ESocial.EvtCdBenefIn.Beneficiario = field(
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
            tpInsc: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nrInsc: str = field(
                metadata={
                    "type": "Element",
                    "pattern": r"\d{8}|\d{14}",
                }
            )

        @dataclass(kw_only=True)
        class Beneficiario(CommonMixin):
            """
            :ivar cpfBenef: Informar o CPF do beneficiário. Validação: Não é possível existir dois eventos
                originais do mesmo órgão público declarante para o mesmo CPF do beneficiário.
            :ivar nmBenefic:
            :ivar dtNascto: Preencher com a data de nascimento.
            :ivar dtInicio: Preencher com a data de início do cadastro do beneficiário. Informar a data de
                início da obrigatoriedade dos eventos não periódicos para o ente público no eSocial caso o
                beneficiário possua cadastro anterior a essa data. Validação: Deve ser igual ou posterior à data
                de início da obrigatoriedade dos eventos não periódicos para o ente público no eSocial e igual
                ou anterior à data atual.
            :ivar sexo: Sexo do beneficiário. Validação: Informação obrigatória se {dtInicio}(./dtInicio) for
                posterior ao início da obrigatoriedade dos eventos não periódicos para o ente público no
                eSocial.
            :ivar racaCor: Etnia e raça do beneficiário, conforme sua autoclassificação (art. 39, § 8º, da Lei
                12.288/2010). Validação: Se {dtInicio}(./dtInicio) for igual ou posterior a [2024-04-22], não
                pode ser informado o valor [6].
            :ivar estCiv:
            :ivar incFisMen:
            :ivar dtIncFisMen: Preencher com a data do reconhecimento da incapacidade. Validação: Informação
                obrigatória e exclusiva se {incFisMen}(./incFisMen) = [S].
            :ivar endereco: Endereço do beneficiário. DESCRICAO_COMPLETA:Grupo de informações do endereço do
                beneficiário.
            :ivar dependente: Informações dos dependentes. CHAVE_GRUPO: {tpDep}, {nmDep}, {dtNascto}
                CONDICAO_GRUPO: OC
            """

            cpfBenef: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nmBenefic: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtNascto: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtInicio: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            sexo: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
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
            dtIncFisMen: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            endereco: ESocial.EvtCdBenefIn.Beneficiario.Endereco = field(
                metadata={
                    "type": "Element",
                }
            )
            dependente: list[ESocial.EvtCdBenefIn.Beneficiario.Dependente] = field(
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
                :ivar sexoDep: Sexo do dependente. Validação: Informação obrigatória se {dtInicio}(../dtInicio)
                    for posterior ao início da obrigatoriedade dos eventos não periódicos para o ente público no
                    eSocial.
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
                sexoDep: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
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
