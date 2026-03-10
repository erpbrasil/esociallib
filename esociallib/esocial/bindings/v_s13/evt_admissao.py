from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin
from esociallib.esocial.bindings.v_s13.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_03_00"


class InfoCeletistaIndAdmissao(Enum):
    """
    Indicativo de admissão.

    :cvar VALUE_1: Normal
    :cvar VALUE_2: Decorrente de ação fiscal
    :cvar VALUE_3: Decorrente de decisão judicial
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class InfoCeletistaTpAdmissao(Enum):
    """
    Tipo de admissão do trabalhador.

    Validação: Se for igual a [5], {codCateg}(2200_vinculo_infoContrato_codCateg) deve ser igual a [104] e
    {procEmi}(2200_ideEvento_procEmi) deve ser igual a [2, 22]. Se for igual a [6], {cadIni}(2200_vinculo_cadIni)
    deve ser igual a [N].

    :cvar VALUE_1: Admissão
    :cvar VALUE_2: Transferência de empresa do mesmo grupo econômico ou transferência entre órgãos do mesmo Ente
        Federativo
    :cvar VALUE_3: Transferência de empresa consorciada ou de consórcio
    :cvar VALUE_4: Transferência por motivo de sucessão, incorporação, cisão ou fusão
    :cvar VALUE_5: Transferência do empregado doméstico para outro representante da mesma unidade familiar
    :cvar VALUE_6: Mudança de CPF
    :cvar VALUE_7: Transferência quando a empresa sucedida é considerada inapta por inexistência de fato
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class InfoEstatutarioTpProv(Enum):
    """
    Preencher com o tipo de provimento.

    Validação: Os valores [3, 5, 6, 8, 9] só são permitidos se a natureza jurídica do declarante for Administração
    Pública (grupo [1]). Se {codCateg}(2200_vinculo_infoContrato_codCateg) = [302], deve ser preenchido com [2, 5,
    8, 10].

    :cvar VALUE_1: Nomeação em cargo efetivo
    :cvar VALUE_2: Nomeação exclusivamente em cargo em comissão
    :cvar VALUE_3: Incorporação ou matrícula (militar)
    :cvar VALUE_5: Redistribuição ou Reforma Administrativa
    :cvar VALUE_6: Diplomação
    :cvar VALUE_7: Contratação por tempo determinado
    :cvar VALUE_8: Remoção (em caso de alteração do órgão declarante)
    :cvar VALUE_9: Designação
    :cvar VALUE_10: Mudança de CPF
    :cvar VALUE_11: Estabilizados - Art. 19 do ADCT
    :cvar VALUE_99: Outros não relacionados acima
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_99 = 99


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


class TrabTemporarioHipLeg(Enum):
    """
    Hipótese legal para contratação de trabalhador temporário.

    :cvar VALUE_1: Necessidade de substituição transitória de pessoal permanente
    :cvar VALUE_2: Demanda complementar de serviços
    """

    VALUE_1 = 1
    VALUE_2 = 2


class VinculoCadIni(Enum):
    """
    Indicar se o evento se refere a cadastramento inicial de vínculo (o ingresso do trabalhador no empregador
    declarante, por admissão ou transferência, é anterior à data de início da obrigatoriedade de envio de seus
    eventos não periódicos) ou se refere a admissão (o ingresso do trabalhador no empregador declarante é igual ou
    posterior à data de início de obrigatoriedade de envio de seus eventos não periódicos).

    :cvar S: Sim (Cadastramento Inicial)
    :cvar N: Não (Admissão)
    """

    S = "S"
    N = "N"


@dataclass(kw_only=True)
class ESocial(CommonMixin):
    """
    S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador.

    :ivar evtAdmissao: Evento Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador. CHAVE_GRUPO:
        {Id} REGRA:REGRA_ADMISSAO_POSTERIOR_INICIO_ATIVIDADES REGRA:REGRA_ADMISSAO_VALIDA_DT_ADM
        REGRA:REGRA_ADMISSAO_VALIDA_DURACAO_CONTRATO REGRA:REGRA_ANOTACAO_JUDICIAL
        REGRA:REGRA_BLOQUEIA_USO_CPF_EMPREGADOR REGRA:REGRA_COMPATIBILIDADE_CATEGORIA_CLASSTRIB
        REGRA:REGRA_COMPATIB_CATEG_EVENTO REGRA:REGRA_EMPREGADO_DOMESTICO REGRA:REGRA_ENVIO_PROC_FECHAMENTO
        REGRA:REGRA_EVENTOS_EXTEMP REGRA:REGRA_EVETRAB_VALIDA_OPCAO_FGTS
        REGRA:REGRA_EXCLUSAO_ADMISSAO_TSVE_INICIO REGRA:REGRA_EXISTE_INFO_EMPREGADOR
        REGRA:REGRA_EXTEMP_DOMESTICO REGRA:REGRA_EXTEMP_REINTEGRACAO REGRA:REGRA_GERAL_VALIDA_DADOS_TABCONTRIB
        REGRA:REGRA_MESMO_PROCEMI REGRA:REGRA_MUDANCA_CPF REGRA:REGRA_REGISTRO_PRELIMINAR
        REGRA:REGRA_RETIFICA_MESMO_VINCULO REGRA:REGRA_VALIDA_EMPREGADOR REGRA:REGRA_VALIDA_MATRICULA
        REGRA:REGRA_VALIDA_TRABALHADOR_BASE_CPF
    :ivar Signature:
    """

    class Meta:
        name = "eSocial"
        namespace = "http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_03_00"

    evtAdmissao: ESocial.EvtAdmissao = field(
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
    class EvtAdmissao(CommonMixin):
        """
        :ivar ideEvento:
        :ivar ideEmpregador:
        :ivar trabalhador: Informações pessoais do trabalhador. CHAVE_GRUPO: {cpfTrab*}
        :ivar vinculo: Informações do vínculo. DESCRICAO_COMPLETA:Grupo de informações do vínculo. CHAVE_GRUPO:
            {matricula*}
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
        trabalhador: ESocial.EvtAdmissao.Trabalhador = field(
            metadata={
                "type": "Element",
            }
        )
        vinculo: ESocial.EvtAdmissao.Vinculo = field(
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
        class Trabalhador(CommonMixin):
            """
            :ivar cpfTrab:
            :ivar nmTrab:
            :ivar sexo:
            :ivar racaCor: Etnia e raça do trabalhador, conforme sua autoclassificação (art. 39, § 8º, da Lei
                12.288/2010). Validação: Se {dtAdm}(2200_vinculo_infoRegimeTrab_infoCeletista_dtAdm),
                {dtExercicio}(2200_vinculo_infoRegimeTrab_infoEstatutario_dtExercicio),
                {sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf) ou
                {transfDom/dtTransf}(2200_vinculo_transfDom_dtTransf) (maior data entre elas) for igual ou
                posterior a [2024-04-22], não pode ser informado o valor [6].
            :ivar estCiv:
            :ivar grauInstr:
            :ivar nmSoc:
            :ivar nascimento:
            :ivar endereco: Endereço do trabalhador DESCRICAO_COMPLETA:Grupo de informações do endereço do
                trabalhador. CONDICAO_GRUPO: N (se {tpRegPrev}(2200_vinculo_tpRegPrev) = [4]); O (se grupo
                {desligamento}(2200_vinculo_desligamento) não estiver preenchido e se
                {tpRegPrev}(2200_vinculo_tpRegPrev) for diferente de [4]); F (nos demais casos)
            :ivar trabImig: Informações do trabalhador imigrante. CONDICAO_GRUPO: N (se
                {paisNac}(2200_trabalhador_nascimento_paisNac) = [105]); OC (se
                {paisNac}(2200_trabalhador_nascimento_paisNac) for diferente de [105]) e se grupo
                {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais casos)
            :ivar infoDeficiencia: Pessoa com deficiência. CONDICAO_GRUPO: N (se
                {tpRegPrev}(2200_vinculo_tpRegPrev) = [4]); OC (se grupo
                {desligamento}(2200_vinculo_desligamento) não estiver preenchido e se
                {tpRegPrev}(2200_vinculo_tpRegPrev) for diferente de [4]); F (nos demais casos)
            :ivar dependente: Informações dos dependentes. CHAVE_GRUPO: {tpDep}, {nmDep}, {dtNascto}
                CONDICAO_GRUPO: OC
            :ivar contato: Informações de contato. CONDICAO_GRUPO: N (se {tpRegPrev}(2200_vinculo_tpRegPrev) =
                [4]); OC (se grupo {desligamento}(2200_vinculo_desligamento) não estiver preenchido e se
                {tpRegPrev}(2200_vinculo_tpRegPrev) for diferente de [4]); F (nos demais casos)
            """

            cpfTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nmTrab: str = field(
                metadata={
                    "type": "Element",
                }
            )
            sexo: str = field(
                metadata={
                    "type": "Element",
                }
            )
            racaCor: str = field(
                metadata={
                    "type": "Element",
                }
            )
            estCiv: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            grauInstr: str = field(
                metadata={
                    "type": "Element",
                }
            )
            nmSoc: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            nascimento: str = field(
                metadata={
                    "type": "Element",
                }
            )
            endereco: None | ESocial.EvtAdmissao.Trabalhador.Endereco = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            trabImig: None | ESocial.EvtAdmissao.Trabalhador.TrabImig = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            infoDeficiencia: None | ESocial.EvtAdmissao.Trabalhador.InfoDeficiencia = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            dependente: list[ESocial.EvtAdmissao.Trabalhador.Dependente] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                },
            )
            contato: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class Endereco(CommonMixin):
                """
                :ivar brasil: Endereço no Brasil. CONDICAO_GRUPO: O (se não informados os grupos
                    {exterior}(2200_trabalhador_endereco_exterior) e {desligamento}(2200_vinculo_desligamento));
                    N (se grupo {exterior}(2200_trabalhador_endereco_exterior) estiver preenchido); F (nos
                    demais casos)
                :ivar exterior: Endereço no exterior. CONDICAO_GRUPO: O (se não informados os grupos
                    {brasil}(2200_trabalhador_endereco_brasil) e {desligamento}(2200_vinculo_desligamento)); N
                    (se grupo {brasil}(2200_trabalhador_endereco_brasil) estiver preenchido); F (nos demais
                    casos)
                """

                brasil: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                exterior: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class TrabImig(CommonMixin):
                """
                :ivar tmpResid: Tempo de residência do trabalhador imigrante. Validação: Preenchimento
                    obrigatório se ({dtAdm}(2200_vinculo_infoRegimeTrab_infoCeletista_dtAdm) ou
                    {dtExercicio}(2200_vinculo_infoRegimeTrab_infoEstatutario_dtExercicio)) &gt;= [2021-07-19].
                :ivar condIng:
                """

                tmpResid: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                condIng: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class InfoDeficiencia(CommonMixin):
                """
                :ivar defFisica:
                :ivar defVisual:
                :ivar defAuditiva:
                :ivar defMental:
                :ivar defIntelectual:
                :ivar reabReadap:
                :ivar infoCota: Informar se o trabalhador deve ser contabilizado no preenchimento de cota de
                    pessoas com deficiência habilitadas ou de beneficiários reabilitados. Validação:
                    Preenchimento obrigatório e exclusivo se {tpRegTrab}(2200_vinculo_tpRegTrab) = [1]. Somente
                    pode ser informado [S] se pelo menos um dos campos a seguir estiver preenchido com [S]:
                    {defFisica}(./defFisica), {defVisual}(./defVisual), {defAuditiva}(./defAuditiva),
                    {defMental}(./defMental), {defIntelectual}(./defIntelectual) e {reabReadap}(./reabReadap).
                    Esta validação não deve ser realizada quando se tratar de evento enviado em versão do
                    leiaute anterior a S-1.0.
                :ivar observacao:
                """

                defFisica: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                defVisual: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                defAuditiva: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                defMental: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                defIntelectual: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                reabReadap: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                infoCota: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                observacao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class Dependente(CommonMixin):
                """
                :ivar tpDep:
                :ivar nmDep:
                :ivar dtNascto:
                :ivar cpfDep:
                :ivar sexoDep: Sexo do dependente. Validação: Preenchimento obrigatório se
                    {tpRegPrev}(2200_vinculo_tpRegPrev) = [2] e {cadIni}(2200_vinculo_cadIni) = [N]. Não
                    informar se {tpRegPrev}(2200_vinculo_tpRegPrev) for diferente de [2].
                :ivar depIRRF:
                :ivar depSF:
                :ivar incTrab: Informar se o dependente tem incapacidade física ou mental para o trabalho.
                    Validação: Não informar se {tpRegPrev}(2200_vinculo_tpRegPrev) = [4]. Preenchimento
                    obrigatório nos demais casos.
                :ivar descrDep:
                """

                tpDep: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                nmDep: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtNascto: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                cpfDep: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                sexoDep: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                depIRRF: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                depSF: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                incTrab: None | str = field(
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
        class Vinculo(CommonMixin):
            """
            :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
                matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: O valor
                informado não pode conter a expressão 'eSocial' nas 7 (sete) primeiras posições.
                REGRA:REGRA_CARACTERE_ESPECIAL
            :ivar tpRegTrab: Tipo de regime trabalhista. Validação: Se
                {codCateg}(2200_vinculo_infoContrato_codCateg) = [104], deve ser preenchido com [1]. Se
                {codCateg}(2200_vinculo_infoContrato_codCateg) = [314], deve ser preenchido com [2].
            :ivar tpRegPrev:
            :ivar cadIni:
            :ivar infoRegimeTrab: Informações do regime trabalhista.
            :ivar infoContrato: Informações do contrato de trabalho.
            :ivar sucessaoVinc: Grupo de informações da sucessão de vínculo trabalhista/estatutário.
                CONDICAO_GRUPO: O (se {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao) = [2,
                3, 4, 7] ou {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) = [5, 8]); N (nos
                demais casos)
            :ivar transfDom: Informações do empregado doméstico transferido de outro representante da mesma
                unidade familiar. CONDICAO_GRUPO: O (se
                {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao) for igual [5]); N (nos demais
                casos)
            :ivar mudancaCPF: Informações de mudança de CPF do trabalhador. CONDICAO_GRUPO: O (se
                {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao) = [6] ou
                {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) = [10]); N (nos demais casos)
            :ivar afastamento: Informações de afastamento do trabalhador DESCRICAO_COMPLETA:Informações de
                afastamento do trabalhador. Preenchimento exclusivo em caso de trabalhador que permaneça
                afastado na data de início da obrigatoriedade dos eventos não periódicos para o empregador no
                eSocial ou na data de transferência ou alteração de CPF do empregado. CONDICAO_GRUPO: N (se
                grupo {desligamento}(2200_vinculo_desligamento) estiver preenchido); OC (nos demais casos)
            :ivar desligamento: Informação do desligamento do trabalhador DESCRICAO_COMPLETA:Informação do
                desligamento do trabalhador. Grupo preenchido exclusivamente caso seja necessário enviar
                cadastramento inicial referente a trabalhador que já tenha sido desligado da empresa antes do
                início dos eventos não periódicos para o empregador no eSocial (por exemplo, envio para
                pagamento de diferenças salariais - acordo/dissídio/convenção coletiva - em meses posteriores ao
                desligamento e sob vigência dos eventos periódicos para o empregador no eSocial) ou no caso de
                desligamento em data anterior à transferência do empregado. CONDICAO_GRUPO: N (se (grupo
                {afastamento}(2200_vinculo_afastamento) ou {cessao}(2200_vinculo_cessao) estiver preenchido) ou
                (se {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao) = [6] ou
                {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) = [10])); OC (nos demais casos)
            :ivar cessao: Informação de cessão/exercício em outro órgão do trabalhador
                DESCRICAO_COMPLETA:Informação de cessão/exercício em outro órgão do trabalhador. Preenchimento
                exclusivo em caso de trabalhador que permaneça cedido/em exercício em outro órgão na data de
                início da obrigatoriedade dos eventos não periódicos para o empregador/ente público no eSocial
                ou na data de transferência ou alteração de CPF do empregado. CONDICAO_GRUPO: N (se grupo
                {desligamento}(2200_vinculo_desligamento) estiver preenchido); OC (nos demais casos)
            """

            matricula: str = field(
                metadata={
                    "type": "Element",
                }
            )
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
            cadIni: VinculoCadIni = field(
                metadata={
                    "type": "Element",
                }
            )
            infoRegimeTrab: ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab = field(
                metadata={
                    "type": "Element",
                }
            )
            infoContrato: ESocial.EvtAdmissao.Vinculo.InfoContrato = field(
                metadata={
                    "type": "Element",
                }
            )
            sucessaoVinc: None | ESocial.EvtAdmissao.Vinculo.SucessaoVinc = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            transfDom: None | ESocial.EvtAdmissao.Vinculo.TransfDom = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            mudancaCPF: None | ESocial.EvtAdmissao.Vinculo.MudancaCpf = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            afastamento: None | ESocial.EvtAdmissao.Vinculo.Afastamento = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            desligamento: None | ESocial.EvtAdmissao.Vinculo.Desligamento = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            cessao: None | ESocial.EvtAdmissao.Vinculo.Cessao = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class InfoRegimeTrab(CommonMixin):
                """
                :ivar infoCeletista: Informações de trabalhador celetista. CONDICAO_GRUPO: O (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [1]); N (nos demais casos)
                :ivar infoEstatutario: Informações de trabalhador estatutário. CONDICAO_GRUPO: O (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [2]); N (nos demais casos)
                """

                infoCeletista: None | ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                infoEstatutario: None | ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoEstatutario = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class InfoCeletista(CommonMixin):
                    """
                    :ivar dtAdm: Preencher com a data de admissão do trabalhador. No caso de transferência do
                        empregado ou de mudança de CPF, preencher com a data inicial do vínculo no primeiro
                        empregador (data de início do vínculo). Validação: Devem ser observadas as seguintes
                        regras: a) Deve ser posterior à data de nascimento do trabalhador e igual ou anterior ao
                        ano do óbito, se existente; b) Se {cadIni}(2200_vinculo_cadIni) = [S], deve ser anterior
                        à data de início da obrigatoriedade dos eventos não periódicos para o empregador no
                        eSocial; c) Se {cadIni}(2200_vinculo_cadIni) = [N] e
                        {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao) = [1], deve ser igual
                        ou posterior à data de início da obrigatoriedade dos eventos não periódicos para o
                        empregador no eSocial.
                    :ivar tpAdmissao:
                    :ivar indAdmissao:
                    :ivar nrProcTrab: Número que identifica o processo trabalhista, quando a admissão se der por
                        decisão judicial. Validação: Informação obrigatória e exclusiva se
                        {indAdmissao}(./indAdmissao) = [3]. Se preenchido, deve ser um processo judicial válido,
                        com 20 (vinte) algarismos.
                    :ivar tpRegJor:
                    :ivar natAtividade:
                    :ivar dtBase:
                    :ivar cnpjSindCategProf:
                    :ivar matAnotJud: Matrícula informada no evento S-2500 (com
                        {indContr}(2500_ideTrab_infoContr_indContr) em S-2500 = [N]) ou S-8200. Validação: Deve
                        corresponder à matrícula cadastrada no evento S-2500 (com
                        {indContr}(2500_ideTrab_infoContr_indContr) em S-2500 = [N]) ou S-8200 para o CPF
                        informado em {cpfTrab}(2200_trabalhador_cpfTrab).
                    :ivar FGTS: Informações do FGTS DESCRICAO_COMPLETA:Informações do Fundo de Garantia do Tempo
                        de Serviço - FGTS. CONDICAO_GRUPO: N (se {tpAdmissao}(../tpAdmissao) = [6] OU (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) for diferente de [104] e
                        {dtAdm}(../dtAdm) &gt;= [1988-10-05]) OU (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) = [104] e {dtAdm}(../dtAdm) &gt;=
                        [2015-10-01])); O (nos demais casos)
                    :ivar trabTemporario: Dados sobre trabalho temporário DESCRICAO_COMPLETA:Dados sobre
                        trabalho temporário. Preenchimento obrigatório no caso de contratação de trabalhador
                        temporário. CONDICAO_GRUPO: N (se {codCateg}(2200_vinculo_infoContrato_codCateg) for
                        diferente de [106]); O (se {codCateg}(2200_vinculo_infoContrato_codCateg) = [106] e se
                        grupo {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais
                        casos)
                    :ivar aprend: Informações relacionadas ao aprendiz. CONDICAO_GRUPO: N (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) for diferente de [103]); O (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) = [103] e se {dtAdm}(../dtAdm) &gt;=
                        [2024-01-22]); OC (se {codCateg}(2200_vinculo_infoContrato_codCateg) = [103], se
                        {dtAdm}(../dtAdm) &lt; [2024-01-22] e se grupo {desligamento}(2200_vinculo_desligamento)
                        não estiver preenchido); F (nos demais casos)
                    """

                    dtAdm: XmlDate = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    tpAdmissao: InfoCeletistaTpAdmissao = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    indAdmissao: InfoCeletistaIndAdmissao = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    nrProcTrab: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    tpRegJor: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    natAtividade: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtBase: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    cnpjSindCategProf: str = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    matAnotJud: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    FGTS: None | ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista.Fgts = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    trabTemporario: None | ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista.TrabTemporario = (
                        field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                    )
                    aprend: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class Fgts(CommonMixin):
                        dtOpcFGTS: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )

                    @dataclass(kw_only=True)
                    class TrabTemporario(CommonMixin):
                        """
                        :ivar hipLeg:
                        :ivar justContr: Descrição do fato determinado que, no caso concreto, justifica a
                            hipótese legal para a contratação de trabalho temporário. O prazo de contratação do
                            trabalho temporário deve ser compatível com o motivo justificador alegado.
                        :ivar ideEstabVinc: Identificação do estabelecimento do tomador ao qual o trabalhador
                            temporário está vinculado
                        :ivar ideTrabSubstituido: Identificação do(s) trabalhador(es) substituído(s).
                            CHAVE_GRUPO: {cpfTrabSubst} CONDICAO_GRUPO: O (se
                            {hipLeg}(2200_vinculo_infoRegimeTrab_infoCeletista_trabTemporario_hipLeg) = [1]); N
                            (nos demais casos)
                        """

                        hipLeg: TrabTemporarioHipLeg = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        justContr: str = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        ideEstabVinc: ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista.TrabTemporario.IdeEstabVinc = field(
                            metadata={
                                "type": "Element",
                            }
                        )
                        ideTrabSubstituido: list[
                            ESocial.EvtAdmissao.Vinculo.InfoRegimeTrab.InfoCeletista.TrabTemporario.IdeTrabSubstituido
                        ] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 9,
                            },
                        )

                        @dataclass(kw_only=True)
                        class IdeEstabVinc(CommonMixin):
                            """
                            :ivar tpInsc:
                            :ivar nrInsc: Informar o número de inscrição do contratante de serviços, de acordo
                                com o tipo de inscrição informado em {ideEstabVinc/tpInsc}(./tpInsc). Validação:
                                Deve ser um identificador válido. Se {dtAdm}(../../dtAdm) &gt;= [2024-04-22] e:
                                a) Se {ideEstabVinc/tpInsc}(./tpInsc) = [1], deve ser informado com 14 (catorze)
                                algarismos. Se o empregador for pessoa jurídica, a raiz do CNPJ informado deve
                                ser diferente de {ideEmpregador/nrInsc}(/ideEmpregador_nrInsc). b) Se
                                {ideEstabVinc/tpInsc}(./tpInsc) = [2], deve ser diferente do CPF do empregado.
                                Se o empregador for pessoa física, também deve ser diferente do CPF do
                                empregador.
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
                        class IdeTrabSubstituido(CommonMixin):
                            """
                            :ivar cpfTrabSubst: CPF do trabalhador substituído. Validação: Deve ser um CPF
                                válido.
                            """

                            cpfTrabSubst: str = field(
                                metadata={
                                    "type": "Element",
                                }
                            )

                @dataclass(kw_only=True)
                class InfoEstatutario(CommonMixin):
                    """
                    :ivar tpProv:
                    :ivar dtExercicio: Data da entrada em exercício pelo servidor. Validação: Devem ser
                        observadas as seguintes regras: a) Deve ser posterior à data de nascimento do
                        trabalhador; b) Se {cadIni}(2200_vinculo_cadIni) = [S], deve ser anterior à data de
                        início da obrigatoriedade dos eventos não periódicos para o empregador/ente público no
                        eSocial; c) Se {cadIni}(2200_vinculo_cadIni) = [N] e
                        {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) for diferente de [5, 8,
                        10], deve ser igual ou posterior à data de início da obrigatoriedade dos eventos não
                        periódicos para o empregador/ente público no eSocial.
                    :ivar tpPlanRP: Tipo de plano de segregação da massa. Validação: Preenchimento obrigatório e
                        exclusivo se {tpRegPrev}(2200_vinculo_tpRegPrev) = [2].
                    :ivar indTetoRGPS: Informar se o servidor está sujeito ao teto do RGPS pela instituição do
                        regime de previdência complementar. Validação: Preenchimento obrigatório e exclusivo se
                        {tpRegPrev}(2200_vinculo_tpRegPrev) = [2].
                    :ivar indAbonoPerm: Indicar se o servidor recebe abono permanência. Validação: Preenchimento
                        obrigatório e exclusivo se {tpRegPrev}(2200_vinculo_tpRegPrev) = [2].
                    :ivar dtIniAbono: Informar a data de inicio do abono permanência. Validação: Preenchimento
                        obrigatório se {indAbonoPerm}(./indAbonoPerm) = [S] e {cadIni}(2200_vinculo_cadIni) =
                        [N]. Não informar se {indAbonoPerm}(./indAbonoPerm) = [N]. Se preenchida, devem ser
                        observadas as seguintes regras: a) Deve ser igual ou posterior à data de exercício do
                        servidor; b) Se {cadIni}(2200_vinculo_cadIni) = [S], deve ser anterior à data de início
                        da obrigatoriedade dos eventos não periódicos para o ente público; c) Se
                        {cadIni}(2200_vinculo_cadIni) = [N], deve ser igual ou anterior à data da transferência
                        ou alteração do CPF do servidor
                        ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf) ou
                        {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF)). Não informar se
                        {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) for diferente de [5, 8,
                        10].
                    """

                    tpProv: InfoEstatutarioTpProv = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    dtExercicio: XmlDate = field(
                        metadata={
                            "type": "Element",
                        }
                    )
                    tpPlanRP: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    indTetoRGPS: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    indAbonoPerm: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    dtIniAbono: None | XmlDate = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

            @dataclass(kw_only=True)
            class InfoContrato(CommonMixin):
                """
                :ivar nmCargo: Informar o nome do cargo. Validação: O preenchimento é obrigatório, exceto se for
                    relativo a servidor nomeado em cargo em comissão ({tpRegTrab}(2200_vinculo_tpRegTrab) = [2]
                    e {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) = [2]).
                :ivar CBOCargo:
                :ivar dtIngrCargo: Data de ingresso do servidor no cargo. Validação: Não preencher se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [1] ou se {tpRegPrev}(2200_vinculo_tpRegPrev) = [4] ou
                    se {CBOCargo}(./CBOCargo) não for informado. Se preenchida, devem ser observadas as
                    seguintes regras: a) Deve ser igual ou posterior à data de exercício do servidor; b) Se
                    {cadIni}(2200_vinculo_cadIni) = [S], deve ser anterior à data de início da obrigatoriedade
                    dos eventos não periódicos para o ente público; c) Se {cadIni}(2200_vinculo_cadIni) = [N],
                    deve ser igual ou anterior à data da transferência ou alteração do CPF do servidor
                    ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf) ou
                    {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF)). Não informar se
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) for diferente de [5, 8, 10].
                :ivar nmFuncao: Informar o nome da função de confiança/cargo em comissão. Validação:
                    Preenchimento obrigatório se for relativo a servidor nomeado em cargo em comissão
                    ({tpRegTrab}(2200_vinculo_tpRegTrab) = [2] e
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) = [2]).
                :ivar CBOFuncao:
                :ivar acumCargo: Informar se o cargo, emprego ou função pública é acumulável. Validação:
                    Preenchimento obrigatório se {cadIni}(2200_vinculo_cadIni) = [N] e se a natureza jurídica do
                    declarante for igual a 1XX-X, 201-1 ou 203-8.
                :ivar codCateg:
                :ivar remuneracao: Informações da remuneração e periodicidade de pagamento. CONDICAO_GRUPO: N
                    (se {tpRegTrab}(2200_vinculo_tpRegTrab) = [2]); O (se {tpRegTrab}(2200_vinculo_tpRegTrab) =
                    [1] e se grupo {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos
                    demais casos)
                :ivar duracao: Duração do contrato de trabalho. CONDICAO_GRUPO: N (se
                    {tpRegTrab}(2200_vinculo_tpRegTrab) = [2]); O (se {tpRegTrab}(2200_vinculo_tpRegTrab) = [1]
                    e se grupo {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais
                    casos)
                :ivar localTrabalho: Informações do local de trabalho. CONDICAO_GRUPO: O (se grupo
                    {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais casos)
                :ivar horContratual: Informações do horário contratual do trabalhador. CONDICAO_GRUPO: O (se
                    {tpRegJor}(2200_vinculo_infoRegimeTrab_infoCeletista_tpRegJor) = [1] e se grupo
                    {desligamento}(2200_vinculo_desligamento) não estiver preenchido); OC (se
                    {tpRegJor}(2200_vinculo_infoRegimeTrab_infoCeletista_tpRegJor) for diferente de [1] e se
                    grupo {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais
                    casos)
                :ivar alvaraJudicial: Dados do alvará judicial DESCRICAO_COMPLETA:Informações do alvará judicial
                    em caso de contratação de menores de 14 anos, em qualquer categoria, e de maiores de 14 e
                    menores de 16, em categoria diferente de "Aprendiz". CONDICAO_GRUPO: OC (se grupo
                    {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais casos)
                :ivar observacoes: Observações do contrato de trabalho. CONDICAO_GRUPO: OC (se grupo
                    {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais casos)
                :ivar treiCap: Treinamentos, capacitações, exercícios simulados e outras anotações
                    DESCRICAO_COMPLETA:Treinamentos, capacitações, exercícios simulados, autorizações ou outras
                    anotações que devam ser anotadas no registro de empregados e/ou na CTPS, por determinação de
                    Norma Regulamentadora - NR. CHAVE_GRUPO: {codTreiCap} CONDICAO_GRUPO: OC (se grupo
                    {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais casos)
                """

                nmCargo: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                CBOCargo: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                dtIngrCargo: None | XmlDate = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                nmFuncao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                CBOFuncao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                acumCargo: None | str = field(
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
                remuneracao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                duracao: None | ESocial.EvtAdmissao.Vinculo.InfoContrato.Duracao = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                localTrabalho: None | ESocial.EvtAdmissao.Vinculo.InfoContrato.LocalTrabalho = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                horContratual: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                alvaraJudicial: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                observacoes: list[ESocial.EvtAdmissao.Vinculo.InfoContrato.Observacoes] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
                treiCap: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )

                @dataclass(kw_only=True)
                class Duracao(CommonMixin):
                    """
                    :ivar tpContr: Tipo de contrato de trabalho. Validação: Se {codCateg}(../codCateg) = [103] e
                        {dtAdm}(2200_vinculo_infoRegimeTrab_infoCeletista_dtAdm) &gt;= [2024-04-22], deve ser
                        informado [2].
                    :ivar dtTerm:
                    :ivar clauAssec: Indicar se o contrato por prazo determinado contém cláusula assecuratória
                        do direito recíproco de rescisão antes da data de seu término. Validação: O
                        preenchimento é obrigatório se {tpContr}(./tpContr) = [2, 3]. Não preencher se
                        {tpContr}(./tpContr) = [1].
                    :ivar objDet:
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
                class LocalTrabalho(CommonMixin):
                    """
                    :ivar localTrabGeral: Estabelecimento onde o trabalhador exercerá suas atividades
                        DESCRICAO_COMPLETA:Estabelecimento (CNPJ, CNO, CAEPF) onde o trabalhador (exceto
                        doméstico) exercerá suas atividades. Caso o trabalhador exerça suas atividades em
                        instalações de terceiros, este campo deve ser preenchido com o estabelecimento do
                        próprio empregador ao qual o trabalhador esteja vinculado. CONDICAO_GRUPO: N (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) = [104]); O (se
                        {codCateg}(2200_vinculo_infoContrato_codCateg) for diferente de [104] e se grupo
                        {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais casos)
                    :ivar localTempDom: Endereço de trabalho do trabalhador doméstico e trabalhador temporário
                        DESCRICAO_COMPLETA:Grupo preenchido exclusivamente em caso de trabalhador doméstico e
                        trabalhador temporário, indicando o endereço onde o trabalhador exerce suas atividades.
                        CONDICAO_GRUPO: N (se {codCateg}(2200_vinculo_infoContrato_codCateg) for diferente de
                        [104, 106]); O (se {codCateg}(2200_vinculo_infoContrato_codCateg) = [104, 106] e se
                        grupo {desligamento}(2200_vinculo_desligamento) não estiver preenchido); F (nos demais
                        casos)
                    """

                    localTrabGeral: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    localTempDom: None | str = field(
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
                :ivar matricAnt: Matrícula do trabalhador no empregador anterior. Validação: O preenchimento é
                    obrigatório se {cadIni}(2200_vinculo_cadIni) = [N]. Se {sucessaoVinc/dtTransf}(./dtTransf)
                    for igual ou posterior a [2024-04-22], a matrícula informada neste campo deve ser idêntica à
                    matricula do trabalhador no empregador anterior.
                :ivar dtTransf: Preencher com a data da transferência do empregado para o empregador declarante.
                    Validação: Devem ser observadas as seguintes regras: a) Deve ser posterior à data de
                    admissão do trabalhador e igual ou anterior ao ano do óbito, se existente; b) Se
                    {cadIni}(2200_vinculo_cadIni) = [S], deve ser anterior à data de início da obrigatoriedade
                    dos eventos não periódicos para o empregador; c) Se {cadIni}(2200_vinculo_cadIni) = [N],
                    deve ser igual ou posterior à data de início da obrigatoriedade dos eventos não periódicos
                    para o empregador.
                :ivar observacao:
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
                observacao: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class TransfDom(CommonMixin):
                """
                :ivar cpfSubstituido: Preencher com o número do CPF do representante anterior da unidade
                    familiar. Validação: Deve ser um CPF válido e diferente do CPF do declarante e do empregado.
                :ivar matricAnt: Matrícula do trabalhador no representante anterior da unidade familiar.
                :ivar dtTransf: Data da transferência do vínculo ao novo representante da unidade familiar.
                """

                cpfSubstituido: str = field(
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
                dtTransf: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class MudancaCpf(CommonMixin):
                """
                :ivar cpfAnt: Preencher com o número do CPF antigo do trabalhador.
                :ivar matricAnt: Preencher com a matrícula anterior do trabalhador.
                :ivar dtAltCPF: Data de alteração do CPF.
                :ivar observacao:
                """

                cpfAnt: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                matricAnt: str = field(
                    metadata={
                        "type": "Element",
                    }
                )
                dtAltCPF: XmlDate = field(
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
            class Afastamento(CommonMixin):
                """
                :ivar dtIniAfast: Data de início do afastamento. Validação: Devem ser observadas as seguintes
                    regras: a) Deve ser igual ou posterior à data de admissão/exercício do trabalhador; b) Se
                    {cadIni}(2200_vinculo_cadIni) = [S], deve ser anterior à data de início da obrigatoriedade
                    dos eventos não periódicos para o empregador; c) Se {cadIni}(2200_vinculo_cadIni) = [N],
                    deve ser anterior à data da transferência ou alteração do CPF do empregado
                    ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf),
                    {transfDom/dtTransf}(2200_vinculo_transfDom_dtTransf) ou
                    {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF)). Não informar se
                    {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao) = [1] ou se
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) for diferente de [5, 8, 10].
                :ivar codMotAfast:
                """

                dtIniAfast: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
                codMotAfast: str = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Desligamento(CommonMixin):
                """
                :ivar dtDeslig: Preencher com a data de desligamento do vínculo (último dia trabalhado).
                    Validação: Devem ser observadas as seguintes regras: a) Deve ser igual ou posterior à data
                    de admissão/exercício do trabalhador; b) Se {cadIni}(2200_vinculo_cadIni) = [S], deve ser
                    anterior à data de início da obrigatoriedade dos eventos não periódicos para o empregador;
                    c) Se {cadIni}(2200_vinculo_cadIni) = [N], deve ser anterior à data da transferência do
                    empregado ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf) ou
                    {transfDom/dtTransf}(2200_vinculo_transfDom_dtTransf)). Não informar se
                    {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao) = [1] ou se
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) for diferente de [5, 8].
                """

                dtDeslig: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass(kw_only=True)
            class Cessao(CommonMixin):
                """
                :ivar dtIniCessao: Data de início da cessão/exercício em outro órgão. Validação: Devem ser
                    observadas as seguintes regras: a) Deve ser igual ou posterior à data de admissão/exercício
                    do trabalhador; b) Se {cadIni}(2200_vinculo_cadIni) = [S], deve ser anterior à data de
                    início da obrigatoriedade dos eventos não periódicos para o ente público e a natureza
                    jurídica do declarante deve ser Administração Pública (grupo [1]); c) Se
                    {cadIni}(2200_vinculo_cadIni) = [N], deve ser anterior à data da transferência ou alteração
                    do CPF do empregado ({sucessaoVinc/dtTransf}(2200_vinculo_sucessaoVinc_dtTransf) ou
                    {dtAltCPF}(2200_vinculo_mudancaCPF_dtAltCPF)) e igual ou posterior a [2021-07-19]. Não
                    informar se {tpAdmissao}(2200_vinculo_infoRegimeTrab_infoCeletista_tpAdmissao) = [1] ou se
                    {tpProv}(2200_vinculo_infoRegimeTrab_infoEstatutario_tpProv) for diferente de [5, 8, 10].
                """

                dtIniCessao: XmlDate = field(
                    metadata={
                        "type": "Element",
                    }
                )
