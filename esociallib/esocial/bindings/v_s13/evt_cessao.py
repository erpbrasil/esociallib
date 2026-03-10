from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCessao/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2231 - Cessão/Exercício em Outro Órgão.

    :ivar evtCessao: Evento Cessão/Exercício em Outro Órgão. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_EXT_SEM_IMPACTO_FOPAG
        REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EXCLUI_EVENTO_CESSAO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_EXTEMP_REINTEGRACAO REGRA:REGRA_MESMO_PROCEMI
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_VINCULO_ATIVO_NA_DTEVENTO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCessao/v_S_01_03_00"

    evtCessao: ESocial.EvtCessao = field(
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
    class EvtCessao(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar infoCessao: Informações da cessão/exercício em outro órgão.
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
        infoCessao: ESocial.EvtCessao.InfoCessao = field(
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
        class InfoCessao(CommonMixin):
            """
            :ivar iniCessao: Informações de início da cessão/exercício em outro órgão. CHAVE_GRUPO:
                {dtIniCessao*} CONDICAO_GRUPO: O (se não for preenchido o grupo {fimCessao}(../fimCessao)); N
                (nos demais casos)
            :ivar fimCessao: Informação de término da cessão/exercício em outro órgão. CHAVE_GRUPO:
                {dtTermCessao*} CONDICAO_GRUPO: O (se não for preenchido o grupo {iniCessao}(../iniCessao)); N
                (nos demais casos) REGRA:REGRA_EXISTE_EVENTO_CESSAO
            """

            iniCessao: None | ESocial.EvtCessao.InfoCessao.IniCessao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            fimCessao: None | ESocial.EvtCessao.InfoCessao.FimCessao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class IniCessao(CommonMixin):
                """
                :ivar dtIniCessao: Data de início da cessão/exercício em outro órgão. Validação: Deve-se
                    obedecer às seguintes regras: a) Não pode ser posterior à data atual; b) Não pode existir
                    evento de cessão/exercício em outro órgão (ou evento de afastamento pelo código de motivo de
                    afastamento [14]) com data anterior a {dtIniCessao}(./dtIniCessao) sem que tenha sido
                    encerrado.
                :ivar cnpjCess: Preencher com o CNPJ do empregador/órgão público cessionário/de destino.
                    Validação: Deve ser um CNPJ diferente do CNPJ do empregador/órgão público e diferente dos
                    estabelecimentos informados através do evento S-1005. REGRA:REGRA_VALIDA_CNPJ
                :ivar respRemun: Informar se o empregador/órgão público declarante continuará informando
                    remunerações (S-1200/S-1202) do trabalhador cedido/em exercício em outro órgão.
                """

                dtIniCessao: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                cnpjCess: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                respRemun: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class FimCessao(CommonMixin):
                """
                :ivar dtTermCessao: Preencher com a data de término da cessão/exercício em outro órgão.
                    Validação: Deve-se obedecer às seguintes regras: a) Deve ser igual ou posterior à data de
                    início da cessão/exercício em outro órgão; b) Não pode ser posterior à data atual.
                """

                dtTermCessao: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
