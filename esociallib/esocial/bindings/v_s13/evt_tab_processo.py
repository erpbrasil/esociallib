from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00"


class TDadosProcIndAutoria(Enum):
    """
    Indicativo da autoria da ação judicial.

    Validação: Preenchimento obrigatório se {tpProc}(1070_infoProcesso_inclusao_ideProcesso_tpProc) = [2].

    :cvar VALUE_1: Próprio contribuinte
    :cvar VALUE_2: Outra entidade, empresa ou empregado
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TDadosProcIndMatProc(Enum):
    """
    Indicativo da matéria do processo.

    :cvar VALUE_1: Exclusivamente tributária ou tributária e FGTS
    :cvar VALUE_7: Exclusivamente FGTS e/ou Contribuição Social Rescisória (Lei Complementar 110/2001)
    """

    VALUE_1 = 1
    VALUE_7 = 7


@dataclass(kw_only=True)
class TIdeProcesso(CommonMixin):
    """
    Identificação do processo e validade das informações DESCRICAO_COMPLETA:Identificação do processo e período de
    validade das informações.

    CHAVE_GRUPO: {tpProc*}, {nrProc*}, {iniValid*}, {fimValid*}.

    :ivar tpProc:
    :ivar nrProc: Informar o número do processo administrativo/judicial de acordo com o tipo informado em
        {tpProc}(./tpProc). Validação: Deve ser um número de processo válido e: a) Se {tpProc}(./tpProc) = [1],
        deve possuir 17 (dezessete) ou 21 (vinte e um) algarismos; b) Se {tpProc}(./tpProc) = [2], deve possuir
        20 (vinte) algarismos; c) Se {tpProc}(./tpProc) = [4], deve possuir 16 (dezesseis) algarismos.
    :ivar iniValid:
    :ivar fimValid:
    """

    class Meta:
        name = "T_ideProcesso"

    tpProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
        }
    )
    nrProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
        }
    )
    iniValid: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
        }
    )
    fimValid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
        },
    )


class InfoSuspIndSusp(Enum):
    """
    Indicativo de suspensão da exigibilidade.

    Validação: Se {tpProc}(1070_infoProcesso_inclusao_ideProcesso_tpProc) = [1], deve ser preenchido com [03, 14,
    92]. Se {tpProc}(1070_infoProcesso_inclusao_ideProcesso_tpProc) = [2], deve ser preenchido com [01, 02, 04, 05,
    08, 09, 10, 11, 12, 13, 90, 92]. Se {tpProc}(1070_infoProcesso_inclusao_ideProcesso_tpProc) = [4], deve ser
    preenchido com [14].

    :cvar VALUE_01: Liminar em mandado de segurança
    :cvar VALUE_02: Depósito judicial do montante integral
    :cvar VALUE_03: Depósito administrativo do montante integral
    :cvar VALUE_04: Antecipação de tutela
    :cvar VALUE_05: Liminar em medida cautelar
    :cvar VALUE_08: Sentença em mandado de segurança favorável ao contribuinte
    :cvar VALUE_09: Sentença em ação ordinária favorável ao contribuinte e confirmada pelo TRF
    :cvar VALUE_10: Acórdão do TRF favorável ao contribuinte
    :cvar VALUE_11: Acórdão do STJ em recurso especial favorável ao contribuinte
    :cvar VALUE_12: Acórdão do STF em recurso extraordinário favorável ao contribuinte
    :cvar VALUE_13: Sentença 1ª instância não transitada em julgado com efeito suspensivo
    :cvar VALUE_14: Contestação administrativa FAP
    :cvar VALUE_90: Decisão definitiva a favor do contribuinte
    :cvar VALUE_92: Sem suspensão da exigibilidade
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_90 = "90"
    VALUE_92 = "92"


@dataclass(kw_only=True)
class TDadosProc(CommonMixin):
    """
    Dados do processo.

    :ivar indAutoria:
    :ivar indMatProc:
    :ivar observacao: Observações relacionadas ao processo.
    :ivar dadosProcJud: Informações complementares do processo judicial. CONDICAO_GRUPO: O (se
        {tpProc}(1070_infoProcesso_inclusao_ideProcesso_tpProc) = [2] e
        {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) = [1]); N (nos demais casos)
    :ivar infoSusp: Informações de suspensão de exigibilidade de tributos DESCRICAO_COMPLETA:Informações de
        suspensão de exigibilidade de tributos em virtude de processo administrativo ou judicial. CHAVE_GRUPO:
        {codSusp} CONDICAO_GRUPO: O (se {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) = [1]); N
        (nos demais casos)
    """

    class Meta:
        name = "T_dadosProc"

    indAutoria: None | TDadosProcIndAutoria = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
        },
    )
    indMatProc: TDadosProcIndMatProc = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
        }
    )
    observacao: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
        },
    )
    dadosProcJud: None | TDadosProc.DadosProcJud = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
        },
    )
    infoSusp: list[TDadosProc.InfoSusp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
            "max_occurs": 99,
        },
    )

    @dataclass(kw_only=True)
    class DadosProcJud(CommonMixin):
        """
        :ivar ufVara: Identificação da Unidade da Federação - UF da Seção Judiciária.
        :ivar codMunic:
        :ivar idVara:
        """

        ufVara: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
            }
        )
        codMunic: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
            }
        )
        idVara: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
                "pattern": r"\d{1,4}",
            }
        )

    @dataclass(kw_only=True)
    class InfoSusp(CommonMixin):
        """
        :ivar codSusp: Código do indicativo da suspensão, atribuído pelo empregador.
        :ivar indSusp:
        :ivar dtDecisao: Data da decisão, sentença ou despacho administrativo.
        :ivar indDeposito: Indicativo de depósito do montante integral. Validação: Se
            {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) = [90], preencher obrigatoriamente
            com [N]. Se {indSusp}(1070_infoProcesso_inclusao_dadosProc_infoSusp_indSusp) = [02, 03] preencher
            obrigatoriamente com [S].
        """

        codSusp: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
            }
        )
        indSusp: InfoSuspIndSusp = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
            }
        )
        dtDecisao: XmlDate = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
            }
        )
        indDeposito: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00",
            }
        )


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1070 - Tabela de Processos Administrativos/Judiciais.

    :ivar evtTabProcesso: Evento Tabela de Processos DESCRICAO_COMPLETA:Evento Tabela de Processos
        Administrativos/Judiciais. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_PERMITE_ALT_EXCL_CODSUSP
        REGRA:REGRA_TABGERAL_ALTERACAO_PERIODO_CONFLITANTE REGRA:REGRA_TABGERAL_EXISTE_REGISTRO_ALTERADO
        REGRA:REGRA_TABGERAL_EXISTE_REGISTRO_EXCLUIDO REGRA:REGRA_TABGERAL_INCLUSAO_PERIODO_CONFLITANTE
        REGRA:REGRA_TAB_PERMITE_EXCLUSAO REGRA:REGRA_VALIDA_DT_FUTURA REGRA:REGRA_VALIDA_PROCESSO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTabProcesso/v_S_01_03_00"

    evtTabProcesso: ESocial.EvtTabProcesso = field(
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
    class EvtTabProcesso(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoProcesso: Informações do processo.
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
        infoProcesso: ESocial.EvtTabProcesso.InfoProcesso = field(
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
            :ivar inclusao: Inclusão de novas informações. CONDICAO_GRUPO: OC
            :ivar alteracao: Alteração das informações. CONDICAO_GRUPO: OC
            :ivar exclusao: Exclusão das informações. CONDICAO_GRUPO: OC
            """

            inclusao: None | ESocial.EvtTabProcesso.InfoProcesso.Inclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            alteracao: None | ESocial.EvtTabProcesso.InfoProcesso.Alteracao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            exclusao: None | ESocial.EvtTabProcesso.InfoProcesso.Exclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Inclusao(CommonMixin):
                ideProcesso: TIdeProcesso = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dadosProc: TDadosProc = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Alteracao(CommonMixin):
                ideProcesso: TIdeProcesso = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dadosProc: TDadosProc = field(
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
                ideProcesso: TIdeProcesso = field(
                    metadata={
                        "type": "Element",
                    }
                )
