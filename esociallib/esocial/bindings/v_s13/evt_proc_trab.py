from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_03_00"


class InfoCcpTpCcp(Enum):
    """
    Indicar o âmbito de celebração do acordo.

    :cvar VALUE_1: CCP no âmbito de empresa
    :cvar VALUE_2: CCP no âmbito de sindicato
    :cvar VALUE_3: NINTER
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoContrTpContr(Enum):
    """
    Tipo de contrato a que se refere o processo judicial ou a demanda submetida à CCP ou ao NINTER.

    Validação: Deve ser igual a [6, 8] se o grupo {ideResp}(2500_ideEmpregador_ideResp) for informado.

    :cvar VALUE_1: Trabalhador com vínculo formalizado no eSocial, sem alteração nas datas de admissão e de
        desligamento
    :cvar VALUE_2: Trabalhador com vínculo formalizado no eSocial, com alteração na data de admissão
    :cvar VALUE_3: Trabalhador com vínculo formalizado no eSocial, com inclusão ou alteração de data de
        desligamento
    :cvar VALUE_4: Trabalhador com vínculo formalizado no eSocial, com alteração na data de admissão e inclusão
        ou alteração de data de desligamento
    :cvar VALUE_5: Empregado com reconhecimento de vínculo
    :cvar VALUE_6: Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo
        empregatício
    :cvar VALUE_7: Trabalhador com vínculo de emprego formalizado em período anterior ao eSocial
    :cvar VALUE_8: Responsabilidade indireta
    :cvar VALUE_9: Trabalhador cujos contratos foram unificados (unicidade contratual)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class InfoTermMtvDesligTsv(Enum):
    """
    Motivo do término do diretor não empregado, com FGTS.

    Validação: Informação obrigatória e exclusiva se {infoContr/codCateg}(2500_ideTrab_infoContr_codCateg) = [721].

    :cvar VALUE_01: Exoneração do diretor não empregado sem justa causa, por deliberação da assembleia, dos
        sócios cotistas ou da autoridade competente
    :cvar VALUE_02: Término de mandato do diretor não empregado que não tenha sido reconduzido ao cargo
    :cvar VALUE_03: Exoneração a pedido de diretor não empregado
    :cvar VALUE_04: Exoneração do diretor não empregado por culpa recíproca ou força maior
    :cvar VALUE_05: Morte do diretor não empregado
    :cvar VALUE_06: Exoneração do diretor não empregado por falência, encerramento ou supressão de parte da
        empresa
    :cvar VALUE_99: Outros
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_99 = "99"


class InfoVlrIndReperc(Enum):
    """
    Indicativo de repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER.

    :cvar VALUE_1: Decisão com repercussão tributária e/ou FGTS com rendimentos informados em S-2501
    :cvar VALUE_2: Decisão sem repercussão tributária ou FGTS
    :cvar VALUE_3: Decisão com repercussão exclusiva para declaração de rendimentos para fins de Imposto de
        Renda com rendimentos informados em S-2501
    :cvar VALUE_4: Decisão com repercussão exclusiva para declaração de rendimentos para fins de Imposto de
        Renda com pagamento através de depósito judicial
    :cvar VALUE_5: Decisão com repercussão tributária e/ou FGTS com pagamento através de depósito judicial
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class SucessaoVincTpInsc(Enum):
    """
    Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.

    Validação: Somente é possível informar [5] se {dtTransf}(./dtTransf) for igual ou anterior a [1999-06-30].

    :cvar VALUE_1: CNPJ
    :cvar VALUE_2: CPF
    :cvar VALUE_5: CGC
    :cvar VALUE_6: CEI
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_5 = 5
    VALUE_6 = 6


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2500 - Processo Trabalhista.

    :ivar evtProcTrab: Evento Processo Trabalhista. CHAVE_GRUPO: {Id} REGRA:REGRA_BLOQUEIA_USO_CPF_EMPREGADOR
        REGRA:REGRA_COMPATIBILIDADE_CATEGORIA_CLASSTRIB REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EXISTE_INFO_EMPREGADOR REGRA:REGRA_INFO_IDESEQTRAB
        REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_MUDANCA_CATEG_NAT_ATIV REGRA:REGRA_RETIFICA_IDENTIFICADOR
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_UNICIDADE_CONTRATUAL REGRA:REGRA_VALIDA_EMPREGADOR
        REGRA:REGRA_VALIDA_MATRICULA REGRA:REGRA_VALIDA_PROC_TRAB REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtProcTrab/v_S_01_03_00"

    evtProcTrab: ESocial.EvtProcTrab = field(
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
    class EvtProcTrab(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador: Informações de identificação do empregador ou do contribuinte que está prestando a
            informação. CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar infoProcesso: Informações do processo judicial ou de demanda submetida à CCP ou ao NINTER.
            CHAVE_GRUPO: {nrProcTrab*} DESCRICAO_COMPLETA: Informações do processo judicial ou de demanda
            submetida à Comissão de Conciliação Prévia (CCP) ou ao Núcleo Intersindical de Conciliação
            Trabalhista (NINTER).
        :ivar ideTrab: Informações do trabalhador. CHAVE_GRUPO: {cpfTrab*}, {ideSeqTrab*}
        :ivar Id:
        """

        ideEvento: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: ESocial.EvtProcTrab.IdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        infoProcesso: ESocial.EvtProcTrab.InfoProcesso = field(
            metadata={
                "type": "Element",
            }
        )
        ideTrab: ESocial.EvtProcTrab.IdeTrab = field(
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
        class IdeEmpregador(CommonMixin):
            """
            :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição do empregador ou
                contribuinte que está prestando a informação, conforme Tabela 05.
            :ivar nrInsc: Informar o número de inscrição do empregador ou contribuinte que está prestando a
                informação, de acordo com o tipo de inscrição indicado no campo {ideEmpregador/tpInsc}(./tpInsc)
                e conforme informado em S-1000.
            :ivar ideResp: Identificação do contribuinte, caso tenha havido imposição de responsabilidade
                indireta. DESCRICAO_COMPLETA: Informações de identificação do contribuinte (responsável direto),
                caso tenha havido imposição de responsabilidade indireta. CONDICAO_GRUPO: O (se houver algum
                {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr) = [8]); OC (se não houver nenhum
                {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr) = [8] e houver algum
                {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr) = [6]); N (nos demais casos)
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
            ideResp: None | ESocial.EvtProcTrab.IdeEmpregador.IdeResp = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class IdeResp(CommonMixin):
                """
                :ivar tpInsc:
                :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição
                    indicado no campo {ideResp/tpInsc}(./tpInsc). Validação: Deve ser um identificador válido e:
                    a) Se {ideResp/tpInsc}(./tpInsc) = [1], deve ser informado com 14 (catorze) algarismos. Se o
                    empregador for pessoa jurídica, a raiz do CNPJ informado deve ser diferente de
                    {ideEmpregador/nrInsc}(../nrInsc), exceto se {ideEmpregador/nrInsc}(../nrInsc) tiver 14
                    (catorze) algarismos. b) Se {ideResp/tpInsc}(./tpInsc) = [2], deve ser diferente do CPF do
                    trabalhador. Se o empregador for pessoa física, também deve ser diferente do CPF do
                    empregador.
                :ivar dtAdmRespDir: Preencher com a data de admissão do trabalhador no empregador de origem
                    (responsável direto) quando se tratar de vínculo que não foi informado no eSocial. Em caso
                    de TSVE sem informação de matrícula no evento S-2300, informar a data de início. Validação:
                    Se informado, deve ser posterior à data de nascimento do trabalhador e igual ou anterior ao
                    ano do óbito, se existente. Não deve ser informado se houver informação no campo
                    {}(./matRespDir).
                :ivar matRespDir: Informar a matrícula no empregador de origem (responsável direto). Validação:
                    Se informado, deve corresponder a uma matrícula informada pelo empregador de origem
                    (responsável direto) no evento S-2190, S-2200 ou S-2300, pertencente ao trabalhador
                    preenchido em {}(../../ideTrab_cpfTrab), no empregador informado em
                    {ideResp/nrInsc}(./nrInsc).
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
                dtAdmRespDir: None | XmlDate = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                matRespDir: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

        @dataclass(kw_only=True)
        class InfoProcesso(CommonMixin):
            """
            :ivar origem:
            :ivar nrProcTrab: Número do processo trabalhista, da ata ou número de identificação da conciliação.
                Validação: Se {origem}(./origem) = [1], deve ser um processo judicial válido, com 20 (vinte)
                algarismos. Se {origem}(./origem) = [2], deve possuir 15 (quinze) algarismos.
            :ivar obsProcTrab: Observações relacionadas ao processo judicial ou à demanda submetida à CCP ou ao
                NINTER.
            :ivar dadosCompl: Informações complementares do processo ou da demanda.
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
            obsProcTrab: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            dadosCompl: ESocial.EvtProcTrab.InfoProcesso.DadosCompl = field(
                metadata={
                    "type": "Element",
                }
            )

            @dataclass(kw_only=True)
            class DadosCompl(CommonMixin):
                """
                :ivar infoProcJud: Informações complementares do processo judicial. CONDICAO_GRUPO: O (se
                    {origem}(2500_infoProcesso_origem) = [1]); N (nos demais casos)
                :ivar infoCCP: Informações complementares da demanda submetida à CCP ou ao NINTER.
                    CONDICAO_GRUPO: O (se {origem}(2500_infoProcesso_origem) = [2]); N (nos demais casos)
                """

                infoProcJud: None | ESocial.EvtProcTrab.InfoProcesso.DadosCompl.InfoProcJud = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoCCP: None | ESocial.EvtProcTrab.InfoProcesso.DadosCompl.InfoCcp = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoProcJud(CommonMixin):
                    """
                    :ivar dtSent: Informar a data da: a) Determinação judicial para o cumprimento da decisão
                        líquida transitada em julgado; b) Homologação de acordo judicial; ou c) Decisão que
                        determinar o cumprimento antecipado de obrigação. Validação: Deve ser igual ou anterior
                        à data atual.
                    :ivar ufVara: Preencher com a sigla da Unidade da Federação onde está localizada a Vara em
                        que o processo tramitou.
                    :ivar codMunic:
                    :ivar idVara:
                    """

                    dtSent: XmlDate = field(
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
                class InfoCcp(CommonMixin):
                    """
                    :ivar dtCCP: Data da celebração do acordo celebrado perante CCP ou NINTER. Validação: Deve
                        ser igual ou anterior à data atual.
                    :ivar tpCCP:
                    :ivar cnpjCCP: Identificar o CNPJ do sindicato representativo do trabalhador, no âmbito da
                        CCP ou NINTER. Validação: O preenchimento é obrigatório e exclusivo se {tpCCP}(./tpCCP)
                        for igual a [2] ou [3]. Deve ser um número de CNPJ válido.
                    """

                    dtCCP: XmlDate = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    tpCCP: InfoCcpTpCcp = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    cnpjCCP: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

        @dataclass(kw_only=True)
        class IdeTrab(CommonMixin):
            """
            :ivar cpfTrab:
            :ivar nmTrab: Informar o nome do trabalhador. Validação: Preenchimento obrigatório se não existir
                contrato com {indContr}(2500_ideTrab_infoContr_indContr) = [S].
            :ivar dtNascto: Preencher com a data de nascimento. Validação: Preenchimento obrigatório se não
                existir contrato com {indContr}(2500_ideTrab_infoContr_indContr) = [S]. Deve ser maior ou igual
                que 01/01/1890 e menor ou igual à data atual.
            :ivar ideSeqTrab: Número sequencial atribuído pela empresa a cada conjunto de dados de processo
                trabalhista, quando for necessário enviar o mesmo processo em múltiplos S-2500, para o mesmo
                {}(./cpfTrab). Validação: Deve ser um identificador único dentre os eventos S-2500 do empregador
                que tenham os mesmos {}(../infoProcesso_nrProcTrab) e {}(./cpfTrab). Se for preenchido, não pode
                haver outro evento S-2500 com os mesmos {}(../infoProcesso_nrProcTrab) e {}(./cpfTrab), e sem o
                campo {}(./ideSeqTrab). Se não for preenchido, não pode haver outro evento S-2500 com os mesmos
                {}(../infoProcesso_nrProcTrab) e {}(./cpfTrab). O valor [0] é reservado para uso interno. O
                campo não pode ser informado se todos os contratos do evento tiverem
                {}(2500_ideTrab_infoContr_indContr) = [S].
            :ivar infoContr: Informações do contrato de trabalho. CHAVE_GRUPO: {matricula}, {codCateg},
                {dtInicio}
            """

            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nmTrab: None | str = field(
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
            ideSeqTrab: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "pattern": r"\d{1,3}",
                },
            )
            infoContr: list[ESocial.EvtProcTrab.IdeTrab.InfoContr] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class InfoContr(CommonMixin):
                """
                :ivar tpContr:
                :ivar indContr: Indicativo se o contrato possui informação no evento S-2190, S-2200 ou S-2300 no
                    declarante. Validação: Deve ser igual a [N] se o grupo {ideResp}(2500_ideEmpregador_ideResp)
                    for informado. Deve ser igual a [S] se {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr) =
                    [1, 2, 3, 4]. Além disso, somente pode haver um contrato com o valor igual a [N].
                :ivar dtAdmOrig: Preencher com a data de admissão original do vínculo (data de admissão antes da
                    alteração). Validação: Preenchimento obrigatório se {infoContr/tpContr}(./tpContr) = [2, 4].
                    Se {infoContr/tpContr}(./tpContr) = [2, 4], deve ser diferente de
                    {}(2200_vinculo_infoRegimeTrab_infoCeletista_dtAdm)/{}(2200_vinculo_infoRegimeTrab_infoEstatutario_dtExercicio)
                    em S-2200. Deve ser posterior à data de nascimento do trabalhador.
                :ivar indReint: Indicativo de reintegração do empregado. Validação: Preenchimento obrigatório e
                    exclusivo se {infoContr/tpContr}(./tpContr) for diferente de [6] e {indContr}(./indContr) =
                    [S]. Caso seja informado [S], deve existir evento de reintegração (S-2298) para a matrícula
                    abaixo informada, com o número de processo nesse evento igual a
                    {nrProcTrab}(2500_infoProcesso_nrProcTrab).
                :ivar indCateg: Indicativo se houve reconhecimento de categoria do trabalhador diferente da
                    informada (no eSocial ou na GFIP) pelo declarante.
                :ivar indNatAtiv: Indicativo se houve reconhecimento de natureza da atividade diferente da
                    cadastrada pelo declarante.
                :ivar indMotDeslig: Indicativo se houve reconhecimento de motivo de desligamento diferente do
                    informado pelo declarante.
                :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor
                    público, a matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Se
                    {indContr}(./indContr) = [N], deve ser criada uma matrícula para o trabalhador. Se
                    {indContr}(./indContr) = [S], deve corresponder à matrícula informada pelo empregador no
                    evento S-2190, S-2200, S-2300 ou S-8200 do respectivo contrato. O campo não deve ser
                    informado somente no caso de TSVE cadastrado em versão do leiaute anterior a S-1.0. Se
                    {infoContr/tpContr}(./tpContr) = [9], deve ser preenchida a matrícula que incorporará as
                    demais (informadas no grupo {unicContr}(2500_ideTrab_infoContr_unicContr)). Validação: Se
                    {indContr}(./indContr) = [N], deve ser aplicada a regra de validação abaixo. Além disso, o
                    valor informado neste campo não pode conter a expressão 'eSocial' nas 7 (sete) primeiras
                    posições. Se {indContr}(./indContr) = [S], deve corresponder a uma matrícula existente no
                    Registro de Eventos Trabalhistas - RET para o respectivo trabalhador.
                    REGRA:REGRA_CARACTERE_ESPECIAL
                :ivar codCateg: Preencher com o código da categoria do trabalhador. Validação: Informação
                    obrigatória e exclusiva se {indContr}(./indContr) = [N] ou se o campo
                    {matricula}(./matricula) não estiver preenchido. Deve ser um código válido e existente na
                    Tabela 01 e obedecer ao que segue: a) Se o campo {matricula}(./matricula) não estiver
                    preenchido, deve ser igual ao código de categoria informado no evento S-2300; b) Se
                    {indContr}(./indContr) = [N] e {infoContr/tpContr}(./tpContr) for diferente de [6], deve ser
                    um código de categoria compatível com o evento S-2200 (conforme regra de validação abaixo);
                    c) Se {indContr}(./indContr) = [N] e {infoContr/tpContr}(./tpContr) = [6], deve ser um
                    código de categoria compatível com o evento S-2300 (conforme regra de validação abaixo).
                    REGRA:REGRA_COMPATIB_CATEG_EVENTO
                :ivar dtInicio: Data de início de TSVE, que pode ser: a) Para o cooperado, a data de ingresso na
                    cooperativa; b) Para o diretor não empregado, a data de posse no cargo; c) Para o dirigente
                    sindical, a data de início do mandato no sindicato; d) Para o estagiário, a data de início
                    do estágio; e) Para o trabalhador avulso, a data de ingresso no Órgão Gestor de Mão de Obra
                    - OGMO ou no sindicato; f) Para o servidor público exercente de cargo eletivo, a data de
                    início do mandato; g) Para os demais trabalhadores, a data de início das atividades.
                    Validação: Informação obrigatória e exclusiva se ({infoContr/tpContr}(./tpContr) = [6] e
                    {indContr}(./indContr) = [N]) ou se o campo {matricula}(./matricula) não estiver preenchido.
                    Deve ser posterior à data de nascimento do trabalhador. Se o campo {matricula}(./matricula)
                    não estiver preenchido, deve ser igual à data de início informada no evento S-2300.
                :ivar infoCompl: Informações complementares do contrato de trabalho. CONDICAO_GRUPO: O (se
                    {indContr}(../indContr) = [N]); N (nos demais casos)
                :ivar mudCategAtiv: Informação do novo código de categoria e/ou da nova natureza da atividade.
                    DESCRICAO_COMPLETA:Informação do novo código de categoria e/ou da nova natureza da
                    atividade, no caso de reconhecimento judicial nesse sentido. CHAVE_GRUPO: {dtMudCategAtiv}
                    CONDICAO_GRUPO: O (se {indCateg}(../indCateg) = [S] ou se {indNatAtiv}(../indNatAtiv) =
                    [S]); N (nos demais casos)
                :ivar unicContr: Informações dos vínculos/contratos incorporados. DESCRICAO_COMPLETA:Informações
                    dos vínculos/contratos incorporados, no caso de reconhecimento de unicidade contratual.
                    CHAVE_GRUPO: {matUnic}, {codCateg}, {dtInicio} CONDICAO_GRUPO: O (se
                    {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr) = [9]); N (nos demais casos)
                :ivar ideEstab: Identificação do estabelecimento. DESCRICAO_COMPLETA:Identificação do
                    estabelecimento responsável pelo pagamento ao trabalhador dos valores informados neste
                    evento.
                """

                tpContr: InfoContrTpContr = field(
                    metadata={
                        "type": "Element",
                    }
                )
                indContr: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtAdmOrig: None | XmlDate = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                indReint: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                indCateg: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                indNatAtiv: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                indMotDeslig: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
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
                dtInicio: None | XmlDate = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoCompl: None | ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                mudCategAtiv: list[ESocial.EvtProcTrab.IdeTrab.InfoContr.MudCategAtiv] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                unicContr: list[ESocial.EvtProcTrab.IdeTrab.InfoContr.UnicContr] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                ideEstab: ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab = field(
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass(kw_only=True)
                class InfoCompl(CommonMixin):
                    """
                    :ivar codCBO: Classificação Brasileira de Ocupações - CBO. Validação: Preenchimento
                        obrigatório se {infoContr/codCateg}(../codCateg) for diferente de [901, 903, 904]). Se
                        informado, deve ser um código válido e existente na tabela de CBO, com 6 (seis)
                        posições.
                    :ivar natAtividade: Natureza da atividade. Validação: Preenchimento obrigatório se
                        {infoContr/codCateg}(../codCateg) for relativo a "Empregado", "Agente Público", "Avulso"
                        ou igual a [401, 731, 734, 738]. Não deve ser preenchido se
                        {infoContr/codCateg}(../codCateg) = [721, 722, 771, 901]. Se
                        {infoContr/codCateg}(../codCateg) = [104], deve ser preenchido com [1]. Se
                        {infoContr/codCateg}(../codCateg) = [102], deve ser preenchido com [2].
                    :ivar remuneracao: Informações da remuneração e periodicidade de pagamento. CHAVE_GRUPO:
                        {dtRemun} CONDICAO_GRUPO: N (se ({infoContr/tpContr}(../../tpContr) for diferente de [6]
                        e {tpRegTrab}(../infoVinc_tpRegTrab) = [2]); O (se ({infoContr/tpContr}(../../tpContr)
                        for diferente de [6] e {tpRegTrab}(../infoVinc_tpRegTrab) = [1]) ou se
                        {infoContr/codCateg}(../../codCateg) = [721, 722, 771]); OC (nos demais casos)
                    :ivar infoVinc: Informações sobre o vínculo trabalhista. CONDICAO_GRUPO: O (se
                        {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr) for diferente de [6]); N (nos demais
                        casos)
                    :ivar infoTerm: Informações de término de TSVE. CONDICAO_GRUPO: OC (se
                        {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr) = [6]; N (nos demais casos)
                    """

                    codCBO: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    natAtividade: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    remuneracao: list[ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.Remuneracao] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 99,
                        },
                    )
                    infoVinc: None | ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    infoTerm: None | ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoTerm = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class Remuneracao(CommonMixin):
                        """
                        :ivar dtRemun: Data a partir da qual as informações de remuneração e periodicidade de
                            pagamento estão vigentes. Validação: Deve ser igual ou posterior à data de admissão
                            (ou de início) e igual ou anterior à data de desligamento (ou de término), se
                            informada.
                        :ivar vrSalFx: Salário base do trabalhador, correspondente à parte fixa da remuneração
                            em {dtRemun}(./dtRemun). Validação: Se {undSalFixo}(./undSalFixo) for igual a [7],
                            preencher com 0 (zero).
                        :ivar undSalFixo:
                        :ivar dscSalVar: Descrição do salário por tarefa ou variável e como este é calculado.
                            Ex.: Comissões pagas no percentual de 10% sobre as vendas. Validação: Preenchimento
                            obrigatório se {undSalFixo}(./undSalFixo) for igual a [6, 7].
                        """

                        dtRemun: XmlDate = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        vrSalFx: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        undSalFixo: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        dscSalVar: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                    @dataclass(kw_only=True)
                    class InfoVinc(CommonMixin):
                        """
                        :ivar tpRegTrab: Tipo de regime trabalhista. Validação: Se
                            {infoContr/codCateg}(../../codCateg) = [104], deve ser preenchido com [1].
                        :ivar tpRegPrev: Tipo de regime previdenciário. Validação: Se
                            {infoContr/codCateg}(../../codCateg) = [104], deve ser preenchido com [1]. Se
                            {infoContr/codCateg}(../../codCateg) = [101, 102, 103, 105, 106, 107, 108, 111], não
                            pode ser preenchido com [2].
                        :ivar dtAdm: Preencher com a data de admissão do trabalhador. Validação: Deve ser
                            posterior à data de nascimento do trabalhador e igual ou anterior ao ano do óbito,
                            se existente.
                        :ivar tmpParc: Preencher com o código relativo ao tipo de contrato em tempo parcial.
                            Informar este campo apenas no caso de empregado submetido a horário de trabalho
                            (Capítulo II do Título II da CLT). Validação: Informação obrigatória e exclusiva se
                            {tpRegTrab}(./tpRegTrab) = [1]. O código [1] só é válido se
                            {infoContr/codCateg}(../../codCateg) = [104]. Os códigos [2, 3] não são válidos se
                            {infoContr/codCateg}(../../codCateg) = [104].
                        :ivar duracao: Duração do contrato de trabalho. CONDICAO_GRUPO: O (se
                            {tpRegTrab}(../tpRegTrab) = [1]); N (nos demais casos)
                        :ivar observacoes: Observações do contrato de trabalho. CONDICAO_GRUPO: OC
                        :ivar sucessaoVinc: Grupo de informações da sucessão de vínculo trabalhista/estatutário.
                            CONDICAO_GRUPO: OC
                        :ivar infoDeslig: Informações do desligamento. CONDICAO_GRUPO: O (se
                            {infoContr/tpContr}(2500_ideTrab_infoContr_tpContr) for diferente [8]); OC (nos
                            demais casos)
                        """

                        tpRegTrab: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        tpRegPrev: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        dtAdm: XmlDate = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        tmpParc: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        duracao: None | ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc.Duracao = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        observacoes: list[ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc.Observacoes] = (
                            field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 99,
                                },
                            )
                        )
                        sucessaoVinc: None | ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc.SucessaoVinc = (
                            field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                        )
                        infoDeslig: None | ESocial.EvtProcTrab.IdeTrab.InfoContr.InfoCompl.InfoVinc.InfoDeslig = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                        @dataclass(kw_only=True)
                        class Duracao(CommonMixin):
                            """
                            :ivar tpContr:
                            :ivar dtTerm: Data do término do contrato por prazo determinado. Validação: O
                                preenchimento é obrigatório se {duracao/tpContr}(./tpContr) = [2]. Não informar
                                se {duracao/tpContr}(./tpContr) = [1]. Se preenchido, deve ser igual ou
                                posterior à data de admissão (no caso de transferência, igual ou posterior a
                                {sucessaoVinc/dtTransf}(../sucessaoVinc_dtTransf)).
                            :ivar clauAssec: Indicar se o contrato por prazo determinado contém cláusula
                                assecuratória do direito recíproco de rescisão antes da data de seu término.
                                Validação: O preenchimento é obrigatório se {duracao/tpContr}(./tpContr) = [2,
                                3]. Não preencher se {duracao/tpContr}(./tpContr) = [1].
                            :ivar objDet: Indicação do objeto determinante da contratação por prazo determinado
                                (obra, serviço, safra, etc.). Validação: O preenchimento é obrigatório e
                                exclusivo se {duracao/tpContr}(./tpContr) = [3].
                            """

                            tpContr: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            dtTerm: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            clauAssec: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            objDet: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )

                        @dataclass(kw_only=True)
                        class Observacoes(CommonMixin):
                            """
                            :ivar observacao: Observação relacionada ao contrato de trabalho.
                            """

                            observacao: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

                        @dataclass(kw_only=True)
                        class SucessaoVinc(CommonMixin):
                            """
                            :ivar tpInsc:
                            :ivar nrInsc:
                            :ivar matricAnt: Matrícula do trabalhador no empregador anterior. Validação: Se
                                {sucessaoVinc/dtTransf}(./dtTransf) for igual ou posterior a [2024-04-22], a
                                matrícula informada neste campo deve ser idêntica à matricula do trabalhador no
                                empregador anterior.
                            :ivar dtTransf: Preencher com a data da transferência do empregado para o empregador
                                declarante. Validação: Deve ser posterior à data de admissão do trabalhador e
                                igual ou anterior ao ano do óbito, se existente.
                            """

                            tpInsc: SucessaoVincTpInsc = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            nrInsc: str = field(
                                metadata={
                                    "type": "Element",
                                    "pattern": r"\d{8,14}",
                                }
                            )
                            matricAnt: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            dtTransf: XmlDate = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

                        @dataclass(kw_only=True)
                        class InfoDeslig(CommonMixin):
                            """
                            :ivar dtDeslig: Preencher com a data de desligamento do vínculo (último dia
                                trabalhado). Validação: Deve ser igual ou posterior a {dtAdm}(../dtAdm) e não
                                superior à data atual (data do envio do evento) acrescida de 10 dias corridos.
                            :ivar mtvDeslig:
                            :ivar dtProjFimAPI: Data projetada para o término do aviso prévio indenizado.
                                Validação: Se informada, deve ser igual ou posterior a {dtDeslig}(./dtDeslig).
                            :ivar pensAlim: Indicativo de pensão alimentícia para fins de retenção de FGTS.
                                Validação: Preenchimento obrigatório e exclusivo se o vínculo for celetista
                                ({tpRegTrab}(../tpRegTrab) = [1]). Se
                                ({dtSent}(2500_infoProcesso_dadosCompl_infoProcJud_dtSent) ou
                                {dtCCP}(2500_infoProcesso_dadosCompl_infoCCP_dtCCP)) &lt; [2024-01-22], o
                                preenchimento é opcional.
                            :ivar percAliment:
                            :ivar vrAlim:
                            """

                            dtDeslig: XmlDate = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            mtvDeslig: str = field(
                                metadata={
                                    "type": "Element",
                                    "pattern": r"\d{2}",
                                }
                            )
                            dtProjFimAPI: None | XmlDate = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            pensAlim: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            percAliment: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            vrAlim: None | str = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )

                    @dataclass(kw_only=True)
                    class InfoTerm(CommonMixin):
                        """
                        :ivar dtTerm: Data do término. Validação: Deve ser igual ou posterior a
                            {dtInicio}(../../dtInicio) e igual ou anterior à data atual acrescida de 10 (dez)
                            dias.
                        :ivar mtvDesligTSV:
                        """

                        dtTerm: XmlDate = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        mtvDesligTSV: None | InfoTermMtvDesligTsv = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )

                @dataclass(kw_only=True)
                class MudCategAtiv(CommonMixin):
                    """
                    :ivar codCateg: Preencher com o código da categoria do trabalhador. Validação: Deve ser um
                        código válido e existente na Tabela 01 e obedecer ao que segue: a) Se {}(../indContr) =
                        [S], deve ser um código de categoria diferente daquele presente no contrato original; b)
                        Se {}(../indContr) = [N], deve ser um código de categoria diferente daquele informado em
                        {infoContr/codCateg}(../codCateg).
                    :ivar natAtividade: Natureza da atividade. Validação: Não informar se
                        {mudCategAtiv/codCateg}(./codCateg) = [721, 722, 771, 901] e observar o que segue: a) Se
                        {mudCategAtiv/codCateg}(./codCateg) = [104], não pode ser preenchido com [2]; b) Se
                        {mudCategAtiv/codCateg}(./codCateg) = [102], não pode ser preenchido com [1]; c) Se
                        {}(../indContr) = [S], deve ser uma natureza de atividade diferente daquela presente no
                        contrato original; d) Se {}(../indContr) = [N], deve ser uma natureza de atividade
                        diferente daquela informada em {infoContr/natAtividade}(../infoCompl_natAtividade).
                    :ivar dtMudCategAtiv: Data a partir da qual foi reconhecida a nova categoria e/ou a nova
                        natureza da atividade. Validação: Deve ser igual ou posterior à data de admissão (ou de
                        início) e igual ou anterior à data de desligamento, se informada. Se
                        {indContr}(../indContr) = [N], deve ser uma data posterior à data de admissão (ou de
                        início).
                    """

                    codCateg: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    natAtividade: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    dtMudCategAtiv: XmlDate = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass(kw_only=True)
                class UnicContr(CommonMixin):
                    """
                    :ivar matUnic: Informar a matrícula incorporada (matrícula cujo vínculo/contrato passou a
                        integrar período de unicidade contratual reconhecido judicialmente). O campo não deve
                        ser informado somente no caso de TSVE cadastrado em versão do leiaute anterior a S-1.0.
                        Validação: Deve corresponder a uma matrícula existente no RET para o respectivo
                        trabalhador e diferente do vínculo/contrato informado em
                        {infoContr}(2500_ideTrab_infoContr).
                    :ivar codCateg: Preencher com o código da categoria do trabalhador (código de categoria cujo
                        contrato passou a integrar período de unicidade contratual reconhecido judicialmente).
                        Validação: Informação obrigatória e exclusiva se o campo {matUnic}(./matUnic) não
                        estiver preenchido. Deve ser igual a um código de categoria de contrato cadastrado no
                        evento S-2300 e diferente do contrato informado em {infoContr}(2500_ideTrab_infoContr).
                    :ivar dtInicio: Data de início de TSVE (data de início cujo contrato passou a integrar
                        período de unicidade contratual reconhecido judicialmente). Validação: Informação
                        obrigatória e exclusiva se o campo {matUnic}(./matUnic) não estiver preenchido. Deve ser
                        igual a uma data de início de contrato cadastrado no evento S-2300 e diferente do
                        contrato informado em {infoContr}(2500_ideTrab_infoContr).
                    """

                    matUnic: None | str = field(
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
                    dtInicio: None | XmlDate = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class IdeEstab(CommonMixin):
                    """
                    :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição do estabelecimento,
                        de acordo com as opções da Tabela 05. No caso de empregador doméstico, informar [3]
                        (CAEPF). Validação: Se {ideEmpregador/tpInsc}(2500_ideEmpregador_tpInsc) = [1], deve ser
                        igual a [1, 4]. Se {ideEmpregador/tpInsc}(2500_ideEmpregador_tpInsc) = [2], deve ser
                        igual a [3, 4].
                    :ivar nrInsc: Informar o número de inscrição do estabelecimento do contribuinte de acordo
                        com o tipo de inscrição indicado no campo acima. No caso de empregador doméstico,
                        informar os 9 (nove) primeiros dígitos do CPF do empregador, seguidos de 5 (cinco)
                        dígitos 0 (zero). Por exemplo, se o CPF do empregador doméstico for 111111111-99,
                        informar 11111111100000. Validação: A inscrição informada deve ser compatível com
                        {ideEstab/tpInsc}(./tpInsc) e o número deve constar na base da RFB e pertencer a
                        {ideEmpregador/nrInsc}(2500_ideEmpregador_nrInsc). Se o processo for referente a
                        empregado doméstico, a inscrição informada deve ser igual aos 9 (nove) primeiros dígitos
                        do CPF do empregador, seguidos de 5 (cinco) dígitos 0 (zero).
                    :ivar infoVlr: Informações dos períodos e valores. Validação: Retornar alerta caso
                        {}(./indReperc) = [1 ou 5] e quantidade de grupos {}(./idePeriodo) seja diferente da
                        quantidade de meses compreendidos entre {}(./compIni) e {}(./compFim).
                        DESCRICAO_COMPLETA:Informações dos períodos e valores decorrentes de processo
                        trabalhista.
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
                    infoVlr: ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr = field(
                        metadata={
                            "type": "Element",
                        }
                    )

                    @dataclass(kw_only=True)
                    class InfoVlr(CommonMixin):
                        """
                        :ivar compIni: Competência inicial a que se refere o processo ou conciliação, no formato
                            AAAA-MM. Validação: Devem ser obedecidas as seguintes regras: a) Se
                            {infoContr/tpContr}(../../tpContr) = [1, 3, 7, 8, 9], deve ser igual ou posterior ao
                            mês/ano da data de admissão; b) Se {infoContr/tpContr}(../../tpContr) = [2, 4, 5],
                            deve ser igual ao mês/ano da data de admissão; c) Se
                            {infoContr/tpContr}(../../tpContr) = [6], deve ser igual ou posterior ao mês/ano da
                            data de início do TSVE.
                        :ivar compFim: Competência final a que se refere o processo ou conciliação, no formato
                            AAAA-MM. Validação: Deve ser igual ou posterior a {compIni}(./compIni) e igual ou
                            anterior ao mês/ano de {dtSent}(2500_infoProcesso_dadosCompl_infoProcJud_dtSent) ou
                            {dtCCP}(2500_infoProcesso_dadosCompl_infoCCP_dtCCP).
                        :ivar indReperc:
                        :ivar indenSD: Houve decisão para pagamento da indenização substitutiva do seguro-
                            desemprego?
                        :ivar indenAbono: Houve decisão para pagamento da indenização substitutiva de abono
                            salarial?
                        :ivar abono: Identificação do(s) ano(s)-base em que houve indenização substitutiva de
                            abono salarial. CHAVE_GRUPO: {anoBase} CONDICAO_GRUPO: O (se
                            {indenAbono}(../indenAbono) = [S]); N (nos demais casos)
                        :ivar idePeriodo: Identificação do período ao qual se referem as bases de cálculo.
                            CHAVE_GRUPO: {perRef} CONDICAO_GRUPO: O (se {indReperc}(../indReperc) = [1 ou 5]); N
                            (nos demais casos)
                        """

                        compIni: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        compFim: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        indReperc: InfoVlrIndReperc = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        indenSD: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        indenAbono: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        abono: list[ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.Abono] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 9,
                            },
                        )
                        idePeriodo: list[ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 999,
                            },
                        )

                        @dataclass(kw_only=True)
                        class Abono(CommonMixin):
                            anoBase: str = field(
                                metadata={
                                    "type": "Element",
                                    "min_inclusive": "1900",
                                    "pattern": r"\d{4}",
                                }
                            )

                        @dataclass(kw_only=True)
                        class IdePeriodo(CommonMixin):
                            """
                            :ivar perRef: Informar o mês/ano (formato AAAA-MM) de referência das informações.
                                Validação: Deve ser um período compreendido entre {compIni}(../compIni) e
                                {compFim}(../compFim), informado no formato AAAA-MM. Retornar alerta caso
                                {}(./perRef) seja posterior ao desligamento, se houver.
                            :ivar baseCalculo: Bases de cálculo de contribuição previdenciária decorrentes de
                                processo trabalhista e ainda não declaradas. CONDICAO_GRUPO: OC
                            :ivar infoFGTS: Informações referentes a bases de cálculo de FGTS para geração de
                                guia. DESCRICAO_COMPLETA:Informações referentes a bases de cálculo de FGTS
                                (valores históricos, sem atualização), inclusive valores de 13º salário, aviso
                                prévio indenizado e seu reflexo sobre o 13º salário, para geração de guia no
                                FGTS Digital. Os campos deste grupo serão somados para compor a base de cálculo
                                para geração de guia. CONDICAO_GRUPO: OC
                            :ivar baseMudCateg: Bases de cálculo já declaradas em GFIP, no caso de
                                reconhecimento de mudança de código de categoria. DESCRICAO_COMPLETA:Bases de
                                cálculo de contribuição previdenciária já declaradas anteriormente em GFIP ou no
                                evento S-1200 (exclusivamente para remuneração de trabalhador sem cadastro no
                                S-2300), no caso de reconhecimento de mudança de código de categoria.
                                CONDICAO_GRUPO: OC (se {indCateg}(2500_ideTrab_infoContr_indCateg) = [S]); N
                                (nos demais casos)
                            :ivar infoInterm: Informações relativas ao trabalho intermitente. CHAVE_GRUPO: {dia}
                                CONDICAO_GRUPO: O ((se {infoContr/indContr}(2500_ideTrab_infoContr_indContr) =
                                [N] e {infoContr/codCateg}(2500_ideTrab_infoContr_codCateg) = [111]) ou (se
                                {infoContr/indContr}(2500_ideTrab_infoContr_indContr) = [S] e o código de
                                categoria no RET for igual a [111])); N (nos demais casos)
                            """

                            perRef: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )
                            baseCalculo: (
                                None | ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo.BaseCalculo
                            ) = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            infoFGTS: (
                                None | ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo.InfoFgts
                            ) = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            baseMudCateg: (
                                None | ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo.BaseMudCateg
                            ) = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                },
                            )
                            infoInterm: list[str] = field(
                                default_factory=list,
                                metadata={
                                    "type": "Element",
                                    "max_occurs": 31,
                                },
                            )

                            @dataclass(kw_only=True)
                            class BaseCalculo(CommonMixin):
                                """
                                :ivar vrBcCpMensal: Valor da base de cálculo da contribuição previdenciária
                                    sobre a remuneração mensal do trabalhador. Validação: Deve ser maior ou
                                    igual a 0 (zero).
                                :ivar vrBcCp13: Valor da base de cálculo da contribuição previdenciária sobre a
                                    remuneração do trabalhador referente ao 13º salário. Validação: Deve ser
                                    maior ou igual a 0 (zero).
                                :ivar infoAgNocivo: Grau de exposição a agentes nocivos DESCRICAO_COMPLETA:Grupo
                                    referente ao detalhamento do grau de exposição do trabalhador aos agentes
                                    nocivos que ensejam a cobrança da contribuição adicional para financiamento
                                    dos benefícios de aposentadoria especial. CONDICAO_GRUPO: O (se o código de
                                    categoria for igual a [1XX, 2XX, 3XX, 731, 734, 738] ou se o código de
                                    categoria for igual a [4XX] com {categOrig} em S-2300 = [1XX, 2XX, 3XX, 731,
                                    734, 738]); N (nos demais casos)
                                """

                                vrBcCpMensal: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                vrBcCp13: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                infoAgNocivo: (
                                    None
                                    | ESocial.EvtProcTrab.IdeTrab.InfoContr.IdeEstab.InfoVlr.IdePeriodo.BaseCalculo.InfoAgNocivo
                                ) = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )

                                @dataclass(kw_only=True)
                                class InfoAgNocivo(CommonMixin):
                                    grauExp: str = field(
                                        metadata={
                                            "type": "Element",
                                        }
                                    )

                            @dataclass(kw_only=True)
                            class InfoFgts(CommonMixin):
                                """
                                :ivar vrBcFGTSProcTrab: Valor da base de cálculo de FGTS ainda não declarada em
                                    SEFIP ou no eSocial, inclusive de verba reconhecida no processo trabalhista.
                                    Validação: Deve ser maior ou igual a 0 (zero).
                                :ivar vrBcFGTSSefip: Valor da base de cálculo de FGTS declarada apenas em SEFIP
                                    (não informada no eSocial) e ainda não recolhida. Validação: Deve ser maior
                                    que 0 (zero).
                                :ivar vrBcFGTSDecAnt: Valor da base de cálculo de FGTS declarada anteriormente
                                    no eSocial e ainda não recolhida. Validação: Somente pode ser informado se
                                    {perRef}(../perRef) for anterior ao início do FGTS Digital. Deve ser maior
                                    que 0 (zero).
                                """

                                vrBcFGTSProcTrab: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                vrBcFGTSSefip: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )
                                vrBcFGTSDecAnt: None | str = field(
                                    default=None,
                                    metadata={
                                        "type": "Element",
                                    },
                                )

                            @dataclass(kw_only=True)
                            class BaseMudCateg(CommonMixin):
                                """
                                :ivar codCateg: Preencher com o código da categoria do trabalhador declarado no
                                    período de referência. Validação: Deve ser um código válido e existente na
                                    Tabela 01.
                                :ivar vrBcCPrev: Valor da remuneração do trabalhador a ser considerada para fins
                                    previdenciários declarada em GFIP ou em S-1200 de trabalhador sem cadastro
                                    no S-2300. Validação: Deve ser maior que 0 (zero).
                                """

                                codCateg: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
                                vrBcCPrev: str = field(
                                    metadata={
                                        "type": "Element",
                                    }
                                )
