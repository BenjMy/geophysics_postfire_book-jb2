#!/usr/bin/env bash
# video_to_frame_png.sh
# Recursively extract a representative frame from all videos in a folder

set -euo pipefail

ROOT_DIR="${1:-.}"

# Check dependency
command -v ffmpeg &>/dev/null || {
    echo "❌ ffmpeg is not installed"
    exit 1
}

echo "📂 Scanning: $ROOT_DIR"
echo "🎞️ Extracting frames..."

# Supported video extensions
find "$ROOT_DIR" -type f \( \
    -iname "*.mp4" -o \
    -iname "*.mov" -o \
    -iname "*.mkv" -o \
    -iname "*.avi" -o \
    -iname "*.webm" \
\) -print0 | while IFS= read -r -d '' video; do

    dir="$(dirname "$video")"
    base="$(basename "${video%.*}")"
    output="${dir}/${base}__frame.png"

    # Skip if already exists
    if [[ -f "$output" ]]; then
        echo "⏭️  Skipping (exists): $output"
        continue
    fi

    echo "🎬 Processing: $video"

    # Extract frame at 1 second (safe default)
    ffmpeg -y -ss 00:00:01 -i "$video" \
        -vframes 1 \
        -q:v 2 \
        "$output" &>/dev/null

    echo "✅ Saved: $output"
done

echo "🏁 Done." 
