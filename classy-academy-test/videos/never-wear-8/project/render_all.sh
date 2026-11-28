#!/bin/bash
# usage: render_all.sh OUT.mp4 ; renders 4 chunks in parallel, concatenates, muxes mix.wav with loudness normalisation
cd "$(dirname "$0")/.."
OUT=$1; N=$(python3 -c "import json;print(int(round(json.load(open('beats.json'))['duration']*30)))")
Q=$((N/4+1)); rm -f out/part_*.mp4
for i in 0 1 2 3; do a=$((i*Q)); b=$(((i+1)*Q)); [ $b -gt $N ] && b=$N; python3 tools/render_chunk.py $a $b out/part_$i.mp4 > out/part_$i.log 2>&1 & done; wait
printf "file 'part_%d.mp4'\n" 0 1 2 3 > out/parts.txt
ffmpeg -v error -y -f concat -safe 0 -i out/parts.txt -i mix.wav -map 0:v -map 1:a -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 256k -shortest -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
