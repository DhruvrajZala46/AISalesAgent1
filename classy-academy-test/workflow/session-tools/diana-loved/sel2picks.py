# sel/sel_N.txt (screening output) -> picks.md lines "tag: key key ..." (key = tag + index); keeps earlier picks.md lines for other tags
import re, glob, os, json
picks = {}
for f in sorted(glob.glob('sel/sel_[0-9]*.txt')):
    tag = None
    for l in open(f):
        m = re.match(r'\s*TAG\s+([a-z]+)', l)
        if m: tag = m.group(1); picks.setdefault(tag, []); continue
        m = re.match(r'\s*PICK\s+(\d+)', l)
        if m and tag:
            k = int(m.group(1)); pins = json.load(open(f'pin/{tag}.json'))
            if k < len(pins) and pins[k].get('videos') and f'{tag}{k}' not in picks[tag]: picks[tag].append(f'{tag}{k}')
rej = {}
if os.path.exists('picks.md'):
    for l in open('picks.md'):
        m = re.match(r'# rejected after screening \(([a-z]+)\): (.*)', l)
        if m: rej[m.group(1)] = m.group(2).split()
out = ['# picks - 7 Things Princess Diana Loved (first pass: chosen from the search sheets; every clip is checked by its frames before use)']
n = 0
for tag in sorted(picks):
    keep = [k for k in picks[tag] if k not in rej.get(tag, [])]
    if keep: out.append(f'{tag}: ' + ' '.join(keep)); n += len(keep)
    if rej.get(tag): out.append(f'# rejected after screening ({tag}): ' + ' '.join(rej[tag]))
open('picks.md', 'w').write('\n'.join(out) + '\n'); print(len(picks), 'tags,', n, 'clips to have in raw/')
