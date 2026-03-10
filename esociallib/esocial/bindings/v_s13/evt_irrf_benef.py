from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_03_00"


class DmDevTpPgto(Enum):
    """
    Informar o evento de origem do pagamento.

    Origem: campo {tpPgto}(1210_ideBenef_infoPgto_tpPgto) de S-1210.

    :cvar VALUE_1: S-1200
    :cvar VALUE_2: S-2299
    :cvar VALUE_3: S-2399
    :cvar VALUE_4: S-1202
    :cvar VALUE_5: S-1207
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class InfoIrTpInfoIr(Enum):
    """
    Consolidação dos tipos de valores relativos ao IRRF.

    :cvar VALUE_11: Rendimentos tributáveis: Remuneração mensal
    :cvar VALUE_12: 13º salário
    :cvar VALUE_14: PLR
    :cvar VALUE_31: Retenções do IRRF efetuadas sobre: Remuneração mensal
    :cvar VALUE_32: 13º salário
    :cvar VALUE_34: PLR
    :cvar VALUE_41: Deduções da base de cálculo do IRRF: Previdência Social Oficial - PSO - Remuneração mensal
    :cvar VALUE_42: PSO - 13º salário
    :cvar VALUE_46: Previdência complementar - Salário mensal
    :cvar VALUE_47: Previdência complementar - 13º salário
    :cvar VALUE_51: Pensão alimentícia - Remuneração mensal
    :cvar VALUE_52: Pensão alimentícia - 13º salário
    :cvar VALUE_54: Pensão alimentícia - PLR
    :cvar VALUE_61: Fundo de Aposentadoria Programada Individual - FAPI - Remuneração mensal
    :cvar VALUE_62: Fundo de Aposentadoria Programada Individual - FAPI - 13º salário
    :cvar VALUE_63: Fundação de previdência complementar do servidor público - Remuneração mensal
    :cvar VALUE_64: Fundação de previdência complementar do servidor público - 13º salário
    :cvar VALUE_67: Plano privado coletivo de assistência à saúde
    :cvar VALUE_68: Desconto simplificado mensal
    :cvar VALUE_70: Rendimento não tributável ou isento do IRRF: Parcela isenta 65 anos - Remuneração mensal
    :cvar VALUE_71: Parcela isenta 65 anos - 13º salário
    :cvar VALUE_72: Diárias
    :cvar VALUE_73: Ajuda de custo
    :cvar VALUE_74: Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho
    :cvar VALUE_75: Abono pecuniário
    :cvar VALUE_76: Rendimento de beneficiário com moléstia grave ou acidente em serviço - Remuneração mensal
    :cvar VALUE_77: Rendimento de beneficiário com moléstia grave ou acidente em serviço - 13º salário
    :cvar VALUE_700: Auxílio moradia
    :cvar VALUE_701: Parte não tributável do valor de serviço de transporte de passageiros ou cargas
    :cvar VALUE_702: Bolsa médico residente - remuneração mensal
    :cvar VALUE_703: Bolsa médico residente - 13º salário
    :cvar VALUE_704: Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de
        emprego, cargo ou função.
    :cvar VALUE_79: Outras isenções
    :cvar VALUE_7900: Verba transitada pela folha de pagamento de natureza diversa de rendimento ou
        retenção/isenção/dedução de IR (exemplo: desconto de convênio farmácia, desconto de consignações, etc.)
    :cvar VALUE_7950: Códigos para compatibilidade de versões anteriores: Rendimento não tributável
    :cvar VALUE_7951: Rendimento não tributável em função de acordos internacionais de bitributação
    :cvar VALUE_7952: Rendimento tributável - RRA
    :cvar VALUE_7953: Retenção de IR - RRA
    :cvar VALUE_7954: Previdência Social Oficial - RRA
    :cvar VALUE_7955: Pensão alimentícia - RRA
    :cvar VALUE_7956: Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-
        labore e aluguéis
    :cvar VALUE_7957: Depósito judicial
    :cvar VALUE_7958: Compensação judicial do ano-calendário
    :cvar VALUE_7959: Compensação judicial de anos anteriores
    :cvar VALUE_7960: Exigibilidade suspensa - Remuneração mensal
    :cvar VALUE_7961: Exigibilidade suspensa - 13º salário
    :cvar VALUE_7962: Exigibilidade suspensa - Férias
    :cvar VALUE_7963: Exigibilidade suspensa - PLR
    :cvar VALUE_7964: Exigibilidade suspensa - RRA
    :cvar VALUE_9011: Exigibilidade suspensa - Rendimento tributável (base de cálculo do IR): Remuneração mensal
    :cvar VALUE_9012: 13º salário
    :cvar VALUE_9014: PLR
    :cvar VALUE_9031: Exigibilidade suspensa - Retenção do IRRF efetuada sobre: Remuneração mensal
    :cvar VALUE_9032: 13º salário
    :cvar VALUE_9034: PLR
    :cvar VALUE_9831: Depósito judicial - Mensal
    :cvar VALUE_9832: Depósito judicial - 13º salário
    :cvar VALUE_9834: Depósito judicial - PLR
    :cvar VALUE_9041: Exigibilidade suspensa - Dedução da base de cálculo do IRRF: Previdência Social Oficial -
        PSO - Remuneração mensal
    :cvar VALUE_9042: PSO - 13º salário
    :cvar VALUE_9046: Previdência complementar - Salário mensal
    :cvar VALUE_9047: Previdência complementar - 13º salário
    :cvar VALUE_9051: Pensão alimentícia - Remuneração mensal
    :cvar VALUE_9052: Pensão alimentícia - 13º salário
    :cvar VALUE_9054: Pensão alimentícia - PLR
    :cvar VALUE_9061: Fundo de Aposentadoria Programada Individual - FAPI - Remuneração mensal
    :cvar VALUE_9062: Fundo de Aposentadoria Programada Individual - FAPI - 13º salário
    :cvar VALUE_9063: Fundação de previdência complementar do servidor público - Remuneração mensal
    :cvar VALUE_9064: Fundação de previdência complementar do servidor público - 13º salário
    :cvar VALUE_9067: Plano privado coletivo de assistência à saúde
    :cvar VALUE_9082: Compensação judicial: Compensação judicial do ano-calendário
    :cvar VALUE_9083: Compensação judicial de anos anteriores
    """

    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_14 = 14
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_34 = 34
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_54 = 54
    VALUE_61 = 61
    VALUE_62 = 62
    VALUE_63 = 63
    VALUE_64 = 64
    VALUE_67 = 67
    VALUE_68 = 68
    VALUE_70 = 70
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_74 = 74
    VALUE_75 = 75
    VALUE_76 = 76
    VALUE_77 = 77
    VALUE_700 = 700
    VALUE_701 = 701
    VALUE_702 = 702
    VALUE_703 = 703
    VALUE_704 = 704
    VALUE_79 = 79
    VALUE_7900 = 7900
    VALUE_7950 = 7950
    VALUE_7951 = 7951
    VALUE_7952 = 7952
    VALUE_7953 = 7953
    VALUE_7954 = 7954
    VALUE_7955 = 7955
    VALUE_7956 = 7956
    VALUE_7957 = 7957
    VALUE_7958 = 7958
    VALUE_7959 = 7959
    VALUE_7960 = 7960
    VALUE_7961 = 7961
    VALUE_7962 = 7962
    VALUE_7963 = 7963
    VALUE_7964 = 7964
    VALUE_9011 = 9011
    VALUE_9012 = 9012
    VALUE_9014 = 9014
    VALUE_9031 = 9031
    VALUE_9032 = 9032
    VALUE_9034 = 9034
    VALUE_9831 = 9831
    VALUE_9832 = 9832
    VALUE_9834 = 9834
    VALUE_9041 = 9041
    VALUE_9042 = 9042
    VALUE_9046 = 9046
    VALUE_9047 = 9047
    VALUE_9051 = 9051
    VALUE_9052 = 9052
    VALUE_9054 = 9054
    VALUE_9061 = 9061
    VALUE_9062 = 9062
    VALUE_9063 = 9063
    VALUE_9064 = 9064
    VALUE_9067 = 9067
    VALUE_9082 = 9082
    VALUE_9083 = 9083


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-5002 - Imposto de Renda Retido na Fonte por Trabalhador.

    :ivar evtIrrfBenef: Evento IRRF por Trabalhador DESCRICAO_COMPLETA:Evento Imposto de Renda Retido na Fonte
        por Trabalhador. CHAVE_GRUPO: {Id}
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtIrrfBenef/v_S_01_03_00"

    evtIrrfBenef: ESocial.EvtIrrfBenef = field(
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
    class EvtIrrfBenef(CommonMixin):
        """
        :ivar ideEvento: Identificação do evento de retorno. CHAVE_GRUPO: {perApur*}
        :ivar ideEmpregador:
        :ivar ideTrabalhador: Identificação do beneficiário DESCRICAO_COMPLETA:Identificação do beneficiário do
            pagamento. CHAVE_GRUPO: {cpfBenef*}
        :ivar Id:
        """

        ideEvento: ESocial.EvtIrrfBenef.IdeEvento = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideTrabalhador: ESocial.EvtIrrfBenef.IdeTrabalhador = field(
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
                de retorno ao empregador. Validação: Deve corresponder ao recibo de um arquivo com informações
                de rendimentos sujeitos a Imposto de Renda Retido na Fonte - IRRF (S-1210 ou S-3000).
            :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência das informações.
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
        class IdeTrabalhador(CommonMixin):
            """
            :ivar cpfBenef: Número de inscrição no Cadastro de Pessoas Físicas - CPF do beneficiário do
                pagamento. Origem: campo {cpfBenef}(1210_ideBenef_cpfBenef) de S-1210.
            :ivar dmDev: Informações do demonstrativo de valores devidos. CHAVE_GRUPO: {perRef}, {ideDmDev},
                {tpPgto} CONDICAO_GRUPO: OC
            :ivar totInfoIR: Totalização dos demonstrativos de valores devidos DESCRICAO_COMPLETA: Totais dos
                rendimentos tributáveis, deduções e isenções para todos os demonstrativos. CONDICAO_GRUPO: OC
            :ivar infoIRComplem: Informações complementares para a DIRF ou para a DAA, com a legislação aplicada
                ao imposto de renda. CHAVE_GRUPO: {perAnt_perRefAjuste} CONDICAO_GRUPO: OC
            """

            cpfBenef: str = field(
                metadata={
                    "type": "Element",
                }
            )
            dmDev: list[ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            totInfoIR: None | ESocial.EvtIrrfBenef.IdeTrabalhador.TotInfoIr = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoIRComplem: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 13,
                },
            )

            @dataclass(kw_only=True)
            class DmDev(CommonMixin):
                """
                :ivar perRef: Período de referência das informações, no formato AAAA-MM (ou AAAA, se for
                    relativo a 13° salário). Origem: campo {perRef}(1210_ideBenef_infoPgto_perRef) de S-1210.
                :ivar ideDmDev: Identificador atribuído pela fonte pagadora para o demonstrativo de valores
                    devidos ao trabalhador. Origem: campo {ideDmDev}(1210_ideBenef_infoPgto_ideDmDev) de S-1210.
                :ivar tpPgto:
                :ivar dtPgto: Informar a data de pagamento. Origem: campo
                    {dtPgto}(1210_ideBenef_infoPgto_dtPgto) de S-1210.
                :ivar codCateg: Preencher com o código da categoria do trabalhador, conforme Tabela 01.
                    Validação: a) Se {tpPgto}(./tpPgto) = [1, 4], retornar o código de categoria informado no
                    evento de origem; b) Se {tpPgto}(./tpPgto) = [2, 3], retornar o código de categoria
                    existente no Registro de Eventos Trabalhistas - RET; c) Se {tpPgto}(./tpPgto) = [5],
                    retornar [000].
                :ivar infoIR: Rendimentos tributáveis, deduções, isenções e retenções do IRRF. CHAVE_GRUPO:
                    {tpInfoIR}
                :ivar totApurMen: Totalizador dos rendimentos tributáveis, deduções, isenções e retenção de
                    tributos com período de apuração mensal. CHAVE_GRUPO: {CRMen} CONDICAO_GRUPO: OC
                :ivar totApurDia: Totalizador de rendimentos tributáveis e tributos com período de apuração
                    diário. CHAVE_GRUPO: {perApurDia}, {CRDia}, {frmTribut}, {paisResidExt} CONDICAO_GRUPO: OC
                    Validação: Em uma mesma ocorrência deste grupo, se {perApur}(5002_ideEvento_perApur) for
                    igual ou posterior ao início da DIRF, deve haver compatibilidade entre a forma de tributação
                    e o tipo de rendimento (tributável ou isento/não tributável).
                :ivar infoRRA: Informações complementares - RRA. DESCRICAO_COMPLETA:Informações complementares
                    relativas a Rendimentos Recebidos Acumuladamente - RRA. Origem: Evento remuneratório
                    (S-1200, S-1202, S-1207, S-2299 ou S-2399) relacionado no evento S-1210 por
                    {tpPgto}(1210_ideBenef_infoPgto_tpPgto), {perRef}(1210_ideBenef_infoPgto_perRef) e
                    {ideDmDev}(1210_ideBenef_infoPgto_ideDmDev). CONDICAO_GRUPO: OC
                :ivar infoPgtoExt: Informações complementares relativas a pagamentos no exterior
                    DESCRICAO_COMPLETA:Informações complementares relativas a pagamentos a residente fiscal no
                    exterior. Evento de origem: S-1210 CONDICAO_GRUPO: OC
                """

                perRef: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                ideDmDev: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                tpPgto: DmDevTpPgto = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtPgto: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                codCateg: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                infoIR: list[ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.InfoIr] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 999,
                    },
                )
                totApurMen: list[ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.TotApurMen] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 50,
                    },
                )
                totApurDia: list[ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.TotApurDia] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 350,
                    },
                )
                infoRRA: None | ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.InfoRra = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoPgtoExt: None | ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.InfoPgtoExt = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoIr(CommonMixin):
                    """
                    :ivar tpInfoIR:
                    :ivar valor: Composição do valor do rendimento tributável, não tributável, retenção, dedução
                        ou isenção do IRRF, de acordo com a classificação apresentada no campo
                        {tpInfoIR}(./tpInfoIR). Validação: Deve corresponder ao somatório dos valores informados
                        nas rubricas (campo {vrRubr}) dos eventos que deram origem ao S-1210 (grupos
                        {infoPerApur} e {infoPerAnt} do S-1200, S-1202, S-1207 e S-2299, e grupo {verbasResc} do
                        S-2399), desde que o campo {indApurIR} vinculado às respectivas rubricas seja igual a
                        [0] ou não informado, obedecendo ao que segue: a) Somar os valores das rubricas cujo
                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a [1, 3] e
                        subtrair os valores das rubricas cujo
                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a [2, 4],
                        observando a tabela de relacionamento abaixo: {tpInfoIR}(./tpInfoIR) = [11],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [11, 13];
                        {tpInfoIR}(./tpInfoIR) = [12],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [12];
                        {tpInfoIR}(./tpInfoIR) = [14],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [14];
                        {tpInfoIR}(./tpInfoIR) = [70],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [70];
                        {tpInfoIR}(./tpInfoIR) = [71],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [71];
                        {tpInfoIR}(./tpInfoIR) = [72],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [72];
                        {tpInfoIR}(./tpInfoIR) = [73],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [73];
                        {tpInfoIR}(./tpInfoIR) = [74],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [74];
                        {tpInfoIR}(./tpInfoIR) = [75],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [75];
                        {tpInfoIR}(./tpInfoIR) = [76],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [76];
                        {tpInfoIR}(./tpInfoIR) = [77],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [77];
                        {tpInfoIR}(./tpInfoIR) = [700],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [700];
                        {tpInfoIR}(./tpInfoIR) = [701],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [701];
                        {tpInfoIR}(./tpInfoIR) = [702],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [702];
                        {tpInfoIR}(./tpInfoIR) = [703],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [703];
                        {tpInfoIR}(./tpInfoIR) = [704],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [704];
                        {tpInfoIR}(./tpInfoIR) = [79],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [79];
                        {tpInfoIR}(./tpInfoIR) = [7900],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9];
                        {tpInfoIR}(./tpInfoIR) = [7950],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [0];
                        {tpInfoIR}(./tpInfoIR) = [7951],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [1];
                        {tpInfoIR}(./tpInfoIR) = [7952],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [15];
                        {tpInfoIR}(./tpInfoIR) = [7956],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [78];
                        {tpInfoIR}(./tpInfoIR) = [7960],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [91];
                        {tpInfoIR}(./tpInfoIR) = [7961],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [92];
                        {tpInfoIR}(./tpInfoIR) = [7962],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [93];
                        {tpInfoIR}(./tpInfoIR) = [7963],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [94];
                        {tpInfoIR}(./tpInfoIR) = [7964],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [95];
                        {tpInfoIR}(./tpInfoIR) = [9011],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9011,
                        9013]; {tpInfoIR}(./tpInfoIR) = [9012],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9012];
                        {tpInfoIR}(./tpInfoIR) = [9014],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9014]. b)
                        Somar os valores das rubricas cujo
                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a [2, 4] e
                        subtrair os valores das rubricas cujo
                        {tpRubr}(1010_infoRubrica_inclusao_dadosRubrica_tpRubr) em S-1010 seja igual a [1, 3],
                        observando a tabela de relacionamento abaixo: {tpInfoIR}(./tpInfoIR) = [31],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [31, 33];
                        {tpInfoIR}(./tpInfoIR) = [32],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [32];
                        {tpInfoIR}(./tpInfoIR) = [34],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [34];
                        {tpInfoIR}(./tpInfoIR) = [41],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [41, 43];
                        {tpInfoIR}(./tpInfoIR) = [42],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [42];
                        {tpInfoIR}(./tpInfoIR) = [46],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [46, 48];
                        {tpInfoIR}(./tpInfoIR) = [47],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [47];
                        {tpInfoIR}(./tpInfoIR) = [51],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [51, 53];
                        {tpInfoIR}(./tpInfoIR) = [52],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [52];
                        {tpInfoIR}(./tpInfoIR) = [54],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [54];
                        {tpInfoIR}(./tpInfoIR) = [61],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [61, 66];
                        {tpInfoIR}(./tpInfoIR) = [62],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [62];
                        {tpInfoIR}(./tpInfoIR) = [63],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [63, 65];
                        {tpInfoIR}(./tpInfoIR) = [64],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [64];
                        {tpInfoIR}(./tpInfoIR) = [67],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [67];
                        {tpInfoIR}(./tpInfoIR) = [68],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [68];
                        {tpInfoIR}(./tpInfoIR) = [7953],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [35];
                        {tpInfoIR}(./tpInfoIR) = [7954],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [44];
                        {tpInfoIR}(./tpInfoIR) = [7955],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [55];
                        {tpInfoIR}(./tpInfoIR) = [7957],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [81];
                        {tpInfoIR}(./tpInfoIR) = [7958],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [82];
                        {tpInfoIR}(./tpInfoIR) = [7959],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [83];
                        {tpInfoIR}(./tpInfoIR) = [9031],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9031,
                        9033]; {tpInfoIR}(./tpInfoIR) = [9032],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9032];
                        {tpInfoIR}(./tpInfoIR) = [9034],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9034];
                        {tpInfoIR}(./tpInfoIR) = [9831],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9831,
                        9833]; {tpInfoIR}(./tpInfoIR) = [9832],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9832];
                        {tpInfoIR}(./tpInfoIR) = [9834],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9834];
                        {tpInfoIR}(./tpInfoIR) = [9041],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9041,
                        9043]; {tpInfoIR}(./tpInfoIR) = [9042],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9042];
                        {tpInfoIR}(./tpInfoIR) = [9046],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9046,
                        9048]; {tpInfoIR}(./tpInfoIR) = [9047],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9047];
                        {tpInfoIR}(./tpInfoIR) = [9051],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9051,
                        9053]; {tpInfoIR}(./tpInfoIR) = [9052],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9052];
                        {tpInfoIR}(./tpInfoIR) = [9054],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9054];
                        {tpInfoIR}(./tpInfoIR) = [9061],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9061,
                        9066]; {tpInfoIR}(./tpInfoIR) = [9062],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9062];
                        {tpInfoIR}(./tpInfoIR) = [9063],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9063,
                        9065]; {tpInfoIR}(./tpInfoIR) = [9064],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9064];
                        {tpInfoIR}(./tpInfoIR) = [9067],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9067];
                        {tpInfoIR}(./tpInfoIR) = [9082],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9082];
                        {tpInfoIR}(./tpInfoIR) = [9083],
                        {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) em S-1010 = [9083].
                        OBS.: Se o campo {indApurIR} vinculado à rubrica for igual a [1], considerar {vrRubr} =
                        [0].
                    :ivar descRendimento:
                    :ivar infoProcJudRub: Informações complementares - Demais rendimentos com exigibilidade
                        suspensa decorrentes de decisão judicial aplicável à rubrica. CHAVE_GRUPO: {nrProc}
                        CONDICAO_GRUPO: OC
                    """

                    tpInfoIR: InfoIrTpInfoIr = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    valor: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    descRendimento: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 100,
                        },
                    )
                    infoProcJudRub: list[ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.InfoIr.InfoProcJudRub] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoProcJudRub(CommonMixin):
                        """
                        :ivar nrProc: Informar o número do processo judicial. Origem: Campo
                            {ideProcessoIRRF/nrProc}(1010_infoRubrica_inclusao_dadosRubrica_ideProcessoIRRF_nrProc)
                            de S-1010, quando {codRubr}(1010_infoRubrica_inclusao_ideRubrica_codRubr) e
                            {ideTabRubr}(1010_infoRubrica_inclusao_ideRubrica_ideTabRubr) de S-1010 com
                            {codIncIRRF}(1010_infoRubrica_inclusao_dadosRubrica_codIncIRRF) = [9X] ou [9XXX]
                            forem informados em {ideDmDev} de evento remuneratório (S-1200, S-1202, S-1207,
                            S-2299 ou S-2399).
                        :ivar ufVara: Identificação da Unidade da Federação - UF da Seção Judiciária. Origem:
                            campo {ufVara}(1070_infoProcesso_inclusao_dadosProc_dadosProcJud_ufVara) de S-1070.
                        :ivar codMunic: Preencher com o código do município, conforme tabela do IBGE. Origem:
                            campo {codMunic}(1070_infoProcesso_inclusao_dadosProc_dadosProcJud_codMunic) de
                            S-1070.
                        :ivar idVara:
                        """

                        nrProc: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        ufVara: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        codMunic: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        idVara: str = field(
                            metadata={
                                "type": "Element",
                                "pattern": r"\d{1,4}",
                            }
                        )

                @dataclass(kw_only=True)
                class TotApurMen(CommonMixin):
                    """
                    :ivar CRMen:
                    :ivar vlrRendTrib: Valor relativo ao rendimento tributável mensal e férias. Validação: Deve
                        ser agrupado conforme segue: a) Quando o evento de origem for S-1200, S-1202, S-2299,
                        S-2399 e respectivo S-1210: {}(./CRMen) = [056107]: se {}(../codCateg) = [101, 102, 103,
                        105, 106, 107, 108, 111, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312,
                        313, 314, 401, 410, 501, 721, 722, 723, 761, 901, 902, 903, 904, 906], {indApurIR} =
                        [0], os campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        for diferente de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [11]; {}(./CRMen) = [056108]: se {}(../codCateg) =
                        [104], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [11];
                        {}(./CRMen) = [056111]: se {}(../codCateg) = [101, 102, 103, 105, 106, 107, 108, 111],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [11]; {}(./CRMen) = [058806]: se {}(../codCateg) = [201, 202, 701, 711, 712, 731, 734,
                        738, 741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [11];
                        {}(./CRMen) = [061001]: se {}(../codCateg) = [712], {indApurIR} = [0] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) = [586], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [11]; {}(./CRMen) =
                        [356201]: se {}(../codCateg) = [1XX], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [14];
                        {}(./CRMen) = [188901]: se {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for
                        informado, {indApurIR} = [0] e {indRRA} = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [11, 12, 14]. b) Quando o
                        evento de origem for S-1207 e respectivo S-1210: {}(./CRMen) = [353301]: se {indApurIR}
                        = [0] e os campos {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e {indRRA} não
                        forem informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [11, 14]; {}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for informado, {indApurIR} = [0]
                        e {indRRA} = [S], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [11, 12, 14].
                    :ivar vlrRendTrib13: Valor relativo ao rendimento do 13º salário. Validação: Deve ser
                        agrupado conforme segue: a) Quando o evento de origem for S-1200, S-1202, S-2299, S-2399
                        e respectivo S-1210: {}(./CRMen) = [056107]: se {}(../codCateg) = [101, 102, 103, 105,
                        106, 107, 108, 111, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313,
                        314, 401, 410, 501, 721, 722, 723, 761, 901, 902, 903, 904, 906], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        for diferente de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [12]; {}(./CRMen) = [056109]: se {}(../codCateg) =
                        [104], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [12], apenas
                        se origem for S-2299; {}(./CRMen) = [056110]: se codCateg = [104], {indApurIR} = [0] e
                        os campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [12], exceto se origem for S-2299; {}(./CRMen) =
                        [056112]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        = [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [12], exceto se origem for S-2299/S-2399; {}(./CRMen) =
                        [056113]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        = [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [12], apenas se origem for S-2299/S-2399; {}(./CRMen) =
                        [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738, 741, 751, 771, 781],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [12]. b)
                        Quando o evento de origem for S-1207 e respectivo S-1210: {}(./CRMen) = [353301]: se
                        {indApurIR} = [0] e os campos {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e
                        {indRRA} não forem informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [12].
                    :ivar vlrPrevOficial: Valor relativo à previdência oficial sobre rendimentos do trabalho,
                        mensal e férias. Validação: Deve ser agrupado conforme segue: a) Quando o evento de
                        origem for S-1200, S-1202, S-2299, S-2399 e respectivo S-1210: {}(./CRMen) = [056107]:
                        se codCateg = [101, 102, 103, 105, 106, 107, 108, 111, 301, 302, 303, 304, 305, 306,
                        307, 308, 309, 310, 311, 312, 313, 314, 401, 410, 501, 721, 722, 723, 761, 901, 902,
                        903, 904, 906], {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [41]; {}(./CRMen) = [056108]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [41];
                        {}(./CRMen) = [056111]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [41]; {}(./CRMen) = [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738,
                        741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [41];
                        {}(./CRMen) = [061001]: se codCateg = [712], {indApurIR} = [0] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) = [586], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [41]; {}(./CRMen) =
                        [188901]: se {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for informado,
                        {indApurIR} = [0] e {indRRA} = [S], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [41, 42]. b) Quando o evento de origem for S-1207 e
                        respectivo S-1210: {}(./CRMen) = [353301]: se {indApurIR} = [0] e os campos
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e {indRRA} não forem informados,
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [41]; {}(./CRMen) = [188901]: se {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não
                        for informado, {indApurIR} = [0] e {indRRA} = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [41, 42].
                    :ivar vlrPrevOficial13: Valor relativo à previdência oficial sobre o 13° salário. Validação:
                        Deve ser agrupado conforme segue: a) Quando o evento de origem for S-1200, S-1202,
                        S-2299, S-2399 e respectivo S-1210: {}(./CRMen) = [056107]: se codCateg = [101, 102,
                        103, 105, 106, 107, 108, 111, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
                        312, 313, 314, 401, 410, 501, 721, 722, 723, 761, 901, 902, 903, 904, 906], {indApurIR}
                        = [0], os campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não
                        forem informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em
                        S-1000 for diferente de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [42]; {}(./CRMen) = [056109]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [42], apenas
                        se origem for S-2299; {}(./CRMen) = [056110]: se codCateg = [104], {indApurIR} = [0] e
                        os campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [42], exceto se origem for S-2299; {}(./CRMen) =
                        [056112]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        = [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [42], exceto se origem for S-2299/S-2399; {}(./CRMen) =
                        [056113]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        = [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [42], apenas se origem for S-2299/S-2399; {}(./CRMen) =
                        [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738, 741, 751, 771, 781],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [42]. b)
                        Quando o evento de origem for S-1207 e respectivo S-1210: {}(./CRMen) = [353301]: se
                        {indApurIR} = [0] e os campos {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e
                        {indRRA} não forem informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [42].
                    :ivar vlrCRMen: Valor relativo ao imposto sobre a renda retido na fonte sobre rendimentos do
                        trabalho, mensal e férias. Validação: Deve ser agrupado conforme segue: a) Quando o
                        evento de origem for S-1200, S-1202, S-2299, S-2399 e respectivo S-1210:
                        {CRMen}(./CRMen) = [056107]: se {codCateg}(../codCateg) = [101, 102, 103, 105, 106, 107,
                        108, 111, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401,
                        410, 501, 721, 722, 723, 761, 901, 902, 903, 904, 906], {indApurIR} = [0], os campos
                        {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31]; {CRMen}(./CRMen) = [056108]: se
                        {codCateg}(../codCateg) = [104], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [31];
                        {CRMen}(./CRMen) = [056111]: se {codCateg}(../codCateg) = [101, 102, 103, 105, 106, 107,
                        108, 111], {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [31]; {CRMen}(./CRMen) = [058806]: se {codCateg}(../codCateg) = [201, 202, 701, 711,
                        712, 731, 734, 738, 741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [31];
                        {CRMen}(./CRMen) = [061001]: se {codCateg}(../codCateg) = [712], {indApurIR} = [0] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) = [586], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [31]; {CRMen}(./CRMen) =
                        [356201]: se {codCateg}(../codCateg) = [1XX], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [34];
                        {CRMen}(./CRMen) = [188901]: se {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não
                        for informado, {indApurIR} = [0] e {indRRA} = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32, 34]. b) Quando o
                        evento de origem for S-1207 e respectivo S-1210: {CRMen}(./CRMen) = [353301]: se
                        {indApurIR} = [0] e os campos {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e
                        {indRRA} não forem informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31, 34]; {CRMen}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for informado, {indApurIR} = [0]
                        e {indRRA} = [S], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32, 34].
                    :ivar vlrCR13Men: Valor relativo ao imposto sobre a renda retido na fonte sobre rendimentos
                        do trabalho, 13° salário. Validação: Deve ser agrupado conforme segue: a) Quando o
                        evento de origem for S-1200, S-1202, S-2299, S-2399 e respectivo S-1210: {}(./CRMen) =
                        [056107]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111, 301, 302, 303, 304,
                        305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401, 410, 501, 721, 722, 723, 761,
                        901, 902, 903, 904, 906], {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32]; {}(./CRMen) = [056109]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [32], apenas
                        se origem for S-2299; {}(./CRMen) = [056110]: se codCateg = [104], {indApurIR} = [0] e
                        os campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32], exceto se origem for S-2299; {}(./CRMen) =
                        [056112]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        = [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32], exceto se origem for S-2299/S-2399; {}(./CRMen) =
                        [056113]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        = [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32], apenas se origem for S-2299/S-2399; {}(./CRMen) =
                        [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738, 741, 751, 771, 781],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [32]. b)
                        Quando o evento de origem for S-1207 e respectivo S-1210: {}(./CRMen) = [353301]: se
                        {indApurIR} = [0] e os campos {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e
                        {indRRA} não forem informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [32].
                    :ivar vlrParcIsenta65: Valor relativo à parcela isenta de proventos de aposentadoria,
                        reserva remunerada, reforma e pensão de beneficiário com 65 anos ou mais. Validação:
                        Deve ser agrupado conforme segue: a) Quando o evento de origem for S-1200, S-1202,
                        S-2299, S-2399 e respectivo S-1210: {}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for informado, {indApurIR} = [0]
                        e {indRRA} = [S], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [70, 71]. b) Quando o evento de origem for S-1207 e
                        respectivo S-1210: {}(./CRMen) = [353301]: se {indApurIR} = [0] e os campos
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e {indRRA} não forem informados,
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [70]; {}(./CRMen) = [188901]: se {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não
                        for informado, {indApurIR} = [0] e {indRRA} = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [70, 71].
                    :ivar vlrParcIsenta65Dec: Valor relativo à parcela isenta de proventos de aposentadoria,
                        reserva remunerada, reforma e pensão de beneficiário com 65 anos ou mais sobre o 13º
                        salário. Validação: Deve ser agrupado conforme segue: a) Quando o evento de origem for
                        S-1207 e respectivo S-1210: {}(./CRMen) = [353301]: se {indApurIR} = [0] e os campos
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e {indRRA} não forem informados,
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [71].
                    :ivar vlrDiarias: Valor relativo a diárias. Validação: Deve ser agrupado conforme segue: a)
                        Quando o evento de origem for S-1200, S-1202, S-2299, S-2399 e respectivo S-1210:
                        {}(./CRMen) = [056107]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111, 301, 302,
                        303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401, 410, 501, 721, 722,
                        723, 761, 901, 902, 903, 904, 906], {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [72]; {}(./CRMen) = [056108]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [72];
                        {}(./CRMen) = [056111]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [72]; {}(./CRMen) = [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738,
                        741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [72].
                    :ivar vlrAjudaCusto: Valor relativo a ajuda de custo. Validação: Deve ser agrupado conforme
                        segue: a) Quando o evento de origem for S-1200, S-1202, S-2299, S-2399 e respectivo
                        S-1210: {}(./CRMen) = [056107]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111,
                        301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401, 410, 501,
                        721, 722, 723, 761, 901, 902, 903, 904, 906], {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [73]; {}(./CRMen) = [056108]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [73];
                        {}(./CRMen) = [056111]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [73]; {}(./CRMen) = [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738,
                        741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [73].
                    :ivar vlrIndResContrato: Valor relativo a indenização e rescisão de contrato, inclusive a
                        título de PDV e acidentes de trabalho. Validação: Deve ser agrupado conforme segue: a)
                        Quando o evento de origem for S-1200, S-1202, S-2299, S-2399 e respectivo S-1210:
                        {}(./CRMen) = [056107]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111, 301, 302,
                        303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401, 410, 501, 721, 722,
                        723, 761, 901, 902, 903, 904, 906], {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [74]; {}(./CRMen) = [056108]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [74];
                        {}(./CRMen) = [056111]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [74]; {}(./CRMen) = [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738,
                        741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [74].
                    :ivar vlrAbonoPec: Valor relativo ao abono pecuniário. Validação: Deve ser agrupado conforme
                        segue: a) Quando o evento de origem for S-1200, S-1202, S-2299, S-2399 e respectivo
                        S-1210: {}(./CRMen) = [056107]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111,
                        301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401, 410, 501,
                        721, 722, 723, 761, 901, 902, 903, 904, 906], {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [75]; {}(./CRMen) = [056108]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [75];
                        {}(./CRMen) = [056111]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [75]; {}(./CRMen) = [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738,
                        741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [75].
                    :ivar vlrRendMoleGrave: Valor relativo ao rendimento de beneficiário com moléstia grave ou
                        acidente em serviço - remuneração mensal. Validação: Deve ser agrupado conforme segue:
                        a) Quando o evento de origem for S-1200, S-1202, S-2299, S-2399 e respectivo S-1210:
                        {}(./CRMen) = [188901]: se {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for
                        informado, {indApurIR} = [0] e {indRRA} = [S], efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [76, 77]. b) Quando o
                        evento de origem for S-1207 e respectivo S-1210: {}(./CRMen) = [353301]: se {indApurIR}
                        = [0] e os campos {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e {indRRA} não
                        forem informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [76]; {}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for informado, {indApurIR} = [0]
                        e {indRRA} = [S], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [76, 77].
                    :ivar vlrRendMoleGrave13: Valor relativo ao rendimento de beneficiário com moléstia grave ou
                        acidente em serviço - 13º salário. Validação: Deve ser agrupado conforme segue: a)
                        Quando o evento de origem for S-1207 e respectivo S-1210: {}(./CRMen) = [353301]: se
                        {indApurIR} = [0] e os campos {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e
                        {indRRA} não forem informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [77].
                    :ivar vlrAuxMoradia: Valor relativo ao auxílio moradia. Validação: Deve ser agrupado
                        conforme segue: a) Quando o evento de origem for S-1200, S-1202, S-2299, S-2399 e
                        respectivo S-1210: {}(./CRMen) = [056107]: se codCateg = [101, 102, 103, 105, 106, 107,
                        108, 111, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401,
                        410, 501, 721, 722, 723, 761, 901, 902, 903, 904, 906], {indApurIR} = [0], os campos
                        {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [700]; {}(./CRMen) = [056108]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [700];
                        {}(./CRMen) = [056111]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [700]; {}(./CRMen) = [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738,
                        741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [700].
                    :ivar vlrBolsaMedico: Valor relativo a bolsa médico residente. Validação: Deve ser agrupado
                        conforme segue: a) Quando o evento de origem for S-1200, S-1202, S-2299, S-2399 e
                        respectivo S-1210: {}(./CRMen) = [056107]: se codCateg = [902], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        for diferente de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [702].
                    :ivar vlrBolsaMedico13: Valor relativo a bolsa médico residente - 13º salário. Validação:
                        Deve ser agrupado conforme segue: a) Quando o evento de origem for S-1200, S-1202,
                        S-2299, S-2399 e respectivo S-1210: {}(./CRMen) = [056107]: se codCateg = [902],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 for diferente
                        de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [703].
                    :ivar vlrJurosMora: Valor relativo aos juros de mora recebidos, devidos pelo atraso no
                        pagamento de remuneração por exercício de emprego, cargo ou função. Validação: Deve ser
                        agrupado conforme segue: a) Quando o evento de origem for S-1200, S-1202, S-2299, S-2399
                        e respectivo S-1210: {}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for informado, {indApurIR} = [0]
                        e {indRRA} = [S], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [704]. b) Quando o evento de origem for S-1207 e
                        respectivo S-1210: {}(./CRMen) = [188901]: se
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não for informado, {indApurIR} = [0]
                        e {indRRA} = [S], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [704].
                    :ivar vlrIsenOutros: Valor relativo aos rendimentos isentos - outros. Validação: Deve ser
                        agrupado conforme segue: a) Quando o evento de origem for S-1200, S-1202, S-2299, S-2399
                        e respectivo S-1210: {}(./CRMen) = [056107]: se codCateg = [101, 102, 103, 105, 106,
                        107, 108, 111, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314,
                        401, 410, 501, 721, 722, 723, 761, 901, 902, 903, 904, 906], {indApurIR} = [0], os
                        campos {indRRA} e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem
                        informados e {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000
                        for diferente de [22], efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [79]; {}(./CRMen) = [056108]: se codCateg = [104],
                        {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [79];
                        {}(./CRMen) = [056111]: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111],
                        {indApurIR} = [0], os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados e
                        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22],
                        efetuar o somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) =
                        [79]; {}(./CRMen) = [058806]: se codCateg = [201, 202, 701, 711, 712, 731, 734, 738,
                        741, 751, 771, 781], {indApurIR} = [0] e os campos {indRRA} e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) não forem informados, efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [79]. b)
                        Quando o evento de origem for S-1207 e respectivo S-1210: {}(./CRMen) = [353301]: se
                        {indApurIR} = [0] e os campos {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) e
                        {indRRA} não forem informados, efetuar o somatório de {valor}(../infoIR_valor) cujo
                        {tpInfoIR}(../infoIR_tpInfoIR) = [79].
                    :ivar descRendimento:
                    """

                    CRMen: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrRendTrib: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrRendTrib13: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrPrevOficial: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrPrevOficial13: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrCRMen: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrCR13Men: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrParcIsenta65: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrParcIsenta65Dec: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrDiarias: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrAjudaCusto: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrIndResContrato: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrAbonoPec: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrRendMoleGrave: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrRendMoleGrave13: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrAuxMoradia: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrBolsaMedico: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrBolsaMedico13: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrJurosMora: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrIsenOutros: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    descRendimento: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 255,
                        },
                    )

                @dataclass(kw_only=True)
                class TotApurDia(CommonMixin):
                    """
                    :ivar perApurDia: Período de apuração diário do Código de Receita - CR. Validação: Deve ser
                        igual ao dia ("DD") da data informada em {dtPgto}(../dtPgto).
                    :ivar CRDia:
                    :ivar frmTribut:
                    :ivar paisResidExt: Código do país de residência para fins fiscais, quando no exterior,
                        conforme Tabela 06.
                    :ivar vlrPagoDia: Valor pago a residente ou domiciliado no exterior. Evento de origem:
                        S-1200, S-1202, S-1207, S-2299, S-2399 e respectivo S-1210. Validação: Efetuar o
                        somatório de {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [11, 12, 14,
                        72, 73, 74, 75, 76, 77, 79, 700, 701, 702, 703, 704], se {indApurIR} = [0] e: a)
                        {codCateg}(../codCateg) for diferente de [712] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) for informado com qualquer valor; ou
                        b) {codCateg}(../codCateg) = [712] e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        for informado com valor diferente de [586].
                    :ivar vlrCRDia: Valor relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do
                        trabalho pagos a residente, para fins fiscais, no exterior. Evento de origem: S-1200,
                        S-1202, S-1207, S-2299, S-2399 e respectivo S-1210. Validação: Deve ser maior ou igual a
                        0 (zero). Caso o valor seja negativo, retornar 0 (zero). Efetuar o somatório de
                        {valor}(../infoIR_valor) cujo {tpInfoIR}(../infoIR_tpInfoIR) = [31, 32, 34], se
                        {indApurIR} = [0] e: a) {codCateg}(../codCateg) for diferente de [712] e
                        {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt) for informado com qualquer valor; ou
                        b) {codCateg}(../codCateg) = [712] e {paisResidExt}(1210_ideBenef_infoPgto_paisResidExt)
                        for informado com valor diferente de [586].
                    """

                    perApurDia: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    CRDia: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    frmTribut: str = field(
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{2}",
                        }
                    )
                    paisResidExt: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrPagoDia: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrCRDia: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class InfoRra(CommonMixin):
                    """
                    :ivar tpProcRRA:
                    :ivar nrProcRRA: Informar o número do processo/requerimento administrativo/judicial.
                    :ivar descRRA:
                    :ivar qtdMesesRRA:
                    :ivar despProcJud:
                    :ivar ideAdv: Identificação dos advogados. CHAVE_GRUPO: {tpInsc}, {nrInsc} CONDICAO_GRUPO:
                        OC
                    """

                    tpProcRRA: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    nrProcRRA: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    descRRA: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    qtdMesesRRA: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    despProcJud: None | ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.InfoRra.DespProcJud = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    ideAdv: list[ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.InfoRra.IdeAdv] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class DespProcJud(CommonMixin):
                        """
                        Despesas com processo judicial DESCRICAO_COMPLETA:Detalhamento das despesas com processo
                        judicial.

                        CONDICAO_GRUPO: OC.

                        :ivar vlrDespCustas: Preencher com o valor das despesas com custas judiciais.
                        :ivar vlrDespAdvogados: Preencher com o valor total das despesas com advogado(s).
                        """

                        vlrDespCustas: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrDespAdvogados: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class IdeAdv(CommonMixin):
                        """
                        :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme
                            Tabela 05.
                        :ivar nrInsc: Informar o número de inscrição do advogado.
                        :ivar vlrAdv: Valor da despesa com o advogado, se houver.
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
                        vlrAdv: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                @dataclass(kw_only=True)
                class InfoPgtoExt(CommonMixin):
                    """
                    :ivar paisResidExt: Código do país de residência para fins fiscais, quando no exterior,
                        conforme Tabela 06.
                    :ivar indNIF:
                    :ivar nifBenef: Número de Identificação Fiscal (NIF).
                    :ivar frmTribut:
                    :ivar endExt: Endereço do beneficiário residente ou domiciliado no exterior. CONDICAO_GRUPO:
                        OC
                    """

                    paisResidExt: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    indNIF: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    nifBenef: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    frmTribut: str = field(
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{2}",
                        }
                    )
                    endExt: None | ESocial.EvtIrrfBenef.IdeTrabalhador.DmDev.InfoPgtoExt.EndExt = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class EndExt(CommonMixin):
                        """
                        :ivar endDscLograd:
                        :ivar endNrLograd: Número do logradouro.
                        :ivar endComplem:
                        :ivar endBairro:
                        :ivar endCidade:
                        :ivar endEstado:
                        :ivar endCodPostal:
                        :ivar telef:
                        """

                        endDscLograd: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 80,
                                "pattern": r"[^\s]{1}[\S\s]*",
                            },
                        )
                        endNrLograd: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        endComplem: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        endBairro: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 60,
                                "pattern": r".*[^\s].*",
                            },
                        )
                        endCidade: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 40,
                                "pattern": r".*[^\s].*",
                            },
                        )
                        endEstado: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 40,
                                "pattern": r".*[^\s].*",
                            },
                        )
                        endCodPostal: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 12,
                                "pattern": r"[A-Za-z0-9]{1,12}",
                            },
                        )
                        telef: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "pattern": r"\d{8,15}",
                            },
                        )

            @dataclass(kw_only=True)
            class TotInfoIr(CommonMixin):
                """
                :ivar consolidApurMen: Totalizador de valores com período de apuração mensal DESCRICAO_COMPLETA:
                    Totalização dos rendimentos tributáveis, deduções e isenções com período de apuração mensal.
                    CHAVE_GRUPO: {CRMen} CONDICAO_GRUPO: OC
                """

                consolidApurMen: list[ESocial.EvtIrrfBenef.IdeTrabalhador.TotInfoIr.ConsolidApurMen] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 50,
                    },
                )

                @dataclass(kw_only=True)
                class ConsolidApurMen(CommonMixin):
                    """
                    :ivar CRMen:
                    :ivar vlrRendTrib: Valor relativo ao rendimento tributável mensal e férias. Validação: Deve
                        ser maior ou igual a 0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrRendTrib}(5002_ideTrabalhador_dmDev_totApurMen_vlrRendTrib).
                    :ivar vlrRendTrib13: Valor relativo ao rendimento do 13º salário. Validação: Deve ser maior
                        ou igual a 0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrRendTrib13}(5002_ideTrabalhador_dmDev_totApurMen_vlrRendTrib13).
                    :ivar vlrPrevOficial: Valor relativo à previdência oficial sobre rendimentos do trabalho,
                        mensal e férias. Validação: Deve ser maior ou igual a 0 (zero). Origem: valores
                        consolidados do campo
                        {totApurMen/vlrPrevOficial}(5002_ideTrabalhador_dmDev_totApurMen_vlrPrevOficial).
                    :ivar vlrPrevOficial13: Valor relativo à previdência oficial sobre o 13° salário. Validação:
                        Deve ser maior ou igual a 0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrPrevOficial13}(5002_ideTrabalhador_dmDev_totApurMen_vlrPrevOficial13).
                    :ivar vlrCRMen: Valor relativo ao imposto sobre a renda retido na fonte sobre rendimentos do
                        trabalho, mensal e férias. Validação: Deve ser maior ou igual a 0 (zero). Origem:
                        valores consolidados do campo
                        {totApurMen/vlrCRMen}(5002_ideTrabalhador_dmDev_totApurMen_vlrCRMen).
                    :ivar vlrCR13Men: Valor relativo ao imposto sobre a renda retido na fonte sobre rendimentos
                        do trabalho, 13° salário. Validação: Deve ser maior ou igual a 0 (zero). Origem: valores
                        consolidados do campo
                        {totApurMen/vlrCR13Men}(5002_ideTrabalhador_dmDev_totApurMen_vlrCR13Men).
                    :ivar vlrParcIsenta65: Valor relativo à parcela isenta de proventos de aposentadoria,
                        reserva remunerada, reforma e pensão de beneficiário com 65 anos ou mais. Validação:
                        Deve ser maior ou igual a 0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrParcIsenta65}(5002_ideTrabalhador_dmDev_totApurMen_vlrParcIsenta65).
                    :ivar vlrParcIsenta65Dec: Valor relativo à parcela isenta de proventos de aposentadoria,
                        reserva remunerada, reforma e pensão de beneficiário com 65 anos ou mais sobre o 13º
                        salário. Validação: Deve ser maior ou igual a 0 (zero). Origem: valores consolidados do
                        campo
                        {totApurMen/vlrParcIsenta65Dec}(5002_ideTrabalhador_dmDev_totApurMen_vlrParcIsenta65Dec).
                    :ivar vlrDiarias: Valor relativo a diárias. Validação: Deve ser maior ou igual a 0 (zero).
                        Origem: valores consolidados do campo
                        {totApurMen/vlrDiarias}(5002_ideTrabalhador_dmDev_totApurMen_vlrDiarias).
                    :ivar vlrAjudaCusto: Valor relativo a ajuda de custo. Validação: Deve ser maior ou igual a 0
                        (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrAjudaCusto}(5002_ideTrabalhador_dmDev_totApurMen_vlrAjudaCusto).
                    :ivar vlrIndResContrato: Valor relativo a indenização e rescisão de contrato, inclusive a
                        título de PDV e acidentes de trabalho. Validação: Deve ser maior ou igual a 0 (zero).
                        Origem: valores consolidados do campo
                        {totApurMen/vlrIndResContrato}(5002_ideTrabalhador_dmDev_totApurMen_vlrIndResContrato).
                    :ivar vlrAbonoPec: Valor relativo ao abono pecuniário. Validação: Deve ser maior ou igual a
                        0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrAbonoPec}(5002_ideTrabalhador_dmDev_totApurMen_vlrAbonoPec).
                    :ivar vlrRendMoleGrave: Valor relativo ao rendimento de beneficiário com moléstia grave ou
                        acidente em serviço - remuneração mensal. Validação: Deve ser maior ou igual a 0 (zero).
                        Origem: valores consolidados do campo
                        {totApurMen/vlrRendMoleGrave}(5002_ideTrabalhador_dmDev_totApurMen_vlrRendMoleGrave).
                    :ivar vlrRendMoleGrave13: Valor relativo ao rendimento de beneficiário com moléstia grave ou
                        acidente em serviço - 13º salário. Validação: Deve ser maior ou igual a 0 (zero).
                        Origem: valores consolidados do campo
                        {totApurMen/vlrRendMoleGrave13}(5002_ideTrabalhador_dmDev_totApurMen_vlrRendMoleGrave13).
                    :ivar vlrAuxMoradia: Valor relativo ao auxílio moradia. Validação: Deve ser maior ou igual a
                        0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrAuxMoradia}(5002_ideTrabalhador_dmDev_totApurMen_vlrAuxMoradia).
                    :ivar vlrBolsaMedico: Valor relativo a bolsa médico residente, mensal. Validação: Deve ser
                        maior ou igual a 0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrBolsaMedico}(5002_ideTrabalhador_dmDev_totApurMen_vlrBolsaMedico).
                    :ivar vlrBolsaMedico13: Valor relativo a bolsa médico residente, 13º salário. Validação:
                        Deve ser maior ou igual a 0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrBolsaMedico13}(5002_ideTrabalhador_dmDev_totApurMen_vlrBolsaMedico13).
                    :ivar vlrJurosMora: Valor relativo aos juros de mora recebidos, devidos pelo atraso no
                        pagamento de remuneração por exercício de emprego, cargo ou função. Validação: Deve ser
                        maior ou igual a 0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrJurosMora}(5002_ideTrabalhador_dmDev_totApurMen_vlrJurosMora).
                    :ivar vlrIsenOutros: Valor relativo aos rendimentos isentos - outros. Validação: Deve ser
                        maior ou igual a 0 (zero). Origem: valores consolidados do campo
                        {totApurMen/vlrIsenOutros}(5002_ideTrabalhador_dmDev_totApurMen_vlrIsenOutros).
                    :ivar descRendimento:
                    """

                    CRMen: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrRendTrib: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrRendTrib13: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrPrevOficial: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrPrevOficial13: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrCRMen: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrCR13Men: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrParcIsenta65: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrParcIsenta65Dec: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrDiarias: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrAjudaCusto: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrIndResContrato: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrAbonoPec: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrRendMoleGrave: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrRendMoleGrave13: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrAuxMoradia: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrBolsaMedico: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrBolsaMedico13: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrJurosMora: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrIsenOutros: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    descRendimento: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 999,
                        },
                    )

            @dataclass(kw_only=True)
            class InfoIrcomplem(CommonMixin):
                """
                :ivar dtLaudo: Data da moléstia grave atribuída pelo laudo. Origem: campo
                    {dtLaudo}(1210_ideBenef_infoIRComplem_dtLaudo) de S-1210.
                :ivar perAnt: Informações complementares de períodos anteriores DESCRICAO_COMPLETA:
                    Identificação do evento S-1210 original e {}(1210_ideBenef_infoPgto_perRef) cujas
                    informações de {}(1210_ideBenef_infoIRComplem) serão alteradas. CONDICAO_GRUPO: OC
                :ivar ideDep: Identificação dos dependentes. CHAVE_GRUPO: {cpfDep} CONDICAO_GRUPO: OC
                :ivar infoIRCR: Informações de Imposto de Renda, por Código de Receita - CR. Evento de origem:
                    S-1210. CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
                :ivar planSaude: Plano de saúde coletivo DESCRICAO_COMPLETA: Plano de saúde coletivo.
                    Identificação da(s) operadora(s) de plano privado coletivo empresarial de assistência à
                    saúde. Evento de origem: S-1210. CHAVE_GRUPO: {cnpjOper}, {regANS} CONDICAO_GRUPO: OC
                :ivar infoReembMed: Reembolsos de despesas médicas DESCRICAO_COMPLETA: Informações relativas a
                    reembolsos efetuados no período de apuração ({perApur}(1210_ideEvento_perApur)) pelo
                    empregador ao trabalhador referente a despesas médicas ou odontológicas pagas pelo
                    trabalhador a prestadores de serviços de saúde. Evento de origem: S-1210. CHAVE_GRUPO:
                    {cnpjOper}, {regANS} CONDICAO_GRUPO: OC
                """

                dtLaudo: None | XmlDate = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                perAnt: None | ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.PerAnt = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                ideDep: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.IdeDep] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 999,
                    },
                )
                infoIRCR: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoIrcr] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                planSaude: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.PlanSaude] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                infoReembMed: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoReembMed] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )

                @dataclass(kw_only=True)
                class PerAnt(CommonMixin):
                    """
                    :ivar perRefAjuste: {}(1210_ideEvento_perApur) do S-1210 cujo
                        {}(1210_ideBenef_infoIRComplem) será alterado. Origem: campo
                        {}(1210_ideBenef_infoIRComplem_perAnt_perRefAjuste) de S-1210.
                    :ivar nrRec1210Orig: Número do recibo do S-1210 original cujas informações de
                        {}(1210_ideBenef_infoIRComplem) serão alteradas. Origem: campo
                        {}(1210_ideBenef_infoIRComplem_perAnt_nrRec1210Orig) de S-1210.
                    """

                    perRefAjuste: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    nrRec1210Orig: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class IdeDep(CommonMixin):
                    """
                    :ivar cpfDep: CPF do dependente. Origem: campo {cpfDep} de
                        S-2200/S-2205/S-2300/S-2400/S-2405 ou
                        {infoDep/cpfDep}(1210_ideBenef_infoIRComplem_infoDep_cpfDep) de S-1210.
                    :ivar depIRRF: Este campo somente é informado em caso de dependente do trabalhador para fins
                        de dedução de seu rendimento tributável pelo Imposto de Renda. Origem: campo {depIRRF}
                        de S-2200/S-2205/S-2300/S-2400/S-2405 ou
                        {depIRRF}(1210_ideBenef_infoIRComplem_infoDep_depIRRF) de S-1210.
                    :ivar dtNascto: Data de nascimento do dependente. Origem: campo {dependente/dtNascto} de
                        S-2200/S-2205/S-2300/S-2400/S-2405 ou
                        {dtNascto}(1210_ideBenef_infoIRComplem_infoDep_dtNascto) de S-1210.
                    :ivar nome: Nome do dependente. Origem: campo {nmDep} de S-2200/S-2205/S-2300/S-2400/S-2405
                        ou {nome}(1210_ideBenef_infoIRComplem_infoDep_nome) de S-1210.
                    :ivar tpDep: Relação de dependência. Origem: campo {tpDep} de
                        S-2200/S-2205/S-2300/S-2400/S-2405 ou {tpDep}(1210_ideBenef_infoIRComplem_infoDep_tpDep)
                        de S-1210.
                    :ivar descrDep: Informar a descrição da dependência. Origem: campo {descrDep} de
                        S-2200/S-2205/S-2300/S-2400/S-2405 ou
                        {descrDep}(1210_ideBenef_infoIRComplem_infoDep_descrDep) de S-1210.
                    """

                    cpfDep: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    depIRRF: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    dtNascto: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    nome: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    tpDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    descrDep: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class InfoIrcr(CommonMixin):
                    """
                    :ivar tpCR:
                    :ivar dedDepen: Dedução do rendimento tributável relativa a dependentes. CHAVE_GRUPO:
                        {tpRend}, {cpfDep} CONDICAO_GRUPO: OC
                    :ivar penAlim: Informação dos beneficiários da pensão alimentícia. CHAVE_GRUPO: {tpRend},
                        {cpfDep} CONDICAO_GRUPO: OC
                    :ivar previdCompl: Informações relativas a planos de previdência complementar. CHAVE_GRUPO:
                        {tpPrev}, {cnpjEntidPC} CONDICAO_GRUPO: OC
                    :ivar infoProcRet: Informações de processos relacionados a não retenção de tributos ou a
                        depósitos judiciais. CHAVE_GRUPO: {tpProcRet}, {nrProcRet}, {codSusp} CONDICAO_GRUPO: OC
                    """

                    tpCR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dedDepen: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoIrcr.DedDepen] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 999,
                        },
                    )
                    penAlim: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoIrcr.PenAlim] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    previdCompl: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoIrcr.PrevidCompl] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    infoProcRet: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoIrcr.InfoProcRet] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 50,
                        },
                    )

                    @dataclass(kw_only=True)
                    class DedDepen(CommonMixin):
                        """
                        :ivar tpRend:
                        :ivar cpfDep: Informar o número de inscrição do dependente no CPF.
                        :ivar vlrDedDep: Preencher com o valor da dedução da base de cálculo.
                        """

                        tpRend: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        cpfDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrDedDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class PenAlim(CommonMixin):
                        """
                        :ivar tpRend:
                        :ivar cpfDep: Número do CPF do dependente/beneficiário da pensão alimentícia.
                        :ivar vlrDedPenAlim: Valor relativo à dedução do rendimento tributável correspondente a
                            pagamento de pensão alimentícia.
                        """

                        tpRend: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        cpfDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrDedPenAlim: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class PrevidCompl(CommonMixin):
                        """
                        :ivar tpPrev:
                        :ivar cnpjEntidPC: Número de inscrição da entidade de previdência complementar.
                        :ivar vlrDedPC: Valor da dedução mensal relativa a previdência complementar.
                        :ivar vlrDedPC13: Valor da dedução do 13º Salário relativa a previdência complementar.
                        :ivar vlrPatrocFunp: Valor da contribuição mensal do ente público patrocinador da
                            Fundação de Previdência Complementar do Servidor Público (Funpresp).
                        :ivar vlrPatrocFunp13: Valor da contribuição do 13º Salário do ente público patrocinador
                            da Fundação de Previdência Complementar do Servidor Público (Funpresp).
                        """

                        tpPrev: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        cnpjEntidPC: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrDedPC: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        vlrDedPC13: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        vlrPatrocFunp: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        vlrPatrocFunp13: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                    @dataclass(kw_only=True)
                    class InfoProcRet(CommonMixin):
                        """
                        :ivar tpProcRet:
                        :ivar nrProcRet: Informar o número do processo administrativo/judicial.
                        :ivar codSusp: Código do indicativo da suspensão, atribuído pelo contribuinte.
                        :ivar infoValores: Informações de valores relacionados a não retenção de tributos ou a
                            depósitos judiciais. CHAVE_GRUPO: {indApuracao} CONDICAO_GRUPO: OC
                        """

                        tpProcRet: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        nrProcRet: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        codSusp: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        infoValores: list[
                            ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoIrcr.InfoProcRet.InfoValores
                        ] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 2,
                            },
                        )

                        @dataclass(kw_only=True)
                        class InfoValores(CommonMixin):
                            """
                            :ivar indApuracao:
                            :ivar vlrNRetido: Valor da retenção que deixou de ser efetuada em função de processo
                                administrativo ou judicial.
                            :ivar vlrDepJud: Valor do depósito judicial em função de processo administrativo ou
                                judicial.
                            :ivar vlrCmpAnoCal: Valor da compensação relativa ao ano calendário em função de
                                processo judicial.
                            :ivar vlrCmpAnoAnt: Valor da compensação relativa a anos anteriores, em função de
                                processo judicial.
                            :ivar vlrRendSusp: Valor do rendimento com exigibilidade suspensa.
                            :ivar dedSusp: Detalhamento das deduções com exigibilidade suspensa. CHAVE_GRUPO:
                                {indTpDeducao}, {cnpjEntidPC} CONDICAO_GRUPO: OC
                            """

                            indApuracao: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vlrNRetido: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vlrDepJud: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vlrCmpAnoCal: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vlrCmpAnoAnt: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vlrRendSusp: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            dedSusp: list[
                                ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoIrcr.InfoProcRet.InfoValores.DedSusp
                            ] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 25,
                                },
                            )

                            @dataclass(kw_only=True)
                            class DedSusp(CommonMixin):
                                """
                                :ivar indTpDeducao:
                                :ivar vlrDedSusp: Valor da dedução da base de cálculo do imposto de renda com
                                    exigibilidade suspensa.
                                :ivar cnpjEntidPC: Número de inscrição da entidade de previdência complementar.
                                :ivar vlrPatrocFunp: Valor da contribuição do ente público patrocinador da
                                    Fundação de Previdência Complementar do Servidor Público (Funpresp).
                                :ivar benefPen: Informação das deduções suspensas por dependentes e
                                    beneficiários da pensão alimentícia. CHAVE_GRUPO: {cpfDep} CONDICAO_GRUPO: O
                                    (se {indTpDeducao}(../indTpDeducao) = [5, 7]); N (nos demais casos)
                                """

                                indTpDeducao: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                vlrDedSusp: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                cnpjEntidPC: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                vlrPatrocFunp: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                benefPen: list[
                                    ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoIrcr.InfoProcRet.InfoValores.DedSusp.BenefPen
                                ] = field(
                                    default_factory=list,
                                    metadata={
                                        "type": "Element",
                                        "max_occurs": 99,
                                    },
                                )

                                @dataclass(kw_only=True)
                                class BenefPen(CommonMixin):
                                    """
                                    :ivar cpfDep: Número de inscrição no CPF.
                                    :ivar vlrDepenSusp: Valor da dedução relativa a dependentes ou a pensão
                                        alimentícia com exigibilidade suspensa.
                                    """

                                    cpfDep: str = field(
                                        metadata={
                                            "type": "Element",
                                        }
                                    )
                                    vlrDepenSusp: str = field(
                                        metadata={
                                            "type": "Element",
                                        }
                                    )

                @dataclass(kw_only=True)
                class PlanSaude(CommonMixin):
                    """
                    :ivar cnpjOper: Informar o número do CNPJ da operadora de plano privado coletivo empresarial
                        de assistência à saúde.
                    :ivar regANS: Registro na Agência Nacional de Saúde - ANS.
                    :ivar vlrSaudeTit: Valor relativo à dedução do rendimento tributável correspondente a
                        pagamento a plano de saúde do titular.
                    :ivar infoDepSau: Informações de dependente de plano de saúde coletivo empresarial.
                        CHAVE_GRUPO: {cpfDep} CONDICAO_GRUPO: OC
                    """

                    cnpjOper: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    regANS: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    vlrSaudeTit: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    infoDepSau: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.PlanSaude.InfoDepSau] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoDepSau(CommonMixin):
                        """
                        :ivar cpfDep: Número de inscrição no CPF do dependente do plano de saúde.
                        :ivar vlrSaudeDep: Valor relativo a dedução do rendimento tributável correspondente a
                            pagamento a plano de saúde do dependente.
                        """

                        cpfDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vlrSaudeDep: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                @dataclass(kw_only=True)
                class InfoReembMed(CommonMixin):
                    """
                    :ivar indOrgReemb:
                    :ivar cnpjOper: CNPJ da operadora do plano de saúde.
                    :ivar regANS: Registro na Agência Nacional de Saúde - ANS.
                    :ivar detReembTit: Informação de reembolso do titular do plano de saúde. CHAVE_GRUPO:
                        {tpInsc}, {nrInsc} CONDICAO_GRUPO: OC
                    :ivar infoReembDep: Informação de reembolso do dependente do plano de saúde. CHAVE_GRUPO:
                        {cpfBenef} CONDICAO_GRUPO: OC
                    """

                    indOrgReemb: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    cnpjOper: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    regANS: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    detReembTit: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    infoReembDep: list[ESocial.EvtIrrfBenef.IdeTrabalhador.InfoIrcomplem.InfoReembMed.InfoReembDep] = (
                        field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 99,
                            },
                        )
                    )

                    @dataclass(kw_only=True)
                    class InfoReembDep(CommonMixin):
                        """
                        :ivar cpfBenef: Número de inscrição no CPF do dependente.
                        :ivar detReembDep: Detalhamento dos reembolsos efetuados aos dependentes
                            DESCRICAO_COMPLETA: Detalhamento dos reembolsos efetuados em
                            {perApur}(1210_ideEvento_perApur) pelo empregador ao trabalhador referente a
                            despesas médicas ou odontológicas pagas pelo trabalhador a prestadores de serviços
                            de saúde relativo a despesas de seus dependentes. CHAVE_GRUPO: {tpInsc}, {nrInsc}
                            CONDICAO_GRUPO: OC
                        """

                        cpfBenef: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        detReembDep: list[str] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 99,
                            },
                        )
