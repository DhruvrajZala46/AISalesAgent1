#!/usr/bin/env bash
# Final mix (from the video folder): voice -14 LUFS, music bed ~-26 LUFS, SFX on top; output final.mp4
set -e
ffmpeg -v error -y -i voice.wav -i music.wav -i sfx.wav -filter_complex "[0]volume=2.4dB[v];[1]volume=-9.8dB[m];[2]volume=-2dB[s];[v][m][s]amix=inputs=3:normalize=0,alimiter=limit=0.95,aresample=48000[a]" -map "[a]" -c:a pcm_s16le mix.wav
ffmpeg -v error -y -i video.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest final.mp4
ffmpeg -i final.mp4 -af ebur128=framelog=quiet -f null - 2>&1 | grep -E "^\s+I:"   # target about -14 LUFS
