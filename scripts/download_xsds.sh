#!/usr/bin/env bash
# =============================================================================
# download_xsds.sh — Baixa os XSDs oficiais do eSocial S-1.3
#
# Os XSDs são publicados pelo governo em:
#   https://www.gov.br/esocial/pt-br/documentacao-tecnica
#
# ATENÇÃO: A URL exata do ZIP muda a cada NT (Nota Técnica).
# Atualize XSD_ZIP_URL ao sair uma nova NT.
# NT atual: NT 07/2026 (março 2026)
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SCHEMAS_DIR="${ROOT_DIR}/esociallib/esocial/schemas/v_s13"
TMP_DIR=$(mktemp -d)

# Atualizar esta URL a cada nova NT
# Verificar em: https://www.gov.br/esocial/pt-br/documentacao-tecnica
XSD_ZIP_URL="https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/2026-02-13_esquemas_xsd_v_s_01_03_00.zip"

# Alternativa: path local se já tiver baixado manualmente
LOCAL_ZIP="${ROOT_DIR}/xsds_s13.zip"

echo "==> Baixando XSDs do eSocial S-1.3..."
echo ""

# Tenta download automático, cai no manual se falhar
if curl -fsSL "${XSD_ZIP_URL}" -o "${TMP_DIR}/xsds.zip" 2>/dev/null; then
    echo "    Download concluído."
    ZIP_FILE="${TMP_DIR}/xsds.zip"
elif [ -f "${LOCAL_ZIP}" ]; then
    echo "    Usando arquivo local: ${LOCAL_ZIP}"
    ZIP_FILE="${LOCAL_ZIP}"
else
    echo "AVISO: Download automático falhou e nenhum arquivo local encontrado."
    echo ""
    echo "Baixe manualmente em:"
    echo "  https://www.gov.br/esocial/pt-br/documentacao-tecnica"
    echo ""
    echo "E extraia os XSDs em:"
    echo "  ${SCHEMAS_DIR}"
    exit 1
fi

echo "==> Extraindo XSDs para ${SCHEMAS_DIR}..."
mkdir -p "${SCHEMAS_DIR}"
unzip -o "${ZIP_FILE}" "*.xsd" -d "${TMP_DIR}/extracted" 2>/dev/null || \
    unzip -o "${ZIP_FILE}" -d "${TMP_DIR}/extracted"

# Copia apenas os .xsd para o destino (ignora PDFs, etc.)
find "${TMP_DIR}/extracted" -name "*.xsd" -exec cp {} "${SCHEMAS_DIR}/" \;

xsd_count=$(find "${SCHEMAS_DIR}" -name "*.xsd" | wc -l)
echo "    ${xsd_count} arquivo(s) XSD extraído(s)."

rm -rf "${TMP_DIR}"

echo ""
echo "==> Pronto. Execute agora:"
echo "    ./scripts/generate_bindings.sh"
