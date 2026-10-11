#!/bin/bash
# One-time setup for a fresh cloud session. Safe to re-run.
#   bash .claude/skills/ce-video/tools/setup.sh WORK_DIR
# Installs the tools, creates WORK_DIR with HyperFrames + brand files + music + sound effects,
# and puts the channel voice profile where the youtube-agent skills look for it.
set -e
R=$(cd "$(dirname "$0")/../../../.." && pwd)          # repo root
SK=$R/.claude/skills; W=${1:?usage: setup.sh WORK_DIR}
mkdir -p "$W"/{assets,tts,pin,pinv,dl,out} ~/.claude/youtube
cp "$R/channel/voice.md" ~/.claude/youtube/voice.md

pip install -q "rembg[cpu]==2.0.85" scipy soundfile pillow numpy 2>&1 | grep -v WARNING || true
command -v yt-dlp >/dev/null || pip install -q yt-dlp
command -v ffmpeg >/dev/null || { echo "ffmpeg missing: install it (apt-get install -y ffmpeg)"; exit 1; }

cd "$W"
[ -f package.json ] || echo '{"name":"ce-video","version":"1.0.0","private":true}' > package.json
[ -d node_modules/hyperframes ] || npm install --silent hyperframes@0.8.143
cp -r "$SK/ce-video/brand/fonts" "$W/"; cp "$SK/ce-video/brand/gsap.min.js" "$W/"
cp "$SK/ce-video/brand/logo_ce.png" "$SK/ce-video/brand/logo_ce_dark.png" "$W/assets/"

# music bed: 5 Mixkit piano tracks (free licence) that measured closest to the channel's own music
for id in 644 664 672 184 571; do
  [ -s "$W/assets/m$id.mp3" ] || curl -sSL -A "Mozilla/5.0" -o "$W/assets/m$id.mp3" "https://assets.mixkit.co/music/$id/$id.mp3"
done
# snow overlay (Mixkit) used on winter/emotional full-screen shots
[ -s "$W/assets/mk8468.mp4" ] || curl -sSL -A "Mozilla/5.0" -o "$W/assets/mk8468.mp4" "https://assets.mixkit.co/videos/8468/8468-720.mp4" || true
# soft sound effects bundled with HyperFrames
X=$W/node_modules/hyperframes/dist/skills/media-use/audio/assets/sfx
for s in whoosh whoosh-short sparkle chime click-soft pop; do cp "$X/$s.mp3" "$W/assets/sfx_$s.mp3"; done
echo "ready: $W"
