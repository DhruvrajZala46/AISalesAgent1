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

# ---------- clip preparation: trim the checked segment, 9:16, SDR, silent; gentle slow-mo (<=1.4x) only if needed ----------
USED = {}; SHORT = []; CREDIT = []
def prep(spec, need):
    key, a, b = spec
    seg = b - a; speed = 1.0
    if need > seg: speed = min(1.4, need / seg)
    if need > seg * speed + 0.05: SHORT.append(f'{key} {a}-{b} needs {need:.1f}s has {seg*speed:.1f}s')
    name = f'{key}_{a:g}_{b:g}_{speed:.2f}.mp4'.replace('-', 'm'); out = os.path.join(A, name)
    if not os.path.exists(out):
        src = os.path.join(R, key + '.mp4'); tm = ''
        if SHOTS.get(key, {}).get('hdr'):
            tm = 'zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,'
        vf = f"{tm}scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1,setpts={speed:.4f}*PTS,fps=30"
        sh(f'ffmpeg -nostdin -v error -y -ss {a} -t {seg:.3f} -i {src} -an -vf "{vf}" -c:v libx264 -preset veryfast -crf 17 -g 30 -keyint_min 30 -sc_threshold 0 -pix_fmt yuv420p -movflags +faststart {out}')
    return name
els, tw = [], []; uid = [0]
def nid(p): uid[0] += 1; return f"{p}{uid[0]}"
GRADE = 'filter:contrast(1.03) saturate(0.95) sepia(0.05);'
def vid(spec, t0, t1, cls='med', style=GRADE, reuse_ok=False):
    key = spec[0]
    if not reuse_ok:
        assert key not in USED, f'{key} used twice ({USED.get(key)} and {t0:.1f})'
        if AISCAN.get(key, 0) >= 0.40 and key not in AIOK: AIFLAG.append(f'{key} ({AISCAN[key]:.2f})')
        USED[key] = round(t0, 1); CREDIT.append(key)
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
def card(txt, i_line, t_in=None):
    """White chapter card, black script wiping in left to right (their number cards)."""
    t0 = (en(i_line - 1) + 0.35) if t_in is None else t_in
    white(t0, en(i_line) + 0.35); text(txt, 'card', t0 + 0.3, en(i_line) + 0.25, dur=1.2, out=0.45)
C = lambda k, a, b: (k, a, b)

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
