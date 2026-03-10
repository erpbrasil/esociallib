from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtComProd/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1260 - Comercialização da Produção Rural Pessoa Física.

    :ivar evtComProd: Evento Comercialização da Produção Rural Pessoa Física. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVE_FOPAG_COMERC_PROD
        REGRA:REGRA_EVE_FOPAG_IND_RETIFICACAO REGRA:REGRA_EVE_FOPAG_INFO_COMPAT_CLASSTRIB
        REGRA:REGRA_EVE_FOPAG_PERMITE_EXCLUSAO REGRA:REGRA_EVE_FOPAG_SIMPLIFICADO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtComProd/v_S_01_03_00"

    evtComProd: ESocial.EvtComProd = field(
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
    class EvtComProd(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador: Informações de identificação do empregador. CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar infoComProd: Informação da comercialização de produção.
        :ivar Id:
        """

        ideEvento: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: ESocial.EvtComProd.IdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        infoComProd: ESocial.EvtComProd.InfoComProd = field(
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
        class IdeEmpregador(CommonMixin):
            """
            :ivar tpInsc:
            :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição
                indicado no campo {ideEmpregador/tpInsc}(./tpInsc) e conforme informado em S-1000.
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
        class InfoComProd(CommonMixin):
            """
            :ivar ideEstabel: Identificação do estabelecimento que comercializou a produção. CHAVE_GRUPO:
                {nrInscEstabRural*}
            """

            ideEstabel: ESocial.EvtComProd.InfoComProd.IdeEstabel = field(
                metadata={
                    "type": "Element",
                }
            )

            @dataclass(kw_only=True)
            class IdeEstabel(CommonMixin):
                """
                :ivar nrInscEstabRural:
                :ivar tpComerc: Valor total da comercialização por "tipo" de comercialização. CHAVE_GRUPO:
                    {indComerc}
                """

                nrInscEstabRural: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{14}",
                    }
                )
                tpComerc: list[ESocial.EvtComProd.InfoComProd.IdeEstabel.TpComerc] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 5,
                    },
                )

                @dataclass(kw_only=True)
                class TpComerc(CommonMixin):
                    """
                    :ivar indComerc: Indicativo de comercialização.
                    :ivar vrTotCom: Preencher com o valor total da comercialização. Validação: Deve ser maior
                        que 0 (zero).
                    :ivar ideAdquir: Identificação dos adquirentes da produção. CHAVE_GRUPO: {tpInsc}, {nrInsc}
                        CONDICAO_GRUPO: F (se {indComerc}(../indComerc) = [3, 7, 8]); N (nos demais casos)
                    :ivar infoProcJud: Informação de processos judiciais DESCRICAO_COMPLETA:Informações de
                        processos judiciais com decisão/sentença favorável ao contribuinte e relativos à
                        contribuição incidente sobre a comercialização. CHAVE_GRUPO: {tpProc}, {nrProc},
                        {codSusp} CONDICAO_GRUPO: OC
                    """

                    indComerc: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrTotCom: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    ideAdquir: list[ESocial.EvtComProd.InfoComProd.IdeEstabel.TpComerc.IdeAdquir] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 9999,
                        },
                    )
                    infoProcJud: list[ESocial.EvtComProd.InfoComProd.IdeEstabel.TpComerc.InfoProcJud] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 10,
                        },
                    )

                    @dataclass(kw_only=True)
                    class IdeAdquir(CommonMixin):
                        """
                        :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme
                            Tabela 05. Validação: Se {indComerc}(../indComerc) for igual a [3, 7], deve ser
                            igual a [1, 2]. Se {indComerc}(../indComerc) for igual a [8], deve ser igual a [1].
                        :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de
                            inscrição indicado no campo {ideAdquir/tpInsc}(./tpInsc). Validação: A inscrição
                            informada deve ser compatível com o {ideAdquir/tpInsc}(./tpInsc) e diferente da
                            inscrição do declarante.
                        :ivar vrComerc: Valor bruto da comercialização da produção. Validação: Deve ser maior
                            que 0 (zero).
                        :ivar nfs: Notas fiscais da aquisição de produção DESCRICAO_COMPLETA:Detalhamento das
                            notas fiscais relativas à comercialização de produção com o adquirente identificado
                            no grupo superior. CHAVE_GRUPO: {serie}, {nrDocto} CONDICAO_GRUPO: F
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
                        vrComerc: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        nfs: list[ESocial.EvtComProd.InfoComProd.IdeEstabel.TpComerc.IdeAdquir.Nfs] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 999,
                            },
                        )

                        @dataclass(kw_only=True)
                        class Nfs(CommonMixin):
                            """
                            :ivar serie:
                            :ivar nrDocto:
                            :ivar dtEmisNF: Data de emissão da nota fiscal/fatura. Validação: O mês/ano da
                                emissão da nota fiscal deve ser igual ao mês/ano indicado no registro de
                                abertura do arquivo.
                            :ivar vlrBruto: Preencher com o valor bruto da(s) nota(s) fiscal(is).
                            :ivar vrCPDescPR: Preencher com o valor da contribuição previdenciária descontada
                                pelo adquirente na comercialização de produção. Se não houver informação,
                                preencher com 0 (zero).
                            :ivar vrRatDescPR: Valor da contribuição destinada ao financiamento dos benefícios
                                concedidos em razão do grau de incidência da incapacidade laborativa decorrente
                                dos riscos ambientais do trabalho, incidente sobre a comercialização de produção
                                rural de produtor rural. Se não houver informação, preencher com 0 (zero).
                            :ivar vrSenarDesc: Valor da contribuição destinada ao SENAR, incidente sobre a
                                comercialização de produção rural de produtor rural pessoa física/segurado
                                especial. Se não houver informação, preencher com 0 (zero).
                            """

                            serie: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "min_length": 1,
                                    "max_length": 5,
                                },
                            )
                            nrDocto: str = field(
                                metadata={
                                    "type": "Element",
                                    "min_length": 1,
                                    "max_length": 20,
                                }
                            )
                            dtEmisNF: XmlDate = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vlrBruto: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrCPDescPR: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrRatDescPR: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSenarDesc: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

                    @dataclass(kw_only=True)
                    class InfoProcJud(CommonMixin):
                        """
                        :ivar tpProc:
                        :ivar nrProc: Informar um número de processo cadastrado através do evento S-1070, cujo
                            {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) seja igual a [1].
                            Validação: Deve ser um número de processo administrativo ou judicial válido e
                            existente na Tabela de Processos (S-1070), com
                            {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) = [1].
                        :ivar codSusp:
                        :ivar vrCPSusp: Valor da contribuição previdenciária com exigibilidade suspensa.
                            Validação: Preenchimento obrigatório se {vrRatSusp}(./vrRatSusp) e
                            {vrSenarSusp}(./vrSenarSusp) não tiverem sido preenchidos. Deve ser um valor maior
                            que 0 (zero).
                        :ivar vrRatSusp: Valor da contribuição para GILRAT com exigibilidade suspensa.
                            Validação: Preenchimento obrigatório se {vrCPSusp}(./vrCPSusp) e
                            {vrSenarSusp}(./vrSenarSusp) não tiverem sido preenchidos. Deve ser um valor maior
                            que 0 (zero).
                        :ivar vrSenarSusp: Valor da contribuição para o SENAR com exigibilidade suspensa.
                            Validação: Preenchimento obrigatório se {vrCPSusp}(./vrCPSusp) e
                            {vrRatSusp}(./vrRatSusp) não tiverem sido preenchidos. Deve ser um valor maior que 0
                            (zero).
                        """

                        tpProc: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        nrProc: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        codSusp: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrCPSusp: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        vrRatSusp: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        vrSenarSusp: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
