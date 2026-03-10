from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00"


@dataclass(kw_only=True)
class TDadosLotacao(CommonMixin):
    """
    Detalhamento das informações da lotação.

    :ivar tpLotacao:
    :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05. Validação: O
        campo não deve ser preenchido se {tpLotacao}(./tpLotacao) for igual a [01, 10, 21, 24, 90, 91, 92]. Nos
        demais casos, observar conteúdo exigido para o campo {dadosLotacao/nrInsc}(./nrInsc), conforme Tabela
        10.
    :ivar nrInsc: Preencher com o número de inscrição (CNPJ, CPF, CNO) ao qual pertence a lotação tributária.
        Validação: a) Deve ser preenchido de acordo com o conteúdo exigido, conforme especificado no campo
        {dadosLotacao/tpInsc}(./tpInsc) e na Tabela 10; b) Deve ser um identificador válido, constante das bases
        da RFB.
    :ivar fpasLotacao: Informações de FPAS e Terceiros relativos à lotação tributária.
    :ivar infoEmprParcial: Informação complementar de obra de construção civil DESCRICAO_COMPLETA:Informação
        complementar que apresenta identificação do contratante de obra de construção civil sob regime de
        empreitada parcial ou subempreitada. CONDICAO_GRUPO: O (se
        {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) = [02]); N (nos demais casos)
    :ivar dadosOpPort: Informações do operador portuário. CONDICAO_GRUPO: O (se
        {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) = [08]); N (nos demais casos)
    """

    class Meta:
        name = "T_dadosLotacao"

    tpLotacao: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        }
    )
    tpInsc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        },
    )
    nrInsc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        },
    )
    fpasLotacao: TDadosLotacao.FpasLotacao = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        }
    )
    infoEmprParcial: None | TDadosLotacao.InfoEmprParcial = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        },
    )
    dadosOpPort: None | TDadosLotacao.DadosOpPort = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        },
    )

    @dataclass(kw_only=True)
    class FpasLotacao(CommonMixin):
        """
        :ivar fpas:
        :ivar codTercs: Preencher com o código de Terceiros, já considerando a existência de eventuais convênios
            para recolhimento direto. Ex.: Se o contribuinte está enquadrado com FPAS [507], cujo código cheio
            de Terceiros é [0079], se possuir convênio com SENAI deve informar o código [0075]. Validação: Se a
            classificação tributária em S-1000 for igual a [01, 02, 03, 04], informar [0000]. Nos demais casos,
            o código de Terceiros informado deve ser compatível com o código de FPAS informado, conforme Tabela
            04.
        :ivar codTercsSusp: Informar o código combinado dos Terceiros para os quais o recolhimento está suspenso
            em virtude de processos judiciais. Ex.: Se o contribuinte possui decisões de processos para
            suspensão de recolhimentos ao SESI (0008) e ao SEBRAE (0064), deve informar o código combinado das
            duas entidades, ou seja, [0072]. Validação: Deve ser um código consistente com a Tabela 04. Deve
            haver pelo menos um processo em
            {procJudTerceiro}(1020_infoLotacao_inclusao_dadosLotacao_fpasLotacao_infoProcJudTerceiros_procJudTerceiro)
            para cada código de Terceiro cujo recolhimento esteja suspenso.
        :ivar infoProcJudTerceiros: Informações de processos judiciais relativos às contribuições destinadas a
            Outras Entidades DESCRICAO_COMPLETA:Informações sobre a existência de processos judiciais, com
            sentença/decisão favorável ao contribuinte, relativos às contribuições destinadas a Outras Entidades
            e Fundos. CONDICAO_GRUPO: O (se
            {codTercsSusp}(1020_infoLotacao_inclusao_dadosLotacao_fpasLotacao_codTercsSusp) for preenchido); N
            (nos demais casos)
        """

        fpas: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            }
        )
        codTercs: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            }
        )
        codTercsSusp: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            },
        )
        infoProcJudTerceiros: None | TDadosLotacao.FpasLotacao.InfoProcJudTerceiros = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            },
        )

        @dataclass(kw_only=True)
        class InfoProcJudTerceiros(CommonMixin):
            """
            :ivar procJudTerceiro: Identificação do processo judicial. CHAVE_GRUPO: {codTerc}, {nrProcJud}
            """

            procJudTerceiro: list[TDadosLotacao.FpasLotacao.InfoProcJudTerceiros.ProcJudTerceiro] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class ProcJudTerceiro(CommonMixin):
                """
                :ivar codTerc: Informar o código de Terceiro. Validação: Deve ser um código de Terceiro válido e
                    compatível com o FPAS/Terceiros informado no grupo superior, conforme Tabela 04.
                :ivar nrProcJud:
                :ivar codSusp:
                """

                codTerc: str = field(
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
                    }
                )
                nrProcJud: str = field(
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
                    }
                )
                codSusp: str = field(
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
                    }
                )

    @dataclass(kw_only=True)
    class InfoEmprParcial(CommonMixin):
        """
        :ivar tpInscContrat: Tipo de inscrição do contratante.
        :ivar nrInscContrat: Número de inscrição (CNPJ/CPF) do contratante. Validação: Deve ser um número de
            CNPJ ou CPF válido, conforme definido em {tpInscContrat}(./tpInscContrat).
        :ivar tpInscProp: Tipo de inscrição do proprietário do CNO. Validação: Preenchimento obrigatório e
            exclusivo quando o proprietário não for encontrado no CNO.
        :ivar nrInscProp: Preencher com o número de inscrição (CNPJ/CPF) do proprietário do CNO. Validação:
            Preenchimento obrigatório e exclusivo se {tpInscProp}(./tpInscProp) for informado. Deve ser um
            número de CNPJ ou CPF válido, conforme indicado em {tpInscProp}(./tpInscProp).
        """

        tpInscContrat: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            }
        )
        nrInscContrat: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            }
        )
        tpInscProp: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            },
        )
        nrInscProp: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            },
        )

    @dataclass(kw_only=True)
    class DadosOpPort(CommonMixin):
        """
        :ivar aliqRat: Preencher com a alíquota definida na legislação vigente para a atividade (CNAE)
            preponderante.
        :ivar fap: Fator Acidentário de Prevenção - FAP. Validação: Deve ser um número maior ou igual a 0,5000 e
            menor ou igual a 2,0000, de acordo com o estabelecido pelo órgão governamental competente.
        """

        aliqRat: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            }
        )
        fap: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
            }
        )


@dataclass(kw_only=True)
class TIdeLotacao(CommonMixin):
    """
    Identificação da lotação e validade das informações DESCRICAO_COMPLETA:Identificação da lotação e período de
    validade das informações.

    CHAVE_GRUPO: {codLotacao*}, {iniValid*}, {fimValid*}.

    :ivar codLotacao: Informar o código atribuído pelo empregador para a lotação tributária. Validação: O código
        atribuído não pode conter a expressão 'eSocial' nas 7 primeiras posições. REGRA:REGRA_CARACTERE_ESPECIAL
    :ivar iniValid:
    :ivar fimValid:
    """

    class Meta:
        name = "T_ideLotacao"

    codLotacao: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        }
    )
    iniValid: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        }
    )
    fimValid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00",
        },
    )


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1020 - Tabela de Lotações Tributárias.

    :ivar evtTabLotacao: Evento Tabela de Lotações Tributárias. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_TABGERAL_ALTERACAO_PERIODO_CONFLITANTE REGRA:REGRA_TABGERAL_EXISTE_REGISTRO_ALTERADO
        REGRA:REGRA_TABGERAL_EXISTE_REGISTRO_EXCLUIDO REGRA:REGRA_TABGERAL_INCLUSAO_PERIODO_CONFLITANTE
        REGRA:REGRA_TABLOTACAO_VALIDA_FPASTERCEIROS REGRA:REGRA_TAB_PERMITE_EXCLUSAO
        REGRA:REGRA_VALIDA_DT_FUTURA
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTabLotacao/v_S_01_03_00"

    evtTabLotacao: ESocial.EvtTabLotacao = field(
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
    class EvtTabLotacao(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoLotacao: Informações da lotação DESCRICAO_COMPLETA:Identificação da operação (inclusão,
            alteração ou exclusão) e das informações da lotação.
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
        infoLotacao: ESocial.EvtTabLotacao.InfoLotacao = field(
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
        class InfoLotacao(CommonMixin):
            """
            :ivar inclusao: Inclusão de novas informações. CONDICAO_GRUPO: OC
            :ivar alteracao: Alteração das informações. CONDICAO_GRUPO: OC
            :ivar exclusao: Exclusão das informações. CONDICAO_GRUPO: OC
            """

            inclusao: None | ESocial.EvtTabLotacao.InfoLotacao.Inclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            alteracao: None | ESocial.EvtTabLotacao.InfoLotacao.Alteracao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            exclusao: None | ESocial.EvtTabLotacao.InfoLotacao.Exclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Inclusao(CommonMixin):
                ideLotacao: TIdeLotacao = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dadosLotacao: TDadosLotacao = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Alteracao(CommonMixin):
                ideLotacao: TIdeLotacao = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dadosLotacao: TDadosLotacao = field(
                    metadata={
                        "type": "Element",
                    }
                )
                novaValidade: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Exclusao(CommonMixin):
                ideLotacao: TIdeLotacao = field(
                    metadata={
                        "type": "Element",
                    }
                )
