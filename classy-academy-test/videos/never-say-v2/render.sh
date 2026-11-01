#!/usr/bin/env bash
# render.sh — Complete End-to-End Voice, Asset Prep, Build, Render & QA Pipeline
# for "8 Things Elegant Ladies Never Say: What to Say Instead" (videos/never-say-v2)
set -euo pipefail

SLUG="never-say-v2"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
WF="$REPO_ROOT/classy-academy-test/workflow"
TOOLS="$WF/tools"
VDIR="$REPO_ROOT/classy-academy-test/videos/$SLUG"
WORK="${1:-/tmp/$SLUG}"

echo "== [1/6] Initializing work folder: $WORK"
bash "$WF/setup.sh" "$WORK"
cp "$VDIR/beats.txt" "$VDIR/gaps.json" "$VDIR/title.txt" "$VDIR/edit.py" "$VDIR/ok.txt" "$WORK/"
cp "$VDIR/beats.txt" "$WORK/beats_tts.txt"

cd "$WORK"

echo "== [2/6] Generating Kokoro af_heart (speed=0.80) narration & Whisper word timestamps"
python3 "$TOOLS/tts.py"
python3 "$TOOLS/words.py" "${WORK}_models"

echo "== [3/6] Running AI watermark scan & building HyperFrames composition (index.html + assets/mix.wav)"
python3 "$TOOLS/aiscan.py"
python3 "$TOOLS/build.py"

echo "== [4/6] Rendering 1920x1080 30fps MP4 via HyperFrames (supports cream framed + phrase layouts)"
npx hyperframes lint
npx hyperframes render -o "out/${SLUG}_v1.mp4" --workers 4

echo "== [5/6] Running strict QA checks (black frames, frozen frames, LUFS loudness, empty backdrops)"
python3 "$TOOLS/qa.py" "out/${SLUG}_v1.mp4"
python3 "$TOOLS/empty.py" "out/${SLUG}_v1.mp4"

echo "== [6/6] Render complete: $WORK/out/${SLUG}_v1.mp4"
