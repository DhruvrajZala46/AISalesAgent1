# pickhelp.py - the second-pass screening lines (scr/*.txt), one compact line per clip that fits, grouped by tag,
# with the automatic flags: OLD (footage matches a clip used in an earlier video), DUP (same footage under another key),
# AI (aiscan score), the clip's longest single take, and its size.
# usage: python3 pickhelp.py [tag tag ...]   (no tags: every tag)   -a also prints the clips marked "no"
import re, glob, json, sys, os
S = json.load(open('shots.json')); AI = json.load(open('aiscan.json'))
OLD = json.load(open('oldclash.json')); DG = json.load(open('dupgroups.json'))
dup = {}
for g in DG:
    for k in g: dup[k] = [x for x in g if x != k]
rows = {}
for f in sorted(glob.glob('scr/h*.txt')):
    for l in open(f):
        p = [x.strip() for x in l.strip().split('|')]
        if len(p) < 5 or not re.fullmatch(r'[a-z]+\d+', p[0]): continue
        rows[p[0]] = p
want = [a for a in sys.argv[1:] if not a.startswith('-')]; allc = '-a' in sys.argv
tags = {}
for k in rows: tags.setdefault(re.match(r'[a-z]+', k).group(0), []).append(k)
miss = sorted(k for k in S if k not in rows)
def cut(s, n): return s if len(s) <= n else s[:n - 1] + '~'
for t in sorted(tags):
    if want and t not in want: continue
    out = []; no = 0
    for k in sorted(tags[t], key=lambda x: int(re.search(r'\d+$', x).group(0))):
        p = rows[k] + [''] * 8
        fit = p[3].lower()
        bad = fit.replace('fits its purpose:', '').strip().startswith('no')
        if bad and not allc: no += 1; continue
        seg = max((b - a for a, b in S[k]['seg']), default=0) if k in S else 0
        fl = []
        if k in OLD: fl.append(f'OLD{len(OLD[k])}')
        if k in dup: fl.append('DUP=' + ','.join(dup[k][:3]))
        if AI.get(k, 0) >= 0.3: fl.append(f'AI{AI[k]:.2f}')
        sz = f"{S[k]['w']}x{S[k]['h']}" if k in S else '?'
        out.append(f"  {k} [{S.get(k, {}).get('d', 0):.0f}s take{seg:.0f} {sz}{' ' + ' '.join(fl) if fl else ''}] {cut(p[1], 80)} | {cut(p[2], 60)} | {cut(p[3].replace('fits its purpose:', '').strip(), 45)} | best {cut(p[4].replace('best seconds', '').strip(), 14)} | txt: {cut(p[5], 45)} | ai: {cut(p[6].replace('AI or fake:', '').strip(), 22)} | {cut(p[7], 34)}")
    print(f'{t}: {len(out)} usable, {no} no'); print('\n'.join(out))
if miss and not want: print('NOT SCREENED:', len(miss), ' '.join(miss[:40]))
