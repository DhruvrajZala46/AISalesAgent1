# dry.py - run the body of the edit with stub layouts: lists every clip slot with the seconds it stays on screen
# (so each chosen window is long enough) and checks that every at(i, "phrase") matches the spoken words.
import json, re, os, sys
P = os.getcwd()
TL = json.load(open('timeline.json')); WORDS = json.load(open('words.json'))
beats = [l.rstrip('\n') for l in open('beats.txt') if l.strip()]
B = {i: dict(start=TL[str(i)][0], end=TL[str(i)][1], text=beats[i - 1]) for i in range(1, len(beats) + 1)}
st = lambda i: B[i]['start']; en = lambda i: B[i]['end']; nx = lambda i: st(i) - 0.1
MISS = []
def at(i, phrase, end=False):
    nw = lambda w: re.sub(r'[^a-z0-9]', '', w.lower())
    want = [nw(w) for w in phrase.split()]
    ws = WORDS[str(i)]; have = [nw(w[0]) for w in ws]
    for k in range(len(have) - len(want) + 1):
        if have[k:k + len(want)] == want: return st(i) + (ws[k + len(want) - 1][2] if end else ws[k][1])
    MISS.append((i, phrase)); return st(i)
total = en(len(beats)) + 4.2
W, H, PW = 1920, 1080, 608
QL = QC = QR = LOW = RT = QL3 = QT = (0, 0, 0, 0); MID = 0; GUIDE = ''
SL = []; SEGS = {}; USED = {}; TEXT = []
def c(n): return (n, 0, 999)
exec('CROP={};MAXSLOW={}\n' + open('clips.py').read()); _CS = set(C)
def rec(spec, t0, t1, kind): SL.append((spec[0], round(t0, 2), round(t1, 2), kind))
def cfull(shots, t1, kind='full'):
    for k, s in enumerate(shots): rec(s[0], s[1], shots[k + 1][1] if k + 1 < len(shots) else t1, kind)
def lclip(shots, t1, x=0): cfull(shots, t1, 'left')
def lrow(specs, times, t_end, **kw):
    for s, t in zip(specs, times): rec(s, t, t_end, 'row')
def _frames(shots, t1, *a, **kw): cfull(shots, t1, 'frame')
def q(html, t0, t1, *a, **kw):
    TEXT.append((round(t0, 2), round(t1, 2), re.sub(r'<[^>]+>', ' ', html)))
    if t1 - t0 < 1.6: print(f'SHORT TEXT {t1-t0:.1f}s: {html[:60]} {t0:.1f}-{t1:.1f}')
def qstack(lines, times, t1, **kw):
    for l, t in zip(lines, times): q(l, t, t1)
def card_from(txt, t0, t1, **kw): TEXT.append((round(t0, 2), round(t1, 2), 'CARD ' + txt))
def photo(png, x0, y0, w, h, t0, t1, **kw): TEXT.append((round(t0, 2), round(t1, 2), 'PHOTO ' + png + ' ' + str(kw.get('label'))))
def pieces(items, times, t_end, **kw):
    for (png, lab_), t in zip(items, times): TEXT.append((round(t, 2), round(t_end, 2), 'CUTOUT ' + png + ' ' + lab_))
def grid8(items, tin, t1, **kw): TEXT.append((round(tin[0], 2), round(t1, 2), 'GRID of eight')); return [f'g{k}' for k in range(8)]
def clabel(txt, cx, y, t0, t1):
    TEXT.append((round(t0, 2), round(t1, 2), 'LABEL ' + txt))
    if t1 - t0 < 1.5: print('SHORT LABEL', txt, round(t1 - t0, 1))
tw = []
def prod(png, *a, **k): TEXT.append((round(a[2], 2), round(a[3], 2), 'CUTOUT ' + png))
class _I:
    width = 600; height = 900
class _PILImage:
    open = staticmethod(lambda p: _I())
A = 'assets'
src = '#' + open('_body_main.py').read().split('# ==== BODY ====', 1)[1]
src = re.sub(r'\ndef two\(.*?\n(?=def lab)', '\ndef two(a, b, t0, tb, t1, la=None, lb=None, tla=None, tlb=None, size=54):\n    rec(a, t0, t1, "two"); rec(b, tb, t1, "two")\n    if la: q(la, tla or t0 + 0.3, t1)\n    if lb: q(lb, tlb or tb + 0.3, t1)\n', src, flags=re.S)
exec(src)
if MISS: print('PHRASES NOT FOUND IN THE WORD TIMINGS:', MISS)
SL.sort(key=lambda s: s[1])
out = []
for n, t0, t1, kind in SL:
    need = t1 - t0 + 0.55; out.append(dict(slot=n, t0=t0, t1=t1, on=round(need, 1), min_clip=round(need / 1.4, 1), kind=kind))
json.dump(out, open('slots.json', 'w'), indent=0)
if '-q' not in sys.argv:
    for o in out: print(f"{o['slot']:6s} {o['t0']:7.1f} {o['on']:5.1f}s  min clip {o['min_clip']:4.1f}s  {o['kind']}")
print(len(out), 'clip slots;', 'longest', max(o['on'] for o in out), 's; shortest', min(o['on'] for o in out), 's')
# gaps: any moment with no clip, card, photo or text on screen
ev = sorted([(o['t0'], o['t1']) for o in out] + [(a, b) for a, b, x in TEXT if x.startswith(('CARD', 'GRID')) or True])
cur = 0.0
for a, b in ev:
    if a > cur + 0.7: print(f'NOTHING ON SCREEN {cur:.1f}-{a:.1f}')
    cur = max(cur, b)
