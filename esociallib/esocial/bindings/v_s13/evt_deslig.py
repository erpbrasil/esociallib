from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00"


@dataclass(kw_only=True)
class TDetVerbas(CommonMixin):
    """
    Detalhamento das verbas rescisórias DESCRICAO_COMPLETA:Detalhamento das verbas rescisórias devidas ao
    trabalhador.

    Deve haver pelo menos uma rubrica de folha, mesmo que o valor líquido a ser pago ao trabalhador seja 0 (zero)
    em função de descontos.

    :ivar codRubr: Informar o código atribuído pelo empregador que identifica a rubrica em sua folha de
        pagamento ou o código da rubrica constante da Tabela de Rubricas Padrão. Validação: Não pode ser
        utilizada rubrica cuja {natRubr}(1010_infoRubrica_inclusao_dadosRubrica_natRubr) em S-1010 seja igual a
        [1801, 9220], desde que mês/ano de {dtDeslig}(2299_infoDeslig_dtDeslig) &gt;= [2021-07].
    :ivar ideTabRubr:
    :ivar qtdRubr:
    :ivar fatorRubr:
    :ivar vrRubr:
    :ivar indApurIR: Indicativo de tipo de apuração de IR. Validação: Informação obrigatória e exclusiva se
        mês/ano de {dtDeslig}(2299_infoDeslig_dtDeslig) &gt;= [2021-07].
    """

    class Meta:
        name = "T_detVerbas"

    codRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    ideTabRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    qtdRubr: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        },
    )
    fatorRubr: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        },
    )
    vrRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    indApurIR: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        },
    )


@dataclass(kw_only=True)
class TInfoAgNocivo(CommonMixin):
    """
    Grau de exposição a agentes nocivos DESCRICAO_COMPLETA:Grupo referente ao detalhamento do grau de exposição do
    trabalhador aos agentes nocivos que ensejam a cobrança da contribuição adicional para financiamento dos
    benefícios de aposentadoria especial.

    CONDICAO_GRUPO: O (se o trabalhador estiver amparado pelo RGPS); N (nos demais casos).
    """

    class Meta:
        name = "T_infoAgNocivo"

    grauExp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )


class IdeAdcTpAcConv(Enum):
    """
    Tipo do instrumento ou situação ensejadora da remuneração relativa a períodos de apuração anteriores.

    Validação: Se {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [04, 22], não pode
    ser informado [E, H, I].

    :cvar A: Acordo Coletivo de Trabalho
    :cvar B: Legislação federal, estadual, municipal ou distrital
    :cvar C: Convenção Coletiva de Trabalho
    :cvar D: Sentença normativa - Dissídio
    :cvar E: Conversão de licença saúde em acidente de trabalho
    :cvar G: Antecipação de diferenças de acordo, convenção ou dissídio coletivo
    :cvar H: Declaração de base de cálculo de FGTS anterior ao início do FGTS Digital
    :cvar I: Sentença judicial (exceto reclamatória trabalhista)
    :cvar J: Parcelas complementares conhecidas após o fechamento da folha
    """

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    G = "G"
    H = "H"
    I = "I"
    J = "J"


class RemunAposDesligIndRemun(Enum):
    """
    Indicativo de situação de remuneração após o desligamento.

    Validação: Informação obrigatória se {dtDeslig}(2299_infoDeslig_dtDeslig) &gt;= [2023-01-16].

    :cvar VALUE_1: Quarentena
    :cvar VALUE_2: Desligamento reconhecido judicialmente com data anterior a competências com remunerações já
        informadas no eSocial
    :cvar VALUE_3: Aposentadoria de servidor com data anterior a competências com remunerações já informadas no
        eSocial
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


@dataclass(kw_only=True)
class TDetVerbasDescFolha(TDetVerbas):
    """
    :ivar descFolha: Informações de desconto do empréstimo em folha. CONDICAO_GRUPO: O (se
        {}(1010_infoRubrica_inclusao_dadosRubrica_natRubr) em S-1010 = [9253]); N (nos demais casos)
    """

    class Meta:
        name = "T_detVerbas_descFolha"

    descFolha: None | TDetVerbasDescFolha.DescFolha = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        },
    )

    @dataclass(kw_only=True)
    class DescFolha(CommonMixin):
        """
        :ivar tpDesc:
        :ivar instFinanc: Código Bancário de Consignado concedente do empréstimo. Validação: Deve ser um código
            válido, conforme Tabela  37 do eSocial Tabelas.
        :ivar nrDoc:
        :ivar observacao: Outras informações do desconto.
        """

        tpDesc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
            }
        )
        instFinanc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
            }
        )
        nrDoc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
            }
        )
        observacao: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
            },
        )


@dataclass(kw_only=True)
class TIdeEstabLotInfoPerAnt(CommonMixin):
    class Meta:
        name = "T_ideEstabLot_infoPerAnt"

    tpInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    codLotacao: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    detVerbas: list[TDetVerbas] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
            "min_occurs": 1,
            "max_occurs": 200,
        },
    )
    infoAgNocivo: None | TInfoAgNocivo = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        },
    )
    infoSimples: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        },
    )


@dataclass(kw_only=True)
class TIdeEstabLot(CommonMixin):
    class Meta:
        name = "T_ideEstabLot"

    tpInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    codLotacao: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        }
    )
    detVerbas: list[TDetVerbasDescFolha] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
            "min_occurs": 1,
            "max_occurs": 200,
        },
    )
    infoAgNocivo: None | TInfoAgNocivo = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        },
    )
    infoSimples: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00",
        },
    )


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2299 - Desligamento.

    :ivar evtDeslig: Evento Desligamento. CHAVE_GRUPO: {Id} REGRA:REGRA_DESLIG_EXCLUI_DESLIGAMENTO_REINTEG
        REGRA:REGRA_DESLIG_EXCLUSAO_EVENTO REGRA:REGRA_DESLIG_EXISTE_EVENTO_POSTERIOR
        REGRA:REGRA_DESLIG_JA_EXISTE_BAIXA REGRA:REGRA_DESLIG_TRABALHADOR_AFASTADO
        REGRA:REGRA_EMPREGADO_DOMESTICO REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EVE_FOPAG_SIMPLIFICADO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXTEMP_DOMESTICO REGRA:REGRA_EXTEMP_REINTEGRACAO
        REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_MUDANCA_CPF
        REGRA:REGRA_REMUN_FGTS_ANTERIOR_ESOCIAL REGRA:REGRA_REMUN_IND_RETIFICACAO
        REGRA:REGRA_REMUN_PERMITE_EXCLUSAO REGRA:REGRA_RETIFICA_MESMO_VINCULO
        REGRA:REGRA_RUBRICA_COMPATIVEL_CATEGORIA REGRA:REGRA_RUBRICA_ECONSIGNADO
        REGRA:REGRA_VALIDA_CODINCCP_EXC_SEGURADO REGRA:REGRA_VALIDA_EMPREGADOR
        REGRA:REGRA_VALIDA_PERIODO_APURACAO REGRA:REGRA_VINCULO_ATIVO_NA_DTEVENTO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtDeslig/v_S_01_03_00"

    evtDeslig: ESocial.EvtDeslig = field(
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
    class EvtDeslig(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar infoDeslig: Informações relativas ao desligamento do vínculo. CHAVE_GRUPO: {dtDeslig*}
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
        infoDeslig: ESocial.EvtDeslig.InfoDeslig = field(
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
        class InfoDeslig(CommonMixin):
            """
            :ivar mtvDeslig:
            :ivar dtDeslig: Preencher com a data de desligamento do vínculo (último dia trabalhado). Validação:
                Deve ser uma data igual ou anterior à data atual acrescida de 10 (dez) dias. No caso de
                empregado reintegrado e quando não se tratar de retificação do desligamento anterior à
                reintegração, também deve ser uma data igual ou posterior a
                {dtEfetRetorno}(2298_infoReintegr_dtEfetRetorno) do evento S-2298.
            :ivar dtAvPrv: Data de concessão do aviso prévio. Validação: Se informada, deve ser igual ou
                posterior à data de admissão e igual ou anterior a {dtDeslig}(./dtDeslig).
            :ivar indPagtoAPI: Indicativo de pagamento de aviso prévio indenizado pelo empregador, ao empregado.
            :ivar dtProjFimAPI: Data projetada para o término do aviso prévio indenizado. Validação: Obrigatório
                se {indPagtoAPI}(./indPagtoAPI) for igual a [S], devendo ser igual ou posterior a
                {dtDeslig}(./dtDeslig).
            :ivar pensAlim: Indicativo de pensão alimentícia para fins de retenção de FGTS. Validação:
                Preenchimento obrigatório e exclusivo se o vínculo for celetista
                ({tpRegTrab}(2200_vinculo_tpRegTrab) em S-2200 = [1]).
            :ivar percAliment:
            :ivar vrAlim:
            :ivar nrProcTrab: Número que identifica o processo trabalhista, quando o desligamento se der por
                decisão judicial. Validação: Se preenchido, deve ser um processo judicial válido, com 20 (vinte)
                algarismos.
            :ivar indPDV: Indicativo se o desligamento ocorreu por meio de adesão a Programa de Demissão
                Voluntária (PDV). Validação: Não informar se {mtvDeslig}(./mtvDeslig) = [10, 11, 12, 13, 28, 29,
                30, 34, 36, 37, 40, 43, 44].
            :ivar infoInterm: Informações relativas ao trabalho intermitente. CHAVE_GRUPO: {dia} CONDICAO_GRUPO:
                O (se o código de categoria no RET for igual a [111] no mês/ano de
                {dtDeslig}(2299_infoDeslig_dtDeslig); N (nos demais casos)
            :ivar observacoes: Observações sobre o desligamento. CONDICAO_GRUPO: OC
            :ivar sucessaoVinc: Sucessão do vínculo trabalhista/estatutário DESCRICAO_COMPLETA:Grupo preenchido
                exclusivamente nos casos de sucessão do vínculo trabalhista, com a identificação da empresa
                sucessora. CONDICAO_GRUPO: O (se {mtvDeslig}(2299_infoDeslig_mtvDeslig) = [11, 12, 13, 28, 29,
                37, 43]); N (nos demais casos)
            :ivar transfTit: Transferência de titularidade do empregado doméstico
                DESCRICAO_COMPLETA:Transferência de titularidade do empregado doméstico para outro representante
                da mesma unidade familiar. CONDICAO_GRUPO: O (se {mtvDeslig}(2299_infoDeslig_mtvDeslig) = [34]);
                N (nos demais casos)
            :ivar mudancaCPF: Informação do novo CPF do trabalhador. CONDICAO_GRUPO: O (se
                {mtvDeslig}(2299_infoDeslig_mtvDeslig) = [36]); N (nos demais casos)
            :ivar verbasResc: Verbas rescisórias DESCRICAO_COMPLETA:Grupo onde são prestadas as informações
                relativas às verbas devidas ao trabalhador na rescisão contratual. CONDICAO_GRUPO: N (se
                {mtvDeslig}(2299_infoDeslig_mtvDeslig) = [11, 12, 13, 25, 28, 29, 30, 34, 36, 43, 44] OU
                {dtDeslig}(2299_infoDeslig_dtDeslig) for anterior ao início de obrigatoriedade dos eventos
                periódicos para o empregador OU {tpRegTrab}(2200_vinculo_tpRegTrab) em S-2200 = [2]); OC (nos
                demais casos)
            :ivar remunAposDeslig: Informações sobre a quarentena remunerada ou outra situação de desligamento
                com data anterior DESCRICAO_COMPLETA:Informações sobre a "quarentena" remunerada de trabalhador
                desligado ou outra situação de desligamento com data anterior. O grupo deve ser preenchido
                apenas no caso do trabalhador que recebe remuneração após o desligamento por estar
                impossibilitado de exercer atividade remunerada, no caso de desligamento reconhecido
                judicialmente com data anterior a competências com remunerações já informadas ou em caso de
                concessão de aposentadoria de servidor com data anterior a competências com remunerações já
                informadas no eSocial. CONDICAO_GRUPO: OC
            :ivar consigFGTS: Informações sobre operação de crédito consignado com garantia de FGTS.
                CONDICAO_GRUPO: OC
            """

            mtvDeslig: str = field(
                metadata={
                    "type": "Element",
                    "pattern": r"\d{2}",
                }
            )
            dtDeslig: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtAvPrv: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            indPagtoAPI: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtProjFimAPI: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            pensAlim: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            percAliment: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            vrAlim: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            nrProcTrab: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            indPDV: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoInterm: list[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 31,
                },
            )
            observacoes: list[ESocial.EvtDeslig.InfoDeslig.Observacoes] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                },
            )
            sucessaoVinc: None | ESocial.EvtDeslig.InfoDeslig.SucessaoVinc = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            transfTit: None | ESocial.EvtDeslig.InfoDeslig.TransfTit = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            mudancaCPF: None | ESocial.EvtDeslig.InfoDeslig.MudancaCpf = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            verbasResc: None | ESocial.EvtDeslig.InfoDeslig.VerbasResc = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            remunAposDeslig: None | ESocial.EvtDeslig.InfoDeslig.RemunAposDeslig = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            consigFGTS: list[ESocial.EvtDeslig.InfoDeslig.ConsigFgts] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class Observacoes(CommonMixin):
                """
                :ivar observacao: Observação relevante sobre o desligamento do trabalhador, que não esteja
                    consignada em outros campos.
                """

                observacao: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class SucessaoVinc(CommonMixin):
                """
                :ivar tpInsc:
                :ivar nrInsc: Informar o número de inscrição do empregador sucessor, de acordo com o tipo de
                    inscrição indicado no campo {sucessaoVinc/tpInsc}(./tpInsc). Validação: Deve ser um número
                    de inscrição válido e diferente da inscrição do declarante, considerando as particularidades
                    aplicadas à informação de CNPJ de órgão público em S-1000. Se
                    {sucessaoVinc/tpInsc}(./tpInsc) = [1], deve possuir 14 (catorze) algarismos e ser diferente
                    do CNPJ base do empregador (exceto se {ideEmpregador/nrInsc}(2299_ideEmpregador_nrInsc)
                    tiver 14 (catorze) algarismos). Também deve ser diferente dos estabelecimentos informados
                    através do evento S-1005, exceto se a natureza jurídica do declarante for Administração
                    Pública (grupo [1]). Se {sucessaoVinc/tpInsc}(./tpInsc) = [2], deve possuir 11 (onze)
                    algarismos.
                """

                tpInsc: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                nrInsc: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class TransfTit(CommonMixin):
                """
                :ivar cpfSubstituto: Preencher com o CPF do novo titular. Validação: Deve ser um CPF válido e
                    diferente do CPF do declarante e do empregado.
                :ivar dtNascto: Preencher com a data de nascimento do novo titular. Validação: Deve corresponder
                    à data de nascimento cadastrada na base de dados do CPF do {cpfSubstituto}(./cpfSubstituto).
                """

                cpfSubstituto: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtNascto: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class MudancaCpf(CommonMixin):
                """
                :ivar novoCPF: Preencher com o novo CPF do trabalhador. Validação: Deve ser um CPF válido e
                    diferente do CPF do empregador e do antigo CPF do trabalhador.
                """

                novoCPF: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class VerbasResc(CommonMixin):
                """
                :ivar dmDev: Demonstrativo de valores devidos ao trabalhador DESCRICAO_COMPLETA:Identificação de
                    cada um dos demonstrativos de valores devidos ao trabalhador. CHAVE_GRUPO: {ideDmDev}
                    REGRA:REGRA_DEMONSTRATIVO
                :ivar procJudTrab:
                :ivar infoMV:
                :ivar procCS: Informação sobre processo judicial que suspende a exigibilidade da Contribuição
                    Social Rescisória. CONDICAO_GRUPO: OC
                """

                dmDev: list[ESocial.EvtDeslig.InfoDeslig.VerbasResc.DmDev] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 50,
                    },
                )
                procJudTrab: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                infoMV: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                procCS: None | ESocial.EvtDeslig.InfoDeslig.VerbasResc.ProcCs = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class DmDev(CommonMixin):
                    """
                    :ivar ideDmDev: Identificador atribuído pela empresa para o demonstrativo de valores devidos
                        ao trabalhador relativo a verbas rescisórias. Validação: Deve ser um identificador único
                        dentro da mesma competência (mês/ano da data de desligamento) para cada um dos
                        demonstrativos do trabalhador. Se {procEmi}(2299_ideEvento_procEmi) = [1, 3] e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [21, 22], o
                        identificador não pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições.
                        REGRA:REGRA_CARACTERE_ESPECIAL
                    :ivar indRRA: Indicativo de Rendimentos Recebidos Acumuladamente - RRA. Somente preencher
                        este campo se for um demonstrativo de RRA.
                    :ivar notAFT: Número da notificação de FGTS que deu origem à confissão. Validação: Se o
                        campo for preenchido: a) O mês/ano de {}(2299_infoDeslig_dtDeslig) deve ser igual ou
                        posterior ao início do FGTS Digital; b) Todas as rubricas de vencimento
                        ({}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 = [1]) informadas no
                        demonstrativo devem possuir {}(1010_infoRubrica_inclusao_dadosRubrica_codIncFGTS) em
                        S-1010 = [71]; c) Devem ser informados apenas caracteres alfanuméricos, com 9 (nove)
                        posições.
                    :ivar infoRRA:
                    :ivar infoPerApur: Verbas rescisórias relativas ao mês/ano da data do desligamento.
                        CONDICAO_GRUPO: O (se não existir o grupo
                        {infoPerAnt}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt)); OC (nos demais casos)
                    :ivar infoPerAnt: Informações relativas a períodos anteriores DESCRICAO_COMPLETA:Remuneração
                        relativa a períodos anteriores, devida em função de acordos coletivos, legislação
                        específica, convenção coletiva de trabalho, dissídio ou conversão de licença saúde em
                        acidente de trabalho. CONDICAO_GRUPO: N (se {}(2299_infoDeslig_verbasResc_dmDev_notAFT)
                        for informado); O (se não existir o grupo
                        {infoPerApur}(2299_infoDeslig_verbasResc_dmDev_infoPerApur)); OC (nos demais casos)
                    """

                    ideDmDev: str = field(
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
                    notAFT: None | str = field(
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
                    infoPerApur: None | ESocial.EvtDeslig.InfoDeslig.VerbasResc.DmDev.InfoPerApur = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoPerAnt: None | ESocial.EvtDeslig.InfoDeslig.VerbasResc.DmDev.InfoPerAnt = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoPerApur(CommonMixin):
                        """
                        :ivar ideEstabLot: Identificação do estabelecimento e lotação
                            DESCRICAO_COMPLETA:Identificação do estabelecimento e da lotação nos quais o
                            trabalhador possui remuneração no período de apuração. O estabelecimento
                            identificado no grupo pode ser: o número do CNPJ do estabelecimento da própria
                            empresa (matriz/filial), o número da obra (própria) no CNO, ou o número do CAEPF (no
                            caso de pessoa física obrigada a inscrição no Cadastro de Atividade Econômica da
                            Pessoa Física). CHAVE_GRUPO: {tpInsc}, {nrInsc}, {codLotacao}
                        """

                        ideEstabLot: list[TIdeEstabLot] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 24,
                            },
                        )

                    @dataclass(kw_only=True)
                    class InfoPerAnt(CommonMixin):
                        """
                        :ivar ideADC: Instrumento ou situação ensejadora da remuneração em períodos anteriores
                            DESCRICAO_COMPLETA:Identificação do instrumento ou situação ensejadora da
                            remuneração relativa a períodos de apuração anteriores. CHAVE_GRUPO: {dtAcConv},
                            {tpAcConv}
                        """

                        ideADC: list[ESocial.EvtDeslig.InfoDeslig.VerbasResc.DmDev.InfoPerAnt.IdeAdc] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 8,
                            },
                        )

                        @dataclass(kw_only=True)
                        class IdeAdc(CommonMixin):
                            """
                            :ivar dtAcConv:
                            :ivar tpAcConv:
                            :ivar dsc:
                            :ivar idePeriodo: Identificação do período de referência da remuneração
                                DESCRICAO_COMPLETA:Identificação do período ao qual se referem as diferenças de
                                remuneração. CHAVE_GRUPO: {perRef}
                            """

                            dtAcConv: None | XmlDate = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": XmlDate(1890, 1, 1),
                                },
                            )
                            tpAcConv: IdeAdcTpAcConv = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            dsc: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            idePeriodo: list[
                                ESocial.EvtDeslig.InfoDeslig.VerbasResc.DmDev.InfoPerAnt.IdeAdc.IdePeriodo
                            ] = field(
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
                                :ivar perRef: Informar o período ao qual se refere o complemento de remuneração,
                                    no formato AAAA-MM. Validação: Deve ser igual ou anterior ao mês/ano da data
                                    do desligamento, informada em {dtDeslig}(2299_infoDeslig_dtDeslig). Deve ser
                                    informado no formato AAAA-MM. Se {tpAcConv}(../tpAcConv) = [H], deve ser
                                    anterior ao início do FGTS Digital e igual ou posterior a [1994-07].
                                :ivar ideEstabLot: Identificação do estabelecimento e lotação
                                    DESCRICAO_COMPLETA:Identificação do estabelecimento e da lotação aos quais
                                    se referem as diferenças de remuneração do mês identificado no grupo
                                    superior. CHAVE_GRUPO: {tpInsc}, {nrInsc}, {codLotacao}
                                """

                                perRef: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                ideEstabLot: list[TIdeEstabLotInfoPerAnt] = field(
                                    default_factory=list,
                                    metadata={
                                        "type": "Element",
                                        "min_occurs": 1,
                                        "max_occurs": 24,
                                    },
                                )

                @dataclass(kw_only=True)
                class ProcCs(CommonMixin):
                    nrProcJud: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

            @dataclass(kw_only=True)
            class RemunAposDeslig(CommonMixin):
                """
                :ivar indRemun:
                :ivar dtFimRemun: Preencher com a data final da quarentena a que está sujeito o trabalhador. No
                    caso de desligamento reconhecido judicialmente ou de concessão de aposentadoria de servidor
                    com data anterior a competências com remunerações já informadas no eSocial, informar o
                    último dia trabalhado. Validação: Deve ser uma data posterior a
                    {dtDeslig}(2299_infoDeslig_dtDeslig).
                """

                indRemun: None | RemunAposDesligIndRemun = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                dtFimRemun: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class ConsigFgts(CommonMixin):
                insConsig: str = field(
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                nrContr: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{1,40}",
                    }
                )
