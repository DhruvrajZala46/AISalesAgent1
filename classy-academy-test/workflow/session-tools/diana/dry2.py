# dry2.py - run _body_main.py with stub layouts: every clip slot with its on-screen seconds, every at() phrase checked
import json, re, os, sys, soundfile as sf
beats = [l.strip() for l in open('beats.txt') if l.strip()]
gap = {i: 0.55 for i in range(1, len(beats) + 1)}; gap[1] = 0.8
gap.update({int(k): v for k, v in json.load(open('gaps.json')).items()})
t = 0.7; B = {}
for i, b in enumerate(beats, 1):
    d = sf.info(f'tts/c{i:03d}.wav').duration; B[i] = dict(start=t, end=t + d, text=b); t += d + gap[i]
total = t + 4.2
json.dump({str(i): [round(v['start'], 3), round(v['end'], 3)] for i, v in B.items()}, open('timeline.json', 'w'))
WORDS = json.load(open('words.json'))
st = lambda i: B[i]['start']; en = lambda i: B[i]['end']; nx = lambda i: st(i) - 0.1; en_ = lambda i: en(i) + 0.5
MISS = []
def at(i, phrase, end=False):
    nw = lambda w: re.sub(r'[^a-z0-9]', '', w.lower()); want = [nw(w) for w in phrase.split()]
    ws = WORDS[str(i)]; have = [nw(w[0]) for w in ws]
    for k in range(len(have) - len(want) + 1):
        if have[k:k + len(want)] == want: return st(i) + (ws[k + len(want) - 1][2] if end else ws[k][1])
    MISS.append((i, phrase)); k = B[i]['text'].lower().find(phrase.lower())
    return st(i) + (en(i) - st(i)) * max(0, k) / len(B[i]['text'])
W, H, PW = 1920, 1080, 608
QL = QC = QR = QT = PB = (0, 0, 0, 0); GUIDE = 'GUIDE'
SL = []; TEXT = []; USED = {}; P = os.getcwd()
C = {}
if os.path.exists('clips.py'): exec('CROP={};MAXSLOW={}\n' + open('clips.py').read())
def c(n): return C.get(n, (n, 0, 999))
def rec(spec, t0, t1, kind): SL.append((spec[0] if isinstance(spec, tuple) else spec, round(t0, 2), round(t1, 2), kind))
def _shots(shots, t1, kind):
    for k, s in enumerate(shots): rec(s[0], s[1], shots[k + 1][1] if k + 1 < len(shots) else t1, kind)
def cfull(shots, t1, **kw): _shots(shots, t1, 'full')
def lclip(shots, t1, x=0): _shots(shots, t1, 'left')
def pframe(shots, t1, **kw): _shots(shots, t1, 'phrase-frame')
def cframe(shots, t1, **kw): _shots(shots, t1, 'cream-frame')
def lrow(specs, times, t_end, **kw):
    for s, t in zip(specs, times): rec(s, t, t_end, 'row')
def frow(specs, times, t_end, **kw):
    for s, t in zip(specs, times): rec(s, t, t_end, 'framed-row')
def twoframes(a, b, t0, tb, t1, **kw): rec(a, t0, t1, 'two'); rec(b, tb, t1, 'two')
def q(html, t0, t1, *a, **kw):
    TEXT.append((round(t0, 2), round(t1, 2), re.sub(r'<[^>]+>|&#\d+;', ' ', html)))
    if t1 - t0 < 1.3: print(f'SHORT TEXT {t1-t0:.1f}s: {re.sub("<[^>]+>", " ", html)[:60]} at {t0:.1f}')
def qstack(lines, times, t1, *a, **kw):
    for l, t_ in zip(lines, times): q(l, t_, t1)
pwords = qstack
def ctext(html, t0, t1, **kw): q(html, t0, t1)
def creambg(t0, t1): pass
def card_at(txt, i, t_out, **kw): TEXT.append((round(en(i - 1) + 0.35, 2), round(t_out, 2), 'CARD ' + txt))
QB = R3 = RT = (0, 0, 0, 0); PICS = []
def pic(name, x0, y0, w, h, t0, t1, **kw): PICS.append((name, round(t0, 2), round(t1, 2))); TEXT.append((round(t0, 2), round(t1, 2), 'PHOTO ' + name))
def P_(n, label=None, pos='', a=None): return (n + '.jpg', 0.66, label, pos)
def pics(items, times, t1, **kw):
    for it, tt in zip(items, times): pic(it[0], 0, 0, 0, 0, tt, t1)
def band(html, t0, t1, size=60): q(html, t0, t1)
def picfull(name, t0, t1, **kw): pic(name, 0, 0, 0, 0, t0, t1)
def capt(html, t0, t1, **kw): q(html, t0, t1)
def cardx(txt, t0, t_out, size=None): TEXT.append((round(t0, 2), round(t_out, 2), 'CARD ' + txt))
def look(big, small, lines, times, t0, t1, tsmall, **kw):
    pic(big + '.jpg', 0, 0, 0, 0, t0, t1); pic(small + '.jpg', 0, 0, 0, 0, tsmall, t1); qstack(lines, times, t1)
os_ = os
exec(open('_body_main.py').read().split("open(os.path.join(P, 'used.txt')")[0])
if MISS: print('PHRASES NOT FOUND IN THE WORD TIMINGS:', MISS)
SL.sort(key=lambda s: s[1]); out = []
for n, t0, t1, kind in SL:
    need = t1 - t0 + 0.55; out.append(dict(slot=n, t0=t0, t1=t1, on=round(need, 1), min_clip=round(need / 1.4, 1), kind=kind))
json.dump(out, open('slots.json', 'w'), indent=0)
if '-q' not in sys.argv:
    for o in out: print(f"{o['slot']:6s} {o['t0']:7.1f} {o['on']:5.1f}s  min clip {o['min_clip']:4.1f}s  {o['kind']}")
print(len(out), 'clip slots; longest', max(o['on'] for o in out), 's; shortest', min(o['on'] for o in out), 's; video', round(total, 1), 's')
neg = [o for o in out if o['t1'] <= o['t0']]
if neg: print('ZERO OR NEGATIVE SLOTS:', neg)
for n_, a_, b_ in PICS:
    if b_ - a_ < 1.6: print(f'SHORT PHOTO {n_} {b_-a_:.1f}s at {a_:.1f}')
json.dump(PICS, open('pics.json', 'w'))
print(len(PICS), 'photos;', len(set(p[0] for p in PICS)), 'different')
import collections
print('PHOTO USED TWICE:', [k for k, v in collections.Counter(p[0] for p in PICS).items() if v > 1])
ev = sorted([(o['t0'], o['t1']) for o in out] + [(a, b) for a, b, x in TEXT]); cur = 0.0
for a, b in ev:
    if a > cur + 0.7: print(f'NOTHING ON SCREEN {cur:.1f}-{a:.1f}')
    cur = max(cur, b)
