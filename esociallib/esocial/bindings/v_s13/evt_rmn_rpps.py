from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v_S_01_03_00"


@dataclass(kw_only=True)
class TItensRemunRppsDescFolha(CommonMixin):
    class Meta:
        name = "T_itensRemun_rpps_descFolha"

    descFolha: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v_S_01_03_00",
        },
    )


@dataclass(kw_only=True)
class TRemunPerAnt(CommonMixin):
    """
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
        matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve
        corresponder à matrícula informada pelo empregador no evento S-2200 ou S-2300 do respectivo contrato.
        Não preencher no caso de Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE sem informação de
        matrícula no evento S-2300 ou, no caso de
        {remunPerAnt}(1202_dmDev_infoPerAnt_idePeriodo_ideEstab_remunPerAnt), se
        {remunOrgSuc}(1202_dmDev_infoPerAnt_remunOrgSuc) = [S].
    :ivar itensRemun:
    """

    class Meta:
        name = "T_remunPerAnt"

    matricula: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v_S_01_03_00",
        },
    )
    itensRemun: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v_S_01_03_00",
            "min_occurs": 1,
            "max_occurs": 200,
        },
    )


@dataclass(kw_only=True)
class TRemunPer(CommonMixin):
    """
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
        matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve
        corresponder à matrícula informada pelo empregador no evento S-2200 ou S-2300 do respectivo contrato.
        Não preencher no caso de Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE sem informação de
        matrícula no evento S-2300 ou, no caso de
        {remunPerAnt}(1202_dmDev_infoPerAnt_idePeriodo_ideEstab_remunPerAnt), se
        {remunOrgSuc}(1202_dmDev_infoPerAnt_remunOrgSuc) = [S].
    :ivar itensRemun:
    """

    class Meta:
        name = "T_remunPer"

    matricula: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v_S_01_03_00",
        },
    )
    itensRemun: list[TItensRemunRppsDescFolha] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v_S_01_03_00",
            "min_occurs": 1,
            "max_occurs": 200,
        },
    )


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1202 - Remuneração de Servidor vinculado ao Regime Próprio de Previd.

    Social.

    :ivar evtRmnRPPS: Evento Remuneração de Servidor vinculado ao RPPS DESCRICAO_COMPLETA:Evento Remuneração de
        Servidor vinculado ao Regime Próprio de Previdência Social. CHAVE_GRUPO: {Id}
        REGRA:REGRA_COMPATIBILIDADE_CATEGORIA_CLASSTRIB REGRA:REGRA_COMPATIB_REGIME_PREV
        REGRA:REGRA_CONTROLE_DUPLICIDADE REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_EVENTOS_EXTEMP
        REGRA:REGRA_EVENTO_POSTERIOR_CAT_OBITO REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB REGRA:REGRA_REMUN_ANUAL_DEZEMBRO
        REGRA:REGRA_REMUN_CATEG_EXISTENTE_RET REGRA:REGRA_REMUN_IND_RETIFICACAO
        REGRA:REGRA_REMUN_JA_EXISTE_DESLIGAMENTO REGRA:REGRA_REMUN_PERMITE_EXCLUSAO
        REGRA:REGRA_REMUN_TRAB_EXISTENTE_RET REGRA:REGRA_REMUN_VALIDA_INFO_COMPLEMENTAR
        REGRA:REGRA_RUBRICA_ECONSIGNADO REGRA:REGRA_TSV_ATIVO_NA_DTEVENTO REGRA:REGRA_VALIDA_EMPREGADOR
        REGRA:REGRA_VALIDA_PERIODO_APURACAO
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtRmnRPPS/v_S_01_03_00"

    evtRmnRPPS: ESocial.EvtRmnRpps = field(
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
    class EvtRmnRpps(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar ideTrabalhador: Identificação do trabalhador. CHAVE_GRUPO: {cpfTrab*}
        :ivar dmDev: Demonstrativo de valores devidos ao trabalhador DESCRICAO_COMPLETA:Identificação de cada um
            dos demonstrativos de valores devidos ao trabalhador. CHAVE_GRUPO: {ideDmDev}
            REGRA:REGRA_DEMONSTRATIVO
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
        ideTrabalhador: ESocial.EvtRmnRpps.IdeTrabalhador = field(
            metadata={
                "type": "Element",
            }
        )
        dmDev: list[ESocial.EvtRmnRpps.DmDev] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )

        @dataclass(kw_only=True)
        class IdeTrabalhador(CommonMixin):
            """
            :ivar cpfTrab:
            :ivar infoComplem: Informações complementares de identificação do trabalhador
                DESCRICAO_COMPLETA:Grupo preenchido quando o evento de remuneração se referir a trabalhador cuja
                categoria não está sujeita ao evento de admissão ou ao evento TSVE - Início, bem como para
                informar remuneração devida pelo órgão sucessor a servidor desligado ainda no sucedido. No caso
                das categorias em que o evento TSVE - Início for opcional, o preenchimento do grupo somente é
                exigido se não existir o respectivo evento. As informações complementares são necessárias para
                correta identificação do trabalhador. CONDICAO_GRUPO: O ((se o trabalhador não tiver nenhum
                cadastro no RET) OU (se {remunOrgSuc}(1202_dmDev_infoPerAnt_remunOrgSuc) = [S])); N (se o
                trabalhador tiver cadastro ativo no RET); OC (nos demais casos)
            """

            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            infoComplem: None | ESocial.EvtRmnRpps.IdeTrabalhador.InfoComplem = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class InfoComplem(CommonMixin):
                """
                :ivar nmTrab:
                :ivar dtNascto:
                :ivar sucessaoVinc: Grupo de informações da sucessão de vínculo. CONDICAO_GRUPO: O (se
                    {remunOrgSuc}(1202_dmDev_infoPerAnt_remunOrgSuc) = [S]); N (nos demais casos)
                """

                nmTrab: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtNascto: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                sucessaoVinc: None | ESocial.EvtRmnRpps.IdeTrabalhador.InfoComplem.SucessaoVinc = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class SucessaoVinc(CommonMixin):
                    """
                    :ivar cnpjOrgaoAnt: Informar o CNPJ do órgão público anterior. Validação: Deve ser um CNPJ
                        válido e diferente da inscrição do declarante, considerando as particularidades
                        aplicadas à informação de CNPJ de órgão público em S-1000. Além disso, deve possuir 14
                        (catorze) algarismos e ser diferente do CNPJ base do órgão público declarante (exceto se
                        {ideEmpregador/nrInsc}(1202_ideEmpregador_nrInsc) tiver 14 (catorze) algarismos) e dos
                        estabelecimentos informados através do evento S-1005.
                    :ivar matricAnt: Matrícula do trabalhador no órgão público anterior.
                    :ivar dtExercicio: Preencher com a data de exercício do servidor. No caso de transferência
                        do servidor, deve ser preenchida a data inicial do vínculo no primeiro órgão público
                        (data de início do vínculo).
                    :ivar observacao:
                    """

                    cnpjOrgaoAnt: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    matricAnt: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    dtExercicio: XmlDate = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    observacao: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

        @dataclass(kw_only=True)
        class DmDev(CommonMixin):
            """
            :ivar ideDmDev: Identificador atribuído pelo órgão público para o demonstrativo de valores devidos
                ao trabalhador. O ente público pode preencher este campo utilizando-se de um identificador
                padrão para todos os trabalhadores; no entanto, havendo mais de um demonstrativo relativo a uma
                mesma competência, devem ser utilizados identificadores diferentes para cada um dos
                demonstrativos. Validação: Deve ser um identificador único dentro do mesmo
                {perApur}(1202_ideEvento_perApur) para cada um dos demonstrativos do trabalhador.
                REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar codCateg:
            :ivar indRRA:
            :ivar infoRRA:
            :ivar infoPerApur: Informações relativas ao período de apuração. CONDICAO_GRUPO: O (se não existir o
                grupo {infoPerAnt}(1202_dmDev_infoPerAnt)); OC (nos demais casos)
            :ivar infoPerAnt: Informações relativas a períodos anteriores DESCRICAO_COMPLETA:Grupo destinado às
                informações de: a) remuneração relativa a diferenças de vencimento provenientes de disposições
                legais; b) verbas de natureza salarial ou não salarial devidas após o desligamento; c) decisões
                administrativas ou judiciais relativas a diferenças de remuneração. OBS.: As informações
                previstas acima podem se referir ao período de apuração definido em
                {perApur}(1202_ideEvento_perApur) ou a períodos anteriores a {perApur}(1202_ideEvento_perApur).
                CONDICAO_GRUPO: O (se não existir o grupo {infoPerApur}(1202_dmDev_infoPerApur) e
                {indApuracao}(1202_ideEvento_indApuracao) = [1]); N (se
                {indApuracao}(1202_ideEvento_indApuracao) = [2]); OC (nos demais casos)
            """

            ideDmDev: str = field(
                metadata={
                    "type": "Element",
                }
            )
            codCateg: str = field(
                metadata={
                    "type": "Element",
                }
            )
            indRRA: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoRRA: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoPerApur: None | ESocial.EvtRmnRpps.DmDev.InfoPerApur = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoPerAnt: None | ESocial.EvtRmnRpps.DmDev.InfoPerAnt = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class InfoPerApur(CommonMixin):
                """
                :ivar ideEstab: Identificação da unidade do órgão público DESCRICAO_COMPLETA:Identificação da
                    unidade do órgão público na qual o servidor possui remuneração. CHAVE_GRUPO: {tpInsc},
                    {nrInsc}
                """

                ideEstab: list[ESocial.EvtRmnRpps.DmDev.InfoPerApur.IdeEstab] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 500,
                    },
                )

                @dataclass(kw_only=True)
                class IdeEstab(CommonMixin):
                    """
                    :ivar tpInsc:
                    :ivar nrInsc: Informar o número de inscrição da unidade do órgão público ou do
                        estabelecimento, de acordo com o tipo de inscrição indicado no campo
                        {ideEstab/tpInsc}(./tpInsc).
                    :ivar remunPerApur: Remuneração do trabalhador DESCRICAO_COMPLETA:Informações relativas à
                        remuneração do trabalhador no período de apuração. CHAVE_GRUPO: {matricula}
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
                    remunPerApur: list[TRemunPer] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 8,
                        },
                    )

            @dataclass(kw_only=True)
            class InfoPerAnt(CommonMixin):
                """
                :ivar remunOrgSuc: Indicar se a remuneração é relativa a verbas de natureza salarial ou não
                    salarial devidas pelo órgão sucessor a servidor desligado ainda no sucedido.
                :ivar idePeriodo: Identificação do período de referência da remuneração
                    DESCRICAO_COMPLETA:Identificação do período ao qual se referem as diferenças de remuneração.
                    CHAVE_GRUPO: {perRef}
                """

                remunOrgSuc: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                idePeriodo: list[ESocial.EvtRmnRpps.DmDev.InfoPerAnt.IdePeriodo] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 180,
                    },
                )

                @dataclass(kw_only=True)
                class IdePeriodo(CommonMixin):
                    """
                    :ivar perRef: Informar o período ao qual se refere o complemento de remuneração, no formato
                        AAAA-MM. Validação: Deve ser igual ou anterior ao período de apuração informado em
                        {perApur}(/ideEvento_perApur). Deve ser informado no formato AAAA-MM.
                    :ivar ideEstab: Identificação da unidade do órgão público DESCRICAO_COMPLETA:Identificação
                        da unidade do órgão público na qual o servidor possui remuneração. CHAVE_GRUPO:
                        {tpInsc}, {nrInsc}
                    """

                    perRef: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    ideEstab: list[ESocial.EvtRmnRpps.DmDev.InfoPerAnt.IdePeriodo.IdeEstab] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 500,
                        },
                    )

                    @dataclass(kw_only=True)
                    class IdeEstab(CommonMixin):
                        """
                        :ivar tpInsc:
                        :ivar nrInsc: Informar o número de inscrição da unidade do órgão público ou do
                            estabelecimento, de acordo com o tipo de inscrição indicado no campo
                            {ideEstab/tpInsc}(./tpInsc).
                        :ivar remunPerAnt: Remuneração do trabalhador DESCRICAO_COMPLETA:Informações relativas à
                            remuneração do trabalhador em períodos anteriores. CHAVE_GRUPO: {matricula}
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
                        remunPerAnt: list[TRemunPerAnt] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 8,
                            },
                        )
