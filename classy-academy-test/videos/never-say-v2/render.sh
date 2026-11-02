#!/usr/bin/env bash
# Step-by-step live-committing Production Build, Render & QA Pipeline for never-say-v2
set -euo pipefail

WORK="$(cd "$(dirname "$0")" && pwd)"
T="$(cd "$WORK/../../workflow/tools" && pwd)"
REPO="$(cd "$WORK/../../.." && pwd)"
cd "$WORK"
mkdir -p raw tts assets out qa render-output

commit_status() {
  local msg="$1"
  cd "$REPO"
  git config user.name "github-actions[bot]"
  git config user.email "github-actions[bot]@users.noreply.github.com"
  git add classy-academy-test/videos/never-say-v2/render-output/ classy-academy-test/videos/never-say-v2/CREDITS.txt || true
  git commit -m "ci(status): $msg [skip ci]" || true
  git pull --rebase origin claude/youtube-channel-analysis-lghfsv || true
  git push origin claude/youtube-channel-analysis-lghfsv || true
  cd "$WORK"
}

echo "=== Step 1: Downloading & Verifying All 88 Video Assets + 4 Piano Tracks ===" | tee render-output/step1.log
python3 fetch_assets.py >> render-output/step1.log 2>&1
commit_status "step 1 assets downloaded"

echo "=== Step 2: Probing Clip Shots & Running AI-Watermark Scan (aiscan.py) ===" | tee render-output/step2.log
python3 "$T/shots.py" qa/shots >> render-output/step2.log 2>&1
python3 "$T/aiscan.py" | tee render-output/aiscan_report.txt
cp shots.json render-output/ || true
cp aiscan.json render-output/ || true
commit_status "step 2 shots and aiscan done"

echo "=== Step 3: Calibrating & Generating Kokoro-82M Narration (voice='af_heart', speed=0.88 -> ~150 WPM) ==="
python3 "$T/tts.py" beats.txt tts 0.88 | tee render-output/tts_report.txt
commit_status "step 3 tts done"

echo "=== Step 4: Extracting Word-Level Timings via faster-whisper (words.py) ==="
python3 "$T/words.py" /tmp/whisper | tee render-output/words_report.txt
cp words.json render-output/ || true
commit_status "step 4 whisper word timings done"

echo "=== Step 5: Assembling Timeline, Audio Mix (-19.5 LUFS + -12dB Solo Piano + Charade Audio) & HTML Stage (build.py) ==="
python3 "$T/build.py" | tee render-output/build_report.txt
cp beats.json render-output/ || true
commit_status "step 5 build.py done"

echo "=== Step 6: Capturing Chrome Text/Card Sprites & Rendering Full 1080p30 MP4 (ffr_capture.js + ffr.py) ==="
mkdir -p ff/sprites
CHROME_BIN=$(python3 -c "import glob, shutil, os; c = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome') + glob.glob('/home/*/.cache/ms-playwright/chromium-*/chrome-linux/chrome') + [shutil.which('google-chrome'), shutil.which('chromium-browser'), shutil.which('chromium')]; print(next(x for x in c if x and os.path.exists(x)))")
echo "Using Chrome binary: $CHROME_BIN" | tee render-output/step6.log
sed -i "s|/opt/pw-browsers/chromium-1194/chrome-linux/chrome|$CHROME_BIN|g" "$T/ffr_capture.js"
NODE_DIR="$(pwd)"
if [ ! -d "$NODE_DIR/node_modules/puppeteer-core" ]; then
  npm install --no-save puppeteer-core@23.11.1 >> render-output/step6.log 2>&1
fi
node "$T/ffr_capture.js" "$NODE_DIR" "$WORK" "$WORK/ff/sprites" >> render-output/step6.log 2>&1
commit_status "step 6a sprites captured"

DUR=$(python3 -c "import re; print(re.search(r'data-duration=\"([\d.]+)\"', open('index.html').read()).group(1))")
echo "Rendering full video duration: ${DUR}s at 1920x1080 @ 30fps..." | tee -a render-output/step6.log
python3 "$T/ffr.py" . 0 "$DUR" out/never-say-v2.mp4 4 | tee render-output/ffr_report.txt
commit_status "step 6b mp4 rendered"

echo "=== Step 7: Running Automated Technical & Visual QA Suite (qa.py, empty.py, flash.py, wordsheet.py, chapters.py) ==="
python3 "$T/qa.py" out/never-say-v2.mp4 | tee render-output/qa_report.txt
python3 "$T/empty.py" out/never-say-v2.mp4 | tee render-output/empty_report.txt
python3 "$T/flash.py" | tee render-output/flash_report.txt
python3 "$T/wordsheet.py" out/never-say-v2.mp4 4.0
python3 "$T/chapters.py" | tee render-output/chapters.txt
cp qa/words_*.jpg render-output/ || true
commit_status "step 7 qa and contact sheets done"

echo "=== Step 8: Uploading Rendered MP4 (out/never-say-v2.mp4) ==="
python3 - << 'EOF'
import subprocess, json, os
mp4 = "out/never-say-v2.mp4"
urls = {"size_bytes": os.path.getsize(mp4)}
try:
    srv_raw = subprocess.run(["curl", "-s", "https://api.gofile.io/servers"], capture_output=True, text=True, timeout=20).stdout
    srv = json.loads(srv_raw).get("data", {}).get("servers", [{}])[0].get("name", "store1")
    up_url = f"https://{srv}.gofile.io/contents/uploadfile"
    res = subprocess.run(["curl", "-s", "-F", f"file=@{mp4}", up_url], capture_output=True, text=True, timeout=300).stdout
    urls["gofile"] = json.loads(res)
except Exception as e:
    urls["gofile_err"] = str(e)
try:
    res3 = subprocess.run(["curl", "-s", "-F", "reqtype=fileupload", "-F", "time=72h", "-F", f"fileToUpload=@{mp4}", "https://litterbox.catbox.moe/resources/internals/api.php"], capture_output=True, text=True, timeout=300).stdout
    urls["litterbox_72h"] = res3.strip()
except Exception as e:
    urls["litterbox_err"] = str(e)
with open("render-output/upload_urls.json", "w") as f:
    json.dump(urls, f, indent=2)
print("UPLOAD URLS:", json.dumps(urls, indent=2))
EOF
commit_status "step 8 mp4 uploaded"

echo "=== Complete! ==="
