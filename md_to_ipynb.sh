#!/usr/bin/env bash
# md_to_ipynb_execute.sh
# Convert .md → .ipynb (jupytext) then execute in-place (nbconvert)
# MyST's --pdf build then reads pre-executed outputs — no --execute flag needed.

set -euo pipefail

NOTEBOOK_DIR="${1:-/home/ben/Nextcloud/BenCSIC/Codes/Tech4agro_org/geophysics_postfire_book-jb2/notebooks/practical_cases}"

[[ ! -d "$NOTEBOOK_DIR" ]] && { echo "❌ Dir not found: $NOTEBOOK_DIR"; exit 1; }
command -v jupytext   &>/dev/null || { echo "❌ jupytext missing";   exit 1; }
command -v jupyter    &>/dev/null || { echo "❌ jupyter missing";    exit 1; }

echo "=== Step 1: .md → .ipynb (jupytext) ==="
while IFS= read -r -d '' md; do
    ipynb="${md%.md}.ipynb"
    echo "  📄 ${md##*/}"
    jupytext --to ipynb \
             --update \
             --opt "split_at_heading=true" \
             --output "$ipynb" \
             "$md" && echo "     ✅ converted"
done < <(find "$NOTEBOOK_DIR" -maxdepth 3 -name "*.md" -print0 | sort -z)

echo ""
echo "=== Step 2: execute .ipynb in-place (nbconvert) ==="
while IFS= read -r -d '' nb; do
    echo "  ⚙️  ${nb##*/}"
    jupyter nbconvert \
        --to notebook \
        --execute \
        --inplace \
        --ExecutePreprocessor.timeout=600 \
        --ExecutePreprocessor.kernel_name=python3 \
        "$nb" && echo "     ✅ executed"
done < <(find "$NOTEBOOK_DIR" -maxdepth 3 -name "*.ipynb" -print0 | sort -z)

echo ""
echo "=== Step 3: build PDF (no --execute needed) ==="
echo "  Run from your book root:"
echo "  myst build --pdf"
