#!/usr/bin/env bash
# upload_temp.sh <video.mp4> - put one rendered Short on litterbox.catbox.moe for 12 hours and print its URL,
# so the YouTube uploader (Zapier) can fetch it. The user approved this host on 12 Nov 2026 (option A,
# "fully automatic"). Only .mp4 files from the scratchpad Shorts work folder are accepted.
set -euo pipefail
f="${1:?usage: upload_temp.sh <video.mp4>}"
case "$f" in
  /tmp/claude-0/*/scratchpad/short-b1/out/*.mp4) ;;
  *) echo "refused: only rendered Shorts in the scratchpad out/ folder" >&2; exit 2 ;;
esac
[ -s "$f" ] || { echo "missing file: $f" >&2; exit 2; }
url=$(curl -sS --fail -F "reqtype=fileupload" -F "time=12h" -F "fileToUpload=@$f" \
      https://litterbox.catbox.moe/resources/internals/api.php)
case "$url" in https://litter.catbox.moe/*) echo "$url" ;; *) echo "upload failed: $url" >&2; exit 1 ;; esac
