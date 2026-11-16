# mult.py - every tagged thumbnail scored against its own channel's usual video (median of up to 60 latest long videos)
import json, glob, os, statistics, collections
T = json.load(open('table.json'))
med = {}
for f in glob.glob('ch/*.json'):
    try: es = [e for e in json.load(open(f)).get('entries') or [] if e and e.get('view_count') is not None and (e.get('duration') or 0) >= 150]
    except Exception: continue
    if len(es) >= 6: med[os.path.basename(f)[:-5]] = statistics.median(e['view_count'] for e in es)
tags = {}
for fn in ('tags_W.txt', 'tags_ML.txt'):
    for l in open(fn):
        if l[:1] in 'WML' and '|' in l: r = l.strip().split('|'); tags[r[0]] = r
ids = {}
for tier, key in (('W', 'win'), ('M', 'mids'), ('L', 'lows')):
    vs = [v for v in T[key] if os.path.exists(f"img/{v['id']}.jpg")]
    for n, v in enumerate(vs, 1): ids[f'{tier}{n:03d}'] = v
rows = []
for k, r in tags.items():
    v = ids.get(k)
    if not v or r[1] == 'X' or v['cid'] not in med or med[v['cid']] <= 0: continue
    rows.append(dict(k=k, kind=r[1], words=r[2], face=r[3], expr=r[4], women=r[5], tone=r[6], mult=v['views'] / med[v['cid']], views=v['views'], title=v['title'], channel=v['channel']))
json.dump(rows, open('mult_rows.json', 'w'))
print('scored', len(rows), 'of', sum(1 for r in tags.values() if r[1] != 'X'), 'on-topic tagged thumbnails;', len(med), 'channel medians')
def show(name, f):
    g = collections.defaultdict(list)
    for r in rows: g[f(r)].append(r['mult'])
    print(f'\n{name}: n | usual multiple | share at 3x+ | share under 0.7x')
    for k, m in sorted(g.items(), key=lambda kv: -statistics.median(kv[1])):
        if len(m) >= 4: print(f'  {k:28} {len(m):3d} | {statistics.median(m):6.2f}x | {100*sum(x>=3 for x in m)/len(m):4.0f}% | {100*sum(x<0.7 for x in m)/len(m):4.0f}%')
names = dict(P='P other people react', S='S signs/warning about her', L='L trait label', C='C command', T='T topic', V='V two-sided', N='N no words', K='K reveal claim', Q='Q question', R='R named rule')
show('kind of words', lambda r: names.get(r['kind'], r['kind']))
show('people react or signs vs the rest', lambda r: 'P or S' if r['kind'] in 'PS' else ('T or L (label)' if r['kind'] in 'TL' else 'other'))
show('face', lambda r: r['face'])
show('a well-known woman', lambda r: 'celeb woman' if r['face'] == 'celeb' and r['women'] == 'y' else ('anon/AI woman' if r['face'] == 'anon' else 'other'))
show('words in the thumbnail', lambda r: '0' if r['words'] == '0' else ('1-3' if r['words'].isdigit() and int(r['words']) <= 3 else ('4-5' if r['words'].isdigit() and int(r['words']) <= 5 else '6+')))
show('expression', lambda r: r['expr'])
show('tone', lambda r: r['tone'])
print('\nP and S thumbnails:')
for r in sorted([r for r in rows if r['kind'] in 'PS'], key=lambda r: -r['mult']): print(f"  {r['k']} {r['mult']:6.1f}x {r['views']/1e3:7.0f}k {r['channel'][:22]:22} {r['title'][:70]}")
