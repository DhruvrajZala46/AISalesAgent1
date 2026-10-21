#!/bin/bash
# compile the real picks, fill the not-yet-sourced ones with placeholders (layout tests only), build the timeline
cd "$(dirname "$0")/.." && python3 -I tools/compile_picks.py | cut -c1-90 && python3 - <<'PY'
import json
p = json.load(open('project/picks.json')); ph = json.load(open('test/picks_placeholder.json'))
for b in json.load(open('plan/briefs.json')):
    if b['id'] not in p: p[b['id']] = ph.get(b['id'], ph['H05'])
json.dump(p, open('project/picks.json', 'w'), indent=1)
PY
python3 -I project/build_timeline.py 2>&1 | grep -v hairvid | tail -6
