from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtReintegr/v_S_01_03_00"


class InfoReintegrTpReint(Enum):
    """
    Tipo de reintegração/outro provimento.

    Validação: Os tipos [3, 4, 5, 6] só podem ser informados se a natureza jurídica do declarante for Administração
    Pública (grupo [1]).

    :cvar VALUE_1: Reintegração por decisão judicial
    :cvar VALUE_2: Reintegração por anistia legal
    :cvar VALUE_3: Reversão de servidor público
    :cvar VALUE_4: Recondução de servidor público
    :cvar VALUE_5: Reinclusão de militar
    :cvar VALUE_6: Revisão de reforma de militar
    :cvar VALUE_9: Outros
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_9 = 9


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2298 - Reintegração/Outros Provimentos.

    :ivar evtReintegr: Evento Reintegração/Outros Provimentos. CHAVE_GRUPO: {Id} REGRA:REGRA_EMPREGADO_DOMESTICO
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO
        REGRA:REGRA_EXISTE_EVENTO_DESLIGAMENTO REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_EXTEMP_REINTEGRACAO REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_REINTEG_EXCLUSAO_EVENTO
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtReintegr/v_S_01_03_00"

    evtReintegr: ESocial.EvtReintegr = field(
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
    class EvtReintegr(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideVinculo:
        :ivar infoReintegr: Informações da reintegração. CHAVE_GRUPO: {dtEfetRetorno*}
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
        infoReintegr: ESocial.EvtReintegr.InfoReintegr = field(
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
        class InfoReintegr(CommonMixin):
            """
            :ivar tpReint:
            :ivar nrProcJud: Em caso de reintegração por determinação judicial, preencher com o número do
                processo. Validação: Informação obrigatória e exclusiva se {tpReint}(./tpReint) = [1]. Se
                preenchido, deve ser um processo judicial válido, com 20 (vinte) algarismos.
            :ivar nrLeiAnistia:
            :ivar dtEfetRetorno: Informar a data do efetivo retorno ao trabalho. Validação: Deve ser uma data
                válida, posterior à data de desligamento do trabalhador. Não pode ser posterior a 30 (trinta)
                dias da data atual.
            :ivar dtEfeito: Informar a data de início dos efeitos financeiros da reintegração. Validação: Deve
                ser uma data igual ou anterior à data do efetivo retorno ao trabalho e posterior à data do
                desligamento.
            """

            tpReint: InfoReintegrTpReint = field(
                metadata={
                    "type": "Element",
                }
            )
            nrProcJud: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            nrLeiAnistia: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "pattern": r"\w{5,13}",
                },
            )
            dtEfetRetorno: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
            dtEfeito: XmlDate = field(
                metadata={
                    "type": "Element",
                }
            )
