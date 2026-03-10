from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtAfastTemp/v_S_01_03_00"


class InfoCessaoInfOnus(Enum):
    """
    Ônus da cessão/requisição.

    :cvar VALUE_1: Ônus do cedente
    :cvar VALUE_2: Ônus do cessionário
    :cvar VALUE_3: Ônus do cedente e cessionário
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoMandSindInfOnusRemun(Enum):
    """
    Ônus da remuneração.

    :cvar VALUE_1: Apenas do empregador
    :cvar VALUE_2: Apenas do sindicato
    :cvar VALUE_3: Parte do empregador, sendo a diferença e/ou complementação salarial paga pelo sindicato
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoRetifOrigRetif(Enum):
    """
    Origem da retificação.

    :cvar VALUE_1: Por iniciativa do empregador
    :cvar VALUE_2: Revisão administrativa
    :cvar VALUE_3: Determinação judicial
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoRetifTpProc(Enum):
    """
    Preencher com o código correspondente ao tipo de processo.

    Validação: O preenchimento é obrigatório se {origRetif}(./origRetif) = [2, 3].

    :cvar VALUE_1: Administrativo
    :cvar VALUE_2: Judicial
    :cvar VALUE_3: Número de Benefício - NB do INSS
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class IniAfastamentoTpAcidTransito(Enum):
    """
    Tipo de acidente de trânsito.

    Validação: Somente pode ser preenchido se {codMotAfast}(./codMotAfast) = [01, 03].

    :cvar VALUE_1: Atropelamento
    :cvar VALUE_2: Colisão
    :cvar VALUE_3: Outros
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2230 - Afastamento Temporário.

    :ivar evtAfastTemp: Evento Afastamento Temporário. CHAVE_GRUPO: {Id} REGRA:REGRA_AFASTAMENTO
        REGRA:REGRA_EMPREGADO_DOMESTICO REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EVENTO_EXT_SEM_IMPACTO_FOPAG REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO
        REGRA:REGRA_EXCLUI_EVENTO_AFASTAMENTO REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXTEMP_DOMESTICO
        REGRA:REGRA_EXTEMP_REINTEGRACAO REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_TSV_ATIVO_NA_DTEVENTO
        REGRA:REGRA_VINCULO_ATIVO_NA_DTEVENTO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtAfastTemp/v_S_01_03_00"

    evtAfastTemp: ESocial.EvtAfastTemp = field(
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
    class EvtAfastTemp(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo: Informações de identificação do trabalhador e do vínculo. CHAVE_GRUPO: {cpfTrab*},
            {matricula*}, {codCateg*}
        :ivar infoAfastamento: Informações do afastamento temporário.
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
        ideVinculo: ESocial.EvtAfastTemp.IdeVinculo = field(
            metadata={
                "type": "Element",
            }
        )
        infoAfastamento: ESocial.EvtAfastTemp.InfoAfastamento = field(
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
        class IdeVinculo(CommonMixin):
            """
            :ivar cpfTrab:
            :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
                matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve
                corresponder à matrícula informada pelo empregador no evento S-2200 ou S-2300 do respectivo
                contrato. Não preencher no caso de Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE sem
                informação de matrícula no evento S-2300.
            :ivar codCateg: Preencher com o código da categoria do trabalhador. Informar somente no caso de TSVE
                sem informação de matrícula no evento S-2300. Validação: Informação obrigatória e exclusiva se
                não houver preenchimento de {matricula}(./matricula). Se informado, deve ser um código válido e
                existente na Tabela 01.
            """

            cpfTrab: str = field(
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
            codCateg: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class InfoAfastamento(CommonMixin):
            """
            :ivar iniAfastamento: Informações de início do afastamento. CHAVE_GRUPO: {dtIniAfast*}
                CONDICAO_GRUPO: O (se não for preenchido o grupo {fimAfastamento}(../fimAfastamento)); OC (nos
                demais casos)
            :ivar infoRetif: Informações de retificação do afastamento DESCRICAO_COMPLETA:Informações de
                retificação do afastamento temporário. Preenchimento obrigatório caso
                {codMotAfast}(../iniAfastamento_codMotAfast) seja retificado de [01] para [03] ou de [03] para
                [01]. CONDICAO_GRUPO: OC ((se {indRetif}(2230_ideEvento_indRetif) = [2]) E (o grupo
                {iniAfastamento}(../iniAfastamento) estiver preenchido); N (nos demais casos)
            :ivar fimAfastamento: Informação do término do afastamento. CHAVE_GRUPO: {dtTermAfast*}
                CONDICAO_GRUPO: O (se não for preenchido o grupo {iniAfastamento}(../iniAfastamento)); OC (nos
                demais casos) REGRA:REGRA_EXISTE_EVENTO_AFASTAMENTO
            """

            iniAfastamento: None | ESocial.EvtAfastTemp.InfoAfastamento.IniAfastamento = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoRetif: None | ESocial.EvtAfastTemp.InfoAfastamento.InfoRetif = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            fimAfastamento: None | ESocial.EvtAfastTemp.InfoAfastamento.FimAfastamento = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class IniAfastamento(CommonMixin):
                """
                :ivar dtIniAfast: Data de início do afastamento. Validação: Deve-se obedecer às seguintes
                    regras: a) Não pode ser posterior à data atual, exceto se: a1) {codMotAfast}(./codMotAfast)
                    = [15] (férias), situação em que pode ser até 60 dias posterior à data atual; a2)
                    {codMotAfast}(./codMotAfast) = [18], situação em que pode ser até 120 dias posterior à data
                    atual; b) É necessário que o trabalhador esteja, antes da data de início do afastamento, em
                    atividade, ou seja, não pode existir evento de afastamento anterior a
                    {dtIniAfast}(./dtIniAfast) sem que este tenha sido encerrado.
                :ivar codMotAfast:
                :ivar infoMesmoMtv: Informar se o afastamento decorre da mesma doença que gerou o afastamento
                    anterior ({codMotAfast}(./codMotAfast) = [01, 03]), dentro de 60 dias.
                :ivar tpAcidTransito:
                :ivar observacao: Detalhar as informações sobre o afastamento do trabalhador, de maneira a
                    explicitar os motivos do mesmo. Validação: O preenchimento é obrigatório se
                    {codMotAfast}(./codMotAfast) = [21].
                :ivar perAquis: Período aquisitivo de férias DESCRICAO_COMPLETA:Informações referentes ao
                    período aquisitivo de férias. CONDICAO_GRUPO: O (se {codMotAfast}(../codMotAfast) = [15] E
                    (o código de categoria no RET for igual a [1XX, 301, 302, 303, 304, 306, 307, 309, 310, 312,
                    410] com {tpRegTrab} em S-2200/S-2300 = [1] OU o código de categoria no RET for igual a
                    [401] com {tpRegTrab}(2300_infoTSVInicio_infoComplementares_infoDirigenteSindical_tpRegTrab)
                    em S-2300 = [1] ou não informado) E {dtIniAfast}(../dtIniAfast) &gt;= [2021-07-19]); N (nos
                    demais casos)
                :ivar infoCessao: Informações complementares - Cessão/Requisição de trabalhador. CONDICAO_GRUPO:
                    O (se {codMotAfast}(../codMotAfast) = [14]); N (nos demais casos)
                :ivar infoMandSind: Informações complementares - Afastamento para exercício de mandato sindical.
                    CONDICAO_GRUPO: O (se {codMotAfast}(../codMotAfast) = [24]); N (nos demais casos)
                :ivar infoMandElet: Informações complementares - Afastamento para exercício de mandato eletivo.
                    CONDICAO_GRUPO: O (se {codMotAfast}(../codMotAfast) = [22] e se a natureza jurídica do
                    declarante for igual a 1XX-X, 201-1 ou 203-8); N (nos demais casos)
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
                infoMesmoMtv: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                tpAcidTransito: None | IniAfastamentoTpAcidTransito = field(
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
                perAquis: None | ESocial.EvtAfastTemp.InfoAfastamento.IniAfastamento.PerAquis = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoCessao: None | ESocial.EvtAfastTemp.InfoAfastamento.IniAfastamento.InfoCessao = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoMandSind: None | ESocial.EvtAfastTemp.InfoAfastamento.IniAfastamento.InfoMandSind = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoMandElet: None | ESocial.EvtAfastTemp.InfoAfastamento.IniAfastamento.InfoMandElet = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class PerAquis(CommonMixin):
                    """
                    :ivar dtInicio: Data de início do período aquisitivo de férias. Validação: Deve observar o
                        que segue: a) Se o código de categoria no Registro de Eventos Trabalhistas - RET for
                        diferente de [304, 410], deve ser igual ou posterior a
                        {dtAdm}(2200_vinculo_infoRegimeTrab_infoCeletista_dtAdm); b) Se o código de categoria no
                        RET for igual a [304], deve ser igual ou posterior a
                        {dtExercOrig}(2300_infoTSVInicio_infoComplementares_infoMandElet_dtExercOrig); c) Se o
                        código de categoria no RET for igual a [410], deve ser igual ou posterior a
                        {dtAdmCed}(2300_infoTSVInicio_infoComplementares_infoTrabCedido_dtAdmCed).
                    :ivar dtFim: Data de término do período aquisitivo de férias. É necessário informar o campo
                        somente se o período aquisitivo for diferente de 1 ano. Validação: Se informada, deve
                        ser uma data posterior a {dtInicio}(./dtInicio).
                    """

                    dtInicio: XmlDate = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtFim: None | XmlDate = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class InfoCessao(CommonMixin):
                    """
                    :ivar cnpjCess: Preencher com o CNPJ do órgão/entidade para o qual o trabalhador foi
                        cedido/requisitado. Validação: Deve ser um CNPJ diferente do CNPJ do empregador e
                        diferente dos estabelecimentos informados através do evento S-1005.
                        REGRA:REGRA_VALIDA_CNPJ
                    :ivar infOnus:
                    """

                    cnpjCess: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    infOnus: InfoCessaoInfOnus = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoMandSind(CommonMixin):
                    """
                    :ivar cnpjSind: CNPJ do sindicato no qual o trabalhador exercerá o mandato. Validação: Deve
                        ser um CNPJ diferente do CNPJ base do empregador e diferente dos informados na Tabela de
                        Estabelecimentos (S-1005). REGRA:REGRA_VALIDA_CNPJ
                    :ivar infOnusRemun:
                    """

                    cnpjSind: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    infOnusRemun: InfoMandSindInfOnusRemun = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoMandElet(CommonMixin):
                    """
                    :ivar cnpjMandElet: CNPJ do órgão no qual o trabalhador exercerá o mandato eletivo.
                        REGRA:REGRA_VALIDA_CNPJ
                    :ivar indRemunCargo: Indicar se o servidor optou pela remuneração do cargo efetivo.
                        Validação: Informação obrigatória e exclusiva se o código de categoria no Registro de
                        Eventos Trabalhistas - RET for igual a [301].
                    """

                    cnpjMandElet: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    indRemunCargo: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

            @dataclass(kw_only=True)
            class InfoRetif(CommonMixin):
                origRetif: InfoRetifOrigRetif = field(
                    metadata={
                        "type": "Element",
                    }
                )
                tpProc: None | InfoRetifTpProc = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                nrProc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{10}|\d{17}|\d{20}|\d{21}",
                    },
                )

            @dataclass(kw_only=True)
            class FimAfastamento(CommonMixin):
                """
                :ivar dtTermAfast: Preencher com a data do término do afastamento do trabalhador. Validação:
                    Deve ser igual ou posterior à data de início do afastamento do trabalhador e anterior a
                    [9999-12-31].
                """

                dtTermAfast: XmlDate = field(
                    metadata={
                        "type": "Element",
                        "max_exclusive": XmlDate(9999, 12, 31),
                    }
                )
