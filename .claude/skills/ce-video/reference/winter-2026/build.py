# v4: opening + point 1. Slower voice, one clip per idea (never reused), product cutouts, continuous music bed, audible soft SFX.
import os, subprocess, json
import numpy as np, soundfile as sf

P = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(P, 'assets')
W, H = 1920, 1080
PW = 608                     # 9:16 panel at full height
def sh(c): subprocess.run(c, shell=True, check=True)
_d = {}
def dur(f):
    if f not in _d: _d[f] = float(subprocess.run(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {A}/{f}", shell=True, capture_output=True, text=True).stdout)
    return _d[f]

# ---------- voice timing (calm pace: speed 0.84 + breathing room) ----------
beats = [l.strip() for l in open(os.path.join(P, 'beats.txt')) if l.strip()]
gap = {}
gap.update({1: 0.7, 2: 0.35, 3: 0.9, 4: 0.25, 5: 0.35, 6: 0.35, 7: 0.3, 8: 0.3, 9: 0.75, 10: 0.8, 11: 0.3, 12: 1.2, 13: 0.8,
            14: 0.35, 15: 0.3, 16: 0.3, 17: 0.6, 18: 0.8, 19: 0.35, 20: 0.6, 21: 0.3, 22: 0.5, 23: 0.3, 24: 0.8, 25: 0.45,
            26: 0.3, 27: 0.3, 28: 0.3, 29: 0.35, 30: 0.7, 31: 0.8, 32: 0.5, 33: 0.3, 34: 0.3, 35: 0.7, 36: 0.7, 37: 1.1})
for i in range(38, 121): gap.setdefault(i, 0.85)
for i in (46, 47, 54, 55, 60, 61, 62, 73, 74, 77, 78, 96, 97, 107, 108, 111, 112, 113, 114, 115, 116): gap[i] = 0.45
for i in (37, 50, 67, 79, 88, 99, 110): gap[i] = 1.1
for i in (38, 51, 68, 80, 89, 100): gap[i] = 0.8
gap[117] = 0.7; gap[118] = 0.8; gap[119] = 0.7; gap[120] = 0.4
sr = 24000; t = 0.9; parts = [np.zeros(int(sr * 0.9))]; T = []
for i, b in enumerate(beats, 1):
    y, s = sf.read(os.path.join(P, 'tts80', f'c{i:03d}.wav')); y = y.mean(1) if y.ndim > 1 else y
    d = len(y) / sr; T.append(dict(i=i, text=b, start=round(t, 3), end=round(t + d, 3)))
    parts += [y, np.zeros(int(sr * gap[i]))]; t += d + gap[i]
voice = np.concatenate(parts + [np.zeros(int(sr * 1.2))]); total = len(voice) / sr
sp = voice[np.abs(voice) > 1e-3]; voice *= 10 ** (-17.7 / 20) / np.sqrt((sp ** 2).mean())
json.dump(T, open(os.path.join(P, 'beats.json'), 'w'), indent=1)
B = {d['i']: d for d in T}
st = lambda i: B[i]['start']; en = lambda i: B[i]['end']
wd = lambda i, f: B[i]['start'] + (B[i]['end'] - B[i]['start']) * f

# ---------- building blocks ----------
els, tw, SFX = [], [], []; uid = [0]; USED = {}; SHORT = []
def nid(p): uid[0] += 1; return f"{p}{uid[0]}"
def sfx(name, t, g): SFX.append((name, max(0.0, t), g))
GRADE = 'filter:contrast(1.03) saturate(0.95) sepia(0.05);'
def vid(src, t0, t1, cls='med', style=GRADE, reuse_ok=False):
    if not reuse_ok:
        assert src not in USED or USED[src] == (t0, t1), f'{src} used twice'
        USED[src] = (t0, t1)
    i = nid('v')
    if t1 - t0 > dur(src) + 0.02: SHORT.append(f'{src} needs {t1-t0:.1f}s has {dur(src):.1f}s')
    return i, f'<video id="{i}" class="{cls}" src="assets/{src}" muted playsinline data-start="{t0:.3f}" data-duration="{t1-t0:.3f}" style="{style}"></video>'
def box(x0, y0, x1, y1, inner, z=''):
    i = nid('b'); els.append(f'<div id="{i}" class="w" style="left:{x0}px;top:{y0}px;width:{x1-x0}px;height:{y1-y0}px;opacity:0;{z}">{inner}</div>'); return i
def drift(i, t0, t1, s=1.06): tw.append(f'tl.fromTo("#{i}",{{scale:1}},{{scale:{s},duration:{t1-t0+0.6:.2f},ease:"none"}},{t0:.3f});')
def fade_in(i, t, d=0.55): tw.append(f'tl.fromTo("#{i}",{{opacity:0}},{{opacity:1,duration:{d},ease:"sine.inOut"}},{t:.3f});')
def fade_out(i, t, d=0.55): tw.append(f'tl.to("#{i}",{{opacity:0,duration:{d},ease:"sine.inOut"}},{t:.3f});')
def grow_corner(i, t, origin="0% 0%"):
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.6}},{{opacity:1,scale:1,duration:1.0,ease:"expo.out",transformOrigin:"{origin}"}},{t:.3f});'); sfx('click-soft', t + 0.03, -21)
def grow_centre(i, t):
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.35}},{{opacity:1,scale:1,duration:1.3,ease:"expo.out",transformOrigin:"50% 50%"}},{t:.3f});'); sfx('click-soft', t + 0.05, -21)

def panel(srcs, x0, x1, t0, t1, entry='corner', swaps=(), y0=0, y1=H, origin="0% 0%", label=None):
    """A clip panel. swaps = [(clip, t)] cross-dissolve to the next clip inside the same panel."""
    end = t1 + 0.55; seq = [(srcs, t0)] + list(swaps); inner = ''
    for k, (s, ts) in enumerate(seq):
        te = (seq[k + 1][1] + 0.6) if k + 1 < len(seq) else end
        v, h = vid(s, ts, te); drift(v, ts, te)
        if k: h = h.replace('style="', 'style="opacity:0;'); tw.append(f'tl.fromTo("#{v}",{{opacity:0}},{{opacity:1,duration:0.6,ease:"sine.inOut"}},{ts:.3f});')
        inner += h
    i = box(x0, y0, x1, y1, inner)
    if entry == 'corner': grow_corner(i, t0, origin)
    elif entry == 'centre': grow_centre(i, t0)
    else: fade_in(i, t0, 0.6)
    fade_out(i, t1, 0.55)
    if label: clabel(label, (x0 + x1) // 2, y1 - 120, t0 + 0.5, t1)
    return i
def photo(src, x0, x1, t0, t1, entry='corner', origin="0% 0%"):
    i0 = nid('ph'); i = box(x0, 0, x1, H, f'<img id="{i0}" class="photo" src="assets/{src}">')
    drift(i0, t0, t1 + 0.55, 1.08)
    (grow_corner if entry == 'corner' else grow_centre)(i, t0, *( [origin] if entry == 'corner' else [])); fade_out(i, t1, 0.55); return i
def clabel(txt, cx, y, t0, t1):
    i = nid('cl'); els.append(f'<div id="{i}" class="cl" style="left:{cx-300}px;top:{y}px;width:600px;opacity:0">{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:0.8,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.5)
def row(srcs, times, t_end, labels=None):
    n = len(srcs); w = W / n
    for k, (s, tt) in enumerate(zip(srcs, times)):
        panel(s, max(0, round(k * w) - 1), min(W, round((k + 1) * w) + 1), tt, t_end, label=(labels or [None] * n)[k])
def pair(srcs, times, t_end, gapx=14):
    x = (W - 2 * PW - gapx) // 2
    for k, (s, tt) in enumerate(zip(srcs, times)):
        x0 = x + k * (PW + gapx); panel(s, x0, x0 + PW, tt, t_end)
def single(src, t0, t1, x0=None, label=None, swaps=()):
    x0 = (W - PW) // 2 if x0 is None else x0
    return panel(src, x0, x0 + PW, t0, t1, entry='centre', label=label, swaps=swaps)
def canvas_full(src, t0, t1, fin=0.7, fout=0.6):
    """Full screen from a vertical clip: soft blurred copy fills the frame, sharp clip centred."""
    e = t1 + fout
    bgv, bgh = vid(src, t0, e, cls='', style=''); fgv, fgh = vid(src, t0, e, reuse_ok=True)
    i = nid('cv'); els.append(f'<div id="{i}" class="w" style="left:0;top:0;width:{W}px;height:{H}px;opacity:0"><div class="canvas">{bgh}</div>'
                             f'<div class="w" style="left:{(W-PW)//2}px;top:0;width:{PW}px;height:{H}px;opacity:1">{fgh}</div></div>')
    drift(fgv, t0, e, 1.07); fade_in(i, t0, fin); fade_out(i, t1, fout); sfx('whoosh', t0 - 0.25, -24); return i
def white(t0, t1, fin=0.45, fout=0.5):
    i = nid('wh'); els.append(f'<div id="{i}" class="white" style="opacity:0"></div>'); fade_in(i, t0, fin); fade_out(i, t1, fout)
    sfx('whoosh-short', t0 - 0.15, -22); return i
def text(html, cls, t0, t1, dur=1.4, out=0.55, style=''):
    i = nid('tx'); els.append(f'<div id="{i}" class="{cls}" style="opacity:0;{style}">{html}</div>')
    tw.append(f'tl.set("#{i}",{{opacity:1}},{t0:.3f});')
    tw.append(f'tl.fromTo("#{i}",{{"--p":100}},{{"--p":0,duration:{dur},ease:"none"}},{t0:.3f});')
    fade_out(i, t1, out)
    if cls in ('card', 'hint'): sfx('sparkle', t0 - 0.05, -19)
    return i
def snow(t0, t1, op=0.42):
    i = nid('sn'); els.append(f'<div id="{i}" class="snow" style="opacity:0"><video id="{i}v" src="assets/mk8468.mp4" muted playsinline data-start="{t0:.3f}" data-duration="{min(t1-t0+0.8,56):.3f}"></video></div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0}},{{opacity:{op},duration:0.8,ease:"none"}},{t0:.3f});'); fade_out(i, t1, 0.8)
def quote_side(src, t0, t1, l1, l2, t2, swaps=()):
    """Clip on the left, the key line written on the right (their 'quote beside a clip')."""
    panel(src, 170, 170 + PW, t0, t1, entry='fade', swaps=swaps)
    text(l1, 'qs1', t0 + 0.35, t1, dur=1.4); text(l2, 'qs2', t2, t1, dur=1.2)
def cutout(png, cx, cy, w, h, t0, t1, label=None, lbs=46):
    """A product photo with no background floating on the backdrop; rises in softly, then breathes."""
    i = nid('ct'); lb = f'<div class="lb" style="font-size:{lbs}px">{label}</div>' if label else ''
    els.append(f'<div id="{i}" class="cut" style="left:{cx-w//2}px;top:{cy-h//2}px;width:{w}px;height:{h+90}px;opacity:0"><div style="height:{h}px;width:{w}px;display:flex;align-items:flex-end;justify-content:center"><img src="assets/{png}"></div>{lb}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:40,scale:0.92}},{{opacity:1,y:0,scale:1,duration:1.1,ease:"expo.out"}},{t0:.3f});')
    tw.append(f'tl.to("#{i}",{{y:-8,duration:{max(0.5,t1-t0-1.1):.2f},ease:"sine.inOut"}},{t0+1.1:.3f});')
    fade_out(i, t1, 0.5); sfx('pop', t0 + 0.05, -24)
def header(txt, cx, t0, t1, y=38):
    i = nid('hd'); els.append(f'<div id="{i}" class="hd" style="left:{cx-258}px;top:{y}px;opacity:0">{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:10}},{{opacity:1,y:0,duration:0.7,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.5)
PH0, PH1, PW2 = 96, 1014, 516    # 85%-height panels for recipes / comparisons

# ================= the edit =================
# --- hook: a real elegant woman in a coat; "stop."
canvas_full('h1.mp4', 0.0, en(1) + 0.25, fin=0.01)
# 2 "Elegant women never wear these seven things..." -> real elegant women: the Princess of Wales, Princess Diana
pair(['h2.mp4', 'h3.mp4'], [st(2) - 0.15, wd(2, 0.4)], en(2) + 0.15)
# 3 "...number four is in almost every closet" -> a closet full of fleece, and a fleece zip-up on
photo('fleece_closet.jpg', (W - 2 * PW - 14) // 2, (W - 2 * PW - 14) // 2 + PW, st(3) - 0.1, en(3) + 0.35)
panel('h4.mp4', (W - 2 * PW - 14) // 2 + PW + 14, (W - 2 * PW - 14) // 2 + 2 * PW + 14, wd(3, 0.45), en(3) + 0.35)
# 4-5 white "in today's video..." -> title over a cinematic winter walk
white(en(3) + 0.4, st(5) + 0.15)
text("in today's video...", 'card', st(4) - 0.05, st(5) - 0.2, dur=1.0, out=0.4)
canvas_full('h5.mp4', st(5) - 0.05, en(5) + 0.35, fin=0.6); snow(st(5), en(5) + 0.4, 0.38)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 8</div><div class="big">7 Things Elegant Women Never Wear in Winter</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.2,ease:"power2.out"}},{st(5)+0.5:.3f});'); fade_out(i, en(5) + 0.3, 0.5); sfx('sparkle', st(5) + 0.45, -18)
# 6 "...what they wear instead" -> one elegant winter outfit grows from the centre
single('h6.mp4', st(6), en(6) + 0.2)
# 7-9 warm / polished / effortlessly expensive -> one panel per word, each labelled
row(['h7.mp4', 'h8.mp4', 'h9.mp4'], [st(7), st(8), st(9)], en(9) + 0.45, labels=['warm', 'polished', 'effortlessly expensive'])
# 10 key line beside a woman bundled against the snow
quote_side('h10.mp4', st(10) - 0.1, en(10) + 0.45, 'Being cold has never been', 'the <i>secret</i> to elegance', wd(10, 0.5)); snow(st(10), en(10) + 0.5, 0.4)
# 11-12 "Some of these may surprise you..." -> centred clip grows, then three elegant women
single('h11.mp4', st(11), wd(12, 0.15))
row(['h12.mp4', 'h13.mp4', 'h14.mp4'], [wd(12, 0.18), wd(12, 0.4), wd(12, 0.65)], en(12) + 0.35)

# --- point 1: flat, lifeless black
white(en(12) + 0.45, en(13) + 0.45)
text('1. Flat, lifeless black', 'card', st(13) + 0.1, en(13) + 0.35)
# 14-17 the problem, one panel per reason
row(['k1.mp4', 'k2.mp4', 'k3.mp4', 'k4.mp4'], [en(13) + 0.4, st(15), st(16) + 0.2, st(17)], en(17) + 0.45,
    labels=['safe', 'easy', 'hides everything', 'always matches'])
# 18 "...heavy instead of chic"
quote_side('k5.mp4', st(18) - 0.1, en(18) + 0.45, '“It can start to feel <i>heavy</i>', 'instead of chic”', wd(18, 0.6))
# 19-20 the principle beside a black knit with real texture
quote_side('k6.mp4', st(19) - 0.1, en(20) + 0.45, "Elegant women don't avoid black", 'they give it <i>texture</i>', st(20))
# 21-24 the textured pieces: the woman wearing each one on the left, the piece itself joins the lineup on the right
panel('k7.mp4', 150, 150 + PW, st(21) - 0.1, en(24) + 0.5, entry='fade', swaps=[('k8.mp4', st(22)), ('k9.mp4', st(23)), ('k10.mp4', st(24))])
for k, (png, lb, tt) in enumerate([('cut_knit.png', 'cashmere knit', st(21)), ('cut_gloves.png', 'leather gloves', st(22)),
                                   ('cut_blazer.png', 'velvet blazer', st(23)), ('cut_cami.png', 'silk camisole', st(24))]):
    cutout(png, [1080, 1560, 1080, 1560][k], [250, 250, 640, 640][k], 340, 300, tt, en(24) + 0.5, lb)
# 25 the softer side of winter
canvas_full('k11.mp4', st(25) - 0.1, en(25) + 0.2); snow(st(25), en(25) + 0.3, 0.38)
# 26-29 one panel per colour, 30 tone on tone
row(['k12.mp4', 'k13.mp4', 'k14.mp4', 'k15.mp4'], [st(26), st(27), st(28), st(29)], en(29) + 0.3,
    labels=['winter white', 'cream', 'camel', 'chocolate brown'])
single('k16.mp4', st(30) - 0.05, en(30) + 0.45, label='tone on tone')
# 31 key line
quote_side('k17.mp4', st(31) - 0.1, en(31) + 0.45, "It's not about giving up black", "it's about making it <i>intentional</i>", wd(31, 0.5))
# 32-35 "Try this": one black outfit, three textures (pieces float between two textured looks)
text('try this...', 'hint', st(32), wd(32, 0.5) + 0.2, dur=1.0, out=0.4)
panel('k24.mp4', 110, 110 + PW2, wd(32, 0.55), en(35) + 0.45, y0=PH0, y1=PH1)
panel('k19.mp4', W - 110 - PW2, W - 110, wd(32, 0.7), en(35) + 0.45, y0=PH0, y1=PH1, origin='100% 0%')
for k, (png, lb, tt) in enumerate([('cut_fineknit.png', 'a fine knit', st(33)), ('cut_trouser.png', 'wool trousers', st(34)), ('cut_gloves2.png', 'leather gloves', st(35))]):
    cutout(png, 745 + k * 215, 430, 200, 440, tt, en(35) + 0.45, lb, lbs=38)
# 36 before / after: the same black, flat vs textured
x0 = (W - 2 * PW2 - 40) // 2
panel('k23.mp4', x0, x0 + PW2, st(36) - 0.05, en(36) + 0.45, y0=PH0 + 20, y1=PH1 + 20)
header('Flat', x0 + PW2 // 2, st(36) + 0.2, en(36) + 0.45)
panel('k20.mp4', x0 + PW2 + 40, x0 + 2 * PW2 + 40, wd(36, 0.35), en(36) + 0.45, y0=PH0 + 20, y1=PH1 + 20, origin='100% 0%')
header('Textured', x0 + PW2 + 40 + PW2 // 2, wd(36, 0.35) + 0.2, en(36) + 0.45)
# 37 camel coat over all black
canvas_full('k21.mp4', st(37) - 0.1, wd(37, 0.5))
single('k22.mp4', wd(37, 0.5), en(37) + 0.45, label='camel over black')
exec(open(os.path.join(P, 'coat.py')).read())
exec(open(os.path.join(P, 'points.py')).read())

# ---------- audio: voice + continuous warm piano bed (never runs out) + clear soft accents ----------
TRACKS = ['m644.mp3', 'm664.mp3', 'm672.mp3', 'm184.mp3', 'm571.mp3']
def load(f):
    sh(f"ffmpeg -nostdin -v error -y -i {A}/{f} -ac 1 -ar {sr} {A}/_m.wav"); y, _ = sf.read(f'{A}/_m.wav'); return y
xf = int(sr * 5); m = load(TRACKS[0]); k = 1
while len(m) < len(voice):
    nxt = load(TRACKS[k % len(TRACKS)]); k += 1
    nxt *= np.sqrt((m[-sr*20:] ** 2).mean() / ((nxt[:sr*20] ** 2).mean() + 1e-12))   # match loudness across the join
    ramp = np.linspace(0, 1, xf); m = np.concatenate([m[:-xf], m[-xf:] * (1 - ramp) + nxt[:xf] * ramp, nxt[xf:]])
m = m[:len(voice)]
m *= 10 ** ((-17.7 - 11) / 20) / np.sqrt((m ** 2).mean())             # bed ~11 dB under the voice
# gentle ducking: music lifts ~4 dB in the pauses between lines, settles under speech
env = np.full(len(voice), 10 ** (-1.5 / 20))
for d in T:
    a_ = int((d['end'] + 0.15) * sr); nxt_ = [x['start'] for x in T if x['start'] > d['end']]
    b_ = int((nxt_[0] - 0.25) * sr) if nxt_ else len(voice)
    if b_ - a_ > int(0.6 * sr): env[a_:b_] = 10 ** (2.5 / 20)
k_ = np.ones(int(0.35 * sr)) / int(0.35 * sr); env = np.convolve(env, k_, mode='same')
m *= env
m[:int(sr * 1.5)] *= np.linspace(0, 1, int(sr * 1.5)); m[-3 * sr:] *= np.linspace(1, 0, 3 * sr)
mix = voice + m; seen = []
for name, t0, g in sorted(SFX, key=lambda e: e[1]):
    if any(abs(t0 - s) < 0.15 for s in seen): continue
    seen.append(t0)
    sh(f"ffmpeg -nostdin -v error -y -i {A}/sfx_{name}.mp3 -af aecho=0.8:0.5:60:0.18 -ac 1 -ar {sr} {A}/_s.wav")
    s, _ = sf.read(f"{A}/_s.wav"); s = s.mean(1) if s.ndim > 1 else s
    s = s * 10 ** ((g + 7) / 20) / (np.abs(s).max() + 1e-9)               # +7 dB: clearly audible, still soft
    a = int(t0 * sr); b = min(len(mix), a + len(s)); mix[a:b] += s[:b - a]
sf.write(f'{A}/mix_raw.wav', mix / max(1.0, np.abs(mix).max()), sr)
sh(f"ffmpeg -nostdin -v error -y -i {A}/mix_raw.wav -af loudnorm=I=-14:TP=-1.0:LRA=7 -ar 48000 {A}/mix.wav")
html = open(os.path.join(P, 'template.tpl')).read()
html = html.replace('%DUR%', f'{total:.2f}').replace('%ELS%', '\n'.join(els)).replace('%TW%', '\n'.join(tw))
open(os.path.join(P, 'index.html'), 'w').write(html)
words = sum(len(b.split()) for b in beats)
print('SHORT:', SHORT)
print(f'total {total:.1f}s, {words/total*60:.0f} words/min overall, {len(els)} elements, {len(seen)} sfx, {len(USED)} unique clips')
