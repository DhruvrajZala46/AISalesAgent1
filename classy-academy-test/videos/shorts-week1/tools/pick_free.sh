#!/usr/bin/env bash
# pick_free.sh <rise_s> <dur_s> -> a music window that overlaps no window in used_music.txt (each used window blocks start-25..start+25)
rise=$1; dur=$2; ex=""
for w in $(cat used_music.txt); do m=${w%@*}; s=${w#*@}; for t in $(python3 -c "s=float('$s'); import numpy as np; print(' '.join(str(x) for x in np.arange(max(0,s-25),s+25.5,0.5)))"); do ex="$ex $m@$t"; done; done
python3 pick_music.py $rise $dur $ex 2>&1 | tail -1
