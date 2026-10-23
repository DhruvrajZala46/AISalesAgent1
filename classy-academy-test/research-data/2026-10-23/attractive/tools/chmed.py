# chmed.py: per-channel subscribers and median views of the latest <=60 long uploads, from every channel listing collected.
import json, glob, os, statistics as st
out = {}
for d in ['../proven/ch', '../deep/track/ch', '../idea/ch', '../idea19/ch', '../idea20/ch', '../thumb/ch', 'ch']:
    for f in glob.glob(d + '/*.json'):
        cid = os.path.basename(f)[:-5]
        try: j = json.load(open(f))
        except Exception: continue
        ents = [e for e in (j.get('entries') or []) if e and e.get('view_count') is not None and (e.get('duration') or 999) >= 180]
        if len(ents) < 4: continue
        x = dict(subs=j.get('channel_follower_count'), median=st.median([e['view_count'] for e in ents]), n=len(ents), name=j.get('channel') or j.get('title'), src=d)
        if cid not in out or d == 'ch': out[cid] = x
dsc = json.load(open('../deep/dataset.json'))['channels']
for cid, c in dsc.items():
    if cid not in out and c.get('median'): out[cid] = dict(subs=c.get('subs'), median=c['median'], n=c.get('n'), name=c.get('name'), src='dataset')
json.dump(out, open('chmed.json', 'w'), ensure_ascii=False); print(len(out), 'channels with a median')
