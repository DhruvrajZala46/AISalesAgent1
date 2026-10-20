# Stage 2: channel medians for channels found by the sweep but not tracked. Latest 60 uploads, public flat listing, approximate dates.
import json, subprocess, os, sys, re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
N = int(sys.argv[1]) if len(sys.argv) > 1 else 150
sw = json.load(open('sweep.json'))
tracked = set(json.load(open('/home/user/AISalesAgent1/.claude/skills/content-idea/channels.json')))
OFF = re.compile(r"\bmen'?s\b|for men|\bmale\b|masculine|\bguys?\b|gentleman|\bhis\b", re.I)
hits, maxv, name = Counter(), Counter(), {}
for k, b in sw.items():
    for r in b['rows']:
        cid = r.get('channel_id')
        if not cid or cid in tracked or (r.get('duration') or 0) < 180 or OFF.search(r.get('title') or ''): continue
        hits[cid] += 1; maxv[cid] = max(maxv[cid], r.get('views') or 0); name[cid] = r.get('channel')
cands = sorted(hits, key=lambda c: (-hits[c], -maxv[c]))
pick = [c for c in cands if hits[c] >= 2][:N]
pick += [c for c in sorted(cands, key=lambda c: -maxv[c]) if c not in pick and maxv[c] >= 300000][:max(0, N + 40 - len(pick))]
print(len(cands), 'untracked channels in sweep;', len(pick), 'to collect', flush=True)
os.makedirs('xch', exist_ok=True)
def fetch(cid):
    f = f'xch/{cid}.json'
    if os.path.exists(f): return cid, True
    r = subprocess.run(['timeout', '180', 'yt-dlp', '--flat-playlist', '-J', '--playlist-end', '60', '--extractor-args', 'youtubetab:approximate_date', f'https://www.youtube.com/channel/{cid}/videos'], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip(): open(f, 'w').write(r.stdout); return cid, True
    return cid, False
done = 0
with ThreadPoolExecutor(4) as ex:
    for cid, ok in ex.map(fetch, pick):
        done += 1
        if done % 10 == 0: print(done, flush=True)
json.dump(dict(pick=pick, hits={c: hits[c] for c in pick}, name={c: name[c] for c in pick}), open('expand_pick.json', 'w'), ensure_ascii=False)
print('DONE')
