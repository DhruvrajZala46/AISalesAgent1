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


# 10 Easy, Elegant 2-Minute Hairstyles (Classy Academy) - beat map (12 Nov 2026)
# Layout of the channel's own hairstyles video ("The Most Elegant & Easy Hairstyles", A-JRkjQs2XI): its replay peaks are the
# vertical tutorial clips on the caramel backdrop, so every step is a whole vertical clip at the left with the step written
# beside it; white script cards per style; full screen only for the hook, the guide and the ending. Every clip checked by eye.
TRACKS_EDIT = ['m659.mp3']; MUSIC_DB = 13; ENDLOGO = 'logo_ca_dark.png'
MUSIC_CREDIT = 'Music: "Romantic" by Francisco Alvear (Mixkit, free license)'
MID = (PW + 1880) // 2
RT = (PW + 40, 30, 1880, 230)
for k in ('s1b15', 's1a6', 'hv_twist12', 'hv_twist4', 's1a1', 'c_leave16', 's2d7', 's2b23', 's2a25', 's3b22', 's3b18', 's3b13', 'sv4a19', 'hv_chignon38',
          's5a3', 't6b37', 't6a45', 's3b16', 's7a7', 'sv8b11', 's10b28', 's10a24', 's10b13', 'hv_long1', 'hv_long22', 's1a5', 'cv_grocery2', 'hv_long2',
          'hv_chignon18', 's9a14', 'cv_ease1', 'hv_long0', 's9a10'): MAXSLOW[k] = 2.0
for k in ('s5a6', 'tpancake9', 'hv_twist13', 's1c5', 'gv_mirror11', 'cv_grocery3', 's7b2'): MAXSLOW[k] = 1.8
for k in ('s2a10', 's3a7', 's7a7', 'cv_dinner41', 's9b28', 'sv4a36'): MAXSLOW[k] = 2.0
CROP['s1a1'] = (107, 0, 900); CROP['s1b26'] = (79, 260, 1000); CROP['s2a25'] = (79, 50, 1000); CROP['s2d12'] = (70, 120, 900); CROP['s3b13'] = (60, 0, 970)
CROP['s3b22'] = (95, 340, 940); CROP['sv4a19'] = (42, 0, 1130); CROP['s5a6'] = (36, 0, 1150); FLIP.add('s5a6'); CROP['s5a3'] = (0, 0, 900)
CROP['s7b2'] = (90, 300, 960); CROP['s9a10'] = (126, 24, 830); CROP['s9b28'] = (124, 0, 840); CROP['s10b28'] = (112, 0, 880)
CROP['s10a24'] = (150, 0, 780); CROP['s10b20'] = (107, 0, 900); CROP['s1c5'] = (118, 0, 860); CROP['hv_chignon18'] = (36, 0, 1150)
def qstack(lines, times, t1, box_=QL, size=58, rh=150):
    """the step lines one under the other beside a clip, each appearing as it is said"""
    x0, y0, x1, y1 = box_; n = len(lines); top = (y0 + y1) // 2 - n * rh // 2
    for k, (txt, tt) in enumerate(zip(lines, times)):
        q(txt, tt, t1, (x0, top + k * rh, x1, top + (k + 1) * rh), size=size, dur=1.0)
def card_from(txt, t0, t_out, size=110):
    white(t0, t_out); text(txt, 'card', t0 + 0.3, t_out - 0.1, dur=1.2, out=0.45, style=f'font-size:{size}px;')
GUIDE = '<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>'
LOW = (180, 740, 1740, 1040)

# ================= HOOK =================
cfull([(K('hv_mid6', 0.3, 5.2), 0.0)], nx(2))
q('You might think elegant hair takes<br><i>an hour and a salon.</i>', 0.3, en(1) + 0.2, LOW, size=66, cls='over')
cfull([(K('cv_ease1', 5.6, 9.4), nx(2))], nx(3))
q('What if you never needed more than<br><i>two minutes?</i>', nx(2) + 0.1, en(2) + 0.3, LOW, size=66, cls='over')
lrow([K('hv_twist13', 16.4, 21.3), K('cv_dinner13', 25.0, 30.2), K('s9a14', 12.0, 14.5)], [nx(3), at(3, 'ten easy'), at(3, 'you can do')], nx(4))
q('<div><span style="font-size:60px">10 Easy, Elegant</span><br><i style="font-size:150px">2-Minute Hairstyles</i></div>',
  at(3, 'ten easy') - 0.1, en(3) + 0.3, QC, cls='over')
lclip([(K('s1a5', 1.8, 6.5), nx(4))], nx(5))
q('No heat. <i>No special skill.</i>', nx(4) + 0.2, nx(5) - 0.1, RT, size=60)
pieces([('ph_elastic.jpg', 'an elastic'), ('ph_bobby.png', 'a few pins'), ('ph_clawblk.png', 'a simple clip')],
       [at(4, 'an elastic'), at(4, 'a few pins'), at(4, 'one or two')], nx(5) - 0.1, hh=380, ybot=820)
lclip([(K('sv8a4', 5.0, 13.6), nx(5))], nx(6))
qstack(['It&#8217;s not about money.', 'It&#8217;s not about <i>perfect hair.</i>', '<i>Any age.</i> Any budget.'],
       [nx(5) + 0.2, at(5, "and it's not"), at(5, 'These work')], nx(6) - 0.1, size=62)
lrow([K('hv_long0', 0.3, 3.9), K('hv_mid10', 3.0, 7.0), K('s1c5', 11.6, 15.6)], [nx(6), at(6, 'shorter'), at(6, 'and fine')], nx(7),
     labels=['long hair', 'shorter hair', 'fine hair'])
cfull([(K('s10b30', 4.8, 9.2), nx(7))], nx(8))
q('One of them takes<br><i>a little practice.</i>', nx(7) + 0.2, en(7) + 0.3, LOW, size=66, cls='over')
lclip([(K('c_leave16', 0.4, 4.2), nx(8)), (K('c_leave16', 16.4, 21.0), at(8, 'So they'))], en(9) + 0.3)
q('Most hold best on hair that<br><i>isn&#8217;t freshly washed.</i>', at(8, 'Most of these') - 0.1, at(8, 'So they') - 0.2, QL, size=62)
q('Perfect for <i>day two.</i>', at(8, 'So they'), en(8) + 0.4, QL, size=72)
q('So, let&#8217;s <i>get started.</i>', nx(9) + 0.1, en(9) + 0.2, QL, size=72)

# ================= 1. THE FRENCH TWIST =================
card_at('1. The French Twist', 10, en(10) + 0.3, size=110)
lclip([(K('hv_twist4', 8.6, 12.5), nx(11)), (K('s1a1', 0.4, 2.4), at(11, 'so your neck') + 0.3)], nx(12))
q('Everything is lifted<br><i>away from your face.</i>', at(11, 'Everything') - 0.1, at(11, 'so your neck') - 0.2, QL, size=62)
q('Your neck and your earrings<br><i>are what people see.</i>', at(11, 'so your neck'), en(11) + 0.3, QL, size=62)
lclip([(K('s1b26', 3.0, 12.6), nx(12))], nx(13))
q('The classic version:<br><i>pins and patience</i>', nx(12) + 0.2, at(12, 'This one') - 0.2, RT, size=52)
q('This one: <i>a single claw clip</i>', at(12, 'This one'), nx(13) - 0.1, RT, size=56)
item('ph_claw.png', MID, 880, 520, at(12, 'a single claw') + 0.2, nx(13) - 0.1, label='tortoiseshell or black', maxw=640, lsize=50)
T1 = nx(13) + 3.4
lclip([(K('s1b15', 0.3, 2.4), nx(13)), (K('s1a6', 1.0, 4.0), T1)], nx(14))
T2 = nx(14) + 4.1
lclip([(K('s1b15', 2.4, 4.7), nx(14)), (K('s1a6', 4.0, 5.65), T2)], nx(15))
lclip([(K('s1b15', 4.7, 6.1), nx(15)), (K('s1a6', 5.65, 7.0), nx(15) + 2.3), (K('hv_twist12', 10.9, 12.3), nx(15) + 4.8)], nx(16))
lclip([(K('s1b15', 6.1, 8.5), nx(16)), (K('s1a6', 7.0, 9.2), nx(16) + 2.9)], nx(17))
qstack(['<i>Gather</i> at the nape', '<i>Twist</i> upward', 'Tuck the ends, or let them fall', '<i>Clip</i> beneath the twist'],
       [nx(13) + 0.3, nx(14) + 0.3, nx(15) + 0.3, nx(16) + 0.3], nx(17) - 0.1, size=60, rh=170)
lrow([K('s1c4', 5.0, 14.4), K('s1a24', 1.6, 10.6)], [nx(17), at(17, 'And for thick')], nx(18),
     labels=['fine hair: one finger', 'thick or wavy: a larger clip'])
lclip([(K('s1b15', 8.5, 9.9), nx(18)), (K('s1a5', 6.7, 9.1), nx(18) + 2.3), (K('cv_grocery2', 0.3, 3.0), at(18, 'or just'))], nx(19))
q('Polished.<br><i>Effortlessly elegant.</i>', at(18, 'polished') - 0.2, at(18, 'whether') - 0.1, QL, size=70)
q('For dinner, or just<br><i>the grocery store.</i>', at(18, 'whether'), en(18) + 0.3, QL, size=64)

# ================= 2. THE WRAPPED LOW PONYTAIL =================
card_at('2. The Wrapped Low Ponytail', 19, en(19) + 0.3, size=100)
lrow([K('s2a16', 3.2, 9.0), K('s2a10', 15.3, 19.0)], [nx(20), at(20, 'or it can')], nx(21), labels=['the elastic showing', 'one small strand'])
lclip([(K('s2d7', 5.6, 10.2), nx(21))], nx(22))
qstack(['Brush back,<br><i>toward the ponytail</i>', 'Secure it low,<br><i>at the nape</i>'], [nx(21) + 0.3, at(21, 'and secure')], nx(22) - 0.1, size=60, rh=260)
lclip([(K('s2b23', 1.3, 8.8), nx(22)), (K('s2a25', 6.2, 9.5), at(22, 'and pin'))], nx(23))
qstack(['Take <i>one small strand</i>', 'Wrap it around the elastic', '<i>Pin the end</i> underneath'],
       [nx(22) + 0.3, at(22, 'wrap it'), at(22, 'and pin')], nx(23) - 0.1, size=60, rh=170)
lclip([(K('s2c1', 8.0, 15.2), nx(23))], nx(24))
q('For flyaways:<br><i>hairspray on a clean toothbrush</i>', at(23, 'Spray a touch') - 0.1, en(23) + 0.3, QL, size=60)
lclip([(K('s2d12', 4.5, 14.0), nx(24))], nx(25))
q('Or a ribbon<br><i>around the elastic</i>', nx(24) + 0.3, at(24, 'Black') - 0.2, QL, size=64)
q('Black, ivory or navy<br><i>always looks classic</i>', at(24, 'Black'), en(24) + 0.3, QL, size=62)
lclip([(K('s2b23', 13.7, 16.4), nx(25)), (K('s2a25', 9.6, 12.2), at(25, "That's what") + 0.9)], nx(26))
qstack(['No elastic showing.', 'No loose ends.', '<i>It feels intentional.</i>'], [nx(25) + 0.2, at(25, 'No loose'), at(25, "That's what")], nx(26) - 0.1, size=64)

# ================= 3. THE FLIPPED PONYTAIL =================
lclip([(K('s3a7', 0.3, 4.6), nx(26))], en(26) + 0.3)
q('Keep that same<br><i>low ponytail</i>', nx(26) + 0.4, en(26) + 0.2, QL, size=66)
card_from('3. The Flipped Ponytail', en(26) + 0.35, at(27, 'and it looks') - 0.1)
lclip([(K('s3b13', 13.9, 15.9), at(27, 'and it looks') - 0.2)], nx(28))
q('Less than a minute', at(27, 'and it looks'), nx(28) - 0.1, QL, size=70)
lclip([(K('s3b22', 5.2, 7.7), nx(28)), (K('s3b13', 3.8, 6.4), at(28, 'to make'))], nx(29))
lclip([(K('s3b22', 7.7, 13.0), nx(29))], nx(30))
lclip([(K('s3b22', 13.4, 15.4), nx(30))], nx(31))
qstack(['<i>Split</i> above the elastic', '<i>Flip</i> up, over and through', '<i>Slide</i> the elastic up'], [nx(28) + 0.3, nx(29) + 0.3, nx(30) + 0.2], nx(31) - 0.1, size=60, rh=170)
lclip([(K('s3b22', 15.5, 16.7), nx(31)), (K('s3b18', 23.4, 27.4), nx(31) + 2.0)], nx(32))
q('A soft twist on each side,<br><i>folding into the center</i>', nx(31) + 0.3, at(31, 'So chic') - 0.2, QL, size=60)
q('<i>So chic.</i>', at(31, 'So chic'), en(31) + 0.3, QL, size=96)

# ================= 4. THE ROLLED CHIGNON =================
card_at('4. The Rolled Chignon', 32, en(32) + 0.3, size=110)
lclip([(K('sv4a19', 6.4, 12.9), nx(33))], nx(34))
lclip([(K('sv4a19', 12.9, 18.8), nx(34))], nx(35))
qstack(['Loosen the elastic,<br><i>open a small pocket</i>', 'Roll it up,<br><i>tuck it into the pocket</i>'], [nx(33) + 0.3, nx(34) + 0.3], nx(35) - 0.1, size=60, rh=260)
lclip([(K('sv4a19', 18.8, 21.8), nx(35)), (K('sv4a26', 27.6, 33.6), at(35, 'and place'))], nx(36))
qstack(['A few <i>bobby pins</i>', 'One flat,<br><i>just above the elastic</i>'], [nx(35) + 0.3, at(35, 'and place')], nx(36) - 0.1, size=60, rh=240)
lclip([(K('sv4a19', 21.8, 24.7), nx(36))], nx(37))
q('Fine hair?<br><i>It holds even more easily.</i>', nx(36) + 0.3, en(36) + 0.3, QL, size=62)
cfull([(K('hv_chignon38', 16.0, 20.5), nx(37))], nx(38))
q('It sits softly at the nape<br><i>and lets your neckline show.</i>', at(37, 'because') - 0.1, en(37) + 0.3, LOW, size=60, cls='over')
lclip([(K('sv4a19', 24.7, 27.0), nx(38))], nx(39))
q('A salon chair?<br><i>You didn&#8217;t.</i>', nx(38) + 0.2, en(38) + 0.3, QL, size=70)

# ================= 5. THE ROPE TWIST =================
card_at('5. The Rope Twist', 39, en(39) + 0.3, size=110)
lclip([(K('s5a6', 0.7, 4.3), nx(40))], nx(41))
lclip([(K('s5a6', 4.3, 7.8), nx(41))], nx(42))
lclip([(K('s5a6', 8.2, 13.6), nx(42))], nx(43))
lclip([(K('s5a6', 13.6, 16.6), nx(43))], nx(44))
qstack(['<i>Split</i> into two equal sections', '<i>Twist</i> both the same way', '<i>Cross</i> them the other way', 'That&#8217;s what <i>creates the rope</i>'],
       [nx(40) + 0.3, nx(41) + 0.3, nx(42) + 0.3, nx(43) + 0.2], nx(44) - 0.1, size=58, rh=165)
lclip([(K('s5a6', 16.6, 22.6), nx(44))], nx(45))
q('Keep going <i>to the ends</i>', nx(44) + 0.3, nx(45) - 0.1, RT, size=58)
item('ph_elastic.jpg', MID, 900, 560, at(44, 'and finish'), nx(45) - 0.1, label='a small clear elastic', maxw=560, lsize=50)
lclip([(K('tpancake9', 18.2, 24.3), nx(45))], nx(46))
q('Gently pull at the sides.', at(45, 'Gently') - 0.1, at(45, 'It shows') - 0.2, QL, size=64)
q('It shows off the shape,<br><i>and your hair looks fuller.</i>', at(45, 'It shows'), en(45) + 0.3, QL, size=60)
lrow([K('s5a3', 9.4, 13.8), K('s6a5', 23.0, 30.0)], [nx(46), at(46, 'or wrap')], nx(47), labels=['over one shoulder', 'or wrapped into a bun'])

# ================= THE GUIDE =================
cfull([(K('cv_dinner17', 0.4, 7.0), nx(47))], nx(48))
q('A secret most elegant women<br><i>never share</i>', nx(47) + 0.2, en(47) + 0.3, LOW, size=64, cls='over')
lclip([(K('cv_dinner41', 14.0, 23.0), nx(48))], nx(49))
qstack(['The hairstyles for <i>their face shape</i>', 'The silhouettes that <i>flatter them</i>', 'The colors that <i>make their skin glow</i>'],
       [at(48, 'which hairstyles') - 0.1, at(48, 'which silhouettes'), at(48, 'and which colors')], nx(49) - 0.1, size=56, rh=170)
cfull([(K('cv_dinner43', 6.0, 12.5), nx(49)), (K('hv_long2', 0.5, 4.6), at(49, "It's sent"))], nx(50))
q(GUIDE, at(49, 'you can access') - 0.2, en(49) + 0.3, QC, cls='over')

# ================= 6. THE ONE-MINUTE SLEEK BUN =================
card_at('6. The One-Minute Sleek Bun', 50, en(50) + 0.3, size=100)
lclip([(K('hv_mid10', 7.2, 13.8), nx(51))], nx(52))
q('Beautiful on <i>shoulder-length hair</i>', nx(51) + 0.3, nx(52) - 0.1, RT, size=54)
item('ph_donut.png', MID, 900, 520, at(51, 'a small hair donut') - 0.1, nx(52) - 0.1, label='a small hair donut', maxw=600, lsize=50)
lclip([(K('t6b37', 2.0, 5.0), nx(52))], nx(53))
lclip([(K('t6b37', 5.0, 7.4), nx(53)), (K('t6a45', 4.9, 7.15), at(53, 'and slip') + 0.4)], nx(54))
lclip([(K('t6b37', 7.4, 10.8), nx(54))], nx(55))
qstack(['A low ponytail,<br><i>through the donut</i>', 'Fan the hair over it,<br>a second elastic on top', 'A few pins<br><i>around the edge</i>'],
       [nx(52) + 0.3, nx(53) + 0.3, nx(54) + 0.3], nx(55) - 0.1, size=56, rh=230)
lclip([(K('t6a44', 2.0, 9.2), nx(55))], nx(56))
q('Fine hair? <i>Dampen it lightly first.</i>', nx(55) + 0.3, nx(56) - 0.1, RT, size=50)
item('ph_mist.png', MID, 900, 560, at(55, 'lightly dampen'), nx(56) - 0.1, label='a light mist of water', maxw=460, lsize=48)
lclip([(K('gv_mirror11', 6.6, 11.6), nx(56))], nx(57))
q('Very long and thick?<br><i>The twist or the chignon</i><br>will suit you better.', nx(56) + 0.3, en(56) + 0.3, QL, size=58)
lclip([(K('t6b37', 10.8, 13.4), nx(57)), (K('hv_chignon18', 41.4, 44.8), at(57, 'And that smooth') + 1.6)], nx(58))
q('<i>About a minute.</i>', nx(57) + 0.2, at(57, 'And that smooth') - 0.2, QL, size=80)
q('A smooth, round shape makes<br><i>everything look more deliberate.</i>', at(57, 'And that smooth'), en(57) + 0.3, QL, size=58)

# ================= 7. THE FLIPPED HALF-UP =================
cfull([(K('hv_long22', 0.5, 3.8), nx(58))], en(58) + 0.4)
q('Hair down, with a little<br><i>more intention</i>', nx(58) + 0.3, en(58) + 0.2, LOW, size=64, cls='over')
card_from('7. The Flipped Half-Up', en(58) + 0.35, en(59) + 1.0)
lclip([(K('s7a7', 3.4, 7.6), en(59) + 0.8), (K('s3b16', 0.3, 2.7), at(60, 'and secure') + 0.9)], nx(61))
lclip([(K('s3b16', 3.0, 10.9), nx(61))], nx(62))
qstack(['A section from<br><i>above your ears</i>', 'A small elastic,<br>close to your hair color', '<i>Flip</i> it up and through', 'Pull down <i>to tighten</i>'],
       [en(59) + 1.2, at(60, 'and secure'), at(61, 'flip that'), at(61, 'and pull it down')], nx(62) - 0.1, size=54, rh=200)
lclip([(K('s7b2', 22.0, 26.4), nx(62))], nx(63))
qstack(['<i>That&#8217;s all.</i>', 'Straight, wavy<br><i>or curly.</i>'], [nx(62) + 0.2, at(62, 'Straight')], nx(63) - 0.1, size=66, rh=220)
lclip([(K('s3b16', 10.9, 12.2), nx(63)), (K('s7a7', 9.0, 12.5), nx(63) + 2.2)], nx(64))
q('A quiet twist<br><i>that looks considered</i>', at(63, 'and the back') - 0.1, at(63, 'Effortless') - 0.2, QL, size=62)
q('Effortless,<br><i>and still put together.</i>', at(63, 'Effortless'), en(63) + 0.3, QL, size=64)

# ================= 8. THE TUCKED SIDE =================
card_at('8. The Tucked Side', 64, en(64) + 0.3, size=110)
lclip([(K('sv8b11', 2.2, 4.75), nx(65))], nx(66))
q('Make a side part.<br><i>Tuck one side behind your ear.</i>', nx(65) + 0.2, en(65) + 0.3, QL, size=60)
photo('ph_pomade.jpg', 70, 90, 720, 900, nx(66), at(66, 'and smooth') - 0.2)
photo('ph_tuckA.jpg', 70, 100, 722, 880, at(66, 'and smooth'), nx(67) - 0.1)
qstack(['<i>Here&#8217;s the key.</i>', 'A tiny amount of gel or pomade,', 'warmed between your fingers,', 'smoothed over the hair as you tuck.', '<i>It gives the strands a little grip.</i>'],
       [nx(66) + 0.2, at(66, 'Warm a tiny'), at(66, 'between your'), at(66, 'and smooth'), at(66, 'It gives')], nx(67) - 0.1, box_=(850, 60, 1880, 1020), size=50, rh=150)
photo('ph_tuckB.jpg', 70, 60, 716, 960, nx(67), nx(68) - 0.1)
q('One barrette, <i>just above the ear</i>', nx(67) + 0.3, nx(68) - 0.1, (850, 30, 1880, 230), size=54)
pieces([('ph_barrette.png', 'gold'), ('ph_barrt.png', 'or tortoiseshell')], [at(67, 'in gold'), at(67, 'or tortoiseshell')], nx(68) - 0.1, x0=850, hh=300, ybot=760)
photo('ph_tuckC.jpg', 120, 150, 660, 820, nx(68), nx(69) - 0.1)
photo('ph_tuckD.jpg', 860, 150, 658, 820, at(68, 'It shows'), nx(69) - 0.1)
q('One side tucked, <i>one side soft.</i>', nx(68) + 0.2, nx(69) - 0.1, (60, 20, 1860, 140), size=54)

# ================= 9. THE HEADBAND ROLL =================
cfull([(K('s9a10', 26.0, 28.8), nx(69))], nx(69) + 5.0)
q('Beautiful on<br><i>shoulder-length hair</i>', nx(69) + 0.4, nx(69) + 4.7, LOW, size=64, cls='over')
card_from('9. The Headband Roll', nx(69) + 4.8, en(70) + 0.3)
lclip([(K('s9a10', 0.5, 4.4), nx(71))], nx(72))
q('A soft elastic headband', nx(71) + 0.3, nx(72) - 0.1, RT, size=56)
pieces([('ph_band.png', 'black'), ('ph_bandbr.png', 'or chocolate brown')], [at(71, 'like black'), at(71, 'or chocolate')], nx(72) - 0.1, hh=300, ybot=780)
lclip([(K('s9b28', 10.0, 15.8), nx(72))], nx(73))
q('Over your hair,<br><i>low at the back</i>', nx(72) + 0.3, en(72) + 0.3, QL, size=64)
lclip([(K('s9a10', 6.0, 12.6), nx(73))], nx(74))
lclip([(K('s9a10', 15.2, 22.6), nx(74))], nx(75))
qstack(['Start <i>near one ear</i>', 'Curve a small section up,<br>tuck the ends under', 'Work toward the back,<br><i>section by section</i>'],
       [nx(73) + 0.3, at(73, 'take a small'), nx(74) + 0.3], nx(75) - 0.1, size=56, rh=220)
lclip([(K('s9b28', 17.4, 22.0), nx(75))], nx(76))
q('If the band slips:<br><i>a bobby pin across it,</i><br>just behind each ear', nx(75) + 0.3, en(75) + 0.3, QL, size=58)
lclip([(K('s9a10', 23.3, 24.3), nx(76)), (K('s9b28', 22.2, 23.5), nx(76) + 1.7)], nx(77))
q('A soft roll at the nape.<br><i>Timeless.</i>', nx(76) + 0.2, en(76) + 0.3, QL, size=68)

# ================= 10. THE FRENCH PIN BUN =================
lclip([(K('s10b20', 4.0, 9.4), nx(77))], at(77, 'The French pin') - 0.1)
q('The one that takes<br><i>a little practice</i>', at(77, 'The one that') - 0.1, at(77, 'The French pin') - 0.4, QL, size=64)
card_from('10. The French Pin Bun', at(77, 'The French pin') - 0.3, en(77) + 0.5)
item('ph_pin.png', 520, 960, 800, nx(78), nx(79) - 0.1, maxw=300)
q('One pin. <i>No elastic.</i><br>Medium to long hair.', nx(78) + 0.2, nx(79) - 0.2, (900, 0, 1820, H), size=70)
lclip([(K('s10a24', 3.6, 5.5), nx(79)), (K('s10b28', 0.3, 1.5), nx(79) + 3.2)], nx(80))
lclip([(K('s10b28', 1.5, 4.3), nx(80)), (K('s10a24', 5.5, 7.0), at(80, 'and wrap') + 0.7)], nx(81))
lclip([(K('s10b28', 4.3, 6.4), nx(81)), (K('s10a24', 7.0, 8.3), nx(81) + 3.7)], nx(82))
lclip([(K('s10b28', 6.4, 12.4), nx(82))], nx(83))
qstack(['A low ponytail,<br><i>in one hand</i>', '<i>Loop</i> it around your thumb', '<i>Twist</i> the rest, tuck it under', 'Pin in, <i>flip,</i> push through'],
       [nx(79) + 0.3, nx(80) + 0.3, nx(81) + 0.3, at(82, 'Slide the pin')], nx(83) - 0.1, size=56, rh=185)
lclip([(K('s10a24', 8.4, 10.4), nx(83))], nx(84))
q('The tighter the twist,<br><i>the better it holds</i>', nx(83) + 0.2, en(83) + 0.3, QL, size=62)
lclip([(K('s10b28', 12.5, 14.0), nx(84)), (K('s10b13', 10.9, 13.7), nx(84) + 2.5)], nx(85))
q('Give it a few tries.<br><i>It&#8217;s worth it.</i>', nx(84) + 0.2, at(84, "There's a quiet") - 0.2, QL, size=66)
q('A quiet confidence,<br><i>held by a single pin</i>', at(84, "There's a quiet"), en(84) + 0.3, QL, size=62)

# ================= RECAP + CLOSE =================
lclip([(K('cv_ease1', 10.6, 15.0), nx(85)), (K('sv4a36', 16.0, 22.8), nx(85) + 6.8)], nx(86))
RC = [('1. The French twist', at(85, 'One clip')), ('2. The wrapped ponytail', at(85, 'One ponytail')), ('3. The flipped ponytail', at(85, 'One ponytail') + 0.5),
      ('4. The rolled chignon', at(85, 'worn four') - 0.1), ('5. The rope twist', at(85, 'worn four') + 0.5), ('6. The sleek bun', at(85, 'A bun')),
      ('7. The flipped half-up', at(85, 'a half-up')), ('8. The tucked side', at(85, 'two for')), ('9. The headband roll', at(85, 'two for') + 0.6),
      ('10. The French pin bun', at(85, 'and one pin'))]
for k, (txt, tt) in enumerate(RC):
    cx = PW + 60 + (k // 5) * 640
    q(f'<i>{txt}</i>', tt, nx(86) - 0.1, (cx, 190 + (k % 5) * 150, cx + 620, 190 + (k % 5 + 1) * 150), size=46, dur=0.8)
q('<span style="font-size:60px">Looking put together was never about having more time.</span><br><i style="font-size:74px">It&#8217;s about knowing what to do with two minutes.</i>',
  nx(86) + 0.3, en(86) + 0.4, QC)
cfull([(K('hv_long1', 0.6, 4.2), nx(87))], nx(88))
q('A little more ease,<br><i>all day</i>', at(87, 'you carry') - 0.1, en(87) + 0.3, LOW, size=66, cls='over')
lclip([(K('s3a7', 6.0, 14.6), nx(88))], nx(89))
q('Which number will you<br><i>try first?</i>', nx(88) + 0.3, at(88, 'And if') - 0.2, QL, size=66)
q('A part two?<br><i>Let us know.</i>', at(88, 'And if'), en(88) + 0.3, QL, size=66)
cfull([(K('hv_chignon18', 36.0, 41.2), nx(89)), (K('cv_dinner41', 23.2, 26.8), at(89, 'you can access'))], nx(90))
q(GUIDE, at(89, 'you can access') - 0.2, en(89) + 0.3, QC, cls='over')
cfull([(K('hv_twist10', 0.0, 1.6), nx(90))], nx(90) + 0.1) if False else None
q('<span style="font-size:60px">Thank you for spending your time with us.</span><br><i style="font-size:74px">A like or comment means the world to us.</i>',
  nx(90) + 0.3, total - 3.2, QC)
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
