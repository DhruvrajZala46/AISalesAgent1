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

# ======================= winter-expensive additions (8 Nov 2026) =======================
# from the channel's 716k "How to Instantly Look More Elegant & Expensive: No Matter Your Budget" (QOEUbAZB07o):
# product cut-outs on the caramel beside a clip, named in script; here every tip ends with its Budget / Splurge pair.
def item(png, cx, ybot, hh, t0, t1, label=None, maxw=420, lsize=46):
    """one product: a cut-out stands on the caramel; a photo with its own background is framed"""
    if _PILImage.open(os.path.join(A, png)).mode == 'RGBA':
        prod(png, cx, ybot, hh, t0, t1, label=label, maxw=maxw, lsize=lsize)
    else:
        im = _PILImage.open(os.path.join(A, png)); r = im.width / im.height
        fh = min(hh * 0.85, maxw / r); fw = fh * r
        photo(png, int(cx - fw / 2), int(ybot - fh), int(fw), int(fh), t0, t1)
        if label: plabel(label, cx, ybot + 6, t0 + 0.35, t1, lsize)

def _col(items, times, t_end, xa, xb, ybot, hh, lsize):
    n = len(items); cw = (xb - xa) / n
    for k, ((png, lab), tt) in enumerate(zip(items, times)):
        item(png, xa + cw * (k + 0.5), ybot, hh / (1 if n == 1 else 1.25 if n == 2 else 1.55), tt, t_end, label=lab, maxw=cw - 30, lsize=lsize)

def bsplit(i, shots, budget, splurge, t_end, btimes=None, stimes=None, bclip=None, sclip=None, blabel=None, slabel=None):
    """a clip on the left; the caramel on the right split in two: Budget (left) and Splurge (right), each named in
    script at the top, its pieces rising in as they are said. bclip/sclip: a framed clip instead of products."""
    lclip(shots, t_end)
    ts = at(i, 'Splurge version'); tb = st(i)
    xa, xm, xb = PW + 30, (PW + 30 + 1890) // 2, 1890
    q('<i>Budget</i>', tb + 0.1, t_end - 0.1, (xa, 40, xm, 210), size=80)
    q('<i>Splurge</i>', ts, t_end - 0.1, (xm, 40, xb, 210), size=80)
    ln = nid('ln'); els.append(f'<div id="{ln}" style="position:absolute;z-index:44;left:{xm-1}px;top:250px;width:2px;height:640px;background:rgba(255,255,255,.55);opacity:0"></div>')
    fade_in(ln, ts - 0.2, 0.6); fade_out(ln, t_end, 0.5)
    for side, its, tms, clip, lab, x0, x1, t0 in (('b', budget, btimes, bclip, blabel, xa, xm, tb + 0.6), ('s', splurge, stimes, sclip, slabel, xm, xb, ts + 0.5)):
        if clip:
            w, h = 300, 534; cx = (x0 + x1) // 2
            _frames([(clip, t0)], t_end, cx - w // 2, 250, w, h, radius=18, shadow=True)
            if lab: plabel(lab, cx, 250 + h + 12, t0 + 0.35, t_end, 44)
        if its:
            tms = tms or [t0 + 0.7 * k for k in range(len(its))]
            _col(its, tms, t_end, x0, x1, 880, 560, 40 if len(its) > 1 else 46)

QR2 = (1260, 60, 1880, 1020)
TT = (PW + 40, 30, 1880, 230)


# 7 Subtle Body Language Habits That Make You Appear Naturally Poised - beat map (9 Nov 2026)
# Layouts of the channel's "7 Body Language Habits That Instantly Make You Look Elegant & Confident" (r_mYSc7FHvk,
# VISUAL-ANALYSIS.md): full clips; the habit's name on a white card in script; clips on the caramel with the lesson in
# white lines beside them, appearing as they are said; rows of clips; framed clips and a script line on cream; film scenes
# and named women (Audrey Hepburn, Grace Kelly, Kate); the guide over a full clip; the CE logo. Every clip once.

def en_(i): return en(i) + 0.5
CROP['s_audrey29'] = (0, 36, 1209)     # past a small vertical "LONGANCE" mark at the right edge
def qstack(lines, times, t1, box_=QL, size=58, rh=150):
    """the reference's lesson lines: one under the other beside a clip, each appearing as it is said"""
    x0, y0, x1, y1 = box_; n = len(lines); top = (y0 + y1) // 2 - n * rh // 2
    for k, (txt, tt) in enumerate(zip(lines, times)):
        q(txt, tt, t1, (x0, top + k * rh, x1, top + (k + 1) * rh), size=size, dur=1.0)

# ================= HOOK =================
cfull([(K('h_calmv32'), 0.0)], at(1, 'she is so') - 0.1)
lclip([(K('rc_calmv27'), at(1, 'she is so') - 0.2), (K('h_oldv41', 0.0, 3.42), at(1, 'and yet'))], nx(2))
q('She is so calm,<br><i>so composed.</i>', at(1, 'she is so'), at(1, 'and yet') - 0.2, QL, size=66)
q('And yet you couldn&#8217;t say<br><i>what she was doing.</i>', at(1, 'and yet'), en(1) + 0.3, QL, size=60)
cfull([(K('h_stillv19'), nx(2)), (K('h_stillv12'), at(2, "She wasn't standing"))], nx(3))
lrow([K('h_subtlev2'), K('h_subtlev5'), K('h_subtlev4')], [nx(3), at(3, 'tiny habits'), at(3, 'the kind people')], en_(3))
cfull([(K('h_begin14'), en(3) + 0.35), (K('h_begin40'), at(5, 'And these'))], at(5, 'Every one') - 0.1)
q('<div><span style="font-size:44px">7 Subtle Body Language Habits</span><br><i style="font-size:118px">Naturally Poised</i></div>',
  at(4, 'seven subtle') - 0.1, en(4) + 0.3, QC, cls='over')
q('Not the usual<br><i>&#8220;stand tall and smile&#8221;</i>', at(5, 'And these') - 0.1, at(5, 'Every one') - 0.2, QC, size=76, cls='over')
frow([K('h_readv9'), K('h_readv6')], [at(5, 'Every one') - 0.2, at(5, 'honest with you')], en_(5), bg='cream', w=430, h=766, gap=60,
     labels=['real research', 'honest'])
cfull([(K('h_oldv11'), nx(6))], en_(6))

# ================= 1. THE SLOW SMILE =================
card_at('1. The Slow Smile', 7, en(7) + 0.3, size=110)
lclip([(K('s_quickv10'), nx(8)), (K('s_quickv19'), at(8, 'It can feel'))], nx(9))
q('A smile that switched on<br><i>like a light</i>', at(8, 'a smile that') - 0.1, at(8, 'It can feel') - 0.2, QL, size=64)
q('It can feel <i>a little rehearsed,</i><br>even when it&#8217;s sincere.', at(8, 'It can feel'), en(8) + 0.3, QL, size=58)
lclip([(K('s_screenv0'), nx(9)), (K('s_screenv8', 8.82, 13.44), at(9, 'whose smiles'))], nx(10))
q('100 people rated<br><i>computer-generated faces</i>', at(9, '100 people') - 0.1, at(9, 'whose smiles') - 0.2, QL, size=60)
qstack(['very quickly', '<i>or more gradually</i>'], [at(9, 'very quickly') - 0.1, at(9, 'or more') - 0.1], en(9) + 0.3, size=66)
lrow([K('s_audrey23'), K('s_audrey29'), K('s_katev8', 0, 10.8)], [nx(10), at(10, 'more attractive'), at(10, 'and more trustworthy')], en_(10),
     labels=['more genuine', 'more attractive', 'more trustworthy'])
lclip([(K('s_screenv12'), nx(11))], nx(12))
q('Digital faces on a screen:<br><i>a small, useful nudge,</i><br>not a guarantee.', nx(11) + 0.3, en(11) + 0.3, QL, size=58)
lclip([(K('s_softv40'), nx(12)), (K('s_eyesv27'), at(12, 'Then let the smile'))], nx(13))
q('Let your eyes<br><i>arrive first.</i>', at(12, 'let your eyes') - 0.1, at(12, 'Then let the smile') - 0.2, QL, size=70)
q('Then let the smile<br><i>build gradually.</i>', at(12, 'Then let the smile'), en(12) + 0.3, QL, size=70)
cfull([(K('s_katev1'), nx(13))], at(13, 'Try it once') - 0.1)
q('It tends to read as<br><i>warm and unforced.</i>', at(13, 'it tends to') - 0.1, at(13, 'Try it once') - 0.2, QC, size=78, cls='over')
lclip([(K('s_mirrorv4'), at(13, 'Try it once') - 0.2)], en_(13))
qstack(['<i>See,</i>', '<i>soften,</i>', '<i>smile.</i>'], [at(13, 'see,'), at(13, 'soften,'), at(13, 'smile.')], en(13) + 0.4, size=80, rh=170)

# ================= 2. THE COMFORTABLE GAZE =================
card_at('2. The Comfortable Gaze', 14, en(14) + 0.3, size=110)
cfull([(K('g_starev10'), nx(15)), (K('g_awayv7'), at(15, 'Or looked away'))], nx(16))
lrow([K('g_museumv4'), K('g_museumv5'), K('g_museumv8', 0.0, 5.9)], [nx(16), at(16, 'from 56'), at(16, 'video clips')], en_(16),
     labels=['500 visitors', '56 countries', None])
lclip([(K('g_eyev9'), nx(17)), (K('mr_laughv31'), at(17, 'Most people'))], nx(18))
q('The average comfortable length:<br><i>just over three seconds</i>', nx(17) + 0.3, at(17, 'Most people') - 0.2, QL, size=80)
q('Most people: between<br><i>two and five seconds</i>', at(17, 'Most people'), en(17) + 0.3, QL, size=62)
cfull([(K('g_galleryv14'), nx(18))], at(18, 'so treat') - 0.1)
lclip([(K('g_talkv28'), at(18, 'so treat') - 0.2), (K('g_talkv33', 0.0, 3.98), at(18, 'Real comfort'))], en_(18))
q('A rough guide,<br><i>not a rule.</i>', at(18, 'so treat'), at(18, 'Real comfort') - 0.2, QL, size=72)
q('Real comfort varies with<br><i>the person and the moment.</i>', at(18, 'Real comfort'), en(18) + 0.3, QL, size=58)
lclip([(K('g_tourv6'), nx(19)), (K('g_driftv31'), at(19, 'then let your gaze')), (K('gk40', 0, 8.63), at(19, 'and come back'))], en_(19))
qstack(['Meet their eyes.', '<i>Let your gaze drift away slowly,</i>', 'and come back.'],
       [at(19, 'Meet their eyes') - 0.1, at(19, 'then let your gaze'), at(19, 'and come back')], en(19) + 0.4, size=58)
cfull([(K('mr_laughv39'), nx(20)), (K('g_awayv0'), at(20, 'and if they'))], nx(21))
cfull([(K('gk37'), nx(21))], en_(21))
q('Soft and unhurried<br><i>reads as poised.</i>', at(21, 'Soft and') - 0.1, en(21) + 0.4, QC, size=80, cls='over')

# ================= 3. YOUR PHONE OUT OF SIGHT =================
card_at('3. Your Phone Out of Sight', 22, en(22) + 0.3, size=104)
cfull([(K('p_down24', 0, 3.1), nx(23))], en(23) + 0.15)
lrow([K('h_meetv8'), K('h_meetv5'), K('p_cafev25')], [nx(24), at(24, 'chatting'), at(24, 'in cafes')], en_(24))
frow([K('p_tablev14'), K('p_handv10')], [nx(25), at(25, "in someone's hand")], at(25, 'reported') - 0.1, bg='cream', w=430, h=766, gap=60,
     labels=['on the table', 'in a hand'])
lclip([(K('p_awayv22', 0, 6.9), at(25, 'reported') - 0.2)], en_(25))
q('Slightly less close,<br><i>less empathy</i>', at(25, 'slightly less') - 0.1, en(25) + 0.4, QL, size=70)
lclip([(K('g_talkv31'), nx(26)), (K('mr_dinnerv18'), at(26, 'It only')), (K('p_cafev18'), at(26, 'But it fits'))], en_(26))
q('The difference<br><i>was small.</i>', nx(26) + 0.2, at(26, 'It only') - 0.2, QL, size=70)
q('It only recorded whether<br>a phone was <i>visible.</i>', at(26, 'It only'), at(26, 'But it fits') - 0.2, QL, size=60)
q('It fits with<br><i>earlier lab work.</i>', at(26, 'But it fits'), en(26) + 0.4, QL, size=70)
lrow([K('p_bagv9'), K('p_pocketv16')], [at(27, 'keep your phone') - 0.2, at(27, 'or your pocket')], en_(27),
     labels=['in your bag', 'or your pocket'])
lclip([(K('p_checkv18'), nx(28))], nx(29))
q('If you truly need to check it,<br><i>say so with a smile.</i>', nx(28) + 0.3, at(28, 'Do you mind') - 0.3, QL, size=60)
q('<i>&#8220;Do you mind if I<br>check this quickly?&#8221;</i>', at(28, 'Do you mind') - 0.2, en(28) + 0.3, QL, size=62)
cfull([(K('p_listenv40', 0, 5.6), nx(29))], en_(29))
q('Your full attention<br><i>is one of the most elegant things you can offer.</i>', nx(29) + 0.2, en(29) + 0.4, QC, size=64, cls='over')

# ================= 4. THE WARM, STEADY GREETING =================
card_at('4. The Warm, Steady Greeting', 30, en(30) + 0.3, size=100)
cfull([(K('hs_shakev2'), nx(31)), (K('hs2_royal5', 0, 8.48), at(31, 'We usually')), (K('hs_katev24', 1.8, 7.23), at(31, "But it's one"))], nx(32))
lrow([K('hs2_women25', 0, 6.5), K('hs2_slow21'), K('hs_meetv15')], [nx(32), at(32, 'shaken twice'), at(32, 'four trained')], en_(32),
     labels=['112 people', 'shaken twice', 'four coders'])
lclip([(K('hs2_greet35'), nx(33)), (K('hs2_royal10'), at(33, 'which is a'))], en_(33))
q('A firm handshake<br><i>was linked to:</i>', at(33, 'a firm') - 0.1, en(33) + 0.4, (PW + 50, 60, 1870, 300), size=60)
qstack(['more outgoing', '<i>emotionally expressive</i>', 'less shy'],
       [at(33, 'more outgoing') - 0.1, at(33, 'emotionally expressive') - 0.1, at(33, 'less shy') - 0.1], en(33) + 0.4, size=66)
cfull([(K('hs_katev25'), nx(34)), (K('hs_meetv13'), at(34, 'The researchers'))], en_(34))
q('<i>An effective form of self-promotion</i><br>for women', at(34, 'an effective') - 0.1, en(34) + 0.4, QC, size=70, cls='over')
ctext('These are <i>links,</i><br>not proof.', nx(35) + 0.2, en_(35), size=86)
cfull([(K('hs2_elegant5', 0, 8.47), nx(36))], en_(36))
lclip([(K('hs2_women24'), nx(37)), (K('s_katev0'), at(37, 'Add a couple'))], en_(37))
qstack(['A little early,', '<i>palm to palm,</i>', 'firm, but never crushing.'],
       [at(37, 'a little early') - 0.1, at(37, 'palm to palm') - 0.1, at(37, 'firm but') - 0.1], at(37, 'Add a couple') - 0.2, size=62)
q('Gentle pumps,<br><i>your slow smile</i><br>and a comfortable gaze.', at(37, 'Add a couple'), en(37) + 0.4, QL, size=60)
lrow([K('hs_hugv7', 2.5, 9.9), K('hs_kissv11')], [nx(38), at(38, 'or a cheek')], en_(38), labels=['a hug', 'or a cheek kiss'])
q('Unhurried,<br><i>warm and steady.</i>', at(38, 'unhurried') - 0.1, en(38) + 0.4, (2 * PW + 40, 60, 1890, 1020), size=64)

# ================= THE GUIDE =================
cfull([(K('m_stylev13', 0.0, 4.7), nx(39)), (K('m_stylev17'), at(39, "They don't guess"))], nx(40))
lrow([K('m_colourv4'), K('m_shapev10'), K('m_hair3')], [nx(40), at(40, 'how to dress'), at(40, 'which hairstyles')], at(40, 'and how to move') - 0.1,
     labels=['best colours', 'your unique shape', 'hairstyles'])
cfull([(K('h_stillv15'), at(40, 'and how to move') - 0.2)], nx(41))
cfull([(K('h_begin48'), nx(41)), (K('h_oldv43'), at(41, 'It will be sent'))], en_(41))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>',
  at(41, 'our personal') - 0.2, en(41) + 0.3, QC, cls='over')

# ================= 5. SUBTLE MIRRORING =================
card_at('5. Subtle Mirroring', 42, en(42) + 0.3, size=110)
cfull([(K('mr_samev12'), nx(43))], at(43, 'Very often') - 0.1)
lclip([(K('mr_samev15'), at(43, 'Very often') - 0.2)], en_(43))
q('You were quietly<br><i>matching each other.</i>', at(43, 'quietly matching') - 0.2, en(43) + 0.4, QL, size=66)
lrow([K('mr_leanv29', 2.1, 12.1), K('mr_samev14', 3.68, 11.26), K('mr_talkv7')], [nx(44), at(44, 'mirrored their'), at(44, 'ended up')], at(44, 'The people being') - 0.1)
cfull([(K('mr_laughv5'), at(44, 'The people being') - 0.2)], en_(44))
lclip([(K('mr_leanv23', 5.6, 20.0), nx(45)), (K('mr_dinnerv12'), at(45, 'After a few'))], en_(45))
q('This doesn&#8217;t mean<br><i>copying anyone.</i>', at(45, "this doesn't mean") - 0.1, at(45, 'After a few') - 0.2, QL, size=68)
q('Gently match their<br><i>pace and energy.</i>', at(45, 'After a few'), en(45) + 0.4, QL, size=68)
cfull([(K('mr_dinnerv7', 4.1, 9.04), nx(46)), (K('mr_leanv12'), at(46, 'If they lean'))], en_(46))
lclip([(K('mr_laughv20'), nx(47)), (K('mr_dinnerv9'), at(47, 'The goal'))], en_(47))
q('Match the feeling,<br><i>not the exact movement.</i>', nx(47) + 0.1, at(47, 'If it ever') - 0.2, QL, size=64)
q('If it ever feels obvious,<br><i>you&#8217;re doing too much.</i>', at(47, 'If it ever'), at(47, 'The goal') - 0.2, QL, size=62)
q('<i>Attunement,</i><br>not imitation.', at(47, 'The goal'), en(47) + 0.4, QL, size=80)

# ================= 6. THE GRACEFUL RECOVERY =================
card_at('6. The Graceful Recovery', 48, en(48) + 0.3, size=104)
lrow([K('rc_spillv1'), K('rc_keysv3'), K('c_presentv4', 22.8, 27.57)], [nx(49), at(49, 'dropped your keys'), at(49, 'or stumbled')], at(49, 'A classic') - 0.1,
     labels=['spilled something', 'dropped your keys', 'stumbled over your words'])
cfull([(K('rc_quizv20'), at(49, 'A classic') - 0.2)], nx(50))
lclip([(K('rc_radiov8'), nx(50)), (K('rc_students45', 22, 34), at(50, 'One was')), (K('rc_spillv13'), at(50, 'In some versions'))], en_(50))
q('<i>1966:</i><br>recordings of two<br>quiz contestants', at(50, '1966') - 0.2, at(50, 'One was') - 0.2, QL, size=62)
qstack(['one very capable,', '<i>one average</i>'], [at(50, 'One was very') - 0.1, at(50, 'and one was average') - 0.1], at(50, 'In some versions') - 0.2, size=66)
q('The contestant<br><i>spilled coffee.</i>', at(50, 'In some versions'), en(50) + 0.4, QL, size=70)
lclip([(K('rc_spillv11'), nx(51))], en_(51))
qstack(['The capable one who spilled:<br><i>more likable</i>', 'The average one who spilled:<br><i>less likable</i>'], [nx(51) + 0.2, at(51, 'while the average')], en(51) + 0.4, size=60, rh=230)
lclip([(K('h_readv3'), nx(52)), (K('rc_radiov7'), at(52, 'with audio')), (K('rc_students18', 0, 5.7), at(52, 'and male')), (K('h_readv7', 0, 10), at(52, 'and researchers'))], en_(52))
q('That doesn&#8217;t mean<br><i>mistakes always help you.</i>', nx(52) + 0.2, at(52, 'It was an old') - 0.2, QL, size=62)
qstack(['an old study,', '<i>audio recordings,</i>', 'male students'], [at(52, 'It was an old'), at(52, 'with audio'), at(52, 'and male')],
       en(52) + 0.4, size=64)
cfull([(K('rc_calmv33'), nx(53))], en_(53))
q('How calmly you handle a slip<br><i>shapes how it feels in the room.</i>', at(53, 'how calmly') - 0.2, en(53) + 0.4, QC, size=70, cls='over')
lclip([(K('rc_breathv13'), nx(54))], en_(54))
qstack(['When something goes wrong,', '<i>pause.</i>', 'Take a slow breath out.'], [at(54, 'When something') - 0.1, at(54, 'pause.') - 0.1, at(54, 'Take a slow') - 0.1], en(54) + 0.4, size=66, rh=160)
lclip([(K('rc_wipev17'), nx(55))], at(55, 'and carry on') - 0.1)
q('Give a <i>small smile</i>', nx(55) + 0.3, at(55, 'Oops') - 0.4, QL, size=70)
q('<i>&#8220;Oops, let me fix that.&#8221;</i>', at(55, 'Oops') - 0.2, at(55, 'and carry on') - 0.2, QL, size=70)
cfull([(K('rc_oopsv0'), at(55, 'and carry on') - 0.2)], nx(56))
cfull([(K('rc_calmv41'), nx(56))], en_(56))
q('No spiral of apologies.<br><i>Keep the moment small.</i>', nx(56) + 0.2, en(56) + 0.4, QC, size=72, cls='over')

# ================= 7. YOU LOOK CALMER THAN YOU FEEL =================
card_at('7. You Look Calmer Than You Feel', 57, en(57) + 0.3, size=96)
cfull([(K('c_heartv14'), nx(58)), (K('c_nervous16'), at(58, 'and been sure'))], en_(58))
lclip([(K('c_nervous13'), nx(59))], at(59, 'In one public') - 0.1)
q('<i>The illusion<br>of transparency</i>', at(59, 'the illusion') - 0.1, at(59, 'In one public') - 0.2, QL, size=80)
lrow([K('sp2_podium13', 3.0, 12.0), K('c_presentv5', 4.1, 24.8), K('sp2_audience3')], [at(59, 'In one public') - 0.2, at(59, 'speakers rated'), at(59, 'than the people')], en_(59))
cfull([(K('c_katev7'), nx(60)), (K('c_kate17'), at(60, 'In other words'))], en_(60))
q('Our nerves are far less visible<br><i>than we think.</i>', at(60, 'our nerves') - 0.1, en(60) + 0.4, QC, size=72, cls='over')
lclip([(K('h_calmv18'), nx(61)), (K('c_breathv15'), at(61, 'silently tell') - 0.2), (K('c_shouldersv18'), at(61, 'Then take one'))], en_(61))
q('Before you walk in,<br><i>silently tell yourself:</i>', at(61, 'Before you') - 0.1, at(61, 'I look calmer') - 0.4, QL, size=62)
q('<i>&#8220;I look calmer<br>than I feel.&#8221;</i>', at(61, 'I look calmer') - 0.2, at(61, 'Then take one') - 0.2, QL, size=74)
qstack(['One slow breath out,', '<i>let your shoulders drop.</i>'], [at(61, 'Then take one'), at(61, 'and let your')], en(61) + 0.4, size=64)
cfull([(K('c_enterv9'), nx(62)), (K('c_enterv19'), at(62, 'but the less'))], en_(62))

# ================= CLOSE =================
cfull([(K('h_poisedv20'), nx(63)), (K('e_commentv10'), at(63, 'just comment'))], nx(64))
q('Comment <i>&#8220;poise&#8221;</i>', at(63, 'just comment') - 0.1, at(63, 'and tell me') - 0.1, QC, size=96, cls='over')
cfull([(K('e_thanksv13'), nx(64)), (K('h_poisedv27'), at(64, 'you can access') - 0.4)], nx(65))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>',
  at(64, 'you can access') - 0.2, en(64) + 0.4, QC, cls='over')
cfull([(K('e_thanksv48'), nx(65))], nx(66))
cfull([(K('e_byev11'), nx(66))], total - 2.6)
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
