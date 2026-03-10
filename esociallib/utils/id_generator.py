"""
id_generator.py — Geração de IDs únicos para eventos eSocial.

Formato oficial do eSocial S-1.3 (36 caracteres):
  ID{tpInsc:1}{nrInsc:14}{AAAA:4}{MMDD:4}{HHMMSS:6}{seq:5}

Exemplo: ID1123456780000002024031512300000001
         ID + 1 + 12345678000000 + 2024 + 0315 + 123000 + 00001
"""

from __future__ import annotations

import threading
from datetime import datetime

_lock = threading.Lock()
_counter: int = 0


def generate_event_id(
    tp_insc: int = 1,
    nr_insc: str = "00000000000000",
) -> str:
    """
    Gera um Id único para o evento no formato oficial eSocial.

    Formato: ID{tpInsc:1}{nrInsc:14}{AAAA}{MMDD}{HHMMSS}{seq:5}
    Total: 2 + 1 + 14 + 4 + 4 + 6 + 5 = 36 caracteres.

    :param tp_insc: Tipo de inscrição (1=CNPJ, 2=CPF).
    :param nr_insc: Número de inscrição (CNPJ/CPF, será padded a 14 dígitos).
    :returns: String Id com exatamente 36 caracteres.
    """
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    nr = str(nr_insc).ljust(14, "0")[:14]

    global _counter
    with _lock:
        _counter += 1
        seq = _counter

    return f"ID{int(tp_insc)}{nr}{ts}{seq:05d}"


def reset_counters() -> None:
    """Reseta contadores — usar apenas em testes."""
    global _counter
    with _lock:
        _counter = 0
