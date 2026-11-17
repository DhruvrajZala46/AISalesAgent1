#!/bin/bash
# resume the render until it finishes (a stall exits 1; --resume keeps finished segments), at most 6 tries
cd "$(dirname "$0")"
for n in 1 2 3 4 5 6; do
  ./render.sh
  grep -q "EXIT 0" render.log && { echo "DONE after try $n"; exit 0; }
  echo "try $n stalled: $(tr '\r' '\n' < render.log | grep -o 'stuck at frame [0-9/]*' | tail -1)"
done
exit 1
