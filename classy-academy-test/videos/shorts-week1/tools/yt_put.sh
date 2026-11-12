#!/usr/bin/env bash
# yt_put.sh <video.mp4> <upload-slot-url> - step 2 of posting a Short (see ../POSTING.md).
# Step 1 is a Zapier YouTube "API Request" (mutating, POST
# https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status with the title,
# description, tags and status JSON). Its `location` header is a private upload slot on the channel. This sends
# the rendered file into that slot, straight to YouTube: nothing public in between, no re-encode.
# Prints: video id | title | publishAt | privacy.
set -euo pipefail
f="${1:?usage: yt_put.sh <video.mp4> <upload-slot-url>}"
u="${2:?missing the upload-slot url (the location header from step 1)}"
case "$u" in
  https://www.googleapis.com/upload/youtube/v3/videos\?*upload_id=*) ;;
  *) echo "refused: not a YouTube upload slot url" >&2; exit 2 ;;
esac
[ -s "$f" ] || { echo "missing file: $f" >&2; exit 2; }
curl -sS --fail-with-body -X PUT -H "Content-Type: video/mp4" --data-binary @"$f" "$u" |
  python3 -c 'import json,sys; d=json.load(sys.stdin); s=d.get("status",{}); print(d.get("id"), "|", d.get("snippet",{}).get("title"), "|", s.get("publishAt"), "|", s.get("privacyStatus"))'
