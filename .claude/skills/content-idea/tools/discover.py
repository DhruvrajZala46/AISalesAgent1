#!/usr/bin/env python3
"""discover.py - find niche channels that are NOT in channels.json yet.

    python3 discover.py OUT_DIR [--add 5] ["extra search query" ...]

Runs YouTube searches for the niche's core queries (public results, no login), counts which
channels keep showing up, and lists the ones channels.json does not have. --add N appends the top N
to channels.json. A channel only matters to the ranking if it has at least 4 long videos, which
collect.py checks next time it runs.
"""
import json, os, sys, subprocess
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); CH = os.path.join(HERE, '..', 'channels.json')
QUERIES = ['things elegant women never wear', 'how to look elegant', 'how to look expensive on a budget',
           'old money style women', 'quiet luxury style women', 'classy woman habits', 'how to be classy',
           'how to be more feminine and elegant', 'elegant fall outfits', 'elegant winter outfits',
           'elegant holiday party outfit', 'french chic style', 'style over 50 elegant']
a = sys.argv[1:]
out_dir = a[0] if a and not a[0].startswith('--') else '.'
add = int(a[a.index('--add') + 1]) if '--add' in a else 0
extra = [x for x in a[1:] if not x.startswith('--') and not x.isdigit()]
known = set(json.load(open(CH)))

seen, name, views = Counter(), {}, Counter()
for q in QUERIES + extra:
    r = subprocess.run(['yt-dlp', '--flat-playlist', '-J', f'ytsearch40:{q}'], capture_output=True, text=True)
    if r.returncode or not r.stdout.strip(): print('search failed:', q); continue
    for e in json.loads(r.stdout).get('entries') or []:
        cid = e.get('channel_id')
        if not cid or (e.get('duration') or 0) < 180: continue
        seen[cid] += 1; name[cid] = e.get('channel') or cid; views[cid] += e.get('view_count') or 0

new = [c for c, _ in seen.most_common() if c not in known]
print(f'{len(seen)} channels in results, {len(new)} not in channels.json\n')
for c in new[:20]:
    print(f'  {seen[c]:>2} hits  {views[c]//1000:>7}k views  {name[c][:32]:<32} {c}')
if add:
    json.dump(sorted(known) + new[:add], open(CH, 'w'), indent=0); print(f'\nadded {min(add, len(new))} to channels.json')
json.dump([dict(id=c, channel=name[c], hits=seen[c]) for c in new], open(os.path.join(out_dir, 'discovered.json'), 'w'), indent=1)
