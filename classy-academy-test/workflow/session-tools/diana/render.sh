#!/bin/bash
cd "$(dirname "$0")"
export HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell
export HF_SEGMENTED_CAPTURE=true
npx hyperframes render -o out/diana_v1.mp4 --workers 4 --quality delivery --resume > render.log 2>&1
echo "EXIT $?" >> render.log
