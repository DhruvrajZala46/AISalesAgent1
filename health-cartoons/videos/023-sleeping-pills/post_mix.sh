#!/usr/bin/env bash
# 023: after ../../tools/mix.sh, lay the brawl SFX (brawl.wav) on top of the mastered mix, as loud as in the reference
# (brawl about 4.6 dB above the median level, peaks about 9 dB above). Usage: BG=<dB> bash post_mix.sh video.mp4 final.mp4
set -e
BG=${BG:-0}
ffmpeg -v error -y -i mix.wav -i brawl.wav -filter_complex "[1]aresample=48000,volume=${BG}dB[b];[0][b]amix=inputs=2:normalize=0,alimiter=limit=0.88:level=false[a]" -map "[a]" -c:a pcm_s16le mix2.wav
ffmpeg -v error -y -i "$1" -i mix2.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest "$2"
