# c1.py: strict on-concept set for "become more attractive / prettier / more beautiful" (women or general audience), with sub-groups.
import json, re
S = '/tmp/claude-0/-home-user-AISalesAgent1/73fc3aa5-807d-530d-b865-5c7bcc671679/scratchpad/'
pool = json.load(open('pool.json'))
for f, tag in (('sweep4.json', 'sweep4'), ('sweep4_year.json', 'sweep4_year')):
    try: data = json.load(open(f))
    except Exception: continue
    for b in data.values():
        for r in b['rows']:
            if not r.get('id') or not r.get('views'): continue
            x = pool.setdefault(r['id'], dict(id=r['id'], title=r.get('title') or '', channel=r.get('channel'), channel_id=r.get('channel_id'), views=r['views'], duration=r.get('duration'), year_approx=r.get('year_approx'), src=[]))
            x['views'] = max(x['views'], r['views']); x['src'] = sorted(set(x['src']) | {tag})
            if r.get('year_approx') and not x.get('year_approx'): x['year_approx'] = r['year_approx']
PROMISE = re.compile(r"more attractive|instantly attractive|(be|become|look|looking|get|appear|feel)( so| more| instantly| extra| naturally| effortlessly)? (attractive|prettier|pretty|beautiful|gorgeous|stunning|irresistibl\w*)\b|prettier|glow.?up|average to attractive|wildly attractive|irresistibly attractive|attractive (woman|women|girl)|what makes (a )?(woman|women|girl) attractive|ways to (be|look) (attractive|beautiful|pretty)|look(s|ing)? (better|good) without make.?up|naturally (pretty|beautiful)|without make.?up", re.I)
SIGNS = re.compile(r"signs? (you|you're|you are|that you)", re.I)
TEEN = re.compile(r"school|teen|strict parents|college girls|high school|student", re.I)
MEN = re.compile(r"\bmen\b|\bman\b|\bguys?\b|masculine|gentlem|looksmax|\bmale\b|\bboys?\b|\bhis\b|beard|for him|muscle", re.I)
JUNK = re.compile(r"sit still,? look pretty|lyric|song|official (video|audio|music)|cover by|acoustic|playlist|helldivers|warhammer|darktide|game|animated|story ?time|subliminal|affirmation|hypnosis|meditation|surgery|botox|skin lightening|saree|drape|sareee|bangs can|crazy rich|clipzone|asking girls|prank|reaction|essay|rent -|1940|1960|vintage guide|glamourdaze|vaseline|kitchen|home|house|car\b|helmet|dog|cat\b|plant|garden|photo|pictures|camera|voice|opera", re.I)
v = []
for r in pool.values():
    t = r.get('title') or ''
    if (r.get('duration') or 0) < 180 or not PROMISE.search(t) or MEN.search(t) or JUNK.search(t): continue
    g = 'signs (flattery)' if SIGNS.search(t) else 'teen / school glow-up' if TEEN.search(t) else 'glow-up (general)' if re.search(r'glow.?up', t, re.I) else 'become more attractive / beautiful'
    v.append({**r, 'group': g})
json.dump(v, open('c1_set.json', 'w'), ensure_ascii=False)
from collections import Counter
for g in ['become more attractive / beautiful', 'glow-up (general)', 'teen / school glow-up', 'signs (flattery)']:
    s = [r for r in v if r['group'] == g]; m1 = [r for r in s if r['views'] >= 1e6]; m5 = [r for r in s if r['views'] >= 5e5]
    print(f"\n### {g}: {len(s)} videos | 1M+: {len(m1)} from {len({r['channel_id'] for r in m1})} channels | 500k+: {len(m5)} from {len({r['channel_id'] for r in m5})} | years 1M+: {sorted({r.get('year_approx') for r in m1 if r.get('year_approx')})}")
    for r in sorted(m5, key=lambda r: -r['views']): print(f"  {r['views']/1e6:6.2f}M {r.get('year_approx')} {(r['channel'] or '')[:26]:26} | {r['title'][:88]}")
