from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtFGTSProcTrab/v_S_01_03_00"


class BasePerRefTpValorProcTrab(Enum):
    """
    Tipo de valor que influi na apuração do FGTS.

    :cvar VALUE_71: FGTS Origem Processo Trabalhista: quando {codCateg}(./codCateg) = [101, 102, 104, 105, 106,
        111, 201, 202, 301, 302, 303, 306, 307, 309, 310, 312, 721] ou ([304, 401, 410], se
        {categOrig}(5503_infoTrabFGTS_categOrig) for diferente de [103, 107, 108])
    :cvar VALUE_72: FGTS Origem Processo Trabalhista - Aprendiz/Contrato Verde e Amarelo: quando
        {codCateg}(./codCateg) = [103, 107, 108] ou ([304, 401, 410], se
        {categOrig}(5503_infoTrabFGTS_categOrig) = [103, 107, 108])
    :cvar VALUE_73: FGTS Origem Processo Trabalhista - Indenização compensatória do empregado doméstico: quando
        {codCateg}(./codCateg) = [104]
    """

    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-5503 - Informações do FGTS por Trabalhador em Processo Trabalhista.

    :ivar evtFGTSProcTrab: Evento Informações do FGTS por Trabalhador em Processo Trabalhista. CHAVE_GRUPO: {Id}
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtFGTSProcTrab/v_S_01_03_00"

    evtFGTSProcTrab: ESocial.EvtFgtsprocTrab = field(
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
    class EvtFgtsprocTrab(CommonMixin):
        """
        :ivar ideEvento: Informações de identificação do evento.
        :ivar ideEmpregador: Informações de identificação do empregador ou do contribuinte que prestou a
            informação. CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar ideProc: Identificação do processo. CHAVE_GRUPO: {nrProcTrab*}
        :ivar ideTrabalhador: Identificação do trabalhador DESCRICAO_COMPLETA:Grupo que apresenta a
            identificação básica do trabalhador ao qual se refere o evento de retorno. CHAVE_GRUPO: {cpfTrab*}
        :ivar infoTrabFGTS: Informações relativas à matrícula e categoria do trabalhador. CHAVE_GRUPO:
            {matricula}, {codCateg}
        :ivar Id:
        """

        ideEvento: ESocial.EvtFgtsprocTrab.IdeEvento = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: ESocial.EvtFgtsprocTrab.IdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        ideProc: ESocial.EvtFgtsprocTrab.IdeProc = field(
            metadata={
                "type": "Element",
            }
        )
        ideTrabalhador: ESocial.EvtFgtsprocTrab.IdeTrabalhador = field(
            metadata={
                "type": "Element",
            }
        )
        infoTrabFGTS: list[ESocial.EvtFgtsprocTrab.InfoTrabFgts] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 99,
            },
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass(kw_only=True)
        class IdeEvento(CommonMixin):
            """
            :ivar nrRecArqBase: Preencher com o número do recibo do arquivo que deu origem ao presente arquivo
                de retorno. Validação: Deve ser um recibo de entrega válido, correspondente ao arquivo que deu
                origem ao presente arquivo de retorno (S-2500 ou S-3500).
            :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência das informações. Origem: mês/ano
                do campo {dtSent}(2500_infoProcesso_dadosCompl_infoProcJud_dtSent) ou
                {dtCCP}(2500_infoProcesso_dadosCompl_infoCCP_dtCCP) de S-2500.
            """

            nrRecArqBase: str = field(
                metadata={
                    "type": "Element",
                }
            )
            perApur: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class IdeEmpregador(CommonMixin):
            """
            :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição do empregador ou
                contribuinte que prestou a informação, conforme Tabela 05.
            :ivar nrInsc: Informar o número de inscrição do empregador ou contribuinte que prestou a informação,
                de acordo com o tipo de inscrição indicado no campo {ideEmpregador/tpInsc}(./tpInsc) e conforme
                informado em S-1000.
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
        class IdeProc(CommonMixin):
            """
            :ivar origem:
            :ivar nrProcTrab: Número do processo trabalhista, da ata ou número de identificação da conciliação.
                Validação: a) Se o evento de origem for S-2500, retornar o campo
                {nrProcTrab}(2500_infoProcesso_nrProcTrab) desse evento; b) Se o evento de origem for S-3500,
                retornar o campo {nrProcTrab}(2500_infoProcesso_nrProcTrab) do evento S-2500 objeto da exclusão.
            """

            origem: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nrProcTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class IdeTrabalhador(CommonMixin):
            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class InfoTrabFgts(CommonMixin):
            """
            :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
                matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Evento de origem:
                S-2500 ou S-3500. Validação: a) Se o evento de origem for S-2500, retornar a
                {matricula}(2500_ideTrab_infoContr_matricula) informada nesse evento; b) Se o evento de origem
                for S-3500, retornar a matrícula informada no evento objeto da exclusão.
            :ivar codCateg: Preencher com o código da categoria do trabalhador, conforme Tabela 01. Evento de
                origem: S-2500 ou S-3500. Validação: Informação obrigatória e exclusiva se o campo
                {matricula}(./matricula) não for informado. Além disso: a) Se o evento de origem for S-2500,
                retornar o {codCateg}(2500_ideTrab_infoContr_codCateg) informado nesse evento; b) Se o evento de
                origem for S-3500, retornar o código de categoria informado no evento objeto da exclusão.
            :ivar categOrig: Preencher com o código correspondente à categoria de origem do dirigente sindical
                ou do trabalhador cedido. Origem: campo
                {infoDirigenteSindical/categOrig}(2300_infoTSVInicio_infoComplementares_infoDirigenteSindical_categOrig),
                {infoTrabCedido/categOrig}(2300_infoTSVInicio_infoComplementares_infoTrabCedido_categOrig) ou
                {infoMandElet/categOrig}(2300_infoTSVInicio_infoComplementares_infoMandElet_categOrig) de
                S-2300.
            :ivar infoFGTSProcTrab: Informações relativas ao FGTS do processo trabalhista.
            """

            matricula: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            codCateg: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            categOrig: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoFGTSProcTrab: ESocial.EvtFgtsprocTrab.InfoTrabFgts.InfoFgtsprocTrab = field(
                metadata={
                    "type": "Element",
                }
            )

            @dataclass(kw_only=True)
            class InfoFgtsprocTrab(CommonMixin):
                """
                :ivar totalFGTS: Valor total de FGTS a recolher no processo trabalhista. Validação: Deve
                    corresponder ao somatório dos valores retornados nos campos
                    {dpsFGTSProcTrab}(./ideEstab_basePerRef_dpsFGTSProcTrab),
                    {dpsFGTSSefip}(./ideEstab_basePerRef_dpsFGTSSefip) e
                    {dpsFGTSDecAnt}(./ideEstab_basePerRef_dpsFGTSDecAnt) abaixo. Se o evento de origem for
                    S-3500, retornar 0 (zero).
                :ivar ideEstab: Identificação do estabelecimento responsável pelo pagamento ao trabalhador dos
                    valores informados. CONDICAO_GRUPO: O (se {totalFGTS}(../totalFGTS) &gt; 0); N (nos demais
                    casos)
                """

                totalFGTS: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                ideEstab: None | ESocial.EvtFgtsprocTrab.InfoTrabFgts.InfoFgtsprocTrab.IdeEstab = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class IdeEstab(CommonMixin):
                    """
                    :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição do estabelecimento,
                        de acordo com as opções da Tabela 05. Origem: campo
                        {ideEstab/tpInsc}(2500_ideTrab_infoContr_ideEstab_tpInsc) de S-2500.
                    :ivar nrInsc: Informar o número de inscrição do estabelecimento do contribuinte de acordo
                        com o tipo de inscrição indicado no campo acima. Origem: campo
                        {ideEstab/nrInsc}(2500_ideTrab_infoContr_ideEstab_nrInsc) de S-2500.
                    :ivar basePerRef: Informações sobre bases de cálculo e valores do FGTS por período de
                        referência. CHAVE_GRUPO: {perRef}, {tpValorProcTrab} CONDICAO_GRUPO: O (se
                        {basePerRef/codCateg}(./codCateg) = [1XX, 2XX, 301, 302, 303, 304, 306, 307, 309, 310,
                        312, 4XX, 721]); N (nos demais casos)
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
                    basePerRef: list[ESocial.EvtFgtsprocTrab.InfoTrabFgts.InfoFgtsprocTrab.IdeEstab.BasePerRef] = (
                        field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                            },
                        )
                    )

                    @dataclass(kw_only=True)
                    class BasePerRef(CommonMixin):
                        """
                        :ivar perRef: Informar o mês/ano (formato AAAA-MM) de referência das informações.
                            Origem: campo {perRef}(2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_perRef) de
                            S-2500.
                        :ivar codCateg: Preencher com o código da categoria do trabalhador, conforme Tabela 01.
                            Validação: a) Se {indContr}(2500_ideTrab_infoContr_indContr) em S-2500 = [N],
                            retornar o código informado no campo
                            {infoContr/codCateg}(2500_ideTrab_infoContr_codCateg) do evento S-2500; b) Se
                            {indContr}(2500_ideTrab_infoContr_indContr) em S-2500 = [S]: b1) Se
                            {indCateg}(2500_ideTrab_infoContr_indCateg) em S-2500 = [N], retornar o código de
                            categoria existente no Registro de Eventos Trabalhistas - RET no último dia da
                            competência de referência; b2) Se {indCateg}(2500_ideTrab_infoContr_indCateg) em
                            S-2500 = [S] e o mês/ano de
                            {dtMudCategAtiv}(2500_ideTrab_infoContr_mudCategAtiv_dtMudCategAtiv) de S-2500 for
                            maior que {perRef}(./perRef), retornar o código de categoria existente no RET no
                            último dia da competência de referência; b3) Se
                            {indCateg}(2500_ideTrab_infoContr_indCateg) em S-2500 = [S] e o mês/ano de
                            {dtMudCategAtiv}(2500_ideTrab_infoContr_mudCategAtiv_dtMudCategAtiv) de S-2500 for
                            menor ou igual a {perRef}(./perRef), retornar
                            {mudCategAtiv/codCateg}(2500_ideTrab_infoContr_mudCategAtiv_codCateg) do evento
                            S-2500.
                        :ivar tpValorProcTrab:
                        :ivar remFGTSProcTrab: Valor da base de cálculo de FGTS ainda não declarada, reconhecida
                            no processo trabalhista. Origem: campo
                            {vrBcFGTSProcTrab}(2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_infoFGTS_vrBcFGTSProcTrab)
                            de S-2500.
                        :ivar dpsFGTSProcTrab: Valor histórico do FGTS a ser depositado na conta vinculada do
                            trabalhador sobre base reconhecida no processo trabalhista. Validação: Deve ser
                            maior que 0 (zero). Deve corresponder à multiplicação de
                            {remFGTSProcTrab}(./remFGTSProcTrab) pela alíquota abaixo: a) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [71], alíquota de 8%; b) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [72], alíquota de 2%; c) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [73], alíquota de 3,2%.
                        :ivar remFGTSSefip: Valor da base de cálculo declarada anteriormente em SEFIP e ainda
                            não recolhida. Origem: campo
                            {vrBcFGTSSefip}(2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_infoFGTS_vrBcFGTSSefip)
                            de S-2500.
                        :ivar dpsFGTSSefip: Valor histórico do FGTS a ser depositado na conta vinculada do
                            trabalhador sobre base já declarada anteriormente em SEFIP. Validação: Deve ser
                            maior que 0 (zero). Deve corresponder à multiplicação de
                            {remFGTSSefip}(./remFGTSSefip) pela alíquota abaixo: a) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [71], alíquota de 8%; b) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [72], alíquota de 2%; c) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [73], alíquota de 3,2%.
                        :ivar remFGTSDecAnt: Valor da base de cálculo declarada anteriormente no eSocial e ainda
                            não recolhida. Origem: campo
                            {vrBcFGTSDecAnt}(2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_infoFGTS_vrBcFGTSDecAnt)
                            de S-2500.
                        :ivar dpsFGTSDecAnt: Valor histórico do FGTS a ser depositado na conta vinculada do
                            trabalhador sobre base já declarada anteriormente no eSocial. Validação: Deve ser
                            maior que 0 (zero). Deve corresponder à multiplicação de
                            {remFGTSDecAnt}(./remFGTSDecAnt) pela alíquota abaixo: a) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [71], alíquota de 8%; b) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [72], alíquota de 2%; c) Se
                            {tpValorProcTrab}(./tpValorProcTrab) = [73], alíquota de 3,2%.
                        """

                        perRef: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        codCateg: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        tpValorProcTrab: BasePerRefTpValorProcTrab = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        remFGTSProcTrab: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        dpsFGTSProcTrab: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        remFGTSSefip: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        dpsFGTSSefip: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        remFGTSDecAnt: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        dpsFGTSDecAnt: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
