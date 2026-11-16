# proc.py - one table of every video found by the searches; the lane; winners, middle, a random low-view sample; thumbnails
import json, glob, re, os, random, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
V = {}
for f in sorted(glob.glob('s/*.json')):
    q = os.path.basename(f)[:-5]
    try: ents = json.load(open(f)).get('entries') or []
    except Exception: continue
    for e in ents:
        if not e or not e.get('id') or e.get('view_count') is None: continue
        v = V.setdefault(e['id'], dict(id=e['id'], title=e.get('title') or '', views=int(e['view_count']), channel=e.get('channel') or '', cid=e.get('channel_id') or '',
                                       dur=int(float(e.get('duration') or 0)), q=[]))
        v['q'].append(q)
FR = re.compile(r'\bfrench\b|parisian|parisienne|\bparis\b|fran[cç]aise', re.I)
WI = re.compile(r'winter|cold[- ]weather|\bcoat|layering|\blayer\b|fall[ /&-]+winter|autumn[ /&-]+winter|\bfw\b', re.I)
ES = re.compile(r'essential|capsule|must[- ]?have|\bbasics?\b|staples?|timeless|classic pieces|every woman|wardrobe|closet|pieces you|items you|clothes you need|only \d+', re.I)
ST = re.compile(r'style|styl|wear|outfit|wardrobe|dress|fashion|clothes|clothing|chic|elegan|classy|look |looks|coat|capsule|essential|closet|\bfit\b', re.I)
OFF = re.compile(r"\bmen\b|men's|\bmens\b|\bguys?\b|\bboys?\b|\bkids?\b|baby|toddler|husband|boyfriend|decor|\bhome\b|house|apartment|haul|vlog|makeup|make-up|skincare|skin care|\bhair|nail|recipe|cook|\bcar\b|camping|travel|packing|pack with|pregnan|maternity|sims|roblox|barbie|doll|diy|sew|knit|crochet|lyrics|song|trailer|movie|film|series|emily in paris|olympic|language|learn french|pronounc|lesson|grammar|bulldog|dog|cat\b|kitchen|garden|workout|diet|weight|museum|tour|food|restaurant|hotel|street interview|what are people wearing|asmr|podcast|news|war\b|army|soldier|hiking|ski\b|skiing|snowboard|running|gym", re.I)
for v in V.values():
    t = v['title']; v['fr'] = bool(FR.search(t)); v['wi'] = bool(WI.search(t)); v['es'] = bool(ES.search(t)); v['st'] = bool(ST.search(t))
    v['off'] = bool(OFF.search(t)); v['short'] = bool(v['dur'] and v['dur'] < 62)
    v['asc'] = sum(ord(c) < 128 for c in t) / max(1, len(t)) > 0.85
    v['lane'] = (not v['off']) and (not v['short']) and v['st'] and v['asc'] and (v['fr'] or v['wi'] or v['es']) and v['dur'] >= 150
allv = list(V.values()); lane = [v for v in allv if v['lane']]
print('videos', len(allv), '| lane', len(lane), '| french', sum(v['fr'] for v in lane), 'winter', sum(v['wi'] for v in lane), 'essentials', sum(v['es'] for v in lane))
win = sorted([v for v in lane if v['views'] >= 1_000_000], key=lambda v: -v['views'])
mid = sorted([v for v in lane if 100_000 <= v['views'] < 1_000_000], key=lambda v: -v['views'])
low = [v for v in lane if 2_000 <= v['views'] < 100_000]
random.seed(11); lows = sorted(random.sample(low, min(120, len(low))), key=lambda v: -v['views'])
random.seed(12); mids = sorted(random.sample(mid, min(80, len(mid))), key=lambda v: -v['views'])
print('1M+', len(win), '| 100k-1M', len(mid), 'sampled', len(mids), '| 2k-100k', len(low), 'sampled', len(lows), '| 5M+', sum(v['views'] >= 5e6 for v in win), '| 10M+', sum(v['views'] >= 1e7 for v in win),
      '| channels among winners', len({v['cid'] for v in win}))
for name, key in (('french', 'fr'), ('winter', 'wi'), ('essentials', 'es')):
    print(f"  {name}: 1M+ {sum(v[key] for v in win)}, 100k-1M {sum(v[key] for v in mid)}, 2k-100k {sum(v[key] for v in low)}")
json.dump(dict(all=allv, lane=lane, win=win, mids=mids, lows=lows), open('table.json', 'w'))
json.dump([dict(cid=v['cid']) for v in win], open('top.json', 'w'))
def get(v):
    f = f"img/{v['id']}.jpg"
    if os.path.exists(f) and os.path.getsize(f) > 2000: return 1
    for name in ('maxresdefault', 'hq720', 'mqdefault', 'hqdefault'):
        try:
            b = urllib.request.urlopen(urllib.request.Request(f"https://i.ytimg.com/vi/{v['id']}/{name}.jpg", headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read()
            if len(b) > 5000: open(f, 'wb').write(b); return 1
        except Exception: pass
    return 0
with ThreadPoolExecutor(8) as ex: ok = sum(ex.map(get, win + mids + lows))
print('thumbnails', ok, 'of', len(win) + len(mids) + len(lows))
for v in win[:60]: print(f"{v['views']/1e6:6.1f}M | {v['dur']//60:2d}:{v['dur']%60:02d} | {'F' if v['fr'] else '-'}{'W' if v['wi'] else '-'}{'E' if v['es'] else '-'} | {v['channel'][:22]:22} | {v['title'][:84]}")
