from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtExpRisco/v_S_01_03_00"


class AgNocTpAval(Enum):
    """
    Tipo de avaliação do agente nocivo.

    Validação: Preenchimento obrigatório e exclusivo se {codAgNoc}(./codAgNoc) for diferente de [09.01.001].

    :cvar VALUE_1: Critério quantitativo
    :cvar VALUE_2: Critério qualitativo
    """

    VALUE_1 = 1
    VALUE_2 = 2


class AgNocUnMed(Enum):
    """
    Dose ou unidade de medida da intensidade ou concentração do agente.

    Validação: Preenchimento obrigatório e exclusivo se {tpAval}(./tpAval) = [1].

    :cvar VALUE_1: dose diária de ruído
    :cvar VALUE_2: decibel linear (dB (linear))
    :cvar VALUE_3: decibel (C) (dB(C))
    :cvar VALUE_4: decibel (A) (dB(A))
    :cvar VALUE_5: metro por segundo ao quadrado (m/s^^2^^)
    :cvar VALUE_6: metro por segundo elevado a 1,75 (m/s^^1,75^^)
    :cvar VALUE_7: parte de vapor ou gás por milhão de partes de ar contaminado (ppm)
    :cvar VALUE_8: miligrama por metro cúbico de ar (mg/m^^3^^)
    :cvar VALUE_9: fibra por centímetro cúbico (f/cm^^3^^)
    :cvar VALUE_10: grau Celsius (ºC)
    :cvar VALUE_11: metro por segundo (m/s)
    :cvar VALUE_12: porcentual
    :cvar VALUE_13: lux (lx)
    :cvar VALUE_14: unidade formadora de colônias por metro cúbico (ufc/m^^3^^)
    :cvar VALUE_15: dose diária
    :cvar VALUE_16: dose mensal
    :cvar VALUE_17: dose trimestral
    :cvar VALUE_18: dose anual
    :cvar VALUE_19: watt por metro quadrado (W/m^^2^^)
    :cvar VALUE_20: ampère por metro (A/m)
    :cvar VALUE_21: militesla (mT)
    :cvar VALUE_22: microtesla (μT)
    :cvar VALUE_23: miliampère (mA)
    :cvar VALUE_24: quilovolt por metro (kV/m)
    :cvar VALUE_25: volt por metro (V/m)
    :cvar VALUE_26: joule por metro quadrado (J/m^^2^^)
    :cvar VALUE_27: milijoule por centímetro quadrado (mJ/cm^^2^^)
    :cvar VALUE_28: milisievert (mSv)
    :cvar VALUE_29: milhão de partículas por decímetro cúbico (mppdc)
    :cvar VALUE_30: umidade relativa do ar (UR (%))
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30


class EpcEpiUtilizEpc(Enum):
    """
    O empregador implementa medidas de proteção coletiva (EPC) para eliminar ou reduzir a exposição dos
    trabalhadores ao agente nocivo?

    :cvar VALUE_0: Não se aplica
    :cvar VALUE_1: Não implementa
    :cvar VALUE_2: Implementa
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class EpcEpiUtilizEpi(Enum):
    """
    Utilização de EPI.

    :cvar VALUE_0: Não se aplica
    :cvar VALUE_1: Não utilizado
    :cvar VALUE_2: Utilizado
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class InfoAmbLocalAmb(Enum):
    """
    Informar o tipo de estabelecimento do ambiente de trabalho.

    :cvar VALUE_1: Estabelecimento do próprio empregador
    :cvar VALUE_2: Estabelecimento de terceiros
    """

    VALUE_1 = 1
    VALUE_2 = 2


class RespRegIdeOc(Enum):
    """
    Órgão de classe ao qual o responsável pelos registros ambientais está vinculado.

    Validação: Preenchimento obrigatório se {codAgNoc}(../agNoc_codAgNoc) for diferente de [09.01.001].

    :cvar VALUE_1: Conselho Regional de Medicina - CRM
    :cvar VALUE_4: Conselho Regional de Engenharia e Agronomia - CREA
    :cvar VALUE_9: Outros
    """

    VALUE_1 = 1
    VALUE_4 = 4
    VALUE_9 = 9


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2240 - Condições Ambientais do Trabalho - Agentes Nocivos.

    :ivar evtExpRisco: Evento Condições Ambientais do Trabalho - Agentes Nocivos. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_EXT_SEM_IMPACTO_FOPAG
        REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_EXTEMP_REINTEGRACAO REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_TSV_ATIVO_NA_DTEVENTO
        REGRA:REGRA_VINCULO_ATIVO_NA_DTEVENTO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtExpRisco/v_S_01_03_00"

    evtExpRisco: ESocial.EvtExpRisco = field(
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
    class EvtExpRisco(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar infoExpRisco: Ambiente de trabalho, atividades desempenhadas e exposição a agentes nocivos
            DESCRICAO_COMPLETA:Informações sobre o ambiente de trabalho, atividades desempenhadas e exposição a
            agentes nocivos. REGRA:REGRA_PERIODO_EXPOSICAO_RISCO CHAVE_GRUPO: {dtIniCondicao*}
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
        infoExpRisco: ESocial.EvtExpRisco.InfoExpRisco = field(
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
        class InfoExpRisco(CommonMixin):
            """
            :ivar dtIniCondicao: Informar a data em que o trabalhador iniciou as atividades nas condições
                descritas ou a data de início da obrigatoriedade deste evento para o empregador no eSocial, a
                que for mais recente. Validação: Deve ser uma data válida, igual ou posterior à data de admissão
                do vínculo a que se refere. Não pode ser anterior à data de início da obrigatoriedade deste
                evento para o empregador no eSocial, nem pode ser posterior a 30 (trinta) dias da data atual.
            :ivar dtFimCondicao: Informar a data em que o trabalhador terminou as atividades nas condições
                descritas. Validação: Preenchimento obrigatório e exclusivo para trabalhador avulso (código de
                categoria no RET igual a [2XX]) e se {dtIniCondicao}(./dtIniCondicao) for igual ou posterior a
                [2023-01-16]. Se informada, deve ser uma data válida, igual ou posterior a
                {dtIniCondicao}(./dtIniCondicao) e igual ou anterior a {dtTerm}(2399_infoTSVTermino_dtTerm) de
                S-2399, se existente.
            :ivar infoAmb: Informações relativas ao ambiente de trabalho. DESCRICAO_COMPLETA:Informações
                relativas ao ambiente de trabalho. Somente no caso de trabalhador avulso (código de categoria no
                RET igual a [2XX]) é possível declarar mais de um ambiente. CHAVE_GRUPO: {tpInsc}, {nrInsc}
                REGRA:REGRA_AMBIENTE_TRABALHO
            :ivar infoAtiv: Descrição das atividades desempenhadas.
            :ivar agNoc: Agente(s) nocivo(s) ao(s) qual(is) o trabalhador está exposto. CHAVE_GRUPO: {codAgNoc},
                {dscAgNoc}
            :ivar respReg: Responsável pelos registros ambientais DESCRICAO_COMPLETA:Informações relativas ao
                responsável pelos registros ambientais. CHAVE_GRUPO: {cpfResp}
            :ivar obs: Observações relativas a registros ambientais. CONDICAO_GRUPO: OC
            """

            dtIniCondicao: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtFimCondicao: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoAmb: list[ESocial.EvtExpRisco.InfoExpRisco.InfoAmb] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 9,
                },
            )
            infoAtiv: ESocial.EvtExpRisco.InfoExpRisco.InfoAtiv = field(
                metadata={
                    "type": "Element",
                }
            )
            agNoc: list[ESocial.EvtExpRisco.InfoExpRisco.AgNoc] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 999,
                },
            )
            respReg: list[ESocial.EvtExpRisco.InfoExpRisco.RespReg] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )
            obs: None | ESocial.EvtExpRisco.InfoExpRisco.Obs = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class InfoAmb(CommonMixin):
                """
                :ivar localAmb:
                :ivar dscSetor: Descrição do lugar administrativo, na estrutura organizacional da empresa, onde
                    o trabalhador exerce suas atividades laborais.
                :ivar tpInsc:
                :ivar nrInsc: Número de inscrição onde está localizado o ambiente. Validação: Deve ser um
                    identificador válido, compatível com o conteúdo do campo {infoAmb/tpInsc}(./tpInsc) e: a) Se
                    {localAmb}(./localAmb) = [1], deve ser válido e existente na Tabela de Estabelecimentos
                    (S-1005); b) Se {localAmb}(./localAmb) = [2], deve ser diferente dos estabelecimentos
                    informados na Tabela S-1005 e, se {infoAmb/tpInsc}(./tpInsc) = [1] e o empregador for pessoa
                    jurídica, a raiz do CNPJ informado deve ser diferente da constante em S-1000.
                """

                localAmb: InfoAmbLocalAmb = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dscSetor: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
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
            class InfoAtiv(CommonMixin):
                """
                :ivar dscAtivDes: Descrição das atividades, físicas ou mentais, realizadas pelo trabalhador, por
                    força do poder de comando a que se submete. As atividades deverão ser escritas com exatidão,
                    e de forma sucinta, com a utilização de verbos no infinitivo impessoal. Ex.: Distribuir
                    panfletos, operar máquina de envase, etc.
                """

                dscAtivDes: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class AgNoc(CommonMixin):
                """
                :ivar codAgNoc:
                :ivar dscAgNoc: Descrição do agente nocivo. Validação: Preenchimento obrigatório se
                    {codAgNoc}(./codAgNoc) = [01.01.001, 01.02.001, 01.03.001, 01.04.001, 01.05.001, 01.06.001,
                    01.07.001, 01.08.001, 01.09.001, 01.10.001, 01.12.001, 01.13.001, 01.14.001, 01.15.001,
                    01.16.001, 01.17.001, 01.18.001, 05.01.001]. Não informar se {codAgNoc}(./codAgNoc) =
                    [09.01.001] e {dtIniCondicao}(../dtIniCondicao) &gt;= [2024-04-22].
                :ivar tpAval:
                :ivar intConc:
                :ivar limTol:
                :ivar unMed:
                :ivar tecMedicao:
                :ivar nrProcJud: Em caso de agente nocivo incluído por determinação administrativa ou judicial,
                    preencher com o número do processo. Validação: Informação obrigatória e exclusiva se
                    {codAgNoc}(./codAgNoc) = [05.01.001]. Se {dtIniCondicao}(2240_infoExpRisco_dtIniCondicao)
                    &lt; [2024-01-22], o preenchimento é opcional.
                :ivar epcEpi: EPC e EPI DESCRICAO_COMPLETA:Informações relativas a Equipamentos de Proteção
                    Coletiva - EPC e Equipamentos de Proteção Individual - EPI. CONDICAO_GRUPO: N (se
                    {codAgNoc}(../codAgNoc) = [09.01.001]); O (nos demais casos)
                """

                codAgNoc: str = field(
                    metadata={
                        "type": "Element",
                        "length": 9,
                        "pattern": r"\d{2}\.\d{2}\.\d{3}",
                    }
                )
                dscAgNoc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                tpAval: None | AgNocTpAval = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                intConc: None | Decimal = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "max_inclusive": Decimal("999999.9999"),
                        "total_digits": 10,
                        "fraction_digits": 4,
                    },
                )
                limTol: None | Decimal = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "max_inclusive": Decimal("999999.9999"),
                        "total_digits": 10,
                        "fraction_digits": 4,
                    },
                )
                unMed: None | AgNocUnMed = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                tecMedicao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 40,
                        "pattern": r".*[^\s].*",
                    },
                )
                nrProcJud: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                epcEpi: None | ESocial.EvtExpRisco.InfoExpRisco.AgNoc.EpcEpi = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class EpcEpi(CommonMixin):
                    """
                    :ivar utilizEPC:
                    :ivar eficEpc: Os EPCs são eficazes na neutralização do risco ao trabalhador? Validação:
                        Preenchimento obrigatório e exclusivo se {utilizEPC}(./utilizEPC) = [2].
                    :ivar utilizEPI:
                    :ivar eficEpi: Os EPIs são eficazes na neutralização do risco ao trabalhador? Validação:
                        Preenchimento obrigatório e exclusivo se {utilizEPI}(./utilizEPI) = [2].
                    :ivar epi: EPI. CONDICAO_GRUPO: O (se {utilizEPI}(../utilizEPI) = [2]); N (nos demais casos)
                        CHAVE_GRUPO: {docAval}
                    :ivar epiCompl: Requisitos das NR-06 e NR-09 pelo(s) EPI(s) informado(s)
                        DESCRICAO_COMPLETA:Requisitos da Norma Regulamentadora 06 - NR-06 e da Norma
                        Regulamentadora 09 - NR-09 pelo(s) EPI(s) informado(s). CONDICAO_GRUPO: O (se
                        {utilizEPI}(../utilizEPI) = [2]); N (nos demais casos)
                    """

                    utilizEPC: EpcEpiUtilizEpc = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    eficEpc: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    utilizEPI: EpcEpiUtilizEpi = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    eficEpi: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    epi: list[ESocial.EvtExpRisco.InfoExpRisco.AgNoc.EpcEpi.Epi] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 50,
                        },
                    )
                    epiCompl: None | ESocial.EvtExpRisco.InfoExpRisco.AgNoc.EpcEpi.EpiCompl = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class Epi(CommonMixin):
                        """
                        :ivar docAval: Certificado de Aprovação - CA ou documento de avaliação do EPI.
                        """

                        docAval: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class EpiCompl(CommonMixin):
                        """
                        :ivar medProtecao: Foi tentada a implementação de medidas de proteção coletiva, de
                            caráter administrativo ou de organização, optando-se pelo EPI por inviabilidade
                            técnica, insuficiência ou interinidade, ou ainda em caráter complementar ou
                            emergencial?
                        :ivar condFuncto: Foram observadas as condições de funcionamento do EPI ao longo do
                            tempo, conforme especificação técnica do fabricante nacional ou importador,
                            ajustadas às condições de campo?
                        :ivar usoInint: Foi observado o uso ininterrupto do EPI ao longo do tempo, conforme
                            especificação técnica do fabricante nacional ou importador, ajustadas às condições
                            de campo?
                        :ivar przValid: Foi observado o prazo de validade do CA no momento da compra do EPI?
                        :ivar periodicTroca: É observada a periodicidade de troca definida pelo fabricante
                            nacional ou importador e/ou programas ambientais, comprovada mediante recibo
                            assinado pelo usuário em época própria?
                        :ivar higienizacao: É observada a higienização conforme orientação do fabricante
                            nacional ou importador?
                        """

                        medProtecao: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        condFuncto: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        usoInint: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        przValid: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        periodicTroca: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        higienizacao: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

            @dataclass(kw_only=True)
            class RespReg(CommonMixin):
                """
                :ivar cpfResp: Preencher com o CPF do responsável pelos registros ambientais. Validação: Deve
                    ser um CPF válido.
                :ivar ideOC:
                :ivar dscOC:
                :ivar nrOC:
                :ivar ufOC: Sigla da Unidade da Federação - UF do órgão de classe. Validação: Preenchimento
                    obrigatório se {codAgNoc}(../agNoc_codAgNoc) for diferente de [09.01.001].
                """

                cpfResp: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                ideOC: None | RespRegIdeOc = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                dscOC: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                        "pattern": r".*[^\s].*",
                    },
                )
                nrOC: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 14,
                        "pattern": r".*[^\s].*",
                    },
                )
                ufOC: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Obs(CommonMixin):
                """
                :ivar obsCompl: Observação(ões) complementar(es) referente(s) a registros ambientais.
                """

                obsCompl: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
