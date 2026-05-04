#!/usr/bin/env bash
# =============================================================================
# clean_and_build.sh (FINAL CLEAN VERSION)
#
# Language-aware MyST build system.
#
# Rules:
#   en → myst.yml (default, no switching needed)
#   es → myst_ES.yml (copied/symlinked to myst.yml)
#
# MyST NEVER receives --lang (handled internally only)
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
# Parse arguments (STRICT separation: MyST vs internal)
# -----------------------------------------------------------------------------
for arg in "$@"; do
    case "$arg" in
        clean)
            CLEAN=true
            ;;
        --all)
            BUILD_ARGS+=("--all")
            ;;
        --lang=*)
            LANG="${arg#--lang=}"
            ;;
        en|es|EN|ES)
            LANG="${arg,,}"
            ;;
        --lang)
            # ignore standalone flag (value handled in next loop)
            ;;
        *)
            # ONLY pass valid MyST args (explicit whitelist behavior)
            if [[ "$arg" != "en" && "$arg" != "es" ]]; then
                BUILD_ARGS+=("$arg")
            fi
            ;;
    esac
done

# handle: --lang es
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

# Default build mode
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
# Activate config (ONLY for non-English)
# -----------------------------------------------------------------------------
if [[ "$LANG" == "en" ]]; then
    echo "🔹 Using default config (myst.yml)"
else
    echo "🔗 Activating Spanish config → myst.yml"
    ln -sf "$LANG_CONFIG" "$ACTIVE_CONFIG"
fi

# -----------------------------------------------------------------------------
# Clean build cache
# -----------------------------------------------------------------------------
if [[ "$CLEAN" == true ]]; then
    echo "============================================================"
    echo " CLEAN MODE"
    echo "============================================================"

    if [[ -d "$BUILD_DIR" ]]; then
        rm -rf "$BUILD_DIR/execute" "$BUILD_DIR/cache"
        echo "🗑️ Cache cleaned"
    else
        echo "⚠️ No build directory found"
    fi
    echo ""
fi

# -----------------------------------------------------------------------------
# FINAL SAFETY FILTER (guarantees no --lang leakage)
# -----------------------------------------------------------------------------
SAFE_BUILD_ARGS=()
for a in "${BUILD_ARGS[@]}"; do
    [[ "$a" != "--lang" ]] && SAFE_BUILD_ARGS+=("$a")
done

# -----------------------------------------------------------------------------
# Build
# -----------------------------------------------------------------------------
echo "============================================================"
echo " Running: myst build --execute ${SAFE_BUILD_ARGS[*]}"
echo "============================================================"
echo ""

myst build --execute "${SAFE_BUILD_ARGS[@]}"
