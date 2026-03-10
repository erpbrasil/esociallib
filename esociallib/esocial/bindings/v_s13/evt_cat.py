from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCAT/v_S_01_03_00"


class CatIniciatCat(Enum):
    """
    Iniciativa da CAT.

    :cvar VALUE_1: Empregador
    :cvar VALUE_2: Ordem judicial
    :cvar VALUE_3: Determinação de órgão fiscalizador
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class CatTpAcid(Enum):
    """
    Tipo de acidente de trabalho.

    :cvar VALUE_1: Típico
    :cvar VALUE_2: Doença
    :cvar VALUE_3: Trajeto
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class CatTpCat(Enum):
    """
    Tipo de CAT.

    :cvar VALUE_1: Inicial
    :cvar VALUE_2: Reabertura
    :cvar VALUE_3: Comunicação de óbito
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class EmitenteIdeOc(Enum):
    """
    Órgão de classe.

    :cvar VALUE_1: Conselho Regional de Medicina - CRM
    :cvar VALUE_2: Conselho Regional de Odontologia - CRO
    :cvar VALUE_3: Registro do Ministério da Saúde - RMS
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class LocalAcidenteTpLocal(Enum):
    """
    Tipo de local do acidente.

    :cvar VALUE_1: Estabelecimento do empregador no Brasil
    :cvar VALUE_2: Estabelecimento do empregador no exterior
    :cvar VALUE_3: Estabelecimento de terceiros onde o empregador presta serviços
    :cvar VALUE_4: Via pública
    :cvar VALUE_5: Área rural
    :cvar VALUE_6: Embarcação
    :cvar VALUE_9: Outros
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_9 = 9


class ParteAtingidaLateralidade(Enum):
    """
    Lateralidade da(s) parte(s) atingida(s).

    Nos casos de órgãos bilaterais, ou seja, que se situam dos lados do corpo, assinalar o lado (direito ou
    esquerdo). Ex.: Caso o órgão atingido seja perna, apontar qual foi a atingida (perna direita, perna esquerda ou
    ambas). Se o órgão atingido é único (como, por exemplo, a cabeça), assinalar este campo como não aplicável.

    :cvar VALUE_0: Não aplicável
    :cvar VALUE_1: Esquerda
    :cvar VALUE_2: Direita
    :cvar VALUE_3: Ambas
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2210 - Comunicação de Acidente de Trabalho.

    :ivar evtCAT: Evento Comunicação de Acidente de Trabalho. CHAVE_GRUPO: {Id} REGRA:REGRA_EMPREGADO_DOMESTICO
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_EXT_SEM_IMPACTO_FOPAG
        REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EXCLUI_EVENTO_CAT REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_EXTEMP_REINTEGRACAO REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_RETIFICA_DT_ACIDENTE REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_TSV_ATIVO_NA_DTEVENTO
        REGRA:REGRA_VINCULO_ATIVO_NA_DTEVENTO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCAT/v_S_01_03_00"

    evtCAT: ESocial.EvtCat = field(
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
    class EvtCat(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar cat: CAT DESCRICAO_COMPLETA:Comunicação de Acidente de Trabalho - CAT. CHAVE_GRUPO: {dtAcid*},
            {hrAcid*}, {tpCat*}
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
        cat: ESocial.EvtCat.Cat = field(
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
        class Cat(CommonMixin):
            """
            :ivar dtAcid: Data do acidente. Validação: Deve ser uma data válida, igual ou anterior à data atual
                e igual ou posterior à data de admissão do trabalhador e à data de início da obrigatoriedade
                deste evento para o empregador no eSocial. Se {tpCat}(./tpCat) = [2, 3], deve ser informado
                valor igual ao preenchido no evento de CAT anterior, quando informado em
                {nrRecCatOrig}(./catOrigem_nrRecCatOrig).
            :ivar tpAcid:
            :ivar hrAcid: Hora do acidente, no formato HHMM. Validação: Preenchimento obrigatório se
                {tpAcid}(./tpAcid) = [1] ou se ({tpAcid}(./tpAcid) = [3] e {dtAcid}(./dtAcid) &gt;=
                [2022-01-26]). Não informar se {tpAcid}(./tpAcid) = [2]. Se preenchida, deve estar no intervalo
                entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos,
                que deve ser menor ou igual a 59. Se {tpCat}(./tpCat) = [2, 3], deve ser informado valor igual
                ao preenchido no evento de CAT anterior, quando informado em
                {nrRecCatOrig}(./catOrigem_nrRecCatOrig).
            :ivar hrsTrabAntesAcid: Horas trabalhadas antes da ocorrência do acidente, no formato HHMM.
                Validação: Preenchimento obrigatório se {tpAcid}(./tpAcid) = [1] ou se ({tpAcid}(./tpAcid) = [3]
                e {dtAcid}(./dtAcid) &gt;= [2022-07-20]). Não informar se {tpAcid}(./tpAcid) = [2]. Se
                preenchida, deve estar no intervalo entre [0000] e [9959], criticando inclusive a segunda parte
                do número, que indica os minutos, que deve ser menor ou igual a 59.
            :ivar tpCat:
            :ivar indCatObito: Houve óbito? Validação: Se o {tpCat}(./tpCat) for igual a [3], o campo deverá
                sempre ser preenchido com [S]. Se o {tpCat}(./tpCat) for igual a [2], o campo deverá sempre ser
                preenchido com [N].
            :ivar dtObito: Data do óbito. Validação: Deve ser uma data válida, igual ou posterior a
                {dtAcid}(./dtAcid) e igual ou anterior à data atual. Preenchimento obrigatório e exclusivo se
                {indCatObito}(./indCatObito) = [S].
            :ivar indComunPolicia: Houve comunicação à autoridade policial?
            :ivar codSitGeradora:
            :ivar iniciatCAT:
            :ivar obsCAT: Observação.
            :ivar ultDiaTrab: Último dia trabalhado. Validação: Preenchimento obrigatório se {dtAcid}(./dtAcid)
                &gt;= [2023-01-16]). Se informada, deve ser uma data igual ou anterior à data atual e igual ou
                posterior à data de admissão do trabalhador. Se {tpCat}(./tpCat) = [2], deve ser informada data
                posterior à data preenchida no evento de CAT anterior, quando informada em
                {nrRecCatOrig}(./catOrigem_nrRecCatOrig).
            :ivar houveAfast: Houve afastamento? Validação: Preenchimento obrigatório se {dtAcid}(./dtAcid)
                &gt;= [2023-01-16]).
            :ivar localAcidente: Local do acidente.
            :ivar parteAtingida: Parte do corpo atingida. DESCRICAO_COMPLETA:Detalhamento da parte atingida pelo
                acidente de trabalho.
            :ivar agenteCausador: Agente causador. DESCRICAO_COMPLETA:Detalhamento do agente causador do
                acidente de trabalho.
            :ivar atestado: Atestado médico.
            :ivar catOrigem: CAT de origem DESCRICAO_COMPLETA:Grupo que indica a CAT anterior, no caso de CAT de
                reabertura ou de comunicação de óbito. CHAVE_GRUPO: {nrRecCatOrig*} CONDICAO_GRUPO: O (se
                {tpCat}(../tpCat) for igual a [2, 3]); N (nos demais casos)
            """

            dtAcid: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            tpAcid: CatTpAcid = field(
                metadata={
                    "type": "Element",
                }
            )
            hrAcid: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            hrsTrabAntesAcid: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            tpCat: CatTpCat = field(
                metadata={
                    "type": "Element",
                }
            )
            indCatObito: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dtObito: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            indComunPolicia: str = field(
                metadata={
                    "type": "Element",
                }
            )
            codSitGeradora: str = field(
                metadata={
                    "type": "Element",
                    "pattern": r"\d{9}",
                }
            )
            iniciatCAT: CatIniciatCat = field(
                metadata={
                    "type": "Element",
                }
            )
            obsCAT: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            ultDiaTrab: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            houveAfast: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            localAcidente: ESocial.EvtCat.Cat.LocalAcidente = field(
                metadata={
                    "type": "Element",
                }
            )
            parteAtingida: ESocial.EvtCat.Cat.ParteAtingida = field(
                metadata={
                    "type": "Element",
                }
            )
            agenteCausador: ESocial.EvtCat.Cat.AgenteCausador = field(
                metadata={
                    "type": "Element",
                }
            )
            atestado: ESocial.EvtCat.Cat.Atestado = field(
                metadata={
                    "type": "Element",
                }
            )
            catOrigem: None | ESocial.EvtCat.Cat.CatOrigem = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class LocalAcidente(CommonMixin):
                """
                :ivar tpLocal:
                :ivar dscLocal: Especificação do local do acidente (pátio, rampa de acesso, posto de trabalho,
                    etc.).
                :ivar tpLograd:
                :ivar dscLograd:
                :ivar nrLograd:
                :ivar complemento:
                :ivar bairro:
                :ivar cep: Código de Endereçamento Postal - CEP. Validação: Preenchimento obrigatório se
                    {tpLocal}(./tpLocal) = [1, 3, 5]. Não preencher se {tpLocal}(./tpLocal) = [2]. Se
                    preenchido, deve ser informado apenas com números, com 8 (oito) posições.
                :ivar codMunic: Preencher com o código do município, conforme tabela do IBGE. Validação:
                    Preenchimento obrigatório se {tpLocal}(./tpLocal) = [1, 3, 4, 5]. Não preencher se
                    {tpLocal}(./tpLocal) = [2]. Se informado, deve ser um código válido e existente na tabela do
                    IBGE.
                :ivar uf: Preencher com a sigla da Unidade da Federação - UF. Validação: Preenchimento
                    obrigatório se {tpLocal}(./tpLocal) = [1, 3, 4, 5]. Não preencher se {tpLocal}(./tpLocal) =
                    [2].
                :ivar pais:
                :ivar codPostal: Código de Endereçamento Postal. Validação: Preenchimento obrigatório se
                    {tpLocal}(./tpLocal) = [2]. Não preencher nos demais casos.
                :ivar ideLocalAcid: Identificação do local onde ocorreu o acidente ou do estabelecimento ao qual
                    o trabalhador avulso está vinculado. CONDICAO_GRUPO: O ((se
                    {ideEmpregador/tpInsc}(2210_ideEmpregador_tpInsc) = [1] e {tpLocal}(../tpLocal) = [1, 3]) ou
                    (se o código de categoria no RET for igual a [2XX] e {dtAcid}(../../dtAcid) &gt;=
                    [2023-01-16])); OC (nos demais casos)
                """

                tpLocal: LocalAcidenteTpLocal = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dscLocal: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                tpLograd: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                dscLograd: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                nrLograd: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                complemento: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                bairro: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                cep: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                codMunic: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                uf: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                pais: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "length": 3,
                    },
                )
                codPostal: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                ideLocalAcid: None | ESocial.EvtCat.Cat.LocalAcidente.IdeLocalAcid = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class IdeLocalAcid(CommonMixin):
                    """
                    :ivar tpInsc:
                    :ivar nrInsc: Informar o número de inscrição do estabelecimento, de acordo com o tipo de
                        inscrição indicado no campo {ideLocalAcid/tpInsc}(./tpInsc). Se o acidente ou a doença
                        ocupacional ocorreu em local onde o trabalhador presta serviços, deve ser um número de
                        inscrição pertencente à contratante dos serviços. No caso de acidente de avulso com
                        {tpLocal}(../tpLocal) diferente de [1, 3], informar o estabelecimento ao qual o
                        trabalhador está vinculado. Validação: Deve ser compatível com o conteúdo do campo
                        {ideLocalAcid/tpInsc}(./tpInsc). Deve ser um identificador válido, constante das bases
                        da RFB, e: a) Se {tpLocal}(../tpLocal) = [1] ou (se o código de categoria no RET for
                        igual a [2XX] e {tpLocal}(../tpLocal) for diferente de [1, 3]), deve ser válido e
                        existente na Tabela de Estabelecimentos (S-1005); b) Se {tpLocal}(../tpLocal) = [3],
                        deve ser diferente dos estabelecimentos informados na Tabela S-1005 e, se
                        {ideLocalAcid/tpInsc}(./tpInsc) = [1], diferente do CNPJ base indicado em S-1000.
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
            class ParteAtingida(CommonMixin):
                codParteAting: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{9}",
                    }
                )
                lateralidade: ParteAtingidaLateralidade = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class AgenteCausador(CommonMixin):
                codAgntCausador: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{9}",
                    }
                )

            @dataclass(kw_only=True)
            class Atestado(CommonMixin):
                """
                :ivar dtAtendimento: Data do atendimento. Validação: Deve ser uma data igual ou posterior a
                    {dtAcid}(../dtAcid) e igual ou anterior à data atual.
                :ivar hrAtendimento: Hora do atendimento, no formato HHMM. Validação: Deve estar no intervalo
                    entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os
                    minutos, que deve ser menor ou igual a 59.
                :ivar indInternacao: Indicativo de internação.
                :ivar durTrat:
                :ivar indAfast: Indicativo de afastamento do trabalho durante o tratamento. Validação: Se o
                    campo {indCatObito}(../indCatObito) for igual a [S], o campo deve sempre ser preenchido com
                    [N].
                :ivar dscLesao:
                :ivar dscCompLesao:
                :ivar diagProvavel: Diagnóstico provável.
                :ivar codCID:
                :ivar observacao:
                :ivar emitente: Médico/Dentista que emitiu o atestado.
                """

                dtAtendimento: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                hrAtendimento: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                indInternacao: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                durTrat: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{1,4}",
                    }
                )
                indAfast: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dscLesao: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{9}",
                    }
                )
                dscCompLesao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 200,
                        "pattern": r"[^\s]{1}[\S\s]*",
                    },
                )
                diagProvavel: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                codCID: str = field(
                    metadata={
                        "type": "Element",
                        "min_length": 3,
                        "max_length": 4,
                    }
                )
                observacao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                emitente: ESocial.EvtCat.Cat.Atestado.Emitente = field(
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass(kw_only=True)
                class Emitente(CommonMixin):
                    """
                    :ivar nmEmit: Nome do médico/dentista que emitiu o atestado.
                    :ivar ideOC:
                    :ivar nrOC:
                    :ivar ufOC: Sigla da UF do órgão de classe. Validação: Preenchimento obrigatório se
                        {ideOC}(./ideOC) = [1, 2].
                    """

                    nmEmit: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    ideOC: EmitenteIdeOc = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    nrOC: str = field(
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 14,
                            "pattern": r".*[^\s].*",
                        }
                    )
                    ufOC: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

            @dataclass(kw_only=True)
            class CatOrigem(CommonMixin):
                """
                :ivar nrRecCatOrig: Informar o número do recibo da última CAT referente ao mesmo acidente/doença
                    relacionada ao trabalho, nos casos: a) de CAT de reabertura; b) de óbito, quando houver CAT
                    anterior. Validação: Deve corresponder ao número do recibo do arquivo relativo à última CAT
                    informada anteriormente, pertencente ao mesmo contrato, desde que
                    {indCatObito}(../indCatObito) da última CAT informada seja igual a [N]. O sistema não
                    efetuará a conferência da informação se {dtAcid}(../dtAcid) for anterior a
                    {sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf),
                    {transfDom/dtTransf}(2200_vinculo_transfDom_dtTransf) ou
                    {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF) do evento S-2200, ou se {dtAcid}(../dtAcid) for
                    anterior a {dtAltCPF}(2300_infoTSVInicio_mudancaCPF) do evento S-2300. OBS.: Quando a data
                    do acidente for anterior à data de obrigatoriedade do empregador ao envio deste evento, a
                    CAT de reabertura e/ou de óbito não devem ser informadas ao eSocial, mantendo-se o
                    procedimento realizado na emissão da CAT original.
                """

                nrRecCatOrig: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
