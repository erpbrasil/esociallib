from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtToxic/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2221 - Exame Toxicológico do Motorista Profissional Empregado.

    :ivar evtToxic: Evento Exame Toxicológico do Motorista Profissional Empregado CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_EXT_SEM_IMPACTO_FOPAG
        REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXISTE_VINCULO
        REGRA:REGRA_EXTEMP_REINTEGRACAO REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_RETIFICA_MESMO_VINCULO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtToxic/v_S_01_03_00"

    evtToxic: ESocial.EvtToxic = field(
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
    class EvtToxic(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar toxicologico: Informações do exame toxicológico do motorista profissional. CHAVE_GRUPO: {dtExame*}
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
        ideVinculo: ESocial.EvtToxic.IdeVinculo = field(
            metadata={
                "type": "Element",
            }
        )
        toxicologico: ESocial.EvtToxic.Toxicologico = field(
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
            Informações de identificação do trabalhador e do vínculo.

            CHAVE_GRUPO: {cpfTrab*}, {matricula*}.

            :ivar cpfTrab:
            :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
                matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve
                corresponder à matrícula informada pelo empregador no evento S-2190 ou S-2200 do respectivo
                vínculo trabalhista. Permitir apenas vínculos com categoria [1XX].
            """

            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            matricula: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class Toxicologico(CommonMixin):
            """
            :ivar dtExame: Data da realização do exame toxicológico. Validação: Deve ser uma data válida, igual
                ou anterior à data atual e igual ou posterior à data de início da obrigatoriedade deste evento
                para o empregador no eSocial.
            :ivar cnpjLab: CNPJ do laboratório responsável pela realização do exame. Validação: Deve ser um CNPJ
                válido, com 14 (catorze) algarismos.
            :ivar codSeqExame:
            :ivar nmMed: Preencher com o nome do médico.
            :ivar nrCRM: Número de inscrição do médico no Conselho Regional de Medicina - CRM. Validação:
                Preenchimento obrigatório, exceto se o endereço do trabalhador em S-2200 ou S-2205 vigente em
                {dtExame}(./dtExame) for no exterior.
            :ivar ufCRM: Preencher com a sigla da Unidade da Federação - UF de expedição do CRM. Validação:
                Preenchimento obrigatório, exceto se o endereço do trabalhador em S-2200 ou S-2205 vigente em
                {dtExame}(./dtExame) for no exterior.
            """

            dtExame: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            cnpjLab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            codSeqExame: str = field(
                metadata={
                    "type": "Element",
                    "length": 11,
                    "pattern": r"[a-zA-z]{2}\d{9}",
                }
            )
            nmMed: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nrCRM: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            ufCRM: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
