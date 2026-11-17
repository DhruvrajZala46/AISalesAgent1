# proc.py - one table of every video the searches found; the charm/presence lane (women's and gender-neutral);
# three view tiers (1M+ all, 100k-1M sample, 2k-100k sample); thumbnails downloaded
import json, glob, re, os, random, urllib.request
from concurrent.futures import ThreadPoolExecutor
V = {}
for f in sorted(glob.glob('s/*.json')):
    q = os.path.basename(f)[:-5]
    try: ents = json.load(open(f)).get('entries') or []
    except Exception: continue
    for e in ents:
        if not e or not e.get('id') or e.get('view_count') is None: continue
        v = V.setdefault(e['id'], dict(id=e['id'], title=e.get('title') or '', views=int(e['view_count']), channel=e.get('channel') or '',
                                       cid=e.get('channel_id') or '', dur=int(float(e.get('duration') or 0)), q=[]))
        v['q'].append(q)
TOP = re.compile(r"charm|unforgettable|magnetic|charisma|attractive|likeable|likable|presence|\baura\b|captivat|irresistib|mesmeri|alluring|classy|\bclass\b|elegan|feminin|\blad(y|ies)\b|ladylike|graceful|\bpoise|sophisticat|mysterious|confident|confidence|respect|first impression|interesting|memorable|admire|high[- ]value|etiquette|manners|leave a lasting|people like you|people love you|draws people|magnet", re.I)
WOM = re.compile(r"\bwom[ae]n\b|\bfeminin|\blad(y|ies)\b|\bgirls?\b|\bshe\b|\bher\b|classy|elegan|high[- ]value woman|ladylike|\bqueen|princess|audrey|grace kelly|diana|french wom", re.I)
OFF = re.compile(r"official (music )?video|lyric|\bsong\b|\bmusic\b|\blive\b\)|cover\b|amazing grace|worship|hillsong|sermon|bishop|church|\bgod\b|jesus|prayer|blackpink|kpop|k-pop|anime|minecraft|roblox|sims|movie|trailer|episode|\bep\.? ?\d|netflix|\bmen\b|\bman\b|men's|\bguys?\b|\bhim\b|\bhis\b|boyfriend|husband|she likes you|women (find|love|want)|attract women|flirt|dating|\bdate\b|seduc|ryan gosling|keanu|dimple|\bmakeup\b|skincare|workout|diet|hair|outfit|wear\b|wardrobe|fashion|dress|shoes|recipe|cook|\bdog\b|\bcat\b|interview|reaction|podcast|\be\d{2,4}\b|full episode|\|\s*ep|ladylike$|• ladylike|᛫ ladylike|beauty roulette|hypnosis|affirmation|meditat|sadhguru|wealth|money|manifest|law of attraction|facial|\bface\b|jaw|looksmax|photoshop|foundation|period|shaving|ted-?x?\b|tedx|snl|saturday night", re.I)
for v in V.values():
    t = v['title']; v['top'] = bool(TOP.search(t)); v['wom'] = bool(WOM.search(t)); v['off'] = bool(OFF.search(t))
    v['asc'] = sum(ord(c) < 128 for c in t) / max(1, len(t)) > 0.85
    v['lane'] = v['top'] and not v['off'] and v['asc'] and 150 <= v['dur'] <= 3600 and v['channel'] not in ('BuzzFeedVideo',)
allv = list(V.values()); lane = [v for v in allv if v['lane']]
print('videos', len(allv), '| lane', len(lane), '| women-worded', sum(v['wom'] for v in lane))
win = sorted([v for v in lane if v['views'] >= 1_000_000], key=lambda v: -v['views'])
mid = [v for v in lane if 100_000 <= v['views'] < 1_000_000]; low = [v for v in lane if 2_000 <= v['views'] < 100_000]
random.seed(21); mids = sorted(random.sample(mid, min(100, len(mid))), key=lambda v: -v['views'])
random.seed(22); lows = sorted(random.sample(low, min(130, len(low))), key=lambda v: -v['views'])
print('1M+', len(win), f"(women-worded {sum(v['wom'] for v in win)}) | 100k-1M", len(mid), 'sampled', len(mids), '| 2k-100k', len(low), 'sampled', len(lows),
      '| 5M+', sum(v['views'] >= 5e6 for v in win), '| 10M+', sum(v['views'] >= 1e7 for v in win), '| channels among winners', len({v['cid'] for v in win}))
json.dump(dict(all=allv, lane=lane, win=win, mids=mids, lows=lows), open('table.json', 'w'))
os.makedirs('img', exist_ok=True)
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
for v in win: print(f"{v['views']/1e6:6.1f}M | {v['dur']//60:3d}m | {'W' if v['wom'] else '-'} | {v['channel'][:22]:22} | {v['title'][:84]}")
