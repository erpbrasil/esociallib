from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00"


@dataclass(kw_only=True)
class TIdePeriodo(CommonMixin):
    """
    Período de validade das informações.

    CHAVE_GRUPO: {iniValid*}, {fimValid*}.
    """

    class Meta:
        name = "T_idePeriodo"

    iniValid: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        }
    )
    fimValid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )


class TInfoCadastroIndDesFolha(Enum):
    """
    Indicativo de opção/enquadramento de desoneração da folha.

    Validação: Pode ser igual a [1] apenas se {classTrib}(./classTrib) = [02, 03, 99]. Pode ser igual a [2] apenas
    para as naturezas jurídicas iguais a [103-1, 106-6, 124-4, 133-3]. Nos demais casos, deve ser igual a [0].

    :cvar VALUE_0: Não aplicável
    :cvar VALUE_1: Empresa enquadrada nos critérios da legislação vigente
    :cvar VALUE_2: Município enquadrado nos critérios da legislação vigente
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class TInfoCadastroIndOpcCp(Enum):
    """
    Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária, nos termos do
    art. 25, § 13, da Lei 8.212/1991 e do art. 25, § 7°, da Lei 8.870/1994.

    O não preenchimento deste campo por parte do produtor rural implica opção pela comercialização da sua produção.
    Validação: Não preencher se {classTrib}(./classTrib) for diferente de [07, 21].

    :cvar VALUE_1: Sobre a comercialização da sua produção
    :cvar VALUE_2: Sobre a folha de pagamento
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TInfoCadastroIndOptRegEletron(Enum):
    """
    Indica se houve opção pelo registro eletrônico de empregados.

    Caso o declarante seja órgão público sem empregados regidos pela CLT, informar [0].

    :cvar VALUE_0: Não optou pelo registro eletrônico de empregados (ou opção não aplicável)
    :cvar VALUE_1: Optou pelo registro eletrônico de empregados
    """

    VALUE_0 = 0
    VALUE_1 = 1


class TInfoCadastroIndPertIrrf(Enum):
    """
    Indicador de pertencimento do IRRF.

    Validação: Preenchimento exclusivo para o empregador com natureza jurídica igual a [126-0, 127-9, 129-5,
    130-9].

    :cvar S: Sim
    """

    S = "S"


class TInfoCadastroIndPorte(Enum):
    """
    Indicativo de microempresa - ME ou empresa de pequeno porte - EPP para permissão de acesso ao módulo
    simplificado.

    Não preencher caso o empregador não se enquadre como micro ou pequena empresa. Validação: Não preencher se
    {classTrib}(./classTrib) = [21, 22].

    :cvar S: Sim
    """

    S = "S"


class TInfoCadastroIndTribFolhaPisPasep(Enum):
    """
    Indicador de tributação sobre a folha de pagamento - PIS e PASEP.

    Preenchimento exclusivo para o empregador em situação de tributação de PIS e PASEP sobre a folha de pagamento.

    :cvar S: Sim
    """

    S = "S"


class InfoOrgInternacionalIndAcordoIsenMulta(Enum):
    """
    Indicativo da existência de acordo internacional para isenção de multa.

    :cvar VALUE_0: Sem acordo
    :cvar VALUE_1: Com acordo
    """

    VALUE_0 = 0
    VALUE_1 = 1


@dataclass(kw_only=True)
class TInfoCadastro(CommonMixin):
    """
    Detalhamento das informações do empregador.

    CONDICAO_GRUPO: N (se {procEmi}(1000_ideEvento_procEmi) = [8]); O (nos demais casos).

    :ivar classTrib:
    :ivar indCoop: Indicativo de cooperativa. Validação: O preenchimento do campo é exclusivo e obrigatório para
        PJ. Somente pode ser diferente de [0] se a natureza jurídica do declarante for igual a 214-3.
    :ivar indConstr: Indicativo de construtora. Validação: O preenchimento do campo é exclusivo e obrigatório
        para PJ.
    :ivar indDesFolha:
    :ivar indOpcCP:
    :ivar indPorte:
    :ivar indOptRegEletron:
    :ivar cnpjEFR: CNPJ do Ente Federativo Responsável - EFR. Validação: Preenchimento obrigatório e exclusivo
        se a natureza jurídica do declarante for Administração Pública (grupo [1]). Nesse caso, informar o campo
        com 14 (catorze) algarismos. Informação validada no cadastro do CNPJ da RFB.
    :ivar dtTrans11096: Data da transformação em sociedade de fins lucrativos - Lei 11.096/2005. Validação: Não
        preencher se {classTrib}(./classTrib) = [21, 22]. Se informada, deve ser maior que [2005-11-21] e menor
        ou igual à data atual.
    :ivar indTribFolhaPisPasep:
    :ivar indPertIRRF:
    :ivar dadosIsencao: Informações complementares - Empresas isentas - Dados da isenção. CONDICAO_GRUPO: OC (se
        {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) = [80]); N (nos demais casos)
    :ivar infoOrgInternacional: Informações exclusivas de organismos internacionais e outras instituições
        extraterritoriais. CONDICAO_GRUPO: O (se a natureza jurídica pertencer ao grupo [5]); N (nos demais
        casos)
    """

    class Meta:
        name = "T_infoCadastro"

    classTrib: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
            "pattern": r"\d{2}",
        }
    )
    indCoop: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    indConstr: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    indDesFolha: TInfoCadastroIndDesFolha = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        }
    )
    indOpcCP: None | TInfoCadastroIndOpcCp = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    indPorte: None | TInfoCadastroIndPorte = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    indOptRegEletron: TInfoCadastroIndOptRegEletron = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        }
    )
    cnpjEFR: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    dtTrans11096: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    indTribFolhaPisPasep: None | TInfoCadastroIndTribFolhaPisPasep = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    indPertIRRF: None | TInfoCadastroIndPertIrrf = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    dadosIsencao: None | TInfoCadastro.DadosIsencao = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )
    infoOrgInternacional: None | TInfoCadastro.InfoOrgInternacional = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
        },
    )

    @dataclass(kw_only=True)
    class DadosIsencao(CommonMixin):
        """
        :ivar ideMinLei:
        :ivar nrCertif:
        :ivar dtEmisCertif: Data de emissão do certificado/publicação da lei.
        :ivar dtVencCertif: Data de vencimento do certificado. Validação: Não pode ser anterior a
            {dtEmisCertif}(./dtEmisCertif).
        :ivar nrProtRenov:
        :ivar dtProtRenov: Data do protocolo de renovação.
        :ivar dtDou: Data de publicação no Diário Oficial da União - DOU.
        :ivar pagDou:
        """

        ideMinLei: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
                "min_length": 1,
                "max_length": 70,
                "pattern": r".*[^\s].*",
            }
        )
        nrCertif: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
                "min_length": 1,
                "max_length": 40,
                "pattern": r".*[^\s].*",
            }
        )
        dtEmisCertif: XmlDate = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
            }
        )
        dtVencCertif: XmlDate = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
            }
        )
        nrProtRenov: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
                "min_length": 1,
                "max_length": 40,
                "pattern": r".*[^\s].*",
            },
        )
        dtProtRenov: None | XmlDate = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
            },
        )
        dtDou: None | XmlDate = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
            },
        )
        pagDou: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
                "pattern": r"\d{1,5}",
            },
        )

    @dataclass(kw_only=True)
    class InfoOrgInternacional(CommonMixin):
        indAcordoIsenMulta: InfoOrgInternacionalIndAcordoIsenMulta = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00",
            }
        )


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-1000 - Informações do Empregador/Contribuinte/Órgão Público.

    :ivar evtInfoEmpregador: Evento Informações do Empregador. CHAVE_GRUPO: {Id}
        REGRA:REGRA_ENVIO_PROC_FECHAMENTO REGRA:REGRA_INFO_EMP_PERIODO_CONFLITANTE
        REGRA:REGRA_INFO_EMP_VALIDA_CLASSTRIB_NATJURID REGRA:REGRA_INFO_EMP_VALIDA_DTINICIAL
        REGRA:REGRA_TAB_PERMITE_EXCLUSAO REGRA:REGRA_VALIDA_DT_FUTURA REGRA:REGRA_VALIDA_EMPREGADOR
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v_S_01_03_00"

    evtInfoEmpregador: ESocial.EvtInfoEmpregador = field(
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
    class EvtInfoEmpregador(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador: Informações de identificação do empregador. CHAVE_GRUPO: {tpInsc*}, {nrInsc*}
        :ivar infoEmpregador: Informações do empregador. DESCRICAO_COMPLETA:Identificação da operação (inclusão,
            alteração ou exclusão) e das respectivas informações do empregador.
        :ivar Id:
        """

        ideEvento: str = field(
            metadata={
                "type": "Element",
            }
        )
        ideEmpregador: ESocial.EvtInfoEmpregador.IdeEmpregador = field(
            metadata={
                "type": "Element",
            }
        )
        infoEmpregador: ESocial.EvtInfoEmpregador.InfoEmpregador = field(
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
            :ivar tpInsc:
            :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição
                indicado no campo {tpInsc}(./tpInsc). Validação: Se {tpInsc}(./tpInsc) for igual a [1], deve ser
                um número de CNPJ válido. Neste caso, deve ser informada apenas a raiz/base (8 posições), exceto
                se a natureza jurídica do declarante for igual a 101-5, 104-0, 107-4, 116-3 ou 134-1, situação
                em que o campo deve ser preenchido com o CNPJ completo (14 posições). Se {tpInsc}(./tpInsc) for
                igual a [2], deve ser um CPF válido.
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
        class InfoEmpregador(CommonMixin):
            """
            :ivar inclusao: Inclusão de novas informações. CONDICAO_GRUPO: OC
            :ivar alteracao: Alteração das informações. CONDICAO_GRUPO: OC
            :ivar exclusao: Exclusão das informações. CONDICAO_GRUPO: OC
            """

            inclusao: None | ESocial.EvtInfoEmpregador.InfoEmpregador.Inclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            alteracao: None | ESocial.EvtInfoEmpregador.InfoEmpregador.Alteracao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            exclusao: None | ESocial.EvtInfoEmpregador.InfoEmpregador.Exclusao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Inclusao(CommonMixin):
                idePeriodo: TIdePeriodo = field(
                    metadata={
                        "type": "Element",
                    }
                )
                infoCadastro: None | TInfoCadastro = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Alteracao(CommonMixin):
                """
                :ivar idePeriodo:
                :ivar infoCadastro:
                :ivar novaValidade: Novo período de validade das informações. DESCRICAO_COMPLETA:Informação
                    preenchida exclusivamente em caso de alteração do período de validade das informações,
                    apresentando o novo período de validade. CONDICAO_GRUPO: OC
                """

                idePeriodo: TIdePeriodo = field(
                    metadata={
                        "type": "Element",
                    }
                )
                infoCadastro: None | TInfoCadastro = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                novaValidade: None | TIdePeriodo = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Exclusao(CommonMixin):
                idePeriodo: TIdePeriodo = field(
                    metadata={
                        "type": "Element",
                    }
                )
