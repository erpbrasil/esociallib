from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtAnotJud/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-8200 - Anotação Judicial do Vínculo.

    :ivar evtAnotJud: Evento Anotação Judicial do Vínculo. CHAVE_GRUPO: {Id} REGRA:REGRA_ADMISSAO_VALIDA_DT_ADM
        REGRA:REGRA_ADMISSAO_VALIDA_DURACAO_CONTRATO REGRA:REGRA_BLOQUEIA_USO_CPF_EMPREGADOR
        REGRA:REGRA_COMPATIBILIDADE_CATEGORIA_CLASSTRIB REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_RETIFICA_MESMO_VINCULO
        REGRA:REGRA_VALIDA_MATRICULA REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtAnotJud/v_S_01_03_00"

    evtAnotJud: ESocial.EvtAnotJud = field(
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
    class EvtAnotJud(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoProcesso: Informações do processo judicial.
        :ivar infoAnotJud: Informações da anotação judicial do vínculo. CHAVE_GRUPO: {cpfTrab*}, {matricula*}
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
        infoProcesso: ESocial.EvtAnotJud.InfoProcesso = field(
            metadata={
                "type": "Element",
            }
        )
        infoAnotJud: ESocial.EvtAnotJud.InfoAnotJud = field(
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
        class InfoProcesso(CommonMixin):
            """
            :ivar nrProcTrab: Número que identifica o processo judicial onde a anotação do vínculo foi
                determinada. Validação: Deve ser um processo judicial válido, com 20 (vinte) algarismos.
            :ivar dtSent: Informar a data da decisão judicial.
            :ivar ufVara: Preencher com a sigla da Unidade da Federação onde está localizada a Vara em que o
                processo tramitou.
            :ivar codMunic:
            :ivar idVara:
            """

            nrProcTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtSent: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            ufVara: str = field(
                metadata={
                    "type": "Element",
                }
            )
            codMunic: str = field(
                metadata={
                    "type": "Element",
                }
            )
            idVara: str = field(
                metadata={
                    "type": "Element",
                    "pattern": r"\d{1,4}",
                }
            )

        @dataclass(kw_only=True)
        class InfoAnotJud(CommonMixin):
            """
            :ivar cpfTrab:
            :ivar nmTrab:
            :ivar dtNascto: Preencher com a data de nascimento.
            :ivar dtAdm: Preencher com a data de admissão do trabalhador. Validação: Deve ser posterior à data
                de nascimento do trabalhador.
            :ivar matricula: Matrícula atribuída ao trabalhador. Validação: O valor informado deve conter a
                expressão 'eSocial-JUD-' nas 12 (doze) primeiras posições. REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar codCateg: Preencher com o código da categoria do trabalhador. Validação: Deve ser um código de
                categoria referente a "Empregado" ([1XX]).
            :ivar natAtividade: Natureza da atividade. Validação: Se {codCateg}(./codCateg) = [104], deve ser
                preenchido com [1]. Se {codCateg}(./codCateg) = [102], deve ser preenchido com [2].
            :ivar tpContr:
            :ivar dtTerm: Data do término do contrato por prazo determinado. Validação: O preenchimento é
                obrigatório se {tpContr}(./tpContr) = [2]. Não informar se {tpContr}(./tpContr) = [1]. Deve ser
                igual ou posterior à data de admissão.
            :ivar tpInscTrab: Preencher com o código correspondente ao tipo de inscrição do estabelecimento
                relativo ao local de trabalho. Validação: Não preencher se {codCateg}(./codCateg) = [104].
            :ivar localTrabalho: Informar o número de inscrição do estabelecimento relativo ao local de
                trabalho. Validação: Preenchimento obrigatório e exclusivo se {tpInscTrab}(./tpInscTrab) for
                informado. Deve ser um identificador válido, constante das bases da RFB, conforme indicado em
                {tpInscTrab}(./tpInscTrab).
            :ivar tpRegTrab:
            :ivar tpRegPrev: Tipo de regime previdenciário. Validação: Se {}(./codCateg) = [104], deve ser
                preenchido com [1]. Se {}(./codCateg) = [101, 102, 103, 105, 106, 107, 108, 111], não pode ser
                preenchido com [2].
            :ivar cargo: Informações do cargo. CHAVE_GRUPO: {dtCargo}
            :ivar remuneracao: Informações da remuneração e periodicidade de pagamento. CHAVE_GRUPO: {dtRemun}
            :ivar incorporacao: Informação do(s) vínculo(s)/contrato(s) já declarado(s) no eSocial e
                incorporado(s) ao vínculo ou sucedido(s) pelo vínculo reconhecido judicialmente. CHAVE_GRUPO:
                {tpInsc}, {nrInsc}, {matIncorp} CONDICAO_GRUPO: OC
            :ivar afastamento: Informações de afastamento do trabalhador. CONDICAO_GRUPO: N (se grupo
                {desligamento}(../desligamento) estiver preenchido); O (nos demais casos)
            :ivar desligamento: Informações de desligamento do trabalhador. CONDICAO_GRUPO: N (se grupo
                {afastamento}(../afastamento) estiver preenchido); O (nos demais casos)
            """

            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nmTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtNascto: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtAdm: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            matricula: str = field(
                metadata={
                    "type": "Element",
                }
            )
            codCateg: str = field(
                metadata={
                    "type": "Element",
                }
            )
            natAtividade: str = field(
                metadata={
                    "type": "Element",
                }
            )
            tpContr: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtTerm: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            tpInscTrab: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            localTrabalho: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            tpRegTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            tpRegPrev: str = field(
                metadata={
                    "type": "Element",
                }
            )
            cargo: list[ESocial.EvtAnotJud.InfoAnotJud.Cargo] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )
            remuneracao: list[ESocial.EvtAnotJud.InfoAnotJud.Remuneracao] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )
            incorporacao: list[ESocial.EvtAnotJud.InfoAnotJud.Incorporacao] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 9,
                },
            )
            afastamento: None | ESocial.EvtAnotJud.InfoAnotJud.Afastamento = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            desligamento: None | ESocial.EvtAnotJud.InfoAnotJud.Desligamento = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Cargo(CommonMixin):
                """
                :ivar dtCargo: Data a partir da qual as informações do cargo estão vigentes. Validação: Deve ser
                    igual ou posterior à data de admissão e igual ou anterior à data de desligamento, se
                    informada.
                :ivar CBOCargo: Informar a Classificação Brasileira de Ocupações - CBO relativa ao cargo.
                    Validação: Deve ser um código válido e existente na tabela de CBO, com 6 (seis) posições.
                """

                dtCargo: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                CBOCargo: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Remuneracao(CommonMixin):
                """
                :ivar dtRemun: Data a partir da qual as informações de remuneração e periodicidade de pagamento
                    estão vigentes. Validação: Deve ser igual ou posterior à data de admissão e igual ou
                    anterior à data de desligamento, se informada.
                :ivar vrSalFx: Salário base do trabalhador, correspondente à parte fixa da remuneração em
                    {dtRemun}(./dtRemun). Validação: Se {undSalFixo}(./undSalFixo) for igual a [7], preencher
                    com 0 (zero).
                :ivar undSalFixo:
                :ivar dscSalVar: Descrição do salário por tarefa ou variável e como este é calculado. Ex.:
                    Comissões pagas no percentual de 10% sobre as vendas. Validação: Preenchimento obrigatório
                    se {undSalFixo}(./undSalFixo) for igual a [6, 7].
                """

                dtRemun: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                vrSalFx: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                undSalFixo: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dscSalVar: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Incorporacao(CommonMixin):
                """
                :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.
                    Validação: Informação obrigatória e exclusiva se a data de transmissão do evento for igual
                    ou posterior a [2024-04-22].
                :ivar nrInsc: Informar o número de inscrição do empregador no qual consta a matrícula
                    incorporada ou sucedida, de acordo com o tipo de inscrição indicado no campo
                    {incorporacao/tpInsc}(./tpInsc). Validação: Preenchimento obrigatório e exclusivo se o campo
                    {incorporacao/tpInsc}(./tpInsc) for informado.
                :ivar matIncorp: Informar a matrícula incorporada (matrícula cujo vínculo/contrato passou a
                    integrar o vínculo reconhecido judicialmente) ou a matrícula no empregador anterior.
                    Validação: Deve corresponder a uma matrícula informada pelo empregador no evento S-2190,
                    S-2200 ou S-2300, pertencente ao trabalhador preenchido em {cpfTrab}(../cpfTrab), no
                    empregador informado em {incorporacao/nrInsc}(./nrInsc).
                """

                tpInsc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                nrInsc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                matIncorp: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Afastamento(CommonMixin):
                """
                :ivar dtIniAfast: Data de início do afastamento. Validação: Deve ser igual ou posterior à data
                    de admissão do trabalhador. Não pode ser posterior à data atual.
                :ivar codMotAfast: Preencher com o código do motivo de afastamento temporário. Validação: Deve
                    ser um código válido e existente na Tabela 18, bem como compatível com o código de categoria
                    do trabalhador, conforme Tabela 18. Somente podem ser informados os códigos [01, 03, 06, 11,
                    12, 17, 18, 19, 20, 22, 24, 29, 35].
                """

                dtIniAfast: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                codMotAfast: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Desligamento(CommonMixin):
                """
                :ivar mtvDeslig:
                :ivar dtDeslig: Preencher com a data de desligamento do vínculo (último dia trabalhado).
                    Validação: Deve ser igual ou posterior à data de admissão do trabalhador e igual ou
                    posterior a [2019-09-24]. Não pode ser posterior à data atual.
                :ivar dtProjFimAPI:
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
