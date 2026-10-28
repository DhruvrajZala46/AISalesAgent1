# sb.py - writes STORYBOARD.md from the built edit: every script line with the shots on screen while it is spoken.
# needs beats.json + storyboard.json (both written by build.py + edit.py) and ok.txt (what each checked clip shows).
import json, re, sys
B = json.load(open('beats.json')); SB = json.load(open('storyboard.json'))
NOTE = {}
for l in open('ok.txt'):
    if l.strip() and not l.startswith('#'):
        k, rest = l.split(None, 1); NOTE[k] = rest.strip()
META = json.load(open('raw/meta.json'))
FILM = {'fymail10': "You've Got Mail (1998)", 'flw5': 'Little Women (1994)'}
def mmss(t): return f'{int(t // 60)}:{t % 60:04.1f}'
def desc(k):
    n = NOTE.get(k, '')
    n = re.sub(r'^[\d.,\- ]+', '', n)          # drop the checked ranges, keep the words
    return n
out = ['# Storyboard: 8 Things Elegant Ladies Never Wear in Winter (Episode 32)', '',
       'Generated from the edit that was rendered (`edit.py` -> `storyboard.json`), so it matches the video exactly.',
       'Times are video time. "Clip" is the pin key in SOURCES-LOG.md with the seconds used.', '',
       '**Sound on every line:** the voice-over, plus one soft piano bed about 12 dB under it, steady from the first word to',
       'the end card. No sound effects anywhere. Film clips play silent under the voice.', '']
for b in B:
    i, t0, t1 = b['i'], b['start'], b['end']
    rows = [s for s in SB if s['t0'] < t1 - 0.05 and s['t1'] > t0 + 0.05]
    out.append(f'### Line {i} ({mmss(t0)}-{mmss(t1)}, {t1 - t0:.1f} s)')
    out.append(f'> {b["text"]}'); out.append('')
    out.append('| On screen | Layout | Clip (seconds used) | What it shows | Transition |'); out.append('|---|---|---|---|---|')
    for s in rows:
        a, z = max(s['t0'], t0), min(s['t1'], t1)
        if not s['clips']:
            out.append(f'| {mmss(s["t0"])}-{mmss(s["t1"])} | {s["kind"]} | none | | {s["move"]} |'); continue
        for c in s['clips']:
            k = c[0]; film = f' **Film: {FILM[k]}, unlicensed, owner\'s decision.**' if k in FILM else ''
            out.append(f'| {mmss(s["t0"])}-{mmss(s["t1"])} | {s["kind"]} | `{k}` {c[1]:g}-{c[2]:g} s | {desc(k)}{film} | {s["move"]} |')
    out.append('')
open(sys.argv[1] if len(sys.argv) > 1 else 'STORYBOARD.md', 'w').write('\n'.join(out) + '\n')
print('lines', len(B), 'shots', sum(len(s['clips']) for s in SB))
