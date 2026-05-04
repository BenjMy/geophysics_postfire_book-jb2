#!/usr/bin/env bash
# =============================================================================
# clean_and_build.sh (CLEAN REWRITE)
#
# Language switching for MyST builds.
#
# CONFIG RULES:
#   English → myst.yml   (default, always used directly)
#   Spanish → myst_ES.yml
#
# Usage:
#   bash clean_and_build.sh
#   bash clean_and_build.sh --lang es
#   bash clean_and_build.sh --lang en --all
#   bash clean_and_build.sh clean --lang es
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

BUILD_DIR="${SCRIPT_DIR}/_build"
ACTIVE_CONFIG="${SCRIPT_DIR}/myst.yml"

# -----------------------------------------------------------------------------
# Defaults
# -----------------------------------------------------------------------------
LANG="en"
CLEAN=false
BUILD_ARGS=()

# -----------------------------------------------------------------------------
# Parse arguments
# -----------------------------------------------------------------------------
for arg in "$@"; do
    case "$arg" in
        clean) CLEAN=true ;;
        --all) BUILD_ARGS+=("--all") ;;
        --lang=*) LANG="${arg#--lang=}" ;;
        en|es|EN|ES) LANG="${arg,,}" ;;
        *) BUILD_ARGS+=("$arg") ;;
    esac
done

# handle "--lang es"
prev=""
for arg in "$@"; do
    if [[ "$prev" == "--lang" ]]; then
        LANG="${arg,,}"
    fi
    prev="$arg"
done

LANG="${LANG,,}"

if [[ "$LANG" != "en" && "$LANG" != "es" ]]; then
    echo "❌ Invalid language: $LANG (use en or es)"
    exit 1
fi

# default build mode
if [[ ${#BUILD_ARGS[@]} -eq 0 ]]; then
    BUILD_ARGS=("--pdf")
fi

# -----------------------------------------------------------------------------
# Resolve config
# -----------------------------------------------------------------------------
if [[ "$LANG" == "en" ]]; then
    LANG_CONFIG="${SCRIPT_DIR}/myst.yml"
else
    LANG_CONFIG="${SCRIPT_DIR}/myst_ES.yml"
fi

if [[ ! -f "$LANG_CONFIG" ]]; then
    echo "❌ Missing config: $LANG_CONFIG"
    exit 1
fi

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
echo "============================================================"
echo " LANGUAGE : ${LANG^^}"
echo " CONFIG   : $LANG_CONFIG"
echo " BUILD    : ${BUILD_ARGS[*]}"
echo " CLEAN    : $CLEAN"
echo "============================================================"
echo ""

# -----------------------------------------------------------------------------
# Activate config ONLY if needed
# -----------------------------------------------------------------------------
if [[ "$LANG" == "en" ]]; then
    echo "🔹 Using default English config (myst.yml) — no symlink needed"
else
    echo "🔗 Activating Spanish config → myst.yml"

    ln -sf "$LANG_CONFIG" "$ACTIVE_CONFIG"
fi

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------
if [[ "$CLEAN" == true ]]; then
    echo "============================================================"
    echo " CLEAN MODE"
    echo "============================================================"

    if [[ -d "$BUILD_DIR" ]]; then
        rm -rf "$BUILD_DIR/execute" "$BUILD_DIR/cache"
        echo "🗑️ Build cache cleaned"
    else
        echo "⚠️ No build directory found"
    fi
    echo ""
fi

# -----------------------------------------------------------------------------
# Build
# -----------------------------------------------------------------------------
echo "============================================================"
echo " Running: myst build --execute ${BUILD_ARGS[*]}"
echo "============================================================"
echo ""

myst build --execute "${BUILD_ARGS[@]}"
