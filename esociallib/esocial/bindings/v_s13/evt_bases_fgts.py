from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtBasesFGTS/v_S_01_03_00"


@dataclass(kw_only=True)
class TDetRubrSusp(CommonMixin):
    """
    :ivar codRubr: Informar o código atribuído pelo empregador que identifica a rubrica em sua folha de
        pagamento. Evento de origem: S-1200, S-2299 ou S-2399.
    :ivar ideTabRubr: Preencher com o identificador da Tabela de Rubricas para a rubrica definida em
        {codRubr}(./codRubr). Evento de origem: S-1200, S-2299 ou S-2399.
    :ivar vrRubr: Valor total da rubrica. Evento de origem: S-1200, S-2299 ou S-2399. Validação: Deve
        corresponder ao somatório dos valores informados no campo {vrRubr} dos eventos de origem para a
        respectiva rubrica.
    :ivar ideProcessoFGTS: Identificação de processo - Incidência de FGTS DESCRICAO_COMPLETA:Processo(s)
        judicial(is) com decisão/sentença favorável, determinando a não incidência de FGTS. Evento de origem:
        S-1010. CHAVE_GRUPO: {nrProc}
    """

    class Meta:
        name = "T_detRubrSusp"

    codRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesFGTS/v_S_01_03_00",
        }
    )
    ideTabRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesFGTS/v_S_01_03_00",
        }
    )
    vrRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesFGTS/v_S_01_03_00",
        }
    )
    ideProcessoFGTS: list[TDetRubrSusp.IdeProcessoFgts] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesFGTS/v_S_01_03_00",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class IdeProcessoFgts(CommonMixin):
        """
        :ivar nrProc: Informar o número do processo.
        """

        nrProc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtBasesFGTS/v_S_01_03_00",
            }
        )


class BasePerApurTpValor(Enum):
    """
    Tipo de valor que influi na apuração do FGTS.

    :cvar VALUE_11: FGTS mensal
    :cvar VALUE_12: FGTS 13° salário
    :cvar VALUE_13: FGTS (período anterior) mensal
    :cvar VALUE_14: FGTS (período anterior) 13º salário
    :cvar VALUE_15: FGTS mensal - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_16: FGTS 13° salário - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_17: FGTS (período anterior) mensal - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_18: FGTS (período anterior) 13º salário - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_21: FGTS mês da rescisão
    :cvar VALUE_22: FGTS 13° salário rescisório
    :cvar VALUE_23: FGTS aviso prévio indenizado
    :cvar VALUE_24: FGTS (período anterior) mês da rescisão
    :cvar VALUE_25: FGTS (período anterior) 13º salário rescisório
    :cvar VALUE_26: FGTS (período anterior) aviso prévio indenizado
    :cvar VALUE_27: FGTS mês da rescisão - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_28: FGTS 13° salário rescisório - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_29: FGTS aviso prévio indenizado - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_30: FGTS (período anterior) mês da rescisão - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_31: FGTS (período anterior) 13° salário rescisório - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_32: FGTS (período anterior) aviso prévio indenizado - Aprendiz/Contrato Verde e Amarelo
    :cvar VALUE_41: FGTS mensal - Indenização compensatória do empregado doméstico
    :cvar VALUE_42: FGTS 13° salário - Indenização compensatória do empregado doméstico
    :cvar VALUE_43: FGTS (período anterior) mensal - Indenização compensatória do empregado doméstico
    :cvar VALUE_44: FGTS (período anterior) 13º salário - Indenização compensatória do empregado doméstico
    :cvar VALUE_45: FGTS mês da rescisão - Indenização compensatória do empregado doméstico
    :cvar VALUE_46: FGTS 13° salário rescisório - Indenização compensatória do empregado doméstico
    :cvar VALUE_47: FGTS aviso prévio indenizado - Indenização compensatória do empregado doméstico
    :cvar VALUE_48: FGTS (período anterior) mês da rescisão - Indenização compensatória do empregado doméstico
    :cvar VALUE_49: FGTS (período anterior) 13º salário rescisório - Indenização compensatória do empregado
        doméstico
    :cvar VALUE_50: FGTS (período anterior) aviso prévio indenizado - Indenização compensatória do empregado
        doméstico
    """

    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_50 = 50


class InfoFgtsClassTrib(Enum):
    """
    Preencher com o código correspondente à classificação tributária do contribuinte, conforme Tabela 08.

    Evento de origem: S-1000. Validação: Retornar somente se for igual a [04, 22].

    :cvar VALUE_04: Microempreendedor Individual - MEI
    :cvar VALUE_22: Segurado especial, inclusive quando for empregador doméstico
    """

    VALUE_04 = "04"
    VALUE_22 = "22"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-5003 - Informações do FGTS por Trabalhador.

    :ivar evtBasesFGTS: Evento Informações do FGTS por Trabalhador. CHAVE_GRUPO: {Id}
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtBasesFGTS/v_S_01_03_00"

    evtBasesFGTS: ESocial.EvtBasesFgts = field(
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
    class EvtBasesFgts(CommonMixin):
        """
        :ivar ideEvento: Identificação do evento de retorno. CHAVE_GRUPO: {indApuracao*}, {perApur*}
        :ivar ideEmpregador:
        :ivar ideTrabalhador: Identificação do trabalhador DESCRICAO_COMPLETA:Grupo que apresenta a
            identificação básica do trabalhador ao qual se refere o evento de retorno. CHAVE_GRUPO: {cpfTrab*}
        :ivar infoFGTS: Informações relativas ao FGTS DESCRICAO_COMPLETA:Informações relativas ao Fundo de
            Garantia do Tempo de Serviço - FGTS.
        :ivar Id:
        """

        ideEvento: ESocial.EvtBasesFgts.IdeEvento = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideTrabalhador: ESocial.EvtBasesFgts.IdeTrabalhador = field(
            metadata={
                "type": "Element",
            }
        )
        infoFGTS: ESocial.EvtBasesFgts.InfoFgts = field(
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
        class IdeEvento(CommonMixin):
            """
            :ivar nrRecArqBase: Preencher com o número do recibo do arquivo que deu origem ao presente arquivo
                de retorno ao empregador. Validação: Deve ser um recibo de entrega válido, correspondente ao
                arquivo que deu origem ao presente arquivo de retorno (S-1200, S-2299, S-2399 ou S-3000).
            :ivar indApuracao:
            :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência das informações, se
                {indApuracao}(./indApuracao) for igual a [1], ou apenas o ano (formato AAAA), se
                {indApuracao}(./indApuracao) for igual a [2].
            """

            nrRecArqBase: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indApuracao: str = field(
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
        class IdeTrabalhador(CommonMixin):
            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )

        @dataclass(kw_only=True)
        class InfoFgts(CommonMixin):
            """
            :ivar dtVenc: Data de vencimento do FGTS mensal. Validação: Preencher somente se houver informação
                no grupo {infoBaseFGTS}(./ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS) e se
                {perApur}(5003_ideEvento_perApur) for anterior ao início do FGTS Digital. Se informada, deve
                corresponder ao dia 7 (sete) do mês subsequente ao indicado em
                {perApur}(5003_ideEvento_perApur), se esse dia for útil. Caso não seja, deve corresponder ao dia
                útil imediatamente anterior. Considera-se como dia não útil o sábado, o domingo e todo aquele
                constante do Calendário Nacional de feriados bancários divulgados pelo Banco Central do Brasil.
            :ivar classTrib:
            :ivar ideEstab: Identificação do estabelecimento DESCRICAO_COMPLETA:Identificação do estabelecimento
                ou obra de construção civil. CHAVE_GRUPO: {tpInsc}, {nrInsc}
            """

            dtVenc: None | XmlDate = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            classTrib: None | InfoFgtsClassTrib = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            ideEstab: list[ESocial.EvtBasesFgts.InfoFgts.IdeEstab] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class IdeEstab(CommonMixin):
                """
                :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.
                    Origem: campo {ideEstabLot/tpInsc} de: a) {infoPerApur}(1200_dmDev_infoPerApur) ou
                    {idePeriodo}(1200_dmDev_infoPerAnt_ideADC_idePeriodo) do S-1200; b)
                    {infoPerApur}(2299_infoDeslig_verbasResc_dmDev_infoPerApur) ou
                    {idePeriodo}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo) do S-2299; c)
                    {dmDev}(2399_infoTSVTermino_verbasResc_dmDev) do S-2399.
                :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideEstab/tpInsc}(./tpInsc). Origem: campo {ideEstabLot/nrInsc} de: a)
                    {infoPerApur}(1200_dmDev_infoPerApur) ou
                    {idePeriodo}(1200_dmDev_infoPerAnt_ideADC_idePeriodo) do S-1200; b)
                    {infoPerApur}(2299_infoDeslig_verbasResc_dmDev_infoPerApur) ou
                    {idePeriodo}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo) do S-2299; c)
                    {dmDev}(2399_infoTSVTermino_verbasResc_dmDev) do S-2399.
                :ivar ideLotacao: Identificação da lotação tributária. CHAVE_GRUPO: {codLotacao}, {tpLotacao},
                    {tpInsc}, {nrInsc}
                """

                tpInsc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                nrInsc: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                ideLotacao: list[ESocial.EvtBasesFgts.InfoFgts.IdeEstab.IdeLotacao] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                    },
                )

                @dataclass(kw_only=True)
                class IdeLotacao(CommonMixin):
                    """
                    :ivar codLotacao: Informar o código atribuído pelo empregador para a lotação tributária.
                        Origem: campo {ideEstabLot/codLotacao} de: a) {infoPerApur}(1200_dmDev_infoPerApur) ou
                        {idePeriodo}(1200_dmDev_infoPerAnt_ideADC_idePeriodo) do S-1200; b)
                        {infoPerApur}(2299_infoDeslig_verbasResc_dmDev_infoPerApur) ou
                        {idePeriodo}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo) do S-2299;
                        c) {dmDev}(2399_infoTSVTermino_verbasResc_dmDev) do S-2399.
                    :ivar tpLotacao: Preencher com o código correspondente ao tipo de lotação, conforme Tabela
                        10. Evento de origem: S-1020. Validação: a) Se origem de {codLotacao}(./codLotacao) for
                        {infoPerApur}(1200_dmDev_infoPerApur) do S-1200,
                        {infoPerApur}(2299_infoDeslig_verbasResc_dmDev_infoPerApur) do S-2299 ou
                        {dmDev}(2399_infoTSVTermino_verbasResc_dmDev) do S-2399, retornar o tipo de lotação
                        vigente em {perApur}(5003_ideEvento_perApur); b) Se origem de {codLotacao}(./codLotacao)
                        for {idePeriodo}(1200_dmDev_infoPerAnt_ideADC_idePeriodo) do S-1200, retornar o tipo de
                        lotação vigente em {perRef}(1200_dmDev_infoPerAnt_ideADC_idePeriodo_perRef) desse
                        evento; c) Se origem de {codLotacao}(./codLotacao) for
                        {idePeriodo}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo) do S-2299,
                        retornar o tipo de lotação vigente em
                        {perRef}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo_perRef) desse
                        evento.
                    :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela
                        05. Evento de origem: S-1020. Validação: a) Se origem de {codLotacao}(./codLotacao) for
                        {infoPerApur}(1200_dmDev_infoPerApur) do S-1200,
                        {infoPerApur}(2299_infoDeslig_verbasResc_dmDev_infoPerApur) do S-2299 ou
                        {dmDev}(2399_infoTSVTermino_verbasResc_dmDev) do S-2399, retornar o tipo de inscrição
                        vigente em {perApur}(5003_ideEvento_perApur); b) Se origem de {codLotacao}(./codLotacao)
                        for {idePeriodo}(1200_dmDev_infoPerAnt_ideADC_idePeriodo) do S-1200, retornar o tipo de
                        inscrição vigente em {perRef}(1200_dmDev_infoPerAnt_ideADC_idePeriodo_perRef) desse
                        evento; c) Se origem de {codLotacao}(./codLotacao) for
                        {idePeriodo}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo) do S-2299,
                        retornar o tipo de inscrição vigente em
                        {perRef}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo_perRef) desse
                        evento.
                    :ivar nrInsc: Preencher com o número de inscrição (CNPJ, CPF, CNO) ao qual pertence a
                        lotação tributária, conforme indicado na Tabela 10. Evento de origem: S-1020. Validação:
                        a) Se origem de {codLotacao}(./codLotacao) for {infoPerApur}(1200_dmDev_infoPerApur) do
                        S-1200, {infoPerApur}(2299_infoDeslig_verbasResc_dmDev_infoPerApur) do S-2299 ou
                        {dmDev}(2399_infoTSVTermino_verbasResc_dmDev) do S-2399, retornar o número de inscrição
                        vigente em {perApur}(5003_ideEvento_perApur); b) Se origem de {codLotacao}(./codLotacao)
                        for {idePeriodo}(1200_dmDev_infoPerAnt_ideADC_idePeriodo) do S-1200, retornar o número
                        de inscrição vigente em {perRef}(1200_dmDev_infoPerAnt_ideADC_idePeriodo_perRef) desse
                        evento; c) Se origem de {codLotacao}(./codLotacao) for
                        {idePeriodo}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo) do S-2299,
                        retornar o número de inscrição vigente em
                        {perRef}(2299_infoDeslig_verbasResc_dmDev_infoPerAnt_ideADC_idePeriodo_perRef) desse
                        evento.
                    :ivar infoTrabFGTS: Informações relativas à matrícula e categoria do trabalhador.
                        CHAVE_GRUPO: {matricula}, {codCateg}
                    """

                    codLotacao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    tpLotacao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    tpInsc: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    nrInsc: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoTrabFGTS: list[ESocial.EvtBasesFgts.InfoFgts.IdeEstab.IdeLotacao.InfoTrabFgts] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoTrabFgts(CommonMixin):
                        """
                        :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor
                            público, a matrícula constante no Sistema de Administração de Recursos Humanos do
                            órgão. Evento de origem: S-1200, S-2299, S-2399 ou S-3000. Validação: a) Se o evento
                            de origem for S-1200/S-2299/S-2399, retornar a matrícula informada nesse evento; b)
                            Se o evento de origem for S-3000, retornar a matrícula informada no evento objeto da
                            exclusão.
                        :ivar codCateg: Preencher com o código da categoria do trabalhador, conforme Tabela 01.
                            Evento de origem: S-1200, S-2299, S-2399 ou S-3000. Validação: a) Se o evento de
                            origem for S-1200, retornar o código de categoria informado nesse evento; b) Se o
                            evento de origem for S-2299 ou S-2399, retornar o código de categoria existente no
                            Registro de Eventos Trabalhistas - RET; c) Se o evento de origem for S-3000
                            (referente a exclusão de S-1200), retornar o código de categoria informado no evento
                            S-1200 (objeto da exclusão); d) Se o evento de origem for S-3000 (referente a
                            exclusão de S-2299 ou S-2399), retornar o código de categoria existente no RET
                            relativo ao contrato informado em S-2299 ou S-2399 (objeto da exclusão).
                        :ivar categOrig: Preencher com o código correspondente à categoria de origem do
                            dirigente sindical ou do trabalhador cedido. Origem: campo
                            {infoDirigenteSindical/categOrig}(2300_infoTSVInicio_infoComplementares_infoDirigenteSindical_categOrig),
                            {infoTrabCedido/categOrig}(2300_infoTSVInicio_infoComplementares_infoTrabCedido_categOrig)
                            ou
                            {infoMandElet/categOrig}(2300_infoTSVInicio_infoComplementares_infoMandElet_categOrig)
                            de S-2300.
                        :ivar tpRegTrab: Tipo de regime trabalhista. Validação: Deve corresponder ao tipo de
                            regime trabalhista existente no RET.
                        :ivar remunSuc: Indicar se a remuneração é relativa a verbas de natureza salarial ou não
                            salarial devidas pela empresa sucessora a empregados desligados ainda na sucedida.
                            Evento de origem: S-1200.
                        :ivar dtDeslig: Preencher com a data de desligamento do vínculo (último dia trabalhado).
                            Validação: Deve corresponder à data de desligamento existente no RET. Não retornar
                            caso haja reintegração com data posterior ao desligamento.
                        :ivar mtvDeslig:
                        :ivar dtTerm: Data do término. Validação: Deve corresponder à data do término existente
                            no RET.
                        :ivar mtvDesligTSV:
                        :ivar sucessaoVinc: Grupo de informações da sucessão de vínculo trabalhista
                            DESCRICAO_COMPLETA:Grupo de informações da sucessão de vínculo trabalhista. Evento
                            de origem: S-1200. CONDICAO_GRUPO: O (se {remunSuc}(../remunSuc) = [S]); N (nos
                            demais casos)
                        :ivar infoBaseFGTS: Bases de cálculo e valores do FGTS DESCRICAO_COMPLETA:Informações
                            referentes a bases de cálculo e valores do FGTS. CONDICAO_GRUPO: OC ((se
                            {codCateg}(../codCateg) = [1XX, 301, 302, 303, 304, 306, 307, 309, 310, 312] com
                            {tpRegTrab}(../tpRegTrab) = [1] ou não informado) OU (se {codCateg}(../codCateg) =
                            [201, 202, 721]) OU (se {codCateg}(../codCateg) = [401, 410] com
                            {categOrig}(../categOrig) = [1XX, 301, 302, 303, 304, 306, 307, 309, 310, 312] ou
                            não informada e com {tpRegTrab}(../tpRegTrab) = [1] ou não informado)); N (nos
                            demais casos)
                        :ivar procCS: Informação sobre processo judicial que suspende a exigibilidade da
                            Contribuição Social Rescisória DESCRICAO_COMPLETA:Informação sobre processo judicial
                            que suspende a exigibilidade da Contribuição Social Rescisória. Evento de origem:
                            S-2299. CONDICAO_GRUPO: OC
                        :ivar eConsignado:
                        """

                        matricula: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        codCateg: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        categOrig: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        tpRegTrab: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        remunSuc: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        dtDeslig: None | XmlDate = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        mtvDeslig: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "pattern": r"\d{2}",
                            },
                        )
                        dtTerm: None | XmlDate = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        mtvDesligTSV: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "pattern": r"\d{2}",
                            },
                        )
                        sucessaoVinc: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        infoBaseFGTS: (
                            None | ESocial.EvtBasesFgts.InfoFgts.IdeEstab.IdeLotacao.InfoTrabFgts.InfoBaseFgts
                        ) = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        procCS: None | ESocial.EvtBasesFgts.InfoFgts.IdeEstab.IdeLotacao.InfoTrabFgts.ProcCs = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        eConsignado: list[
                            ESocial.EvtBasesFgts.InfoFgts.IdeEstab.IdeLotacao.InfoTrabFgts.EConsignado
                        ] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                            },
                        )

                        @dataclass(kw_only=True)
                        class InfoBaseFgts(CommonMixin):
                            """
                            :ivar basePerApur: Bases de cálculo e valores, exceto se {tpAcConv} = [E, H, I]
                                DESCRICAO_COMPLETA:Informações sobre bases de cálculo e valores do FGTS
                                referentes à remuneração do período de apuração e de períodos anteriores, exceto
                                se {tpAcConv} = [E, H, I]. Evento de origem: S-1200, S-2299 ou S-2399.
                                CHAVE_GRUPO: {tpValor}, {indIncid}, {notAFT}, {natRubr} CONDICAO_GRUPO: OC
                            :ivar infoBasePerAntE: Informações sobre bases e valores do FGTS quando
                                {tpAcConv}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_infoBasePerAntE_tpAcConv)
                                = [E, H, I] DESCRICAO_COMPLETA:Informações referentes a bases de cálculo e
                                valores do FGTS de períodos anteriores quando {tpAcConv}(./tpAcConv) = [E, H,
                                I]. CHAVE_GRUPO: {perRef}, {tpAcConv} CONDICAO_GRUPO: OC
                            """

                            basePerApur: list[
                                ESocial.EvtBasesFgts.InfoFgts.IdeEstab.IdeLotacao.InfoTrabFgts.InfoBaseFgts.BasePerApur
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 99,
                                },
                            )
                            infoBasePerAntE: list[
                                ESocial.EvtBasesFgts.InfoFgts.IdeEstab.IdeLotacao.InfoTrabFgts.InfoBaseFgts.InfoBasePerAntE
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 180,
                                },
                            )

                            @dataclass(kw_only=True)
                            class BasePerApur(CommonMixin):
                                """
                                :ivar tpValor:
                                :ivar indIncid:
                                :ivar remFGTS: Remuneração (valor da base de cálculo) do FGTS, conforme definido
                                    nos campos {tpValor}(./tpValor) e {indIncid}(./indIncid). Validação: Deve
                                    ser maior que 0 (zero). Deve corresponder ao somatório dos valores
                                    informados no campo {vrRubr} em S-1200 e S-2299 (grupos {infoPerApur} e
                                    {infoPerAnt}, quando {tpAcConv} for diferente de [E, H, I]), e também em
                                    S-2399, devendo somar os valores das rubricas cujo
                                    {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual
                                    a [1, 3] e subtrair os valores das rubricas cujo
                                    {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual
                                    a [2, 4], observando a Tabela 23.
                                :ivar dpsFGTS: Valor histórico do FGTS a ser depositado na conta vinculada do
                                    trabalhador. Validação: Deve ser maior que 0 (zero) e informado somente se
                                    {indIncid}(./indIncid) = [1]. Deve corresponder à multiplicação de
                                    {remFGTS}(./remFGTS) pela alíquota abaixo: a) Se {tpValor}(./tpValor) = [11,
                                    12, 13, 14, 21, 22, 23, 24, 25, 26], alíquota de 8%; b) Se
                                    {tpValor}(./tpValor) = [15, 16, 17, 18, 27, 28, 29, 30, 31, 32], alíquota de
                                    2%; c) Se {tpValor}(./tpValor) = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                                    alíquota de 3,2%.
                                :ivar notAFT: Número da notificação de FGTS que deu origem à confissão. Evento
                                    de origem: S-1200, S-2299 ou S-2399.
                                :ivar natRubr: Informar o código de classificação da rubrica. Evento de origem:
                                    S-1010. Validação: Retornar somente se {notAFT}(./notAFT) for informado.
                                :ivar detRubrSusp: Detalhamento da(s) rubrica(s) com incidência de FGTS suspensa
                                    DESCRICAO_COMPLETA:Detalhamento da(s) rubrica(s) com incidência de FGTS
                                    suspensa em decorrência de decisão judicial. CHAVE_GRUPO: {codRubr},
                                    {ideTabRubr} CONDICAO_GRUPO: O (se {indIncid}(../indIncid) = [9]); N (nos
                                    demais casos)
                                """

                                tpValor: BasePerApurTpValor = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                indIncid: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                remFGTS: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                dpsFGTS: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                notAFT: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                natRubr: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                detRubrSusp: list[TDetRubrSusp] = field(
                                    default_factory=list,
                                    metadata={
                                        "type": "Element",
                                    },
                                )

                            @dataclass(kw_only=True)
                            class InfoBasePerAntE(CommonMixin):
                                """
                                :ivar perRef: Informar o período ao qual se refere a remuneração, no formato
                                    AAAA-MM. Evento de origem: S-1200 ou S-2299. Validação: Deve corresponder ao
                                    período informado no evento de origem.
                                :ivar tpAcConv:
                                :ivar basePerAntE: Bases de cálculo e valores quando
                                    {tpAcConv}(5003_infoFGTS_ideEstab_ideLotacao_infoTrabFGTS_infoBaseFGTS_infoBasePerAntE_tpAcConv)
                                    = [E, H, I] DESCRICAO_COMPLETA:Informações sobre bases de cálculo e valores
                                    do FGTS referentes à remuneração de períodos anteriores quando
                                    {tpAcConv}(../tpAcConv) = [E, H, I]. CHAVE_GRUPO: {tpValorE}, {indIncidE}
                                """

                                perRef: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                tpAcConv: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                basePerAntE: list[
                                    ESocial.EvtBasesFgts.InfoFgts.IdeEstab.IdeLotacao.InfoTrabFgts.InfoBaseFgts.InfoBasePerAntE.BasePerAntE
                                ] = field(
                                    default_factory=list,
                                    metadata={
                                        "type": "Element",
                                        "min_occurs": 1,
                                        "max_occurs": 99,
                                    },
                                )

                                @dataclass(kw_only=True)
                                class BasePerAntE(CommonMixin):
                                    """
                                    :ivar tpValorE: Tipo de valor que influi na apuração do FGTS.
                                    :ivar indIncidE: Indicativo de incidência de FGTS. Validação: Se
                                        {codIncFGTS}(1010_infoRubrica_inclusao_dadosRubrica_codIncFGTS) em
                                        S-1010 for igual a [11, 12, 21], deve ser retornado [1]. Se
                                        {codIncFGTS}(1010_infoRubrica_inclusao_dadosRubrica_codIncFGTS) em
                                        S-1010 for igual a [91, 92, 93], deve ser retornado [9].
                                    :ivar remFGTSE: Remuneração (valor da base de cálculo) do FGTS, conforme
                                        definido nos campos {tpValorE}(./tpValorE) e {indIncidE}(./indIncidE).
                                        Validação: Deve ser maior que 0 (zero). Deve corresponder ao somatório
                                        dos valores informados no campo {vrRubr} em S-1200 e S-2299 (grupo
                                        {infoPerAnt}, agrupado por {tpAcConv}(../tpAcConv)), devendo somar os
                                        valores das rubricas cujo
                                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja
                                        igual a [1, 3] e subtrair os valores das rubricas cujo
                                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja
                                        igual a [2, 4], observando a Tabela 23.
                                    :ivar dpsFGTSE: Valor histórico do FGTS a ser depositado na conta vinculada
                                        do trabalhador. Validação: Deve ser maior que 0 (zero) e informado
                                        somente se {indIncidE}(./indIncidE) = [1]. Deve corresponder à
                                        multiplicação de {remFGTSE}(./remFGTSE) pela alíquota abaixo: a) Se
                                        {tpValorE}(./tpValorE) = [13, 14, 24, 25, 26], alíquota de 8%; b) Se
                                        {tpValorE}(./tpValorE) = [17, 18, 30, 31, 32], alíquota de 2%; c) Se
                                        {tpValorE}(./tpValorE) = [43, 44, 48, 49, 50], alíquota de 3,2%.
                                    :ivar detRubrSusp: Detalhamento da(s) rubrica(s) com incidência de FGTS
                                        suspensa DESCRICAO_COMPLETA:Detalhamento da(s) rubrica(s) com incidência
                                        de FGTS suspensa em decorrência de decisão judicial. CHAVE_GRUPO:
                                        {codRubr}, {ideTabRubr} CONDICAO_GRUPO: O (se {indIncidE}(../indIncidE)
                                        = [9]); N (nos demais casos)
                                    """

                                    tpValorE: str = field(
                                        metadata={
                                            "type": "Element",
                                        }
                                    )
                                    indIncidE: str = field(
                                        metadata={
                                            "type": "Element",
                                        }
                                    )
                                    remFGTSE: str = field(
                                        metadata={
                                            "type": "Element",
                                        }
                                    )
                                    dpsFGTSE: None | str = field(
                                        default=None,
                                        metadata={
                                            "type": "Element",
                                        },
                                    )
                                    detRubrSusp: list[TDetRubrSusp] = field(
                                        default_factory=list,
                                        metadata={
                                            "type": "Element",
                                        },
                                    )

                        @dataclass(kw_only=True)
                        class ProcCs(CommonMixin):
                            """
                            :ivar nrProcJud: Informar o número de processo judicial cadastrado.
                            """

                            nrProcJud: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

                        @dataclass(kw_only=True)
                        class EConsignado(CommonMixin):
                            """
                            Informações relativas ao desconto do eConsignado DESCRICAO_COMPLETA:Informações
                            relativas ao desconto do eConsignado.

                            DESCRICAO_COMPLETA:As inclusões, alterações ou exclusões dos dados que compõem este
                            grupo não surtirão efeito se a guia já estiver paga ou vencida. CHAVE_GRUPO:
                            {instFinanc}, {nrContrato} CONDICAO_GRUPO: O (se existir rubrica com
                            {codIncFGTS}(1010_infoRubrica_inclusao_dadosRubrica_codIncFGTS) em S-1010 igual a [31]
                            e {perApur}(5003_ideEvento_perApur) maior ou igual a data de início do eConsignado no
                            eSocial); N (nos demais casos).

                            :ivar instFinanc:
                            :ivar nrContrato:
                            :ivar vreConsignado: Valor do desconto do empréstimo eConsignado. Origem: soma das
                                rubricas com {codIncFGTS}(1010_infoRubrica_inclusao_dadosRubrica_codIncFGTS) em
                                S-1010 igual a [31].
                            """

                            instFinanc: str = field(
                                metadata={
                                    "type": "Element",
                                    "pattern": r"\d{3}",
                                }
                            )
                            nrContrato: str = field(
                                metadata={
                                    "type": "Element",
                                    "min_length": 2,
                                    "max_length": 15,
                                    "pattern": r"[A-Za-z0-9][-_A-Za-z0-9/.//]{0,13}[A-Za-z0-9]",
                                }
                            )
                            vreConsignado: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
