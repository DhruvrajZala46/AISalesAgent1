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
    if need > seg: speed = min(MAXSLOW.get(key, 1.4), need / seg)
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
    if need > seg: speed = min(MAXSLOW.get(key, 1.4), need / seg)
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
# Princess Diana's 7 Jewels: Who Wears Them Now? (The Classy Elegance) - beat map (19 Nov 2026)
# Layouts: only those read off the channel's own videos (VISUAL-EDITING-DNA.md; videos/unforgettable-charm/VISUAL-ANALYSIS.md):
#   full clips (the whole vertical clip over its own blurred copy) | the rule's name on a white card in script |
#   a clip on the caramel with the lesson in white lines beside it, appearing as they are said | rows of clips |
#   a framed clip on cream with the EXACT WORDS in script beside it | two framed pictures under a small label (a comparison) |
#   one sentence alone on the caramel | the NAMED WOMAN shown in real archive film and real press photographs, framed on the
#   caramel with the place and year in script (the channel shows a named woman in photos and archive film: Audrey, Diana, Grace) |
#   the guide over a full clip | the CE logo.
# Sound: the voice and ONE soft solo-piano bed, steady, no ducking, NO sound effects (none are in the channel's measured files).
TRACKS_EDIT = ['healinge.mp3', 'gym2e.mp3']; MUSIC_DB = 13; ENDLOGO = 'logo_ce_dark.png'
MUSIC_CREDIT = 'Music: "Healing" and "Gymnopedie No 2" by Kevin MacLeod (incompetech.com), licensed under Creative Commons: By Attribution 4.0 (creativecommons.org/licenses/by/4.0/)'
def en_(i): return en(i) + 0.5
def qstack(lines, times, t1, box_=QL, size=58, rh=150, cls=''):
    """lines one under the other beside a clip, each appearing as it is said"""
    x0, y0, x1, y1 = box_; n = len(lines); top = (y0 + y1) // 2 - n * rh // 2
    for k, (txt, tt) in enumerate(zip(lines, times)):
        q(txt, tt, t1, (x0, top + k * rh, x1, top + (k + 1) * rh), size=size, dur=1.0, cls=cls)
PX = 250                                              # the framed clip of a phrase screen (540 x 960, rounded) on cream
PB = (860, 60, 1850, 1020)                            # the words beside it
def pframe(shots, t1, x0=PX):
    """the speech video's phrase screen: a rounded framed clip at the left of the cream backdrop"""
    return cframe(shots, t1, x0=x0)
def pwords(lines, times, t1, size=60, rh=170, box_=PB):
    """the exact words in dark script beside the framed clip, each line appearing as it is said"""
    qstack(lines, times, t1, box_, size=size, rh=rh, cls='dark')
GUIDE = '<div><span style="font-size:50px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>'
exec(open(os.path.join(P, 'clips.py')).read())      # C: slot -> (key, start, end); every window checked by eye. CROP / MAXSLOW per key.
def c(n): return K(*C[n])
def veil(t0, t1, a=0.46):
    """the channel puts its titles over a DARK full clip: a soft dark glow behind the words, the clip still shows round it"""
    i = nid('vl')
    els.append(f'<div id="{i}" style="position:absolute;inset:0;z-index:44;opacity:0;pointer-events:none;'
               f'background:radial-gradient(ellipse 50% 46% at 50% 50%, rgba(22,15,11,{a}) 0%, rgba(22,15,11,{a*0.6:.2f}) 55%, rgba(22,15,11,0) 100%)"></div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0}},{{opacity:1,duration:0.5,ease:"sine.out"}},{max(t0 - 0.2, 0):.3f});'); fade_out(i, t1, 0.5)
_q0 = q
def q(html, t0, t1, box_=(660, 0, 1880, H), size=58, cls='', dur=1.4):
    if 'over' in cls and box_ == QC: veil(t0, t1)
    return _q0(html, t0, t1, box_, size=size, cls=cls, dur=dur)
# ---- real press photographs of Diana: framed on the caramel, a slow push-in so a still never sits dead ----
def pic(name, x0, y0, w, h, t0, t1, label=None, pos='50% 30%', zoom=1.08, lsize=50, origin='50% 35%'):
    i = nid('ph'); j = nid('pi'); PHOTOS.append(name)
    els.append(f'<div id="{i}" class="w" style="left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;opacity:0;border-radius:6px;overflow:hidden;box-shadow:0 24px 56px rgba(60,30,12,.30)">'
               f'<img id="{j}" src="assets/{name}" class="photo" style="object-position:{pos};transform-origin:{origin}"></div>')
    _rise(i, t0, t1); tw.append(f'tl.fromTo("#{j}",{{scale:1}},{{scale:{zoom},duration:{t1-t0+0.6:.2f},ease:"none"}},{t0:.3f});')
    if label: plabel(label, x0 + w // 2, y0 + h + 6, t0 + 0.35, t1, lsize)
    return i
PH_H = 900                                              # a tall photo frame, 60 px above, room for the label below
def pics(items, times, t1, h=PH_H, y0=60, gap=44, x0=None, x1=None, zoom=1.08):
    """a row of framed photographs, centred (or inside x0..x1); items = (file, aspect w/h shown, label, object-position)"""
    ws = [int(h * it[1]) for it in items]; tot = sum(ws) + gap * (len(items) - 1); room = (W if x0 is None else x1 - x0) - 80
    if tot > room: h = int(h * (room - gap * (len(items) - 1)) / sum(ws)); ws = [int(h * it[1]) for it in items]; tot = sum(ws) + gap * (len(items) - 1)
    xa = (W - tot) // 2 if x0 is None else x0 + ((x1 - x0) - tot) // 2
    for it, tt, w_ in zip(items, times, ws):
        pic(it[0], xa, y0, w_, h, tt, t1, label=it[2] if len(it) > 2 else None, pos=it[3] if len(it) > 3 else '50% 30%', zoom=zoom); xa += w_ + gap
def picfull(name, t0, t1, pos='50% 30%', zoom=1.06, wfrac=None):
    """a photograph as a full screen the channel's way: the whole picture in the centre over its own soft blurred copy"""
    im = _PILImage.open(os.path.join(A, name)); r = im.width / im.height; w_ = int(min(W, H * r)) if wfrac is None else int(W * wfrac)
    i = nid('pf'); j = nid('pj'); PHOTOS.append(name)
    els.append(f'<div id="{i}" class="w" style="left:0;top:0;width:{W}px;height:{H}px;opacity:0;overflow:hidden">'
               f'<img src="assets/{name}" style="position:absolute;left:-5%;top:-5%;width:110%;height:110%;object-fit:cover;filter:blur(28px) brightness(.90) saturate(.9)">'
               f'<div style="position:absolute;left:{(W-w_)//2}px;top:0;width:{w_}px;height:{H}px;overflow:hidden"><img id="{j}" src="assets/{name}" class="photo" style="object-position:{pos};transform-origin:50% 35%"></div></div>')
    fade_in(i, t0, 0.5); fade_out(i, t1, 0.55)
    tw.append(f'tl.fromTo("#{j}",{{scale:1}},{{scale:{zoom},duration:{t1-t0+0.6:.2f},ease:"none"}},{t0:.3f});'); return i
def when(txt, t0, t1, size=64, y=930):
    """the place and year of an archive picture, in script along the bottom of a full picture"""
    return q(f'<i>{txt}</i>', t0, t1, (180, y, 1740, y + 130), size=size, cls='over', dur=0.9)
def asp(n): im = _PILImage.open(os.path.join(A, n)); return im.width / im.height
def P_(n, label=None, pos='50% 30%', a=None): return (n + '.jpg', a or asp(n + '.jpg'), label, pos)
QB = (160, 810, 1760, 1050)                              # a line along the bottom of a full picture
R3 = (2 * PW + 40, 60, 1890, 1020)                       # the right third beside two clips
RT = (1250, 60, 1890, 1020)                              # the right column beside two framed photographs
def band(html, t0, t1, size=60): return q(html, t0, t1, QB, size=size, cls='over', dur=1.0)
def cardx(txt, t0, t_out, size=None):
    white(t0, t_out); text(txt, 'card', t0 + 0.3, t_out - 0.1, dur=1.2, out=0.45, style=f'font-size:{size}px;' if size else '')
def capt(html, t0, t1, size=56, y=925): return q(html, t0, t1, (160, y, 1760, y + 130), size=size, dur=1.0)
def look(big, small, lines, times, t0, t1, tsmall, pos_b='50% 20%', pos_s='50% 20%'):
    """one off-duty outfit: a tall photograph at the left, a second one beside it, the pieces named at the right as they are said"""
    ab = asp(big + '.jpg'); hb = 980; wb = int(hb * ab); pic(big + '.jpg', 110, 50, wb, hb, t0, t1, pos=pos_b)
    as_ = asp(small + '.jpg'); ws = 400; hs = int(ws / as_)
    if hs > 640: hs = 640; ws = int(hs * as_)
    xs = 110 + wb + 50; pic(small + '.jpg', xs, (H - hs) // 2, ws, hs, tsmall, t1, pos=pos_s)
    qstack(lines, times, t1, box_=(xs + ws + 30, 60, 1890, 1020), size=54, rh=140)
# ================= HOOK (reference: full clips, then the title over a clip) =================
cfull([(c('h1a'), 0.0)], at(1, 'A sapphire ring') - 0.1)
q('Have you ever noticed<br><i>the jewel before the dress?</i>', at(1, 'Have you ever'), at(1, 'A sapphire ring') - 0.3, QC, size=72, cls='over')
picfull('pengage_2.jpg', at(1, 'A sapphire ring') - 0.1, at(1, 'Pearls at her') - 0.1, pos='50% 40%')
picfull('pcoll_19.jpg', at(1, 'Pearls at her') - 0.1, at(1, 'A necklace worn') - 0.1, pos='50% 30%')
picfull('pheadband_16.jpg', at(1, 'A necklace worn') - 0.1, nx(2), pos='50% 30%')
cfull([(c('h2a'), nx(2)), (c('h2b'), at(2, 'Some went back')), (c('h2c'), at(2, 'Some went home')), (c('h2d'), at(2, 'And one is'))], nx(3))
q('Almost thirty years later,<br><i>where is every piece today?</i>', st(2) + 0.2, at(2, 'Some went back') - 0.2, QC, size=70, cls='over')
q('<i>Some went back to the palace.</i>', at(2, 'Some went back'), at(2, 'Some went home') - 0.2, QC, size=72, cls='over')
q('<i>Some went home to her family.</i>', at(2, 'Some went home'), at(2, 'And one is') - 0.2, QC, size=72, cls='over')
q('And one is worn by a woman<br><i>you would never guess.</i>', at(2, 'And one is'), nx(3) - 0.2, QC, size=70, cls='over')
q('Each one still carries<br><i>a little of her story.</i>', st(3), en(3) + 0.4, QC, size=80)
lclip([(c('h4a'), nx(4)), (c('h4b'), at(4, 'It has very'))], nx(5))
q('That kind of meaning<br><i>isn&#8217;t accidental.</i>', st(4), at(4, 'It has very') - 0.2, QL, size=84)
q('It has very little to do<br><i>with what a jewel is worth,</i>', at(4, 'It has very'), at(4, 'and everything') - 0.2, QL, size=64)
qstack(['and everything to do with', '<i>how it was chosen,</i>', '<i>how it was worn,</i>', '<i>and who it was passed to.</i>'],
       [at(4, 'and everything'), at(4, 'how it was chosen'), at(4, 'how it was worn'), at(4, 'and who it')], en(4) + 0.4, size=62, rh=140)
cfull([(c('h5a'), nx(5))], nx(6))
q('<div><i style="font-size:120px">Princess Diana&#8217;s 7 Jewels</i><br><span style="font-size:56px">Who Wears Them Now?</span></div>',
  at(5, 'seven of Princess') - 0.3, en(5) + 0.3, QC, cls='over')
cfull([(c('h6a'), nx(6)), (c('h6b'), at(6, 'A few may'))], at(6, 'And the last') - 0.1)
picfull('pengage_12.jpg', at(6, 'And the last') - 0.1, nx(7) - 0.5, pos='50% 50%')
band('The last one is <i>the jewel the whole world knows.</i>', at(6, 'And the last'), en(6) + 0.2, size=58)

# ================= 1. THE SPENCER TIARA =================
card_at('1. The Spencer Tiara', 7, nx(8) - 0.15)
cfull([(c('s8a'), nx(8))], at(8, 'It was her own') - 0.1)
pics([P_('pspencer_9', None, '50% 25%'), P_('pspencer_15', None, '50% 30%')],
     [at(8, 'It was her own') - 0.1, at(8, 'the Spencer tiara')], at(8, 'Both of her') - 0.1, h=860, y0=60)
capt('<i>St Paul&#8217;s Cathedral, 29 July 1981</i>', nx(8) + 0.4, at(8, 'It was her own') - 0.2)
capt('Her own family&#8217;s: <i>the Spencer tiara</i>', at(8, 'It was her own'), at(8, 'Both of her') - 0.2)
pic('pspencer_5.jpg', 160, 60, 640, 960, at(8, 'Both of her') - 0.1, nx(9), pos='50% 25%')
q('Both of her older sisters<br><i>wore it at their weddings.</i>', at(8, 'Both of her'), nx(9) - 0.2, (900, 60, 1860, 1020), size=64)
pic('pcelia_0.jpg', 160, 60, 640, 960, nx(9), nx(10), pos='50% 20%')
q('So where is it now?<br><i>It went home.</i>', st(9), at(9, 'And in') - 0.2, (900, 60, 1860, 1020), size=74)
q('<i>Celia McCorquodale,</i><br>her niece, 2018', at(9, 'her niece'), at(9, 'the first time') - 0.2, (900, 60, 1860, 1020), size=68)
q('The first time in twenty-one years<br><i>anyone but Diana wore it.</i>', at(9, 'the first time'), nx(10) - 0.2, (900, 60, 1860, 1020), size=56)
pframe([(c('s10a'), nx(10))], nx(11))
pwords(['A grandmother&#8217;s gold brooch.', '<i>A mother&#8217;s ring.</i>', 'And it sits in a box,', '<i>because it feels too precious.</i>'],
       [at(10, 'A grandmother'), at(10, 'A mother'), at(10, 'And it sits'), at(10, 'because it feels')], en(10) + 0.4, size=58, rh=150)
cfull([(c('s11b'), nx(11))], at(11, 'Because a classic') - 0.1)
picfull('pcelia_6.jpg', at(11, 'Because a classic') - 0.1, at(11, 'And while you') - 0.1, pos='50% 25%')
cfull([(c('s11c'), at(11, 'And while you') - 0.1)], nx(12))
q('Elegant women wear family pieces<br><i>on their own big days.</i>', at(11, 'Elegant women'), at(11, 'Not every day') - 0.2, QC, size=64, cls='over')
q('A wedding · <i>a birthday dinner</i> · a first day somewhere new', at(11, 'a wedding'), at(11, 'Because a classic') - 0.2, QC, size=56, cls='over')
q('Ask for its story.<br><i>Keep the note with the piece.</i>', at(11, 'ask the woman'), nx(12) - 0.2, QC, size=64, cls='over')
cfull([(c('s12a'), nx(12))], nx(13) - 0.4)
q('The most beautiful jewels<br><i>are the ones that remember.</i>', st(12), en(12) + 0.4, QC, size=72, cls='over')

# ================= 2. THE LOVER'S KNOT =================
card_at('2. The Lover&#8217;s Knot', 13, nx(14) - 0.15)
pic('pknot_3.jpg', 120, 200, 1000, 680, nx(14), nx(15), pos='50% 50%', zoom=1.04)
q('<i>Queen Mary&#8217;s</i><br>Lover&#8217;s Knot tiara', at(14, 'a tiara that'), at(14, 'with pearls') - 0.2, (1180, 60, 1880, 1020), size=66)
q('Pearls hanging<br><i>beneath diamond arches.</i>', at(14, 'with pearls'), nx(15) - 0.2, (1180, 60, 1880, 1020), size=64)
cfull([(c('k15a'), nx(15))], at(15, 'and those hanging') - 0.1)
pic('pknot_16.jpg', 160, 60, 640, 960, at(15, 'and those hanging') - 0.1, nx(16), pos='50% 20%')
band('It&#8217;s said to have been <i>heavy.</i>', at(15, 'But it'), at(15, 'Some say') - 0.2, size=56)
q('Some say<br><i>it gave her headaches.</i>', at(15, 'Some say'), nx(16) - 0.2, (900, 60, 1860, 1020), size=70)
pics([P_('pkateknot_12', None, '50% 20%'), P_('pkateknot_43', None, '50% 20%'), P_('pkateknot_24', None, '50% 20%')],
     [nx(16), at(16, 'And where'), at(16, 'Princess of Wales')], nx(17), h=840, y0=60)
capt('<i>Catherine, Princess of Wales · since 2015</i>', at(16, 'And where'), nx(17) - 0.2)
pframe([(c('k17a'), nx(17))], nx(18))
pwords(['An earring that pinches.', '<i>A necklace catching your hair.</i>', 'The whole evening', '<i>spent fixing it.</i>'],
       [at(17, 'an earring'), at(17, 'or a necklace'), at(17, 'and you spend'), at(17, 'fixing it')], en(17) + 0.4, size=58, rh=150)
cfull([(c('k18a'), nx(18)), (c('k18b'), at(18, 'Instead of wearing')), (c('k18c'), at(18, 'If it pinches'))], nx(19))
q('Comfortable <i>before</i> it&#8217;s admired.', at(18, 'Elegant women'), at(18, 'Because the moment') - 0.2, QC, size=72, cls='over')
q('People notice the fidgeting,<br><i>not the jewel.</i>', at(18, 'people notice'), at(18, 'Instead of wearing') - 0.2, QC, size=64, cls='over')
q('Wear it at home<br><i>for an hour before.</i>', at(18, 'try it at home'), at(18, 'If it pinches') - 0.2, QC, size=68, cls='over')
q('Soft backs,<br><i>or a lighter pair.</i>', at(18, 'change the backs'), nx(19) - 0.2, QC, size=68, cls='over')
q('<i>Elegance never looks like it hurts.</i>', st(19), en(19) + 0.4, QC, size=84)

# ================= 3. THE EMERALD HEADBAND =================
card_at('3. The Emerald Headband', 20, nx(21) - 0.15)
pics([P_('pheadband_27', None, '50% 25%'), P_('pheadband_10', None, '50% 25%')],
     [nx(21), at(21, 'Diana took')], nx(22), h=860, y0=60)
capt('<i>Melbourne, 1985</i>', nx(21) + 0.4, at(21, 'and wore it') - 0.2)
capt('A necklace, <i>worn across her forehead</i>', at(21, 'and wore it'), nx(22) - 0.2)
picfull('pheadband_4.jpg', nx(22), nx(23), pos='50% 30%')
band('A necklace, <i>worn in a way no one had seen before.</i>', at(22, 'A necklace'), en(22) + 0.3, size=56)
pics([P_('pkateemerald_4', None, '50% 20%'), P_('pkateemerald_9', None, '50% 25%')], [nx(23), at(23, 'this time')], nx(24), h=860, y0=60)
capt('<i>Boston, 2022 · this time as a necklace</i>', at(23, 'Catherine'), nx(24) - 0.2)
pframe([(c('e24a'), nx(24))], nx(25))
pwords(['Each piece, one way:', '<i>the way it came</i>', '<i>out of the box.</i>'], [st(24) + 0.2, at(24, 'the way it'), at(24, 'out of the')], en(24) + 0.4, size=60)
lrow([c('e25a'), c('e25b'), c('e25c')], [at(25, 'A long necklace'), at(25, 'A pendant'), at(25, 'A strand of')], at(25, 'Instead of buying') - 0.1,
     labels=['<i>as a bracelet</i>', '<i>at the collarbone</i>', '<i>as a choker</i>'])
q('Give one piece<br><i>a second life.</i>', at(25, 'Elegant women'), at(25, 'A long necklace') - 0.2, QC, size=80)
cfull([(c('e26a'), at(25, 'Instead of buying') - 0.1)], nx(27))
q('One piece, two ways.<br><i>Nothing new to buy.</i>', at(25, 'Instead of buying'), en(25) + 0.4, QC, size=70, cls='over')
q('Seeing what you already own<br><i>with fresh eyes.</i>', st(26), en(26) + 0.4, QC, size=70, cls='over')

# ================= GUIDE =================
picfull('pdsmile_29.jpg', nx(27), at(27, 'whether gold') - 0.1, pos='50% 30%')
cfull([(c('g27c'), at(27, 'whether gold') - 0.1), (c('g27b'), at(27, 'If you'))], nx(28) - 0.2)
q('Gold or silver?<br><i>Which colours bring your face to life?</i>', at(27, 'which colours'), at(27, 'If you') - 0.3, QC, size=60, cls='over')
q(GUIDE, at(27, 'personal stylist guide') - 0.3, nx(28) - 0.3, QC, cls='over')

# ================= 4. THE COLLINGWOOD PEARLS =================
card_at('4. The Collingwood Pearls', 28, nx(29) - 0.15)
pic('pcoll_19.jpg', 160, 60, 640, 960, nx(29), at(29, 'She wore them') - 0.1, pos='50% 30%')
pic('pcoll_29.jpg', 900, 160, 760, 760, at(29, 'a round diamond') - 0.1, at(29, 'She wore them') - 0.1, pos='50% 50%', zoom=1.04)
q('<i>a round diamond, a pearl below</i>', at(29, 'a round diamond'), at(29, 'She wore them') - 0.2, (880, 930, 1700, 1050), size=50)
pic('pspencer_20.jpg', 160, 60, 640, 960, at(29, 'She wore them') - 0.1, at(29, 'And thirteen') - 0.1, pos='50% 25%')
q('On her <i>wedding day</i>', at(29, 'She wore them'), at(29, 'And thirteen') - 0.2, (900, 60, 1860, 1020), size=72)
pic('pcoll_32.jpg', 160, 60, 600, 960, at(29, 'And thirteen') - 0.1, nx(30), pos='50% 40%')
q('Thirteen years later,<br><i>with a black evening dress</i>', at(29, 'And thirteen'), nx(30) - 0.2, (900, 60, 1860, 1020), size=64)
pics([P_('pkatecoll_16', None, '50% 25%'), P_('pkatecoll_10', None, '50% 25%')],
     [nx(30), at(30, 'and she has')], nx(31), h=860, y0=60)
capt('<i>Catherine · since 2017</i>', st(30) + 0.4, nx(31) - 0.2)
pframe([(c('c31a'), nx(31))], nx(32))
pwords(['Pearls saved', '<i>for formal occasions,</i>', 'years in a box.'], [st(31) + 0.2, at(31, 'for formal'), at(31, 'so they spend')], en(31) + 0.4, size=62)
lrow([c('c32a'), c('c32b')], [at(32, 'With a crisp'), at(32, 'With a navy')], at(32, 'Because a pearl') - 0.1, labels=['<i>one pair of pearls</i>', '<i>Saturday night</i>'])
q('One pair of pearl earrings,<br><i>both worlds.</i>', at(32, 'Elegant women'), at(32, 'With a crisp') - 0.2, QC, size=70)
cfull([(c('c32c'), at(32, 'Because a pearl') - 0.1)], at(32, 'Real, freshwater') - 0.1)
picfull('pkatecoll_0.jpg', at(32, 'Real, freshwater') - 0.1, nx(33), pos='50% 30%')
q('Soft enough for the day,<br><i>refined enough for the evening.</i>', at(32, 'Because a pearl'), at(32, 'Real, freshwater') - 0.2, QC, size=62, cls='over')
q('Real, freshwater or faux:<br><i>the most timeless choice.</i>', at(32, 'Real, freshwater'), en(32) + 0.4, QC, size=62, cls='over')
q('One classic pair, worn everywhere,<br><i>says more than a drawer full.</i>', st(33), en(33) + 0.4, QC, size=66)

# ================= 5. THE SAPPHIRES MADE NEW =================
card_at('5. The Sapphires Made New', 34, nx(35) - 0.15)
pics([P_('psapstud_2', None, '50% 30%'), P_('psapstud_8', None, '50% 30%')], [nx(35), at(35, 'Diana wore the')], nx(36), h=860, y0=60)
capt('A wedding gift, 1981 · <i>worn as simple studs</i>', at(35, 'Diana wore the'), nx(36) - 0.2)
pics([P_('pkatesap_0', None, '50% 50%'), P_('pkatesap_14', None, '50% 25%'), P_('pkatesap_18', None, '50% 50%')],
     [nx(36), at(36, 'She had them'), at(36, 'so they move')], nx(37), h=840, y0=60)
capt('<i>With Catherine · reworked into drops</i>', at(36, 'With Catherine'), nx(37) - 0.2)
pframe([(c('m37a'), nx(37))], nx(38))
pwords(['Jewellery we never wear.', 'A ring that feels <i>too heavy.</i>', 'Earrings that feel', '<i>a little dated.</i>'],
       [st(37) + 0.2, at(37, 'A ring that'), at(37, 'Gold earrings'), at(37, 'a little dated')], en(37) + 0.4, size=58, rh=150)
cfull([(c('m38a'), nx(38)), (c('m38b'), at(38, 'A good jeweller')), (c('m38c'), at(38, 'The stones stay'))], nx(39))
q('Don&#8217;t leave them in the dark.<br><i>Have them changed.</i>', at(38, 'Elegant women'), at(38, 'A good jeweller') - 0.2, QC, size=66, cls='over')
q('Studs into drops · <i>a ring into a pendant</i><br>one lonely earring <i>into a necklace</i>', at(38, 'A good jeweller'), at(38, 'The stones stay') - 0.2, QC, size=54, cls='over')
q('The stones stay. The memory stays.<br><i>Only the shape changes.</i>', at(38, 'The stones stay'), en(38) + 0.4, QC, size=60, cls='over')
q('A jewel should fit your life,<br><i>not just your jewellery box.</i>', st(39), en(39) + 0.4, QC, size=70)

# ================= 6. THE CROSS SHE BORROWED =================
card_at('6. The Cross She Borrowed', 40, nx(41) - 0.15)
pics([P_('pattallah_2', None, '50% 20%'), P_('pattallah_10', None, '50% 20%')], [nx(41), at(41, 'Diana wore')], at(41, 'It wasn') - 0.1, h=860, y0=60)
capt('<i>London, October 1987</i>', nx(41) + 0.4, at(41, 'It wasn') - 0.2)
pic('pattallah_3.jpg', 120, 140, 1000, 800, at(41, 'It wasn') - 0.1, nx(42), pos='50% 50%', zoom=1.04)
q('<i>It wasn&#8217;t hers.</i>', at(41, 'It wasn'), at(41, 'It belonged') - 0.2, (1180, 60, 1880, 1020), size=80)
q('Lent by her friend,<br><i>Naim Attallah</i>', at(41, 'It belonged'), nx(42) - 0.2, (1180, 60, 1880, 1020), size=64)
pic('pattallah_15.jpg', 200, 60, 640, 960, nx(42), nx(43), pos='50% 50%', zoom=1.04)
q('<i>Sotheby&#8217;s, London</i><br>2023', at(42, 'it was sold'), at(42, 'And the buyer') - 0.2, (960, 60, 1860, 1020), size=70)
q('The buyer:<br><i>Kim Kardashian</i>', at(42, 'And the buyer'), nx(43) - 0.2, (960, 60, 1860, 1020), size=80)
q('We often think we have to own something<br><i>to wear it.</i>', st(43) + 0.2, en(43) + 0.4, QC, size=66)
cfull([(c('b44a'), nx(44)), (c('b44b'), at(44, 'A sister')), (c('b44c'), at(44, 'Ask kindly'))], nx(45))
q('<i>Elegant women share.</i>', at(44, 'Elegant women'), at(44, 'A mother') - 0.2, QC, size=80, cls='over')
q('A mother&#8217;s pearls <i>for a daughter&#8217;s wedding</i>', at(44, 'A mother'), at(44, 'A friend') - 0.2, QC, size=58, cls='over')
q('A friend&#8217;s evening bag · <i>a sister&#8217;s brooch</i>', at(44, 'A friend'), at(44, 'Ask kindly') - 0.2, QC, size=58, cls='over')
q('Ask kindly · <i>wear it carefully</i><br>give it back <i>with a little thank-you note</i>', at(44, 'Ask kindly'), en(44) + 0.4, QC, size=56, cls='over')
q('Some of the most beautiful things we wear<br><i>are simply trusted to us.</i>', st(45), en(45) + 0.4, QC, size=62)

# ================= 7. THE SAPPHIRE RING =================
card_at('7. The Sapphire Ring', 46, nx(47) - 0.15)
picfull('pengage_5.jpg', nx(47), at(47, 'a large oval') - 0.1, pos='50% 30%')
capt('<i>February 1981 · the engagement</i>', nx(47) + 0.4, at(47, 'a large oval') - 0.2)
picfull('pengage_10.jpg', at(47, 'a large oval') - 0.1, at(47, 'Some newspapers') - 0.1, pos='50% 50%')
band('An oval sapphire, <i>fourteen diamonds</i>', at(47, 'a large oval'), at(47, 'Some newspapers') - 0.2, size=58)
cfull([(c('r47a'), at(47, 'Some newspapers') - 0.1)], nx(48))
q('&#8220;The commoner&#8217;s sapphire&#8221;', at(47, 'Some newspapers'), at(47, 'She chose it') - 0.2, QC, size=76, cls='over')
q('<i>She chose it anyway.</i>', at(47, 'She chose it'), en(47) + 0.4, QC, size=80, cls='over')
pics([P_('pwkengage_0', None, '50% 25%'), P_('pwkengage_17', None, '50% 25%'), P_('pwkengage_11', None, '50% 50%')],
     [nx(48), at(48, 'with that same'), at(48, 'He said')], nx(49), h=840, y0=60)
capt('<i>Kenya, October 2010 · the same ring</i>', at(48, 'in Kenya'), at(48, 'He said') - 0.2)
capt('&#8220;making sure his mother <i>didn&#8217;t miss out</i>&#8221;', at(48, 'He said'), nx(49) - 0.2)
pframe([(c('r49a'), nx(49))], nx(50))
pwords(['The bigger stone.', '<i>The more famous name.</i>', 'The one other people', '<i>will notice.</i>'],
       [at(49, 'The bigger'), at(49, 'The more famous'), at(49, 'The one other'), at(49, 'will notice')], en(49) + 0.4, size=60, rh=150)
cfull([(c('r50a'), nx(50)), (c('r50b'), at(50, 'Because when'))], nx(51))
q('Choose the piece you love,<br><i>and keep it close.</i>', at(50, 'Elegant women'), at(50, 'Because when') - 0.2, QC, size=66, cls='over')
q('<i>Will I still love wearing this</i><br>in thirty years?', at(50, 'will I still'), en(50) + 0.4, QC, size=66, cls='over')
cfull([(c('r51a'), nx(51))], nx(52) - 0.4)
q('Not the most expensive.<br><i>The ones that were loved.</i>', st(51), en(51) + 0.4, QC, size=70, cls='over')

# ================= CLOSE =================
lclip([(c('z52a'), nx(52)), (c('z52a2'), at(52, 'Pearls for'))], at(52, 'Seven jewels') - 0.1)
qstack(['A tiara that went home.', 'A tiara that gave her headaches.', 'A necklace worn as a headband.', 'Pearls for the biggest days.'],
       [at(52, 'A tiara that went'), at(52, 'A tiara that gave'), at(52, 'A necklace worn'), at(52, 'Pearls for')], at(52, 'Earrings made') - 0.1, size=54, rh=130)
qstack(['Earrings made new.', 'A cross that was only borrowed.', '<i>And a ring that kept a mother close.</i>'],
       [at(52, 'Earrings made'), at(52, 'A cross that'), at(52, 'And a ring')], at(52, 'Seven jewels') - 0.1, size=54, rh=130)
cfull([(c('z52b'), at(52, 'Seven jewels') - 0.1)], nx(53))
q('Seven jewels,<br><i>each one still telling her story.</i>', at(52, 'Seven jewels'), en(52) + 0.4, QC, size=66, cls='over')
cfull([(c('z53a'), nx(53))], nx(54))
q('Which one would you<br><i>wear first?</i>', st(53), en(53) + 0.3, QC, size=84, cls='over')
cfull([(c('z54b'), nx(54))], at(54, 'If it did') - 0.1)
picfull('pkatesap_5.jpg', at(54, 'If it did') - 0.1, total - 3.0, pos='50% 30%')
q(GUIDE, at(54, 'personal stylist guide') - 0.3, at(54, 'Until next time') + 0.6, QC, cls='over')
