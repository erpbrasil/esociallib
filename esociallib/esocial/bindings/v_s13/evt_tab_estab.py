from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00"


@dataclass(kw_only=True)
class TIdeEstab(CommonMixin):
    """
    Identificação do estabelecimento e validade das informações DESCRICAO_COMPLETA:Identificação do
    estabelecimento, obra de construção civil ou unidade de órgão público e período de validade das informações.

    CHAVE_GRUPO: {tpInsc*}, {nrInsc*}, {iniValid*}, {fimValid*}.

    :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05. Validação: Se
        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [04], deve ser igual a [1].
    :ivar nrInsc: Informar o número de inscrição do estabelecimento (inclusive Sociedade em Conta de
        Participação - SCP), obra de construção civil ou órgão público de acordo com o tipo de inscrição
        indicado no campo {ideEstab/tpInsc}(./tpInsc). Validação: Deve ser compatível com o conteúdo do campo
        {ideEstab/tpInsc}(./tpInsc). Deve ser um identificador válido, constante das bases da RFB, vinculado ao
        empregador.
    :ivar iniValid:
    :ivar fimValid:
    """

    class Meta:
        name = "T_ideEstab"

    tpInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        }
    )
    iniValid: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        }
    )
    fimValid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        },
    )


class InfoCaepfTpCaepf(Enum):
    """
    Tipo de CAEPF.

    Validação: Deve ser compatível com o cadastro da RFB.

    :cvar VALUE_1: Contribuinte individual
    :cvar VALUE_2: Produtor rural
    :cvar VALUE_3: Segurado especial
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


@dataclass(kw_only=True)
class TDadosEstab(CommonMixin):
    """
    Detalhamento das informações do estabelecimento DESCRICAO_COMPLETA:Detalhamento das informações do
    estabelecimento, obra de construção civil ou unidade de órgão público.

    :ivar cnaePrep:
    :ivar cnpjResp: Preencher com o CNPJ responsável pela inscrição no cadastro de obras da RFB. Validação:
        Preenchimento obrigatório e exclusivo por Pessoa Jurídica e se
        {ideEstab/tpInsc}(1005_infoEstab_inclusao_ideEstab_tpInsc) = [4]. Informação obrigatória se
        {iniValid}(1005_infoEstab_inclusao_ideEstab_iniValid) &gt;= [2022-04]. Deve ser um identificador válido,
        constante das bases da RFB, vinculado ao empregador.
    :ivar aliqGilrat: Informações de apuração da alíquota GILRAT do estabelecimento. CONDICAO_GRUPO: OC
    :ivar infoCaepf: Informações relativas ao CAEPF DESCRICAO_COMPLETA:Informações relativas ao Cadastro de
        Atividade Econômica da Pessoa Física - CAEPF. CONDICAO_GRUPO: O (se
        {ideEstab/tpInsc}(1005_infoEstab_inclusao_ideEstab_tpInsc) = [3]); N (nos demais casos)
    :ivar infoObra: Indicativo de substituição da contribuição patronal - Obra de construção civil
        DESCRICAO_COMPLETA:Grupo preenchido obrigatória e exclusivamente por empresa construtora, relacionando
        os estabelecimentos inscritos no Cadastro Nacional de Obras - CNO, para indicar a substituição ou não da
        contribuição patronal incidente sobre a remuneração dos trabalhadores de obra de construção civil.
        CONDICAO_GRUPO: O (se {indConstr}(1000_infoEmpregador_inclusao_infoCadastro_indConstr) em S-1000 = [1] e
        {ideEstab/tpInsc}(1005_infoEstab_inclusao_ideEstab_tpInsc) = [4]); N (nos demais casos)
    :ivar infoTrab: Informações trabalhistas DESCRICAO_COMPLETA:Informações trabalhistas relativas ao
        estabelecimento. CONDICAO_GRUPO: OC
    """

    class Meta:
        name = "T_dadosEstab"

    cnaePrep: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        }
    )
    cnpjResp: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        },
    )
    aliqGilrat: None | TDadosEstab.AliqGilrat = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        },
    )
    infoCaepf: None | TDadosEstab.InfoCaepf = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        },
    )
    infoObra: None | TDadosEstab.InfoObra = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        },
    )
    infoTrab: None | TDadosEstab.InfoTrab = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
        },
    )

    @dataclass(kw_only=True)
    class AliqGilrat(CommonMixin):
        """
        :ivar aliqRat: Informar a alíquota RAT, quando divergente da legislação vigente para a atividade (CNAE)
            preponderante. A divergência só é permitida se existir o grupo com informações sobre o processo
            administrativo/judicial que permite a aplicação de alíquota diferente. Validação: Preenchimento
            obrigatório e exclusivo se a alíquota informada for diferente da definida na legislação vigente para
            o código CNAE informado (neste caso, deverá haver informações de processo em
            {procAdmJudRat}(1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudRat)). Se informada, deve
            ser diferente da alíquota definida na legislação vigente para a atividade (CNAE) preponderante.
        :ivar fap: Fator Acidentário de Prevenção - FAP. Validação: Preenchimento obrigatório e exclusivo por
            Pessoa Jurídica e: a) {ideEstab/tpInsc}(1005_infoEstab_inclusao_ideEstab_tpInsc) = [4] e o campo
            {cnpjResp}(../cnpjResp) não estiver informado; ou b)
            {ideEstab/tpInsc}(1005_infoEstab_inclusao_ideEstab_tpInsc) = [1, 4] e o fator informado for
            diferente do definido pelo órgão governamental competente para o estabelecimento ou para o CNPJ
            responsável pela inscrição no CNO (neste caso, deverá haver informações de processo em
            {procAdmJudFap}(1005_infoEstab_inclusao_dadosEstab_aliqGilrat_procAdmJudFap)); ou c)
            {ideEstab/tpInsc}(1005_infoEstab_inclusao_ideEstab_tpInsc) = [1, 4] e o estabelecimento ou o CNPJ
            responsável pela inscrição no CNO não for encontrado na tabela FAP. Se informado, deve ser um número
            maior ou igual a 0,5000 e menor ou igual a 2,0000 e, no caso da alínea "b", deve ser diferente do
            valor definido pelo órgão governamental competente.
        :ivar procAdmJudRat: Processo administrativo/judicial relativo à alíquota RAT. DESCRICAO_COMPLETA:Grupo
            que identifica, em caso de existência, o processo administrativo ou judicial em que houve
            decisão/sentença favorável ao contribuinte modificando a alíquota RAT da empresa. CONDICAO_GRUPO: OC
        :ivar procAdmJudFap: Processo administrativo/judicial relativo ao FAP. DESCRICAO_COMPLETA:Grupo que
            identifica, em caso de existência, o processo administrativo/judicial em que houve decisão ou
            sentença favorável ao contribuinte suspendendo ou alterando a alíquota FAP aplicável ao
            contribuinte. CONDICAO_GRUPO: OC
        """

        aliqRat: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
            },
        )
        fap: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
            },
        )
        procAdmJudRat: None | TDadosEstab.AliqGilrat.ProcAdmJudRat = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
            },
        )
        procAdmJudFap: None | TDadosEstab.AliqGilrat.ProcAdmJudFap = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
            },
        )

        @dataclass(kw_only=True)
        class ProcAdmJudRat(CommonMixin):
            """
            :ivar tpProc:
            :ivar nrProc: Informar um número de processo cadastrado através do evento S-1070, cujo
                {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) seja igual a [1]. Validação: Deve
                ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos
                (S-1070), com {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) = [1].
            :ivar codSusp:
            """

            tpProc: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                }
            )
            nrProc: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                }
            )
            codSusp: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                }
            )

        @dataclass(kw_only=True)
        class ProcAdmJudFap(CommonMixin):
            """
            :ivar tpProc:
            :ivar nrProc: Informar um número de processo cadastrado através do evento S-1070, cujo
                {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) seja igual a [1]. Validação: Deve
                ser um número de processo administrativo ou judicial válido e existente na Tabela de Processos
                (S-1070), com {indMatProc}(1070_infoProcesso_inclusao_dadosProc_indMatProc) = [1].
            :ivar codSusp:
            """

            tpProc: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                }
            )
            nrProc: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                }
            )
            codSusp: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                }
            )

    @dataclass(kw_only=True)
    class InfoCaepf(CommonMixin):
        tpCaepf: InfoCaepfTpCaepf = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
            }
        )

    @dataclass(kw_only=True)
    class InfoObra(CommonMixin):
        """
        :ivar indSubstPatrObra: Indicativo de substituição da contribuição patronal de obra de construção civil.
        """

        indSubstPatrObra: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
            }
        )

    @dataclass(kw_only=True)
    class InfoTrab(CommonMixin):
        """
        :ivar infoApr: Informações relacionadas à contratação de aprendiz DESCRICAO_COMPLETA:Informações
            relacionadas à contratação de aprendiz. Preenchimento obrigatório somente no caso de dispensa, ainda
            que parcial, de contratação de aprendiz em virtude de processo judicial ou quando houver contratação
            de aprendiz por meio de entidade educativa ou de prática desportiva. CONDICAO_GRUPO: OC
        :ivar infoPCD: Informações sobre a contratação de PCD. DESCRICAO_COMPLETA:Informações sobre a
            contratação de pessoa com deficiência (PCD). Essa informação deve ser prestada apenas no
            estabelecimento matriz. Preenchimento obrigatório somente no caso de dispensa, ainda que parcial, de
            contratação de PCD em virtude de processo judicial. CONDICAO_GRUPO: OC
        """

        infoApr: None | TDadosEstab.InfoTrab.InfoApr = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
            },
        )
        infoPCD: None | TDadosEstab.InfoTrab.InfoPcd = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
            },
        )

        @dataclass(kw_only=True)
        class InfoApr(CommonMixin):
            """
            :ivar nrProcJud: Preencher com o número do processo judicial. Validação: Se informado, deve ser um
                número de processo judicial válido.
            :ivar infoEntEduc: Identificação da(s) entidade(s) educativa(s) ou de prática desportiva.
                CHAVE_GRUPO: {nrInsc} CONDICAO_GRUPO: OC
            """

            nrProcJud: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                },
            )
            infoEntEduc: list[TDadosEstab.InfoTrab.InfoApr.InfoEntEduc] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class InfoEntEduc(CommonMixin):
                """
                :ivar nrInsc: Informar o número de inscrição da entidade educativa ou de prática desportiva.
                    Validação: Deve ser um número de CNPJ válido, com 14 (catorze) algarismos. Se o empregador
                    for pessoa jurídica, a raiz do CNPJ informado deve ser diferente de
                    {ideEmpregador/nrInsc}(1005_ideEmpregador_nrInsc).
                """

                nrInsc: str = field(
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                    }
                )

        @dataclass(kw_only=True)
        class InfoPcd(CommonMixin):
            """
            :ivar nrProcJud: Preencher com o número do processo judicial. Validação: Deve ser um número de
                processo judicial válido.
            """

            nrProcJud: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00",
                }
            )


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos.

    :ivar evtTabEstab: Evento Tabela de Estabelecimentos DESCRICAO_COMPLETA:Evento Tabela de Estabelecimentos,
        Obras ou Unidades de Órgãos Públicos. CHAVE_GRUPO: {Id} REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_TABESTAB_VALIDA_ESTABELECIMENTO
        REGRA:REGRA_TABESTAB_VALIDA_INFO_CNO REGRA:REGRA_TABGERAL_ALTERACAO_PERIODO_CONFLITANTE
        REGRA:REGRA_TABGERAL_EXISTE_REGISTRO_ALTERADO REGRA:REGRA_TABGERAL_EXISTE_REGISTRO_EXCLUIDO
        REGRA:REGRA_TABGERAL_INCLUSAO_PERIODO_CONFLITANTE REGRA:REGRA_TAB_PERMITE_EXCLUSAO
        REGRA:REGRA_VALIDA_DT_FUTURA
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtTabEstab/v_S_01_03_00"

    evtTabEstab: ESocial.EvtTabEstab = field(
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
    class EvtTabEstab(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar infoEstab: Informações do estabelecimento.
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
        infoEstab: ESocial.EvtTabEstab.InfoEstab = field(
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
        class InfoEstab(CommonMixin):
            """
            :ivar inclusao: Inclusão de novas informações. CONDICAO_GRUPO: OC
            :ivar alteracao: Alteração das informações. CONDICAO_GRUPO: OC
            :ivar exclusao: Exclusão das informações. CONDICAO_GRUPO: OC
            """

            inclusao: None | ESocial.EvtTabEstab.InfoEstab.Inclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            alteracao: None | ESocial.EvtTabEstab.InfoEstab.Alteracao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            exclusao: None | ESocial.EvtTabEstab.InfoEstab.Exclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Inclusao(CommonMixin):
                ideEstab: TIdeEstab = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dadosEstab: TDadosEstab = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Alteracao(CommonMixin):
                ideEstab: TIdeEstab = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dadosEstab: TDadosEstab = field(
                    metadata={
                        "type": "Element",
                    }
                )
                novaValidade: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Exclusao(CommonMixin):
                ideEstab: TIdeEstab = field(
                    metadata={
                        "type": "Element",
                    }
                )
