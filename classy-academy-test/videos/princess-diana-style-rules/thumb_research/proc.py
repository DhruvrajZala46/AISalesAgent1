# proc.py - every video the searches found; lanes: DIANA (any Diana video), STYLE (fashion / style / outfit / dress / wear / elegance worded),
# tiers by views; thumbnails downloaded for winners and samples
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
DI = re.compile(r"\bdiana\b|lady di\b|princess of wales|people's princess", re.I)
ST = re.compile(r"fashion|style|styl|outfit|dress|wear|wore|wardrobe|clothes|look[s ]|gown|elegan|classy|chic|jewel|tiara|handbag|\bbag\b|hair|beauty|icon", re.I)
ROY = re.compile(r"royal|queen|kate middleton|princess|meghan|duchess|audrey|grace kelly|jackie|bessette|old money|elegant|classy|timeless|style icon", re.I)
KID = re.compile(r"kids|roma\b|nastya|toys|pretend|sofia little|rebecca zamolo|say yes to the dress|tlc|yuecubed|dirty diana|devitt|future, metro|liambrandon|getting dressed|saree|murder", re.I)
OFF = re.compile(r"official (music )?video|lyric|\bsong\b|\bmusic\b|trailer|the crown|spencer|netflix|musical|cover\b|tribute song|candle in the wind|asmr|roblox|sims|minecraft|doll|barbie|drawing|makeup tutorial|transform", re.I)
for v in V.values():
    t = v['title']; v['di'] = bool(DI.search(t)); v['st'] = bool(ST.search(t)); v['roy'] = bool(ROY.search(t)); v['off'] = bool(OFF.search(t))
    v['asc'] = sum(ord(c) < 128 for c in t) / max(1, len(t)) > 0.85; v['long'] = v['dur'] >= 150
allv = [v for v in V.values() if v['asc'] and v['long'] and not v['off'] and not KID.search(v['channel'] + ' ' + v['title'])]
dia = [v for v in allv if v['di']]; dst = [v for v in dia if v['st']]; rst = [v for v in allv if v['st'] and v['roy'] and not v['di']]
fmt = lambda n: f'{n/1e6:.1f}M' if n >= 1e6 else f'{n/1e3:.0f}k'
def tiers(vs): return {k: sum(lo <= v['views'] < hi for v in vs) for k, lo, hi in (('10M+', 1e7, 1e12), ('5-10M', 5e6, 1e7), ('1-5M', 1e6, 5e6), ('100k-1M', 1e5, 1e6), ('10k-100k', 1e4, 1e5), ('<10k', 0, 1e4))}
print('all found', len(V), '| long, english, on-topic', len(allv)); print('Diana (any topic)', len(dia), tiers(dia)); print('Diana style', len(dst), tiers(dst)); print('other royal / icon style', len(rst), tiers(rst))
key = lambda v: -v['views']
dia_win = sorted([v for v in dia if v['views'] >= 2e6], key=key)
dst_win = sorted([v for v in dst if v['views'] >= 3e5], key=key)
rst_win = sorted([v for v in rst if v['views'] >= 1e6], key=key)
random.seed(5); lowp = [v for v in dst if 2000 <= v['views'] < 50000]; dst_low = sorted(random.sample(lowp, min(60, len(lowp))), key=key)
midp = [v for v in dst if 50000 <= v['views'] < 300000]; random.seed(6); dst_mid = sorted(random.sample(midp, min(40, len(midp))), key=key)
T = dict(DW=dia_win, SW=dst_win, RW=rst_win, SM=dst_mid, SL=dst_low)
json.dump(dict(all=allv, **T), open('table.json', 'w'))
def get(v):
    f = f"img/{v['id']}.jpg"
    if os.path.exists(f) and os.path.getsize(f) > 2000: return 1
    for name in ('maxresdefault', 'hq720', 'mqdefault', 'hqdefault'):
        try:
            b = urllib.request.urlopen(urllib.request.Request(f"https://i.ytimg.com/vi/{v['id']}/{name}.jpg", headers={'User-Agent': 'Mozilla/5.0'}), timeout=20).read()
            if len(b) > 5000: open(f, 'wb').write(b); return 1
        except Exception: pass
    return 0
ids = {v['id']: v for k in T for v in T[k]}
with ThreadPoolExecutor(8) as ex: ok = sum(ex.map(get, ids.values()))
print('thumbnails', ok, 'of', len(ids), {k: len(T[k]) for k in T})
for name, vs in (('DIANA 2M+ (any topic)', dia_win), ('DIANA STYLE 300k+', dst_win), ('OTHER ROYAL / ICON STYLE 1M+', rst_win)):
    print('\n' + name)
    for v in vs[:45]: print(f"{fmt(v['views']):>7} | {v['dur']//60:3d}m | {v['channel'][:24]:24} | {v['title'][:95]}")
