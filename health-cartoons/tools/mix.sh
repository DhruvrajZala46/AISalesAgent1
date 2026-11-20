#!/usr/bin/env bash
# Final mix (from the video folder): voice on top, music bed ~14 dB under it, SFX on top, mastered to about -10 LUFS
# (the reference channel's YouTube uploads measure -8.7 to -10.2 LUFS). Usage: bash ../../tools/mix.sh [video.mp4] [final.mp4] [seconds]
set -e
VID=${1:-video.mp4}; OUT=${2:-final.mp4}; DUR=${3:-}
LIM=${LIM:-0.75}   # limiter ceiling; lower it (e.g. LIM=0.72) if the true peak measures above -1 dB
T=""; [ -n "$DUR" ] && T="-t $DUR"
ffmpeg -v error -y -i voice.wav -i music.wav -i sfx.wav -filter_complex "[0]volume=2.4dB[v];[1]volume=-9.8dB[m];[2]volume=-2dB[s];[v][m][s]amix=inputs=3:normalize=0[a]" -map "[a]" $T -c:a pcm_s16le mixraw.wav
# master: gentle bus compression, +5 dB, limiter at 0.75 -> about -10.3 LUFS, true peak about -0.4 dB (reference: -8.7 to -10.2)
ffmpeg -v error -y -i mixraw.wav -af "acompressor=threshold=-24dB:ratio=4:attack=3:release=60:makeup=6,volume=5dB,alimiter=limit=$LIM:attack=5:release=50:level=false,aresample=48000" -c:a pcm_s16le mix.wav
ffmpeg -v error -y -i "$VID" -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest "$OUT"
ffmpeg -i "$OUT" -af ebur128=framelog=quiet -f null - 2>&1 | grep -E "^\s+I:"   # target about -10 LUFS
