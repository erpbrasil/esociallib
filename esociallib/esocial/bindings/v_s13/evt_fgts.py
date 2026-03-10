from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtFGTS/v_S_01_03_00"


class BasePerApurTpValor(Enum):
    """
    Tipo de valor que influi na apuração do FGTS.

    Validação: Se o evento de origem for S-5003, deve corresponder ao valor informado no campo
    {tpValor}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_basePerApur_tpValor) desse evento. Se o
    evento de origem for S-1270, deve ser retornado [19].

    :cvar VALUE_11: FGTS mensal
    :cvar VALUE_12: FGTS 13° salário
    :cvar VALUE_13: FGTS (período anterior) mensal
    :cvar VALUE_14: FGTS (período anterior) 13º salário
    :cvar VALUE_15: FGTS mensal - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_16: FGTS 13° salário - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_17: FGTS (período anterior) mensal - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_18: FGTS (período anterior) 13º salário - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_19: FGTS - Avulsos não portuários
    :cvar VALUE_21: FGTS mês da rescisão
    :cvar VALUE_22: FGTS 13° salário rescisório
    :cvar VALUE_23: FGTS aviso prévio indenizado
    :cvar VALUE_24: FGTS (período anterior) mês da rescisão
    :cvar VALUE_25: FGTS (período anterior) 13º salário rescisório
    :cvar VALUE_26: FGTS (período anterior) aviso prévio indenizado
    :cvar VALUE_27: FGTS mês da rescisão - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_28: FGTS 13° salário rescisório - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_29: FGTS aviso prévio indenizado - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_30: FGTS (período anterior) mês da rescisão - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_31: FGTS (período anterior) 13° salário rescisório - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_32: FGTS (período anterior) aviso prévio indenizado - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_41: FGTS mensal - Indenização compensatória do empregado doméstico
    :cvar VALUE_42: FGTS 13° salário - Indenização compensatória do empregado doméstico
    :cvar VALUE_43: FGTS (período anterior) mensal - Indenização compensatória do empregado doméstico
    :cvar VALUE_44: FGTS (período anterior) 13º salário - Indenização compensatória do empregado doméstico
    :cvar VALUE_45: FGTS mês da rescisão - Indenização compensatória do empregado doméstico
    :cvar VALUE_46: FGTS 13° salário rescisório - Indenização compensatória do empregado doméstico
    :cvar VALUE_47: FGTS aviso prévio indenizado - Indenização compensatória do empregado doméstico
    :cvar VALUE_48: FGTS (período anterior) mês da rescisão - Indenização compensatória do empregado doméstico
    :cvar VALUE_49: FGTS (período anterior) 13º salário rescisório - Indenização compensatória do empregado
        doméstico
    :cvar VALUE_50: FGTS (período anterior) aviso prévio indenizado - Indenização compensatória do empregado
        doméstico
    """

    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
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
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_50 = 50


class InfoFgtsIndExistInfo(Enum):
    """
    Indicativo de existência de FGTS.

    :cvar VALUE_1: Há informações de FGTS
    :cvar VALUE_2: Há movimento, porém não há informações de FGTS
    :cvar VALUE_3: Não há movimento no período informado em {perApur}(5013_ideEvento_perApur)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-5013 - Informações do FGTS Consolidadas por Contribuinte.

    :ivar evtFGTS: Evento Informações do FGTS Consolidadas por Contribuinte. CHAVE_GRUPO: {Id}
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtFGTS/v_S_01_03_00"

    evtFGTS: ESocial.EvtFgts = field(
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
    class EvtFgts(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoFGTS: Informações relativas ao FGTS DESCRICAO_COMPLETA:Informações relativas ao Fundo de
            Garantia do Tempo de Serviço - FGTS.
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
        infoFGTS: ESocial.EvtFgts.InfoFgts = field(
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
        class InfoFgts(CommonMixin):
            """
            :ivar nrRecArqBase:
            :ivar indExistInfo:
            :ivar ideEstab: Identificação do estabelecimento DESCRICAO_COMPLETA:Identificação do estabelecimento
                ou obra de construção civil. CHAVE_GRUPO: {tpInsc}, {nrInsc} CONDICAO_GRUPO: OC
            """

            nrRecArqBase: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indExistInfo: InfoFgtsIndExistInfo = field(
                metadata={
                    "type": "Element",
                }
            )
            ideEstab: list[ESocial.EvtFgts.InfoFgts.IdeEstab] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class IdeEstab(CommonMixin):
                """
                :ivar tpInsc:
                :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideEstab/tpInsc}(./tpInsc). Evento de origem: S-1270 ou S-5003.
                :ivar ideLotacao: Identificação da lotação tributária. CHAVE_GRUPO: {codLotacao}, {tpLotacao},
                    {tpInsc}, {nrInsc}
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
                ideLotacao: list[ESocial.EvtFgts.InfoFgts.IdeEstab.IdeLotacao] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                    },
                )

                @dataclass(kw_only=True)
                class IdeLotacao(CommonMixin):
                    """
                    :ivar codLotacao: Informar o código atribuído pelo empregador para a lotação tributária.
                        Evento de origem: S-1270 ou S-5003.
                    :ivar tpLotacao: Preencher com o código correspondente ao tipo de lotação, conforme Tabela
                        10. Evento de origem: S-1020 ou S-5003.
                    :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela
                        05. Evento de origem: S-1020 ou S-5003.
                    :ivar nrInsc: Preencher com o número de inscrição (CNPJ, CPF, CNO) ao qual pertence a
                        lotação tributária, conforme indicado na Tabela 10. Evento de origem: S-1020 ou S-5003.
                    :ivar infoBaseFGTS: Bases de cálculo e valores do FGTS DESCRICAO_COMPLETA:Informações
                        referentes a bases de cálculo e valores do FGTS no estabelecimento/lotação.
                        CONDICAO_GRUPO: OC
                    """

                    codLotacao: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    tpLotacao: str = field(
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
                    infoBaseFGTS: None | ESocial.EvtFgts.InfoFgts.IdeEstab.IdeLotacao.InfoBaseFgts = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoBaseFgts(CommonMixin):
                        """
                        :ivar basePerApur: Bases de cálculo e valores do FGTS, exceto se {tpAcConv} = [E, H, I]
                            DESCRICAO_COMPLETA:Informações consolidadas das bases de cálculo e valores do FGTS
                            do período de apuração e de períodos anteriores, exceto se {tpAcConv} = [E, H, I].
                            Evento de origem: S-1270 ou S-5003. CHAVE_GRUPO: {tpValor}, {indIncid}, {notAFT},
                            {natRubr} CONDICAO_GRUPO: OC
                        :ivar infoBasePerAntE: Informações sobre bases de cálculo e valores do FGTS, quando
                            {tpAcConv}(5013_infoFGTS_ideEstab_ideLotacao_infoBaseFGTS_infoBasePerAntE_tpAcConv)
                            = [E, H, I] DESCRICAO_COMPLETA:Informações referentes a bases de cálculo e valores
                            do FGTS de períodos anteriores quando {tpAcConv}(./tpAcConv) = [E, H, I]. Evento de
                            origem: S-5003. CHAVE_GRUPO: {perRef}, {tpAcConv} CONDICAO_GRUPO: OC
                        """

                        basePerApur: list[ESocial.EvtFgts.InfoFgts.IdeEstab.IdeLotacao.InfoBaseFgts.BasePerApur] = (
                            field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 99,
                                },
                            )
                        )
                        infoBasePerAntE: list[
                            ESocial.EvtFgts.InfoFgts.IdeEstab.IdeLotacao.InfoBaseFgts.InfoBasePerAntE
                        ] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 180,
                            },
                        )

                        @dataclass(kw_only=True)
                        class BasePerApur(CommonMixin):
                            """
                            :ivar tpValor:
                            :ivar indIncid: Indicativo de incidência de FGTS. Validação: Se {tpValor}(./tpValor)
                                for diferente de [19], deve corresponder ao valor informado no campo
                                {indIncid}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_basePerApur_indIncid)
                                do evento S-5003. Se {tpValor}(./tpValor) = [19], deve ser retornado [1].
                            :ivar baseFGTS: Remuneração (valor da base de cálculo) do FGTS. Validação: Deve ser
                                maior que 0 (zero). Se {tpValor}(./tpValor) for diferente de [19], deve
                                corresponder ao somatório dos valores informados no campo
                                {remFGTS}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_basePerApur_remFGTS)
                                do evento S-5003, agrupados por {tpValor}(./tpValor) e {indIncid}(./indIncid).
                                Se {tpValor}(./tpValor) = [19], deve corresponder à remuneração dos
                                trabalhadores avulsos não portuários contratados, conforme informado no campo
                                {vrBcFGTS}(1270_remunAvNP_vrBcFgts) do evento S-1270.
                            :ivar vrFGTS: Valor histórico do FGTS a ser depositado na conta vinculada do
                                trabalhador. Validação: Deve ser maior que 0 (zero). Se {tpValor}(./tpValor) for
                                diferente de [19], deve corresponder ao somatório dos valores informados no
                                campo
                                {dpsFGTS}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_basePerApur_dpsFGTS)
                                do evento S-5003, agrupados por {tpValor}(./tpValor). Se {tpValor}(./tpValor) =
                                [19], deve corresponder ao somatório dos valores informados no campo
                                {baseFGTS}(./baseFGTS), e aplicar a alíquota de 8%.
                            :ivar notAFT: Número da notificação de FGTS que deu origem à confissão. Evento de
                                origem: S-5003.
                            :ivar natRubr: Informar o código de classificação da rubrica. Evento de origem:
                                S-5003.
                            """

                            tpValor: BasePerApurTpValor = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            indIncid: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            baseFGTS: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrFGTS: None | str = field(
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
                            natRubr: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )

                        @dataclass(kw_only=True)
                        class InfoBasePerAntE(CommonMixin):
                            """
                            :ivar perRef: Informar o período ao qual se refere a remuneração no formato AAAA-MM.
                                Validação: Deve corresponder ao período informado no evento de origem.
                            :ivar tpAcConv:
                            :ivar basePerAntE: Bases de cálculo e valores do FGTS, quando
                                {tpAcConv}(5013_infoFGTS_ideEstab_ideLotacao_infoBaseFGTS_infoBasePerAntE_tpAcConv)
                                = [E, H, I] DESCRICAO_COMPLETA:Informações consolidadas das bases de cálculo e
                                valores do FGTS de períodos anteriores quando {tpAcConv}(../tpAcConv) = [E, H,
                                I]. CHAVE_GRUPO: {tpValorE}, {indIncidE}
                            """

                            perRef: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            tpAcConv: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            basePerAntE: list[
                                ESocial.EvtFgts.InfoFgts.IdeEstab.IdeLotacao.InfoBaseFgts.InfoBasePerAntE.BasePerAntE
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "min_occurs": 1,
                                    "max_occurs": 99,
                                },
                            )

                            @dataclass(kw_only=True)
                            class BasePerAntE(CommonMixin):
                                """
                                :ivar tpValorE: Tipo de valor que influi na apuração do FGTS. Validação: Deve
                                    corresponder ao valor informado no campo
                                    {tpValorE}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_infoBasePerAntE_basePerAntE_tpValorE)
                                    do evento de origem.
                                :ivar indIncidE: Indicativo de incidência de FGTS. Validação: Deve corresponder
                                    ao valor informado no campo
                                    {indIncidE}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_infoBasePerAntE_basePerAntE_indIncidE)
                                    do evento de origem.
                                :ivar baseFGTSE: Remuneração (valor da base de cálculo) do FGTS. Validação: Deve
                                    ser maior que 0 (zero). Deve corresponder ao somatório dos valores
                                    informados no campo
                                    {remFGTSE}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_infoBasePerAntE_basePerAntE_remFGTSE)
                                    do evento de origem, agrupados por {tpValorE}(./tpValorE) e
                                    {indIncidE}(./indIncidE).
                                :ivar vrFGTSE: Valor histórico do FGTS a ser depositado na conta vinculada do
                                    trabalhador. Validação: Deve ser maior que 0 (zero). Deve corresponder ao
                                    somatório dos valores informados no campo
                                    {dpsFGTSE}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_infoBasePerAntE_basePerAntE_dpsFGTSE)
                                    do evento de origem, agrupados por {tpValorE}(./tpValorE).
                                """

                                tpValorE: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                indIncidE: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                baseFGTSE: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                vrFGTSE: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
