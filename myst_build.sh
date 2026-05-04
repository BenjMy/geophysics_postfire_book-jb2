#!/usr/bin/env bash
# =============================================================================
# clean_and_build.sh
# Build PDF or full site from a language-specific MyST config file.
#
# Expects myst_EN.md and myst_ES.md (or myst.yml variants) in the project root.
# The selected config is temporarily symlinked/copied as myst.yml before build.
#
# Usage:
#   bash clean_and_build.sh                        # build PDF in EN (default)
#   bash clean_and_build.sh --lang es              # build PDF in ES
#   bash clean_and_build.sh --lang en --all        # build everything in EN
#   bash clean_and_build.sh clean --lang es --all  # clean + build everything in ES
#   bash clean_and_build.sh clean                  # clean + build PDF in EN
#
# Flags (order-independent):
#   clean          remove execution cache before build
#   --lang en|es   select language config (default: en)
#   --all          build HTML + PDF (passes --all to myst build)
#                  omitting --all defaults to --pdf
# =============================================================================
set -euo pipefail

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${SCRIPT_DIR}/_build"
MYST_CONFIG="${SCRIPT_DIR}/myst.yml"   # the active config myst expects

# -----------------------------------------------------------------------------
# Defaults
# -----------------------------------------------------------------------------
CLEAN=false
LANG="en"
BUILD_ARGS=()   # extra args passed to myst build (--pdf or --all)

# -----------------------------------------------------------------------------
# Parse arguments (order-independent)
# -----------------------------------------------------------------------------
for arg in "$@"; do
    case "$arg" in
        clean)      CLEAN=true ;;
        --all)      BUILD_ARGS+=("--all") ;;
        --lang)     ;;   # handled below via shift-style workaround
        --lang=*)   LANG="${arg#--lang=}" ;;
        en|es|EN|ES) LANG="${arg,,}" ;;   # bare language token, lowercase
        *)          BUILD_ARGS+=("$arg") ;;
    esac
done

# Handle "--lang en" / "--lang es" (space-separated) by scanning positional pairs
prev=""
for arg in "$@"; do
    if [[ "$prev" == "--lang" ]]; then
        LANG="${arg,,}"
    fi
    prev="$arg"
done

# Validate language
LANG="${LANG,,}"   # normalise to lowercase
if [[ "$LANG" != "en" && "$LANG" != "es" ]]; then
    echo "❌  Unknown language: '$LANG'. Use 'en' or 'es'."
    exit 1
fi

# Default build target = PDF
if [[ ${#BUILD_ARGS[@]} -eq 0 ]]; then
    BUILD_ARGS=("--pdf")
fi

# -----------------------------------------------------------------------------
# Resolve language config file
# Supports both:
#   myst_EN.yml / myst_ES.yml   (YAML configs)
#   myst_EN.md  / myst_ES.md    (MyST-MD project configs, if used)
# -----------------------------------------------------------------------------
LANG_UPPER="${LANG^^}"
LANG_CONFIG=""

for ext in yml yaml md; do
    candidate="${SCRIPT_DIR}/myst_${LANG_UPPER}.${ext}"
    if [[ -f "$candidate" ]]; then
        LANG_CONFIG="$candidate"
        break
    fi
done

if [[ -z "$LANG_CONFIG" ]]; then
    echo "❌  No language config found for '${LANG_UPPER}'."
    echo "    Expected one of:"
    echo "      ${SCRIPT_DIR}/myst_${LANG_UPPER}.yml"
    echo "      ${SCRIPT_DIR}/myst_${LANG_UPPER}.yaml"
    echo "      ${SCRIPT_DIR}/myst_${LANG_UPPER}.md"
    exit 1
fi

# Determine target config filename (must match what myst expects: myst.yml)
LANG_CONFIG_EXT="${LANG_CONFIG##*.}"
MYST_CONFIG="${SCRIPT_DIR}/myst.${LANG_CONFIG_EXT}"

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
echo "============================================================"
echo "  LANGUAGE : ${LANG_UPPER}"
echo "  CONFIG   : ${LANG_CONFIG}"
echo "  BUILD    : ${BUILD_ARGS[*]}"
echo "  CLEAN    : ${CLEAN}"
echo "============================================================"
echo ""

# -----------------------------------------------------------------------------
# Activate language config
# Backup existing myst.yml if it is not already a language-specific file,
# then symlink the selected language config as myst.yml.
# -----------------------------------------------------------------------------
BACKUP="${SCRIPT_DIR}/myst.${LANG_CONFIG_EXT}.bak"

if [[ -f "$MYST_CONFIG" && ! -L "$MYST_CONFIG" ]]; then
    echo "  📦  Backing up existing $(basename "$MYST_CONFIG") → $(basename "$BACKUP")"
    cp "$MYST_CONFIG" "$BACKUP"
fi

echo "  🔗  Activating config: $(basename "$LANG_CONFIG") → $(basename "$MYST_CONFIG")"
ln -sf "$LANG_CONFIG" "$MYST_CONFIG"
echo ""

# Restore the original config on exit (even on error)
restore_config() {
    if [[ -f "$BACKUP" ]]; then
        echo ""
        echo "  ♻️   Restoring original $(basename "$MYST_CONFIG") from backup"
        mv "$BACKUP" "$MYST_CONFIG"
    else
        # Remove the symlink if there was no original
        [[ -L "$MYST_CONFIG" ]] && rm -f "$MYST_CONFIG"
    fi
}
trap restore_config EXIT

# -----------------------------------------------------------------------------
# Optional cleaning
# -----------------------------------------------------------------------------
if [[ "$CLEAN" == true ]]; then
    echo "============================================================"
    echo "  CLEAN MODE: Removing execution cache"
    echo "============================================================"
    if [[ ! -d "$BUILD_DIR" ]]; then
        echo "  ⚠️   Build directory does not exist: $BUILD_DIR — skipping clean"
    else
        for folder in execute cache; do
            target="${BUILD_DIR}/${folder}"
            if [[ -d "$target" ]]; then
                rm -rf "$target"
                echo "  🗑️   Removed $target"
            else
                echo "  ✅  $target does not exist — nothing to remove"
            fi
        done
    fi
    echo ""
fi

# -----------------------------------------------------------------------------
# Build
# -----------------------------------------------------------------------------
echo "============================================================"
echo "  Running: myst build --execute ${BUILD_ARGS[*]}"
echo "============================================================"
echo ""
myst build --execute "${BUILD_ARGS[@]}"
