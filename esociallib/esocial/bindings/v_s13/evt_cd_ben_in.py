from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCdBenIn/v_S_01_03_00"


class InfoBenInicioIndSitBenef(Enum):
    """
    Indicar a situação do benefício no órgão declarante.

    Validação: Preenchimento obrigatório e exclusivo se {cadIni}(./cadIni) = [N].

    :cvar VALUE_1: Benefício concedido pelo próprio órgão declarante
    :cvar VALUE_2: Benefício transferido de outro órgão
    :cvar VALUE_3: Mudança de CPF do beneficiário
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoHomologSitHomolog(Enum):
    """
    Informar se o benefício requer ou não homologação pelo Tribunal de Contas.

    :cvar VALUE_0: Não homologado
    :cvar VALUE_1: Homologado
    :cvar VALUE_2: Não requer homologação
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2410 - Cadastro de Benefício - Entes Públicos - Início.

    :ivar evtCdBenIn: Evento Cadastro de Benefício - Início DESCRICAO_COMPLETA:Evento Cadastro de Benefício -
        Entes Públicos - Início. CHAVE_GRUPO: {Id} REGRA:REGRA_BENEFICIO_VALIDA_NUMERO
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_EXTEMP_REATIVACAO REGRA:REGRA_MUDANCA_CPF REGRA:REGRA_RETIFICA_MESMO_BENEFICIO
        REGRA:REGRA_VALIDA_CNPJ
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCdBenIn/v_S_01_03_00"

    evtCdBenIn: ESocial.EvtCdBenIn = field(
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
    class EvtCdBenIn(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar beneficiario: Informações do beneficiário. CHAVE_GRUPO: {cpfBenef*}
        :ivar infoBenInicio: Informações do benefício - Início. CHAVE_GRUPO: {nrBeneficio*}
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
        beneficiario: ESocial.EvtCdBenIn.Beneficiario = field(
            metadata={
                "type": "Element",
            }
        )
        infoBenInicio: ESocial.EvtCdBenIn.InfoBenInicio = field(
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
        class Beneficiario(CommonMixin):
            """
            :ivar cpfBenef: Informar o CPF do beneficiário. Validação: Deve observar o que segue: a) Se
                {cadIni}(2410_infoBenInicio_cadIni) = [S], deve estar cadastrado no evento S-2400 com data de
                início igual à data de obrigatoriedade dos eventos não periódicos para o ente público no
                eSocial; b) Se {indSitBenef}(2410_infoBenInicio_indSitBenef) = [1], deve estar cadastrado no
                evento S-2400 com data de início igual ou anterior a
                {dtIniBeneficio}(2410_infoBenInicio_dtIniBeneficio) (ou a
                {dtPublic}(2410_infoBenInicio_dtPublic), caso este campo tenha sido informado); c) Se
                {indSitBenef}(2410_infoBenInicio_indSitBenef) = [2, 3], deve estar cadastrado no evento S-2400
                com data de início igual ou anterior a {dtTransf}(2410_infoBenInicio_sucessaoBenef_dtTransf) ou
                {dtAltCPF}(2410_infoBenInicio_mudancaCPF_dtAltCPF), respectivamente.
            :ivar matricula: Matrícula do servidor/militar constante no Sistema de Administração de Recursos
                Humanos do órgão cujo vínculo deu ensejo ao benefício. No caso de pensão por morte, informar a
                matrícula do instituidor da pensão. Validação: Informação obrigatória se
                {cadIni}(2410_infoBenInicio_cadIni) = [N] e
                {tpBeneficio}(2410_infoBenInicio_dadosBeneficio_tpBeneficio) pertencer ao grupo [01, 02, 03, 04,
                05, 06, 11] da Tabela 25. REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar cnpjOrigem: Preencher com o CNPJ do órgão público responsável pela matrícula do
                servidor/militar. Informação obrigatória se {cadIni}(2410_infoBenInicio_cadIni) = [N], desde que
                haja informação de matrícula. Validação: Preenchimento obrigatório se
                {cadIni}(2410_infoBenInicio_cadIni) = [N] e houver informação de {matricula}(./matricula),
                exceto se existir vínculo (evento S-2200) no órgão declarante para o beneficiário (indicado em
                {cpfBenef}(./cpfBenef) e {matricula}(./matricula)) ou, se
                {tpBeneficio}(2410_infoBenInicio_dadosBeneficio_tpBeneficio) pertencer ao grupo [06] da Tabela
                25, para o instituidor da pensão por morte (indicado em
                {cpfInst}(2410_infoBenInicio_dadosBeneficio_infoPenMorte_instPenMorte_cpfInst) e
                {matricula}(./matricula)). Se informado, deve ser um CNPJ válido, com 14 (catorze) algarismos.
            """

            cpfBenef: str = field(
                metadata={
                    "type": "Element",
                }
            )
            matricula: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            cnpjOrigem: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class InfoBenInicio(CommonMixin):
            """
            :ivar cadIni: Indicar se a data de início do benefício é anterior à obrigatoriedade dos eventos não
                periódicos para o ente público no eSocial.
            :ivar indSitBenef:
            :ivar nrBeneficio: Número do benefício. REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar dtIniBeneficio: Data de início do benefício. Validação: Deve observar o que segue: a) Se
                {cadIni}(./cadIni) = [S], deve ser anterior à data de início da obrigatoriedade dos eventos não
                periódicos para o ente público no eSocial; b) Se {cadIni}(./cadIni) = [N], deve ser igual ou
                posterior à data de início da obrigatoriedade dos eventos não periódicos para o ente público no
                eSocial e igual ou anterior à data atual.
            :ivar dtPublic: Informar a data de publicação da concessão do benefício, somente quando o ato
                concessório tiver vigência retroativa. Validação: Deve ser posterior a
                {dtIniBeneficio}(./dtIniBeneficio).
            :ivar dadosBeneficio: Dados relativos ao benefício.
            :ivar sucessaoBenef: Grupo de informações de transferência de benefício. CONDICAO_GRUPO: O (se
                {indSitBenef}(2410_infoBenInicio_indSitBenef) = [2]); N (nos demais casos)
            :ivar mudancaCPF: Informações de mudança de CPF do beneficiário. CONDICAO_GRUPO: O (se
                {indSitBenef}(2410_infoBenInicio_indSitBenef) = [3]); N (nos demais casos)
            :ivar infoBenTermino: Informações da cessação do benefício DESCRICAO_COMPLETA:Informações da
                cessação do benefício. Grupo preenchido exclusivamente caso seja necessário enviar evento de
                reativação de benefício cessado antes do início dos eventos não periódicos para o ente público
                no eSocial ou para informação de diferenças de proventos e pensões devidos sob a vigência dos
                eventos periódicos para o ente público no eSocial. CONDICAO_GRUPO: OC (se
                {cadIni}(2410_infoBenInicio_cadIni) = [S] ou {indSitBenef}(2410_infoBenInicio_indSitBenef) =
                [2]); N (nos demais casos)
            """

            cadIni: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indSitBenef: None | InfoBenInicioIndSitBenef = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            nrBeneficio: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtIniBeneficio: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtPublic: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            dadosBeneficio: ESocial.EvtCdBenIn.InfoBenInicio.DadosBeneficio = field(
                metadata={
                    "type": "Element",
                }
            )
            sucessaoBenef: None | ESocial.EvtCdBenIn.InfoBenInicio.SucessaoBenef = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            mudancaCPF: None | ESocial.EvtCdBenIn.InfoBenInicio.MudancaCpf = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoBenTermino: None | ESocial.EvtCdBenIn.InfoBenInicio.InfoBenTermino = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class DadosBeneficio(CommonMixin):
                """
                :ivar tpBeneficio: Tipo de benefício. Validação: Deve ser um código válido e existente na Tabela
                    25. Se {cadIni}(2410_infoBenInicio_cadIni) = [N], não é permitido utilizar código do grupo
                    [08] dessa tabela.
                :ivar tpPlanRP:
                :ivar dsc: Descrição do instrumento ou situação que originou o pagamento do benefício.
                    Validação: Preenchimento obrigatório se {tpBeneficio}(./tpBeneficio) = [0909, 1001, 1009].
                :ivar indDecJud: Informar se o benefício foi concedido por determinação judicial. Validação:
                    Preenchimento obrigatório se {cadIni}(2410_infoBenInicio_cadIni) = [N].
                :ivar infoPenMorte: Informações relativas à pensão por morte. CONDICAO_GRUPO: O (se
                    {tpBeneficio}(../tpBeneficio) pertencer ao grupo [06]); N (nos demais casos)
                :ivar infoHomolog: Informações relativas à homologação do benefício pelo Tribunal de Contas.
                    CONDICAO_GRUPO: OC Validação: Se o grupo não for informado e
                    {dtIniBeneficio}(2410_infoBenInicio_dtIniBeneficio) &gt;= [2025-11-24], retornar alerta.
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
                indDecJud: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoPenMorte: None | ESocial.EvtCdBenIn.InfoBenInicio.DadosBeneficio.InfoPenMorte = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoHomolog: None | ESocial.EvtCdBenIn.InfoBenInicio.DadosBeneficio.InfoHomolog = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoPenMorte(CommonMixin):
                    """
                    :ivar tpPenMorte:
                    :ivar instPenMorte: Informações do instituidor da pensão por morte. CONDICAO_GRUPO: O (se
                        {cadIni}(2410_infoBenInicio_cadIni) = [N]); F (se {cadIni}(2410_infoBenInicio_cadIni) =
                        [S])
                    """

                    tpPenMorte: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    instPenMorte: None | ESocial.EvtCdBenIn.InfoBenInicio.DadosBeneficio.InfoPenMorte.InstPenMorte = (
                        field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                    )

                    @dataclass(kw_only=True)
                    class InstPenMorte(CommonMixin):
                        """
                        :ivar cpfInst: Preencher com o CPF do instituidor da pensão por morte. Validação: Deve
                            ser um CPF válido e diferente do CPF do beneficiário.
                        :ivar dtInst: Data de óbito do instituidor da pensão por morte.
                        :ivar tpDepInst:
                        :ivar descrDepInst:
                        """

                        cpfInst: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        dtInst: XmlDate = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        tpDepInst: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        descrDepInst: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                @dataclass(kw_only=True)
                class InfoHomolog(CommonMixin):
                    """
                    :ivar sitHomolog:
                    :ivar dtHomolog: Informar a data da homologação do benefício pelo Tribunal de Contas
                        competente. Validação: Informação obrigatória e exclusiva se {sitHomolog}(./sitHomolog)
                        = [1].
                    """

                    sitHomolog: InfoHomologSitHomolog = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtHomolog: None | XmlDate = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

            @dataclass(kw_only=True)
            class SucessaoBenef(CommonMixin):
                """
                :ivar cnpjOrgaoAnt: Informar o CNPJ do órgão público anterior. Validação: Deve ser um CNPJ
                    válido e diferente da inscrição do declarante, considerando as particularidades aplicadas à
                    informação de CNPJ de órgão público em S-1000. Além disso, deve possuir 14 (catorze)
                    algarismos e ser diferente do CNPJ base do órgão público declarante (exceto se
                    {ideEmpregador/nrInsc}(2410_ideEmpregador_nrInsc) tiver 14 (catorze) algarismos) e dos
                    estabelecimentos informados através do evento S-1005.
                :ivar nrBeneficioAnt: Número do benefício no ente público anterior.
                :ivar dtTransf: Preencher com a data da transferência do benefício para o órgão público
                    declarante. Validação: Devem ser observadas as seguintes regras: a) Deve ser posterior à
                    data de início do benefício; b) Deve ser igual ou posterior à data de início da
                    obrigatoriedade dos eventos não periódicos para o ente público no eSocial e igual ou
                    anterior à data atual.
                :ivar observacao:
                """

                cnpjOrgaoAnt: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                nrBeneficioAnt: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtTransf: XmlDate = field(
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

            @dataclass(kw_only=True)
            class MudancaCpf(CommonMixin):
                """
                :ivar cpfAnt: Preencher com o número do CPF antigo do beneficiário.
                :ivar nrBeneficioAnt: Preencher com o número do benefício anterior.
                :ivar dtAltCPF: Data de alteração do CPF.
                :ivar observacao:
                """

                cpfAnt: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                nrBeneficioAnt: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtAltCPF: XmlDate = field(
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

            @dataclass(kw_only=True)
            class InfoBenTermino(CommonMixin):
                """
                :ivar dtTermBeneficio: Data de cessação do benefício. Validação: Devem ser observadas as
                    seguintes regras: a) Deve ser igual ou posterior à data de início do benefício; b) Se
                    {cadIni}(2410_infoBenInicio_cadIni) = [S], deve ser anterior à data de início da
                    obrigatoriedade dos eventos não periódicos para o ente público no eSocial; c) Se
                    {indSitBenef}(2410_infoBenInicio_indSitBenef) = [2], deve ser anterior a
                    {dtTransf}(2410_infoBenInicio_sucessaoBenef_dtTransf).
                :ivar mtvTermino:
                """

                dtTermBeneficio: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                mtvTermino: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{2}",
                    }
                )
