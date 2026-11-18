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
# 7 Things Princess Diana Loved That You Can Still Buy Today (The Classy Elegance) - beat map (18 Nov 2026)
# Layouts: only those read off the channel's own videos (VISUAL-EDITING-DNA.md; videos/unforgettable-charm/VISUAL-ANALYSIS.md):
#   full clips (the whole vertical clip over its own blurred copy) | the rule's name on a white card in script |
#   a clip on the caramel with the lesson in white lines beside it, appearing as they are said | rows of clips |
#   a framed clip on cream with the EXACT WORDS in script beside it | two framed pictures under a small label (a comparison) |
#   one sentence alone on the caramel | the NAMED WOMAN shown in real archive film and real press photographs, framed on the
#   caramel with the place and year in script (the channel shows a named woman in photos and archive film: Audrey, Diana, Grace) |
#   the guide over a full clip | the CE logo.
# Sound: the voice and ONE soft solo-piano bed, steady, no ducking, NO sound effects (none are in the channel's measured files).
TRACKS_EDIT = ['gym1e.mp3']; MUSIC_DB = 13; ENDLOGO = 'logo_ce_dark.png'
MUSIC_CREDIT = 'Music: "Gymnopedie No 1" by Kevin MacLeod (incompetech.com), licensed under Creative Commons: By Attribution 4.0 (creativecommons.org/licenses/by/4.0/)'
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
# ================= HOOK (reference: full clips of women, then the title over a clip) =================
cfull([(c('h1a'), 0.0), (c('h1b'), at(1, 'The good bag')), (c('h1c'), at(1, 'The perfume')), (c('h1d'), at(1, 'The jumper'))], nx(2))
q('Have you ever saved your favourite things<br><i>for a special day that never comes?</i>', at(1, 'saved your'), at(1, 'The good bag') - 0.2, QC, size=64, cls='over')
picfull('pbalmoral_0.jpg', nx(2), at(2, 'she wore'))
picfull('psheep_37.jpg', at(2, 'she wore'), at(2, 'On ordinary days'))
picfull('pladydior_0.jpg', at(2, 'On ordinary days'), nx(3))
band('<i>Princess Diana didn&#8217;t.</i>', at(2, 'Princess Diana'), at(2, 'The things she') - 0.1, size=90)
pics([P_('pbalmoral_2'), P_('psheep_1'), P_('pgucci_5')], [nx(3), at(3, 'decades later'), at(3, 'still look right')], nx(4), h=860, y0=70)
creambg_ = None
lclip([(c('h4a'), nx(4))], at(4, 'and everything') - 0.1)
q('That kind of style<br><i>isn&#8217;t accidental.</i>', st(4), at(4, 'It has very') - 0.2, QL, size=84)
q('It has very little to do<br><i>with how much she spent,</i>', at(4, 'It has very'), at(4, 'and everything') - 0.2, QL, size=64)
q('and everything to do with<br><i>how she chose,</i><br>and how often she used<br><i>what she loved.</i>', at(4, 'and everything'), en(4) + 0.4, QC, size=70)
cfull([(c('h5a'), nx(5))], nx(6))
q('<div><span style="font-size:52px">7 Things</span><br><i style="font-size:120px">Princess Diana Loved</i><br><span style="font-size:46px">that you can still buy today</span></div>',
  at(5, 'seven things') - 0.3, at(5, 'the true story') - 0.1, QC, cls='over')
cfull([(c('h6a'), nx(6)), (c('h6b'), at(6, 'One or two')), (c('h6c'), at(6, 'And the last'))], nx(7) - 0.5)
q('The last one is<br><i>the most personal of all.</i>', at(6, 'And the last'), en(6) + 0.2, QC, size=72, cls='over')

# ================= 1. HER GREEN WELLIES =================
card_at('1. Her Green Wellies', 7, nx(8) - 0.15)
pics([P_('pbalmoral_6', None, '50% 40%'), P_('pbalmoral_0', None, '50% 40%'), P_('pbalmoral_47', None, '50% 40%')],
     [nx(8), at(8, 'She was nineteen'), at(8, 'She wore green')], at(8, 'and a pair') - 0.1, h=840, y0=60)
capt('<i>Balmoral, May 1981</i>', nx(8) + 0.4, at(8, 'She was nineteen') - 0.2)
capt('She was <i>nineteen.</i>', at(8, 'She was nineteen'), at(8, 'And she') - 0.2)
capt('green corduroy trousers · <i>a knitted jumper</i>', at(8, 'She wore green'), at(8, 'and a pair') - 0.2, size=52)
pic('pbalmoral_9.jpg', 160, 60, 470, 960, at(8, 'and a pair') - 0.1, nx(9), pos='50% 60%')
prod('ph_hunterboot.png', 1240, 900, 760, at(8, 'green Hunter'), nx(9), label='<i>green Hunter wellies</i>', maxw=700)
q('The fashionable version<br><i>of something practical</i>', st(9) + 0.3, at(9, 'and it never') - 0.2, QC, size=76)
q('never quite feels right<br><i>outdoors.</i>', at(9, 'and it never'), en(9) + 0.4, QC, size=76)
cfull([(c('w10a'), nx(10)), (c('w10b'), at(10, 'Because a classic'))], at(10, 'And those same') - 0.1)
q('Plain, sturdy,<br><i>made for real weather.</i>', at(10, 'Plain, sturdy'), at(10, 'Because a classic') - 0.2, QC, size=76, cls='over')
q('You look <i>relaxed</i>,<br>instead of careful.', at(10, 'so you look'), at(10, 'And those same') - 0.2, QC, size=76, cls='over')
prod('ph_hunterboot.png', W // 2, 900, 760, at(10, 'And those same') - 0.1, nx(11), label='<i>still made today</i>', maxw=760)
lrow([c('w11a'), c('w11b')], [nx(11), at(11, 'Keep the rest')], nx(12), labels=['green, navy or black', None])
qstack(['Keep the rest quiet:', '<i>dark trousers,</i>', '<i>a soft knit,</i>', '<i>a warm coat.</i>'], [at(11, 'Keep the rest'), at(11, 'dark trousers'), at(11, 'a soft knit'), at(11, 'a warm coat')], nx(12) - 0.1, box_=(2 * PW + 40, 60, 1890, 1020), size=60, rh=140)
cfull([(c('w12a'), nx(12))], nx(13) - 0.4)
q('Elegance is knowing what the day needs,<br><i>and dressing for it with calm confidence.</i>', at(12, "It's knowing"), en(12) + 0.4, QC, size=62, cls='over')

# ================= 2. THE BLACK SHEEP JUMPER =================
card_at('2. The Black Sheep Jumper', 13, nx(14) - 0.15)
pics([P_('psheep_0', None, '50% 30%'), P_('psheep_41', None, '50% 40%')], [nx(14), at(14, 'knitted with rows')], nx(15), h=820, y0=60)
capt('<i>Polo, June 1981</i>', nx(14) + 0.4, at(14, 'knitted with rows') - 0.2)
capt('rows of white sheep, <i>and one black sheep</i>', at(14, 'knitted with rows'), nx(15) - 0.2)
lclip([(c('s15a'), nx(15)), (c('s15b'), at(15, 'who sold'))], nx(16))
q('Warm and Wonderful', at(15, 'It came from'), at(15, 'started by') - 0.2, QL, size=86)
q('Sally Muir<br>and Joanna Osborne<br><i>a market stall in Covent Garden</i>', at(15, 'started by'), nx(16) - 0.2, QL, size=60)
pic('psheep_43.jpg', 150, 50, 816, 990, nx(16), at(16, 'So they knitted') - 0.1, pos='50% 40%')
q('&#8220;how much<br><i>she loved it&#8221;</i>', at(16, 'saying how much'), at(16, 'Sally Muir') - 0.2, (1050, 60, 1880, 1020), size=80)
q('Sally Muir imagined<br><i>the engagement ring</i><br>had caught in the threads.', at(16, 'Sally Muir'), at(16, 'So they knitted') - 0.2, (1050, 60, 1880, 1020), size=58)
pics([P_('psheep_1'), P_('psheep_16')], [at(16, 'So they knitted') - 0.1, at(16, 'a new one')], nx(17), h=860, y0=60)
capt('<i>The new one, 1983</i>', at(16, 'a new one'), nx(17) - 0.2)
pics([P_('psheep_28'), P_('psheep_33')], [nx(17), at(17, 'more than a million')], at(17, 'And the same') - 0.1, h=700, y0=110)
capt("<i>Sotheby&#8217;s, New York, 2023</i>", nx(17) + 0.3, at(17, 'more than a million') - 0.2)
capt('more than <i>a million dollars</i>', at(17, 'more than a million'), at(17, 'And the same') - 0.2)
lclip([(c('s17a'), at(17, 'And the same') - 0.1)], nx(18))
q('The same design<br><i>is still knitted today.</i>', at(17, 'And the same'), en(17) + 0.4, QL, size=74)
pframe([(c('s18a'), nx(18))], nx(19))
pwords(['A piece that makes you smile', '<i>stays in the drawer</i>', 'because it doesn&#8217;t feel', '<i>serious enough.</i>'],
       [st(18) + 0.3, at(18, 'but it stays'), at(18, 'because it'), at(18, 'serious enough')], en(18) + 0.4, size=56, rh=150)
lrow([c('s19a'), c('s19b')], [nx(19), at(19, 'Just one')], at(19, 'Because when') - 0.1)
q('One playful piece.<br><i>Just one.</i>', nx(19) + 0.3, at(19, 'Because when') - 0.2, R3, size=70)
pic('psheep_35.jpg', 160, 50, 560, 990, at(19, 'Because when') - 0.1, nx(20), pos='50% 30%')
qstack(['When the rest is quiet,', '<i>it looks intentional.</i>'], [at(19, 'Because when'), at(19, 'the playful piece')], at(19, 'Try it') - 0.1, box_=(800, 60, 1880, 1020), size=66)
qstack(['a red jumper', '<i>navy trousers</i>', 'a white collar', '<i>simple flat shoes</i>'],
       [at(19, 'a red jumper'), at(19, 'with navy'), at(19, 'a white collar'), at(19, 'simple flat')], nx(20) - 0.1, box_=(800, 60, 1880, 1020), size=64, rh=150)
cfull([(c('s20a'), nx(20))], nx(21) - 0.4)
q('Elegance doesn&#8217;t ask you to stop having fun.<br><i>It simply chooses where the fun goes.</i>', st(20), en(20) + 0.4, QC, size=60, cls='over')

# ================= 3. SOFT BROWN, NOT BLUE =================
card_at('3. Soft Brown, Not Blue', 21, nx(22) - 0.15)
pics([P_('pblueliner_0', None, '50% 35%'), P_('pblueliner_3', None, '50% 35%')], [nx(22), at(22, 'bright blue eyeliner')], at(22, 'Then, in') - 0.1, h=860, y0=60)
capt('bright <i>blue eyeliner</i>', at(22, 'bright blue eyeliner'), at(22, 'Then, in') - 0.2)
pic('pvogue_1.jpg', 170, 50, 720, 990, at(22, 'Then, in') - 0.1, nx(23), pos='50% 40%')
q('<i>British Vogue, 1991</i><br>make-up artist<br>Mary Greenwell', at(22, 'British Vogue'), nx(23) - 0.2, (960, 60, 1880, 1020), size=66)
q('&#8220;Blue eyes should never wear<br><i>blue pencil or shadow.&#8221;</i>', at(23, 'Blue eyes'), at(23, 'Beiges and browns') - 0.2, QC, size=70)
q('&#8220;Beiges and browns are<br><i>just so much prettier.&#8221;</i>', at(23, 'Beiges and browns'), at(23, 'And Diana loved') - 0.2, QC, size=70)
q('And Diana<br><i>loved the change.</i>', at(23, 'And Diana loved'), en(23) + 0.3, QC, size=84)
pic('pvogue_12.jpg', 160, 60, 880, 990, nx(24), nx(25), pos='50% 35%')
q('What she kept:<br><i>loads of mascara.</i>', st(24) + 0.3, en(24) + 0.4, (1110, 60, 1880, 1020), size=70)
pframe([(c('e25a'), nx(25))], nx(26))
pwords(['Most of us match', '<i>our make-up to our eyes,</i>', 'or keep it the way', '<i>we did at twenty.</i>'],
       [st(25) + 0.3, at(25, 'make-up to our'), at(25, 'or keep'), at(25, 'at twenty')], en(25) + 0.4, size=58, rh=150)
lclip([(c('e26a'), nx(26)), (c('e26a2'), at(26, 'take a soft')), (c('e26b'), at(26, 'Smudge it')), (c('e26c'), at(26, 'Then let one')), (c('e26d'), at(26, 'Because a liner'))], nx(27))
qstack(['Instead of a bright liner,', '<i>a soft brown or taupe pencil</i>'], [at(26, 'Instead of'), at(26, 'take a soft')], at(26, 'Smudge it') - 0.2, size=60)
qstack(['Smudge it close', '<i>to your upper lashes</i>'], [at(26, 'Smudge it'), at(26, 'to your upper')], at(26, 'Then let one') - 0.2, size=66)
qstack(['One good coat', '<i>of mascara</i>'], [at(26, 'Then let one'), at(26, 'of mascara')], at(26, 'Because a liner') - 0.2, size=74)
q('A soft brown makes your eyes<br><i>look clearer and brighter.</i>', at(26, 'while a soft'), en(26) + 0.4, QL, size=60)
cfull([(c('e27a'), nx(27))], nx(28) - 0.2)
q('Sometimes the most elegant change<br><i>is simply taking one thing away.</i>', st(27), en(27) + 0.4, QC, size=64, cls='over')

# ================= THE GUIDE (reference: after point 3, over full clips) =================
lrow([c('g28a'), c('g28b')], [nx(28), at(28, 'their best colours')], at(28, 'If you') - 0.1)
qstack(['their best colours,', '<i>the shapes that flatter them,</i>', '<i>the hairstyles that suit their face</i>'], [at(28, 'their best colours'), at(28, 'the shapes'), at(28, 'the hairstyles')], at(28, 'If you') - 0.2, box_=(2 * PW + 40, 60, 1890, 1020), size=52, rh=150)
q('The right colours<br><i>change everything.</i>', at(28, 'The right colours'), at(28, 'Many elegant') - 0.2, (2 * PW + 40, 60, 1890, 1020), size=66)
cfull([(c('g28d'), at(28, 'If you') - 0.1)], nx(29) - 0.4)
q(GUIDE, at(28, 'our personal stylist') - 0.3, en(28) + 0.2, QC, cls='over')

# ================= 4. ONE SHOE, THREE COLOURS =================
card_at('4. One Shoe, Three Colours', 29, nx(30) - 0.15)
pics([P_('ptods_4', None, '50% 50%'), P_('ptods_2', None, '50% 50%')], [nx(30), at(30, 'Italian driving')], at(30, 'with little rubber') - 0.1, h=880, y0=60)
capt('<i>soft Italian driving loafers</i>', at(30, 'Italian driving'), at(30, 'with little rubber') - 0.2)
pic('pgommino_7.jpg', 260, 90, 1400, 900, at(30, 'with little rubber') - 0.1, at(30, 'And she') - 0.1, pos='50% 50%', zoom=1.05)
capt('<i>little rubber pebbles on the sole</i>', at(30, 'little rubber'), at(30, 'And she') - 0.2)
pieces([('ph_gombeige.png', '<i>beige suede</i>'), ('ph_gomblue.png', '<i>light blue suede</i>'), ('ph_gomtan.png', '<i>tan leather</i>')],
       [at(30, 'beige suede'), at(30, 'light blue suede'), at(30, 'tan leather')], nx(31), x0=80, x1=1840, ybot=780, hh=520)
q('<i>They&#8217;re still made today.</i>', at(30, "They're still"), nx(31) - 0.2, (180, 870, 1740, 1010), size=60)
pframe([(c('l31a'), nx(31))], nx(32))
pwords(['The endless search', '<i>for the perfect pair.</i>', 'Buying, returning,', '<i>buying again.</i>'],
       [st(31) + 0.3, at(31, 'for the perfect'), at(31, 'Buying'), at(31, 'buying again')], en(31) + 0.4, size=62, rh=150)
cfull([(c('l32a'), nx(32)), (c('l32b'), at(32, 'That isn')), (c('l32c'), at(32, 'And every'))], nx(33))
q('When it works,<br><i>get it in a second colour.</i>', at(32, 'they simply get'), at(32, 'That isn') - 0.2, QC, size=74, cls='over')
q('That isn&#8217;t boring.<br><i>That&#8217;s knowing yourself.</i>', at(32, 'That isn'), at(32, 'And every') - 0.2, QC, size=76, cls='over')
lrow([c('l33a'), c('l33b'), c('l33c')], [at(33, 'jeans'), at(33, 'a skirt'), at(33, 'tailored trousers')], nx(34), labels=['jeans', 'a skirt', 'tailored trousers'])
q('A soft flat loafer<br><i>in beige, navy or tan</i>', at(33, 'Choose a soft'), at(33, 'jeans') - 0.2, QC, size=70)
cfull([(c('l34a'), nx(34))], nx(35) - 0.4)
q('Fewer decisions, <i>more ease.</i>', st(34), at(34, 'And that ease') - 0.2, QC, size=80, cls='over')
q('That ease shows in the way you walk,<br><i>with quiet confidence.</i>', at(34, 'And that ease'), en(34) + 0.4, QC, size=62, cls='over')

# ================= 5. THE EVERYDAY TOTE =================
card_at('5. The Everyday Tote', 35, nx(36) - 0.15)
pics([P_('pgucci_7', None, '50% 40%'), P_('pgucci_4', None, '50% 40%'), P_('pgucci_9', None, '50% 40%')],
     [nx(36), at(36, 'two curved bamboo'), at(36, 'all around London')], at(36, 'Gucci had') - 0.1, h=860, y0=60)
capt('<i>London, the early nineties</i>', nx(36) + 0.4, at(36, 'Gucci had') - 0.2)
prod('ph_guccitote.png', 640, 900, 760, at(36, 'Gucci had') - 0.1, nx(37), maxw=780)
q('Introduced in <i>1991</i>', at(36, 'Gucci had'), at(36, 'And thirty') - 0.2, (1130, 60, 1880, 1020), size=66)
q('Thirty years later,<br>Gucci renamed it<br><i>the Diana.</i>', at(36, 'And thirty'), nx(37) - 0.2, (1130, 60, 1880, 1020), size=70)
pframe([(c('t37a'), nx(37))], nx(38))
pwords(['A bag for every outfit,', '<i>and still nothing</i>', '<i>quite works.</i>'], [st(37) + 0.3, at(37, 'and still feel'), at(37, 'quite works')], en(37) + 0.4, size=62)
cfull([(c('t38a'), nx(38)), (c('t38b'), at(38, 'A classic shape')), (c('t38c'), at(38, 'Because a calm')), (c('t38e'), at(38, 'It works with'))], at(38, 'Look for') - 0.1)
q('One good everyday bag.', at(38, 'one good everyday'), at(38, 'A classic shape') - 0.7, QC, size=84, cls='over')
q('A classic shape · <i>a warm neutral</i><br>no big logo · <i>big enough for real life</i>', at(38, 'A classic shape') + 0.1, at(38, 'Because a calm') - 0.2, QC, size=56, cls='over')
q('It works with <i>jeans in the morning</i><br>and <i>a dress in the evening.</i>', at(38, 'It works with'), at(38, 'Look for') - 0.2, QC, size=62, cls='over')
lrow([c('t38d')], [at(38, 'Look for')], nx(39))
q('A structured tote<br><i>in tan, black or cream.</i><br>At any price.', at(38, 'Look for'), nx(39) - 0.2, QL, size=66)
cfull([(c('t39a'), nx(39))], nx(40) - 0.4)
q('When your bag never needs a second thought,<br><i>you&#8217;re free to think about everything else.</i>', st(39), en(39) + 0.4, QC, size=56, cls='over')

# ================= 6. THE BAG SHE DIDN'T SAVE =================
card_at('6. The Bag She Didn&#8217;t Save', 40, nx(41) - 0.15)
pic('pchirac_26.jpg', 90, 140, 1300, 715, nx(41), at(41, 'A small, structured') - 0.1, pos='50% 40%', zoom=1.05)
capt('<i>Paris, 1995 · with Bernadette Chirac</i>', at(41, 'Bernadette'), at(41, 'A small, structured') - 0.2)
prod('ph_ladydior.png', 700, 880, 700, at(41, 'A small, structured') - 0.1, nx(42), maxw=640)
q('A small, structured bag<br><i>with a top handle</i>', at(41, 'A small, structured'), at(41, 'Its nickname') - 0.2, (1180, 60, 1880, 1020), size=58)
q('<i>Chouchou</i><br>&#8220;favourite&#8221;', at(41, 'Its nickname'), nx(42) - 0.2, (1180, 60, 1880, 1020), size=90)
pics([P_('pladydior_4', None, '50% 40%'), P_('pladydior_14', None, '50% 40%'), P_('pladydior_2', None, '50% 40%')],
     [nx(42), at(42, 'Within two months'), at(42, 'she was carrying')], at(42, 'In 1996') - 0.1, h=860, y0=60)
capt('She didn&#8217;t put it away <i>for special occasions.</i>', st(42) + 0.3, at(42, 'In 1996') - 0.2, size=54)
pic('pladydior_6.jpg', 200, 40, 490, 1000, at(42, 'In 1996') - 0.1, nx(43), pos='50% 30%')
q('<i>The Met Gala,</i><br>New York, 1996', at(42, 'In 1996'), at(42, 'And that same') - 0.2, (800, 60, 1880, 1020), size=72)
q('Dior renamed it<br><i>the Lady Dior.</i>', at(42, 'And that same'), at(42, "It's still made") - 0.2, (800, 60, 1880, 1020), size=78)
q('<i>Still made today.</i>', at(42, "It's still made"), en(42) + 0.4, (800, 60, 1880, 1020), size=70)
pframe([(c('b43a'), nx(43))], nx(44))
pwords(['The good bag stays', '<i>in its dust bag.</i>', 'The silk scarf stays', '<i>in the drawer.</i>'],
       [at(43, 'The good bag'), at(43, 'in its dust'), at(43, 'The silk scarf'), at(43, 'in the drawer')], en(43) + 0.4, size=60, rh=150)
cfull([(c('b44a'), nx(44)), (c('b44b'), at(44, 'Because when'))], at(44, 'So start') - 0.1)
q('Elegant women use what they love.<br><i>Not carelessly, but often.</i>', at(44, 'Elegant women'), at(44, 'Because when') - 0.2, QC, size=64, cls='over')
q('You carry yourself differently.<br><i>You feel more polished, and it shows.</i>', at(44, 'you carry yourself'), at(44, 'So start') - 0.2, QC, size=60, cls='over')
lrow([c('b44c'), c('b44d'), c('b44e')], [at(44, 'Your nicest bag'), at(44, 'Your good scarf'), at(44, 'Even a pretty')], nx(45),
     labels=['<i>on a Tuesday</i>', '<i>to the grocery store</i>', '<i>out of the wardrobe</i>'])
cfull([(c('b45a'), nx(45))], nx(46) - 0.4)
q('The special day you&#8217;re saving them for<br><i>is usually today.</i>', st(45), en(45) + 0.4, QC, size=66, cls='over')

# ================= 7. HER PERFUME =================
card_at('7. Her Perfume', 46, nx(47) - 0.15)
pic('pvogue_12.jpg' if False else 'pblueliner_2.jpg', 170, 60, 760, 960, nx(47), nx(48), pos='50% 35%')
q('&#8220;She always, always, always<br><i>wore fragrance.&#8221;</i>', at(47, 'always, always'), en(47) + 0.4, (1000, 60, 1880, 1020), size=64)
cfull([(c('p48a'), nx(48)), (c('p48c'), at(48, 'according to')), (c('p48b'), at(48, 'Diana was dabbing'))], at(48, 'and spilled') - 0.1)
when('29 July 1981', nx(48) + 0.4, at(48, 'according to') - 0.2)
capt('according to her make-up artist that day, <i>Barbara Daly</i>', at(48, 'according to'), at(48, 'Diana was dabbing') - 0.2, size=48)
prod('ph_quelques.png', 1460, 880, 640, at(48, 'Quelques Fleurs'), at(48, 'and spilled') - 0.1, label='<i>Quelques Fleurs</i>', maxw=420)
pics([P_('pwedding_35', None, '50% 40%'), P_('pwedding_18', None, '50% 50%'), P_('pwedding_33', None, '50% 40%')],
     [at(48, 'and spilled') - 0.1, at(48, 'down the front'), at(48, 'So she simply')], at(48, 'And the world') - 0.1, h=860, y0=60)
picfull('pwedding_46.jpg', at(48, 'And the world') - 0.1, nx(49))
band('<i>And the world never noticed.</i>', at(48, 'And the world'), en(48) + 0.4, size=78)
prod('ph_firstbottle.png', 560, 900, 780, nx(49), nx(50), maxw=640)
q('&#8220;a bottle of<br><i>Mummy&#8217;s favourite perfume&#8221;</i>', at(49, 'In his memoir'), at(49, 'It was First') - 0.2, (1000, 60, 1880, 1020), size=64)
q('<i>First</i><br>Van Cleef &amp; Arpels', at(49, 'It was First'), at(49, "And it's still") - 0.2, (1000, 60, 1880, 1020), size=86)
q('<i>Still sold today.</i>', at(49, "And it's still"), en(49) + 0.4, (1000, 60, 1880, 1020), size=72)
pframe([(c('p50a'), nx(50))], nx(51))
pwords(['Scent is the most personal thing', '<i>a woman wears.</i>', 'No one can photograph it.', '<i>But it&#8217;s what the people</i>', '<i>who love you remember.</i>'],
       [st(50) + 0.3, at(50, 'a woman wears'), at(50, 'No one can'), at(50, "But it's what"), at(50, 'who love you')], en(50) + 0.4, size=54, rh=140)
cfull([(c('p51a'), nx(51)), (c('p51b'), at(51, 'Keep it on'))], at(51, 'Wear it on') - 0.1)
q('Choose one you truly love.<br><i>Not the newest, not the most expensive.</i>', at(51, 'So choose'), at(51, 'Keep it on') - 0.2, QC, size=60, cls='over')
q('Keep it on your dresser,<br><i>not in a drawer.</i>', at(51, 'Keep it on'), at(51, 'Wear it on') - 0.2, QC, size=70, cls='over')
lclip([(c('p51d'), at(51, 'Wear it on') - 0.1)], at(51, 'Let it quietly') + 1.6)
qstack(['Wear it on ordinary days:', '<i>on a walk,</i>', '<i>at your desk,</i>', '<i>at the school gate.</i>'], [at(51, 'Wear it on'), at(51, 'on a walk'), at(51, 'at your desk'), at(51, 'at the school')], at(51, 'Let it quietly') + 1.5, size=62, rh=140)
cfull([(c('p52a'), at(51, 'Let it quietly') + 1.5)], nx(53) - 0.4)
q('The things you love, worn often,<br><i>become the way people remember you.</i>', st(52), en(52) + 0.4, QC, size=62, cls='over')

# ================= CLOSE =================
pics([P_('pbalmoral_36'), P_('psheep_1'), P_('pvogue_12')], [at(53, 'Green wellies'), at(53, 'A playful'), at(53, 'Soft brown')], at(53, 'One shoe') - 0.1, h=880, y0=60)
pieces([('ph_gomblue.png', None), ('ph_guccitote.png', None), ('ph_ladydior.png', None), ('ph_firstbottle.png', None)],
       [at(53, 'One shoe'), at(53, 'An everyday'), at(53, 'The bag she'), at(53, 'And her perfume')], at(53, 'Seven things') - 0.1, x0=60, x1=1860, ybot=900, hh=640)
cfull([(c('c53a'), at(53, 'Seven things') - 0.1)], nx(54))
q('Most of the feeling behind them<br><i>costs nothing at all.</i>', at(53, 'and most of'), en(53) + 0.4, QC, size=66, cls='over')
cfull([(c('c54a'), nx(54))], nx(55))
q('Which one would you<br><i>choose first?</i>', st(54), en(54) + 0.3, QC, size=84, cls='over')
cfull([(c('c55a'), nx(55)), (c('c55b'), at(55, 'And for your'))], total - 3.0)
q(GUIDE, at(55, 'personal stylist guide') - 0.3, at(55, 'Until next time') + 0.6, QC, cls='over')
