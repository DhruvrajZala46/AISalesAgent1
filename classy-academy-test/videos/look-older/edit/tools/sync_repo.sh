#!/bin/bash
# sync_repo.sh : copies the text files of the editable project (never media) into the repo, videos/look-older/
set -e
L="$(cd "$(dirname "$0")/.." && pwd)"; R=/home/user/AISalesAgent1/classy-academy-test/videos/look-older
cd "$L" && python3 -I project/records.py >/dev/null
mkdir -p "$R/edit/project/tools" "$R/edit/tools" "$R/edit/plan" "$R/edit/picks"
cp project/*.py project/*.json project/README.txt "$R/edit/project/"
cp project/tools/*.py "$R/edit/project/tools/"
cp tools/*.py tools/*.sh "$R/edit/tools/"
cp plan/briefs.json plan/SOURCING-BRIEF.md plan/ig_verify.jsonl "$R/edit/plan/"
rm -f "$R/edit/picks/"*.json
python3 -c "
import json
tl=json.load(open('project/timeline.json'))
print(' '.join(sorted({m['asset'] for sg in tl['segments'] for m in sg.get('shots',[])+sg.get('panels',[])})))" | tr ' ' '\n' | while read a; do cp "picks/$a.json" "$R/edit/picks/"; done
cp out/SOURCES-LOG.md out/CREDITS.txt out/SCRIPT-TO-VISUAL-MAP.md "$R/"
cp project/README.txt "$R/edit/README.txt"
du -sh "$R/edit"; ls "$R"
