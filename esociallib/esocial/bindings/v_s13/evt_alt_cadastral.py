from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtAltCadastral/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2205 - Alteração de Dados Cadastrais do Trabalhador.

    :ivar evtAltCadastral: Evento Alteração de Dados Cadastrais do Trabalhador. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXISTE_TRABALHADOR REGRA:REGRA_EXTEMP_DOMESTICO
        REGRA:REGRA_EXTEMP_REINTEGRACAO REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtAltCadastral/v_S_01_03_00"

    evtAltCadastral: ESocial.EvtAltCadastral = field(
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
    class EvtAltCadastral(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideTrabalhador: Identificação do trabalhador. CHAVE_GRUPO: {cpfTrab*}
        :ivar alteracao: Alteração de dados cadastrais do trabalhador. CHAVE_GRUPO: {dtAlteracao*}
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
        ideTrabalhador: ESocial.EvtAltCadastral.IdeTrabalhador = field(
            metadata={
                "type": "Element",
            }
        )
        alteracao: ESocial.EvtAltCadastral.Alteracao = field(
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
        class IdeTrabalhador(CommonMixin):
            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class Alteracao(CommonMixin):
            """
            :ivar dtAlteracao:
            :ivar dadosTrabalhador: Informações pessoais do trabalhador.
            """

            dtAlteracao: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dadosTrabalhador: ESocial.EvtAltCadastral.Alteracao.DadosTrabalhador = field(
                metadata={
                    "type": "Element",
                }
            )

            @dataclass(kw_only=True)
            class DadosTrabalhador(CommonMixin):
                """
                :ivar nmTrab:
                :ivar sexo:
                :ivar racaCor: Etnia e raça do trabalhador, conforme sua autoclassificação (art. 39, § 8º, da
                    Lei 12.288/2010). Validação: Se {dtAlteracao}(../dtAlteracao) for igual ou posterior a
                    [2024-04-22], não pode ser informado o valor [6].
                :ivar estCiv:
                :ivar grauInstr:
                :ivar nmSoc:
                :ivar paisNac:
                :ivar endereco: Endereço do trabalhador DESCRICAO_COMPLETA:Grupo de informações do endereço do
                    trabalhador. CONDICAO_GRUPO: O (se houver trabalhador ativo no RET com {tpRegPrev} diferente
                    de [4] ou com código de categoria diferente de [308]; N (nos demais casos)
                :ivar trabImig: Informações do trabalhador imigrante. CONDICAO_GRUPO: OC (se
                    {paisNac}(2205_alteracao_dadosTrabalhador_paisNac) for diferente de [105]); N (nos demais
                    casos)
                :ivar infoDeficiencia: Pessoa com deficiência. CONDICAO_GRUPO: OC (se houver trabalhador ativo
                    no RET com {tpRegPrev} diferente de [4] ou com código de categoria diferente de [308]; N
                    (nos demais casos)
                :ivar dependente: Informações dos dependentes. CHAVE_GRUPO: {tpDep}, {nmDep}, {dtNascto}
                    CONDICAO_GRUPO: OC
                :ivar contato: Informações de contato. CONDICAO_GRUPO: OC (se houver trabalhador ativo no RET
                    com {tpRegPrev} diferente de [4] ou com código de categoria diferente de [308]; N (nos
                    demais casos)
                """

                nmTrab: str = field(
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
                grauInstr: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                nmSoc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                paisNac: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                endereco: None | ESocial.EvtAltCadastral.Alteracao.DadosTrabalhador.Endereco = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                trabImig: None | ESocial.EvtAltCadastral.Alteracao.DadosTrabalhador.TrabImig = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoDeficiencia: None | ESocial.EvtAltCadastral.Alteracao.DadosTrabalhador.InfoDeficiencia = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                dependente: list[ESocial.EvtAltCadastral.Alteracao.DadosTrabalhador.Dependente] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                contato: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
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
                class TrabImig(CommonMixin):
                    """
                    :ivar tmpResid: Tempo de residência do trabalhador imigrante. Validação: Preenchimento
                        obrigatório quando houver trabalhador com
                        ({dtAdm}(2200_vinculo_infoRegimeTrab_infoCeletista_dtAdm) ou
                        {dtExercicio}(2200_vinculo_infoRegimeTrab_infoEstatutario_dtExercicio) ou
                        {dtInicio}(2300_infoTSVInicio_dtInicio)) no Registro de Eventos Trabalhistas - RET &gt;=
                        [2021-07-19].
                    :ivar condIng:
                    """

                    tmpResid: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    condIng: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoDeficiencia(CommonMixin):
                    """
                    :ivar defFisica:
                    :ivar defVisual:
                    :ivar defAuditiva:
                    :ivar defMental:
                    :ivar defIntelectual:
                    :ivar reabReadap:
                    :ivar infoCota: Informar se o trabalhador deve ser contabilizado no preenchimento de cota de
                        pessoas com deficiência habilitadas ou de beneficiários reabilitados. Validação:
                        Preenchimento obrigatório e exclusivo quando houver trabalhador cadastrado no evento
                        S-2200 com {tpRegTrab}(2200_vinculo_tpRegTrab) = [1] e ativo em
                        {dtAlteracao}(2205_alteracao_dtAlteracao). Somente pode ser informado [S] se pelo menos
                        um dos campos a seguir estiver preenchido com [S]: {defFisica}(./defFisica),
                        {defVisual}(./defVisual), {defAuditiva}(./defAuditiva), {defMental}(./defMental),
                        {defIntelectual}(./defIntelectual) e {reabReadap}(./reabReadap). Esta validação não deve
                        ser realizada quando se tratar de evento enviado em versão do leiaute anterior a S-1.0.
                    :ivar observacao:
                    """

                    defFisica: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    defVisual: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    defAuditiva: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    defMental: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    defIntelectual: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    reabReadap: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoCota: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    observacao: None | str = field(
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
                    :ivar sexoDep: Sexo do dependente. Validação: Preenchimento obrigatório e exclusivo quando
                        houver trabalhador cadastrado no evento S-2200, ativo em
                        {dtAlteracao}(2205_alteracao_dtAlteracao) e com {tpRegPrev} = [2] no RET. Esta validação
                        não deve ser realizada quando se tratar de recepção de evento extemporâneo.
                    :ivar depIRRF:
                    :ivar depSF:
                    :ivar incTrab: Informar se o dependente tem incapacidade física ou mental para o trabalho.
                        Validação: Preenchimento obrigatório se o trabalhador estiver cadastrado no evento
                        S-2200, ativo em {dtAlteracao}(2205_alteracao_dtAlteracao) e com {tpRegPrev} diferente
                        de [4] no RET, ou cadastrado no evento S-2300 e ativo em
                        {dtAlteracao}(2205_alteracao_dtAlteracao). Não informar nos demais casos.
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
                    depSF: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    incTrab: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    descrDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
