# Strict in-niche concept sets from every search pool collected (concept sweep, focused sweep, 20 Oct sweep, 20 Oct angle searches).
import json, re
from collections import defaultdict
pool = {}
def add(r, year=None, src=''):
    if not r.get('id') or not r.get('views'): return
    x = pool.setdefault(r['id'], dict(id=r['id'], title=r.get('title') or '', channel=r.get('channel'), channel_id=r.get('channel_id'), views=r['views'], duration=r.get('duration'), year_approx=year, src=set()))
    x['views'] = max(x['views'], r['views']); x['src'].add(src)
    if year and not x['year_approx']: x['year_approx'] = year
for f in ('csweep.json', 'ksweep.json'):
    for b in json.load(open(f)).values():
        for r in b['rows']: add(r, r.get('year_approx'), f)
D = '../deep/'
for b in json.load(open(D + 'sweep.json')).values():
    for r in b['rows']: add(r, None, 'sweep20oct')
for v in json.load(open(D + 'angle_search.json')).values():
    if v != 'ERR':
        for r in v: add(r, None, 'angle20oct')
ds = json.load(open(D + 'dataset.json'))
for r in ds['rows']:
    add(dict(id=r['id'], title=r['title'], channel=r['channel'], channel_id=r['channel_id'], views=r['views'], duration=r['duration']), int(r['date'][:4]) if r.get('date') else None, 'dataset')
print(len(pool), 'unique videos in the pool')
STYLE = re.compile(r"fashion|style|styling|outfit|clothes|clothing|\bwear|dress|wardrobe|make.?up|\bhair|haircut|jeans|shoes|accessor|jewel|glasses|lipstick|eyeliner|\bbrows?\b|colou?r|look (expensive|rich|classy|elegant|younger|older)|elegan|classy|chic", re.I)
OFF = re.compile(r"skin ?care|wrinkle|face yoga|massage|\bmask\b|supplement|collagen|diet|exercise|workout|vap(e|ing)|tai chi|qi gong|banana|cream|serum|botox|surgery|\bkids?\b|song|playlist|\bcar\b|kitchen|\bhome\b|bedroom|interior|decor|minecraft|\bmen\b|\bman\b|\bguys?\b|gentle(man|men)|masculine|beard|\bmale\b|older guys|did people used", re.I)
K = {
 'K1 look older / younger': r"look(s|ing)? older|look(s|ing)? old\b|\bages? you\b|aging you|ageing you|\bage you\b|add(s|ing)? (\d+ |ten )?years|old lady|years older|instantly age|(look|dress|style).{0,25}younger|years younger|youthful",
 'K2 look expensive / classy / rich': r"look(s|ing)? (more |so |always |instantly |extra )?(expensive|rich|wealthy|classy|elegant|luxurious|high.?end|sophisticated|like a million)|expensive.?looking|look like money",
 'K3 styling mistakes (not age)': r"mistake|make your outfits better|outfits better",
 'K4 elegant / classy habits & identity': r"habits?|how to be (elegant|classy|a lady|ladylike)|classy (women|woman|lady|ladies)|elegant (women|woman|lady|ladies)|things classy|signs (you|of)",
 'K5 capsule / minimalist wardrobe': r"capsule|minimalist wardrobe|wardrobe essentials|wardrobe staples|timeless wardrobe",
 'K6 never wear / stop wearing / what not to wear': r"never wear|stop wearing|don.?t wear|should(n.?t| never) wear|what not to wear|not to wear",
}
res = {}
for k, rx in K.items():
    rx = re.compile(rx, re.I)
    v = [r for r in pool.values() if rx.search(r['title']) and STYLE.search(r['title']) and not OFF.search(r['title']) and (r['duration'] or 0) >= 180]
    if k.startswith('K3'): v = [r for r in v if not re.search(K['K1 look older / younger'], r['title'], re.I)]
    m1 = sorted([r for r in v if r['views'] >= 1e6], key=lambda r: -r['views']); m5 = [r for r in v if r['views'] >= 5e5]
    res[k] = dict(n=len(v), n1M=len(m1), ch1M=len({r['channel_id'] for r in m1}), n500k=len(m5), ch500k=len({r['channel_id'] for r in m5}),
                  years1M=sorted({r['year_approx'] for r in m1 if r['year_approx']}), top=[{**r, 'src': sorted(r['src'])} for r in sorted(m5, key=lambda r: -r['views'])])
    print(f"\n=== {k}: {len(v)} on-concept long videos | >=1M: {len(m1)} videos from {res[k]['ch1M']} channels | >=500k: {len(m5)} from {res[k]['ch500k']} channels | years with 1M+: {res[k]['years1M']}")
    for r in m1[:40]: print(f"   {r['views']/1e6:5.2f}M {r['year_approx']} {(r['channel'] or '')[:26]:26} | {r['title'][:82]}")
json.dump(res, open('kfam.json', 'w'), ensure_ascii=False, indent=0, default=list)
