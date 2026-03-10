#!/usr/bin/env bash
# =============================================================================
# generate_bindings.sh — Gera os bindings Python xsdata a partir dos XSDs S-1.3
#
# Pré-requisitos:
#   pip install "xsdata[lxml,cli]>=24.0"
#   XSDs S-1.3 devem estar em esociallib/esocial/schemas/v_s13/
#
# Uso:
#   ./scripts/generate_bindings.sh
#   ./scripts/generate_bindings.sh --dry-run   # mostra o que seria gerado
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

SCHEMAS_DIR="${ROOT_DIR}/esociallib/esocial/schemas/v_s13"
OUTPUT_PACKAGE="esociallib.esocial.bindings.v_s13"
OUTPUT_DIR="${ROOT_DIR}/esociallib/esocial/bindings/v_s13"
CONFIG_FILE="${ROOT_DIR}/.xsdata.xml"

# ── Verificações ──────────────────────────────────────────────────────────────

echo "==> Verificando pré-requisitos..."

if ! command -v xsdata &> /dev/null; then
    echo "ERRO: xsdata não encontrado."
    echo "      Execute: pip install 'xsdata[lxml,cli]>=24.0'"
    exit 1
fi

xsdata_version=$(xsdata version 2>/dev/null || echo "0.0.0")
echo "    xsdata ${xsdata_version} encontrado."

xsd_count=$(find "${SCHEMAS_DIR}" -name "*.xsd" 2>/dev/null | wc -l)
if [ "${xsd_count}" -eq 0 ]; then
    echo ""
    echo "ERRO: Nenhum XSD encontrado em ${SCHEMAS_DIR}"
    echo ""
    echo "Baixe os XSDs do eSocial S-1.3 em:"
    echo "  https://www.gov.br/esocial/pt-br/documentacao-tecnica"
    echo ""
    echo "Ou execute o script de download:"
    echo "  ./scripts/download_xsds.sh"
    exit 1
fi

echo "    ${xsd_count} arquivo(s) XSD encontrado(s) em schemas/v_s13/"

if [ "${1:-}" == "--dry-run" ]; then
    echo ""
    echo "==> DRY RUN — comando que seria executado:"
    echo ""
    echo "    xsdata generate \\"
    echo "        ${SCHEMAS_DIR} \\"
    echo "        --config ${CONFIG_FILE} \\"
    echo "        --package ${OUTPUT_PACKAGE}"
    echo ""
    exit 0
fi

# ── Limpeza do output anterior ────────────────────────────────────────────────

echo ""
echo "==> Limpando bindings anteriores em ${OUTPUT_DIR}..."
find "${OUTPUT_DIR}" -name "*.py" ! -name "__init__.py" -delete
echo "    Limpo."

# ── Geração ───────────────────────────────────────────────────────────────────

echo ""
echo "==> Gerando bindings xsdata..."
echo "    Schemas: ${SCHEMAS_DIR}"
echo "    Pacote:  ${OUTPUT_PACKAGE}"
echo "    Config:  ${CONFIG_FILE}"
echo ""

xsdata generate \
    "${SCHEMAS_DIR}" \
    --config "${CONFIG_FILE}" \
    --package "${OUTPUT_PACKAGE}"

# ── Resultado ─────────────────────────────────────────────────────────────────

generated_count=$(find "${OUTPUT_DIR}" -name "*.py" ! -name "__init__.py" | wc -l)
echo ""
echo "==> Concluído. ${generated_count} arquivo(s) gerado(s) em:"
echo "    ${OUTPUT_DIR}"
echo ""
echo "Próximos passos:"
echo "  1. Revisar os builders em esociallib/builders/ e descomentar os campos"
echo "  2. Executar os testes: pytest tests/"
echo "  3. Commitar os bindings gerados (são artefatos do repositório)"
