# 8 Things That Quietly Age You: What to Wear Instead - the edit, beat by beat.
# Built ONLY from the layouts of the channel's #1 video, "8 Things Elegant Ladies Never Wear: What to Wear Instead"
# (My7qteRU9k0), read off its storyboard (videos/age-swaps/VISUAL-ANALYSIS.md):
#   A full-screen clip | B white card, black script | C title over a clip | D one vertical clip centred on caramel |
#   E row of clips edge to edge, one per spoken item | F the principle line on caramel | G clip left + quote right |
#   H/I two framed clips with a list or labels | K guide over clips | L outro over a clip + CA end card
# Footage: Pinterest video pins (Instagram/TikTok creators' reels) and film scenes found there. No free-stock sites.
# Every clip appears ONCE; none from the #1 video or the two previous videos. No sound effects; soft piano ~12 dB under.
# Bad first, good second: the mistake in a row, then the swap. No website on screen.

import os as _os

import os as _os

els.append('''<style>
.cream { position:absolute; inset:0; background:#f6f0e9; }
.whitebg { position:absolute; inset:0; background:#ffffff; }
.qx { position:absolute; z-index:45; display:flex; align-items:center; justify-content:center; text-align:center;
  color:#fff; font-family:"Playfair"; line-height:1.32; text-shadow:0 2px 18px rgba(60,40,25,.30);
  --p:100; -webkit-mask-image:linear-gradient(90deg,#000 45%,transparent 55%); mask-image:linear-gradient(90deg,#000 45%,transparent 55%);
  -webkit-mask-size:220% 100%; mask-size:220% 100%; -webkit-mask-position:calc(var(--p)*1%) 0; mask-position:calc(var(--p)*1%) 0; }
.qx i { font-family:"Pinyon"; font-style:normal; font-size:1.32em; line-height:0.8; }
.qx.dark { color:#4b3f37; text-shadow:none; }
.qx.over { text-shadow:0 2px 22px rgba(0,0,0,.55), 0 0 2px rgba(0,0,0,.35); }
.ttl .s { display:block; font-size:40px; letter-spacing:2px; margin-bottom:6px; }
.card { color:#3b3b3b !important; }
</style>''')

nx = lambda i: st(i) - 0.1           # a picture comes in just before its line
FILL = {}                             # key -> vertical centre (0..1) of the 16:9 window cut from a portrait clip

# ---- full-screen / wide preparation: a 1920x1080 window cut from the clip (portrait clips: at FILL[key]) ----
_prep_base = prep
def prep(spec, need):
    key, a, b = spec
    if key not in FILL: return _prep_base(spec, need)
    seg = b - a; speed = 1.0
    if need > seg: speed = min(1.4, need / seg)
    if need > seg * speed + 0.05: SHORT.append(f'{key} {a}-{b} needs {need:.1f}s has {seg*speed:.1f}s')
    fy = FILL[key]; name = f'F_{key}_{a:g}_{b:g}_{speed:.2f}_{fy:g}.mp4'.replace('-', 'm'); out = os.path.join(A, name)
    if not os.path.exists(out):
        w, h = SHOTS[key]['w'], SHOTS[key]['h']
        tm = ('zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,'
              if SHOTS[key].get('hdr') else '')
        if w / h >= 1.70: zc = 'scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080,'
        else:
            H2 = int(round(1920 * h / w / 2) * 2); y = int(round(fy * (H2 - 1080)))
            zc = f'scale=1920:{H2}:flags=lanczos,crop=1920:1080:0:{y},unsharp=5:5:0.55,'
        vf = f'{tm}{zc}setsar=1,setpts={speed:.4f}*PTS,fps=30'
        sh(f'ffmpeg -nostdin -v error -y -ss {a} -t {seg:.3f} -i {R}/{key}.mp4 -an -vf "{vf}" -c:v libx264 -preset veryfast -crf 17 -g 30 -keyint_min 30 -sc_threshold 0 -pix_fmt yuv420p -movflags +faststart {os.path.join(A, name)}')
    return name

def _frames(shots, t1, x0, y0, w, h, radius=0, shadow=False, xf=0.45, dr=1.04, entry='fade'):
    inner = []; t0 = shots[0][1]
    for k, sh_ in enumerate(shots):
        spec, t = sh_[0], sh_[1]
        assert k == 0 or t > shots[k - 1][1] + 0.8, f'shots too close at {t:.1f}'
        tend = (shots[k + 1][1] + xf) if k + 1 < len(shots) else t1 + 0.55
        v, hh = vid(spec, t, tend, style=GRADE + 'position:absolute;left:0;top:0;')
        if dr != 1.0: drift(v, t, tend, dr)
        if k: tw.append(f'tl.fromTo("#{v}",{{opacity:0}},{{opacity:1,duration:{xf},ease:"sine.inOut"}},{t:.3f});')
        inner.append(hh)
    z = (f'border-radius:{radius}px;' if radius else '') + ('box-shadow:0 24px 56px rgba(60,30,12,.26);' if shadow else '')
    i = box(x0, y0, x0 + w, y0 + h, ''.join(inner), z=z)
    if entry == 'centre': grow_centre(i, t0)
    else: fade_in(i, t0, 0.5)
    fade_out(i, t1, 0.55); return i

FACE = json.load(open(os.path.join(P, 'facepos.json')))     # tools/facepos.py: median face height (0..1) in each shot
FACEFIX = {}                                              # detector misses, read by eye (filled after the frame check)
def _fy(spec):
    """the vertical position of the 16:9 window in a portrait clip: the face sits at 38% of the screen height"""
    k, a, b = spec; F = FACEFIX.get(k, FACE.get(f'{k} {a:g} {b:g}'))
    if F is None or not 0.12 < F < 0.8: F = 0.33
    w, h = SHOTS[k]['w'], SHOTS[k]['h']; H2 = 1920 * h / w
    if H2 <= 1081: return 0.5
    return round(min(1.0, max(0.0, (F * H2 - 0.38 * 1080) / (H2 - 1080))), 3)
def full(shots, t1, fy=None, **kw):
    """A: full-screen clip(s). shots = [(spec, t) or (spec, t, fy)]; the window follows the faces (facepos.json)"""
    for sh_ in shots: FILL[sh_[0][0]] = _fy(sh_[0])
    return _frames([s[:2] for s in shots], t1, 0, 0, W, H, **kw)

VW, VH = 562, 1000                                       # the rounded vertical frame (9:16), 40 px from top and bottom
def vframe(shots, t1, x0=None):
    """D (x0=None: centred) / E (x0=40): rounded vertical frame on the caramel backdrop"""
    return _frames(shots, t1, (W - VW) // 2 if x0 is None else x0, 40, VW, VH, radius=34, shadow=True)

WW, WH, WX, WY = 1310, 737, 305, 300                     # J: the wide rounded frame under a quote
def wide(shots, t1, fy=0.4):
    for sh_ in shots: FILL[sh_[0][0]] = _fy(sh_[0])
    return _frames([s[:2] for s in shots], t1, WX, WY, WW, WH, radius=34, shadow=True)

def cream(t0, t1):
    i = nid('cr'); els.append(f'<div id="{i}" class="cream" style="opacity:0"></div>'); fade_in(i, t0 - 0.05, 0.45); fade_out(i, t1, 0.5); return i

def oncream(shots, t1, x0=None):
    """L (x0=None: centred) / M (x0=75): a vertical clip, full height, square corners, on cream"""
    cream(shots[0][1], t1)
    return _frames(shots, t1, (W - PW) // 2 if x0 is None else x0, 0, PW, H)

def q(html, t0, t1, box_=(660, 0, 1880, H), size=58, cls='', dur=1.4):
    """the quote: white serif, a word or two in script, wiping in left to right (the channel's text reveal)"""
    x0, y0, x1, y1 = box_
    return text(f'<div>{html}</div>', 'qx ' + cls, t0, t1, dur=dur,
                style=f'left:{x0}px;top:{y0}px;width:{x1-x0}px;height:{y1-y0}px;font-size:{size}px;')
QR = (650, 60, 1860, 1020)                               # right of an E frame
QC = (180, 0, 1740, H)                                   # centred (F, K)
QT = (180, 60, 1740, 290)                                # above the J frame
MT = (760, 60, 1840, 1020)                               # right of an M clip (dark text)


def card_at(txt, i_line, t_out, size=None):
    """D: the white card, grey-black script wiping in; it stays over the first words of the point, as in Part 1"""
    t0 = en(i_line - 1) + 0.35
    white(t0, t_out); text(txt, 'card', t0 + 0.3, t_out - 0.1, dur=1.2, out=0.45, style=f'font-size:{size}px;' if size else '')

def onwhite(shots, t1):
    """E: a vertical clip, full height, square corners, centred on white"""
    i = nid('wb'); els.append(f'<div id="{i}" class="whitebg" style="opacity:0"></div>')
    fade_in(i, shots[0][1] - 0.05, 0.45); fade_out(i, t1, 0.5)
    return _frames(shots, t1, (W - PW) // 2, 0, PW, H)

def halves(specs, times, t_end):
    """H: two vertical panels edge to edge, half and half"""
    for k, (s, tt) in enumerate(zip(specs, times)):
        panel(s, [0, 959][k], [961, 1920][k], tt, t_end, origin=['0% 0%', '100% 0%'][k])

SW = 770
def side(shots, t1):
    """I: a clip filling the left 40%, the quote on the caramel backdrop at the right"""
    return _frames(shots, t1, 0, 0, SW, H)
QI = (830, 60, 1870, 1020)                               # right of an I clip

def centre(shots, t1):
    """D: one vertical clip (or a few in turn) centred on the caramel backdrop, growing from the centre"""
    return _frames(shots, t1, (W - PW) // 2, 0, PW, H, entry='centre')

def prow(specs, times, t_end, n=3):
    """E: a row of vertical clips from the left, one per spoken item; with fewer clips than n the backdrop shows on the right"""
    w = W / n
    for k, (s, tt) in enumerate(zip(specs, times)):
        panel(s, max(0, round(k * w) - 1), min(W, round((k + 1) * w) + 1), tt, t_end)

FW, FH, FX, FY = 520, 924, 70, 78                        # G: the framed clip at the left of a quote
def gside(shots, t1):
    """G: a framed vertical clip at the left on caramel, the quote at the right (q(..., QG))"""
    return _frames(shots, t1, FX, FY, FW, FH, radius=6, shadow=True)
QG = (650, 60, 1860, 1020)

def twoframes(a, b, t0, tb, t1, la=None, lb=None, mid=None, tm=None):
    """H/I: two framed clips on caramel; labels above each (I) or a short list between them (H)"""
    xa, xb, y0, w_, h_ = 300, 1100, 150, 520, 860
    if mid: xa, xb = 150, 1250
    _frames([(a, t0)], t1, xa, y0, w_, h_, radius=6, shadow=True)
    _frames([(b, tb)], t1, xb, y0, w_, h_, radius=6, shadow=True)
    if la: q(la, t0 + 0.3, t1, (xa - 40, 40, xa + w_ + 40, 140), size=56, dur=0.9)
    if lb: q(lb, tb + 0.3, t1, (xb - 40, 40, xb + w_ + 40, 140), size=56, dur=0.9)
    if mid:
        for k, (txt, tt) in enumerate(zip(mid, tm)):
            q(txt, tt, t1, (690, 330 + k * 140, 1230, 450 + k * 140), size=48, dur=0.9)

# ======================= v2 (user review, 3 Nov 2026): The Classy Elegance channel's own layouts =======================
# Read off the storyboards of the channel's own videos (7 Things Elegant French Women Never Wear, 8 Things That Make You
# Look Older, 7 Things Elegant Ladies Never Wear in Winter, 8 Ways to Always Look Put Together):
#  - full screen from a vertical reel = the WHOLE clip, sharp, in the centre, over a soft blurred copy of itself
#    (never a 16:9 crop of a vertical clip: that cut faces in v1)
#  - one clip at the left (or left third) of the caramel backdrop, the line to remember beside it
#  - rows of whole 9:16 clips from the left edge, one per spoken item, caramel showing at the right
#  - product photos cut out on the caramel with their name in script; real photos in frames
from PIL import Image as _PILImage
CANV = set()                                   # specs prepared as blurred-backdrop full screens
_prep_fill2 = prep
def prep(spec, need):
    if tuple(spec) not in CANV: return _prep_fill2(spec, need)
    key, a, b = spec
    seg = b - a; speed = 1.0
    if need > seg: speed = min(1.4, need / seg)
    if need > seg * speed + 0.05: SHORT.append(f'{key} {a}-{b} needs {need:.1f}s has {seg*speed:.1f}s')
    name = f'K_{key}_{a:g}_{b:g}_{speed:.2f}' + ('_c%g_%g_%g' % CROP[key] if key in CROP else '') + '.mp4'
    name = name.replace('-', 'm'); out = os.path.join(A, name)
    if not os.path.exists(out):
        w, h = SHOTS[key]['w'], SHOTS[key]['h']
        tm = ('zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,'
              if SHOTS[key].get('hdr') else '')
        pre = ''
        if key in CROP:
            x0, y0, hh = CROP[key]; ww = hh * 720 / 1280
            pre = f'scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,crop={ww:.0f}:{hh:.0f}:{x0:.0f}:{y0:.0f},'
        if w / h >= 1.70 and key not in CROP:
            fc = f'[0:v]{tm}scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080,setsar=1,setpts={speed:.4f}*PTS,fps=30[o]'
        else:
            fc = (f'[0:v]{tm}{pre}setsar=1,split[a][b];[a]scale=480:270:force_original_aspect_ratio=increase,crop=480:270,boxblur=12:2,'
                  f'scale=1920:1080,eq=brightness=-0.04:saturation=0.92[bg];[b]scale=-2:1080:flags=lanczos[fg];'
                  f'[bg][fg]overlay=(W-w)/2:0,setsar=1,setpts={speed:.4f}*PTS,fps=30[o]')
        sh(f'ffmpeg -nostdin -v error -y -ss {a} -t {seg:.3f} -i {R}/{key}.mp4 -an -filter_complex "{fc}" -map "[o]" -c:v libx264 -preset veryfast -crf 17 -g 30 -keyint_min 30 -sc_threshold 0 -pix_fmt yuv420p -movflags +faststart {out}')
    return name

def cfull(shots, t1):
    """A: full screen the channel's way - the whole vertical clip in the centre over its own soft blurred copy"""
    for s in shots: CANV.add(tuple(s[0]))
    return _frames([s[:2] for s in shots], t1, 0, 0, W, H, dr=1.025)

def lclip(shots, t1, x=0):
    """one whole vertical clip (or a few in turn) on the caramel backdrop: x=0 at the left edge, x=330 the left third"""
    return _frames(shots, t1, x, 0, PW, H)
QL = (PW + 50, 60, 1870, 1020)                         # beside a clip at x=0
QL3 = (330 + PW + 40, 60, 1880, 1020)                  # beside a clip at the left third

def lrow(specs, times, t_end, w=PW, x0=0, labels=None):
    """a row of whole vertical clips from the left edge, one per spoken item (caramel shows at the right)"""
    for k, (s, tt) in enumerate(zip(specs, times)):
        panel(s, x0 + k * w, x0 + (k + 1) * w, tt, t_end, label=(labels or [None] * len(specs))[k])

def _rise(i, t0, t1):
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:34}},{{opacity:1,y:0,duration:0.8,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.5)
PHOTOS = []
def prod(png, cx, ybot, hh, t0, t1, label=None, maxw=430, lsize=60):
    """a product photo cut out on the caramel backdrop (the channel's packshots), its name in script underneath"""
    im = _PILImage.open(os.path.join(A, png)); r = im.width / im.height
    h2 = hh; w2 = hh * r
    if w2 > maxw: w2 = maxw; h2 = w2 / r
    i = nid('pd'); PHOTOS.append(png)
    els.append(f'<div id="{i}" style="position:absolute;z-index:46;left:{cx-w2/2:.0f}px;top:{ybot-h2:.0f}px;width:{w2:.0f}px;height:{h2:.0f}px;opacity:0">'
               f'<img src="assets/{png}" style="width:100%;height:100%;display:block;filter:drop-shadow(0 22px 26px rgba(70,35,15,.38))"></div>')
    _rise(i, t0, t1)
    if label: plabel(label, cx, ybot + 6, t0 + 0.35, t1, lsize)
def plabel(txt, cx, y, t0, t1, size=60):
    t0 = min(t0, t1 - 1.0)                     # never fade in after the fade-out starts (the label would stay on screen)
    i = nid('pl'); els.append(f'<div id="{i}" class="cl" style="left:{cx-330}px;top:{y}px;width:660px;font-size:{size}px;text-shadow:0 2px 14px rgba(60,40,25,.35);opacity:0">{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:14}},{{opacity:1,y:0,duration:0.8,ease:"power2.out"}},{t0:.3f});'); fade_out(i, t1, 0.5)
def photo(png, x0, y0, w, h, t0, t1, label=None, pos='50% 50%'):
    """a real photo (jewellery, a film portrait, a vintage postcard) in a frame on the caramel backdrop"""
    i = nid('ph'); PHOTOS.append(png)
    els.append(f'<div id="{i}" class="w" style="left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;opacity:0;border-radius:4px;box-shadow:0 24px 56px rgba(60,30,12,.30)">'
               f'<img src="assets/{png}" class="photo" style="object-position:{pos}"></div>')
    _rise(i, t0, t1)
    if label: plabel(label, x0 + w // 2, y0 + h + 8, t0 + 0.35, t1, 56)

# ======================= elegant-at-home: the original's cream layouts ("How to Look Elegant & Expensive at Home") ==========
# storyboard of GmiAMO93vFE: rounded clips centred on a cream backdrop, grey script lines on cream, framed rows with gaps,
# fabric circles on caramel, numbered white cards. No zoom: every vertical clip is shown whole.
els.append('''<style>
.qx.dark i { color:#6b5a4c; }
.circ { position:absolute; z-index:46; border-radius:50%; overflow:hidden; box-shadow:0 18px 40px rgba(60,30,12,.30); }
.circ img { width:100%; height:100%; object-fit:cover; display:block; }
</style>''')

def creambg(t0, t1):
    return cream(t0 + 0.05, t1)

def cframe(shots, t1, w=540, h=960, x0=None, y0=None, bg=True, radius=26):
    """a rounded vertical frame on the cream backdrop (original 2:13, 3:27-3:37, 6:35, 7:24-7:34)"""
    if bg: creambg(shots[0][1], t1)
    x0 = (W - w) // 2 if x0 is None else x0; y0 = (H - h) // 2 if y0 is None else y0
    return _frames(shots, t1, x0, y0, w, h, radius=radius, shadow=True, entry='centre')

def ctext(html, t0, t1, size=60, box_=None, dur=1.4, bg=True):
    """a line in grey serif/script alone on the cream backdrop (original 0:44, 5:50-5:55, 6:25)"""
    if bg: creambg(t0 - 0.3, t1)
    return q(html, t0, t1, box_ or (200, 0, 1720, H), size=size, cls='dark', dur=dur)

def frow(specs, times, t_end, w=470, h=836, gap=50, y0=None, x0=None, labels=None, bg=None, radius=18):
    """framed clips in a row with gaps, each one growing in on its word (original 2:23-2:28, 2:52-3:07, 6:55)"""
    n = len(specs); x0 = (W - (n * w + (n - 1) * gap)) // 2 if x0 is None else x0; y0 = (H - h) // 2 if y0 is None else y0
    if bg == 'cream': creambg(times[0], t_end)
    for k, (s, tt) in enumerate(zip(specs, times)):
        xa = x0 + k * (w + gap)
        i = _frames([(s, tt)], t_end, xa, y0, w, h, radius=radius, shadow=True)
        if labels and labels[k]: plabel(labels[k], xa + w // 2, y0 + h - 110, tt + 0.4, t_end, 58)

def circle(png, cx, cy, r, t0, t1, label=None, lsize=54):
    """a fabric swatch in a circle on the caramel backdrop (original 2:38-2:43)"""
    i = nid('ci'); PHOTOS.append(png)
    els.append(f'<div id="{i}" class="circ" style="left:{cx-r}px;top:{cy-r}px;width:{2*r}px;height:{2*r}px;opacity:0"><img src="assets/{png}"></div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.6}},{{opacity:1,scale:1,duration:0.8,ease:"power3.out",transformOrigin:"50% 50%"}},{t0:.3f});'); fade_out(i, t1, 0.5)
    if label: plabel(label, cx, cy + r + 12, t0 + 0.35, t1, lsize)

# ======================= holiday-never-wear additions (6 Nov 2026) =======================
# from the channel's winter "Never Wear" upload (JF7PzFJl4eU): colour swatches named on the caramel, outfit pieces
# cut out beside the clip of that outfit, appearing one by one as each piece is said.
def dot(color, cx, cy, r, t0, t1, label=None, lsize=50):
    """a plain colour swatch (a circle of the named colour) on the caramel backdrop"""
    i = nid('dt')
    els.append(f'<div id="{i}" class="circ" style="left:{cx-r}px;top:{cy-r}px;width:{2*r}px;height:{2*r}px;background:{color};opacity:0"></div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,scale:0.6}},{{opacity:1,scale:1,duration:0.8,ease:"power3.out",transformOrigin:"50% 50%"}},{t0:.3f});'); fade_out(i, t1, 0.5)
    if label: plabel(label, cx, cy + r + 12, t0 + 0.35, t1, lsize)

def pieces(items, times, t_end, x0=PW + 40, x1=1880, ybot=None, hh=None, lsize=None, maxw=None):
    """outfit pieces in a row on the caramel beside a clip, each rising in on its word, its name underneath.
    A cut-out (PNG with transparency) stands on the caramel; a photo with its own background is framed."""
    n = len(items); cw = (x1 - x0) / n
    ybot = ybot or (860 if n >= 4 else 840); hh = hh or (600 if n >= 4 else 560); lsize = lsize or (44 if n >= 4 else 54)
    for k, ((png, lab), tt) in enumerate(zip(items, times)):
        cx = x0 + cw * (k + 0.5)
        if _PILImage.open(os.path.join(A, png)).mode == 'RGBA':
            prod(png, cx, ybot, hh, tt, t_end, label=lab, maxw=maxw or cw - 40, lsize=lsize)
        else:
            im = _PILImage.open(os.path.join(A, png)); r = im.width / im.height
            fw = min(cw - 50, hh * 0.85 * r); fh = fw / r
            photo(png, int(cx - fw / 2), int(ybot - fh), int(fw), int(fh), tt, t_end)
            if lab: plabel(lab, cx, ybot + 6, tt + 0.35, t_end, lsize)

def K(k, a=None, b=None):
    """a clip spec: the given window, or the clip's longest single shot (no cut inside it)"""
    if a is None:
        segs = SHOTS[k]['seg']; a, b = max(segs, key=lambda s: s[1] - s[0])
    elif b is None:
        b = SHOTS[k]['d']
    return (k, round(a, 2), round(b, 2))

# 8 Things Elegant Ladies Never Wear on Christmas & NYE - beat map (6 Nov 2026)
# Layouts of the channel's own winter "Never Wear" upload and the #1 video (VISUAL-ANALYSIS.md): white numbered cards,
# the mistake in a row (bad first), the principle on caramel, a clip with the named pieces cut out beside it, rows of
# good examples with their names, colour swatches, fabric circles, the guide over a full screen, the CE logo.
# Full screen = the whole vertical clip over its blurred copy (no crops). Every clip once.

def en_(i): return en(i) + 0.5
QR2 = (1260, 60, 1880, 1020)                      # right of a two-clip row

# ================= HOOK =================
cfull([(K('h_party0'), 0.0), (K('h_party2_4'), at(1, 'and noticed') - 0.1)], nx(2))
lrow([K('h_glitter1'), K('h_costume0'), K('h_party12', 9.6, 13.1)], [nx(2), at(2, "She's not wearing"), at(2, 'And yet')], nx(3))
lclip([(K('h_secret10', 0, 3.6), nx(3)), (K('n_pearl0'), at(3, 'During') - 0.1), (K('a_takeoff12', 13.7, 22.0), at(3, "It's about what") - 0.1)], en(3) + 0.35)
q('During the holidays, elegance<br>is rarely about what you <i>add</i>.', at(3, 'During') - 0.1, at(3, "It's about what") - 0.2, QL, size=60)
q('It&#8217;s about what<br>you <i>leave out</i>.', at(3, "It's about what"), en(3) + 0.3, QL, size=70)
white(en(3) + 0.35, at(4, 'eight') - 0.1); text("in today&#8217;s video...", 'card', en(3) + 0.65, at(4, 'eight') - 0.25, dur=1.0, out=0.4)
cfull([(K('h_tree9'), at(4, 'eight') - 0.3)], nx(5))
q('<i style="font-size:100px">8 Things Elegant Ladies Never Wear<br>on Christmas &amp; NYE</i>', at(4, 'eight') + 0.1, en(4) + 0.4, QC, cls='over')
lrow([K('h_season22', 0, 8.77), K('h_season24', 2.0, 7.1), K('h_nye2_11')], [nx(5), at(5, 'three simple'), at(5, 'you can copy')], nx(6))
cfull([(K('h_nye2_9'), nx(6))], en_(6))

# ================= 1. HEAD-TO-TOE SEQUINS =================
card_at('1. Head-to-toe sequins', 7, en(7) + 0.3, size=110)
cfull([(K('s_party6'), st(8) - 0.1)], at(8, 'But when') - 0.1)
lrow([K('s_seqdress14', 0, 6.5), K('h_glitter10'), K('s_seqdress6')], [at(8, 'But when') - 0.2, at(8, 'your bag'), at(8, 'the eye has')], at(8, 'and the whole') - 0.1)
cfull([(K('s_seqdress13'), at(8, 'and the whole') - 0.2)], nx(9))
q('Elegant women follow one rule:<br><i>one shine, one matte</i>.', st(9) + 0.1, en(9) + 0.3, QL, size=62)
lclip([(K('s_seqblack16'), nx(9)), (K('s_seqknit0', 0, 2.6), at(10, 'a fine knit') - 0.2), (K('s_seqblouse0'), at(10, 'a silk blouse')), (K('s_seqblack6'), at(10, 'or a plain'))], at(10, 'If you want') - 0.1)
pieces([('ph_fineknit.png', 'a fine knit'), ('ph_silkblouse.png', 'a silk blouse'), ('ph_blacksweater.png', 'a black sweater')],
       [at(10, 'a fine knit'), at(10, 'a silk blouse'), at(10, 'or a plain')], at(10, 'If you want') - 0.1)
lclip([(K('s_seqtop0', 9.0, 17.4), at(10, 'If you want') - 0.2)], nx(11))
pieces([('ph_seqtop.png', 'a sequin top'), ('ph_woolpant.png', 'matte wool trousers'), ('ph_satinbrown.png', 'a satin midi skirt')],
       [at(10, 'a sequin top'), at(10, 'matte wool'), at(10, 'or a satin')], nx(11))
q('Sparkle looks expensive when it has<br>something <i>quiet</i> to sit next to.', st(11) + 0.1, en(11) + 0.3, QC, size=66)
lclip([(K('s_seqclose2'), nx(12))], at(12, 'Good sequins') - 0.1)
q('Check the quality<br><i>before you buy</i>.', nx(12) + 0.3, at(12, 'Good sequins') - 0.2, QL, size=66)
lrow([K('s_seqclose7'), K('s_seqlining0'), K('s_seqlining3')], [at(12, 'Good sequins') - 0.2, at(12, 'sewn flat'), at(12, 'usually lined')], nx(13),
     labels=['dense', 'sewn flat', 'lined'])
cfull([(K('s_party2'), nx(13))], en_(13))

# ================= 2. NOVELTY HOLIDAY SWEATERS =================
card_at('2. Novelty holiday sweaters and themed prints', 14, en(14) + 0.3, size=90)
lrow([K('n_reindeer2'), K('n_reindeer9'), K('n_pompom23'), K('n_pompom12')],
     [st(15) - 0.2, at(15, 'snowflakes'), at(15, 'glittery trees'), at(15, 'anything with')], at(15, 'Unless') - 0.1, w=480)
cfull([(K('n_sweater9'), at(15, 'Unless') - 0.2)], nx(16))
lclip([(K('n_green9', 1.2, 13.21), nx(16)), (K('n_cable18', 0, 3.4), at(16, 'Think a')), (K('n_green7', 1.7, 7.7), at(16, 'a bottle-green')), (K('n_burgundy4'), at(16, 'or a deep'))], nx(17))
q('Carry the festive spirit through<br><i>colour and texture</i>.', nx(16) + 0.3, at(16, 'Think a') - 0.2, QL, size=60)
pieces([('ph_cable.png', 'a cream cable knit'), ('ph_greenknit.png', 'bottle-green cashmere'), ('ph_burgturtle.png', 'a burgundy turtleneck')],
       [at(16, 'a cream'), at(16, 'a bottle-green'), at(16, 'or a deep')], nx(17))
lrow([K('n_knitsatin7', 5.5, 11.68), K('n_knittrous6'), K('n_pearl5')], [nx(17), at(17, 'or tailored'), at(17, 'and add')], at(17, "It's still cozy") - 0.1,
     labels=['a satin midi skirt', 'tailored trousers', 'pearl earrings'])
cfull([(K('n_knitsatin12'), at(17, "It's still cozy") - 0.2)], nx(18))
lclip([(K('e_bye7'), nx(18))], at(18, 'like a velvet') - 0.1)
q('Keep it to <i>one tiny detail</i>.', nx(18) + 0.3, at(18, 'like a velvet') - 0.2, QL, size=66)
lrow([K('n_bow4', 11.8, 16.5), K('n_redlip4')], [at(18, 'like a velvet') - 0.2, at(18, 'or a classic')], en_(18), labels=['a velvet bow', 'a classic red lip'])

# ================= 3. MICRO-MINIS, TOO TIGHT, TOO REVEALING =================
card_at('3. Micro-minis and anything too tight or too revealing', 19, en(19) + 0.3, size=84)
lclip([(K('r_confident20', 0, 10.13), st(20) - 0.1)], nx(21))
q('Elegance doesn&#8217;t mean<br><i>covering up</i>.', st(20) + 0.1, at(20, 'It means') - 0.2, QL, size=66)
q('It means pieces you can<br><i>enjoy wearing</i>.', at(20, 'It means'), en(20) + 0.3, QL, size=66)
lrow([K('r_tug5'), K('r_neckline5'), K('r_tight0')], [at(21, "If you're tugging") - 0.2, at(21, 'adjusting your'), at(21, 'or holding')], at(21, "you won't") - 0.1)
cfull([(K('r_mini12'), at(21, "you won't") - 0.2)], nx(22))
lclip([(K('r_shoulder35', 12.6, 18.3), nx(22))], at(22, 'like your') - 0.1)
q('The rule of <i>one reveal</i>.', nx(22) + 0.3, at(22, 'like your') - 0.2, QL, size=70)
lrow([K('r_shoulder24'), K('r_back17'), K('r_slit0')], [at(22, 'like your') - 0.2, at(22, 'your back'), at(22, 'or a subtle')], at(22, 'and keep') - 0.1,
     labels=['your shoulders', 'your back', 'a subtle slit'])
cfull([(K('r_back2'), at(22, 'and keep') - 0.2)], nx(23))
lclip([(K('r_velvetmidi1', 3.0, 10.1), nx(23)), (K('r_slipblazer11'), at(23, 'A satin slip')), (K('r_offknit16'), at(23, 'An off-shoulder'))], nx(24))
pieces([('ph_velvetmidi.png', 'a velvet midi, low back'), ('ph_slipdress.png', 'a slip dress'), ('ph_blazerblack.png', 'a tailored blazer'), ('ph_offknit.png', 'an off-shoulder knit')],
       [nx(23) + 0.2, at(23, 'A satin slip'), at(23, 'a tailored blazer'), at(23, 'An off-shoulder')], nx(24), lsize=44)
cfull([(K('r_confident17'), nx(24))], en_(24))

# ================= THE GUIDE =================
lclip([(K('u_drape0'), st(25) - 0.1)], nx(26))
q('They know exactly which colours<br>make their skin <i>glow</i>.', at(25, 'They know') - 0.1, en(25) + 0.3, QL, size=58)
lrow([K('u_emerald22', 2.0, 7.3), K('u_sapphire23'), K('u_wine8')], [nx(26), at(26, 'sapphire'), at(26, 'and wine')], at(26, 'while warmer') - 0.1,
     labels=['emerald', 'sapphire', 'wine'])
lrow([K('u_olive13'), K('u_rust18'), K('u_brown20'), K('u_wine19')], [at(26, 'while warmer') - 0.2, at(26, 'rust'), at(26, 'chocolate brown'), at(26, 'and warm')], nx(27), w=480,
     labels=['olive', 'rust', 'chocolate brown', 'warm burgundy'])
cfull([(K('n_knitsatin14', 0, 6.5), nx(27)), (K('c_cape14', 0, 11.4), at(27, 'our personal') - 0.4)], en_(27))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(27, 'our personal') - 0.2, en(27) + 0.3, QC, cls='over')

# ================= 4. THIN, SHINY FABRICS THAT CLING =================
card_at('4. Thin, shiny fabrics that cling', 28, en(28) + 0.3, size=104)
cfull([(K('f_cheapsatin7', 3.0, 11.5), st(29) - 0.1)], at(29, 'Very thin') - 0.1)
lrow([K('f_cling10', 0, 11.6), K('f_cheapsatin3'), K('f_cling6')], [at(29, 'Very thin') - 0.2, at(29, 'creases easily'), at(29, 'has a flat')], nx(30),
     labels=['every line', 'creases', 'a plastic shine'])
q('Fabrics with <i>weight</i><br>and a softer glow.', nx(30) + 0.2, at(30, 'Velvet') - 0.2, QC, size=70)
for k, (png, lab, w) in enumerate([('ph_velvetfab.png', 'velvet', 'Velvet'), ('ph_crepefab.png', 'crepe', 'crepe'), ('ph_satinfab.png', 'heavy satin', 'heavy satin'),
                                   ('ph_silkfab.png', 'silk blends', 'silk blends'), ('ph_woolfab.png', 'fine wool', 'fine wool'), ('ph_jerseyfab.png', 'a good jersey', 'a good jersey')]):
    circle(png, 560 + (k % 3) * 400, 270 + (k // 3) * 440, 165, at(30, w) - 0.1, nx(31), label=lab, lsize=52)
lclip([(K('f_fitting2'), nx(31)), (K('f_light11'), at(31, 'Hold the fabric') - 0.1)], nx(32))
q('A quick test<br><i>in the fitting room</i>.', nx(31) + 0.3, at(31, 'Hold the fabric') - 0.2, QL, size=64)
q('Hold it up <i>to the light</i>.', at(31, 'Hold the fabric'), at(31, 'If you can see') - 0.2, QL, size=66)
q('See-through, or a harsh shine?<br><i>Put it back.</i>', at(31, 'If you can see'), en(31) + 0.3, QL, size=60)
cfull([(K('f_drape1'), nx(32)), (K('f_velvet0'), at(32, 'will always'))], en_(32))

# ================= 5. ACCESSORY OVERLOAD =================
card_at('5. Accessory overload', 33, en(33) + 0.3, size=110)
lrow([K('a_over32'), K('a_bangles6', 0, 12.0), K('a_earrings9'), K('a_crystalbag13')],
     [st(34) - 0.2, at(34, 'a stack'), at(34, 'light-up'), at(34, 'and a bag')], at(34, 'Each piece') - 0.1, w=480)
cfull([(K('a_over33'), at(34, 'Each piece') - 0.2)], nx(35))
lclip([(K('a_earrings2'), nx(35))], at(35, "If you're wearing") - 0.1)
q('One <i>hero</i> accessory.', nx(35) + 0.3, at(35, 'If your earrings') - 0.2, QL, size=74)
photo('ph_crystalear.png', 1000, 130, 560, 700, at(35, 'If your earrings') - 0.1, at(35, "If you're wearing") - 0.1, label='statement crystals, no necklace')
lclip([(K('a_necklace8', 0, 14.5), at(35, "If you're wearing") - 0.2)], nx(36))
pieces([('ph_necklace.png', 'a beautiful necklace'), ('ph_studs.png', 'simple studs')], [at(35, 'a beautiful'), at(35, 'go for')], nx(36), hh=560)
lclip([(K('a_brooch3', 0, 8.3), nx(36)), (K('a_gloves2', 3.5, 14.1), at(36, 'a pair of')), (K('a_clutch8'), at(36, 'a small satin'))], nx(37))
pieces([('ph_brooch.png', 'a pearl brooch'), ('ph_gloves.png', 'leather gloves'), ('ph_satinclutch.png', 'a satin clutch'), ('ph_greenbow.png', 'a velvet bow')],
       [nx(36) + 0.2, at(36, 'a pair of'), at(36, 'a small satin'), at(36, 'or a velvet')], nx(37), lsize=44)
lclip([(K('a_takeoff6'), nx(37))], en(37) + 0.35)
q('The <i>one-thing-off</i> rule.', nx(37) + 0.3, at(37, 'Take off') - 0.2, QL, size=70)
q('Take off one accessory.<br>The outfit <i>looks better</i>.', at(37, 'Take off'), en(37) + 0.3, QL, size=62)

# ================= 6. A BULKY PUFFER OR TEDDY COAT =================
card_at('6. A bulky puffer or oversized teddy coat over a party dress', 38, en(38) + 0.3, size=84)
lrow([K('c_puffer15'), K('c_teddy12'), K('c_puffer10')], [st(39) - 0.2, at(39, 'but a huge'), at(39, 'and your proportions')], nx(40))
lrow([K('c_camel3'), K('c_brown16'), K('c_charcoal12')], [nx(40), at(40, 'chocolate brown'), at(40, 'or charcoal')], at(40, 'A belted') - 0.1,
     labels=['camel', 'chocolate brown', 'charcoal'])
lclip([(K('c_wrap1'), at(40, 'A belted') - 0.2), (K('c_cape8', 0, 8.3), at(40, 'Or a long'))], nx(41))
pieces([('ph_wrapcoat.png', 'a belted wrap coat'), ('ph_cape.png', 'a long cape')], [at(40, 'A belted'), at(40, 'Or a long')], nx(41), hh=640)
lclip([(K('c_brown5'), nx(41)), (K('c_brown11'), at(41, 'and it looks'))], nx(42))
prod('ph_browncoat.png', 930, 930, 820, nx(41) + 0.2, nx(42), label='chocolate brown')
for k, (col, lab, w) in enumerate([('#6e1f2c', 'burgundy', 'burgundy'), ('#efe5d3', 'cream', 'cream'), ('#c8a04a', 'gold', 'and gold')]):
    dot(col, 1360 + k * 210, 470, 88, at(41, w) - 0.1, nx(42), label=lab, lsize=46)
cfull([(K('c_longer5', 0, 8.03), nx(42))], en_(42))

# ================= CLASSY CLOSET =================
cfull([(K('k_tryon11'), st(43) - 0.1)], nx(44))
q('<div><span style="font-size:44px">Try The Whole Outfit On With</span><br><i style="font-size:120px">Classy Closet</i></div>', at(43, 'you can try') - 0.2, en(43) + 0.3, QC, cls='over')
lrow([K('k_tryon0'), K('k_phone5'), K('k_tryon2')], [nx(44), at(44, 'browse our'), at(44, 'and tap')], at(44, "It's completely") - 0.1,
     labels=['upload a full-body photo', 'browse the outfits', 'tap to try them on'])
cfull([(K('k_phone14'), at(44, "It's completely") - 0.2)], en_(44))
q('<div><span style="font-size:44px">Completely Free &#183; Link Below</span><br><i style="font-size:120px">Classy Closet</i></div>', at(44, "It's completely") - 0.1, en(44) + 0.3, QC, cls='over')

# ================= 7. TOWERING HEELS =================
card_at('7. Towering heels you can&#8217;t walk in', 45, en(45) + 0.3, size=100)
lclip([(K('t_heels1', 0, 4.0), st(46) - 0.2), (K('t_heels5'), at(46, 'the whole look'))], nx(47))
q('Elegance is in<br><i>how you move</i>.', at(46, 'Elegance is'), en(46) + 0.3, QL, size=70)
lclip([(K('t_kitten6'), nx(47)), (K('t_sling2', 0, 9.5), at(47, 'a slingback')), (K('t_block1'), at(47, 'or a block')), (K('t_pointed20', 1.4, 6.93), at(47, 'A pointed toe'))], nx(48))
q('Between <i>1.5 and 3 inches</i>.', nx(47) + 0.3, at(47, 'like a kitten') - 0.2, QL, size=66)
pieces([('ph_kitten.png', 'a kitten heel'), ('ph_sling.png', 'a slingback'), ('ph_satinblock.png', 'a block heel in satin'), ('ph_suedeblock.png', 'or suede')],
       [at(47, 'like a kitten'), at(47, 'a slingback'), at(47, 'or a block'), at(47, 'or suede')], at(47, 'A pointed toe') - 0.1, hh=420, lsize=44)
prod('ph_pointed.png', 1264, 800, 560, at(47, 'A pointed toe'), nx(48), label='a pointed toe')
lclip([(K('t_flats2'), nx(48))], nx(49))
prod('ph_flats.png', 1264, 720, 420, at(48, 'satin ballet') - 0.1, nx(49), label='satin ballet flats with a strap')
cfull([(K('t_walk15'), nx(49)), (K('t_walk3'), at(49, 'If you can'))], en_(49))

# ================= 8. SKIPPING THE FINISHING TOUCHES =================
card_at('8. Skipping the finishing touches', 50, en(50) + 0.3, size=104)
cfull([(K('k_tryon14'), st(51) - 0.1)], at(51, "Velvet that's") - 0.1)
lrow([K('z_creased0', 0, 6.1), K('z_roller9', 3.0, 11.2)], [at(51, "Velvet that's") - 0.2, at(51, 'Lint all')], at(51, 'Scuffed') - 0.1, labels=['creases', 'lint on black'])
q('Velvet creased<br>from <i>the closet</i>.', at(51, "Velvet that's"), at(51, 'Scuffed') - 0.2, QR2, size=62)
lrow([K('z_scuff20'), K('z_tights2', 4.0, 12.3)], [at(51, 'Scuffed') - 0.2, at(51, 'Snagged')], nx(52), labels=['scuffed heels', 'snagged tights'])
q('A hem that&#8217;s<br><i>come down</i>.', at(51, "A hem"), at(51, 'These tiny') - 0.2, QR2, size=62)
q('Tiny things people<br><i>notice in photos</i>.', at(51, 'These tiny'), en(51) + 0.3, QR2, size=60)
lclip([(K('z_steam1', 0, 12.2), nx(52))], nx(53))
q('Ten minutes<br><i>before you leave</i>.', nx(52) + 0.3, at(52, 'Steam your') - 0.6, QL, size=66)
prod('ph_steamer.png', 1264, 880, 520, at(52, 'Steam your'), at(52, 'Never press') - 0.1, label='steam your velvet', lsize=54)
q('Or hang it in the bathroom<br>while you <i>shower</i>.', at(52, 'or hang it'), at(52, 'Never press') - 0.2, (PW + 50, 40, 1870, 320), size=54)
q('Never press it flat<br>with a <i>hot iron</i>.', at(52, 'Never press'), en(52) + 0.3, QL, size=62)
lclip([(K('z_roller0'), nx(53)), (K('z_polish4'), at(53, 'Wipe your'))], nx(54))
pieces([('ph_roller.png', 'a lint roller'), ('ph_polish.png', 'a cloth and polish'), ('ph_tights.png', 'spare tights'), ('ph_minirollers.png', 'a mini lint roller')],
       [at(53, 'Run a lint'), at(53, 'Wipe your'), at(53, 'a spare pair'), at(53, 'and a mini')], nx(54), hh=460, lsize=44)
cfull([(K('z_flash15'), nx(54)), (K('z_flash41'), at(54, 'Flash shows'))], at(54, 'like see-through') - 0.1)
q('Flash shows what<br>the <i>mirror</i> doesn&#8217;t.', at(54, 'Flash shows') - 0.1, at(54, 'like see-through') - 0.2, QC, size=76, cls='over')
lclip([(K('z_flash44', 0, 9.43), at(54, 'like see-through') - 0.2)], en_(54))
q('See-through fabric,<br>lint, bra straps.<br><i>Fix it before you go.</i>', at(54, 'like see-through'), en(54) + 0.3, QL, size=62)

# ================= BONUS: THREE OUTFIT FORMULAS =================
card_at('3 outfit formulas to copy', 55, en(55) + 0.3, size=110)
TT = (PW + 40, 30, 1880, 230)
lclip([(K('o_green9'), nx(56))], nx(57))
q('<i>Christmas dinner</i>', nx(56) + 0.1, nx(57) - 0.1, TT, size=72)
pieces([('ph_greendress.png', 'a green velvet midi'), ('ph_nudekitten.png', 'nude kitten heels'), ('ph_pearlear2.png', 'pearl earrings'), ('ph_camelcoat2.png', 'a camel wool coat')],
       [at(56, 'a bottle-green'), at(56, 'nude kitten'), at(56, 'pearl earrings'), at(56, 'and a camel')], nx(57), ybot=900, hh=560, lsize=44)
lclip([(K('o_office10', 4.3, 11.0), nx(57)), (K('o_office8', 0, 7.0), at(57, 'a tailored blazer'))], nx(58))
q('<i>The office party</i>', nx(57) + 0.1, nx(58) - 0.1, TT, size=72)
pieces([('ph_champskirt.png', 'a satin midi skirt'), ('ph_fineknit2.png', 'a fine-knit sweater'), ('ph_blazercamel.png', 'a tailored blazer'), ('ph_hoops.png', 'gold hoops')],
       [at(57, 'a satin midi'), at(57, 'a fine-knit'), at(57, 'a tailored blazer'), at(57, 'and gold')], nx(58), ybot=900, hh=560, lsize=44)
lclip([(K('o_slip13'), nx(58)), (K('o_silktrous0'), at(58, 'or a silk')), (K('o_crystal2'), at(58, 'like a crystal')), (K('o_seqjacket7'), at(58, 'or a sequin'))], nx(59))
q('<i>New Year&#8217;s Eve</i>', nx(58) + 0.1, nx(59) - 0.1, TT, size=72)
pieces([('ph_blackslip.png', 'a black satin slip'), ('ph_silktop.png', 'or a silk top'), ('ph_seqjacket.png', 'one sparkle piece'), ('ph_redlip.png', 'a classic red lip')],
       [at(58, 'a black satin'), at(58, 'or a silk'), at(58, 'one sparkle'), at(58, 'and a classic')], nx(59), ybot=900, hh=560, lsize=44)
lclip([(K('h_tree16', 5.7, 11.5), nx(59))], en_(59))
q('Notice the pattern?<br><i>One star,</i> and everything<br>else stays quiet.', st(59) + 0.1, en(59) + 0.4, QL, size=64)

# ================= CLOSE =================
cfull([(K('e_thanks8'), nx(60)), (K('e_comment2'), at(60, 'Tell me')), (K('e_comment14', 0, 8.28), at(60, 'And what are'))], nx(61))
cfull([(K('e_thanks9'), nx(61)), (K('e_comment12'), at(61, 'A simple like'))], nx(62))
cfull([(K('e_thanks3'), nx(62)), (K('e_comment5'), at(62, 'my favourite'))], nx(63))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(62, 'our personal') - 0.2, en(62) + 0.4, QC, cls='over')
cfull([(K('h_party3'), nx(63))], total - 2.6)
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
