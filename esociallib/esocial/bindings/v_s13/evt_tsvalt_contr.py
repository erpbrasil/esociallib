from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTSVAltContr/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual.

    :ivar evtTSVAltContr: Evento TSVE - Alteração Contratual DESCRICAO_COMPLETA:Evento Trabalhador Sem Vínculo
        de Emprego/Estatutário - Alteração Contratual. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_RETIFICA_MESMO_VINCULO
        REGRA:REGRA_TSV_ATIVO_NA_DTEVENTO REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTSVAltContr/v_S_01_03_00"

    evtTSVAltContr: ESocial.EvtTsvaltContr = field(
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
    class EvtTsvaltContr(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideTrabSemVinculo:
        :ivar infoTSVAlteracao: TSVE - Alteração Contratual. CHAVE_GRUPO: {dtAlteracao*}
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
        ideTrabSemVinculo: str = field(
            metadata={
                "type": "Element",
            }
        )
        infoTSVAlteracao: ESocial.EvtTsvaltContr.InfoTsvalteracao = field(
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
        class InfoTsvalteracao(CommonMixin):
            """
            :ivar dtAlteracao:
            :ivar natAtividade: Natureza da atividade. Validação: Preenchimento obrigatório se o código de
                categoria no Registro de Eventos Trabalhistas - RET for igual a [201, 202, 401, 731, 734, 738].
                Não deve ser preenchido se o código de categoria no RET for igual a [721, 722, 771, 901].
            :ivar infoComplementares: Informações complementares DESCRICAO_COMPLETA:Grupo onde são fornecidas
                informações complementares, preenchidas conforme a categoria do TSVE. CONDICAO_GRUPO: O (de
                acordo com a condição dos grupos inferiores); OC (nos demais casos)
            """

            dtAlteracao: str = field(
                metadata={
                    "type": "Element",
                }
            )
            natAtividade: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoComplementares: None | ESocial.EvtTsvaltContr.InfoTsvalteracao.InfoComplementares = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class InfoComplementares(CommonMixin):
                """
                :ivar cargoFuncao: Cargo/Função ocupado pelo TSVE DESCRICAO_COMPLETA:Grupo que apresenta o cargo
                    e/ou função ocupada pelo TSVE. CONDICAO_GRUPO: OC (se o código de categoria no RET for igual
                    a [901, 903, 904, 906]); O (nos demais casos)
                :ivar remuneracao: Informações da remuneração e periodicidade de pagamento. CONDICAO_GRUPO: O
                    (se o código de categoria no RET for igual a [721, 722, 771, 906]); OC (nos demais casos)
                :ivar infoDirigenteSindical: Informações relativas ao dirigente sindical. CONDICAO_GRUPO: O (se
                    o código de categoria no RET for igual a [401]); N (nos demais casos)
                :ivar infoTrabCedido: Informações relativas ao trabalhador cedido/em exercício em outro órgão
                    DESCRICAO_COMPLETA:Informações relativas ao trabalhador cedido/em exercício em outro órgão,
                    preenchidas exclusivamente pelo cessionário/órgão de destino. CONDICAO_GRUPO: O (se o código
                    de categoria no RET for igual a [410]); N (nos demais casos)
                :ivar infoMandElet: Informações relativas a servidor público exercente de mandato eletivo.
                    CONDICAO_GRUPO: O (se o código de categoria no RET for igual a [304]); N (nos demais casos)
                :ivar infoEstagiario: Informações relativas ao estagiário ou ao beneficiário do Programa
                    Nacional de Prestação de Serviço Civil Voluntário. CONDICAO_GRUPO: O (se o código de
                    categoria no RET for igual a [901, 906]); N (nos demais casos)
                :ivar localTrabGeral: Estabelecimento onde o trabalhador exercerá suas atividades
                    DESCRICAO_COMPLETA:Estabelecimento (CNPJ, CNO, CAEPF) onde o trabalhador exercerá suas
                    atividades. Caso o trabalhador exerça suas atividades em instalações de terceiros, este
                    campo deve ser preenchido com o estabelecimento do próprio declarante ao qual o trabalhador
                    esteja vinculado. CONDICAO_GRUPO: O (se o código de categoria no RET for igual a [2XX, 304,
                    305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771, 901, 902, 906] e
                    {dtAlteracao}(2306_infoTSVAlteracao_dtAlteracao) &gt;= [2024-01-22]); F (se o código de
                    categoria no RET for igual a [2XX, 304, 305, 4XX, 721, 722, 723, 731, 734, 738, 761, 771,
                    901, 902, 906] e {dtAlteracao}(2306_infoTSVAlteracao_dtAlteracao) &lt; [2024-01-22]); N (nos
                    demais casos)
                """

                cargoFuncao: None | ESocial.EvtTsvaltContr.InfoTsvalteracao.InfoComplementares.CargoFuncao = field(
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
                infoDirigenteSindical: (
                    None | ESocial.EvtTsvaltContr.InfoTsvalteracao.InfoComplementares.InfoDirigenteSindical
                ) = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoTrabCedido: None | ESocial.EvtTsvaltContr.InfoTsvalteracao.InfoComplementares.InfoTrabCedido = (
                    field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                )
                infoMandElet: None | ESocial.EvtTsvaltContr.InfoTsvalteracao.InfoComplementares.InfoMandElet = field(
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
                    :ivar nmCargo: Informar o nome do cargo. Validação: Preenchimento obrigatório se o código de
                        categoria no RET for diferente de [410].
                    :ivar CBOCargo:
                    :ivar nmFuncao: Informar o nome da função de confiança. Validação: Preenchimento obrigatório
                        se o código de categoria no RET for igual a [410] e não houver informação de
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
                class InfoDirigenteSindical(CommonMixin):
                    """
                    :ivar tpRegPrev: Tipo de regime previdenciário. Validação: Se
                        {infoDirigenteSindical/categOrig}(2300_infoTSVInicio_infoComplementares_infoDirigenteSindical_categOrig)
                        do evento S-2300 for relativa a "Empregado", não pode ser preenchido com [2].
                    """

                    tpRegPrev: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoTrabCedido(CommonMixin):
                    """
                    :ivar tpRegPrev: Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares
                        das Forças Armadas). Validação: Se
                        {infoTrabCedido/categOrig}(2300_infoTSVInicio_infoComplementares_infoTrabCedido_categOrig)
                        do evento S-2300 for relativa a "Empregado", não pode ser preenchido com [2, 4].
                    """

                    tpRegPrev: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoMandElet(CommonMixin):
                    """
                    :ivar indRemunCargo:
                    :ivar tpRegPrev: Tipo de regime previdenciário.
                    """

                    indRemunCargo: None | str = field(
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
