#!/usr/bin/env bash
# setup.sh - prepare a fresh session and a work folder for one new video.
#   bash classy-academy-test/workflow/setup.sh <scratchpad>/<slug>
# Media lives in the work folder (never in git). Safe to run again: it skips what is already there.
set -euo pipefail
WF="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; REPO="$(cd "$WF/../.." && pwd)"
W="${1:?usage: setup.sh <work folder>}"; mkdir -p "$W"/{assets,fonts,tts,raw,pin,out}; W="$(cd "$W" && pwd)"

echo "== python packages"
python3 - <<'EOF' || pip install -q "numpy" "opencv-python-headless<5" pillow soundfile kokoro-onnx yt-dlp
import numpy, cv2, PIL, soundfile, kokoro_onnx, yt_dlp
assert hasattr(cv2, 'CascadeClassifier')
EOF

echo "== voice model (Kokoro, af_heart)"
K=/root/.cache/hyperframes/tts; mkdir -p $K/models $K/voices
B=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -s $K/models/kokoro-v1.0.onnx ] || curl -sSL -o $K/models/kokoro-v1.0.onnx $B/kokoro-v1.0.onnx
[ -s $K/voices/voices-v1.0.bin ] || curl -sSL -o $K/voices/voices-v1.0.bin $B/voices-v1.0.bin

echo "== HyperFrames 0.8.143 (renderer) in the work folder"
cd "$W"
[ -f package.json ] || echo '{"name":"video","version":"1.0.0","private":true}' > package.json
[ -d node_modules/hyperframes ] || npm install --silent hyperframes@0.8.143
npx hyperframes browser --help >/dev/null 2>&1 || true
npx hyperframes doctor 2>&1 | grep -E "Chrome|FFmpeg|FFprobe" || true   # Docker is not needed: rendering runs locally

echo "== channel assets: fonts, logos, GSAP"
cp --update=none "$WF"/assets/fonts/* fonts/
cp --update=none "$WF"/assets/logo_ce.png "$WF"/assets/logo_ce_dark.png assets/
cp --update=none "$WF"/assets/gsap.min.js .

echo "== music: Mixkit 'Classical 4/5/9/10' by Jonny S. (free licence)"
for id in 711 712 716 717; do
  [ -s assets/m$id.mp3 ] || curl -sSL -o assets/m$id.mp3 https://assets.mixkit.co/music/$id/$id.mp3
done

echo "== voice profile for the YouTube agent skills"
mkdir -p ~/.claude/youtube && cp "$REPO/classy-academy-test/voice.md" ~/.claude/youtube/voice.md

echo "== ready: $W"
echo "   tools: $WF/tools   (run them from inside the work folder)"
