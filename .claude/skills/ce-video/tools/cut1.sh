#!/bin/bash
# Cut one source clip into a 720x1280 30fps segment for the edit.
#   cut1.sh <name> <dl/x|pinv/x> <start-seconds> [length]
# Run from the video work dir: sources are read from ./dl and ./pinv, output goes to ./assets/<name>.mp4
n=$1; src=$2; ss=$3; len=${4:-11}
f=./${src}.mp4
ffmpeg -nostdin -v error -y -ss $ss -i $f -t $len -an -vf "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,fps=30" -c:v libx264 -preset veryfast -crf 16 -pix_fmt yuv420p ./assets/$n.mp4 || echo FAIL $n
