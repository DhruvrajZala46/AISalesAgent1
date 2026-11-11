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


# Understated Winter Footwear Rules That Instantly Elevate Everyday Outfits - beat map (11 Nov 2026)
# Layouts of the channel's own winter video ("7 Things Elegant Ladies Never Wear in Winter", JF7PzFJl4eU; VISUAL-ANALYSIS.md):
# white numbered cards; the problem shown literally in a row of clips; the fix beside its product cut out on the caramel;
# "the test" written line by line beside a clip of the test; the guide over a full clip; the CE logo. Every clip once.

def en_(i): return en(i) + 0.5
MID = (PW + 1880) // 2
CROP['r6_rubber4'] = (60, 0, 980)    # past the small captions at the bottom
def qstack(lines, times, t1, box_=QL, size=58, rh=150):
    """the lesson lines one under the other beside a clip, each appearing as it is said"""
    x0, y0, x1, y1 = box_; n = len(lines); top = (y0 + y1) // 2 - n * rh // 2
    for k, (txt, tt) in enumerate(zip(lines, times)):
        q(txt, tt, t1, (x0, top + k * rh, x1, top + (k + 1) * rh), size=size, dur=1.0)
def fix(clips, t1, title, t_title, png, label, t_item, title2=None, t_title2=None):
    """the fix: a clip at the left, a line at the top of the caramel, the product cut out beneath it as it is named"""
    lclip(clips, t1)
    q(title, t_title, (t_title2 - 0.2) if title2 else t1 - 0.1, TT, size=56)
    if title2: q(title2, t_title2, t1 - 0.1, TT, size=56)
    item(png, MID, 960, 600, t_item, t1, label=label, maxw=620, lsize=50)

# ================= HOOK =================
cfull([(K('h_down1'), 0.0), (K('h_down5'), at(1, 'they quietly'))], nx(2))
q('Before anyone hears you speak&#8230;<br><i>they quietly glance down.</i>', at(1, 'before anyone') - 0.1, en(1) + 0.3, QC, size=70, cls='over')
lclip([(K('h_flatlay3'), nx(2)), (K('h_worn8'), at(2, 'could guess'))], nx(3))
q('A photo of someone&#8217;s<br><i>most-worn shoes</i>', at(2, 'a photo') - 0.1, at(2, 'could guess') - 0.2, QL, size=66)
q('Their age and income,<br><i>better than chance</i>', at(2, 'could guess'), en(2) + 0.3, QL, size=66)
cfull([(K('h_campus0'), nx(3))], at(3, 'But it tells') - 0.1)
q('A small study,<br><i>not a rule.</i>', at(3, 'a small study') - 0.1, at(3, 'But it tells') - 0.2, QC, size=80, cls='over')
cfull([(K('h_down9'), at(3, 'But it tells') - 0.2)], en_(3))
q('Shoes are <i>read fast.</i>', at(3, 'Shoes are') - 0.1, en(3) + 0.4, QC, size=96, cls='over')
cfull([(K('h_boots17', 0.54, 8.6), nx(4))], at(4, 'and once') - 0.1)
q('<div><span style="font-size:44px">8 Understated</span><br><i style="font-size:118px">Winter Footwear Rules</i></div>',
  at(4, 'eight') - 0.1, at(4, 'and once') - 0.2, QC, cls='over')
lrow([K('h_outfit12'), K('h_outfit4'), K('h_boots9')], [at(4, 'and once') - 0.2, at(4, "you'll never"), at(4, 'unsee')], en_(4))

# ================= 1. THE HEEL CHECK =================
card_at('1. The Heel Check', 5, en(5) + 0.3, size=110)
lrow([K('r1_tired6'), K('r1_wet13'), K('r1_grit19')], [nx(6), at(6, 'In winter'), at(6, 'and grit')], en_(6),
     labels=['worn to the metal', 'wet pavement', 'and grit'])
lclip([(K('r1_click8'), nx(7)), (K('r1_tired3'), at(7, 'and it makes'))], en_(7))
q('A worn heel<br><i>does two things.</i>', nx(7) + 0.2, at(7, 'It clicks') - 0.2, QL, size=70)
qstack(['It clicks and scrapes', '<i>with every step,</i>', 'and the whole shoe <i>looks tired.</i>'],
       [at(7, 'It clicks'), at(7, 'with every'), at(7, 'and it makes')], en(7) + 0.4, size=62)
fix([(K('r1_cobbler1'), nx(8)), (K('r1_heeltip18'), at(8, 'replace the heel'))], en_(8),
    'Take your boots<br><i>to a cobbler</i>', nx(8) + 0.2, 'ph_heeltip.png', 'a new heel tip', at(8, 'the heel tip'))
lclip([(K('r1_cobbler6', 0, 4.7), nx(9)), (K('r1_repair15'), at(9, 'which is'))], en_(9))
q('Usually quick, and it protects<br><i>the heel itself</i>', nx(9) + 0.2, en(9) + 0.4, QL, size=62)
lclip([(K('r1_mirror8', 0.0, 5.42), nx(10)), (K('r1_behind17'), at(10, 'If the heel'))], en_(10))
qstack(['<i>The test:</i>', 'stand in front of a mirror,', '<i>look at your shoes from behind.</i>', 'Heel leans or tip thin? <i>It&#8217;s time.</i>'],
       [nx(10) + 0.2, at(10, 'Stand in'), at(10, 'look at your'), at(10, 'If the heel')], en(10) + 0.4, size=56, rh=135)

# ================= 2. THE TWENTY-FOUR HOUR RULE =================
card_at('2. The Twenty-Four Hour Rule', 11, en(11) + 0.3, size=100)
lclip([(K('r2_fav7'), nx(12)), (K('r2_leather0'), at(12, 'But feet'))], en_(12))
q('Our favourite pair,<br><i>every single day</i>', nx(12) + 0.2, at(12, 'But feet') - 0.2, QL, size=66)
q('Shoes can take around<br><i>24 hours to fully dry</i>', at(12, 'can take'), en(12) + 0.4, QL, size=64)
lrow([K('r2_crease1'), K('r2_crease7'), K('r2_crease12')], [nx(13), at(13, 'lose their'), at(13, 'and start')], en_(13),
     labels=['crease deeper', 'lose their shape', 'start to smell'])
fix([(K('r2_rotate3'), nx(14)), (K('r2_trees0'), at(14, 'and place'))], en_(14),
    'Rotate <i>two or three pairs</i>', nx(14) + 0.2, 'ph_shoetree.png', 'wooden shoe trees', at(14, 'wooden shoe'),
    'They hold the shape<br><i>while the leather dries</i>', at(14, 'They hold'))
lclip([(K('r2_smooth12', 6.9, 13.2), nx(15))], en_(15))
qstack(['<i>The test:</i>', 'look at the toe of your boot.', 'Smooth, holding its line?', '<i>You&#8217;re doing it right.</i>'],
       [nx(15) + 0.2, at(15, 'look at'), at(15, "If it's"), at(15, "you're doing")], en(15) + 0.4, size=58, rh=135)

# ================= 3. THE HEEL-SLIP TEST =================
card_at('3. The Heel-Slip Test', 16, en(16) + 0.3, size=110)
lclip([(K('r3_box2'), nx(17)), (K('r3_walk30', 1.9, 14.42), at(17, 'and feel'))], en_(17))
q('Perfect in the box,<br><i>a little loose when you walk</i>', nx(17) + 0.2, en(17) + 0.4, QL, size=62)
cfull([(K('r3_walk25', 0, 12.64), nx(18))], en_(18))
q('About a quarter of an inch<br><i>is normal</i>', at(18, 'about a quarter') - 0.1, en(18) + 0.4, QC, size=78, cls='over')
lrow([K('r3_slip18'), K('r3_slip21'), K('r3_slip30')], [nx(19), at(19, 'the fit is off'), at(19, "and you'll walk")], en_(19),
     labels=[None, 'the fit is off', 'hurried, shuffling'])
fix([(K('r3_tryon5'), nx(20)), (K('r3_walk19'), at(20, 'The boot should')), (K('r3_liner5'), at(20, 'If the slip'))], en_(20),
    'Walk around properly<br><i>before buying</i>', nx(20) + 0.2, 'ph_heelgrip.png', 'small heel liners', at(20, 'small heel'),
    'The boot should move<br><i>with your foot</i>', at(20, 'The boot should'))
fix([(K('r3_socks9', 0, 15), nx(21)), (K('r3_fit12'), at(21, 'go up'))], en_(21),
    'Try them on with<br><i>the socks you&#8217;ll wear</i>', nx(21) + 0.2, 'ph_woolsock.png', 'thick winter socks', at(21, 'thick winter'),
    'Half a size up,<br><i>or a wider fit</i>', at(21, 'go up'))

# ================= 4. THE SMALL PARTS =================
card_at('4. The Small Parts', 22, en(22) + 0.3, size=110)
lrow([K('r4_lace1'), K('r4_lace5'), K('r4_zip5')], [nx(23), at(23, 'A missing'), at(23, 'A zip')], at(23, 'These are') - 0.1,
     labels=['a frayed lace', 'a missing tip', 'a zip that gapes'])
cfull([(K('r4_lace15'), at(23, 'These are') - 0.2)], en_(23))
q('The first things people see<br><i>up close</i>', at(23, 'the first') - 0.1, en(23) + 0.4, QC, size=76, cls='over')
fix([(K('r4_newlace10'), nx(24)), (K('r1_cobbler10'), at(24, 'and take a sticky'))], en_(24),
    'Fresh flat laces<br><i>in a matching tone</i>', nx(24) + 0.2, 'ph_flatlace2.png', 'fresh flat laces', at(24, 'fresh flat'),
    'A sticky zip?<br><i>To the cobbler.</i>', at(24, 'and take a sticky'))
lclip([(K('r4_daylight0'), nx(25))], en_(25))
qstack(['<i>The test:</i>', 'look at your shoes <i>in daylight,</i>', 'not in your bedroom light.'],
       [nx(25) + 0.2, at(25, 'look at'), at(25, 'not in')], en(25) + 0.4, size=60)

# ================= THE GUIDE =================
cfull([(K('m_style12', 8.03, 12.73), nx(26)), (K('m_style14'), at(26, "They don't guess"))], nx(27))
lrow([K('cl_drape14'), K('m_shape0'), K('m_hair10')], [nx(27), at(27, 'how to dress'), at(27, 'which hairstyles')], at(27, 'and how to move') - 0.1,
     labels=['best colours', 'your unique shape', 'hairstyles'])
cfull([(K('m_walk18'), at(27, 'and how to move') - 0.2)], nx(28))
cfull([(K('m_walk31'), nx(28)), (K('h_outfit19'), at(28, 'It will be sent'))], en_(28))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>',
  at(28, 'our personal') - 0.2, en(28) + 0.3, QC, cls='over')

# ================= 5. THE PALE-BOOT PROBLEM =================
card_at('5. The Pale-Boot Problem', 29, en(29) + 0.3, size=104)
lclip([(K('r5_cream3'), nx(30)), (K('r5_white10', 0, 6.0), at(30, 'but they show')), (K('r5_cream7'), at(30, 'One 2026'))], en_(30))
q('Beautiful in photos,<br><i>but they show every scuff</i>', nx(30) + 0.2, at(30, 'One 2026') - 0.2, QL, size=62)
q('Cream boots<br><i>mark easily</i>', at(30, 'One 2026'), en(30) + 0.4, QL, size=72)
lclip([(K('r5_white11', 0, 3.9), nx(31)), (K('r5_cream10'), at(31, 'reads as'))], en_(31))
q('A scuffed toe, a grey edge:<br><i>it reads as careless</i>', nx(31) + 0.2, en(31) + 0.4, QL, size=60)
lclip([(K('r5_white5'), nx(32)), (K('r5_clean3'), at(32, 'and keep'))], en_(32))
q('Pale boots<br><i>for dry days</i>', nx(32) + 0.2, at(32, 'and keep') - 0.2, TT, size=56)
q('A matching polish<br><i>or cleaner</i>', at(32, 'and keep'), en(32) + 0.4, TT, size=56)
pieces([('ph_polish.png', 'polish'), ('ph_cleaner.png', 'cleaner')], [at(32, 'matching polish'), at(32, 'or cleaner')], en_(32), ybot=900, hh=520, lsize=50)
lrow([K('r5_brown4'), K('r5_burgundy0'), K('r5_black10')], [nx(33), at(33, 'burgundy'), at(33, 'and black')], en_(33),
     labels=['deep brown', 'burgundy', 'black'])
lclip([(K('r5_window11', 2.1, 8.16), nx(34))], en_(34))
qstack(['<i>The test:</i>', 'tilt the boot toward a window.', 'If you can see the scuffs,', '<i>so can everyone else.</i>'],
       [nx(34) + 0.2, at(34, 'tilt'), at(34, 'If you can'), at(34, 'so can')], en(34) + 0.4, size=58, rh=135)

# ================= 6. THE QUIET WALK =================
card_at('6. The Quiet Walk', 35, en(35) + 0.3, size=110)
lrow([K('r1_click0', 0, 9), K('r6_shop12', 3.53, 9.03), K('r6_marble16')], [nx(36), at(36, 'a sole that'), at(36, 'a boot that')], en_(36),
     labels=['clicks sharply', 'squeaks on shop floors', 'slaps with every step'])
cfull([(K('r6_quiet7'), nx(37))], en_(37))
q('Elegant women tend to<br><i>move quietly.</i>', nx(37) + 0.1, en(37) + 0.4, QC, size=84, cls='over')
lclip([(K('r6_rubber4', 0.0, 7.98), nx(38)), (K('r6_quiet16'), at(38, 'It also helps'))], en_(38))
qstack(['A thin <i>rubber heel tip,</i>', 'soles with <i>a little grip,</i>', 'calm, <i>even steps.</i>'],
       [at(38, 'a thin rubber'), at(38, 'and look for'), at(38, 'It also helps')], en(38) + 0.4, size=62)
lclip([(K('r6_floor19', 0, 6.0), nx(39)), (K('r6_floor25'), at(39, 'If you wince'))], en_(39))
qstack(['<i>The test:</i>', 'walk across a hard floor at home.', 'If you wince at the sound,', '<i>so will other people.</i>'],
       [nx(39) + 0.2, at(39, 'walk across'), at(39, 'If you wince'), at(39, 'so will')], en(39) + 0.4, size=58, rh=135)

# ================= 7. ONE TREND DETAIL, NEVER THREE =================
card_at('7. One Trend Detail, Never Three', 40, en(40) + 0.3, size=96)
lclip([(K('r7_croc2', 12.12, 21.62), nx(41))], en_(41))
pieces([('ph_crocboot.png', 'glossy croc'), ('ph_buckleboot.png', 'big buckles'), ('ph_sockboot.png', 'sock shafts'), ('ph_cowboyboot.png', 'cowboy edges')],
       [at(41, 'Glossy croc'), at(41, 'big buckles'), at(41, 'stretched'), at(41, 'cowboy')], en_(41), ybot=860, hh=560, lsize=42)
lrow([K('r7_buckle5'), K('r7_sock4'), K('r7_cowboy9')], [nx(42), at(42, 'several loud'), at(42, 'busy')], en_(42))
lclip([(K('r7_minimal9'), nx(43)), (K('r7_minimal13', 0, 3.8), at(43, 'keep everything')), (K('r5_black32'), at(43, 'a clean line'))], en_(43))
qstack(['Let the shape <i>do the talking.</i>', 'One detail you love,', 'a plain coat, a simple trouser,', '<i>a clean line.</i>'],
       [nx(43) + 0.2, at(43, 'Pick one'), at(43, 'a plain coat'), at(43, 'a clean line')], en(43) + 0.4, size=58, rh=135)
lclip([(K('r5_black34'), nx(44))], en_(44))
qstack(['<i>The test:</i>', 'can you describe the boot', 'in more than three words?', '<i>It might be doing too much.</i>'],
       [nx(44) + 0.2, at(44, 'if you can'), at(44, 'in more than'), at(44, 'it might')], en(44) + 0.4, size=58, rh=135)

# ================= 8. THE INSIDE MOMENT =================
card_at('8. The Inside Moment', 45, en(45) + 0.3, size=110)
lrow([K('r8_friend0'), K('r8_airport0'), K('r8_door1', 0, 6.4)], [nx(46), at(46, 'at an airport'), at(46, 'at a dinner')], en_(46),
     labels=['at a friend&#8217;s home', 'airport security', 'shoes at the door'])
lclip([(K('in_off22'), nx(47)), (K('in_damp5'), at(47, 'or the boots'))], en_(47))
q('Your shoes are on show,<br><i>inside and out</i>', nx(47) + 0.2, at(47, 'If the insole') - 0.2, QL, size=64)
q('A grey, worn insole<br><i>undoes everything</i>', at(47, 'If the insole'), en(47) + 0.4, QL, size=64)
fix([(K('r8_dry2'), nx(48)), (K('in_insole25', 9.5, 30), at(48, 'and swap'))], en_(48),
    'Let your boots dry,<br><i>use shoe trees</i>', nx(48) + 0.2, 'ph_insole.png', 'fresh insoles', at(48, 'and swap'))
lclip([(K('in_off13'), nx(49))], en_(49))
qstack(['<i>The test:</i>', 'slip your boot off and look inside.', 'Happy for someone else to see it?', '<i>You&#8217;re ready.</i>'],
       [nx(49) + 0.2, at(49, 'slip your'), at(49, "If you'd"), at(49, "you're ready")], en(49) + 0.4, size=58, rh=135)

# ================= CLOSE =================
cfull([(K('e_walk7', 0, 7.04), nx(50)), (K('e_walk25'), at(50, "And if you're")), (K('e_walk29'), at(50, 'the personal') - 0.4)], nx(51))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>',
  at(50, 'the personal') - 0.2, en(50) + 0.4, QC, cls='over')
cfull([(K('e_comment0'), nx(51)), (K('e_bye5'), at(51, 'Until next'))], total - 2.6)
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
