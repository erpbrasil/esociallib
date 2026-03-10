from __future__ import annotations

from dataclasses import dataclass, field

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtExcProcTrab/v_S_01_03_00"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-3500 - Exclusão de Eventos - Processo Trabalhista.

    :ivar evtExcProcTrab: Evento Exclusão DESCRICAO_COMPLETA:Evento Exclusão de Eventos - Processo Trabalhista.
        CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EXC_RET_2501
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtExcProcTrab/v_S_01_03_00"

    evtExcProcTrab: ESocial.EvtExcProcTrab = field(
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
    class EvtExcProcTrab(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoExclusao: Informação do evento que será excluído DESCRICAO_COMPLETA:Grupo que identifica o
            evento objeto da exclusão.
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
        infoExclusao: ESocial.EvtExcProcTrab.InfoExclusao = field(
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
        class InfoExclusao(CommonMixin):
            """
            :ivar tpEvento:
            :ivar nrRecEvt: Preencher com o número do recibo do evento que será excluído. Validação: O recibo
                deve ser relativo ao mesmo tipo de evento indicado em {tpEvento}(./tpEvento).
            :ivar ideProcTrab: Identificação do processo, do trabalhador e do período de apuração.
                DESCRICAO_COMPLETA:Identificação do processo, do trabalhador e do período a que se refere o
                evento que será excluído.
            """

            tpEvento: str = field(
                metadata={
                    "type": "Element",
                    "length": 6,
                }
            )
            nrRecEvt: str = field(
                metadata={
                    "type": "Element",
                }
            )
            ideProcTrab: ESocial.EvtExcProcTrab.InfoExclusao.IdeProcTrab = field(
                metadata={
                    "type": "Element",
                }
            )

            @dataclass(kw_only=True)
            class IdeProcTrab(CommonMixin):
                """
                :ivar nrProcTrab: Número do processo trabalhista, da ata ou número de identificação da
                    conciliação. Validação: Deve ser o mesmo número do processo informado no evento objeto da
                    exclusão.
                :ivar cpfTrab: Preencher com o número do CPF do trabalhador. Validação: Preenchimento
                    obrigatório e exclusivo se {tpEvento}(../tpEvento) = [S-2500]. Deve ser o mesmo CPF
                    informado no evento S-2500 objeto da exclusão.
                :ivar perApurPgto: Mês/ano em que é devida a obrigação de pagar a parcela prevista no
                    acordo/sentença. Validação: Preenchimento obrigatório e exclusivo se {tpEvento}(../tpEvento)
                    = [S-2501, S-2555]. Deve ser o mesmo período informado no evento S-2501 ou S-2555 objeto da
                    exclusão.
                :ivar ideSeqProc: Número sequencial atribuído pela empresa ao processo trabalhista, quando for
                    necessário enviar o mesmo processo em múltiplos S-2500 ou S-2501. Validação: Se
                    {}(../tpEvento) = [S-2500], deve ser o identificador informado em
                    {}(2500_ideTrab_ideSeqTrab). Se {}(../tpEvento) = [S-2501], deve ser o identificador
                    informado em {}(2501_ideProc_ideSeqProc). Se {}(../tpEvento) = [S-2555], não deve ser
                    informado.
                """

                nrProcTrab: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                cpfTrab: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                perApurPgto: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                ideSeqProc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{1,3}",
                    },
                )
