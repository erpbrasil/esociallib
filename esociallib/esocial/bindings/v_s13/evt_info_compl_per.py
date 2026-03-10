from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtInfoComplPer/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1280 - Informações Complementares aos Eventos Periódicos.

    :ivar evtInfoComplPer: Evento Informações Complementares DESCRICAO_COMPLETA:Evento Informações
        Complementares aos Eventos Periódicos. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVE_FOPAG_IND_RETIFICACAO
        REGRA:REGRA_EVE_FOPAG_INFO_COMPAT_CLASSTRIB REGRA:REGRA_EVE_FOPAG_PERMITE_EXCLUSAO
        REGRA:REGRA_EVE_FOPAG_SIMPLIFICADO REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_REMUN_ANUAL_DEZEMBRO REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtInfoComplPer/v_S_01_03_00"

    evtInfoComplPer: ESocial.EvtInfoComplPer = field(
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
    class EvtInfoComplPer(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoSubstPatr: Inf. complementares - Empresas enquadradas nos arts. 7º a 9º da Lei 12.546/2011
            DESCRICAO_COMPLETA:Grupo preenchido exclusivamente por empresa enquadrada nos arts. 7º a 9º da Lei
            12.546/2011, conforme classificação tributária indicada no evento S-1000. CONDICAO_GRUPO: O (se
            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 = [1]); N (nos demais
            casos)
        :ivar infoSubstPatrOpPort: Informação de substituição prevista na Lei 12.546/2011
            DESCRICAO_COMPLETA:Grupo preenchido exclusivamente pelo Órgão Gestor de Mão de Obra - OGMO
            ({classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [09]), listando apenas
            seus códigos de lotação com operadores portuários enquadrados nos arts. 7º a 9º da Lei 12.546/2011.
            CHAVE_GRUPO: {codLotacao} CONDICAO_GRUPO: OC (se
            {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [09]; N (nos demais
            casos)
        :ivar infoAtivConcom: Empresas enquadradas no Simples Nacional - Atividades concomitantes
            DESCRICAO_COMPLETA:Grupo preenchido por empresa enquadrada no regime de tributação Simples Nacional
            com tributação previdenciária substituída e não substituída. CONDICAO_GRUPO: O (se
            {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [03]); N (nos demais
            casos)
        :ivar infoPercTransf11096: Transformação de entidade beneficente em empresa de fins lucrativos
            DESCRICAO_COMPLETA:Grupo preenchido por entidade que tenha se transformado em sociedade de fins
            lucrativos nos termos e no prazo da Lei 11.096/2005. CONDICAO_GRUPO: O (se
            {dtTrans11096}(1000_infoEmpregador_inclusao_infoCadastro_dtTrans11096) em S-1000 for informado); N
            (nos demais casos)
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
        infoSubstPatr: None | ESocial.EvtInfoComplPer.InfoSubstPatr = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        infoSubstPatrOpPort: list[ESocial.EvtInfoComplPer.InfoSubstPatrOpPort] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 9999,
            },
        )
        infoAtivConcom: None | ESocial.EvtInfoComplPer.InfoAtivConcom = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        infoPercTransf11096: None | ESocial.EvtInfoComplPer.InfoPercTransf11096 = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass(kw_only=True)
        class InfoSubstPatr(CommonMixin):
            """
            :ivar indSubstPatr: Indicativo de substituição da contribuição previdenciária patronal.
            :ivar percRedContrib: Percentual não substituído pela contribuição prevista na Lei 12.546/2011.
                Informar 0 (zero) se {indSubstPatr}(./indSubstPatr) = [1]. Caso contrário, preencher com o
                percentual correspondente à razão entre a receita de atividades não relacionadas nos arts. 7º e
                8º da Lei 12.546/2011 e a receita bruta total. Validação: Se {indSubstPatr}(./indSubstPatr) =
                [1], informar 0 (zero).
            """

            indSubstPatr: str = field(
                metadata={
                    "type": "Element",
                }
            )
            percRedContrib: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class InfoSubstPatrOpPort(CommonMixin):
            """
            :ivar codLotacao: Informar o código atribuído pelo empregador para a lotação tributária. Validação:
                Deve ser um código válido e existente na Tabela de Lotações Tributárias (S-1020), com
                {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) = [08].
            """

            codLotacao: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class InfoAtivConcom(CommonMixin):
            """
            :ivar fatorMes: Informe o fator a ser utilizado para cálculo da contribuição patronal do mês dos
                trabalhadores envolvidos na execução das atividades enquadradas no Anexo IV em conjunto com as
                dos Anexos I a III e V da Lei Complementar 123/2006.
            :ivar fator13: Informe o fator a ser utilizado para cálculo da contribuição patronal do décimo
                terceiro dos trabalhadores envolvidos na execução das atividades enquadradas no Anexo IV em
                conjunto com as dos Anexos I a III e V da Lei Complementar 123/2006.
            """

            fatorMes: str = field(
                metadata={
                    "type": "Element",
                }
            )
            fator13: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class InfoPercTransf11096(CommonMixin):
            """
            :ivar percTransf: Informe o percentual de contribuição social devida em caso de transformação em
                sociedade de fins lucrativos - Lei 11.096/2005.
            """

            percTransf: str = field(
                metadata={
                    "type": "Element",
                }
            )
