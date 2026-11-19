#!/bin/bash
cd "$(dirname "$0")"
RESUME= ./render.sh
grep -q "EXIT 0" render.log && { echo "DONE after try 1"; exit 0; }
for n in 2 3 4 5 6; do
  RESUME=--resume ./render.sh
  grep -q "EXIT 0" render.log && { echo "DONE after try $n"; exit 0; }
  echo "try $n stalled"
done
exit 1
