#!/usr/bin/env bash
# Usage: tools/process_voice.sh <raw_dir> <proc_dir>
# Raw ElevenLabs mp3s must be named NN_role.mp3 (role = swab|wax|drum|doctor|patient|... see PLAYBOOK voice table).
# Cartoon roles are pitch-shifted (chipmunk-style, like the reference channel); the doctor is sped up 8%.
set -e
RAW=$1; OUT=$2; mkdir -p "$OUT"
for f in "$RAW"/*.mp3; do
  n=$(basename "$f" .mp3); role=${n#*_}
  case $role in
    swab|gum|noodle|burger|cartoonA) r=1.3348;;      # +5 semitones
    wax|stomach|palate|cartoonB)  r=1.0905;;      # +1.5 semitones
    drum|intestine|brain|cartoonC) r=1.1225;;      # +2 semitones
    *) r=1;;
  esac
  T=1; [ "$role" = doctor ] && T=1.08
  ff=$(python3 -c "print(round($T/$r,4))")
  ffmpeg -v error -y -i "$f" -af "asetrate=44100*$r,aresample=44100,atempo=$ff,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse" -ar 44100 -ac 1 "$OUT/$n.wav"
  echo "$n $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT/$n.wav")"
done
