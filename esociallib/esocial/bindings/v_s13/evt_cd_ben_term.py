from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCdBenTerm/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2420 - Cadastro de Benefício - Entes Públicos - Término.

    :ivar evtCdBenTerm: Evento Cadastro de Benefício - Término DESCRICAO_COMPLETA:Evento Cadastro de Benefício -
        Entes Públicos - Término. CHAVE_GRUPO: {Id} REGRA:REGRA_BENEFICIO_ATIVO_NA_DTEVENTO
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_EXTEMP_REATIVACAO REGRA:REGRA_MUDANCA_CPF REGRA:REGRA_RETIFICA_MESMO_BENEFICIO
        REGRA:REGRA_VALIDA_CNPJ
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCdBenTerm/v_S_01_03_00"

    evtCdBenTerm: ESocial.EvtCdBenTerm = field(
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
    class EvtCdBenTerm(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideBeneficio:
        :ivar infoBenTermino: Informações da cessação do benefício. CHAVE_GRUPO: {dtTermBeneficio*}
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
        ideBeneficio: str = field(
            metadata={
                "type": "Element",
            }
        )
        infoBenTermino: ESocial.EvtCdBenTerm.InfoBenTermino = field(
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
        class InfoBenTermino(CommonMixin):
            """
            :ivar dtTermBeneficio: Data de cessação do benefício. Validação: Deve ser igual ou anterior à data
                atual. No caso de benefício reativado, também deve ser uma data igual ou posterior a
                {dtEfetReativ}(2418_infoReativ_dtEfetReativ) do evento S-2418.
            :ivar mtvTermino:
            :ivar cnpjOrgaoSuc: Informar o CNPJ do órgão público sucessor. Validação: Preenchimento obrigatório
                e exclusivo se {mtvTermino}(./mtvTermino) = [09]. Deve ser um CNPJ válido e diferente da
                inscrição do declarante, considerando as particularidades aplicadas à informação de CNPJ de
                órgão público em S-1000. Além disso, deve possuir 14 (catorze) algarismos e ser diferente do
                CNPJ base do órgão público declarante (exceto se
                {ideEmpregador/nrInsc}(2420_ideEmpregador_nrInsc) tiver 14 (catorze) algarismos) e dos
                estabelecimentos informados através do evento S-1005.
            :ivar novoCPF: Preencher com o novo CPF do beneficiário. Validação: Preenchimento obrigatório e
                exclusivo se {mtvTermino}(./mtvTermino) = [10]. Deve ser um CPF válido e diferente do antigo CPF
                do beneficiário.
            """

            dtTermBeneficio: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            mtvTermino: str = field(
                metadata={
                    "type": "Element",
                    "pattern": r"\d{2}",
                }
            )
            cnpjOrgaoSuc: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            novoCPF: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
