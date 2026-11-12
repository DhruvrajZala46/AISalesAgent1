#!/usr/bin/env bash
# upload_temp.sh <video.mp4> - put one rendered Short on a temporary file host and print a direct download URL,
# so the YouTube uploader (Zapier) can fetch it. The user approved a temporary host on 12 Nov 2026 (option A,
# "fully automatic"). litterbox.catbox.moe refused uploads from this machine (HTTP 412), so this uses
# tmpfiles.org's public upload API (files are deleted after 60 minutes).
# Only .mp4 files from the scratchpad Shorts work folder are accepted.
set -euo pipefail
f="${1:?usage: upload_temp.sh <video.mp4>}"
case "$f" in
  /tmp/claude-0/*/scratchpad/short-b1/out/*.mp4) ;;
  *) echo "refused: only rendered Shorts in the scratchpad out/ folder" >&2; exit 2 ;;
esac
[ -s "$f" ] || { echo "missing file: $f" >&2; exit 2; }
resp=$(curl -sS --fail -F "file=@$f" https://tmpfiles.org/api/v1/upload)
url=$(printf '%s' "$resp" | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["url"])')
case "$url" in
  http*://tmpfiles.org/*) echo "${url/tmpfiles.org\//tmpfiles.org/dl/}" | sed 's#^http://#https://#' ;;
  *) echo "upload failed: $resp" >&2; exit 1 ;;
esac
