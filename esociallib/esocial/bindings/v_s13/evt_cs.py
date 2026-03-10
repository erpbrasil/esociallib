from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_03_00"


class BasesAquisIndAquis(Enum):
    """
    Indicativo da aquisição.

    Origem: campo {indAquis} de S-1250.

    :cvar VALUE_1: Aquisição da produção de produtor rural pessoa física ou segurado especial em geral
    :cvar VALUE_2: Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por
        entidade do PAA
    :cvar VALUE_3: Aquisição da produção de produtor rural pessoa jurídica por entidade do PAA
    :cvar VALUE_4: Aquisição da produção de produtor rural pessoa física ou segurado especial em geral -
        Produção isenta (Lei 13.606/2018)
    :cvar VALUE_5: Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por
        entidade do PAA - Produção isenta (Lei 13.606/2018)
    :cvar VALUE_6: Aquisição da produção de produtor rural pessoa jurídica por entidade do PAA - Produção isenta
        (Lei 13.606/2018)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class BasesRemunIndIncid(Enum):
    """
    Preencher com o código correspondente ao tipo de incidência para fins de apuração da contribuição
    previdenciária.

    Validação: a) Para empresas com {classTrib}(5011_infoCS_infoContrib_classTrib) = [01, 70, 80], todas as bases
    de cálculo devem ser totalizadas com {indIncid}(./indIncid) = [9], EXCETO para
    {classTrib}(5011_infoCS_infoContrib_classTrib) = [01] E {ideEstab/tpInsc}(5011_infoCS_ideEstab_tpInsc) = [4],
    que deve ser totalizada com {indIncid}(./indIncid) = [1]. b) Para empresas com
    {classTrib}(5011_infoCS_infoContrib_classTrib) = [03], considerar a informação prestada no campo
    {indSimples}(5001_infoCp_ideEstabLot_infoCategIncid_indSimples) do evento S-5001, conforme abaixo: - Se o
    {indSimples}(5001_infoCp_ideEstabLot_infoCategIncid_indSimples) em S-5001 = [1] (contrib. subst.
    integralmente), a base de cálculo do respectivo trabalhador deve ser totalizada com {indIncid}(./indIncid) =
    [9]; - Se o {indSimples}(5001_infoCp_ideEstabLot_infoCategIncid_indSimples) em S-5001 = [2] (contrib. não
    substituída), a base de cálculo do respectivo trabalhador deve ser totalizada com {indIncid}(./indIncid) = [1]
    (normal); - Se o {indSimples}(5001_infoCp_ideEstabLot_infoCategIncid_indSimples) em S-5001 = [3] (ativ.
    concomitante), a base de cálculo do respectivo trabalhador deve ser totalizada com {indIncid}(./indIncid) =
    [2]. c) Para empresas com {classTrib}(5011_infoCS_infoContrib_classTrib) = [10] (sindicato de avulsos não
    portuários), as bases de cálculo dos trabalhadores avulsos da categoria [202] devem ser totalizadas com
    {indIncid}(./indIncid) = [9]. d) Para {classTrib}(5011_infoCS_infoContrib_classTrib) = [22] (segurado
    especial), as bases de cálculo dos trabalhadores devem ser totalizadas com {indIncid}(./indIncid) = [9], EXCETO
    para a categoria [104] (empregado doméstico) ou se {ideEstab/tpInsc}(5011_infoCS_ideEstab_tpInsc) = [4], que
    deve ser totalizada com {indIncid}(./indIncid) = [1]. e) Para contribuinte com
    {classTrib}(5011_infoCS_infoContrib_classTrib) = [99] e com {indCoop}(5011_infoCS_infoContrib_infoPJ_indCoop) =
    [1] (cooperativa de trabalho), as remunerações dos cooperados (categoria [731, 734]) cuja lotação esteja
    classificada com {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) em S-1020 = [05, 06, 07] devem
    ser totalizadas com {indIncid}(./indIncid) = [9]. Nos demais casos, {indIncid}(./indIncid) = [1]. f) Para
    contribuintes com {classTrib}(5011_infoCS_infoContrib_classTrib) = [11], as bases de cálculo dos trabalhadores
    devem ser totalizadas com {indIncid}(./indIncid) = [9], EXCETO para as categorias de contribuinte individual,
    que devem ser totalizadas com {indIncid}(./indIncid) = [1]. g) Para
    {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) em S-1020 = [91, 92], todas as bases de cálculo
    devem ser totalizadas com {indIncid}(./indIncid) = [9].

    :cvar VALUE_1: Normal
    :cvar VALUE_2: Atividade concomitante
    :cvar VALUE_9: Substituída ou isenta
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_9 = 9


class InfoCsIndExistInfo(Enum):
    """
    Indicativo de existência de valores de bases e de contribuições sociais.

    :cvar VALUE_1: Há informações com apuração de contribuições sociais
    :cvar VALUE_2: Há movimento, porém sem apuração de contribuições sociais
    :cvar VALUE_3: Não há movimento no período informado em {perApur}(5011_ideEvento_perApur)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoPjIndTribFolhaPisPasep(Enum):
    """
    Indicador de tributação sobre a folha de pagamento - PIS e PASEP.

    Evento de origem: S-1000.

    :cvar S: Sim
    """

    S = "S"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-5011 - Informações das Contribuições Sociais Consolidadas por Contribuinte.

    :ivar evtCS: Evento Informações das Contribuições Sociais Consolidadas por Contribuinte. CHAVE_GRUPO: {Id}
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtCS/v_S_01_03_00"

    evtCS: ESocial.EvtCs = field(
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
    class EvtCs(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoCS: Informações relativas às contribuições sociais DESCRICAO_COMPLETA:Informações relativas às
            contribuições sociais devidas à Previdência Social e a Outras Entidades e Fundos.
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
        infoCS: ESocial.EvtCs.InfoCs = field(
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
        class InfoCs(CommonMixin):
            """
            :ivar nrRecArqBase:
            :ivar indExistInfo:
            :ivar infoCPSeg: Informações de contribuição previdenciária do segurado. CONDICAO_GRUPO: OC
            :ivar infoContrib: Informações gerais do contribuinte DESCRICAO_COMPLETA:Informações gerais do
                contribuinte necessárias à apuração das contribuições sociais.
            :ivar ideEstab: Identificação do estabelecimento/obra DESCRICAO_COMPLETA:Informações de
                identificação do estabelecimento ou obra de construção civil. CHAVE_GRUPO: {tpInsc}, {nrInsc}
                CONDICAO_GRUPO: OC
            :ivar infoCRContrib: Totalizador dos Códigos de Receita do contribuinte
                DESCRICAO_COMPLETA:Informações consolidadas das contribuições sociais devidas à Previdência
                Social e Outras Entidades e Fundos, por Código de Receita - CR. CHAVE_GRUPO: {tpCR}
                CONDICAO_GRUPO: OC
            """

            nrRecArqBase: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indExistInfo: InfoCsIndExistInfo = field(
                metadata={
                    "type": "Element",
                }
            )
            infoCPSeg: None | ESocial.EvtCs.InfoCs.InfoCpseg = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoContrib: ESocial.EvtCs.InfoCs.InfoContrib = field(
                metadata={
                    "type": "Element",
                }
            )
            ideEstab: list[ESocial.EvtCs.InfoCs.IdeEstab] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            infoCRContrib: list[ESocial.EvtCs.InfoCs.InfoCrcontrib] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class InfoCpseg(CommonMixin):
                """
                :ivar vrDescCP: Valor total da contribuição descontada dos segurados. Origem: campo
                    {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001, quando
                    {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 = [21].
                :ivar vrCpSeg: Valor total calculado relativo à contribuição dos segurados. Origem: campo
                    {vrCpSeg}(5001_infoCpCalc_vrCpSeg) de S-5001.
                """

                vrDescCP: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                vrCpSeg: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class InfoContrib(CommonMixin):
                """
                :ivar classTrib:
                :ivar infoPJ: Informações exclusivas da PJ DESCRICAO_COMPLETA:Informações complementares,
                    exclusivas da Pessoa Jurídica. CONDICAO_GRUPO: O (se
                    {ideEmpregador/tpInsc}(5011_ideEmpregador_tpInsc) = [1]); N (nos demais casos)
                """

                classTrib: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{2}",
                    }
                )
                infoPJ: None | ESocial.EvtCs.InfoCs.InfoContrib.InfoPj = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoPj(CommonMixin):
                    """
                    :ivar indCoop: Indicativo de cooperativa. Evento de origem: S-1000.
                    :ivar indConstr: Indicativo de construtora. Evento de origem: S-1000.
                    :ivar indSubstPatr: Indicativo de substituição da contribuição previdenciária patronal.
                        Origem: campo {indSubstPatr}(1280_infoSubstPatr_indSubstPatr) de S-1280.
                    :ivar percRedContrib: Percentual de redução da contribuição prevista na Lei 12.546/2011.
                        Evento de origem: S-1280.
                    :ivar percTransf: Percentual de contribuição social - Lei 11.096/2005. Evento de origem:
                        S-1280.
                    :ivar indTribFolhaPisPasep:
                    :ivar infoAtConc: Informações de atividades concomitantes DESCRICAO_COMPLETA:Informações
                        prestadas por empresa enquadrada no regime de tributação Simples Nacional com tributação
                        previdenciária substituída e não substituída. CONDICAO_GRUPO: O (se
                        {classTrib}(../../classTrib) = [03]; N (nos demais casos)
                    """

                    indCoop: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    indConstr: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    indSubstPatr: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    percRedContrib: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    percTransf: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    indTribFolhaPisPasep: None | InfoPjIndTribFolhaPisPasep = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoAtConc: None | ESocial.EvtCs.InfoCs.InfoContrib.InfoPj.InfoAtConc = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoAtConc(CommonMixin):
                        """
                        :ivar fatorMes: Informe o fator a ser utilizado para cálculo da contribuição patronal do
                            mês dos trabalhadores envolvidos na execução das atividades enquadradas no Anexo IV
                            em conjunto com as dos Anexos I a III e V da Lei Complementar 123/2006. Evento de
                            origem: S-1280.
                        :ivar fator13: Informe o fator a ser utilizado para cálculo da contribuição patronal do
                            décimo terceiro dos trabalhadores envolvidos na execução das atividades enquadradas
                            no Anexo IV em conjunto com as dos Anexos I a III e V da Lei Complementar 123/2006.
                            Evento de origem: S-1280.
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
            class IdeEstab(CommonMixin):
                """
                :ivar tpInsc:
                :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideEstab/tpInsc}(./tpInsc). Evento de origem: S-1260, S-1270 ou S-5001.
                :ivar infoEstab: Informações do estabelecimento DESCRICAO_COMPLETA:Informações relativas a cada
                    estabelecimento, necessárias à apuração das contribuições sociais. CONDICAO_GRUPO: N (se
                    {ideEstab/tpInsc}(../tpInsc) = [2] OU (se {ideEstab/tpInsc}(../tpInsc) = [3] e se tratar de
                    empregador doméstico) OU se não existir informação em S-1200, S-1270, S-2299 ou S-2399
                    relativas ao estabelecimento); O (nos demais casos)
                :ivar ideLotacao: Identificação da lotação tributária. CHAVE_GRUPO: {codLotacao} CONDICAO_GRUPO:
                    O (se existir informação em S-1200, S-1270, S-2299 ou S-2399 relativas ao estabelecimento
                    identificado em {ideEstab/nrInsc}(../nrInsc)); N (nos demais casos)
                :ivar basesAquis: Informações sobre aquisição rural DESCRICAO_COMPLETA:Informações de bases de
                    cálculo relativas à aquisição de produção rural. Evento de origem: S-1250 (existente até a
                    versão 2.5 do leiaute). CHAVE_GRUPO: {indAquis} CONDICAO_GRUPO: O (se existir informação em
                    S-1250 relativa ao estabelecimento identificado em {ideEstab/nrInsc}(../nrInsc) e se não
                    houver informação de {indExcApur1250}(1299_infoFech_indExcApur1250) em S-1299); N (nos
                    demais casos)
                :ivar basesComerc: Informações da comercialização da produção DESCRICAO_COMPLETA:Informações de
                    bases de cálculo relativas à comercialização da produção rural da Pessoa Física. Informações
                    desse grupo conforme informado pelo contribuinte em S-1260. CHAVE_GRUPO: {indComerc}
                    CONDICAO_GRUPO: O (se houver evento S-1260 válido na competência relativo ao estabelecimento
                    identificado em {ideEstab/nrInsc}(../nrInsc)); N (nos demais casos)
                :ivar infoCREstab: Códigos de Receita por estabelecimento DESCRICAO_COMPLETA:Informações das
                    contribuições sociais devidas à Previdência Social e Outras Entidades e Fundos, consolidadas
                    por estabelecimento e por Código de Receita - CR. CHAVE_GRUPO: {tpCR} CONDICAO_GRUPO: OC
                :ivar basesPisPasep: Bases da contribuição do PIS/PASEP DESCRICAO_COMPLETA:Valores
                    correspondentes às bases da contribuição do PIS/PASEP. CONDICAO_GRUPO: O (se
                    {}(5011_infoCS_infoContrib_infoPJ_indTribFolhaPisPasep) = [S], {}(5011_ideEvento_perApur)
                    &gt;= [2025-01] e {ideEmpregador/tpInsc}(5011_ideEmpregador_tpInsc)= [1]; N (nos demais
                    casos) O cálculo do CR 8301-02 e do CR 8301-22 dependem da versão e do período de apuração
                    do fechamento. Se a versão for S-1.3 e {}(1299_ideEvento_perApur) &gt;= [2025-01], então o
                    CR será calculado sobre {}(5011_infoCS_ideEstab_basesPisPasep); em caso contrário, o CR será
                    calculado com as bases da previdência.
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
                infoEstab: None | ESocial.EvtCs.InfoCs.IdeEstab.InfoEstab = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                ideLotacao: list[ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                    },
                )
                basesAquis: list[ESocial.EvtCs.InfoCs.IdeEstab.BasesAquis] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 6,
                    },
                )
                basesComerc: list[ESocial.EvtCs.InfoCs.IdeEstab.BasesComerc] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 5,
                    },
                )
                infoCREstab: list[ESocial.EvtCs.InfoCs.IdeEstab.InfoCrestab] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                basesPisPasep: None | ESocial.EvtCs.InfoCs.IdeEstab.BasesPisPasep = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoEstab(CommonMixin):
                    """
                    :ivar cnaePrep: Preencher com o código CNAE, conforme informado em S-1005. Evento de origem:
                        S-1005.
                    :ivar cnpjResp: Preencher com o CNPJ responsável pela inscrição no cadastro de obras da RFB.
                        Evento de origem: S-1005.
                    :ivar aliqRat: Informar a alíquota RAT. Validação: Deve corresponder à alíquota declarada no
                        evento S-1005. Caso não haja informação, retornar a alíquota definida na legislação
                        vigente para o código CNAE informado.
                    :ivar fap: Fator Acidentário de Prevenção - FAP. Validação: Informação obrigatória e
                        exclusiva se {ideEmpregador/tpInsc}(5011_ideEmpregador_tpInsc) = [1]. Deve corresponder
                        ao FAP estabelecido para a empresa pelo órgão governamental competente, exceto se: a)
                        {ideEstab/tpInsc}(5011_infoCS_ideEstab_tpInsc) = [4] e se não existir o campo
                        {cnpjResp}(./cnpjResp); ou b) {ideEstab/tpInsc}(5011_infoCS_ideEstab_tpInsc) = [1, 4] e
                        se houver informação de
                        {procAdmJudFap}(1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudFap) em S-1005;
                        ou c) {ideEstab/tpInsc}(5011_infoCS_ideEstab_tpInsc) = [1, 4] e o estabelecimento ou o
                        CNPJ responsável pela inscrição no CNO não for encontrado na tabela FAP referente ao ano
                        de {perApur}(5011_ideEvento_perApur). Caso haja alguma exceção acima, retornar o FAP
                        declarado no evento S-1005.
                    :ivar aliqRatAjust:
                    :ivar infoEstabRef: Informações de RAT e FAP de referência DESCRICAO_COMPLETA: Informações
                        de RAT e FAP de referência, nos casos de processo administrativo ou judicial que altere
                        a(s) alíquota(s). CONDICAO_GRUPO: OC (se houver informação de
                        {procAdmJudRat}(1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudRat) em S-1005
                        ou de {procAdmJudFap}(1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudFap) em
                        S-1005); N (nos demais casos)
                    :ivar infoComplObra: Informações complementares relativas a obras
                        DESCRICAO_COMPLETA:Informações complementares relativas a obras de construção civil.
                        CONDICAO_GRUPO: O (se houver informação de
                        {infoObra}(1005_infoEstab_inclusao_dadosEstab_infoObra) em S-1005); N (nos demais casos)
                    """

                    cnaePrep: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    cnpjResp: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    aliqRat: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    fap: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    aliqRatAjust: None | Decimal = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_inclusive": Decimal("0.5"),
                            "max_inclusive": Decimal("6"),
                            "total_digits": 5,
                            "fraction_digits": 4,
                        },
                    )
                    infoEstabRef: None | ESocial.EvtCs.InfoCs.IdeEstab.InfoEstab.InfoEstabRef = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoComplObra: None | ESocial.EvtCs.InfoCs.IdeEstab.InfoEstab.InfoComplObra = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoEstabRef(CommonMixin):
                        """
                        :ivar aliqRat: Retornar a alíquota RAT definida na legislação vigente. Validação: Deve
                            corresponder à alíquota definida na legislação vigente para o código CNAE informado
                            em S-1005.
                        :ivar fap: Fator Acidentário de Prevenção - FAP estabelecido pelo órgão governamental
                            competente. Validação: Informação obrigatória e exclusiva se
                            {ideEmpregador/tpInsc}(5011_ideEmpregador_tpInsc) = [1]. Deve corresponder ao FAP
                            estabelecido para a empresa pelo órgão governamental competente.
                        :ivar aliqRatAjust:
                        """

                        aliqRat: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        fap: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        aliqRatAjust: None | Decimal = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_inclusive": Decimal("0.5"),
                                "max_inclusive": Decimal("6"),
                                "total_digits": 5,
                                "fraction_digits": 4,
                            },
                        )

                    @dataclass(kw_only=True)
                    class InfoComplObra(CommonMixin):
                        """
                        :ivar indSubstPatrObra: Indicativo de substituição da contribuição patronal de obra de
                            construção civil. Origem: campo
                            {indSubstPatrObra}(1005_infoEstab_inclusao_dadosEstab_infoObra_indSubstPatrObra) de
                            S-1005.
                        """

                        indSubstPatrObra: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                @dataclass(kw_only=True)
                class IdeLotacao(CommonMixin):
                    """
                    :ivar codLotacao: Informar o código atribuído pelo empregador para a lotação tributária.
                        Evento de origem: S-1270 ou S-5001.
                    :ivar fpas: Preencher com o código relativo ao FPAS. Evento de origem: S-1020.
                    :ivar codTercs: Preencher com o código de Terceiros, conforme Tabela 04. Evento de origem:
                        S-1020.
                    :ivar codTercsSusp: Informar o código combinado dos Terceiros para os quais o recolhimento
                        está suspenso em virtude de processos judiciais. Evento de origem: S-1020.
                    :ivar infoTercSusp: Informações de suspensão de contribuição a Terceiros
                        DESCRICAO_COMPLETA:Informações de suspensão de contribuições destinadas a Outras
                        Entidades e Fundos (Terceiros). CHAVE_GRUPO: {codTerc} CONDICAO_GRUPO: OC
                    :ivar infoEmprParcial: Informação complementar de obra de construção civil
                        DESCRICAO_COMPLETA:Informação complementar que apresenta identificação do contratante e
                        do proprietário de obra de construção civil contratada sob regime de empreitada parcial
                        ou subempreitada. Evento de origem: S-1020. CONDICAO_GRUPO: O (se
                        {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) em S-1020 relativo a
                        {codLotacao}(../codLotacao) for igual a [02]); N (nos demais casos)
                    :ivar dadosOpPort: Informações relativas ao operador portuário. CONDICAO_GRUPO: O (se
                        {tpLotacao}(1020_infoLotacao_inclusao_dadosLotacao_tpLotacao) em S-1020 relativo a
                        {codLotacao}(../codLotacao) for igual a [08]); N (nos demais casos)
                    :ivar basesRemun: Bases de cálculo por categoria DESCRICAO_COMPLETA:Bases de cálculo da
                        contribuição previdenciária incidente sobre remunerações, por categoria. CHAVE_GRUPO:
                        {indIncid}, {codCateg} CONDICAO_GRUPO: O (se houver evento S-1200/S-2299/S-2399 com
                        informações de remuneração válido na competência relativo ao estabelecimento
                        identificado em {ideEstab/nrInsc}(../../nrInsc)); N (nos demais casos)
                    :ivar basesAvNPort: Contratação de avulsos não portuários DESCRICAO_COMPLETA:Informações de
                        bases de cálculo relativas à contratação de trabalhadores avulsos não portuários.
                        Informações desse grupo conforme informado pelo contribuinte em S-1270. CONDICAO_GRUPO:
                        O (se houver evento S-1270 válido na competência relativo ao estabelecimento
                        identificado em {ideEstab/nrInsc}(../../nrInsc)); N (nos demais casos)
                    :ivar infoSubstPatrOpPort: Informação de substituição prevista na Lei 12.546/2011
                        DESCRICAO_COMPLETA:Grupo preenchido exclusivamente pelo Órgão Gestor de Mão de Obra -
                        OGMO ({classTrib}(5011_infoCS_infoContrib_classTrib) = [09]), relativamente a operador
                        portuário enquadrado nos arts. 7º a 9º da Lei 12.546/2011. CONDICAO_GRUPO: OC (se
                        {classTrib}(5011_infoCS_infoContrib_classTrib) = [09]; N (nos demais casos)
                    """

                    codLotacao: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    fpas: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    codTercs: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    codTercsSusp: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoTercSusp: list[ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.InfoTercSusp] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 15,
                        },
                    )
                    infoEmprParcial: None | ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.InfoEmprParcial = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    dadosOpPort: None | ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.DadosOpPort = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    basesRemun: list[ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.BasesRemun] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    basesAvNPort: None | ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.BasesAvNport = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoSubstPatrOpPort: None | ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.InfoSubstPatrOpPort = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class InfoTercSusp(CommonMixin):
                        """
                        :ivar codTerc: Informar o código de Terceiro. Origem: campo
                            {codTerc}(1020_infoLotacao_inclusao_dadosLotacao_fpasLotacao_infoProcJudTerceiros_procJudTerceiro_codTerc)
                            de S-1020.
                        """

                        codTerc: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class InfoEmprParcial(CommonMixin):
                        """
                        :ivar tpInscContrat: Tipo de inscrição do contratante.
                        :ivar nrInscContrat: Número de inscrição (CNPJ/CPF) do contratante.
                        :ivar tpInscProp: Tipo de inscrição do proprietário do CNO. Validação: Retornar o tipo
                            de inscrição do proprietário no CNO. Caso não tenha sido encontrado, retornar
                            {tpInscProp}(1020_infoLotacao_inclusao_dadosLotacao_infoEmprParcial_tpInscProp) de
                            S-1020. Se o tipo de inscrição do proprietário no CNO não for encontrado e se não
                            houver informação de
                            {tpInscProp}(1020_infoLotacao_inclusao_dadosLotacao_infoEmprParcial_tpInscProp) em
                            S-1020, retornar
                            {tpInscContrat}(5011_infoCS_ideEstab_ideLotacao_infoEmprParcial_tpInscContrat).
                        :ivar nrInscProp: Preencher com o número de inscrição (CNPJ/CPF) do proprietário do CNO.
                            Validação: Retornar o número de inscrição do proprietário no CNO. Caso não tenha
                            sido encontrado, retornar
                            {nrInscProp}(1020_infoLotacao_inclusao_dadosLotacao_infoEmprParcial_nrInscProp) de
                            S-1020. Se o número de inscrição do proprietário no CNO não for encontrado e se não
                            houver informação de
                            {nrInscProp}(1020_infoLotacao_inclusao_dadosLotacao_infoEmprParcial_nrInscProp) em
                            S-1020, retornar
                            {nrInscContrat}(5011_infoCS_ideEstab_ideLotacao_infoEmprParcial_nrInscContrat).
                        :ivar cnoObra:
                        """

                        tpInscContrat: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        nrInscContrat: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        tpInscProp: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        nrInscProp: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        cnoObra: str = field(
                            metadata={
                                "type": "Element",
                                "pattern": r"\d{12}",
                            }
                        )

                    @dataclass(kw_only=True)
                    class DadosOpPort(CommonMixin):
                        """
                        :ivar cnpjOpPortuario: Preencher com o CNPJ do operador portuário. Origem: campo
                            {dadosLotacao/nrInsc}(1020_infoLotacao_inclusao_dadosLotacao_nrInsc) de S-1020.
                        :ivar aliqRat: Informar a alíquota RAT. Origem: campo
                            {dadosOpPort/aliqRat}(1020_infoLotacao_inclusao_dadosLotacao_dadosOpPort_aliqRat) de
                            S-1020.
                        :ivar fap: Fator Acidentário de Prevenção - FAP. Origem: campo
                            {dadosOpPort/fap}(1020_infoLotacao_inclusao_dadosLotacao_dadosOpPort_fap) de S-1020.
                        :ivar aliqRatAjust:
                        """

                        cnpjOpPortuario: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        aliqRat: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        fap: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        aliqRatAjust: Decimal = field(
                            metadata={
                                "type": "Element",
                                "min_inclusive": Decimal("0.5"),
                                "max_inclusive": Decimal("6"),
                                "total_digits": 5,
                                "fraction_digits": 4,
                            }
                        )

                    @dataclass(kw_only=True)
                    class BasesRemun(CommonMixin):
                        """
                        :ivar indIncid:
                        :ivar codCateg: Preencher com o código da categoria do trabalhador, conforme definido em
                            S-5001.
                        :ivar basesCp: Bases, contribuições do segurado e deduções da CP
                            DESCRICAO_COMPLETA:Valores correspondentes às bases, contribuições do segurado e
                            deduções da contribuição previdenciária.
                        :ivar basesCp13: Valores correspondentes às remunerações a título de 13º salário
                            incluídas em folha mensal - Empresas desoneradas. CONDICAO_GRUPO: OC (se
                            {indDesFolha}(1000_infoEmpregador_inclusao_infoCadastro_indDesFolha) em S-1000 =
                            [1], exceto para CNO com
                            {indSubstPatrObra}(5011_infoCS_ideEstab_infoEstab_infoComplObra_indSubstPatrObra) =
                            [2]); N (nos demais casos)
                        """

                        indIncid: BasesRemunIndIncid = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        codCateg: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        basesCp: ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.BasesRemun.BasesCp = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        basesCp13: None | ESocial.EvtCs.InfoCs.IdeEstab.IdeLotacao.BasesRemun.BasesCp13 = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                        @dataclass(kw_only=True)
                        class BasesCp(CommonMixin):
                            """
                            :ivar vrBcCp00: Preencher com a base de cálculo da contribuição previdenciária sobre
                                a remuneração. Origem: para {codCateg}(../codCateg) diferente de [104]:
                                somatório do campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [11, 15]; para {codCateg}(../codCateg) = [104]: somatório do campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [11, 15], limitado ao teto do salário de contribuição. OBS.: A
                                contribuição previdenciária patronal do empregador doméstico tem como base de
                                cálculo o somatório do salário de contribuição de cada empregado.
                            :ivar vrBcCp15: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 15 anos de
                                contribuição. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001, se
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [12, 16].
                            :ivar vrBcCp20: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 20 anos de
                                contribuição. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [13, 17].
                            :ivar vrBcCp25: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 25 anos de
                                contribuição. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [14, 18].
                            :ivar vrSuspBcCp00: Valor da BC com incidência suspensa em decorrência de decisão
                                judicial. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [91, 95].
                            :ivar vrSuspBcCp15: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                direito a aposentadoria especial aos 15 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [92, 96].
                            :ivar vrSuspBcCp20: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                expectativa de aposentadoria especial aos 20 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [93, 97].
                            :ivar vrSuspBcCp25: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                direito a aposentadoria especial aos 25 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [94, 98].
                            :ivar vrBcCp00VA: Preencher com a base de cálculo da contribuição previdenciária
                                sobre a remuneração - Contrato Verde e Amarelo. Origem: somatório do campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [41, 45].
                            :ivar vrBcCp15VA: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 15 anos de
                                contribuição - Contrato Verde e Amarelo. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001, se
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [42, 46].
                            :ivar vrBcCp20VA: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 20 anos de
                                contribuição - Contrato Verde e Amarelo. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [43, 47].
                            :ivar vrBcCp25VA: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 25 anos de
                                contribuição - Contrato Verde e Amarelo. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [44, 48].
                            :ivar vrSuspBcCp00VA: Valor da BC com incidência suspensa em decorrência de decisão
                                judicial - Contrato Verde e Amarelo. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [81, 85].
                            :ivar vrSuspBcCp15VA: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                direito a aposentadoria especial aos 15 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial - Contrato Verde e Amarelo. Origem:
                                campo {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de
                                S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [82, 86].
                            :ivar vrSuspBcCp20VA: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                expectativa de aposentadoria especial aos 20 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial - Contrato Verde e Amarelo. Origem:
                                campo {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de
                                S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [83, 87].
                            :ivar vrSuspBcCp25VA: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                direito a aposentadoria especial aos 25 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial - Contrato Verde e Amarelo. Origem:
                                campo {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de
                                S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [84, 88].
                            :ivar vrDescSest: Valor total descontado do trabalhador para recolhimento ao SEST.
                                Origem: campo {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [22].
                            :ivar vrCalcSest: Valor calculado relativo à contribuição devida pelo trabalhador
                                para recolhimento ao SEST. Origem: campo
                                {vrCsSegTerc}(5001_infoCp_ideEstabLot_infoCategIncid_calcTerc_vrCsSegTerc) de
                                S-5001, quando
                                {calcTerc/tpCR}(5001_infoCp_ideEstabLot_infoCategIncid_calcTerc_tpCR) em S-5001
                                = [121802], exceto se houver informação de processo judicial do trabalhador,
                                quando deve ser utilizado o valor apurado em {vrDescSest}(./vrDescSest).
                            :ivar vrDescSenat: Valor total descontado do trabalhador para recolhimento ao SENAT.
                                Origem: campo {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [23].
                            :ivar vrCalcSenat: Valor calculado relativo à contribuição devida pelo trabalhador
                                para recolhimento ao SENAT. Origem: campo
                                {vrCsSegTerc}(5001_infoCp_ideEstabLot_infoCategIncid_calcTerc_vrCsSegTerc) de
                                S-5001, quando
                                {calcTerc/tpCR}(5001_infoCp_ideEstabLot_infoCategIncid_calcTerc_tpCR) em S-5001
                                = [122102], exceto se houver informação de processo judicial do trabalhador,
                                quando deve ser utilizado o valor apurado em {vrDescSenat}(./vrDescSenat).
                            :ivar vrSalFam: Valor total do salário-família para a categoria indicada. Origem:
                                campo {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de
                                S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [31].
                            :ivar vrSalMat: Valor total do salário-maternidade para a categoria indicada.
                                Origem: campo {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor)
                                de S-5001, quando
                                {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em S-5001 =
                                [32].
                            """

                            vrBcCp00: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrBcCp15: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrBcCp20: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrBcCp25: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSuspBcCp00: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSuspBcCp15: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSuspBcCp20: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSuspBcCp25: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrBcCp00VA: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrBcCp15VA: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrBcCp20VA: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrBcCp25VA: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrSuspBcCp00VA: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrSuspBcCp15VA: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrSuspBcCp20VA: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrSuspBcCp25VA: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrDescSest: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrCalcSest: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrDescSenat: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrCalcSenat: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSalFam: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSalMat: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

                        @dataclass(kw_only=True)
                        class BasesCp13(CommonMixin):
                            """
                            :ivar vrBcCp00: Preencher com a base de cálculo da contribuição previdenciária -
                                Remuneração a título de 13º salário. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [51].
                            :ivar vrBcCp15: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 15 anos de
                                contribuição - Remuneração a título de 13º salário. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [52].
                            :ivar vrBcCp20: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 20 anos de
                                contribuição - Remuneração a título de 13º salário. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [53].
                            :ivar vrBcCp25: Preencher com a base de cálculo da contribuição adicional para o
                                financiamento dos benefícios de aposentadoria especial após 25 anos de
                                contribuição - Remuneração a título de 13º salário. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [54].
                            :ivar vrSuspBcCp00: Valor da base de cálculo com incidência suspensa em decorrência
                                de decisão judicial - Remuneração a título de 13º salário. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [71].
                            :ivar vrSuspBcCp15: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                direito a aposentadoria especial aos 15 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial - Remuneração a título de 13º
                                salário. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [72].
                            :ivar vrSuspBcCp20: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                expectativa de aposentadoria especial aos 20 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial - Remuneração a título de 13º
                                salário. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [73].
                            :ivar vrSuspBcCp25: Valor da base de cálculo da contribuição previdenciária
                                adicional correspondente a exposição a agente nocivo que dá ao trabalhador
                                direito a aposentadoria especial aos 25 anos de trabalho, com incidência
                                suspensa em decorrência de decisão judicial - Remuneração a título de 13º
                                salário. Origem: campo
                                {valor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_valor) de S-5001,
                                quando {tpValor}(5001_infoCp_ideEstabLot_infoCategIncid_infoBaseCS_tpValor) em
                                S-5001 = [74].
                            """

                            vrBcCp00: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrBcCp15: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrBcCp20: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrBcCp25: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSuspBcCp00: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSuspBcCp15: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSuspBcCp20: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            vrSuspBcCp25: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

                    @dataclass(kw_only=True)
                    class BasesAvNport(CommonMixin):
                        """
                        :ivar vrBcCp00: Valor da base de cálculo da contribuição previdenciária sobre a
                            remuneração dos trabalhadores avulsos não portuários. Origem: campo
                            {vrBcCp00}(1270_remunAvNP_vrBcCp00) de S-1270.
                        :ivar vrBcCp15: Valor da base de cálculo da contribuição adicional para o financiamento
                            dos benefícios de aposentadoria especial após 15 anos de contribuição. Origem: campo
                            {vrBcCp15}(1270_remunAvNP_vrBcCp15) de S-1270.
                        :ivar vrBcCp20: Valor da base de cálculo da contribuição adicional para o financiamento
                            dos benefícios de aposentadoria especial após 20 anos de contribuição. Origem: campo
                            {vrBcCp20}(1270_remunAvNP_vrBcCp20) de S-1270.
                        :ivar vrBcCp25: Valor da base de cálculo da contribuição adicional para o financiamento
                            dos benefícios de aposentadoria especial após 25 anos de contribuição. Origem: campo
                            {vrBcCp25}(1270_remunAvNP_vrBcCp25) de S-1270.
                        :ivar vrBcCp13: Valor da base de cálculo da contribuição previdenciária sobre o 13°
                            salário dos trabalhadores avulsos não portuários contratados. Origem: campo
                            {vrBcCp13}(1270_remunAvNP_vrBcCp13) de S-1270.
                        :ivar vrDescCP: Preencher com o valor total da contribuição descontada dos trabalhadores
                            avulsos não portuários. Origem: campo {vrDescCP}(1270_remunAvNP_vrDescCP) de S-1270.
                        """

                        vrBcCp00: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrBcCp15: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrBcCp20: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrBcCp25: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrBcCp13: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrDescCP: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class InfoSubstPatrOpPort(CommonMixin):
                        """
                        :ivar cnpjOpPortuario: Preencher com o CNPJ do operador portuário. Origem: campo
                            {dadosLotacao/nrInsc}(1020_infoLotacao_inclusao_dadosLotacao_nrInsc) de S-1020
                            relativo a {codLotacao}(1280_infoSubstPatrOpPort_codLotacao) em S-1280.
                        """

                        cnpjOpPortuario: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                @dataclass(kw_only=True)
                class BasesAquis(CommonMixin):
                    """
                    :ivar indAquis:
                    :ivar vlrAquis: Valor total da aquisição de produção rural de produtor rural. Origem: campo
                        {vlrTotAquis} de S-1250.
                    :ivar vrCPDescPR: Preencher com o valor da contribuição previdenciária descontada pelo
                        adquirente de produção de produtor rural - sub-rogação. Origem: somatório do campo
                        {vrCpDescPR} de S-1250.
                    :ivar vrCPNRet: Valor da contribuição previdenciária que deixou de ser retida pelo
                        declarante em decorrência de decisão/sentença judicial.
                    :ivar vrRatNRet: Valor da GILRAT, incidente sobre a aquisição de produção rural de produtor
                        rural, cuja retenção deixou de ser efetuada em decorrência de decisão/sentença judicial.
                    :ivar vrSenarNRet: Valor da contribuição destinada ao SENAR, incidente sobre a aquisição de
                        produção rural de produtor rural pessoa física/segurado especial, que deixou de ser
                        retida em decorrência de decisão/sentença judicial.
                    :ivar vrCPCalcPR: Valor calculado relativo à contribuição previdenciária do produtor rural,
                        de acordo com {indAquis}(./indAquis), conforme segue: a) {indAquis}(./indAquis) = [1,
                        2]: {vlrAquis}(./vlrAquis) x 1,2%; b) {indAquis}(./indAquis) = [3]:
                        {vlrAquis}(./vlrAquis) x 1,7%; c) {indAquis}(./indAquis) = [4, 5, 6]: 0 (zero).
                    :ivar vrRatDescPR: Valor da contribuição destinada ao financiamento dos benefícios
                        concedidos em razão do grau de incidência da incapacidade laborativa decorrente dos
                        riscos ambientais do trabalho, incidente sobre a aquisição de produção rural de produtor
                        rural.
                    :ivar vrRatCalcPR: Valor calculado relativo à contribuição GILRAT devida pelo produtor
                        rural, de acordo com {indAquis}(./indAquis), conforme segue: a) {indAquis}(./indAquis) =
                        [1, 2, 3]: {vlrAquis}(./vlrAquis) x 0,1%; b) {indAquis}(./indAquis) = [4, 5, 6]: 0
                        (zero).
                    :ivar vrSenarDesc: Valor da contribuição destinada ao SENAR, incidente sobre a aquisição de
                        produção rural de produtor rural pessoa física/segurado especial. Origem: campo
                        {vrSenarDesc} de S-1250.
                    :ivar vrSenarCalc: Valor calculado da contribuição devida pelo produtor rural ao SENAR,
                        conforme segue: a) {indAquis}(./indAquis) = [1, 2, 4, 5]: {vlrAquis}(./vlrAquis) x 0,2%;
                        b) {indAquis}(./indAquis) = [3, 6]: 0 (zero). OBS.: No período de 04/2020 a 06/2020, a
                        alíquota deve ser 0,1%.
                    """

                    indAquis: BasesAquisIndAquis = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vlrAquis: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrCPDescPR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrCPNRet: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrRatNRet: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrSenarNRet: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrCPCalcPR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrRatDescPR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrRatCalcPR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrSenarDesc: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrSenarCalc: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class BasesComerc(CommonMixin):
                    """
                    :ivar indComerc: Indicativo de comercialização. Origem: campo
                        {indComerc}(1260_infoComProd_ideEstabel_tpComerc_indComerc) de S-1260.
                    :ivar vrBcComPR: Valor da base de cálculo da comercialização da produção rural do produtor
                        rural PF/segurado especial a outra PF no varejo ou a outro produtor rural PF/segurado
                        especial ou no mercado externo, conforme {indComerc}(./indComerc). Origem: campo
                        {vrTotCom}(1260_infoComProd_ideEstabel_tpComerc_vrTotCom) de S-1260.
                    :ivar vrCPSusp: Valor da contribuição previdenciária com exigibilidade suspensa. Origem:
                        campo {vrCPSusp}(1260_infoComProd_ideEstabel_tpComerc_infoProcJud_vrCPSusp) de S-1260.
                    :ivar vrRatSusp: Valor da contribuição para GILRAT com exigibilidade suspensa. Origem: campo
                        {vrRatSusp}(1260_infoComProd_ideEstabel_tpComerc_infoProcJud_vrRatSusp) de S-1260.
                    :ivar vrSenarSusp: Valor da contribuição para o SENAR com exigibilidade suspensa. Origem:
                        campo {vrSenarSusp}(1260_infoComProd_ideEstabel_tpComerc_infoProcJud_vrSenarSusp) de
                        S-1260.
                    """

                    indComerc: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrBcComPR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrCPSusp: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    vrRatSusp: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    vrSenarSusp: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class InfoCrestab(CommonMixin):
                    """
                    :ivar tpCR:
                    :ivar vrCR: Valor correspondente ao CR apurado. Validação: Deve ser apurado de acordo com a
                        legislação em vigor na competência. Deve ser maior que 0 (zero).
                    :ivar vrSuspCR: Valor suspenso correspondente ao CR apurado. Validação: Deve ser apurado de
                        acordo com as informações de processos judiciais e administrativos.
                    """

                    tpCR: str = field(
                        metadata={
                            "type": "Element",
                            "pattern": r"\d{6}",
                        }
                    )
                    vrCR: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrSuspCR: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class BasesPisPasep(CommonMixin):
                    """
                    :ivar vrBcPisPasep: Preencher com a base da contribuição do PIS/PASEP. Origem: somatório do
                        campo {}(5001_infoPisPasep_ideEstab_infoCategPisPasep_infoBasePisPasep_valorPisPasep) de
                        S-5001, quando
                        {}(5001_infoPisPasep_ideEstab_infoCategPisPasep_infoBasePisPasep_tpValorPisPasep) em
                        S-5001 = [11].
                    :ivar vrBcPisPasepSusp: Preencher com a base da contribuição do PIS/PASEP suspensa. Origem:
                        somatório do campo
                        {}(5001_infoPisPasep_ideEstab_infoCategPisPasep_infoBasePisPasep_valorPisPasep) de
                        S-5001, quando
                        {}(5001_infoPisPasep_ideEstab_infoCategPisPasep_infoBasePisPasep_tpValorPisPasep) em
                        S-5001 = [91].
                    """

                    vrBcPisPasep: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    vrBcPisPasepSusp: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )

            @dataclass(kw_only=True)
            class InfoCrcontrib(CommonMixin):
                """
                :ivar tpCR:
                :ivar vrCR: Valor correspondente ao CR apurado. Validação: Deve ser apurado de acordo com a
                    legislação em vigor na competência. Deve ser maior que 0 (zero).
                :ivar vrCRSusp: Valor do tributo com exigibilidade suspensa.
                """

                tpCR: str = field(
                    metadata={
                        "type": "Element",
                        "pattern": r"\d{6}",
                    }
                )
                vrCR: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                vrCRSusp: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
