"""
builders/ — Construtores de dataclass por tipo de evento.

Cada módulo registra seu builder via @register_builder("S-XXXX").
Este __init__ importa todos para garantir o registro.

Ao adicionar um novo evento:
  1. Crie builders/s_XXXX.py
  2. Adicione o import abaixo
"""

# Tabelas
from esociallib.builders import s_1000  # noqa: F401
from esociallib.builders import s_1005  # noqa: F401
from esociallib.builders import s_1010  # noqa: F401
from esociallib.builders import s_1020  # noqa: F401
from esociallib.builders import s_1070  # noqa: F401

# Não-periódicos
from esociallib.builders import s_2190  # noqa: F401
from esociallib.builders import s_2200  # noqa: F401
from esociallib.builders import s_2205  # noqa: F401
from esociallib.builders import s_2206  # noqa: F401
from esociallib.builders import s_2210  # noqa: F401
from esociallib.builders import s_2220  # noqa: F401
from esociallib.builders import s_2221  # noqa: F401
from esociallib.builders import s_2230  # noqa: F401
from esociallib.builders import s_2240  # noqa: F401
from esociallib.builders import s_2298  # noqa: F401
from esociallib.builders import s_2299  # noqa: F401
from esociallib.builders import s_2300  # noqa: F401
from esociallib.builders import s_2306  # noqa: F401
from esociallib.builders import s_2399  # noqa: F401
from esociallib.builders import s_2400  # noqa: F401
from esociallib.builders import s_2405  # noqa: F401
from esociallib.builders import s_2410  # noqa: F401
from esociallib.builders import s_2416  # noqa: F401
from esociallib.builders import s_2418  # noqa: F401
from esociallib.builders import s_2420  # noqa: F401
from esociallib.builders import s_2500  # noqa: F401

# Periódicos
from esociallib.builders import s_1200  # noqa: F401
from esociallib.builders import s_1202  # noqa: F401
from esociallib.builders import s_1207  # noqa: F401
from esociallib.builders import s_1210  # noqa: F401
from esociallib.builders import s_1260  # noqa: F401
from esociallib.builders import s_1270  # noqa: F401
from esociallib.builders import s_1280  # noqa: F401
from esociallib.builders import s_1298  # noqa: F401
from esociallib.builders import s_1299  # noqa: F401

# Exclusão
from esociallib.builders import s_3000  # noqa: F401
from esociallib.builders import s_3500  # noqa: F401
