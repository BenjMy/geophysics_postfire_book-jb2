#!/usr/bin/env bash
# =============================================================================
# clean_and_build.sh
# Default: build PDF
# Optional: clean execution cache before build
#
# Usage:
#   bash clean_and_build.sh              # build PDF (default)
#   bash clean_and_build.sh clean        # clean + build PDF
#   bash clean_and_build.sh --all        # build everything (no clean)
#   bash clean_and_build.sh clean --all  # clean + build everything
# =============================================================================

set -euo pipefail

BUILD_DIR="/home/ben/Nextcloud/BenCSIC/Codes/Tech4agro_org/geophysics_postfire_book-jb2/_build"

CLEAN=false
ARGS=()

# -----------------------------
# Parse arguments
# -----------------------------
for arg in "$@"; do
    if [[ "$arg" == "clean" ]]; then
        CLEAN=true
    else
        ARGS+=("$arg")
    fi
done

# -----------------------------
# Default build mode = PDF
# -----------------------------
if [[ ${#ARGS[@]} -eq 0 ]]; then
    ARGS=("--pdf")
fi

# -----------------------------
# Optional cleaning
# -----------------------------
if [[ "$CLEAN" == true ]]; then
    echo "============================================================"
    echo "  CLEAN MODE: Removing execution cache in $BUILD_DIR"
    echo "============================================================"

    if [[ ! -d "$BUILD_DIR" ]]; then
        echo "❌ Build directory does not exist: $BUILD_DIR"
        exit 1
    fi

    for folder in execute cache; do
        target="$BUILD_DIR/$folder"
        if [[ -d "$target" ]]; then
            rm -rf "$target"
            echo "  🗑️  Removed $target"
        else
            echo "  ✅  $target does not exist — nothing to remove"
        fi
    done

    echo ""
else
    echo "============================================================"
    echo "  NO CLEANING (default)"
    echo "============================================================"
    echo ""
fi

# -----------------------------
# Build
# -----------------------------
echo "============================================================"
echo "  Running: myst build --execute ${ARGS[*]}"
echo "============================================================"
echo ""

myst build --execute "${ARGS[@]}"
