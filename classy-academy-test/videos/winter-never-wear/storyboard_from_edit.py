# storyboard_from_edit.py - writes STORYBOARD.md from the built edit: every script line with what is on screen while it is spoken.
# usage (inside the work folder): python3 storyboard_from_edit.py [STORYBOARD.md] [ok5.txt]
# needs beats.json + storyboard.json (both written by build.py + edit.py) and the checked-clip notes (what each clip shows).
import json, re, sys
B = json.load(open('beats.json')); SB = json.load(open('storyboard.json'))
OKF = sys.argv[2] if len(sys.argv) > 2 else 'ok5.txt'
NOTE = {}
for l in open(OKF):
    p = l.split(None, 1)
    if len(p) == 2 and not l.startswith('#') and not p[1].startswith('SKIP'): NOTE.setdefault(p[0], p[1].strip())
META = json.load(open('raw/meta.json'))
def mmss(t): return f'{int(t // 60)}:{t % 60:04.1f}'
def desc(k):
    if k.endswith('.png'):                      # product cut-out (background removed from a product photo pin)
        pin = 'p_' + k[4:-4]; return f'product cut-out (`{pin}`): {META.get(pin, {}).get("title", "")[:70]}'
    if k.startswith('film_'): return f'*Charade* (1963): {re.sub(r" [(]film time.*", "", META.get(k, {}).get("title", ""))}'
    return re.sub(r'^[\d.,\- ]+', '', NOTE.get(k, META.get(k, {}).get('title', '')))
out = ['# Storyboard v5: 8 Things Elegant Ladies Never Wear in Winter (Episode 15)', '',
       'Generated from the edit that was rendered (`edit.py` -> `storyboard.json`), so it matches the video exactly. The plan it',
       'follows is `VISUAL-SCRIPT.md`; the layouts are the owner\'s own (`workflow/EDIT-RULES.md`): rows of tall reels on the',
       'caramel backdrop, framed reels, one centred reel, product cut-outs, the principle line beside a reel, white number cards,',
       'and full screen only for landscape footage (the *Charade* scenes).', '',
       'Times are video time. "Clip" is the key in SOURCES-LOG.md with the seconds used.', '',
       '**Sound on every line:** the voice-over, plus one soft piano bed about 12 dB under it, steady from the first word to',
       'the end card. No sound effects anywhere. Film clips play silent under the voice.', '']
for b in B:
    i, t0, t1 = b['i'], b['start'], b['end']
    rows = [s for s in SB if s['t0'] < t1 - 0.05 and s['t1'] > t0 + 0.05]
    out.append(f'### Line {i} ({mmss(t0)}-{mmss(t1)}, {t1 - t0:.1f} s)')
    out.append(f'> {b["text"]}'); out.append('')
    out.append('| On screen | Layout | Clip (seconds used) | What it shows | Movement |'); out.append('|---|---|---|---|---|')
    for s in rows:
        if not s['clips']:
            out.append(f'| {mmss(s["t0"])}-{mmss(s["t1"])} | {s["kind"]} | none | | {s["move"]} |'); continue
        for c in s['clips']:
            k = c[0]; used = '' if k.endswith('.png') else f' {c[1]:g}-{c[2]:g} s'
            out.append(f'| {mmss(s["t0"])}-{mmss(s["t1"])} | {s["kind"]} | `{k}`{used} | {desc(k).replace("|", "/")} | {s["move"].replace("|", "/")} |')
    out.append('')
open(sys.argv[1] if len(sys.argv) > 1 else 'STORYBOARD.md', 'w').write('\n'.join(out) + '\n')
print('lines', len(B), 'shots', sum(len(s['clips']) for s in SB))
