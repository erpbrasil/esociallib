from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.tipos import (
    TIdeEmpregador,
    TIdeEventoTrabAdmissao,
    TsNatAtividade,
    TsTpContr,
    TsUndSalFixo,
)
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2190 - Registro Preliminar de Trabalhador.

    :ivar evtAdmPrelim: Evento Registro Preliminar de Trabalhador. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ADMISSAO_VALIDA_DT_ADM REGRA:REGRA_ADMISSAO_VALIDA_DURACAO_CONTRATO
        REGRA:REGRA_BLOQUEIA_USO_CPF_EMPREGADOR REGRA:REGRA_COMPATIBILIDADE_CATEGORIA_CLASSTRIB
        REGRA:REGRA_EMPREGADO_DOMESTICO REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_RETIFICA_MESMO_VINCULO
        REGRA:REGRA_VALIDA_ADMISSAO_PRELIMINAR REGRA:REGRA_VALIDA_EMPREGADOR REGRA:REGRA_VALIDA_MATRICULA
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00"

    evtAdmPrelim: ESocial.EvtAdmPrelim = field(
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
    class EvtAdmPrelim(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoRegPrelim: Informações do registro preliminar do trabalhador. CHAVE_GRUPO: {cpfTrab*},
            {matricula*}
        :ivar Id:
        """

        ideEvento: TIdeEventoTrabAdmissao = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: TIdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        infoRegPrelim: ESocial.EvtAdmPrelim.InfoRegPrelim = field(
            metadata={
                "type": "Element",
            }
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
                "length": 36,
                "pattern": r"ID\d{34}",
            }
        )

        @dataclass(kw_only=True)
        class InfoRegPrelim(CommonMixin):
            """
            :ivar cpfTrab:
            :ivar dtNascto: Preencher com a data de nascimento.
            :ivar dtAdm: Preencher com a data de admissão do trabalhador (ou data de início, no caso de
                Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE). Validação: Deve ser posterior à data de
                nascimento do trabalhador, igual ou posterior à data de início da obrigatoriedade dos eventos
                não periódicos para o empregador e igual ou anterior ao ano do óbito, se existente.
            :ivar matricula: Matrícula atribuída ao trabalhador pela empresa. Validação: O valor informado não
                pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições.
                REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar codCateg: Preencher com o código da categoria do trabalhador. Validação: Deve ser um código de
                categoria sujeito ao Registro de Eventos Trabalhistas - RET de trabalhador não vinculado ao
                Regime Próprio de Previdência Social - RPPS, ou seja, "Empregado" ([1XX]), algumas categorias de
                "Agente Público" ([301, 302, 303, 304, 306, 307, 309, 310, 312]), "Avulso" ([2XX]), "Cessão"
                ([4XX]), algumas categorias de "Contribuinte Individual" ([721, 722, 723, 731, 734, 738, 761,
                771]) ou de "Bolsista" ([901, 902]).
            :ivar natAtividade: Natureza da atividade. Validação: Preenchimento obrigatório se
                {codCateg}(./codCateg) for relativo a "Empregado", "Agente Público", "Avulso" ou igual a [401,
                731, 734, 738]. Não deve ser preenchido se {codCateg}(./codCateg) = [721, 722, 771, 901]. Se
                {codCateg}(./codCateg) = [104], deve ser preenchido com [1]. Se {codCateg}(./codCateg) = [102],
                deve ser preenchido com [2].
            :ivar infoRegCTPS: Informações referentes ao registro e à CTPS Digital
                DESCRICAO_COMPLETA:Informações referentes ao registro eletrônico de empregados e à Carteira de
                Trabalho e Previdência Digital - CTPS Digital. CONDICAO_GRUPO: OC (se
                {codCateg}(2190_infoRegPrelim_codCateg) for relativo a "Empregado" ou "Agente Público"); N (nos
                demais casos)
            """

            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                    "pattern": r"\d{11}",
                }
            )
            dtNascto: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtAdm: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            matricula: str = field(
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 30,
                    "pattern": r".*[^\s].*",
                }
            )
            codCateg: str = field(
                metadata={
                    "type": "Element",
                    "pattern": r"\d{3}",
                }
            )
            natAtividade: None | TsNatAtividade = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoRegCTPS: None | ESocial.EvtAdmPrelim.InfoRegPrelim.InfoRegCtps = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class InfoRegCtps(CommonMixin):
                """
                :ivar CBOCargo: Informar a Classificação Brasileira de Ocupações - CBO relativa ao cargo.
                    Validação: Deve ser um código válido e existente na tabela de CBO, com 6 (seis) posições.
                :ivar vrSalFx:
                :ivar undSalFixo:
                :ivar tpContr: Tipo de contrato de trabalho. Validação: Se {codCateg}(../codCateg) = [103] e
                    {dtAdm}(../dtAdm) &gt;= [2024-04-22], deve ser informado [2].
                :ivar dtTerm: Data do término do contrato por prazo determinado. Validação: O preenchimento é
                    obrigatório se {tpContr}(./tpContr) = [2]. Não informar se {tpContr}(./tpContr) = [1]. Deve
                    ser igual ou posterior à data de admissão.
                """

                CBOCargo: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{6}",
                    }
                )
                vrSalFx: Decimal = field(
                    metadata={
                        "type": "Element",
                        "min_inclusive": Decimal("0"),
                        "max_inclusive": Decimal("999999999999.99"),
                        "total_digits": 14,
                        "fraction_digits": 2,
                    }
                )
                undSalFixo: TsUndSalFixo = field(
                    metadata={
                        "type": "Element",
                    }
                )
                tpContr: TsTpContr = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtTerm: None | XmlDate = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
