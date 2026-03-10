"""Hierarquia de exceções da esociallib."""


class EsocialError(Exception):
    """Exceção base para todos os erros da esociallib."""


class EsocialValidationError(EsocialError):
    """
    Falha na validação XSD ou em regra de negócio.

    :param errors: Lista de mensagens de erro.
    :param event_type: Tipo de evento que falhou (ex: 'S-2200').
    """

    def __init__(self, errors: list[str], event_type: str = ""):
        self.errors = errors
        self.event_type = event_type
        msg = f"Validação falhou para {event_type}:\n" + "\n".join(
            f"  - {e}" for e in errors
        )
        super().__init__(msg)


class EsocialSignatureError(EsocialError):
    """
    Falha na assinatura digital do XML.

    :param message: Descrição do erro.
    """


class EsocialTransmissionError(EsocialError):
    """
    Falha na transmissão SOAP ao eSocial.

    :param message: Descrição do erro.
    :param status_code: HTTP status code (se disponível).
    :param response_body: Corpo da resposta (se disponível).
    """

    def __init__(
        self,
        message: str = "",
        status_code: int | None = None,
        response_body: str | None = None,
    ):
        self.status_code = status_code
        self.response_body = response_body
        super().__init__(message)


class EsocialBatchError(EsocialError):
    """
    Erro de lote — um ou mais eventos rejeitados pelo governo.

    :param protocol: Protocolo do lote.
    :param rejections: Lista de dicts com detalhes das rejeições.
    """

    def __init__(
        self,
        protocol: str = "",
        rejections: list[dict] | None = None,
    ):
        self.protocol = protocol
        self.rejections = rejections or []
        msg = (
            f"Lote {protocol} com {len(self.rejections)} evento(s) rejeitado(s)"
        )
        super().__init__(msg)
