from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtAltContratual/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2206 - Alteração de Contrato de Trabalho/Relação Estatutária.

    :ivar evtAltContratual: Evento Alteração de Contrato de Trabalho/Relação Estatutária. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ADMISSAO_VALIDA_DURACAO_CONTRATO REGRA:REGRA_ALTERA_CATEG REGRA:REGRA_EMPREGADO_DOMESTICO
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXTEMP_DOMESTICO REGRA:REGRA_EXTEMP_REINTEGRACAO
        REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_RETIFICA_MESMO_VINCULO
        REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF REGRA:REGRA_VINCULO_ATIVO_NA_DTEVENTO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtAltContratual/v_S_01_03_00"

    evtAltContratual: ESocial.EvtAltContratual = field(
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
    class EvtAltContratual(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar altContratual: Alteração de dados contratuais. CHAVE_GRUPO: {dtAlteracao*}, {dtEf*}
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
        altContratual: ESocial.EvtAltContratual.AltContratual = field(
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
        class AltContratual(CommonMixin):
            """
            :ivar dtAlteracao:
            :ivar dtEf: Data dos efeitos remuneratórios da alteração contratual. Se a alteração foi fruto de
                lei, acordo coletivo, convenção coletiva ou sentença normativa, informar a data a partir da qual
                a alteração produz efeitos remuneratórios. Validação: Deve ser uma data válida, igual ou
                posterior à data de admissão.
            :ivar dscAlt:
            :ivar vinculo: Informações do vinculo. DESCRICAO_COMPLETA:Grupo de informações do vínculo
                trabalhista.
            """

            dtAlteracao: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtEf: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            dscAlt: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 150,
                    "pattern": r"[^\s]{1}[\S\s]*",
                },
            )
            vinculo: ESocial.EvtAltContratual.AltContratual.Vinculo = field(
                metadata={
                    "type": "Element",
                }
            )

            @dataclass(kw_only=True)
            class Vinculo(CommonMixin):
                """
                :ivar tpRegPrev:
                :ivar infoRegimeTrab: Informações do regime trabalhista. CONDICAO_GRUPO: N (se
                    {tpRegPrev}(2206_altContratual_vinculo_tpRegPrev) = [1, 3, 4] e
                    {tpRegTrab}(2200_vinculo_tpRegTrab) em S-2200 = [2]); O (nos demais casos)
                :ivar infoContrato: Informações do contrato de trabalho.
                """

                tpRegPrev: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                infoRegimeTrab: None | ESocial.EvtAltContratual.AltContratual.Vinculo.InfoRegimeTrab = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoContrato: ESocial.EvtAltContratual.AltContratual.Vinculo.InfoContrato = field(
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass(kw_only=True)
                class InfoRegimeTrab(CommonMixin):
                    """
                    :ivar infoCeletista: Informações de trabalhador celetista. CONDICAO_GRUPO: O (se
                        {tpRegTrab}(2200_vinculo_tpRegTrab) em S-2200 = [1]); N (nos demais casos)
                    :ivar infoEstatutario: Informações de trabalhador estatutário. CONDICAO_GRUPO: O (se
                        {tpRegPrev}(2206_altContratual_vinculo_tpRegPrev) = [2] e
                        {tpRegTrab}(2200_vinculo_tpRegTrab) em S-2200 = [2]); N (nos demais casos)
                    """

                    infoCeletista: (
                        None | ESocial.EvtAltContratual.AltContratual.Vinculo.InfoRegimeTrab.InfoCeletista
                    ) = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoEstatutario: (
                        None | ESocial.EvtAltContratual.AltContratual.Vinculo.InfoRegimeTrab.InfoEstatutario
                    ) = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoCeletista(CommonMixin):
                        """
                        :ivar tpRegJor:
                        :ivar natAtividade:
                        :ivar dtBase:
                        :ivar cnpjSindCategProf:
                        :ivar trabTemporario: Dados sobre trabalho temporário DESCRICAO_COMPLETA:Dados sobre
                            trabalho temporário. Preenchimento obrigatório no caso de prorrogação de contrato de
                            trabalhador temporário. CONDICAO_GRUPO: OC (se
                            {codCateg}(2206_altContratual_vinculo_infoContrato_codCateg) = [106]); N (nos demais
                            casos)
                        :ivar aprend: Informações relacionadas ao aprendiz. CONDICAO_GRUPO: O (se
                            {codCateg}(2206_altContratual_vinculo_infoContrato_codCateg) = [103] e se
                            {dtAlteracao}(2206_altContratual_dtAlteracao) &gt;= [2024-01-22]); OC (se
                            {codCateg}(2206_altContratual_vinculo_infoContrato_codCateg) = [103] e se
                            {dtAlteracao}(2206_altContratual_dtAlteracao) &lt; [2024-01-22]); N (nos demais
                            casos)
                        """

                        tpRegJor: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        natAtividade: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        dtBase: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        cnpjSindCategProf: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        trabTemporario: (
                            None
                            | ESocial.EvtAltContratual.AltContratual.Vinculo.InfoRegimeTrab.InfoCeletista.TrabTemporario
                        ) = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        aprend: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                        @dataclass(kw_only=True)
                        class TrabTemporario(CommonMixin):
                            """
                            :ivar justProrr: Descrever a justificativa para a prorrogação do contrato de
                                trabalho temporário.
                            """

                            justProrr: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

                    @dataclass(kw_only=True)
                    class InfoEstatutario(CommonMixin):
                        """
                        :ivar tpPlanRP:
                        :ivar indTetoRGPS: Informar se o servidor está sujeito ao teto do RGPS pela instituição
                            do regime de previdência complementar.
                        :ivar indAbonoPerm: Indicar se o servidor recebe abono permanência.
                        """

                        tpPlanRP: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        indTetoRGPS: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        indAbonoPerm: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                @dataclass(kw_only=True)
                class InfoContrato(CommonMixin):
                    """
                    :ivar nmCargo: Informar o nome do cargo. Validação: O preenchimento é obrigatório, exceto se
                        for relativo a servidor nomeado em cargo em comissão (no evento S-2200,
                        {tpRegTrab}(2200_vinculo_tpRegTrab) = [2] e
                        {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) = [2]).
                    :ivar CBOCargo:
                    :ivar nmFuncao: Informar o nome da função de confiança/cargo em comissão. Validação:
                        Preenchimento obrigatório se for relativo a servidor nomeado em cargo em comissão (no
                        evento S-2200, {tpRegTrab}(2200_vinculo_tpRegTrab) = [2] e
                        {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) = [2]).
                    :ivar CBOFuncao:
                    :ivar acumCargo: Informar se o cargo, emprego ou função pública é acumulável. Validação:
                        Preenchimento obrigatório se a natureza jurídica do declarante for igual a 1XX-X, 201-1
                        ou 203-8.
                    :ivar codCateg:
                    :ivar remuneracao: Informações da remuneração e periodicidade de pagamento. CONDICAO_GRUPO:
                        O (se {tpRegTrab}(2200_vinculo_tpRegTrab) em S-2200 = [1]); N (nos demais casos)
                    :ivar duracao: Duração do contrato de trabalho. CONDICAO_GRUPO: O (se
                        {tpRegTrab}(2200_vinculo_tpRegTrab) em S-2200 = [1]); N (nos demais casos)
                    :ivar localTrabalho: Informações do local de trabalho.
                    :ivar horContratual: Informações do horário contratual do trabalhador. CONDICAO_GRUPO: O (se
                        {tpRegJor}(../../infoRegimeTrab_infoCeletista_tpRegJor) = [1]); OC (nos demais casos)
                    :ivar alvaraJudicial: Dados do alvará judicial DESCRICAO_COMPLETA:Informações do alvará
                        judicial em caso de contratação de menores de 14 anos, em qualquer categoria, e de
                        maiores de 14 e menores de 16, em categoria diferente de "Aprendiz". CONDICAO_GRUPO: OC
                    :ivar observacoes: Observações do contrato de trabalho. CONDICAO_GRUPO: OC
                    :ivar treiCap: Treinamentos, capacitações, exercícios simulados e outras anotações.
                        DESCRICAO_COMPLETA:Treinamentos, capacitações, exercícios simulados, autorizações ou
                        outras anotações que devam ser anotadas no registro de empregados e/ou na CTPS, por
                        determinação de Norma Regulamentadora - NR. CHAVE_GRUPO: {codTreiCap} CONDICAO_GRUPO: OC
                    """

                    nmCargo: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    CBOCargo: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    nmFuncao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    CBOFuncao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    acumCargo: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    codCateg: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    remuneracao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    duracao: None | ESocial.EvtAltContratual.AltContratual.Vinculo.InfoContrato.Duracao = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    localTrabalho: ESocial.EvtAltContratual.AltContratual.Vinculo.InfoContrato.LocalTrabalho = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    horContratual: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    alvaraJudicial: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    observacoes: list[ESocial.EvtAltContratual.AltContratual.Vinculo.InfoContrato.Observacoes] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    treiCap: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class Duracao(CommonMixin):
                        """
                        :ivar tpContr: Tipo de contrato de trabalho. Validação: Se {codCateg}(../codCateg) =
                            [103] e {dtAlteracao}(2206_altContratual_dtAlteracao) &gt;= [2024-04-22], deve ser
                            informado [2].
                        :ivar dtTerm: Data do término do contrato por prazo determinado. Validação: O
                            preenchimento é obrigatório se {tpContr}(./tpContr) = [2]. Não informar se
                            {tpContr}(./tpContr) = [1]. Se preenchido, deve ser igual ou posterior à data de
                            admissão (no caso de transferência ou mudança de CPF, igual ou posterior a
                            {sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf),
                            {transfDom/dtTransf}(2200_vinculo_transfDom_dtTransf) ou
                            {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF) do evento S-2200, conforme o caso).
                            Retornar alerta caso a data informada seja anterior a
                            {dtAlteracao}(2206_altContratual_dtAlteracao).
                        :ivar objDet:
                        """

                        tpContr: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        dtTerm: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        objDet: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                    @dataclass(kw_only=True)
                    class LocalTrabalho(CommonMixin):
                        """
                        :ivar localTrabGeral: Estabelecimento onde o trabalhador exercerá suas atividades
                            DESCRICAO_COMPLETA:Estabelecimento (CNPJ, CNO, CAEPF) onde o trabalhador (exceto
                            doméstico) exercerá suas atividades. Caso o trabalhador exerça suas atividades em
                            instalações de terceiros, este campo deve ser preenchido com o estabelecimento do
                            próprio empregador ao qual o trabalhador esteja vinculado. CONDICAO_GRUPO: O (se
                            {codCateg}(2206_altContratual_vinculo_infoContrato_codCateg) for diferente de
                            [104]); N (nos demais casos)
                        :ivar localTempDom: Endereço de trabalho do trabalhador doméstico e trabalhador
                            temporário DESCRICAO_COMPLETA:Grupo preenchido exclusivamente em caso de trabalhador
                            doméstico e trabalhador temporário, indicando o endereço onde o trabalhador exerce
                            suas atividades. CONDICAO_GRUPO: O (se
                            {codCateg}(2206_altContratual_vinculo_infoContrato_codCateg) = [104, 106]); N (nos
                            demais casos)
                        """

                        localTrabGeral: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        localTempDom: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                    @dataclass(kw_only=True)
                    class Observacoes(CommonMixin):
                        """
                        :ivar observacao: Observação relacionada ao contrato de trabalho.
                        """

                        observacao: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
