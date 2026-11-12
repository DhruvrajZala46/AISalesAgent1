#!/usr/bin/env bash
# loudness-normalise a rendered Short to -14 LUFS (YouTube's playback level), video untouched
in="$1"; out="${in%.mp4}_final.mp4"
ffmpeg -nostdin -v error -y -i "$in" -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k -movflags +faststart "$out"
printf "%s  " "$(basename "$out")"; ffmpeg -nostdin -i "$out" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1
