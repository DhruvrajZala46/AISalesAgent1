# Candidate angles measured on the whole screened dataset. Hit = >=3x channel median, >=20k views, channel median >=3k.
import json, re, statistics as st
D = json.load(open('dataset.json'))
CA = 'UCJUn02MVnahA9My9-DUkTBQ'
rows = [r for r in D['rows'] if r['multiple'] is not None and r['channel_id'] != CA]
OFFMEN = re.compile(r"\bmen\b|\bman\b|gentle(man|men)|beard|masculine", re.I)
C = {
 'C1 outdated vs timeless': r"outdated|\bdated\b|out of style|dying in 20|officially out|\bare out\b|look(s)? modern|modern,? not|instantly date|date(s)? your|matronly|old.?fashioned|timeless vs|never go(es)? out of style|always in style",
 'C2 colour combinations': r"colou?r combo|colou?r combination|colou?r formula|colou?rs? (that|which) (make|look|instantly)|colou?rs defining|colou?r pairing|colou?rs? making",
 'C3 fine/thin hair': r"(fine|thin|thinning|flat)\W{0,3}(and |& |/)?(thin\W{0,2})?hair|hair.{0,25}\b(fine|thin)\b",
 'C4 rude people / disrespect': r"\brude\b|disrespect|respect you|difficult people|mean people|\bpetty\b|immune to|insult|passive.?aggressive|toxic (people|person)|people who (disrespect|ignore)|handle (rude|people|criticism)",
 'C5 why dressing well / how people treat you': r"dress(ing)? well|dressed well|well.?dressed|treat(ed|s)? (me|you|her) (differently|better|with)|first impressions?|why (some )?(women|people|she) always look|always look cool|dare to dress",
 'C6 etiquette / manners': r"etiquette|manners|old.?fashioned (things|rules|habits)",
 'X age / look younger (rejected)': r"younger|aging|ageing|look older|age (well|gracefully)|with age",
}
def hit(r): return r['multiple'] >= 3 and (r['views'] or 0) >= 20000 and (r['channel_median'] or 0) >= 3000
def S(rs):
    if not rs: return dict(n=0)
    h = [r for r in rs if hit(r)]
    return dict(n=len(rs), ch=len({r['channel_id'] for r in rs}), med=round(st.median(r['multiple'] for r in rs), 2), hits=len(h), hit_ch=len({r['channel_id'] for r in h}), rate=round(len(h) / len(rs), 3))
base = {w: S([r for r in rows if r['age_days'] is not None and lo < r['age_days'] <= hi]) for w, (lo, hi) in {'0-120': (-1, 120), '121-365': (120, 365), '>365': (365, 99999)}.items()}
print('BASELINE', base)
out = {}
for k, rx in C.items():
    rx = re.compile(rx, re.I)
    rs = [r for r in rows if rx.search(r['title']) and not OFFMEN.search(r['title'])]
    w = {name: S([r for r in rs if r['age_days'] is not None and lo < r['age_days'] <= hi]) for name, (lo, hi) in {'0-120': (-1, 120), '121-365': (120, 365), '>365': (365, 99999)}.items()}
    w['undated (search only)'] = S([r for r in rs if r['age_days'] is None])
    idx = {name: round(w[name].get('rate', 0) / base[name]['rate'], 2) for name in ('0-120', '121-365', '>365')}
    hits = sorted([r for r in rs if hit(r)], key=lambda r: -r['multiple'])
    weak = sorted([r for r in rs if r['multiple'] < 0.7 and (r['channel_median'] or 0) >= 3000 and r['age_days'] and r['age_days'] > 30], key=lambda r: r['multiple'])
    out[k] = dict(windows=w, hit_rate_index_vs_baseline=idx, hits=hits[:40], weak=weak[:25], n_total=len(rs))
    print(f"\n=== {k}: {len(rs)} videos, {len({r['channel_id'] for r in rs})} channels | index vs baseline {idx}")
    for name, s in w.items(): print('   ', name, s)
    for r in [h for h in hits if h['age_days'] is not None and h['age_days'] <= 365][:14]:
        print(f"      HIT {r['multiple']:5.1f} {r['views']//1000:>5}k {r['date']} {r['channel'][:20]:20} | {r['title'][:80]}")
    for r in weak[:5]: print(f"      weak {r['multiple']:4.2f} {r['views']//1000:>5}k {r['date']} {r['channel'][:20]:20} | {r['title'][:80]}")
json.dump(dict(baseline=base, candidates=out), open('cands.json', 'w'), ensure_ascii=False, indent=1)
