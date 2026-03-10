from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate

from esociallib.common_mixin import CommonMixin

__NAMESPACE__ = "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00"


class TsIndApurIr(Enum):
    """
    :cvar VALUE_0: Normal (apuração sob a folha de pagamento declarada no eSocial)
    :cvar VALUE_1: Situação especial de apuração de IR
    """

    VALUE_0 = 0
    VALUE_1 = 1


class TsIndApuracao(Enum):
    """
    Indicativo de período de apuração.

    :cvar VALUE_1: Mensal
    :cvar VALUE_2: Anual (13° salário)
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TsIndGuia(Enum):
    """
    Indicativo do tipo de guia.

    :cvar VALUE_1: Documento de Arrecadação do eSocial - DAE
    """

    VALUE_1 = 1


class TsIndMv(Enum):
    """
    Indicador de desconto da contribuição previdenciária do trabalhador.

    :cvar VALUE_1: O declarante aplica a(s) alíquota(s) de desconto do segurado sobre a remuneração por ele
        informada (o percentual da(s) alíquota(s) será(ão) obtido(s) considerando a remuneração total do
        trabalhador)
    :cvar VALUE_2: O declarante aplica a(s) alíquota(s) de desconto do segurado sobre a diferença entre o limite
        máximo do salário de contribuição e a remuneração de outra(s) empresa(s) para as quais o trabalhador
        informou que houve o desconto
    :cvar VALUE_3: O declarante não realiza desconto do segurado, uma vez que houve desconto sobre o limite
        máximo de salário de contribuição em outra(s) empresa(s)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsIndRetif(Enum):
    """
    Informe [1] para arquivo original ou [2] para arquivo de retificação.

    :cvar VALUE_1: Original
    :cvar VALUE_2: Retificação
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TsIndSimples(Enum):
    """
    Indicador de contribuição substituída.

    Validação: O preenchimento do campo é obrigatório apenas no caso das empresas enquadradas no regime de
    tributação Simples Nacional, com tributação previdenciária substituída e não substituída
    ({classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [03]). Para os demais
    empregadores, não deve ser informado.

    :cvar VALUE_1: Contribuição substituída integralmente
    :cvar VALUE_2: Contribuição não substituída
    :cvar VALUE_3: Contribuição não substituída concomitante com contribuição substituída
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsNatAtividade(Enum):
    """
    Natureza da atividade.

    Validação: Se {codCateg}(../../infoContrato_codCateg) = [104], deve ser preenchido com [1]. Se
    {codCateg}(../../infoContrato_codCateg) = [102], deve ser preenchido com [2].

    :cvar VALUE_1: Trabalho urbano
    :cvar VALUE_2: Trabalho rural
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TsProcEmi(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_2: Aplicativo governamental - Simplificado Pessoa Física
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_4: Aplicativo governamental - Simplificado Pessoa Jurídica
    :cvar VALUE_22: Aplicativo governamental para dispositivos móveis - Empregador Doméstico
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_22 = 22


class TsProcEmi8(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_8: Aplicativo governamental para envio de eventos pelo Judiciário
    """

    VALUE_8 = 8


class TsProcEmiPf(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_2: Aplicativo governamental - Simplificado Pessoa Física
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_22: Aplicativo governamental para dispositivos móveis - Empregador Doméstico
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_22 = 22


class TsProcEmiPj(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_4: Aplicativo governamental - Simplificado Pessoa Jurídica
    """

    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_4 = 4


class TsProcEmiPjSemSimplificado(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    """

    VALUE_1 = 1
    VALUE_3 = 3


class TsProcEmiSem8(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_2: Aplicativo governamental - Simplificado Pessoa Física
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_4: Aplicativo governamental - Simplificado Pessoa Jurídica
    :cvar VALUE_9: Aplicativo governamental - Integração com a Junta Comercial
    :cvar VALUE_22: Aplicativo governamental para dispositivos móveis - Empregador Doméstico
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_9 = 9
    VALUE_22 = 22


class TsProcEmiTodos(Enum):
    """
    Processo de emissão do evento.

    :cvar VALUE_1: Aplicativo do empregador
    :cvar VALUE_2: Aplicativo governamental - Simplificado Pessoa Física
    :cvar VALUE_3: Aplicativo governamental - Web Geral
    :cvar VALUE_4: Aplicativo governamental - Simplificado Pessoa Jurídica
    :cvar VALUE_8: Aplicativo governamental para envio de eventos pelo Judiciário
    :cvar VALUE_9: Aplicativo governamental - Integração com a Junta Comercial
    :cvar VALUE_22: Aplicativo governamental para dispositivos móveis - Empregador Doméstico
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_22 = 22


class TsSimNao(Enum):
    """
    :cvar S: Sim
    :cvar N: Não
    """

    S = "S"
    N = "N"


class TsTmpParc(Enum):
    """
    Preencher com o código relativo ao tipo de contrato em tempo parcial.

    Validação: O código [1] só é válido se {codCateg}(../codCateg) = [104]. Os códigos [2, 3] não são válidos se
    {codCateg}(../codCateg) = [104].

    :cvar VALUE_0: Não é contrato em tempo parcial
    :cvar VALUE_1: Limitado a 25 horas semanais
    :cvar VALUE_2: Limitado a 30 horas semanais
    :cvar VALUE_3: Limitado a 26 horas semanais
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsTpAmb(Enum):
    """
    Identificação do ambiente.

    :cvar VALUE_1: Produção
    :cvar VALUE_2: Produção restrita
    :cvar VALUE_7: Validação (uso interno)
    :cvar VALUE_8: Teste (uso interno)
    :cvar VALUE_9: Desenvolvimento (uso interno)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class TsTpContr(Enum):
    """
    Tipo de contrato de trabalho.

    :cvar VALUE_1: Prazo indeterminado
    :cvar VALUE_2: Prazo determinado, definido em dias
    :cvar VALUE_3: Prazo determinado, vinculado à ocorrência de um fato
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TsTpDesc(Enum):
    """
    Indicativo do tipo de desconto.

    :cvar VALUE_1: eConsignado
    """

    VALUE_1 = 1


class TsTpInsc1(Enum):
    """
    Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.

    :cvar VALUE_1: CNPJ
    """

    VALUE_1 = 1


class TsTpInsc12(Enum):
    """
    Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.

    :cvar VALUE_1: CNPJ
    :cvar VALUE_2: CPF
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TsTpInsc134(Enum):
    """
    Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.

    :cvar VALUE_1: CNPJ
    :cvar VALUE_3: CAEPF
    :cvar VALUE_4: CNO
    """

    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_4 = 4


class TsTpProc12(Enum):
    """
    Preencher com o código correspondente ao tipo de processo.

    :cvar VALUE_1: Administrativo
    :cvar VALUE_2: Judicial
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TsTpTrib(Enum):
    """
    Abrangência da decisão.

    :cvar VALUE_1: IRRF
    :cvar VALUE_2: Contribuições sociais do trabalhador
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TsUf(Enum):
    AC = "AC"
    AL = "AL"
    AP = "AP"
    AM = "AM"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MT = "MT"
    MS = "MS"
    MG = "MG"
    PA = "PA"
    PB = "PB"
    PR = "PR"
    PE = "PE"
    PI = "PI"
    RJ = "RJ"
    RN = "RN"
    RS = "RS"
    RO = "RO"
    RR = "RR"
    SC = "SC"
    SP = "SP"
    SE = "SE"
    TO = "TO"


class TsUndSalFixo(Enum):
    """
    Unidade de pagamento da parte fixa da remuneração.

    :cvar VALUE_1: Por hora
    :cvar VALUE_2: Por dia
    :cvar VALUE_3: Por semana
    :cvar VALUE_4: Por quinzena
    :cvar VALUE_5: Por mês
    :cvar VALUE_6: Por tarefa
    :cvar VALUE_7: Não aplicável - Salário exclusivamente variável
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


@dataclass(kw_only=True)
class TAlvaraJudicial(CommonMixin):
    """
    :ivar nrProcJud: Preencher com o número do processo judicial. Validação: Deve ser um número de processo
        judicial válido.
    """

    class Meta:
        name = "T_alvaraJudicial"

    nrProcJud: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 20,
        }
    )


class TAprendIndAprend(Enum):
    """
    Indicativo de modalidade de contratação de aprendiz.

    :cvar VALUE_1: Contratação direta: contratação do aprendiz efetivada pelo estabelecimento cumpridor da cota
        de aprendizagem
    :cvar VALUE_2: Contratação indireta: contratação do aprendiz efetivada por entidades sem fins lucrativos ou
        por entidades de prática desportiva a serviço do estabelecimento cumpridor da cota
    """

    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class TContato(CommonMixin):
    class Meta:
        name = "T_contato"

    fonePrinc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 8,
            "max_length": 13,
            "pattern": r".*[^\s].*",
        },
    )
    emailPrinc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 6,
            "max_length": 60,
            "pattern": r".*[^\s].*",
        },
    )


@dataclass(kw_only=True)
class TEnderecoExterior(CommonMixin):
    """
    Endereço no exterior.

    CONDICAO_GRUPO: O (se não informado o grupo {brasil}(../brasil)); N (nos demais casos).

    :ivar paisResid: Preencher com o código do país. Validação: Deve ser um código válido e existente na Tabela
        06.
    :ivar dscLograd:
    :ivar nrLograd:
    :ivar complemento:
    :ivar bairro:
    :ivar nmCid:
    :ivar codPostal:
    """

    class Meta:
        name = "T_endereco_exterior"

    paisResid: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{3}",
        }
    )
    dscLograd: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrLograd: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 10,
            "pattern": r".*[^\s].*",
        }
    )
    complemento: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        },
    )
    bairro: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        },
    )
    nmCid: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 2,
            "max_length": 50,
            "pattern": r".*[^\s].*",
        }
    )
    codPostal: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 4,
            "max_length": 12,
            "pattern": r".*[^\s].*",
        },
    )


class THorContratualTpJornada(Enum):
    """
    Tipo de jornada.

    :cvar VALUE_2: Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)
    :cvar VALUE_3: Jornada com horário diário fixo e folga variável
    :cvar VALUE_4: Jornada com horário diário fixo e folga fixa (no domingo)
    :cvar VALUE_5: Jornada com horário diário fixo e folga fixa (exceto no domingo)
    :cvar VALUE_6: Jornada com horário diário fixo e folga fixa (em outro dia da semana), com folga adicional
        periódica no domingo
    :cvar VALUE_7: Turno ininterrupto de revezamento
    :cvar VALUE_9: Demais tipos de jornada
    """

    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_9 = 9


@dataclass(kw_only=True)
class TIdeBeneficio(CommonMixin):
    """
    Identificação do beneficiário e do benefício.

    CHAVE_GRUPO: {cpfBenef*}, {nrBeneficio*}.

    :ivar cpfBenef: Informar o CPF do beneficiário.
    :ivar nrBeneficio: Número do benefício.
    """

    class Meta:
        name = "T_ideBeneficio"

    cpfBenef: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}",
        }
    )
    nrBeneficio: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoRetornoMensal(CommonMixin):
    """
    Identificação do evento de retorno.

    Evento de origem: S-1299. CHAVE_GRUPO: {perApur*}.

    :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência das informações.
    """

    class Meta:
        name = "T_ideEvento_retorno_mensal"

    perApur: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 7,
            "pattern": r"([2]\d{3}|19[6-9]\d)-(1[0-2]|0[1-9])",
        }
    )


@dataclass(kw_only=True)
class TIdeTrabSemVinculo(CommonMixin):
    """
    Identificação do TSVE DESCRICAO_COMPLETA:Identificação do Trabalhador Sem Vínculo de Emprego/Estatutário -
    TSVE.

    CHAVE_GRUPO: {cpfTrab*}, {matricula*}, {codCateg*}.

    :ivar cpfTrab:
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa. Validação: Deve corresponder à matrícula
        informada pelo empregador no evento S-2300 do respectivo contrato. Não preencher no caso de TSVE sem
        informação de matrícula no evento S-2300.
    :ivar codCateg: Preencher com o código da categoria do trabalhador. Informar somente no caso de TSVE sem
        informação de matrícula no evento S-2300. Validação: Informação obrigatória e exclusiva se não houver
        preenchimento de {matricula}(./matricula). Se informado, deve ser um código válido e existente na Tabela
        01.
    """

    class Meta:
        name = "T_ideTrabSemVinculo"

    cpfTrab: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}",
        }
    )
    matricula: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        },
    )
    codCateg: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{3}",
        },
    )


@dataclass(kw_only=True)
class TIdeVinculo(CommonMixin):
    """
    Informações de identificação do trabalhador e do vínculo.

    CHAVE_GRUPO: {cpfTrab*}, {matricula*}.

    :ivar cpfTrab:
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
        matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve
        corresponder à matrícula informada pelo empregador no evento S-2200 do respectivo vínculo trabalhista.
    """

    class Meta:
        name = "T_ideVinculo"

    cpfTrab: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}",
        }
    )
    matricula: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
        }
    )


@dataclass(kw_only=True)
class TIdeVinculoBaixa(CommonMixin):
    """
    Informações de identificação do trabalhador e do vínculo.

    CHAVE_GRUPO: {cpfTrab*}, {matricula*}.

    :ivar cpfTrab:
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
        matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve
        corresponder à matrícula informada pelo empregador no evento S-2190 ou S-2200 do respectivo vínculo
        trabalhista.
    """

    class Meta:
        name = "T_ideVinculo_baixa"

    cpfTrab: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}",
        }
    )
    matricula: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
        }
    )


@dataclass(kw_only=True)
class TIdeVinculoSst(CommonMixin):
    """
    Informações de identificação do trabalhador e do vínculo.

    CHAVE_GRUPO: {cpfTrab*}, {matricula*}, {codCateg*}.

    :ivar cpfTrab:
    :ivar matricula: Matrícula atribuída ao trabalhador pela empresa ou, no caso de servidor público, a
        matrícula constante no Sistema de Administração de Recursos Humanos do órgão. Validação: Deve
        corresponder à matrícula informada pelo empregador no evento S-2190, S-2200 ou S-2300 do respectivo
        contrato. Não preencher no caso de Trabalhador Sem Vínculo de Emprego/Estatutário - TSVE sem informação
        de matrícula no evento S-2300.
    :ivar codCateg: Preencher com o código da categoria do trabalhador. Informar somente no caso de TSVE sem
        informação de matrícula no evento S-2300. Validação: Informação obrigatória e exclusiva se não houver
        preenchimento de {matricula}(./matricula). Se informado, deve ser um código válido e existente na Tabela
        01.
    """

    class Meta:
        name = "T_ideVinculo_sst"

    cpfTrab: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}",
        }
    )
    matricula: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
        },
    )
    codCateg: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{3}",
        },
    )


class TInfoEstagiarioNatEstagio(Enum):
    """
    Natureza do estágio ou da prestação de serviço civil voluntário.

    Validação: Se o código de categoria for igual a [906], deve ser preenchido com [N].

    :cvar O: Obrigatório
    :cvar N: Não obrigatório
    """

    O = "O"
    N = "N"


class TInfoEstagiarioNivEstagio(Enum):
    """
    Informar o nível do estágio ou da prestação de serviço civil voluntário.

    Validação: Preenchimento obrigatório se o código de categoria for igual a [901]. Se o código de categoria for
    igual a [906], não pode ser informado [9].

    :cvar VALUE_1: Fundamental
    :cvar VALUE_2: Médio
    :cvar VALUE_3: Formação profissional
    :cvar VALUE_4: Superior
    :cvar VALUE_8: Especial
    :cvar VALUE_9: Mãe social (Lei 7.644/1987)
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_9 = 9


@dataclass(kw_only=True)
class TInfoInterm(CommonMixin):
    """
    :ivar dia:
    :ivar hrsTrab: Horas trabalhadas no dia pelo empregado com contrato de trabalho intermitente, no formato
        HHMM. Validação: Preenchimento obrigatório e exclusivo se
        {}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22]. Se preenchida, deve estar no
        intervalo entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos,
        que deve ser menor ou igual a 59.
    """

    class Meta:
        name = "T_infoInterm"

    dia: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_inclusive": "0",
            "max_inclusive": "31",
            "pattern": r"\d{1,2}",
        }
    )
    hrsTrab: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 4,
            "pattern": r"(([0-1][0-9]|2[0-3])[0-5][0-9])",
        },
    )


@dataclass(kw_only=True)
class TInfoIntermProcTrab(CommonMixin):
    """
    :ivar dia:
    :ivar hrsTrab: Horas trabalhadas no dia pelo empregado com contrato de trabalho intermitente, no formato
        HHMM. Validação: Preenchimento obrigatório e exclusivo se
        {}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [22] em
        {}(2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_perRef). Se preenchida, deve estar no intervalo
        entre [0000] e [2359], criticando inclusive a segunda parte do número, que indica os minutos, que deve
        ser menor ou igual a 59.
    """

    class Meta:
        name = "T_infoIntermProcTrab"

    dia: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_inclusive": "0",
            "max_inclusive": "31",
            "pattern": r"\d{1,2}",
        }
    )
    hrsTrab: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 4,
            "pattern": r"(([0-1][0-9]|2[0-3])[0-5][0-9])",
        },
    )


@dataclass(kw_only=True)
class TNascimento(CommonMixin):
    """
    Grupo de informações do nascimento do trabalhador.

    :ivar dtNascto: Preencher com a data de nascimento.
    :ivar paisNascto: Preencher com o código do país de nascimento do trabalhador. Validação: Deve ser um código
        válido e existente na Tabela 06.
    :ivar paisNac:
    """

    class Meta:
        name = "T_nascimento"

    dtNascto: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    paisNascto: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{3}",
        }
    )
    paisNac: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{3}",
        }
    )


@dataclass(kw_only=True)
class TNovaValidade(CommonMixin):
    """
    Novo período de validade das informações.

    DESCRICAO_COMPLETA:Informação preenchida exclusivamente em caso de alteração do período de validade das
    informações, apresentando o novo período de validade. CONDICAO_GRUPO: OC.
    """

    class Meta:
        name = "T_novaValidade"

    iniValid: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 7,
            "pattern": r"([2]\d{3}|19[6-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    fimValid: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 7,
            "pattern": r"([2]\d{3}|19[6-9]\d)-(1[0-2]|0[1-9])",
        },
    )


@dataclass(kw_only=True)
class TTreiCap(CommonMixin):
    class Meta:
        name = "T_treiCap"

    codTreiCap: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{4}",
        }
    )


@dataclass(kw_only=True)
class TAprend(CommonMixin):
    """
    :ivar indAprend:
    :ivar cnpjEntQual: Informar o número de inscrição no CNPJ da entidade qualificadora, no caso de contratação
        direta. Validação: Preenchimento obrigatório e exclusivo se {indAprend}(./indAprend) = [1]. Deve ser um
        CNPJ válido, com 14 (catorze) algarismos.
    :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição do estabelecimento para o qual a
        contratação de aprendiz foi efetivada, no caso de contratação indireta, conforme Tabela 05. Validação:
        Preenchimento obrigatório e exclusivo se {indAprend}(./indAprend) = [2].
    :ivar nrInsc: Informar o número de inscrição do estabelecimento para o qual a contratação de aprendiz foi
        efetivada, no caso de contratação indireta, de acordo com o tipo de inscrição indicado no campo
        {aprend/tpInsc}(./tpInsc). Validação: Preenchimento obrigatório e exclusivo se {indAprend}(./indAprend)
        = [2]. Deve ser um identificador válido e: a) Se {aprend/tpInsc}(./tpInsc) = [1], deve ser informado com
        14 (catorze) algarismos. Se o empregador for pessoa jurídica, a raiz do CNPJ informado deve ser
        diferente de {ideEmpregador/nrInsc}(/ideEmpregador_nrInsc). b) Se {aprend/tpInsc}(./tpInsc) = [2], deve
        ser diferente do CPF do empregado. Se o empregador for pessoa física, também deve ser diferente do CPF
        do empregador.
    :ivar cnpjPrat: Informar o número de inscrição no CNPJ do estabelecimento onde estão sendo realizadas as
        atividades práticas, quando ocorrer uma das seguintes situações: a) Modalidade alternativa de
        cumprimento de cota de aprendizagem (neste caso, informar o CNPJ da entidade concedente da parte
        prática); b) Realização das atividades práticas na empresa contratante do serviço terceirizado; c)
        Centralização das atividades práticas em estabelecimento da própria empresa, diverso do estabelecimento
        responsável pelo cumprimento da cota. Validação: Deve ser um CNPJ válido, com 14 (catorze) algarismos.
    """

    class Meta:
        name = "T_aprend"

    indAprend: TAprendIndAprend = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    cnpjEntQual: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{14}",
        },
    )
    tpInsc: None | TsTpInsc12 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    nrInsc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}|\d{14}",
        },
    )
    cnpjPrat: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{14}",
        },
    )


@dataclass(kw_only=True)
class TDescFolha(CommonMixin):
    """
    Informações de desconto do empréstimo em folha.

    CONDICAO_GRUPO: O (se {}(1010_infoRubrica_inclusao_dadosRubrica_natRubr) em S-1010 = [9253]); N (nos demais
    casos).

    :ivar tpDesc:
    :ivar instFinanc:
    :ivar nrDoc:
    :ivar observacao: Outras informações do desconto.
    """

    class Meta:
        name = "T_descFolha"

    tpDesc: TsTpDesc = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    instFinanc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{3}",
        }
    )
    nrDoc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 2,
            "max_length": 15,
            "pattern": r"[A-Za-z0-9][-_A-Za-z0-9/.//]{0,13}[A-Za-z0-9]",
        }
    )
    observacao: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 255,
            "pattern": r"[^\s]{1}[\S\s]*",
        },
    )


@dataclass(kw_only=True)
class TDetReemb(CommonMixin):
    """
    :ivar tpInsc: Informar o código correspondente ao tipo de inscrição do prestador de serviços.
    :ivar nrInsc: Informar o número de inscrição do prestador de serviços de assistência médica, de acordo com o
        tipo de inscrição indicado em {tpInsc}(./tpInsc). Validação: Deve ser um CNPJ ou CPF válido, de acordo
        com o tipo de inscrição indicado em {tpInsc}(./tpInsc). Não pode ser igual a {}(1210_ideBenef_cpfBenef).
    :ivar vlrReemb: Valor do reembolso relativo ao ano do período indicado em {perApur}(1210_ideEvento_perApur).
        Validação: Informação não obrigatória se {vlrReembAnt}(./vlrReembAnt) for maior que zero.
    :ivar vlrReembAnt: Valor do reembolso relativo a anos anteriores. Validação: Informação não obrigatória se
        {vlrReemb}(./vlrReemb) for maior que zero.
    """

    class Meta:
        name = "T_detReemb"

    tpInsc: TsTpInsc12 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}|\d{14}",
        }
    )
    vlrReemb: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.99"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    vlrReembAnt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.99"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )


@dataclass(kw_only=True)
class TDetReembTot(CommonMixin):
    """
    :ivar tpInsc: Informar o código correspondente ao tipo de inscrição do prestador de serviços.
    :ivar nrInsc: Informar o número de inscrição do prestador de serviços de assistência médica, de acordo com o
        tipo de inscrição indicado em {tpInsc}(./tpInsc).
    :ivar vlrReemb: Valor do reembolso relativo ao ano do período indicado em {perApur}(1210_ideEvento_perApur).
    :ivar vlrReembAnt: Valor do reembolso relativo a anos anteriores.
    """

    class Meta:
        name = "T_detReemb_Tot"

    tpInsc: TsTpInsc12 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}|\d{14}",
        }
    )
    vlrReemb: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.99"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )
    vlrReembAnt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.99"),
            "total_digits": 14,
            "fraction_digits": 2,
        },
    )


@dataclass(kw_only=True)
class TEnderecoBrasil(CommonMixin):
    """
    Endereço no Brasil.

    CONDICAO_GRUPO: O (se não informado o grupo {exterior}(../exterior)); N (nos demais casos).

    :ivar tpLograd:
    :ivar dscLograd:
    :ivar nrLograd:
    :ivar complemento:
    :ivar bairro:
    :ivar cep:
    :ivar codMunic:
    :ivar uf: Preencher com a sigla da Unidade da Federação - UF.
    """

    class Meta:
        name = "T_endereco_brasil"

    tpLograd: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 4,
        },
    )
    dscLograd: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )
    nrLograd: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 10,
            "pattern": r".*[^\s].*",
        }
    )
    complemento: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        },
    )
    bairro: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 90,
            "pattern": r".*[^\s].*",
        },
    )
    cep: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{8}",
        }
    )
    codMunic: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{7}",
        }
    )
    uf: TsUf = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )


@dataclass(kw_only=True)
class THorContratual(CommonMixin):
    """
    :ivar qtdHrsSem:
    :ivar tpJornada:
    :ivar tmpParc:
    :ivar horNoturno: Indicar se a jornada semanal possui horário noturno (no todo ou em parte). Validação:
        Informação obrigatória se {codCateg}(../codCateg) for diferente de [111].
    :ivar dscJorn: Descrição da jornada semanal contratual, contendo os dias da semana e os respectivos horários
        contratuais (entrada, saída e intervalos).
    """

    class Meta:
        name = "T_horContratual"

    qtdHrsSem: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        },
    )
    tpJornada: THorContratualTpJornada = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    tmpParc: TsTmpParc = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    horNoturno: None | TsSimNao = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    dscJorn: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 999,
            "pattern": r"[^\s]{1}[\S\s]*",
        }
    )


@dataclass(kw_only=True)
class TIdeEmpregador(CommonMixin):
    """
    Informações de identificação do empregador.

    CHAVE_GRUPO: {tpInsc*}, {nrInsc*}.

    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no
        campo {ideEmpregador/tpInsc}(./tpInsc) e conforme informado em S-1000.
    """

    class Meta:
        name = "T_ideEmpregador"

    tpInsc: TsTpInsc12 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{8}|\d{11}|\d{14}",
        }
    )


@dataclass(kw_only=True)
class TIdeEmpregadorCnpj(CommonMixin):
    """
    Informações de identificação do empregador.

    CHAVE_GRUPO: {tpInsc*}, {nrInsc*}.
    """

    class Meta:
        name = "T_ideEmpregador_cnpj"

    tpInsc: TsTpInsc1 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{8}|\d{14}",
        }
    )


@dataclass(kw_only=True)
class TIdeEmpregadorExclusao(CommonMixin):
    """
    Informações de identificação do empregador.

    CHAVE_GRUPO: {tpInsc}, {nrInsc}.

    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no
        campo {ideEmpregador/tpInsc}(./tpInsc) e conforme informado em S-1000.
    """

    class Meta:
        name = "T_ideEmpregador_exclusao"

    tpInsc: TsTpInsc12 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{8}|\d{11}|\d{14}",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoEvtTab(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_evtTab"

    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoEvtTabInicial(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_evtTab_inicial"

    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmiSem8 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoExclusao(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_exclusao"

    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmiTodos = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoExclusaoProcTrab(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_exclusao_proc_trab"

    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoFolha(CommonMixin):
    """
    Informações de identificação do evento.

    CHAVE_GRUPO: {indApuracao*}, {perApur*}, {indGuia*}.
    """

    class Meta:
        name = "T_ideEvento_folha"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    indApuracao: TsIndApuracao = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    perApur: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )
    indGuia: None | TsIndGuia = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoFolhaMensal(CommonMixin):
    """
    Informações de identificação do evento.

    CHAVE_GRUPO: {perApur*}, {indGuia*}.
    """

    class Meta:
        name = "T_ideEvento_folha_mensal"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    perApur: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 7,
            "pattern": r"([2]\d{3}|19[6-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: None | TsIndGuia = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoFolhaMensalPf(CommonMixin):
    """
    Informações de identificação do evento.

    CHAVE_GRUPO: {perApur*}, {indGuia*}.
    """

    class Meta:
        name = "T_ideEvento_folha_mensal_PF"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    perApur: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 7,
            "pattern": r"([2]\d{3}|19[6-9]\d)-(1[0-2]|0[1-9])",
        }
    )
    indGuia: None | TsIndGuia = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmiPf = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoFolhaOpp(CommonMixin):
    """
    Informações de identificação do evento.

    CHAVE_GRUPO: {indApuracao*}, {perApur*}.
    """

    class Meta:
        name = "T_ideEvento_folha_opp"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    indApuracao: TsIndApuracao = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    perApur: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmiPj = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoFolhaSemRetificacao(CommonMixin):
    """
    Informações de identificação do evento.

    CHAVE_GRUPO: {indApuracao*}, {perApur*}, {indGuia*}.
    """

    class Meta:
        name = "T_ideEvento_folha_sem_retificacao"

    indApuracao: TsIndApuracao = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    perApur: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )
    indGuia: None | TsIndGuia = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoRetornoContrib(CommonMixin):
    """
    Identificação do evento de retorno.

    Evento de origem: S-1299. CHAVE_GRUPO: {indApuracao*}, {perApur*}.

    :ivar indApuracao:
    :ivar perApur: Informar o mês/ano (formato AAAA-MM) de referência das informações, se
        {indApuracao}(./indApuracao) for igual a [1], ou apenas o ano (formato AAAA), se
        {indApuracao}(./indApuracao) for igual a [2].
    """

    class Meta:
        name = "T_ideEvento_retorno_contrib"

    indApuracao: TsIndApuracao = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    perApur: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 4,
            "max_length": 7,
            "pattern": r"[2]{1}\d{3}-(1[0-2]|0[1-9])|[2]{1}\d{3}",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoTrab(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_trab"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoTrabPj(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_trab_PJ"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmiPj = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoTrabPjSemSimplificado(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_trab_PJ_sem_simplificado"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmiPjSemSimplificado = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoTrabAdmissao(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_trab_admissao"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmiSem8 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoTrabIndGuia(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_trab_indGuia"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    indGuia: None | TsIndGuia = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TIdeEventoTrabJud(CommonMixin):
    """
    Informações de identificação do evento.
    """

    class Meta:
        name = "T_ideEvento_trab_jud"

    indRetif: TsIndRetif = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrRecibo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 23,
            "pattern": r"[1]{1}\.\d{1}\.\d{19}",
        },
    )
    tpAmb: TsTpAmb = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    procEmi: TsProcEmi8 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    verProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 20,
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TInfoEstagiario(CommonMixin):
    """
    :ivar natEstagio:
    :ivar nivEstagio:
    :ivar areaAtuacao: Área de atuação do estagiário ou, no caso de prestação de serviço civil voluntário,
        jornada semanal do desempenho de atividades em formato decimal.
    :ivar nrApol: Número da apólice de seguro.
    :ivar dtPrevTerm: Data prevista para o término do estágio ou da prestação de serviço civil voluntário.
        Validação: Deve ser uma data posterior à data de início do estágio ou da prestação de serviço civil
        voluntário.
    :ivar instEnsino: Instituição de ensino ou entidade de formação/qualificação.
    :ivar ageIntegracao: Agente de integração. CONDICAO_GRUPO: OC (se o código de categoria for igual a [901]);
        N (nos demais casos)
    :ivar supervisorEstagio: Supervisor do estágio. CONDICAO_GRUPO: OC (se o código de categoria for igual a
        [901]); N (nos demais casos)
    """

    class Meta:
        name = "T_infoEstagiario"

    natEstagio: TInfoEstagiarioNatEstagio = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nivEstagio: None | TInfoEstagiarioNivEstagio = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    areaAtuacao: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 100,
            "pattern": r"[^\s]{1}[\S\s]*",
        },
    )
    nrApol: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        },
    )
    dtPrevTerm: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    instEnsino: TInfoEstagiario.InstEnsino = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    ageIntegracao: None | TInfoEstagiario.AgeIntegracao = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    supervisorEstagio: None | TInfoEstagiario.SupervisorEstagio = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )

    @dataclass(kw_only=True)
    class InstEnsino(CommonMixin):
        """
        :ivar cnpjInstEnsino: Preencher com o CNPJ da instituição de ensino, no caso de estágio, ou da entidade
            de formação/qualificação, no caso de prestação de serviço civil voluntário. Deve ser preenchido
            apenas se a instituição/entidade for brasileira. Validação: Se informado, deve ser um CNPJ válido,
            com 14 (catorze) algarismos.
        :ivar nmRazao: Informar a razão social. Validação: Preenchimento obrigatório e exclusivo se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) não estiver preenchido.
        :ivar dscLograd: Descrição do logradouro. Validação: Preenchimento obrigatório e exclusivo se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) não estiver preenchido.
        :ivar nrLograd: Número do logradouro. Se não houver número a ser informado, preencher com "S/N".
            Validação: Preenchimento obrigatório e exclusivo se o campo {cnpjInstEnsino}(./cnpjInstEnsino) não
            estiver preenchido.
        :ivar bairro: Nome do bairro/distrito. Validação: Preenchimento obrigatório e exclusivo se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) não estiver preenchido.
        :ivar cep: Código de Endereçamento Postal - CEP. Validação: Não informar se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) estiver preenchido. Se informado, deve ser preenchido apenas com
            números, com 8 (oito) posições.
        :ivar codMunic: Preencher com o código do município, conforme tabela do IBGE. Validação: Não informar se
            o campo {cnpjInstEnsino}(./cnpjInstEnsino) estiver preenchido. Se informado, deve ser um código
            válido e existente na tabela do IBGE.
        :ivar uf: Preencher com a sigla da Unidade da Federação - UF. Validação: Não informar se o campo
            {cnpjInstEnsino}(./cnpjInstEnsino) estiver preenchido.
        """

        cnpjInstEnsino: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "pattern": r"\d{14}",
            },
        )
        nmRazao: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            },
        )
        dscLograd: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^\s]{1}[\S\s]*",
            },
        )
        nrLograd: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "min_length": 1,
                "max_length": 10,
                "pattern": r".*[^\s].*",
            },
        )
        bairro: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "min_length": 1,
                "max_length": 90,
                "pattern": r".*[^\s].*",
            },
        )
        cep: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "pattern": r"\d{8}",
            },
        )
        codMunic: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "pattern": r"\d{7}",
            },
        )
        uf: None | TsUf = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            },
        )

    @dataclass(kw_only=True)
    class AgeIntegracao(CommonMixin):
        """
        :ivar cnpjAgntInteg: CNPJ do agente de integração. Validação: Deve ser um CNPJ válido, com 14 (catorze)
            algarismos.
        """

        cnpjAgntInteg: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "pattern": r"\d{14}",
            }
        )

    @dataclass(kw_only=True)
    class SupervisorEstagio(CommonMixin):
        """
        :ivar cpfSupervisor: CPF do responsável pela supervisão do estagiário. Validação: Deve ser um CPF
            válido.
        """

        cpfSupervisor: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "pattern": r"\d{11}",
            }
        )


@dataclass(kw_only=True)
class TInfoMv(CommonMixin):
    """
    Informação de múltiplos vínculos DESCRICAO_COMPLETA:Grupo preenchido exclusivamente em caso de trabalhador que
    possua outros vínculos/atividades nos quais já tenha ocorrido desconto de contribuição previdenciária.

    CONDICAO_GRUPO: OC.

    :ivar indMV:
    :ivar remunOutrEmpr: Remuneração recebida pelo trabalhador em outras empresas ou atividades
        DESCRICAO_COMPLETA:Informações relativas ao trabalhador que possui vínculo empregatício com outra(s)
        empresa(s) e/ou que exerce outras atividades como contribuinte individual, detalhando as empresas que
        efetuaram (ou efetuarão) desconto da contribuição. CHAVE_GRUPO: {tpInsc}, {nrInsc}, {codCateg}
    """

    class Meta:
        name = "T_infoMV"

    indMV: TsIndMv = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    remunOutrEmpr: list[TInfoMv.RemunOutrEmpr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )

    @dataclass(kw_only=True)
    class RemunOutrEmpr(CommonMixin):
        """
        :ivar tpInsc:
        :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado
            no campo {remunOutrEmpr/tpInsc}(./tpInsc). Validação: a) Se {remunOutrEmpr/tpInsc}(./tpInsc) = [1],
            deve ser um CNPJ válido, diferente do CNPJ base indicado no evento de Informações do Empregador
            (S-1000) e dos estabelecimentos informados através do evento S-1005. b) Se
            {remunOutrEmpr/tpInsc}(./tpInsc) = [2], deve ser um CPF válido e diferente do CPF do trabalhador e
            ainda, caso o empregador seja pessoa física, diferente do CPF do empregador.
        :ivar codCateg:
        :ivar vlrRemunOE:
        """

        tpInsc: TsTpInsc12 = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            }
        )
        nrInsc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "pattern": r"\d{11}|\d{14}",
            }
        )
        codCateg: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "pattern": r"\d{3}",
            }
        )
        vlrRemunOE: Decimal = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "min_exclusive": Decimal("0"),
                "max_inclusive": Decimal("999999999999.99"),
                "total_digits": 14,
                "fraction_digits": 2,
            }
        )


@dataclass(kw_only=True)
class TInfoRra(CommonMixin):
    """
    Informações complementares de RRA.

    DESCRICAO_COMPLETA:Informações complementares relativas a Rendimentos Recebidos Acumuladamente - RRA.
    CONDICAO_GRUPO: O (se {indRRA}(../indRRA) = [S]); N (nos demais casos).

    :ivar tpProcRRA:
    :ivar nrProcRRA: Informar o número do processo/requerimento administrativo/judicial. Validação: Informação
        obrigatória se {tpProcRRA}(./tpProcRRA) = [2] e opcional se {tpProcRRA}(./tpProcRRA) = [1]. Deve ser
        número de processo válido e: a) Se {tpProcRRA}(./tpProcRRA) = [1], deve possuir 17 (dezessete) ou 21
        (vinte e um) algarismos; b) Se {tpProcRRA}(./tpProcRRA) = [2], deve possuir 20 (vinte) algarismos.
    :ivar descRRA:
    :ivar qtdMesesRRA:
    :ivar despProcJud:
    :ivar ideAdv: Identificação dos advogados. CHAVE_GRUPO: {tpInsc}, {nrInsc} CONDICAO_GRUPO: OC (se
        {vlrDespAdvogados}(../despProcJud_vlrDespAdvogados) &gt; 0); N (nos demais casos)
    """

    class Meta:
        name = "T_infoRRA"

    tpProcRRA: TsTpProc12 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrProcRRA: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{17}|\d{20}|\d{21}",
        },
    )
    descRRA: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 50,
            "pattern": r".*[^\s].*",
        }
    )
    qtdMesesRRA: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("999.9"),
            "total_digits": 4,
            "fraction_digits": 1,
        }
    )
    despProcJud: None | TInfoRra.DespProcJud = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        },
    )
    ideAdv: list[TInfoRra.IdeAdv] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "max_occurs": 99,
        },
    )

    @dataclass(kw_only=True)
    class DespProcJud(CommonMixin):
        """
        Despesas com processo judicial DESCRICAO_COMPLETA:Detalhamento das despesas com processo judicial.

        CONDICAO_GRUPO: OC.

        :ivar vlrDespCustas: Preencher com o valor das despesas com custas judiciais. Validação: Deve ser maior
            ou igual a 0 (zero).
        :ivar vlrDespAdvogados: Preencher com o valor total das despesas com advogado(s). Validação: Se o grupo
            {}(../ideAdv) for preenchido, o valor informado neste campo deve ser maior ou igual à soma do(s)
            campo(s) {}(../ideAdv_vlrAdv) do grupo {}(../ideAdv). Deve ser maior ou igual a 0 (zero). O não
            preenchimento do grupo {}(../ideAdv) indica que o contribuinte declarante não possui as informações
            detalhadas por advogado.
        """

        vlrDespCustas: Decimal = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("999999999999.99"),
                "total_digits": 14,
                "fraction_digits": 2,
            }
        )
        vlrDespAdvogados: Decimal = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("999999999999.99"),
                "total_digits": 14,
                "fraction_digits": 2,
            }
        )

    @dataclass(kw_only=True)
    class IdeAdv(CommonMixin):
        """
        :ivar tpInsc: Preencher com o código correspondente ao tipo de inscrição, conforme Tabela 05.
        :ivar nrInsc: Informar o número de inscrição do advogado. Validação: Deve ser um número de inscrição
            válido, de acordo com o tipo de inscrição indicado no campo {ideAdv/tpInsc}(./tpInsc), considerando
            as particularidades aplicadas à informação de CNPJ de órgão público em S-1000. Se
            {ideAdv/tpInsc}(./tpInsc) = [1], deve possuir 14 (catorze) algarismos e, no caso de declarante
            pessoa jurídica, ser diferente do CNPJ base do empregador (exceto se
            {ideEmpregador/nrInsc}(/ideEmpregador_nrInsc) tiver 14 (catorze) algarismos). Se
            {ideAdv/tpInsc}(./tpInsc) = [2], deve possuir 11 (onze) algarismos e, no caso de declarante pessoa
            física, ser diferente do CPF do empregador.
        :ivar vlrAdv: Valor da despesa com o advogado, se houver.
        """

        tpInsc: TsTpInsc12 = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            }
        )
        nrInsc: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "pattern": r"\d{11}|\d{14}",
            }
        )
        vlrAdv: None | Decimal = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("999999999999.99"),
                "total_digits": 14,
                "fraction_digits": 2,
            },
        )


@dataclass(kw_only=True)
class TInfoSimples(CommonMixin):
    """
    Informação relativa a empresas do Simples DESCRICAO_COMPLETA:Informação relativa a empresas enquadradas no
    regime de tributação Simples Nacional.

    CONDICAO_GRUPO: O (se {classTrib}(1000_infoEmpregador_inclusao_infoCadastro_classTrib) em S-1000 = [03]); N
    (nos demais casos).

    :ivar indSimples: Indicador de contribuição substituída.
    """

    class Meta:
        name = "T_infoSimples"

    indSimples: TsIndSimples = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )


@dataclass(kw_only=True)
class TItensRemunRpps(CommonMixin):
    """
    Itens da remuneração do trabalhador DESCRICAO_COMPLETA:Rubricas que compõem a remuneração do trabalhador.

    :ivar codRubr: Informar o código atribuído pelo empregador que identifica a rubrica em sua folha de
        pagamento.
    :ivar ideTabRubr:
    :ivar qtdRubr: Informar a quantidade de referência para apuração (em horas, cotas, meses, etc.). Validação:
        Deve ser maior que 0 (zero).
    :ivar fatorRubr: Informar o fator, percentual, etc. da rubrica, quando necessário. Validação: Deve ser maior
        que 0 (zero).
    :ivar vrRubr:
    :ivar indApurIR: Indicativo de tipo de apuração de IR.
    """

    class Meta:
        name = "T_itensRemun_rpps"

    codRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
            "pattern": r".*[^\s].*",
        }
    )
    ideTabRubr: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 8,
            "pattern": r".*[^\s].*",
        }
    )
    qtdRubr: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999.99"),
            "total_digits": 12,
            "fraction_digits": 2,
        },
    )
    fatorRubr: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("999.99"),
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    vrRubr: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.99"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    indApurIR: TsIndApurIr = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )


@dataclass(kw_only=True)
class TLocalTrabGeral(CommonMixin):
    """
    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do contribuinte de acordo com o tipo de inscrição indicado no
        campo {localTrabGeral/tpInsc}(./tpInsc). Validação: Deve ser um número de inscrição válido e existente
        na Tabela de Estabelecimentos (S-1005), bem como compatível com {localTrabGeral/tpInsc}(./tpInsc).
    :ivar descComp:
    """

    class Meta:
        name = "T_localTrabGeral"

    tpInsc: TsTpInsc134 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{12}|\d{14}",
        }
    )
    descComp: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 80,
            "pattern": r"[^\s]{1}[\S\s]*",
        },
    )


@dataclass(kw_only=True)
class TProcJudTrab(CommonMixin):
    """
    Informações sobre a existência de processos judiciais do trabalhador DESCRICAO_COMPLETA:Informações sobre a
    existência de processos judiciais do trabalhador com decisão favorável quanto à não incidência de contribuições
    sociais e/ou Imposto de Renda.

    CHAVE_GRUPO: {tpTrib}, {nrProcJud}, {codSusp} CONDICAO_GRUPO: OC.
    """

    class Meta:
        name = "T_procJudTrab"

    tpTrib: TsTpTrib = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrProcJud: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "length": 20,
        }
    )
    codSusp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{1,14}",
        }
    )


@dataclass(kw_only=True)
class TRemuneracao(CommonMixin):
    """
    :ivar vrSalFx:
    :ivar undSalFixo:
    :ivar dscSalVar: Descrição do salário por tarefa ou variável e como este é calculado. Ex.: Comissões pagas
        no percentual de 10% sobre as vendas. Validação: Preenchimento obrigatório se {undSalFixo}(./undSalFixo)
        for igual a [6, 7].
    """

    class Meta:
        name = "T_remuneracao"

    vrSalFx: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999.99"),
            "total_digits": 14,
            "fraction_digits": 2,
        }
    )
    undSalFixo: TsUndSalFixo = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    dscSalVar: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 999,
            "pattern": r"[^\s]{1}[\S\s]*",
        },
    )


@dataclass(kw_only=True)
class TSucessaoVinc(CommonMixin):
    """
    :ivar tpInsc:
    :ivar nrInsc: Informar o número de inscrição do empregador anterior, de acordo com o tipo de inscrição
        indicado no campo {sucessaoVinc/tpInsc}(./tpInsc).
    :ivar matricAnt: Matrícula do trabalhador no empregador anterior.
    :ivar dtAdm: Preencher com a data de admissão do trabalhador. No caso de transferência do empregado, deve
        ser preenchida a data inicial do vínculo no primeiro empregador (data de início do vínculo).
    """

    class Meta:
        name = "T_sucessaoVinc"

    tpInsc: TsTpInsc12 = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
    nrInsc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "pattern": r"\d{11}|\d{14}",
        }
    )
    matricAnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
            "min_length": 1,
            "max_length": 30,
        },
    )
    dtAdm: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.esocial.gov.br/schema/evt/evtAdmPrelim/v_S_01_03_00",
        }
    )
