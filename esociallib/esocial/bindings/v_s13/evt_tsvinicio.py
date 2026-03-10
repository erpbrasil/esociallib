from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTSVInicio/v_S_01_03_00"


class InfoTsvinicioCadIni(Enum):
    """
    Indicar se o evento se refere a cadastramento inicial (o ingresso do trabalhador no empregador declarante é
    anterior à data de início da obrigatoriedade de envio de seus eventos não periódicos) ou se refere a início de
    TSVE (o ingresso do trabalhador no empregador declarante é igual ou posterior à data de início da
    obrigatoriedade de envio de seus eventos não periódicos).

    :cvar S: Sim (Cadastramento Inicial)
    :cvar N: Não (Início de TSVE)
    """

    S = "S"
    N = "N"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início.

    :ivar evtTSVInicio: Evento TSVE - Início DESCRICAO_COMPLETA:Evento Trabalhador Sem Vínculo de
        Emprego/Estatutário - Início. CHAVE_GRUPO: {Id} REGRA:REGRA_COMPATIBILIDADE_CATEGORIA_CLASSTRIB
        REGRA:REGRA_COMPATIB_CATEG_EVENTO REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EVETRAB_VALIDA_OPCAO_FGTS REGRA:REGRA_EXCLUSAO_ADMISSAO_TSVE_INICIO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_MUDANCA_CPF REGRA:REGRA_REGISTRO_PRELIMINAR REGRA:REGRA_RETIFICA_MESMO_VINCULO
        REGRA:REGRA_TSV_VERIFICA_DUPLICIDADE REGRA:REGRA_VALIDA_EMPREGADOR REGRA:REGRA_VALIDA_MATRICULA
        REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTSVInicio/v_S_01_03_00"

    evtTSVInicio: ESocial.EvtTsvinicio = field(
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
    class EvtTsvinicio(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar trabalhador: Grupo de informações do trabalhador. CHAVE_GRUPO: {cpfTrab*}
        :ivar infoTSVInicio: TSVE - Início DESCRICAO_COMPLETA:Trabalhador Sem Vínculo de Emprego/Estatutário -
            TSVE - Início. CHAVE_GRUPO: {matricula*}, {codCateg*}, {dtInicio*}
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
        trabalhador: ESocial.EvtTsvinicio.Trabalhador = field(
            metadata={
                "type": "Element",
            }
        )
        infoTSVInicio: ESocial.EvtTsvinicio.InfoTsvinicio = field(
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
        class Trabalhador(CommonMixin):
            """
            :ivar cpfTrab:
            :ivar nmTrab:
            :ivar sexo:
            :ivar racaCor: Etnia e raça do trabalhador, conforme sua autoclassificação (art. 39, § 8º, da Lei
                12.288/2010). Validação: Se {dtInicio}(2300_infoTSVInicio_dtInicio) for igual ou posterior a
                [2024-04-22], não pode ser informado o valor [6].
            :ivar estCiv:
            :ivar grauInstr:
            :ivar nmSoc:
            :ivar nascimento:
            :ivar endereco: Endereço do trabalhador DESCRICAO_COMPLETA:Grupo de informações do endereço do
                trabalhador. CONDICAO_GRUPO: N (se {codCateg}(2300_infoTSVInicio_codCateg) = [308]); O (nos
                demais casos)
            :ivar trabImig: Informações do trabalhador imigrante. CONDICAO_GRUPO: OC (se
                {paisNac}(2300_trabalhador_nascimento_paisNac) for diferente de [105]); N (nos demais casos)
            :ivar infoDeficiencia: Pessoa com deficiência. CONDICAO_GRUPO: N (se
                {codCateg}(2300_infoTSVInicio_codCateg) = [308]); OC (nos demais casos)
            :ivar dependente: Informações dos dependentes. CHAVE_GRUPO: {tpDep}, {nmDep}, {dtNascto}
                CONDICAO_GRUPO: OC
            :ivar contato: Informações de contato. CONDICAO_GRUPO: N (se {codCateg}(2300_infoTSVInicio_codCateg)
                = [308]); OC (nos demais casos)
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
            nascimento: str = field(
                metadata={
                    "type": "Element",
                }
            )
            endereco: None | ESocial.EvtTsvinicio.Trabalhador.Endereco = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            trabImig: None | ESocial.EvtTsvinicio.Trabalhador.TrabImig = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoDeficiencia: None | ESocial.EvtTsvinicio.Trabalhador.InfoDeficiencia = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            dependente: list[ESocial.EvtTsvinicio.Trabalhador.Dependente] = field(
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
                    obrigatório se {dtInicio}(2300_infoTSVInicio_dtInicio) &gt;= [2021-07-19].
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
                observacao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Dependente(CommonMixin):
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
                incTrab: str = field(
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

        @dataclass(kw_only=True)
        class InfoTsvinicio(CommonMixin):
            """
            :ivar cadIni:
            :ivar matricula: Matrícula atribuída ao trabalhador pela empresa. Validação: Preenchimento
                obrigatório se {indRetif}(2300_ideEvento_indRetif) = [1]. No caso de retificação
                ({indRetif}(2300_ideEvento_indRetif) = [2]), a matrícula deve ser preenchida caso tenha sido
                informada no evento original. O valor informado não pode conter a expressão 'eSocial' nas 7
                (sete) primeiras posições. REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar codCateg:
            :ivar dtInicio: Data de início, que pode ser: a) Para o cooperado, a data de ingresso na
                cooperativa; b) Para o diretor não empregado, a data de posse no cargo; c) Para o dirigente
                sindical, a data de início do mandato no sindicato; d) Para o estagiário, a data de início do
                estágio; e) Para o trabalhador avulso, a data de ingresso no Órgão Gestor de Mão de Obra - OGMO
                ou no sindicato; f) Para o servidor público exercente de cargo eletivo, a data de início do
                mandato; g) Para os demais trabalhadores, a data de início das atividades. Validação: Devem ser
                observadas as seguintes regras: a) Deve ser posterior à data de nascimento do trabalhador, não
                pode ser posterior a 30 (trinta) dias da data atual e deve ser igual ou anterior ao ano do
                óbito, se existente; b) Se {cadIni}(./cadIni) = [S], deve ser anterior à data de início da
                obrigatoriedade dos eventos não periódicos para o empregador no eSocial; c) Se
                {cadIni}(./cadIni) = [N], deve ser igual ou posterior à data de início da obrigatoriedade dos
                eventos não periódicos para o empregador no eSocial.
            :ivar nrProcTrab: Número que identifica o processo trabalhista, quando o início de TSVE se der por
                decisão judicial. Validação: Se preenchido, deve ser um processo judicial válido, com 20 (vinte)
                algarismos.
            :ivar natAtividade: Natureza da atividade. Validação: Preenchimento obrigatório se
                {codCateg}(./codCateg) = [201, 202, 401, 731, 734, 738]. Não deve ser preenchido se
                {codCateg}(./codCateg) = [721, 722, 771, 901].
            :ivar infoComplementares: Informações complementares DESCRICAO_COMPLETA:Grupo onde são fornecidas
                informações complementares, preenchidas conforme a categoria do TSVE. CONDICAO_GRUPO: O (de
                acordo com a condição dos grupos inferiores); OC (nos demais casos)
            :ivar mudancaCPF: Informações de mudança de CPF do trabalhador. CONDICAO_GRUPO: N (se
                {cadIni}(2300_infoTSVInicio_cadIni) = [S]); OC (nos demais casos)
            :ivar afastamento: Informações de afastamento do TSVE DESCRICAO_COMPLETA:Informações de afastamento
                do TSVE. Preenchimento exclusivo em caso de trabalhador que permaneça afastado na data de início
                da obrigatoriedade dos eventos não periódicos para o empregador no eSocial ou na data de
                alteração do CPF. CONDICAO_GRUPO: N (se grupo {termino}(2300_infoTSVInicio_termino) estiver
                preenchido); OC (nos demais casos)
            :ivar termino: Informação do término do TSVE DESCRICAO_COMPLETA:Informação do término do TSVE. Grupo
                preenchido exclusivamente caso seja necessário enviar cadastramento inicial referente a
                trabalhador com data de término anterior ao início dos eventos não periódicos para o empregador
                no eSocial (por exemplo, envio para pagamento de retiradas em meses posteriores à data de
                término e sob vigência dos eventos periódicos para o empregador no eSocial). CONDICAO_GRUPO: N
                (se {cadIni}(2300_infoTSVInicio_cadIni) = [N] ou grupo
                {afastamento}(2300_infoTSVInicio_afastamento) estiver preenchido); OC (nos demais casos)
            """

            cadIni: InfoTsvinicioCadIni = field(
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
            codCateg: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtInicio: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            nrProcTrab: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            natAtividade: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoComplementares: None | ESocial.EvtTsvinicio.InfoTsvinicio.InfoComplementares = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            mudancaCPF: None | ESocial.EvtTsvinicio.InfoTsvinicio.MudancaCpf = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            afastamento: None | ESocial.EvtTsvinicio.InfoTsvinicio.Afastamento = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            termino: None | ESocial.EvtTsvinicio.InfoTsvinicio.Termino = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class InfoComplementares(CommonMixin):
                """
                :ivar cargoFuncao: Cargo/Função ocupado pelo TSVE DESCRICAO_COMPLETA:Grupo que apresenta o cargo
                    e/ou função ocupada pelo TSVE. CONDICAO_GRUPO: OC (se
                    {codCateg}(2300_infoTSVInicio_codCateg) = [901, 903, 904, 906]); O (nos demais casos)
                :ivar remuneracao: Informações da remuneração e periodicidade de pagamento. CONDICAO_GRUPO: O
                    (se {codCateg}(2300_infoTSVInicio_codCateg) = [721, 722, 771, 906]); OC (nos demais casos)
                :ivar FGTS: Informações do FGTS DESCRICAO_COMPLETA:Informações do Fundo de Garantia do Tempo de
                    Serviço - FGTS. CONDICAO_GRUPO: O (se {codCateg}(2300_infoTSVInicio_codCateg) = [721]); N
                    (nos demais casos)
                :ivar infoDirigenteSindical: Informações relativas ao dirigente sindical. CONDICAO_GRUPO: O (se
                    {codCateg}(2300_infoTSVInicio_codCateg) = [401]); N (nos demais casos)
                :ivar infoTrabCedido: Informações relativas ao trabalhador cedido ou servidor público indicado
                    para conselho DESCRICAO_COMPLETA:Informações relativas ao trabalhador cedido/em exercício em
                    outro órgão ou servidor público indicado para conselho, preenchidas exclusivamente pelo
                    cessionário/órgão de destino. CONDICAO_GRUPO: O (se {codCateg}(2300_infoTSVInicio_codCateg)
                    = [305, 410]); N (nos demais casos)
                :ivar infoMandElet: Informações relativas a servidor público exercente de mandato eletivo.
                    CONDICAO_GRUPO: O (se {codCateg}(2300_infoTSVInicio_codCateg) = [304]); N (nos demais casos)
                :ivar infoEstagiario: Informações relativas ao estagiário ou ao beneficiário do Programa
                    Nacional de Prestação de Serviço Civil Voluntário. CONDICAO_GRUPO: O (se
                    {codCateg}(2300_infoTSVInicio_codCateg) = [901, 906]); N (nos demais casos)
                :ivar localTrabGeral: Estabelecimento onde o trabalhador exercerá suas atividades
                    DESCRICAO_COMPLETA:Estabelecimento (CNPJ, CNO, CAEPF) onde o trabalhador exercerá suas
                    atividades. Caso o trabalhador exerça suas atividades em instalações de terceiros, este
                    campo deve ser preenchido com o estabelecimento do próprio declarante ao qual o trabalhador
                    esteja vinculado. CONDICAO_GRUPO: O (se {codCateg}(2300_infoTSVInicio_codCateg) = [2XX, 304,
                    305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771, 901, 902, 906] e
                    {dtInicio}(2300_infoTSVInicio_dtInicio) &gt;= [2024-01-22]); F (se
                    {codCateg}(2300_infoTSVInicio_codCateg) = [2XX, 304, 305, 4XX, 721, 722, 723, 731, 734, 738,
                    761, 771, 901, 902, 906] e {dtInicio}(2300_infoTSVInicio_dtInicio) &lt; [2024-01-22]); N
                    (nos demais casos)
                """

                cargoFuncao: None | ESocial.EvtTsvinicio.InfoTsvinicio.InfoComplementares.CargoFuncao = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                remuneracao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                FGTS: None | ESocial.EvtTsvinicio.InfoTsvinicio.InfoComplementares.Fgts = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoDirigenteSindical: (
                    None | ESocial.EvtTsvinicio.InfoTsvinicio.InfoComplementares.InfoDirigenteSindical
                ) = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoTrabCedido: None | ESocial.EvtTsvinicio.InfoTsvinicio.InfoComplementares.InfoTrabCedido = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoMandElet: None | ESocial.EvtTsvinicio.InfoTsvinicio.InfoComplementares.InfoMandElet = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoEstagiario: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                localTrabGeral: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class CargoFuncao(CommonMixin):
                    """
                    :ivar nmCargo: Informar o nome do cargo. Validação: Preenchimento obrigatório se
                        {codCateg}(2300_infoTSVInicio_codCateg) for diferente de [410].
                    :ivar CBOCargo:
                    :ivar nmFuncao: Informar o nome da função de confiança. Validação: Preenchimento obrigatório
                        se {codCateg}(2300_infoTSVInicio_codCateg) = [410] e não houver informação de
                        {nmCargo}(./nmCargo).
                    :ivar CBOFuncao:
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

                @dataclass(kw_only=True)
                class Fgts(CommonMixin):
                    dtOpcFGTS: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoDirigenteSindical(CommonMixin):
                    """
                    :ivar categOrig: Preencher com o código correspondente à categoria de origem do dirigente
                        sindical. Validação: Deve ser um código válido e existente na Tabela 01, diferente de
                        [401].
                    :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela
                        05. Validação: O preenchimento é obrigatório e exclusivo se
                        {infoDirigenteSindical/categOrig}(./categOrig) corresponder a "Empregado", "Agente
                        Público", "Avulso" ou for igual a [721].
                    :ivar nrInsc: Informar o número de inscrição do empregador de origem do dirigente sindical,
                        de acordo com o tipo de inscrição indicado no campo
                        {infoDirigenteSindical/tpInsc}(./tpInsc). Validação: Preenchimento obrigatório e
                        exclusivo se {infoDirigenteSindical/tpInsc}(./tpInsc) for informado. Se preenchido, deve
                        ser um número de inscrição válido e diferente da inscrição do declarante, considerando
                        as particularidades aplicadas à informação de CNPJ de órgão público em S-1000. Se
                        {infoDirigenteSindical/tpInsc}(./tpInsc) = [1], deve possuir 14 (catorze) algarismos e
                        ser diferente do CNPJ base do empregador e dos estabelecimentos informados através do
                        evento S-1005. Se {infoDirigenteSindical/tpInsc}(./tpInsc) = [2], deve possuir 11 (onze)
                        algarismos.
                    :ivar dtAdmOrig: Preencher com a data de admissão (ou de início) do dirigente sindical na
                        empresa de origem. Validação: O preenchimento é obrigatório se
                        {infoDirigenteSindical/categOrig}(./categOrig) corresponder a "Empregado", "Agente
                        Público", "Avulso" ou for igual a [721].
                    :ivar matricOrig: Preencher com a matrícula do trabalhador na empresa de origem. Validação:
                        Preenchimento obrigatório se {infoDirigenteSindical/categOrig}(./categOrig) corresponder
                        a "Empregado" ou "Agente Público".
                    :ivar tpRegTrab: Tipo de regime trabalhista. Validação: O preenchimento é obrigatório e
                        exclusivo se {infoDirigenteSindical/categOrig}(./categOrig) corresponder a "Empregado"
                        ou "Agente Público".
                    :ivar tpRegPrev: Tipo de regime previdenciário. Validação: Se
                        {infoDirigenteSindical/categOrig}(./categOrig) for relativa a "Empregado", não pode ser
                        preenchido com [2].
                    """

                    categOrig: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
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
                    dtAdmOrig: None | XmlDate = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    matricOrig: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    tpRegTrab: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    tpRegPrev: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoTrabCedido(CommonMixin):
                    """
                    :ivar categOrig: Preencher com o código correspondente à categoria de origem do trabalhador
                        cedido ou do servidor público indicado para conselho. Validação: Deve ser um código
                        válido e existente na Tabela 01, diferente de [305, 410].
                    :ivar cnpjCednt: Informar o CNPJ do empregador/órgão público cedente/de origem. Validação:
                        Deve ser um CNPJ diferente do CNPJ do empregador/órgão público e diferente dos
                        estabelecimentos informados através do evento S-1005. REGRA:REGRA_VALIDA_CNPJ
                    :ivar matricCed: Preencher com a matrícula do trabalhador no empregador/órgão público
                        cedente/de origem.
                    :ivar dtAdmCed:
                    :ivar tpRegTrab: Tipo de regime trabalhista.
                    :ivar tpRegPrev: Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares
                        das Forças Armadas). Validação: Se {infoTrabCedido/categOrig}(./categOrig) for relativa
                        a "Empregado", não pode ser preenchido com [2, 4]. Se
                        {codCateg}(2300_infoTSVInicio_codCateg) = [305], deve ser preenchido com [2].
                    """

                    categOrig: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    cnpjCednt: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    matricCed: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtAdmCed: XmlDate = field(
                        metadata={
                            "type": "Element",
                            "min_inclusive": XmlDate(1890, 1, 1),
                        }
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

                @dataclass(kw_only=True)
                class InfoMandElet(CommonMixin):
                    """
                    :ivar categOrig: Preencher com o código correspondente à categoria de origem do servidor.
                        Validação: Deve ser um código válido e existente na Tabela 01, diferente de [304].
                    :ivar cnpjOrig: Informar o CNPJ do órgão público de origem. REGRA:REGRA_VALIDA_CNPJ
                    :ivar matricOrig: Preencher com a matrícula do servidor no órgão público de origem.
                    :ivar dtExercOrig:
                    :ivar indRemunCargo:
                    :ivar tpRegTrab: Tipo de regime trabalhista.
                    :ivar tpRegPrev: Tipo de regime previdenciário.
                    """

                    categOrig: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    cnpjOrig: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    matricOrig: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtExercOrig: XmlDate = field(
                        metadata={
                            "type": "Element",
                            "min_inclusive": XmlDate(1890, 1, 1),
                        }
                    )
                    indRemunCargo: None | str = field(
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

            @dataclass(kw_only=True)
            class MudancaCpf(CommonMixin):
                """
                :ivar cpfAnt: Preencher com o número do CPF antigo do trabalhador.
                :ivar matricAnt: Preencher com a matrícula anterior do trabalhador.
                :ivar dtAltCPF: Data de alteração do CPF.
                :ivar observacao:
                """

                cpfAnt: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                matricAnt: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
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
            class Afastamento(CommonMixin):
                """
                :ivar dtIniAfast: Data de início do afastamento. Validação: Devem ser observadas as seguintes
                    regras: a) Deve ser igual ou posterior à data de início do TSVE; b) Se
                    {cadIni}(2300_infoTSVInicio_cadIni) = [S], deve ser anterior à data de início da
                    obrigatoriedade dos eventos não periódicos para o empregador; c) Se
                    {cadIni}(2300_infoTSVInicio_cadIni) = [N], deve ser anterior à data de alteração do CPF do
                    trabalhador ({dtAltCPF}(2300_infoTSVInicio_mudancaCPF_dtAltCPF)).
                :ivar codMotAfast: Preencher com o código do motivo de afastamento temporário. Validação: Deve
                    ser um código válido e existente na Tabela 18, bem como compatível com o código de categoria
                    do trabalhador, conforme Tabela 18.
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
            class Termino(CommonMixin):
                """
                :ivar dtTerm: Preencher com a data do término. Validação: Devem ser observadas as seguintes
                    regras: a) Deve ser igual ou posterior à data de início do TSVE; b) Deve ser anterior à data
                    de início da obrigatoriedade dos eventos não periódicos para o empregador.
                """

                dtTerm: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
