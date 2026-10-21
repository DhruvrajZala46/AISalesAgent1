# The proof table for concept K1: every 500k+ in-niche video, with domain, channel size, channel median (latest 60 long uploads), multiple, likes, approx year.
import json, glob, os, re, statistics as st
k = json.load(open('kfam.json')); L = json.load(open('likes_k.json')); D = json.load(open('../deep/dataset.json'))
med, subs, name = {}, {}, {}
for cid, c in D['channels'].items(): med[cid], subs[cid], name[cid] = c['median'], c['subs'], c['name']
for f in glob.glob('ch/*.json'):
    cid = os.path.basename(f)[:-5]
    try: d = json.load(open(f))
    except Exception: continue
    v = [e['view_count'] for e in d.get('entries') or [] if e and e.get('view_count') is not None and (e.get('duration') or 0) >= 180]
    med[cid] = st.median(v) if len(v) >= 4 else None; subs[cid] = d.get('channel_follower_count'); name[cid] = d.get('channel')
def dom(t):
    if re.search(r"skin|doctor|dr\.|yoga|facial|filler|procedure|anti.?ageing habits|stay young|fit forever|stoic|philosophy|baby face|we tried", t, re.I): return 'other (skin/health/novelty)'
    if re.search(r"make.?up|eyeliner|lipstick|brow|contour|lash", t, re.I): return 'makeup'
    if re.search(r"hair|pixie|bob\b|haircut", t, re.I): return 'hair'
    return 'clothes / style'
rows = []
for r in k['K1 look older / younger']['top']:
    cid = r['channel_id']; l = L.get(r['id'], {})
    m = med.get(cid); lv = l.get('viewCount') or r['views']
    rows.append(dict(id=r['id'], url='https://youtu.be/' + r['id'], title=r['title'], channel=r['channel'], subs=subs.get(cid), channel_median_now=m,
                     views=r['views'], multiple=round(r['views'] / m, 1) if m else None, likes=l.get('likes'), likes_per_1k=round(1000 * l['likes'] / lv, 1) if l.get('likes') and lv else None,
                     year_approx=r['year_approx'], domain=dom(r['title'])))
json.dump(rows, open('k1_table.json', 'w'), ensure_ascii=False, indent=1)
from collections import Counter
for d in ['clothes / style', 'makeup', 'hair', 'other (skin/health/novelty)']:
    x = [r for r in rows if r['domain'] == d]; x1 = [r for r in x if r['views'] >= 1e6]
    print(f"\n### {d}: {len(x)} videos >=500k from {len({r['channel'] for r in x})} channels; >=1M: {len(x1)} from {len({r['channel'] for r in x1})} channels; years {sorted({r['year_approx'] for r in x if r['year_approx']})}")
    for r in sorted(x, key=lambda r: -r['views']):
        print(f"  {r['views']/1e6:5.2f}M {str(r['year_approx']):4} subs={r['subs'] or '?':>8} med={int(r['channel_median_now'] or 0):>8} x={r['multiple'] or '?':>5} likes={r['likes'] or '?':>7} ({r['likes_per_1k']}/1k) {r['channel'][:22]:22} | {r['title'][:70]}")
