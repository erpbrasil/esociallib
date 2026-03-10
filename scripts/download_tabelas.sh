#!/usr/bin/env bash
# download_tabelas.sh — Baixa todas as tabelas de referência do eSocial (site oficial).
#
# Fonte: https://frontend.esocial.gov.br/adm/Home/Index
# Endpoint: POST https://frontend.esocial.gov.br/adm/Home/BaixarConteudoTabela
#
# Os valores (TABELA + versão) são extraídos do <select> da página oficial.
# Algumas tabelas têm espaço no código (ex: "TABELA 65|6") — isso é intencional.
#
# Uso:
#   ./scripts/download_tabelas.sh
#
# Os arquivos são salvos em esociallib/tabelas/ no formato CSV (pipe-separated).
# Versione no git para acompanhar mudanças nas tabelas oficiais.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DEST_DIR="$PROJECT_DIR/esociallib/tabelas"

BASE_URL="https://frontend.esocial.gov.br/adm/Home/BaixarConteudoTabela"

# Valores exatos do <select id="CodigoTabela"> da página oficial.
# Formato: "valor_do_option|nome_descritivo_para_arquivo"
# IMPORTANTE: os valores incluem espaços e maiúsculas/minúsculas exatamente
# como aparecem no HTML do portal.
TABELAS=(
    "TABELA1|13|01_categorias_trabalhadores"
    "TABELA2|1|02_financiamento_aposent_especial"
    "TABELA3|9|03_natureza_rubricas"
    "TABELA4|1|04_fpas_terceiros"
    "TABELA5|1|05_tipos_inscricao"
    "TABELA6|4|06_paises"
    "TABELA8|1|08_classificacao_tributaria"
    "TABELA9|14|09_tipos_arquivo"
    "TABELA10|5|10_tipos_lotacao"
    "TABELA11|9|11_compat_trab_classtrib_lotacao"
    "TABELA13|1|13_parte_corpo_atingida"
    "TABELA14|1|14_agente_causador_acidente"
    "TABELA15|3|15_situacao_geradora_acidente"
    "TABELA17|1|17_natureza_lesao"
    "TABELA18|12|18_motivos_afastamento"
    "TABELA19|10|19_motivos_desligamento"
    "TABELA20|1|20_tipos_logradouros"
    "TABELA21|4|21_incidencia_tributaria_irrf"
    "TABELA22|4|22_agentes_nocivos_aposent_especial"
    "TABELA23|1|23_aposentadoria_especial_inss"
    "TABELA24|3|24_compat_fpas_classtrib"
    "TABELA25|2|25_tipos_dependente"
    "TABELA27|2|27_procedimentos_diagnosticos"
    "TABELA29|2|29_treinamentos_capacitacoes"
    "TABELA30|1|30_tributacao_beneficiarios_exterior"
    "TABELA 32|2|32_receita_reclamatoria_trabalhista"
    "TABELA34|2|34_motivos_cessacao_beneficios"
    "TABELA35|5|35_tipos_beneficios"
    "TABELA37|11|37_instituicoes_emprestimo_consignado"
    "TABELA50|9|50_cbo"
    "TABELA51|1|51_codigos_terceiro"
    "TABELA52|1|52_horarios"
    "TABELA53|3|53_naturezas_juridicas"
    "TABELA54|19|54_rubricas"
    "TABELA56|1|56_cnae"
    "TABELA57|7|57_contrib_previdenciaria_empregado"
    "TABELA58|4|58_retencao_irrf"
    "TABELA59|1|59_tipo_decisao_judicial_admin"
    "TABELA60|1|60_cid"
    "TABELA61|1|61_cargos"
    "TABELA64|1|64_lotacoes_tributaria"
    "TABELA 65|6|65_salario_familia"
    "TABELA67|5|67_causas_afastamento_mte"
    "TABELA 68|5|68_rubricas_rescisorias_mte"
    "Tabela 69|1|69_info_adicionais_rescisao_mte"
    "TABELA70|1|70_tipos_admissao"
    "TABELA71|1|71_tipos_cat"
    "TABELA72|1|72_tipos_aso"
    "TABELA73|1|73_tipos_aviso_previo"
    "TABELA74|1|74_motivos_cancelamento_aviso_previo"
    "TABELA77|1|77_processo_fap"
    "TABELA78|5|78_receita_totalizadores"
    "TABELA79|2|79_tipo_valor_contrib_prev_totalizadores"
    "TABELA80|1|80_tipo_valor_irrf_totalizadores"
    "TABELA81|1|81_cnae_mei_web"
    "TABELA82|1|82_bases_calculo_fgts_totalizadores"
    "TABELA83|1|83_tipos_deposito_fgts_totalizadores"
    "TABELA84|2|84_feriados"
    "TABELA85|1|85_descricao_fpas"
    "TABELA86|2|86_teto_isencao_verde_amarela"
)

mkdir -p "$DEST_DIR"

echo "=== Download das tabelas do eSocial (portal oficial) ==="
echo "Fonte: https://frontend.esocial.gov.br/adm/Home/Index"
echo "Destino: $DEST_DIR"
echo ""

SUCCESS=0
FAIL=0

for ENTRY in "${TABELAS[@]}"; do
    # Formato: "CODIGO_TABELA|VERSAO|NOME_ARQUIVO"
    # O código pode conter espaços (ex: "TABELA 65|6|65_salario_familia")
    # Separamos pelo último dois campos após o primeiro pipe
    NOME_ARQ="${ENTRY##*|}"
    REST="${ENTRY%|*}"
    CODIGO="${REST}"

    FILENAME="tabela_${NOME_ARQ}.csv"
    FILEPATH="$DEST_DIR/$FILENAME"

    printf "  %-55s " "$NOME_ARQ (${CODIGO})"

    # O valor enviado ao servidor é exatamente o value do <option>: "TABELAX|versao"
    HTTP_CODE=$(curl -s -o "$FILEPATH" -w "%{http_code}" \
        -X POST "$BASE_URL" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        --data-urlencode "codigoTabela=${CODIGO}" \
        2>/dev/null)

    if [ "$HTTP_CODE" = "200" ] && [ -s "$FILEPATH" ]; then
        LINES=$(wc -l < "$FILEPATH")
        SIZE=$(wc -c < "$FILEPATH" | tr -d ' ')
        printf "OK  (%s linhas, %s bytes)\n" "$LINES" "$SIZE"
        SUCCESS=$((SUCCESS + 1))
    else
        printf "FALHOU (HTTP %s)\n" "$HTTP_CODE"
        rm -f "$FILEPATH"
        FAIL=$((FAIL + 1))
    fi
done

echo ""
echo "=== Resultado: $SUCCESS OK, $FAIL falhas ==="
echo "Arquivos salvos em: $DEST_DIR"
