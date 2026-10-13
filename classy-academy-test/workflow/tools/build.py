# build.py - turns the approved script into the video page, in the channel's measured style:
# real credited clips only (each used once), caramel backdrop / panel rows / full-screen clips / white number cards,
# soft solo piano ~12 dB under the voice from first word to last, NO sound effects (none found in the channel's videos).
import os, re, subprocess, json, hashlib
import numpy as np, soundfile as sf

# usage (inside the video work folder, after setup.sh): python3 build.py   -> index.html + assets/mix.wav, then `npx hyperframes render`
# needs in the work folder: beats.txt, tts/cNNN.wav, raw/ + raw/meta.json, shots.json, edit.py (the beat-by-beat edit), assets/ music
TOOLS = os.path.dirname(os.path.abspath(__file__))
P = os.getcwd(); A = os.path.join(P, 'assets'); R = os.path.join(P, 'raw')
W, H = 1920, 1080
PW = 608
SHOTS = json.load(open(os.path.join(P, 'shots.json'))); META = json.load(open(os.path.join(R, 'meta.json')))
def sh(c): subprocess.run(c, shell=True, check=True)
# ---------- hard gate: never build with an AI-flagged clip (aiscan.json from tools/aiscan.py) ----------
AISCAN = json.load(open(os.path.join(P, 'aiscan.json'))) if os.path.exists(os.path.join(P, 'aiscan.json')) else None
assert AISCAN is not None, 'run tools/aiscan.py first (AI watermark scan of raw/ clips)'
# aiok.txt: clips that scored >= 0.40 but were checked by eye at full size and have NO sparkle ("key  why")
AIOK = {l.split()[0] for l in open(os.path.join(P, 'aiok.txt')) if l.strip()} if os.path.exists(os.path.join(P, 'aiok.txt')) else set()
AIFLAG = []


# ---------- voice timing ----------
beats = [l.strip() for l in open(os.path.join(P, 'beats.txt')) if l.strip()]
# pauses (measured on the channel): 0.55 s between lines, a breath after "Number X, ...", a longer one before
# each new point. Override any line in gaps.json, e.g. {"12": 1.15}.
gap = {i: 0.55 for i in range(1, len(beats) + 1)}
gap[1] = 0.8
for i, b in enumerate(beats, 1):
    if re.match(r'(Number|And finally, number) \w+\b', b): gap[i] = 0.75
    if i < len(beats) and re.match(r'(Number|And finally, number) \w+\b', beats[i]): gap[i] = 1.15
if os.path.exists(os.path.join(P, 'gaps.json')):
    gap.update({int(k): v for k, v in json.load(open(os.path.join(P, 'gaps.json'))).items()})
sr = 24000; t = 0.7; parts = [np.zeros(int(sr * 0.7))]; T = []
for i, b in enumerate(beats, 1):
    y, s = sf.read(os.path.join(P, 'tts', f'c{i:03d}.wav')); y = y.mean(1) if y.ndim > 1 else y
    d = len(y) / sr; T.append(dict(i=i, text=b, start=round(t, 3), end=round(t + d, 3)))
    parts += [y, np.zeros(int(sr * gap[i]))]; t += d + gap[i]
TAIL = 4.2
voice = np.concatenate(parts + [np.zeros(int(sr * TAIL))]); total = len(voice) / sr
sp = voice[np.abs(voice) > 1e-3]; voice *= 10 ** (-17.7 / 20) / np.sqrt((sp ** 2).mean())
json.dump(T, open(os.path.join(P, 'beats.json'), 'w'), indent=1)
B = {d['i']: d for d in T}
st = lambda i: B[i]['start']; en = lambda i: B[i]['end']
wd = lambda i, f: B[i]['start'] + (B[i]['end'] - B[i]['start']) * f
# at(12, "navy blazer"): the moment those words start in line 12 (words.json from tools/words.py); falls back to text position
WORDS = json.load(open(os.path.join(P, 'words.json'))) if os.path.exists(os.path.join(P, 'words.json')) else {}
def at(i, phrase, end=False):
    nw = lambda w: re.sub(r'[^a-z0-9]', '', w.lower())
    want = [nw(w) for w in phrase.split()]
    if str(i) in WORDS:
        ws = WORDS[str(i)]; have = [nw(w[0]) for w in ws]
        for k in range(len(have) - len(want) + 1):
            if have[k:k + len(want)] == want: return st(i) + (ws[k + len(want) - 1][2] if end else ws[k][1])
    k = B[i]['text'].lower().find(phrase.lower()); assert k >= 0, f'"{phrase}" not in line {i}'
    return wd(i, (k + (len(phrase) if end else 0)) / len(B[i]['text']))

# ---------- clip preparation: trim the checked segment, 9:16, SDR, silent; gentle slow-mo (<=1.4x) only if needed ----------
USED = {}; SHORT = []; CREDIT = []
CROP = {}   # edit.py: CROP['key'] = (x0, y0, h) -> that 9:16 window of the clip (720x1280 space) fills the frame
def prep(spec, need):
    key, a, b = spec
    seg = b - a; speed = 1.0
    still = seg < 0.05            # C(key, t, t): a held frame (the analysis moments: lines drawn on a still woman)
    if still: seg = need
    if need > seg: speed = min(1.4, need / seg)
    if need > seg * speed + 0.05: SHORT.append(f'{key} {a}-{b} needs {need:.1f}s has {seg*speed:.1f}s')
    name = f'{key}_{a:g}_{b:g}_{speed:.2f}' + ('_c%g_%g_%g' % CROP[key] if key in CROP else '') + '.mp4'; name = name.replace('-', 'm'); out = os.path.join(A, name)
    if not os.path.exists(out):
        src = os.path.join(R, key + '.mp4'); tm = ''
        if SHOTS.get(key, {}).get('hdr'):
            tm = 'zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,'
        cr = CROP.get(key)   # (x0, y0, h) in 720x1280 space: zoom past a burned-in caption, cut at 2x for sharpness
        if cr:
            x0, y0, hh = cr; ww = hh * 720 / 1280
            zc = f"scale=1440:2560:force_original_aspect_ratio=increase,crop=1440:2560,crop={2*ww:.0f}:{2*hh:.0f}:{2*x0:.0f}:{2*y0:.0f},scale=720:1280,"
        else: zc = "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,"
        vf = f"{tm}{zc}setsar=1,setpts={speed:.4f}*PTS,fps=30"
        if still:
            sh(f'ffmpeg -nostdin -v error -y -ss {a} -i {src} -frames:v 1 -an -vf "{vf}" {out}.png')
            sh(f'ffmpeg -nostdin -v error -y -loop 1 -t {seg+0.1:.3f} -i {out}.png -vf fps=30 -c:v libx264 -preset veryfast -crf 17 -g 30 -pix_fmt yuv420p -movflags +faststart {out}'); os.remove(out + '.png')
        else:
            sh(f'ffmpeg -nostdin -v error -y -ss {a} -t {seg:.3f} -i {src} -an -vf "{vf}" -c:v libx264 -preset veryfast -crf 17 -g 30 -keyint_min 30 -sc_threshold 0 -pix_fmt yuv420p -movflags +faststart {out}')
    return name
els, tw = [], []; uid = [0]
def nid(p): uid[0] += 1; return f"{p}{uid[0]}"
GRADE = 'filter:contrast(1.03) saturate(0.95) sepia(0.05);'
SEGS = {}   # key -> [(a, b)]: the same clip may come back only with different footage (e.g. her "before", then her "after")
def vid(spec, t0, t1, cls='med', style=GRADE, reuse_ok=False):
    key = spec[0]
    if not reuse_ok:
        for a, b in (SEGS.get(key, []) if spec[2] - spec[1] >= 0.05 else []):   # a held frame may come from footage that also plays
            assert spec[2] <= a + 0.05 or spec[1] >= b - 0.05, f'{key} {spec[1]}-{spec[2]} repeats footage already shown ({a}-{b}, at {USED.get(key)})'
        if AISCAN.get(key, 0) >= 0.40 and key not in AIOK: AIFLAG.append(f'{key} ({AISCAN[key]:.2f})')
        if key not in USED: USED[key] = round(t0, 1); CREDIT.append(key)
        SEGS.setdefault(key, []).append((spec[1], spec[2]))
    name = prep(spec, t1 - t0); i = nid('v')
    return i, f'<video id="{i}" class="{cls}" src="assets/{name}" muted playsinline data-start="{t0:.3f}" data-duration="{t1-t0:.3f}" style="{style}"></video>'
def box(x0, y0, x1, y1, inner, z=''):
    i = nid('b'); els.append(f'<div id="{i}" class="w" style="left:{x0}px;top:{y0}px;width:{x1-x0}px;height:{y1-y0}px;opacity:0;{z}">{inner}</div>'); return i
def drift(i, t0, t1, s=1.06): tw.append(f'tl.fromTo("#{i}",{{scale:1}},{{scale:{s},duration:{t1-t0+0.6:.2f},ease:"none"}},{t0:.3f});')
def fade_in(i, t, d=0.55): tw.append(f'tl.fromTo("#{i}",{{opacity:0}},{{opacity:1,duration:{d},ease:"sine.inOut"}},{t:.3f});')
def fade_out(i, t, d=0.55): tw.append(f'tl.to("#{i}",{{opacity:0,duration:{d},ease:"sine.inOut"}},{t:.3f});')
def grow_corner(i, t, origin="0% 0%"):
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.58}},{{opacity:1,scale:1,duration:0.8,ease:"power3.out",transformOrigin:"{origin}"}},{t:.3f});')
def grow_centre(i, t):
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.4}},{{opacity:1,scale:1,duration:1.2,ease:"power3.out",transformOrigin:"50% 50%"}},{t:.3f});')
def clabel(txt, cx, y, t0, t1):
    i = nid('cl'); els.append(f'<div id="{i}" class="cl" style="left:{cx-300}px;top:{y}px;width:600px;opacity:0">{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:0.8,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.5)
def panel(spec, x0, x1, t0, t1, entry='corner', y0=0, y1=H, origin="0% 0%", label=None, lby=None):
    v, h = vid(spec, t0, t1 + 0.55); drift(v, t0, t1 + 0.55)
    i = box(x0, y0, x1, y1, h)
    if entry == 'corner': grow_corner(i, t0, origin)
    elif entry == 'centre': grow_centre(i, t0)
    else: fade_in(i, t0, 0.6)
    fade_out(i, t1, 0.55)
    if label: clabel(label, (x0 + x1) // 2, (y1 - 120) if lby is None else lby, t0 + 0.45, t1)
    return i
def row(specs, times, t_end, labels=None):
    n = len(specs); w = W / n
    for k, (s, tt) in enumerate(zip(specs, times)):
        panel(s, max(0, round(k * w) - 1), min(W, round((k + 1) * w) + 1), tt, t_end, label=(labels or [None] * n)[k])
def pair(specs, times, t_end, labels=None, gapx=14):
    x = (W - 2 * PW - gapx) // 2
    for k, (s, tt) in enumerate(zip(specs, times)):
        x0 = x + k * (PW + gapx); panel(s, x0, x0 + PW, tt, t_end, origin=['0% 0%', '100% 0%'][k], label=(labels or [None, None])[k])
def single(spec, t0, t1, label=None):
    x0 = (W - PW) // 2; return panel(spec, x0, x0 + PW, t0, t1, entry='centre', label=label)
def canvas_full(spec, t0, t1, fin=0.7, fout=0.6):
    """Full screen from a vertical clip: soft blurred copy fills the frame, sharp clip centred."""
    e = t1 + fout
    bgv, bgh = vid(spec, t0, e, cls='', style=''); fgv, fgh = vid(spec, t0, e, reuse_ok=True)
    i = nid('cv'); els.append(f'<div id="{i}" class="w" style="left:0;top:0;width:{W}px;height:{H}px;opacity:0"><div class="canvas">{bgh}</div>'
                             f'<div class="w" style="left:{(W-PW)//2}px;top:0;width:{PW}px;height:{H}px;opacity:1">{fgh}</div></div>')
    drift(fgv, t0, e, 1.07); fade_in(i, t0, fin); fade_out(i, t1, fout); return i
def white(t0, t1, fin=0.45, fout=0.5):
    i = nid('wh'); els.append(f'<div id="{i}" class="white" style="opacity:0"></div>'); fade_in(i, t0, fin); fade_out(i, t1, fout); return i
def text(html, cls, t0, t1, dur=1.4, out=0.55, style=''):
    i = nid('tx'); els.append(f'<div id="{i}" class="{cls}" style="opacity:0;{style}">{html}</div>')
    tw.append(f'tl.set("#{i}",{{opacity:1}},{t0:.3f});')
    tw.append(f'tl.fromTo("#{i}",{{"--p":100}},{{"--p":0,duration:{dur},ease:"none"}},{t0:.3f});')
    fade_out(i, t1, out); return i
def quote_side(spec, t0, t1, l1, l2, t2):
    panel(spec, 170, 170 + PW, t0, t1, entry='fade')
    text(l1, 'qs1', t0 + 0.35, t1, dur=1.4); text(l2, 'qs2', t2, t1, dur=1.2)
def header(txt, cx, t0, t1, y=38):
    i = nid('hd'); els.append(f'<div id="{i}" class="hd" style="left:{cx-258}px;top:{y}px;opacity:0">{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:10}},{{opacity:1,y:0,duration:0.7,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.5)
PH0, PH1, PW2 = 96, 1014, 516
def compare(a, b, ha, hb, t0, tb, t1):
    x0 = (W - 2 * PW2 - 40) // 2
    panel(a, x0, x0 + PW2, t0, t1, y0=PH0 + 20, y1=PH1 + 20); header(ha, x0 + PW2 // 2, t0 + 0.2, t1)
    panel(b, x0 + PW2 + 40, x0 + 2 * PW2 + 40, tb, t1, y0=PH0 + 20, y1=PH1 + 20, origin='100% 0%'); header(hb, x0 + PW2 + 40 + PW2 // 2, tb + 0.2, t1)
def card(txt, i_line, t_in=None, style=''):
    """White chapter card, black script wiping in left to right (their number cards). style='font-size:96px' for long names."""
    t0 = (en(i_line - 1) + 0.35) if t_in is None else t_in
    white(t0, en(i_line) + 0.35); text(txt, 'card', t0 + 0.3, en(i_line) + 0.25, dur=1.2, out=0.45, style=style)
C = lambda k, a, b: (k, a, b)

# ---------- the "stage" edit (from the 79-video replay study, research/edit-evidence): one calm frame per point ----------
# The frame stays put for the whole point; the pictures change INSIDE it (soft 0.4 s dissolve, a new picture every <=5 s),
# so the eye never has to re-find the picture. Same woman before -> after where the footage allows.
def stage(shots, t1, x0=None, w=PW, y0=0, y1=H, xf=0.4, entry='fade'):
    """shots = [(spec, t), ...]: each picture comes in at t; the frame appears with the first, leaves at t1."""
    x0 = (W - w) // 2 if x0 is None else x0
    inner = []; t0 = shots[0][1]
    for k, (spec, t) in enumerate(shots):
        assert k == 0 or t > shots[k - 1][1] + 0.8, f'stage shots too close at {t:.1f}'
        tend = (shots[k + 1][1] + xf) if k + 1 < len(shots) else t1 + 0.55
        v, h = vid(spec, t, tend, style=GRADE + 'position:absolute;left:0;top:0;')
        drift(v, t, tend, 1.05)
        if k: tw.append(f'tl.fromTo("#{v}",{{opacity:0}},{{opacity:1,duration:{xf},ease:"sine.inOut"}},{t:.3f});')
        inner.append(h)
    i = box(x0, y0, x0 + w, y1, ''.join(inner))
    if entry == 'centre': grow_centre(i, t0)
    else: fade_in(i, t0, 0.5)
    fade_out(i, t1, 0.55); return i
MK = {'no': ('#a8432f', 'M17 17 L37 37 M37 17 L17 37'), 'yes': ('#4f6b3a', 'M14 28 L24 38 L41 16')}
def mark(kind, word, t0, t1, cx=1592, y=330):
    """The avoid / instead label beside the frame: a white disc with a red cross or a green tick, and one or two words."""
    col, d = MK[kind]; i = nid('mk')
    els.append(f'<div id="{i}" class="cl" style="left:{cx-300}px;top:{y}px;width:600px;opacity:0">'
               f'<svg viewBox="0 0 54 54" style="display:block;margin:0 auto 6px;width:104px;height:104px">'
               f'<circle cx="27" cy="27" r="26.5" fill="rgba(70,35,15,.16)"/><circle cx="27" cy="27" r="24.5" fill="#fbf7f2"/>'
               f'<path d="{d}" style="fill:none;stroke:{col};stroke-width:4.6;stroke-linecap:round;stroke-linejoin:round"/></svg>{word}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.85}},{{opacity:1,scale:1,duration:0.6,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.4)


# ---------- the "demo" edit (body shape, Oct 2026): ONE real woman per point, the tip drawn on her, a list building beside her ----------
# Evidence (research-2026-10-12-edit-evidence.md + the 13 body-shape winners' replay peaks, videos/body-shape/edit-evidence.md):
# the biggest peak in the topic is a real woman doing the hand test with a label and an arrow on her (10.7x the median);
# a red arrow on the garment detail 5.2x; a checklist building beside the try-on 1.7-1.9x; one-real-woman videos 2.45% liked vs 1.03%.
FX0 = 330                      # the demo frame: x FX0..FX0+PW, full height; the list sits on the right
LX = 1040                      # left edge of the list / labels column
def to_screen(px, py, x0=None, w=PW, h=H):
    """a point in the prepared 720x1280 clip -> screen pixels, for a frame at x0 (no drift on annotated shots)"""
    x0 = FX0 if x0 is None else x0; s = max(w / 720, h / 1280)
    return x0 + w / 2 + (px - 360) * s, h / 2 + (py - 640) * s
def demo(shots, t1, x0=None, w=PW, xf=0.35, entry='fade'):
    """shots = [(spec, t) or (spec, t, drift)]: one frame for the point, one woman inside it; drift 1.0 on shots that carry annotations"""
    x0 = FX0 if x0 is None else x0
    inner = []; t0 = shots[0][1]
    for k, sh_ in enumerate(shots):
        spec, t = sh_[0], sh_[1]; dr = sh_[2] if len(sh_) > 2 else 1.04
        assert k == 0 or t > shots[k - 1][1] + 0.8, f'demo shots too close at {t:.1f}'
        tend = (shots[k + 1][1] + xf) if k + 1 < len(shots) else t1 + 0.55
        v, h = vid(spec, t, tend, style=GRADE + 'position:absolute;left:0;top:0;')
        if dr != 1.0: drift(v, t, tend, dr)
        if k: tw.append(f'tl.fromTo("#{v}",{{opacity:0}},{{opacity:1,duration:{xf},ease:"sine.inOut"}},{t:.3f});')
        inner.append(h)
    i = box(x0, 0, x0 + w, H, ''.join(inner), z='box-shadow:0 26px 60px rgba(60,30,12,.28);')
    if entry == 'centre': grow_centre(i, t0)
    else: fade_in(i, t0, 0.5)
    fade_out(i, t1, 0.55); return i
def _ann(inner, x0, y0, w, h, t0, t1, mode='wipe', dur=0.8):
    i = nid('an')
    els.append(f'<div id="{i}" class="ann" style="left:{x0:.0f}px;top:{y0:.0f}px;width:{w:.0f}px;height:{h:.0f}px;opacity:0">'
               f'<svg width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}">{inner}</svg></div>')
    if mode == 'wipe':
        tw.append(f'tl.set("#{i}",{{opacity:1}},{t0:.3f});')
        tw.append(f'tl.fromTo("#{i}",{{"--p":100}},{{"--p":0,duration:{dur},ease:"power1.inOut"}},{t0:.3f});')
    else:
        tw.append(f'tl.set("#{i}",{{"--p":0}},{t0:.3f});')
        tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.82}},{{opacity:1,scale:1,duration:0.55,ease:"power2.out"}},{t0:.3f});')
    fade_out(i, t1, 0.4); return i
ACOL = '#fbf7f2'
def hline(y, xa, xb, t0, t1, dash=False, ticks=True):
    """a line drawn across her (screen coords), left to right, e.g. the waist, the thirds line, a width"""
    pad = 14; d = ' stroke-dasharray="16 12"' if dash else ''
    tk = (f'<line x1="{pad}" y1="{pad-12}" x2="{pad}" y2="{pad+12}"/><line x1="{xb-xa+pad}" y1="{pad-12}" x2="{xb-xa+pad}" y2="{pad+12}"/>' if ticks else '')
    inner = f'<g stroke="{ACOL}" stroke-width="5" stroke-linecap="round" fill="none"><line x1="{pad}" y1="{pad}" x2="{xb-xa+pad}" y2="{pad}"{d}/>{tk}</g>'
    return _ann(inner, xa - pad, y - pad, xb - xa + 2 * pad, 2 * pad, t0, t1)
def vline(x, ya, yb, t0, t1, dash=False):
    pad = 14; d = ' stroke-dasharray="16 12"' if dash else ''
    inner = f'<g stroke="{ACOL}" stroke-width="5" stroke-linecap="round" fill="none"><line x1="{pad}" y1="{pad}" x2="{pad}" y2="{yb-ya+pad}"{d}/></g>'
    return _ann(inner, x - pad, ya - pad, 2 * pad, yb - ya + 2 * pad, t0, t1, mode='pop')
def ring(cx, cy, rx, ry, t0, t1):
    """an oval drawn around the detail (the neckline, the waist, the shoe)"""
    pad = 10; w, h = 2 * rx + 2 * pad, 2 * ry + 2 * pad
    inner = f'<ellipse cx="{w/2}" cy="{h/2}" rx="{rx}" ry="{ry}" stroke="{ACOL}" stroke-width="5" fill="none"/>'
    return _ann(inner, cx - w / 2, cy - h / 2, w, h, t0, t1, mode='pop')
def vshape(cx, ytop, half, depth, t0, t1):
    """the V of a neckline (or of a long pendant), drawn on her"""
    pad = 12; w, h = 2 * half + 2 * pad, depth + 2 * pad
    inner = f'<path d="M{pad} {pad} L{w/2} {depth+pad} L{w-pad} {pad}" stroke="{ACOL}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    return _ann(inner, cx - w / 2, ytop - pad, w, h, t0, t1)
def arrow(x0_, y0_, x1_, y1_, t0, t1):
    """an arrow from (x0,y0) to (x1,y1), screen coords: it points at the detail being named"""
    pad = 24; xa, ya, xb, yb = min(x0_, x1_), min(y0_, y1_), max(x0_, x1_), max(y0_, y1_)
    ax, ay, bx, by = x0_ - xa + pad, y0_ - ya + pad, x1_ - xa + pad, y1_ - ya + pad
    import math as _m
    ang = _m.atan2(by - ay, bx - ax); hl = 22
    p1 = (bx - hl * _m.cos(ang - 0.5), by - hl * _m.sin(ang - 0.5)); p2 = (bx - hl * _m.cos(ang + 0.5), by - hl * _m.sin(ang + 0.5))
    inner = (f'<g stroke="{ACOL}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none">'
             f'<line x1="{ax:.0f}" y1="{ay:.0f}" x2="{bx:.0f}" y2="{by:.0f}"/><path d="M{p1[0]:.0f} {p1[1]:.0f} L{bx:.0f} {by:.0f} L{p2[0]:.0f} {p2[1]:.0f}"/></g>')
    return _ann(inner, xa - pad, ya - pad, xb - xa + 2 * pad, yb - ya + 2 * pad, t0, t1, mode='wipe' if x1_ >= x0_ else 'pop')
def tag(txt, x, y, t0, t1, anchor='left'):
    """a small cream label next to a line or an arrow ("short torso", "the narrowest point")"""
    i = nid('al'); left = x if anchor == 'left' else x - 600
    al = 'left' if anchor == 'left' else 'right'
    els.append(f'<div id="{i}" class="alab" style="left:{left:.0f}px;top:{y:.0f}px;width:600px;text-align:{al};opacity:0"><span>{txt}</span></div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:10}},{{opacity:1,y:0,duration:0.55,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.4); return i
CK = {'yes': 'M14 28 L24 38 L41 16', 'no': 'M17 17 L37 37 M37 17 L17 37'}
CKC = {'yes': '#4f6b3a', 'no': '#a8432f'}
def steps(items, t_end, x=LX, y0=360, dy=118):
    """the list building beside her: items = [(kind 'yes'/'no', words, t)], each with a disc + tick/cross (the screenshot of the point)"""
    for k, (kind, txt, tt) in enumerate(items):
        i = nid('ck')
        els.append(f'<div id="{i}" class="chk ckl" style="left:{x+78}px;top:{y0 + k*dy}px;opacity:0">'
                   f'<svg viewBox="0 0 54 54"><circle cx="27" cy="27" r="25" fill="#fbf7f2"/><path id="{i}p" d="{CK[kind]}" style="stroke:{CKC[kind]};stroke-width:5.2"/></svg>{txt}</div>')
        tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-24}},{{opacity:1,x:0,duration:0.6,ease:"power2.out"}},{tt:.3f});')
        tw.append(f'tl.to("#{i}p",{{strokeDashoffset:0,duration:0.45,ease:"power2.out"}},{tt+0.25:.3f});')
        fade_out(i, t_end, 0.5)
def kicker(txt, t0, t1, x=LX, y=215):
    """the point's name, small, above its list (where she is in the video)"""
    i = nid('kk'); els.append(f'<div id="{i}" class="kick" style="left:{x}px;top:{y}px;opacity:0">{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:10}},{{opacity:1,y:0,duration:0.7,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.5); return i

exec(open(os.path.join(P, 'edit.py')).read())
if AIFLAG: raise SystemExit('STOP - AI watermark suspected, replace these clips: ' + ', '.join(AIFLAG))

# ---------- end card ----------
i = nid('ew'); els.append(f'<div id="{i}" class="endwhite" style="opacity:0"></div>'); fade_in(i, total - 3.0, 0.9)
j = nid('el'); els.append(f'<img id="{j}" class="endlogo" src="assets/logo_ce_dark.png" style="opacity:0">')
tw.append(f'tl.fromTo("#{j}",{{opacity:0,scale:0.96}},{{opacity:1,scale:1,duration:1.3,ease:"power2.out"}},{total-2.4:.3f});')

# ---------- audio: voice + soft solo piano, steady ~12 dB under the voice, no sound effects ----------
TRACKS = ['m711.mp3', 'm716.mp3', 'm712.mp3', 'm717.mp3']
def load(f):
    sh(f"ffmpeg -nostdin -v error -y -i {A}/{f} -af 'highpass=f=40,equalizer=f=150:t=q:w=1:g=2,equalizer=f=3500:t=q:w=1.2:g=2' -ac 1 -ar {sr} {A}/_m.wav")
    y, _ = sf.read(f'{A}/_m.wav'); return y
def trim_silence(y):
    e = np.abs(y) > 10 ** (-50 / 20); idx = np.where(e)[0]; return y[idx[0]:idx[-1]] if len(idx) else y
xf = int(sr * 4); m = trim_silence(load(TRACKS[0])); k = 1
while len(m) < len(voice):
    nxt = trim_silence(load(TRACKS[k % len(TRACKS)])); k += 1
    nxt *= np.sqrt((m[-sr*20:] ** 2).mean() / ((nxt[:sr*20] ** 2).mean() + 1e-12))
    ramp = np.linspace(0, 1, xf); m = np.concatenate([m[:-xf], m[-xf:] * (1 - ramp) + nxt[:xf] * ramp, nxt[xf:]])
m = m[:len(voice)]
m *= 10 ** ((-17.7 - 12) / 20) / np.sqrt((m ** 2).mean())
m[:int(sr * 1.2)] *= np.linspace(0, 1, int(sr * 1.2)); m[-int(3.5 * sr):] *= np.linspace(1, 0, int(3.5 * sr))
mix = voice + m
sf.write(f'{A}/mix_raw.wav', mix / max(1.0, np.abs(mix).max()), sr)
sh(f"ffmpeg -nostdin -v error -y -i {A}/mix_raw.wav -af loudnorm=I=-14:TP=-1.0:LRA=9 -ar 48000 {A}/mix.wav")
html = open(os.path.join(TOOLS, 'template.tpl')).read().replace('%TITLE%', open(os.path.join(P, 'title.txt')).read().strip() if os.path.exists(os.path.join(P, 'title.txt')) else 'The Classy Elegance')
html = html.replace('%DUR%', f'{total:.2f}').replace('%ELS%', '\n'.join(els)).replace('%TW%', '\n'.join(tw))
open(os.path.join(P, 'index.html'), 'w').write(html)
cr = []
for k_ in CREDIT:
    mt = META.get(k_, {}); cr.append(f"{mt.get('creator','?')} (@{mt.get('user','?')}) {mt.get('url','')}")
open(os.path.join(P, 'CREDITS.txt'), 'w').write('\n'.join(dict.fromkeys(cr)) + '\n\nMusic: "Classical 4", "Classical 9", "Classical 5", "Classical 10" by Jonny S. (Mixkit, free license)\n')
words = sum(len(b.split()) for b in beats)
print('SHORT:', SHORT)
print(f'total {total:.1f}s, {words/total*60:.0f} words/min, {len(els)} elements, {len(USED)} unique clips')
