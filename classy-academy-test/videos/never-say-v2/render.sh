#!/usr/bin/env bash
# Full Production Build, Render & QA Pipeline for:
# "8 Things Elegant Ladies Never Say: What to Say Instead" (never-say-v2)
set -euo pipefail

WORK="$(cd "$(dirname "$0")" && pwd)"
T="$(cd "$WORK/../../workflow/tools" && pwd)"
cd "$WORK"
mkdir -p raw tts assets out qa render-output

echo "=== Step 1: Downloading & Verifying All 88 Video Assets + 4 Piano Tracks ==="
python3 fetch_assets.py

echo "=== Step 2: Probing Clip Shots & Running AI-Watermark Scan (aiscan.py) ==="
python3 "$T/shots.py" qa/shots
python3 "$T/aiscan.py" | tee render-output/aiscan_report.txt

echo "=== Step 3: Calibrating & Generating Kokoro-82M Narration (voice='af_heart', speed=0.88 -> ~150 WPM) ==="
python3 "$T/tts.py" beats.txt tts 0.88 | tee render-output/tts_report.txt

echo "=== Step 4: Extracting Word-Level Timings via faster-whisper (words.py) ==="
python3 "$T/words.py" /tmp/whisper | tee render-output/words_report.txt

echo "=== Step 5: Assembling Timeline, Audio Mix (-19.5 LUFS + -12dB Solo Piano + Charade Audio) & HTML Stage (build.py) ==="
python3 "$T/build.py" | tee render-output/build_report.txt

echo "=== Step 6: Capturing Chrome Text/Card Sprites & Rendering Full 1080p30 MP4 (ffr_capture.js + ffr.py) ==="
mkdir -p ff/sprites
CHROME_BIN=$(python3 -c "import glob; c = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome') + glob.glob('/home/*/.cache/ms-playwright/chromium-*/chrome-linux/chrome') + ['/usr/bin/google-chrome', '/usr/bin/chromium-browser', '/usr/bin/chromium']; print(next(x for x in c if __import__('os').path.exists(x)))")
echo "Using Chrome binary: $CHROME_BIN"
sed -i "s|/opt/pw-browsers/chromium-1194/chrome-linux/chrome|$CHROME_BIN|g" "$T/ffr_capture.js"
NODE_DIR="$(pwd)"
if [ ! -d "$NODE_DIR/node_modules/puppeteer-core" ]; then
  npm install --no-save puppeteer-core@23.11.1
fi
node "$T/ffr_capture.js" "$NODE_DIR" "$WORK" "$WORK/ff/sprites"
DUR=$(python3 -c "import re; print(re.search(r'data-duration=\"([\d.]+)\"', open('index.html').read()).group(1))")
echo "Rendering full video duration: ${DUR}s at 1920x1080 @ 30fps..."
python3 "$T/ffr.py" . 0 "$DUR" out/never-say-v2.mp4 4 | tee render-output/ffr_report.txt

echo "=== Step 7: Running Automated Technical & Visual QA Suite (qa.py, empty.py, flash.py, wordsheet.py, chapters.py) ==="
python3 "$T/qa.py" out/never-say-v2.mp4 | tee render-output/qa_report.txt
python3 "$T/empty.py" out/never-say-v2.mp4 | tee render-output/empty_report.txt
python3 "$T/flash.py" | tee render-output/flash_report.txt
python3 "$T/wordsheet.py" out/never-say-v2.mp4 4.0
python3 "$T/chapters.py" | tee render-output/chapters.txt
cp qa/words_*.jpg render-output/ || true

echo "=== Step 8: Uploading Rendered MP4 (out/never-say-v2.mp4) ==="
python3 - << 'EOF'
import subprocess, json, os
mp4 = "out/never-say-v2.mp4"
urls = {}
# 1. Try Gofile (try upload.gofile.io or querying best server first)
try:
    srv_raw = subprocess.run(["curl", "-s", "https://api.gofile.io/servers"], capture_output=True, text=True, timeout=20).stdout
    srv = json.loads(srv_raw).get("data", {}).get("servers", [{}])[0].get("name", "store1")
    up_url = f"https://{srv}.gofile.io/contents/uploadfile"
    res = subprocess.run(["curl", "-s", "-F", f"file=@{mp4}", up_url], capture_output=True, text=True, timeout=300).stdout
    urls["gofile"] = json.loads(res)
except Exception as e:
    urls["gofile_err"] = str(e)
try:
    res2 = subprocess.run(["curl", "-s", "-F", f"file=@{mp4}", "https://upload.gofile.io/uploadfile"], capture_output=True, text=True, timeout=300).stdout
    urls["gofile_legacy"] = json.loads(res2)
except Exception as e:
    urls["gofile_legacy_err"] = str(e)
# 2. Try litterbox / catbox / transfer.sh / 0x0.st as backup download links
try:
    res3 = subprocess.run(["curl", "-s", "-F", "reqtype=fileupload", "-F", "time=72h", "-F", f"fileToUpload=@{mp4}", "https://litterbox.catbox.moe/resources/internals/api.php"], capture_output=True, text=True, timeout=300).stdout
    urls["litterbox_72h"] = res3.strip()
except Exception as e:
    urls["litterbox_err"] = str(e)
with open("render-output/upload_urls.json", "w") as f:
    json.dump(urls, f, indent=2)
print("UPLOAD URLS:", json.dumps(urls, indent=2))
EOF

echo "=== Complete! ==="
