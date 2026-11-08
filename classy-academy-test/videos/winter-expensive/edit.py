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

# How to Look Expensive & Put-Together in Winter (No Matter Your Budget) - beat map (8 Nov 2026)
# Layouts of the channel's 716k "How to Instantly Look More Elegant & Expensive: No Matter Your Budget" (VISUAL-ANALYSIS.md):
# white numbered cards, full clips, a clip with the reason beside it, rows of clips named per item, product cut-outs on
# the caramel, the guide over a full clip, the CE logo. Every tip ends with its Budget / Splurge pair. Every clip once.

def en_(i): return en(i) + 0.5
CROP['p_messy18'] = (48, 170, 1110)    # past a small caption at the top (a gentle 1.15x crop)
CROP['hr_bun8'] = (97, 345, 935)

# ================= HOOK =================
cfull([(K('h_coat36'), 0.0), (K('h_cashmere2'), at(1, 'and a closet') - 0.1)], nx(2))
lclip([(K('h_winter11', 0, 6.73), nx(2)), (K('h_winter5'), at(2, 'and some of it'))], en(2) + 0.35)
q('Most of it costs<br><i>very little</i>.', at(2, 'most of what') - 0.1, at(2, 'and some of it') - 0.2, QL, size=66)
q('And some of it costs<br><i>nothing at all</i>.', at(2, 'and some of it'), en(2) + 0.3, QL, size=66)
white(en(2) + 0.35, at(3, 'eight') - 0.1); text("in today&#8217;s video...", 'card', en(2) + 0.65, at(3, 'eight') - 0.25, dur=1.0, out=0.4)
cfull([(K('h_simple10', 0, 4.9), at(3, 'eight') - 0.3)], at(3, 'with a budget') - 0.1)
q('<i style="font-size:100px">How to Look Expensive<br>&amp; Put-Together in Winter</i>', at(3, 'eight') + 0.1, at(3, 'with a budget') - 0.2, QC, cls='over')
lrow([K('o_mid14', 0.0, 4.62), K('o_lux15')], [at(3, 'with a budget') - 0.2, at(3, 'a splurge')], nx(4), labels=['budget', 'splurge'])
lrow([K('h_closet2', 52.51, 59.61), K('h_closet13', 0, 10.0), K('h_closet7', 3.0, 15.0)], [nx(4), at(4, 'build elegant'), at(4, 'from what')], nx(5))
lrow([K('o_same14'), K('o_same5'), K('o_mid15', 3.0, 12.54)], [nx(5), at(5, 'the same winter'), at(5, 'three different')], at(5, "Let's get") - 0.1,
     labels=['budget', 'mid-range', 'splurge'])
cfull([(K('h_simple16'), at(5, "Let's get") - 0.2)], en_(5))

# ================= 1. WEAR A COAT THAT FITS YOU =================
card_at('1. Wear a coat that fits you', 6, en(6) + 0.3, size=104)
cfull([(K('c_walk2', 0, 4.43), st(7) - 0.1), (K('c_walk16'), at(7, 'your coat is'))], at(7, "It's the first") - 0.1)
q('In winter, your coat<br>is <i>your outfit</i>.', at(7, 'In winter') - 0.1, at(7, "It's the first") - 0.2, QC, size=82, cls='over')
lrow([K('c_photo9', 0, 5.47), K('c_walk13'), K('c_dinner5')], [at(7, "It's the first") - 0.2, at(7, 'every walk'), at(7, 'every dinner')], nx(8),
     labels=['every photo', 'every walk', 'every dinner'])
lclip([(K('c_camel5'), nx(8))], nx(9))
q('A $60 coat that <i>fits</i><br>can look more expensive<br>than a $600 coat that doesn&#8217;t.', nx(8) + 0.3, en(8) + 0.3, QL, size=56)
lclip([(K('c_knee0'), nx(9)), (K('c_shoulder15', 0, 6.0), at(9, 'First, the shoulder'))], nx(10))
q('Check the fit<br><i>in the mirror</i>.', nx(9) + 0.3, at(9, 'First, the shoulder') - 0.2, QL, size=70)
q('The shoulder seam sits at<br><i>the edge of your shoulder</i>.', at(9, 'First, the shoulder'), en(9) + 0.3, QL, size=56)
lclip([(K('c_arms4'), nx(10)), (K('c_arms12'), at(10, 'If the whole'))], nx(11))
q('<i>Lift both arms.</i><br>If the coat rides up to your waist,<br>it&#8217;s too small.', nx(10) + 0.3, en(10) + 0.3, QL, size=56)
lclip([(K('c_sleeve13'), nx(11))], nx(12))
q('Sleeves end at<br><i>your wrist bone</i>.', nx(11) + 0.3, en(11) + 0.3, QL, size=70)
lrow([K('c_hip3'), K('c_knee14')], [nx(12), at(12, 'or around')], nx(13), labels=['just below the hip', 'around the knee'])
q('The two most<br><i>polished lengths</i>.', at(12, 'Those two') - 0.1, en(12) + 0.3, QR2, size=58)
lclip([(K('c_tryon8'), nx(13))], nx(14))
q('Wool-blend coats,<br><i>secondhand</i>.', nx(13) + 0.3, at(13, 'and check') - 0.2, QL, size=70)
item('ph_label.png', 1264, 880, 640, at(13, 'and check') - 0.1, nx(14), label='at least 50% wool')
cfull([(K('c_shoulder2', 0, 15.1), nx(14))], nx(15))
q('A tailor can shorten the sleeves<br>for <i>far less</i>.', nx(14) + 0.3, en(14) + 0.3, QC, size=72, cls='over')
lclip([(K('c_camel13'), nx(15))], at(15, 'in a classic') - 0.1)
q('The one piece<br><i>worth spending on</i>.', nx(15) + 0.3, at(15, 'in a classic') - 0.2, QL, size=70)
lrow([K('c_camel21', 3.57, 12.27), K('c_charcoal7', 0, 6.07), K('c_brown8', 2.5, 9.4)], [at(15, 'in a classic') - 0.2, at(15, 'charcoal'), at(15, 'chocolate brown')], nx(16), w=480,
     labels=['camel', 'charcoal', 'chocolate brown'])
item('ph_browncoat.png', 1680, 900, 760, at(15, 'which is one') - 0.1, nx(16), label='this season&#8217;s colour', maxw=420)

# ================= 2. KNITWEAR THAT LOOKS LIKE QUALITY =================
card_at('2. Choose knitwear that looks like quality', 16, en(16) + 0.3, size=92)
lclip([(K('k_test9', 0, 5.57), st(17) - 0.1), (K('k_test11'), at(17, 'The difference'))], nx(18))
q('Same price.<br><i>Not the same sweater.</i>', st(17) + 0.2, at(17, 'The difference') - 0.2, QL, size=66)
q('The difference is<br><i>the fabric and the care</i>.', at(17, 'The difference'), en(17) + 0.3, QL, size=62)
lclip([(K('k_merino4', 2.09, 7.67), nx(18)), (K('k_cashmere0'), at(18, 'Then rub'))], nx(19))
q('<i>Pinch it.</i><br>It should spring back.', at(18, 'Pinch') - 0.1, at(18, 'Then rub') - 0.2, QL, size=66)
q('<i>Rub it with your thumb.</i><br>Fuzz in the store<br>means pills at home.', at(18, 'Then rub'), en(18) + 0.3, QL, size=58)
lclip([(K('k_cashmere7', 0, 7.73), nx(19))], nx(20))
pieces([('ph_lambswool.png', 'merino &amp; lambswool'), ('ph_cashmere2.png', 'cashmere')], [at(19, 'merino'), at(19, 'cashmere')], nx(20))
lrow([K('k_pill8', 0.23, 10.29), K('k_pill9'), K('k_pill16', 0, 8.0)], [nx(20), at(20, 'those tiny'), at(20, 'is one of')], nx(21))
lclip([(K('k_shaver6'), nx(21))], nx(22))
item('ph_shaver.png', 1264, 900, 620, nx(21) + 0.3, nx(22), label='a fabric shaver')
lrow([K('k_handwash0'), K('k_dryflat0', 0, 4.5)], [nx(22), at(22, 'and dry')], nx(23), labels=['cold or by hand', 'dry flat'])
bsplit(23, [(K('k_neutral0'), nx(23))], None, [('ph_cashmere3.png', 'one great cashmere sweater')], en_(23),
       bclip=K('k_thrift4', 0, 8.67), blabel='secondhand merino &amp; lambswool')

# ================= 3. TWO OR THREE COLOURS FROM ONE FAMILY =================
card_at('3. Stick to two or three colours from the same family', 24, en(24) + 0.3, size=84)
cfull([(K('p_messy18'), st(25) - 0.1)], at(25, 'The easiest fix') - 0.1)
lclip([(K('p_tonal5'), at(25, 'The easiest fix') - 0.2)], nx(26))
q('Two or three colours<br>from <i>the same family</i>.', at(25, 'The easiest fix'), en(25) + 0.3, QL, size=64)
lrow([K('p_camel10', 0, 8.1), K('p_grey10'), K('p_navy5')], [nx(26), at(26, 'Charcoal'), at(26, 'Navy')], nx(27),
     labels=['camel &amp; cream', 'charcoal &amp; grey', 'navy &amp; white'])
cfull([(K('p_mono22'), nx(27)), (K('p_mono34', 0, 5.8), at(27, "That's why"))], nx(28))
q('Taller. Calmer.<br><i>More expensive.</i>', at(27, "That's why"), en(27) + 0.3, QC, size=84, cls='over')
lrow([K('p_warm26'), K('p_cool19')], [nx(28), at(28, 'cool with cool')], nx(29), labels=['warm with warm', 'cool with cool'])
dot('#c19a6b', 1420, 430, 110, at(28, 'A warm camel') - 0.1, nx(29), label='warm camel', lsize=46)
dot('#cfd8e0', 1730, 430, 110, at(28, 'an icy grey') - 0.1, nx(29), label='icy grey', lsize=46)
lclip([(K('h_closet10'), nx(29)), (K('p_belt8', 0, 9.0), at(29, 'like a black')), (K('p_gold13'), at(29, 'or a gold'))], nx(30))
q('One colour family,<br>then <i>a single contrast</i>.', nx(29) + 0.3, at(29, 'like a black') - 0.2, QL, size=62)
item('ph_blackbelt.png', 1000, 700, 300, at(29, 'like a black') - 0.1, nx(30), label='a black belt', maxw=480)
item('ph_goldear.png', 1560, 860, 520, at(29, 'or a gold') - 0.1, nx(30), label='a gold earring', maxw=420)
bsplit(30, [(K('p_tonal7', 6.0, 20.8), nx(30))], None, [('ph_charcoat.png', 'a wool coat over a cashmere knit')], en_(30),
       bclip=K('p_tonal0'), blabel='neutral basics, one palette')

# ================= 4. SMOOTH HAIR AND SOFT LIPS =================
card_at('4. Smooth, polished hair and soft lips', 31, en(31) + 0.3, size=96)
lrow([K('hr_static11'), K('hr_frizz8'), K('hr_hat7', 0, 8.48), K('lp_chapped18')], [st(32) - 0.2, at(32, 'frizz'), at(32, 'flat hat'), at(32, 'and chapped')],
     at(32, 'because no one') - 0.1, w=480, labels=['static', 'frizz', 'flat hat hair', 'chapped lips'])
cfull([(K('hr_fly9'), at(32, 'because no one') - 0.2)], nx(33))
lclip([(K('hr_oil11', 2.0, 8.07), nx(33)), (K('hr_fly13'), at(33, 'and smooth'))], nx(34))
q('A tiny drop of <i>hair oil</i><br>on your ends and flyaways.', nx(33) + 0.3, en(33) + 0.3, QL, size=58)
lclip([(K('hr_comb6'), nx(34)), (K('hr_boar9', 0.0, 3.9), at(34, 'boar-bristle'))], nx(35))
pieces([('ph_comb.png', 'a wooden comb'), ('ph_boar.png', 'a boar-bristle brush')], [nx(34) + 0.2, at(34, 'boar-bristle')], nx(35))
lclip([(K('hr_bun8'), nx(35)), (K('hr_beret0'), at(35, 'or a low ponytail')), (K('hr_static4'), at(35, 'and when you take'))], nx(36))
q('A low, <i>sleek bun</i><br>under your hat.', nx(35) + 0.3, at(35, 'and when you take') - 0.2, QL, size=66)
q('Take it off,<br><i>finger-comb</i> the top.', at(35, 'and when you take'), en(35) + 0.3, QL, size=66)
lclip([(K('hr_wet0', 0, 5.0), nx(36))], nx(37))
q('Never step into the cold<br>with <i>wet hair</i>.', nx(36) + 0.3, en(36) + 0.3, QL, size=64)
lrow([K('lp_scrub0'), K('lp_balm0', 3.9, 10.44)], [nx(37), at(37, 'then use')], nx(38), labels=['once a week', 'a plain, smooth balm'])
q('Soft lips and smooth hair<br>look expensive <i>on anyone</i>.', at(37, 'Soft lips') - 0.1, en(37) + 0.3, QR2, size=50)
bsplit(38, [(K('hr_fly7'), nx(38))], [('ph_hairoil.png', 'hair oil'), ('ph_lipbalm.png', 'lip balm')], None, en_(38),
       btimes=[at(38, 'hair oil'), at(38, 'lip balm')], sclip=K('hr_trim1'), slabel='a fresh trim')

# ================= THE GUIDE =================
cfull([(K('h_simple29'), nx(39)), (K('c_brown11', 0, 7.47), at(39, 'access the personal') - 0.4), (K('h_winter24'), at(40, 'No more'))], en_(40))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(39, 'access the personal') - 0.2, en(40) + 0.3, QC, cls='over')

# ================= 5. ACCESSORIES THAT LOOK INTENTIONAL =================
card_at('5. Make your accessories look intentional', 41, en(41) + 0.3, size=92)
lrow([K('a_set1'), K('a_set4'), K('a_set17')], [st(42) - 0.2, at(42, 'and gloves'), at(42, 'often a hat')], at(42, 'Think of') - 0.1,
     labels=['a scarf', 'gloves', 'a hat'])
lclip([(K('a_gloves4'), at(42, 'Think of') - 0.2)], nx(43))
q('Think of them as<br><i>free luxury</i>.', at(42, 'Think of'), en(42) + 0.3, QL, size=72)
lrow([K('a_gloves8'), K('a_gloves0', 0, 14.6), K('a_gloves16')], [nx(43), at(43, 'Tan'), at(43, 'brown leather')], nx(44),
     labels=['gloves, coat &amp; bag', 'tan or black', 'brown leather'])
lrow([K('a_scarf4', 12.18, 20.8), K('a_boldscarf8'), K('a_scarf12')], [nx(44), at(44, 'or a quiet'), at(44, 'in wool')], nx(45),
     labels=['a solid colour', 'a quiet pattern', 'wool, no logos'])
lclip([(K('a_boldscarf9'), nx(45)), (K('a_studs7', 0, 12.0), at(45, 'Pearl or gold'))], nx(46))
q('Keep it to<br><i>one statement</i>.', nx(45) + 0.3, at(45, 'Pearl or gold') - 0.2, QL, size=72)
item('ph_studs.png', 1264, 860, 560, at(45, 'Pearl or gold') - 0.1, nx(46), label='pearl or gold studs')
cfull([(K('a_beltcoat9'), nx(46))], at(46, 'It defines') - 0.1)
lclip([(K('a_beltcoat8'), at(46, 'It defines') - 0.2)], nx(47))
item('ph_brownbelt.png', 1264, 640, 260, at(46, 'It defines'), nx(47), label='a belt over your coat', maxw=760)
bsplit(47, [(K('a_scarf11', 0, 20.1), nx(47))], [('ph_gloves.png', 'leather gloves'), ('ph_scarf.png', 'a secondhand wool scarf')],
       [('ph_cashscarf.png', 'one cashmere scarf')], en_(47), btimes=[at(47, 'leather or'), at(47, 'a secondhand')])

# ================= 6. CARE FOR YOUR SHOES AND YOUR COAT =================
card_at('6. Take care of your shoes and your coat', 48, en(48) + 0.3, size=92)
lclip([(K('l_sleek13'), st(49) - 0.1)], at(49, 'Winter is rough') - 0.1)
q('What separates<br><i>polished from tired</i>.', st(49) + 0.3, at(49, 'Winter is rough') - 0.2, QL, size=66)
lrow([K('s_salt1'), K('s_slush10'), K('s_lint5')], [at(49, 'Winter is rough') - 0.2, at(49, 'and slush'), at(49, 'to lint')], nx(50),
     labels=['salt', 'slush', 'lint &amp; wrinkles'])
lclip([(K('s_wipe0', 30.5, 44.0), nx(50)), (K('s_salt2'), at(50, 'If you see'))], nx(51))
q('Wipe your boots<br><i>after wet days</i>.', nx(50) + 0.3, at(50, 'If you see') - 0.2, QL, size=66)
q('Equal parts<br><i>white vinegar and water</i>.', at(50, 'mix equal'), en(50) + 0.3, QL, size=62)
lclip([(K('s_polish9', 0, 20.1), nx(51)), (K('s_suede4', 0, 20.1), at(51, 'For suede'))], nx(52))
q('A little <i>leather cream</i><br>or polish.', nx(51) + 0.3, at(51, 'For suede') - 0.2, QL, size=66)
item('ph_suedebrush.png', 1264, 900, 620, at(51, 'For suede') - 0.1, nx(52), label='a suede brush')
cfull([(K('s_cobbler1'), nx(52)), (K('s_cobbler14', 0, 13.0), at(52, 'and they make'))], nx(53))
lrow([K('s_lint4', 0, 11.0), K('s_hanger3', 0, 4.5)], [nx(53), at(53, 'Hang it')], nx(54), labels=['a lint roller', 'a wide hanger'])
q('So the shoulders<br><i>keep their shape</i>.', at(53, 'so the shoulders') - 0.1, en(53) + 0.3, QR2, size=56)
cfull([(K('s_brush22'), nx(54))], nx(55))
q('A clean, brushed coat<br>looks like it cost <i>twice as much</i>.', nx(54) + 0.2, en(54) + 0.3, QC, size=72, cls='over')
bsplit(55, [(K('s_brush4', 4.3, 13.56), nx(55))], [('ph_roller.png', 'a lint roller'), ('ph_shoecream.png', 'shoe cream'), ('ph_hanger.png', 'a wide hanger')],
       [('ph_garmentbrush.png', 'the cobbler &amp; a garment brush')], en_(55), btimes=[at(55, 'a lint roller'), at(55, 'a shoe cream'), at(55, 'and a wide')])

# ================= 7. LAYER THIN, NOT BULKY =================
card_at('7. Layer thin, not bulky', 56, en(56) + 0.3, size=110)
lrow([K('l_bulky6'), K('l_bulky10', 0, 14.5), K('l_chunky12')], [st(57) - 0.2, at(57, 'but bulk'), at(57, 'look heavy')], at(57, 'The secret') - 0.1)
lclip([(K('l_shirt7'), at(57, 'The secret') - 0.2)], nx(58))
q('<i>Thin to thick.</i><br><i>Fitted to loose.</i>', at(57, 'thin to thick') - 0.1, en(57) + 0.3, QL, size=76)
lclip([(K('l_thermal10'), nx(58)), (K('l_shirt2', 2.0, 6.0), at(58, 'Add a shirt')), (K('l_coaton10'), at(58, 'Then put'))], nx(59))
q('A thin <i>base layer</i>.', nx(58) + 0.3, at(58, 'Add a shirt') - 0.2, QL, size=70)
q('A shirt or <i>a fine knit</i>.', at(58, 'Add a shirt'), at(58, 'Then put') - 0.2, QL, size=70)
q('Your coat <i>on top</i>.', at(58, 'Then put'), en(58) + 0.3, QL, size=70)
lrow([K('l_collar1', 5.54, 14.8), K('l_cuff1', 2.4, 8.0)], [nx(59), at(59, 'and let a half')], nx(60), labels=['the collar out', 'a half inch of cuff'])
q('Tiny details say<br><i>you planned it</i>.', at(59, 'Those tiny') - 0.1, en(59) + 0.3, QR2, size=56)
lclip([(K('l_chunky14', 2.0, 8.2), nx(60))], nx(61))
q('Avoid stacking<br><i>two chunky knits</i>.', nx(60) + 0.3, en(60) + 0.3, QL, size=68)
cfull([(K('l_sleek14'), nx(61))], nx(62))
bsplit(62, [(K('l_thermal14', 7.6, 16.94), nx(62))], [('ph_thermal.png', 'a simple thermal')], [('ph_merinobase.png', 'a soft merino base layer')], en_(62))

# ================= 8. A WARM SIGNATURE SCENT =================
card_at('8. Wear a warm signature scent', 63, en(63) + 0.3, size=104)
lclip([(K('f_vanilla3', 0, 15.83), st(64) - 0.1), (K('f_vanilla0', 8.5, 11.94), at(64, 'while very light'))], nx(65))
q('Scent is<br><i>the finishing touch</i>.', st(64) + 0.2, at(64, 'Warm notes') - 0.2, QL, size=70)
q('Vanilla, amber,<br><i>sandalwood and musk</i>.', at(64, 'Warm notes'), at(64, 'while very light') - 0.2, QL, size=66)
q('Light, fresh scents<br><i>fade quickly</i> in the cold.', at(64, 'while very light'), en(64) + 0.3, QL, size=60)
lclip([(K('f_lotion1'), nx(65))], nx(66))
q('Right after<br><i>moisturising</i>.', nx(65) + 0.3, en(65) + 0.3, QL, size=72)
lrow([K('f_spray7'), K('f_spray8')], [nx(66), at(66, 'the base of')], at(66, 'A little goes') - 0.1,
     labels=['your wrists', 'your neck &amp; behind your ears'])
cfull([(K('f_spray12'), at(66, 'A little goes') - 0.2)], nx(67))
q('Noticed only<br><i>when they&#8217;re close</i>.', at(66, 'A little goes'), en(66) + 0.3, QC, size=76, cls='over')
bsplit(67, [(K('f_oil3', 15.0, 26.0), nx(67))], [('ph_bodyoil.png', 'body oil'), ('ph_solidperf.png', 'solid perfume'), ('ph_travelperf.png', 'travel size')],
       [('ph_perfume.png', 'one full-size bottle')], en_(67), btimes=[at(67, 'a body oil'), at(67, 'a solid'), at(67, 'or a travel')])

# ================= BONUS: ONE OUTFIT, THREE BUDGETS =================
card_at('One winter outfit, three budgets', 68, en(68) + 0.3, size=100)
lclip([(K('o_outfit16'), nx(69)), (K('o_formula34'), at(69, 'like camel'))], nx(70))
q('<i>The formula</i>', nx(69) + 0.2, nx(70) - 0.1, TT, size=76)
pieces([('ph_camelcoat.png', 'a coat'), ('ph_creamknit.png', 'a knit'), ('ph_tailtrous.png', 'trousers'), ('ph_boots.png', 'boots')],
       [at(69, 'a coat'), at(69, 'a knit'), at(69, 'trousers'), at(69, 'and boots')], nx(70), ybot=900, hh=600)
lclip([(K('o_outfit2', 0, 4.8), nx(70)), (K('o_budget4'), at(70, 'dark trousers'))], nx(71))
q('<i>Budget</i>', nx(70) + 0.1, nx(71) - 0.1, TT, size=80)
pieces([('ph_camelcoat2.png', 'secondhand wool blend'), ('ph_creamknit2.png', 'pills removed'), ('ph_darktrous.png', 'hemmed to the boot'), ('ph_fauxgloves.png', 'faux-leather gloves')],
       [at(70, 'a secondhand'), at(70, 'a cream knit'), at(70, 'dark trousers'), at(70, 'and faux-leather')], nx(71), ybot=900, hh=600)
lclip([(K('o_mid2'), nx(71))], nx(72))
q('<i>Mid-range</i>', nx(71) + 0.1, nx(72) - 0.1, TT, size=80)
pieces([('ph_camelcoat3.png', 'high-street wool blend'), ('ph_merino.png', 'merino'), ('ph_tailtrous2.png', 'tailored trousers'), ('ph_boots2.png', 'leather boots')],
       [at(71, 'a wool-blend'), at(71, 'a merino'), at(71, 'tailored'), at(71, 'and leather')], nx(72), ybot=900, hh=600)
lclip([(K('o_outfit9', 0, 12.0), nx(72)), (K('o_lux13'), at(72, 'wool trousers'))], nx(73))
q('<i>Splurge</i>', nx(72) + 0.1, nx(73) - 0.1, TT, size=80)
pieces([('ph_woolcash.png', 'wool-cashmere'), ('ph_cashmere.png', 'cashmere'), ('ph_tailtrous3.png', 'wool trousers'), ('ph_boots3.png', 'leather boots'), ('ph_cashscarf2.png', 'a cashmere scarf')],
       [at(72, 'a wool-cashmere'), at(72, 'a cashmere knit'), at(72, 'wool trousers'), at(72, 'leather boots'), at(72, 'and a soft')], nx(73), ybot=900, hh=560, lsize=38)
lrow([K('p_camel9', 0, 12.37), K('o_mid7', 0.0, 4.54), K('o_lux3')], [nx(73), nx(73) + 0.4, nx(73) + 0.8], at(73, 'Only the fabric') - 0.1,
     labels=['budget', 'mid-range', 'splurge'])
cfull([(K('o_same9'), at(73, 'Only the fabric') - 0.2)], en_(73))
q('Same colours. Same shapes.<br><i>Only the fabric changes.</i>', at(73, 'Only the fabric') - 0.1, en(73) + 0.4, QC, size=72, cls='over')

# ================= CLOSE =================
cfull([(K('e_bye10'), nx(74)), (K('e_comment6'), at(74, 'and tell me'))], nx(75))
cfull([(K('e_bye14', 0, 12.03), nx(75)), (K('o_same3', 0, 7.0), at(75, 'access the personal') - 0.4)], nx(76))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(75, 'access the personal') - 0.2, en(75) + 0.4, QC, cls='over')
cfull([(K('e_bye9'), nx(76))], nx(77))
cfull([(K('e_bye19', 0, 5.9), nx(77))], total - 2.6)
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
