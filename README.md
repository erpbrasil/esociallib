# esociallib

Biblioteca Python para geração, validação, assinatura e transmissão de eventos **eSocial S-1.3**.

Desenvolvida pela [KMEE](https://kmee.com.br) como componente pip do módulo `l10n_br_esocial` para Odoo.

---

## Instalação

```bash
pip install esociallib
```

### Desenvolvimento

```bash
git clone https://github.com/erpbrasil/esociallib
cd esociallib
pip install -e ".[dev]"

./scripts/download_xsds.sh      # baixa XSDs oficiais do gov.br
./scripts/generate_bindings.sh  # gera bindings xsdata
pytest tests/
```

---

## Uso rápido

```python
from esociallib.generator import to_xml
from esociallib.assinatura import assinar
from esociallib.transmissao import enviar_lote, consultar_lote

# 1. Gerar XML a partir de um dict de dados
xml = to_xml("S-2200", {
    "tp_insc": 1,
    "nr_insc": "12345678",
    "cpf_trab": "12345678901",
    "nm_trab": "JOAO DA SILVA",
    "dt_adm": "2024-03-01",
    "matricula": "000123",
    # ...
}, environment="restricted")

# 2. Assinar com certificado ICP-Brasil A1
pfx = open("certificado.pfx", "rb").read()
xml_assinado = assinar(xml, cert_pfx=pfx, cert_password="senha")

# 3. Enviar lote (máx. 50 eventos)
protocolo = enviar_lote([xml_assinado], cert_pfx=pfx,
                        cert_password="senha", environment="restricted")

# 4. Consultar resultado
resultado = consultar_lote(protocolo, cert_pfx=pfx,
                           cert_password="senha", environment="restricted")

for evento in resultado.eventos:
    if evento.aceito:
        print(f"Aceito. Recibo: {evento.nr_recibo}")
    else:
        print(f"Rejeitado: {evento.code} — {evento.description}")
```

---

## Decisões arquiteturais

### 1. Lib de XML — não um cliente eSocial completo

A responsabilidade central é **gerar e validar XML** a partir de dicionários Python. Assinatura digital e transmissão SOAP são delegadas para bibliotecas especializadas do ecossistema [erpbrasil](https://github.com/erpbrasil). Isso permite:

- Usar a esociallib em qualquer contexto Python, não só Odoo
- Atualizar o leiaute (regenerar bindings) sem tocar na camada de transmissão
- Testar geração de XML sem precisar de certificado ou conexão com o governo
- Reutilizar `erpbrasil.assinatura` e `erpbrasil.transmissao` para outros documentos fiscais

### 2. Bindings gerados com xsdata

Os bindings Python são gerados pelo [xsdata](https://xsdata.readthedocs.io) a partir dos XSDs oficiais S-1.3:

- Gera **dataclasses Python puras** (PEP 557) — sem herança de classes base pesadas
- Tipagem completa compatível com mypy e IDEs modernas
- Atualização de leiaute é um único comando: `xsdata generate ./schemas/`
- Fluxo determinístico e auditável: XSD → comando → arquivo `.py`

Os bindings gerados são commitados no repositório para que usuários da lib não precisem ter o xsdata instalado.

### 3. Assinatura delegada para erpbrasil.assinatura

A assinatura digital ICP-Brasil (RSA-SHA1 + C14N + XML-DSig) é tratada pela [erpbrasil.assinatura](https://github.com/erpbrasil/erpbrasil.assinatura), que suporta certificados A1 (PKCS#12) e A3 (HSM/token) e é mantida de forma independente com foco em criptografia brasileira.

**Nota:** O eSocial exige **RSA-SHA1**, não RSA-SHA256. Isso está definido no Manual do Desenvolvedor eSocial v1.15 e nos WSDLs dos webservices. A escolha do algoritmo é configuração da `erpbrasil.assinatura`, não da esociallib.

### 4. Transmissão delegada para erpbrasil.transmissao

O transporte SOAP 1.1 com mTLS é tratado pela [erpbrasil.transmissao](https://github.com/erpbrasil/erpbrasil.transmissao). A esociallib contribui apenas com:

- Os envelopes SOAP específicos do eSocial (`EnviarLoteEventos`, `ConsultarLoteEventos`)
- Os endpoints de produção e produção restrita
- O parser do retorno XML do governo → `LoteResult` / `EventoResult`

O eSocial tem protocolo fundamentalmente diferente dos documentos SEFAZ: lotes de até 50 eventos, polling assíncrono obrigatório desde julho/2024, e webservices da Receita Federal / MTE. Por isso a transmissão é implementada diretamente sobre `erpbrasil.transmissao`, sem camadas intermediárias.

### 5. Builders registráveis por evento

Cada tipo de evento tem um módulo `builders/s_XXXX.py` que registra uma função via `@register_builder("S-XXXX")`. Essa função recebe um dict e retorna um `EventoXml` construído com lxml.etree.

- Adicionar um novo evento não exige alterar código existente — apenas criar um arquivo e um import
- O builder de cada evento documenta explicitamente quais campos são esperados no dict
- É possível testar cada builder isoladamente, sem Odoo e sem certificado
- O registry permite introspecção (`list_supported_events()`) e facilita cobertura de testes

Os mappers Odoo (`hr.employee` → dict, `hr.payslip` → dict) ficam no `l10n_br_esocial`, não aqui. A esociallib não conhece modelos Odoo.

### 6. Validação XSD antes da assinatura

O XML é validado contra o XSD oficial antes de ser assinado e transmitido. Isso detecta erros de preenchimento localmente, sem round-trip até o portal do governo.

Os XSDs não são distribuídos no pacote por serem de autoria do governo federal. O script `scripts/download_xsds.sh` automatiza o download. Uma vez instalados, os schemas são compilados e cacheados em memória.

### 7. Tabelas de referência versionadas

As 60 tabelas oficiais do eSocial (CBO, CNAE, CID, motivos de afastamento, etc.) são baixadas do [portal oficial](https://frontend.esocial.gov.br/adm/Home/Index) e versionadas no git para acompanhar mudanças. O script `scripts/download_tabelas.sh` automatiza a atualização.

---

## Eventos suportados (S-1.3)

| Grupo | Eventos |
|-------|---------|
| Tabelas | S-1000, S-1005, S-1010, S-1020, S-1070 |
| Não-periódicos | S-2190, S-2200, S-2205, S-2206, S-2210, S-2220, S-2221, S-2230, S-2240, S-2298, S-2299, S-2300, S-2306, S-2399, S-2400, S-2405, S-2410, S-2416, S-2418, S-2420, S-2500 |
| Periódicos | S-1200, S-1202, S-1207, S-1210, S-1260, S-1270, S-1280, S-1298, S-1299 |
| Exclusão | S-3000, S-3500 |

## Atualização de leiaute

Quando o governo publicar uma nova NT:

```bash
./scripts/download_xsds.sh      # baixa novos XSDs
./scripts/generate_bindings.sh  # regenera bindings (sobrescreve)
# atualizar _EVENT_XSD_MAP em validators.py se houver eventos novos
pytest tests/
```

## Licença

MIT — [KMEE](https://kmee.com.br)
