# Per concept family: how many long-form videos passed 1M / 500k views, from how many independent channels, across which years.
import json, re, sys
from collections import defaultdict
S = json.load(open('csweep.json'))
MEN = re.compile(r"\bmen\b|\bman\b|\bguys?\b|gentle(man|men)|masculine|beard|\bhis\b|older guys|boys?\b|\bmale\b", re.I)
R = {
 'look older (age-appearance mistakes)': r"look(s|ing)? older|look(s|ing)? old\b|\bages? you\b|aging you|ageing you|\bage you\b|add(s|ing)? (\d+ |ten )?years|old lady|years older|look(s)? (\d+|ten) years older|instantly age",
 'look younger': r"younger|youthful|years off|look(s)? (\d+|ten) years younger",
 'look cheap': r"look(s|ing)? cheap|cheapen|tacky|look(s|ing)? poor|trashy|look(s|ing)? broke",
 'look expensive / rich / classy': r"look(s|ing)? (more |so |always |instantly |extra )?(expensive|rich|wealthy|classy|elegant|luxurious|high.?end|sophisticated|like a million)|expensive.?looking|look like money",
 'fashion / style mistakes (general)': r"mistake",
 'never wear / stop wearing': r"never wear|stop wearing|don.?t wear|should(n.?t| never) wear|not to wear|never buy",
 'classy habits / behaviour': r"habit|how to be classy|classy (women|woman|lady|ladies)|things classy|elegant (women|woman|lady|ladies)|high.?value",
 'capsule / wardrobe essentials': r"capsule|essentials|staples|timeless wardrobe|wardrobe basics|must.?have",
 'body type / proportions': r"body (type|shape)|look(s)? taller|look(s)? slimmer|look(s)? thinner|flatter|petite|curvy|hourglass|apple shape|pear shape",
 'colour analysis': r"colou?r analysis|colou?rs? (that|for)|skin tone|undertone|colou?r season",
 'glow up / more attractive': r"glow.?up|attractive|prettier|level up",
 'feminine': r"feminin",
 'put together / polished (rejected)': r"put.?together|polished",
 'hairstyles': r"hair",
 'etiquette': r"etiquette|manners",
}
fam = defaultdict(dict)
for k, b in S.items():
    f = b['family']; rx = re.compile(R[f], re.I)
    for r in b['rows']:
        t = r['title'] or ''
        if (r.get('duration') or 0) < 180 or not r.get('views') or MEN.search(t) or not rx.search(t): continue
        fam[f][r['id']] = r
out = {}
for f, vids in fam.items():
    v = list(vids.values())
    m1 = [r for r in v if r['views'] >= 1_000_000]; m5 = [r for r in v if r['views'] >= 500_000]
    out[f] = dict(n_on_concept=len(v), n_1M=len(m1), ch_1M=len({r['channel_id'] for r in m1}), n_500k=len(m5), ch_500k=len({r['channel_id'] for r in m5}),
                  years_1M=sorted({r['year_approx'] for r in m1 if r['year_approx']}), years_500k=sorted({r['year_approx'] for r in m5 if r['year_approx']}),
                  top=sorted(m5, key=lambda r: -r['views']))
print(f"{'family':40} {'on':>4} {'>=1M':>5} {'ch1M':>5} {'>=500k':>7} {'ch500k':>7}  years(>=1M)")
for f, s in sorted(out.items(), key=lambda kv: (-kv[1]['ch_1M'], -kv[1]['ch_500k'])):
    print(f"{f[:40]:40} {s['n_on_concept']:4d} {s['n_1M']:5d} {s['ch_1M']:5d} {s['n_500k']:7d} {s['ch_500k']:7d}  {s['years_1M']}")
json.dump(out, open('cfam.json', 'w'), ensure_ascii=False, indent=0)
