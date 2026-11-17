import json, glob, os, statistics, collections
T = json.load(open('table.json')); med = {}
for f in glob.glob('ch/*.json'):
    try: es = [e for e in json.load(open(f)).get('entries') or [] if e and e.get('view_count') is not None and (e.get('duration') or 0) >= 150]
    except Exception: continue
    if len(es) >= 6: med[os.path.basename(f)[:-5]] = statistics.median(e['view_count'] for e in es)
ids = {}
for tier, key in (('S', 'SW'), ('M', 'SM'), ('L', 'SL'), ('R', 'RW'), ('D', 'DW')):
    vs = [v for v in T[key] if os.path.exists(f"img/{v['id']}.jpg")]
    for n, v in enumerate(vs, 1): ids[f'{tier}{n:03d}'] = v
rows = []
for l in open('tags.txt'):
    if l[0] in 'SML' and '|' in l:
        r = l.strip().split('|'); v = ids[r[0]]
        m = v['views'] / med[v['cid']] if med.get(v['cid']) else None
        rows.append(dict(k=r[0], kind=r[1], words=int(r[2]), pics=int(r[3]), marks=len(r) > 4, views=v['views'], mult=m, title=v['title'], channel=v['channel'], tier=r[0][0]))
json.dump(rows, open('rows.json', 'w'))
sc = [r for r in rows if r['mult'] is not None]
print(len(rows), 'tagged;', len(sc), 'with a channel median;', len(med), 'channels')
NAME = dict(O='her outfits shown', F='her face only', J='jewels / products', D='a dress alone', V='a video frame', X='other people lead', A='AI or drawing', G='grid of many')
def show(name, f, minn=4):
    g = collections.defaultdict(list)
    for r in sc: g[f(r)].append(r['mult'])
    print(f'\n{name}: n | usual multiple | 5x+ | under 1x')
    for k, m in sorted(g.items(), key=lambda kv: -statistics.median(kv[1])):
        if len(m) >= minn: print(f'  {str(k):26} {len(m):3d} | {statistics.median(m):6.1f}x | {100*sum(x>=5 for x in m)/len(m):4.0f}% | {100*sum(x<1 for x in m)/len(m):4.0f}%')
show('KIND', lambda r: NAME[r['kind']])
show('WORDS', lambda r: 'no words' if r['words'] == 0 else '1-3 words' if r['words'] <= 3 else '4+ words')
show('OUTFIT thumbnails: pictures of her', lambda r: ('1 picture' if r['pics'] == 1 else '2-3 pictures' if r['pics'] <= 3 else '4+ pictures') if r['kind'] == 'O' else 'x', 3)
show('OUTFIT thumbnails: words', lambda r: ('no words' if r['words'] == 0 else 'words') if r['kind'] == 'O' else 'x', 3)
print('\nby view tier (share of each kind):')
for t, nm in (('S', '300k+'), ('M', '50k-300k'), ('L', '2k-50k')):
    rs = [r for r in rows if r['tier'] == t]; c = collections.Counter(r['kind'] for r in rs)
    print(f"  {nm:9} n={len(rs):2d} " + ' '.join(f"{NAME[k]} {100*c[k]/len(rs):.0f}%" for k in 'OFJDVXAG') + f" | no words {100*sum(r['words']==0 for r in rs)/len(rs):.0f}%")
top = [r for r in rows if r['views'] >= 1e6]; c = collections.Counter(r['kind'] for r in top)
print('  1M+ n=%d' % len(top), dict((NAME[k], v) for k, v in c.items()), 'no words:', sum(r['words'] == 0 for r in top))
print('\nmarks (circles / arrows on the detail):'); [print('  ', r['k'], f"{r['views']:,}", f"{r['mult']:.1f}x" if r['mult'] else '-', r['channel'], '|', r['title'][:70]) for r in rows if r['marks']]
print('\ntop multiples:'); [print('  ', r['k'], NAME[r['kind']], r['words'], 'words', f"{r['views']:,}", f"{r['mult']:.0f}x", r['channel'][:20], '|', r['title'][:60]) for r in sorted(sc, key=lambda r: -r['mult'])[:22]]
