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
# 10 Elegant Ways to Tie a Scarf This Winter (Classy Academy) - beat map (12 Nov 2026)
# Layout of the channel's own tutorial video ("The Most Elegant & Easy Hairstyles", A-JRkjQs2XI): every step is a whole vertical
# tutorial clip at the left on the caramel backdrop with the step written beside it; a white script card per tie; full screen
# (the whole clip over its own blurred copy) only for the hook, the guide and the ending. Every clip window checked by eye.
# Sound: the voice and ONE soft solo-piano bed, steady, no ducking, NO sound effects (none are in the channel's measured files).
TRACKS_EDIT = ['m22n.mp3']; MUSIC_DB = 14; ENDLOGO = 'logo_ce_dark.png'
MUSIC_CREDIT = 'Music: "Piano Reflections" by Ahjay Stelino (Mixkit, free license)'
MID = (PW + 1880) // 2
RT = (PW + 40, 30, 1880, 230)
LOW = (180, 740, 1740, 1040)
for k in ('t2c42', 't1b5', 't8b45', 't9c34', 't1c7', 't3a28', 't1c32', 't3a18', 't3c28', 't5c27', 't4b38', 't1c38', 'x6c9', 'x2b15', 't2b32', 't7c21',
          't2b19', 't1c30', 't7a30', 't9c16', 't9a41', 't7c25', 't10a19', 'x6b15', 'x5b5', 't10b26', 't7c17', 't10b11', 't10b34', 't7a26',
          't5c43', 't2b29', 'x2b13'): MAXSLOW[k] = 2.0
for k in ('t3a18', 't2c42', 't1b5', 't9c34', 't8b45'): MAXSLOW[k] = 2.1
for k in ('bsnow20', 't7b6', 'bcoat1', 'bcoat13', 't8c9', 't9c48', 'bleave7', 'bgrey7', 'bcash7', 'bfold7', 't7a2', 'bsnow8', 'bsnow22', 't7b15',
          't7b17', 'bgrey0', 'bcoat29', 'bsnow14', 'z58b4', 'z26_16'): MAXSLOW[k] = 1.7
MAXSLOW['z58b4'] = 2.0; MAXSLOW['t1c38'] = 2.8; MAXSLOW['bleave6'] = 1.7
# crops (720x1280 space: x0, y0, height; width = height * 9/16): each removes a burned-in caption, a watermark or empty room
CROP['t2c42'] = (118, 0, 860)       # caption pills low in the frame
CROP['t1b5'] = (79, 280, 1000)      # label above her head
CROP['t8b45'] = (82, 290, 990)      # label above her head
CROP['t9c34'] = (72, 250, 1024)     # label above her head
CROP['t2b32'] = (70, 180, 1031)     # black side bars, label above her head
CROP['t4b38'] = (60, 100, 1066)     # black side bars
CROP['x2b15'] = (65, 0, 1010)       # small caption low in the frame
CROP['t7c21'] = (180, 10, 600)      # an icon and caption on her chest
CROP['x2b13'] = (215, 400, 600)     # typed captions above, account mark and sticker below: hands and scarf only
CROP['t3a28'] = (112, 40, 880)      # caption boxes low in the frame, black side bars
CROP['x5b5'] = (62, 222, 1058)      # title above her head
CROP['t2b29'] = (65, 0, 1010)       # small caption low in the frame
CROP['z58b4'] = (0, 0, 1230)        # small mark in the bottom right corner
CROP['t8c9'] = (65, 230, 1050)      # she is small in the frame
CROP['t9c48'] = (120, 380, 900)     # title at the top, she is small in the frame
CROP['t9c16'] = (60, 200, 880)      # TikTok mark at the bottom right
CROP['t7c25'] = (95, 340, 940)      # banners at the top
CROP['t7a2'] = (110, 380, 800)      # she is small in the frame
CROP['bcoat29'] = (80, 120, 924)    # TikTok marks at the left and right edges
CROP['t7b17'] = (90, 0, 1120)       # small mark at the left edge
def qstack(lines, times, t1, box_=QL, size=58, rh=150):
    """the step lines one under the other beside a clip, each appearing as it is said"""
    x0, y0, x1, y1 = box_; n = len(lines); top = (y0 + y1) // 2 - n * rh // 2
    for k, (txt, tt) in enumerate(zip(lines, times)):
        q(txt, tt, t1, (x0, top + k * rh, x1, top + (k + 1) * rh), size=size, dur=1.0)
def card_from(txt, t0, t_out, size=110):
    white(t0, t_out); text(txt, 'card', t0 + 0.3, t_out - 0.1, dur=1.2, out=0.45, style=f'font-size:{size}px;')
GUIDE = '<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>'

# ================= HOOK =================
cfull([(K('bcoat13', 6.8, 11.6), 0.0)], nx(2))
q('You might think elegance in winter takes<br><i>a whole new wardrobe.</i>', 0.3, en(1) + 0.2, LOW, size=64, cls='over')
cfull([(K('t2b19', 15.0, 20.6), nx(2))], nx(3))
q('What if you never needed more than<br><i>one scarf, and five seconds?</i>', nx(2) + 0.1, en(2) + 0.3, LOW, size=64, cls='over')
cfull([(K('t7b6', 0.2, 2.75), nx(3)), (K('bcoat1', 2.4, 6.6), at(3, 'holds just') - 0.3)], nx(4))
q('Your scarf holds as much power<br><i>as the coat itself.</i>', at(3, 'Your scarf') - 0.1, en(3) + 0.3, LOW, size=64, cls='over')
lclip([(K('bsnow20', 11.85, 15.65), nx(4)), (K('t7b6', 2.85, 4.75), nx(4) + 4.75)], nx(5))
q('The finishing touch,<br><i>never an afterthought.</i>', nx(4) + 0.4, en(4) + 0.2, QL, size=70)
lrow([K('t7a2', 2.2, 9.0), K('t1b5', 12.3, 18.2)], [nx(5), at(5, 'ten elegant')], nx(6))
q('<div><span style="font-size:56px;display:block;margin-bottom:34px">10 Elegant Ways</span><i style="font-size:104px">to Tie a Scarf</i>'
  '<span style="font-size:56px;display:block;margin-top:44px">This Winter</span></div>', at(5, 'ten elegant') - 0.1, en(5) + 0.3, (2 * PW + 20, 0, 1900, H))
lclip([(K('t1c30', 0.4, 5.2), nx(6))], nx(7))
q('We&#8217;ll guide you through<br><i>each one.</i>', at(6, "We'll guide") - 0.1, nx(7) - 0.1, QL, size=68)
lclip([(K('x5b5', 0.65, 4.4), nx(7)), (K('t2c42', 12.6, 17.0), at(7, 'These work') - 0.2)], nx(8))
qstack(['No designer scarf.', 'No <i>special skill.</i>', '<i>Any age.</i> Any budget.'],
       [nx(7) + 0.3, at(7, "and you don't"), at(7, 'These work')], nx(8) - 0.1, size=62)
lclip([(K('t1c32', 6.4, 11.9), nx(8))], en(9) + 0.3)
q('One looks complicated.<br><i>It only takes two small moves.</i>', nx(8) + 0.3, nx(9) - 0.2, QL, size=60)
q('So, let&#8217;s <i>get started.</i>', nx(9) + 0.1, en(9) + 0.2, QL, size=72)

# ================= 1. THE PARISIAN KNOT =================
card_at('1. The Parisian Knot', 10, en(10) + 0.3, size=110)
lclip([(K('t8b45', 5.7, 7.5), nx(11)), (K('t1b5', 9.9, 11.2), nx(11) + 3.3), (K('t2c42', 9.8, 11.9), nx(11) + 5.55), (K('t9c34', 10.35, 12.05), nx(11) + 9.5)], nx(12))
q('It works with<br><i>almost any scarf</i>', nx(11) + 3.5, nx(11) + 5.5, QL, size=64)
qstack(['A <i>tailored coat</i>', 'or a casual jacket'], [nx(11) + 5.9, nx(11) + 9.6], nx(12) - 0.1, size=64)
lclip([(K('t2c42', 0.1, 2.4), nx(12)), (K('t1b5', 7.32, 8.8), nx(12) + 4.35), (K('t9c34', 7.3, 8.72), nx(12) + 7.0)], nx(13))
lclip([(K('t2c42', 2.4, 6.5), nx(13))], nx(14))
qstack(['<i>Fold</i> it in half', 'Drape it,<br>both ends <i>through the loop</i>'], [nx(12) + 0.3, at(13, 'then slip')], nx(14) - 0.1, size=60, rh=210)
lclip([(K('t9c34', 8.72, 10.3), nx(14))], nx(14) + 2.75)
q('A little trick<br><i>for the coldest days</i>', nx(14) + 0.3, nx(14) + 2.7, QL, size=64)
q('<span style="font-size:60px">Give the loop one twist</span><br><i style="font-size:74px">before you pull the ends through.</i>', nx(14) + 3.0, nx(14) + 7.8, QC)
lclip([(K('t1b5', 8.8, 9.9), nx(14) + 7.9), (K('t2c42', 6.5, 7.6), nx(14) + 9.75)], nx(15))
q('It closes the gap,<br><i>and keeps the cold air out</i>', nx(14) + 8.1, en(14) + 0.3, QL, size=62)
lclip([(K('t2c42', 7.6, 9.8), nx(15)), (K('t8b45', 7.6, 11.2), nx(15) + 4.15)], nx(16))
q('Close to your neck,<br><i>the ends short and tidy</i>', nx(15) + 0.3, at(15, 'And it takes') - 0.4, QL, size=62)
q('About five seconds.<br><i>It&#8217;s that simple.</i>', at(15, 'And it takes'), en(15) + 0.3, QL, size=66)

# ================= 2. THE WOVEN KNOT =================
lclip([(K('t3a28', 0.4, 3.1), nx(16))], at(16, 'The woven') - 0.6)
q('Keep that<br><i>same fold</i>', nx(16) + 0.4, at(16, 'The woven') - 0.7, QL, size=70)
card_from('2. The Woven Knot', at(16, 'The woven') - 0.55, at(17, 'But here') - 0.1)
lclip([(K('t1c32', 12.0, 14.2), at(17, 'But here') - 0.2), (K('t1c7', 28.7, 30.6), nx(17) + 6.5)], nx(18))
q('The Parisian knot,<br><i>with one extra twist</i>', at(17, "It's really") - 0.1, nx(18) - 0.1, QL, size=64)
lclip([(K('t1c7', 18.45, 19.1), nx(18)), (K('t3a28', 3.1, 5.3), nx(18) + 0.85), (K('t1c7', 19.1, 20.15), nx(18) + 4.8), (K('t3a28', 5.3, 6.9), nx(18) + 6.45)], nx(19))
lclip([(K('x2b13', 12.0, 13.95), nx(19)), (K('t1c7', 20.15, 21.9), nx(19) + 3.3), (K('t3a28', 6.9, 8.2), nx(19) + 5.7)], nx(20))
lclip([(K('t3a28', 8.2, 9.9), nx(20)), (K('t1c7', 23.3, 26.2), nx(20) + 2.9)], nx(21))
qstack(['Fold, drape,<br><i>one end through</i>', '<i>Half-turn</i> the loop,<br>second end through', 'Over and under:<br><i>it lies flat</i>'],
       [nx(18) + 0.3, nx(19) + 0.3, nx(20) + 0.3], nx(21) - 0.1, size=56, rh=220)
lclip([(K('t3a28', 9.9, 12.9), nx(21)), (K('t1c7', 26.2, 28.7), nx(21) + 5.4)], nx(22))
q('Beautiful with<br><i>a woven wool scarf</i>', nx(21) + 0.3, at(21, 'and it instantly') - 0.3, QL, size=62)
q('Polished.<br><i>Intentional.</i>', at(21, 'and it instantly'), at(21, 'So stunning') - 0.2, QL, size=70)
q('<i>So stunning.</i>', at(21, 'So stunning'), en(21) + 0.3, QL, size=96)

# ================= 3. THE ONCE-AROUND =================
card_at('3. The Once-Around', 22, en(22) + 0.3, size=110)
lclip([(K('t3c28', 4.0, 8.95), nx(23))], nx(24))
q('Round and round?', at(23, "It's tempting") - 0.1, at(23, 'But elegance') - 0.2, QL, size=70)
q('Elegance is all about<br><i>balance.</i>', at(23, 'But elegance'), en(23) + 0.3, QL, size=70)
lclip([(K('t3a18', 16.45, 22.9), nx(24))], nx(25))
lclip([(K('t3a18', 22.9, 26.0), nx(25))], nx(26))
qstack(['Wrap it <i>just once</i>', 'One side <i>much longer</i>', 'Once around,<br>both ends in front', '<i>Loosen</i> the loop'],
       [nx(24) + 0.3, at(24, 'Drape the scarf'), at(24, 'wrap that'), nx(25) + 0.3], nx(26) - 0.1, size=58, rh=180)
lrow([K('bcash7', 2.6, 7.0), K('z26_16', 3.6, 7.0)], [nx(26), at(26, 'and just')], nx(27),
     labels=['a fine cashmere scarf', 'a chunky knit'])
lclip([(K('t3a18', 26.5, 30.1), nx(27)), (K('t2b19', 0.9, 4.5), at(27, 'It feels') - 0.2)], nx(28))
q('One soft,<br><i>relaxed line</i>', nx(27) + 0.3, at(27, 'It feels') - 0.3, QL, size=68)
q('It feels effortless,<br><i>because it is.</i>', at(27, 'It feels'), en(27) + 0.3, QL, size=66)

# ================= 4. THE SOFT KNOT =================
card_at('4. The Soft Knot', 28, en(28) + 0.3, size=110)
lclip([(K('t4b38', 0.4, 2.6), nx(29)), (K('t5c27', 0.95, 5.35), at(29, 'Cross the longer') - 0.3)], nx(30))
lclip([(K('t5c27', 5.45, 8.3), nx(30)), (K('t4b38', 6.9, 9.3), nx(30) + 3.6)], nx(31))
qstack(['One side <i>a little longer</i>', 'Long end <i>over</i>, under,<br>and up through the gap', 'Let it fall,<br><i>smooth both ends flat</i>'],
       [nx(29) + 0.3, at(29, 'Cross the longer'), nx(30) + 0.3], nx(31) - 0.1, size=56, rh=210)
lclip([(K('t4b38', 9.35, 11.45), nx(31)), (K('x6b15', 7.2, 10.7), nx(31) + 3.6), (K('x6b15', 12.72, 13.98), nx(31) + 9.8)], nx(32))
q('Almost any scarf,<br><i>whatever its length</i>', nx(31) + 0.3, at(31, 'And for an') - 0.3, QL, size=62)
q('A simple gold pin,<br><i>or a brooch</i>', at(31, 'hold it'), en(31) + 0.3, QL, size=66)
lclip([(K('t5c27', 8.3, 12.6), nx(32)), (K('t2c42', 19.6, 22.3), nx(32) + 8.1)], nx(33))
qstack(['One loose knot,<br><i>just below your chin</i>', 'It frames your face', '<i>Nothing is pulled tight</i>'],
       [nx(32) + 0.3, at(32, 'It frames'), at(32, 'and it looks')], at(32, 'Even the simplest') - 0.3, size=58, rh=180)
q('Even the simplest coat<br><i>feels polished.</i>', at(32, 'Even the simplest'), en(32) + 0.3, QL, size=64)

# ================= 5. THE FAKE KNOT =================
card_at('5. The Fake Knot', 33, nx(34) + 1.0, size=110)
lclip([(K('t5c43', 12.25, 14.75), nx(34) + 0.9)], nx(35))
q('Something intricate?<br><i>You didn&#8217;t.</i>', nx(34) + 1.3, en(34) + 0.2, QL, size=68)
lclip([(K('t1c38', 2.8, 4.6), nx(35)), (K('x6c9', 1.45, 3.95), at(35, 'and tie') + 0.05)], nx(36))
lclip([(K('x6c9', 4.0, 6.75), nx(36)), (K('t1c38', 7.9, 9.95), nx(36) + 3.2)], nx(37))
qstack(['One side <i>a little longer</i>', 'One <i>very loose knot</i><br>in the longer side', 'Other end <i>through the knot</i>,<br>then slide it up'],
       [nx(35) + 0.3, at(35, 'and tie'), nx(36) + 0.3], nx(37) - 0.1, size=56, rh=210)
T37 = at(37, 'Over a simple') - 0.2
lclip([(K('t2b29', 7.25, 9.3), nx(37)), (K('x6c9', 6.8, 8.8), T37), (K('t2b29', 5.6, 7.2), T37 + 2.5)], nx(38))
q('With a coat:<br><i>close to your neck</i>', nx(37) + 0.3, T37 - 0.1, QL, size=64)
q('Over a knit:<br><i>lower, like a necklace</i>', T37 + 0.2, en(37) + 0.3, QL, size=64)
lclip([(K('t1c38', 10.05, 10.85), nx(38)), (K('t1c38', 10.95, 11.85), nx(38) + 1.75), (K('t1c38', 11.95, 12.65), nx(38) + 3.75), (K('t5c43', 9.3, 12.2), nx(38) + 4.95)], at(38, 'Clean lines') - 0.3)
q('The ends fall in<br><i>one clean line</i>', nx(38) + 0.3, at(38, "It's easy") - 0.3, QL, size=64)
q('Easy to adjust,<br><i>quick to take off</i>', at(38, "It's easy"), at(38, 'Clean lines') - 0.4, QL, size=64)
q('<span style="font-size:60px">Clean lines always win.</span><br><i style="font-size:84px">So chic.</i>', at(38, 'Clean lines') - 0.05, en(38) + 0.3, QC)

# ================= THE GUIDE =================
cfull([(K('bsnow22', 0.3, 4.6), nx(39))], nx(40))
q('A secret most elegant women<br><i>never share</i>', nx(39) + 0.3, en(39) + 0.2, LOW, size=64, cls='over')
lrow([K('t7b15', 0.4, 6.6), K('t7b17', 1.6, 6.6), K('bsnow8', 0.6, 5.0)], [nx(40), at(40, 'which silhouettes'), at(40, 'and which hairstyles')], nx(41),
     labels=['colors that make you glow', 'silhouettes that flatter', 'hairstyles for your face'])
cfull([(K('bcoat13', 0.9, 6.6), nx(41)), (K('bcoat13', 15.8, 19.4), nx(41) + 6.6)], nx(42))
q(GUIDE, at(41, 'you can access') - 0.2, en(41) + 0.3, QC, cls='over')

# ================= 6. THE HIDDEN KNOT =================
card_at('6. The Hidden Knot', 42, en(42) + 0.3, size=110)
cfull([(K('bsnow14', 0.3, 8.1), nx(43))], nx(44))
q('Staying warm really is the priority.', nx(43) + 0.3, at(43, 'But winter') - 0.2, LOW, size=60, cls='over')
q('Balance comfort<br><i>with elegance.</i>', at(43, 'But winter'), en(43) + 0.3, LOW, size=66, cls='over')
lclip([(K('x2b15', 0.3, 2.4), nx(44)), (K('t2b32', 14.3, 18.4), nx(44) + 3.7)], nx(45))
lclip([(K('x2b15', 2.4, 6.6), nx(45))], nx(46))
lclip([(K('x2b15', 6.6, 8.8), nx(46)), (K('t7c21', 9.3, 12.0), nx(46) + 3.9)], nx(47))
qstack(['<i>Middle</i> at the front,<br>ends down your back', '<i>Cross</i> behind,<br>bring them forward', 'One loose knot,<br><i>tucked under the wrap</i>', 'Smooth the ends flat,<br><i>or tuck them into your coat</i>'],
       [nx(44) + 0.3, at(44, 'Cross them'), nx(45) + 0.3, nx(46) + 0.3], nx(47) - 0.1, size=50, rh=200)
lclip([(K('t2b19', 12.9, 14.7), nx(47)), (K('t1c30', 21.6, 24.45), nx(47) + 3.1)], nx(48))
qstack(['Like a <i>soft turtleneck</i>', 'No loose ends.', '<i>Nothing to fix.</i>'], [nx(47) + 0.3, at(47, 'No loose'), at(47, 'nothing to fix')], nx(48) - 0.1, size=64)
cfull([(K('bleave7', 0.3, 4.6), nx(48))], en(48) + 0.3)
q('Warm, and<br><i>effortlessly elegant.</i>', at(48, 'Warm') - 0.1, en(48) + 0.2, LOW, size=66, cls='over')

# ================= 7. THE DRAPE =================
card_at('7. The Drape', 49, en(49) + 0.3, size=110)
q('<span style="font-size:60px">True elegance is subtle,</span><br><i style="font-size:76px">never flashy or loud.</i>', nx(50) + 0.2, nx(51) - 0.15, QC)
lclip([(K('t2c42', 24.3, 29.85), nx(51))], nx(52))
qstack(['Around the <i>back of your neck</i>', 'Both sides <i>straight down</i>', 'Under your coat,<br><i>along the lapels</i>'],
       [nx(51) + 0.3, at(51, 'let both sides'), at(51, 'and wear it')], nx(52) - 0.1, size=58, rh=190)
lclip([(K('t5c27', 0.05, 0.9), nx(52)), (K('z58b4', 3.95, 5.55), nx(52) + 1.25), (K('z58b4', 2.75, 3.85), nx(52) + 4.0)], nx(53))
q('Both ends even.', nx(52) + 0.3, at(52, 'Or leave') - 0.2, QL, size=70)
q('Or one a little longer,<br><i>on purpose.</i>', at(52, 'Or leave'), en(52) + 0.3, QL, size=64)
lclip([(K('t2c42', 29.9, 32.2), nx(53)), (K('t7c17', 5.6, 10.9), nx(53) + 3.6)], nx(54))
q('Two long lines<br><i>follow your lapels</i>', at(53, 'because those') - 0.1, at(53, "That's what") - 0.2, QL, size=64)
q('That&#8217;s what makes it<br><i>so flattering.</i>', at(53, "That's what"), en(53) + 0.3, QL, size=64)
lclip([(K('z58b4', 5.65, 6.95), nx(54)), (K('z58b4', 0.85, 1.98), nx(54) + 2.15), (K('t7c17', 11.0, 14.9), nx(54) + 3.95), (K('bcoat1', 7.0, 11.4), nx(54) + 8.3)], nx(55))
q('Intentional,<br><i>with no effort at all</i>', nx(54) + 0.3, at(54, "It's best") - 0.3, QL, size=64)
q('Best with a shorter scarf,<br><i>on a calm day</i>', at(54, "It's best"), at(54, 'Save the knots') - 0.3, QL, size=62)
q('Save the knots<br><i>for the windy ones.</i>', at(54, 'Save the knots'), en(54) + 0.3, QL, size=64)

# ================= 8. THE SHOULDER THROW =================
card_at('8. The Shoulder Throw', 55, nx(55) + 3.3, size=104)
lclip([(K('t7b6', 9.12, 10.68), nx(55) + 3.2)], nx(56))
q('One end in front,<br><i>one end behind</i>', nx(55) + 3.5, nx(56) - 0.1, QL, size=66)
lclip([(K('t8c9', 0.4, 5.0), nx(56)), (K('t7a30', 2.6, 5.45), nx(56) + 3.6), (K('t7a30', 5.55, 9.2), at(56, 'and with a small') - 0.7)], nx(57))
qstack(['<i>Open</i> the scarf out', 'Drape it around your neck', 'A small flick:<br><i>one end over the opposite shoulder</i>'],
       [nx(56) + 0.3, at(56, 'Drape it'), at(56, 'and with a small')], nx(57) - 0.1, size=56, rh=190)
lclip([(K('t8c9', 5.05, 11.6), nx(57)), (K('t7b6', 5.75, 9.05), nx(57) + 7.4)], nx(58))
q('For a thick,<br><i>generous scarf</i>', nx(57) + 0.3, at(57, "and there's") - 0.3, QL, size=66)
q('Quietly confident.<br><i>Relaxed, never fussy.</i>', at(57, "and there's"), en(57) + 0.3, QL, size=64)
lrow([K('pg319', 0.3, 8.9), K('bgrey7', 2.45, 6.6)], [at(58, 'A cream scarf') - 0.2, at(58, 'A burgundy scarf') - 0.2], nx(59),
     labels=['cream on camel', 'burgundy on grey'])
q('A little secret<br><i>about color</i>', nx(58) + 0.3, at(58, 'A cream scarf') - 0.3, QC, size=72)
lclip([(K('bgrey0', 17.0, 23.4), nx(59))], nx(60))
q('Two or three colors.<br><i>Cohesive and refined.</i>', nx(59) + 0.3, en(59) + 0.3, QL, size=64)

# ================= 9. THE BLANKET SCARF TRIANGLE =================
lclip([(K('bfold7', 2.0, 5.7), nx(60))], en(60) + 0.3)
q('A big square<br><i>blanket scarf?</i>', nx(60) + 0.4, en(60) + 0.2, QL, size=66)
card_from('9. The Blanket Scarf Triangle', en(60) + 0.35, at(61, 'But too much') - 0.1, size=92)
lclip([(K('t9c48', 2.5, 7.2), at(61, 'But too much') - 0.2)], nx(62))
q('Too much fabric<br><i>takes away the polish</i>', at(61, 'But too much'), at(61, 'The secret') - 0.2, QL, size=62)
q('The secret is<br><i>one fold.</i>', at(61, 'The secret'), en(61) + 0.3, QL, size=70)
lclip([(K('t7c25', 2.9, 6.5), nx(62)), (K('t9c16', 8.0, 9.9), nx(62) + 6.75)], nx(63))
lclip([(K('t9c16', 9.9, 13.1), nx(63)), (K('t9a41', 3.2, 8.6), at(63, 'Let them hang') - 0.3)], nx(64))
lclip([(K('t9c16', 30.0, 33.5), nx(64))], nx(65))
qstack(['<i>Corner to corner:</i><br>a triangle', 'Point down, in front', 'Corners <i>behind and back</i><br>to the front', 'Bulky? <i>Roll the long edge</i>'],
       [nx(62) + 0.3, at(62, 'Hold the two'), nx(63) + 0.3, nx(64) + 0.3], nx(65) - 0.1, size=54, rh=200)
lclip([(K('t9c48', 9.2, 15.3), nx(65))], nx(66))
q('A little soft<br><i>and undone</i>', nx(65) + 0.3, at(65, 'And there') - 0.3, QL, size=68)
q('<i>And there you have it.</i>', at(65, 'And there'), en(65) + 0.3, QL, size=68)

# ================= 10. THE BELTED WRAP =================
card_at('10. The Belted Wrap', 66, en(66) + 0.3, size=110)
lclip([(K('t10b11', 1.6, 9.9), nx(67))], nx(68))
qstack(['<i>Open</i> it fully', 'Over your shoulders,<br><i>like a shawl</i>', 'Both sides <i>down the front</i>'],
       [nx(67) + 0.3, at(67, 'and drape'), at(67, 'Let both sides')], nx(68) - 0.1, size=58, rh=190)
lclip([(K('t10b11', 9.9, 12.2), nx(68)), (K('t10a19', 2.3, 6.45), nx(68) + 3.0), (K('t10a19', 6.55, 8.45), at(68, 'will go with') - 0.3)], nx(69))
q('A slim leather belt,<br><i>at your waist</i>', nx(68) + 0.3, at(68, 'A belt in') - 0.3, QL, size=64)
q('Black or brown<br><i>goes with almost anything</i>', at(68, 'A belt in'), en(68) + 0.3, QL, size=60)
lclip([(K('t10a19', 8.55, 10.4), nx(69)), (K('t10b34', 18.6, 24.2), nx(69) + 2.6), (K('t10b11', 12.3, 15.0), at(69, 'Your hands') + 0.7)], nx(70))
qstack(['The scarf becomes<br><i>a soft cape</i>', 'The belt gives it <i>a shape</i>', 'Your hands are free'],
       [nx(69) + 0.3, at(69, 'It looks intentional'), at(69, 'Your hands')], nx(70) - 0.1, size=58, rh=190)
lclip([(K('t10b34', 33.4, 39.6), nx(70))], nx(71))
q('A coffee date,<br>or an evening out', nx(70) + 0.3, at(70, 'Absolutely') - 0.2, QL, size=62)
q('<i>Absolutely stunning.</i>', at(70, 'Absolutely'), en(70) + 0.3, QL, size=84)

# ================= RECAP + CLOSE =================
lclip([(K('t10b26', 7.15, 10.35), nx(71)), (K('t7a26', 1.4, 3.4), nx(71) + 4.9)], nx(72))
RC = ['1. The Parisian knot', '2. The woven knot', '3. The once-around', '4. The soft knot', '5. The fake knot',
      '6. The hidden knot', '7. The drape', '8. The shoulder throw', '9. The blanket triangle', '10. The belted wrap']
for k, txt in enumerate(RC):
    cx = PW + 60 + (k // 5) * 640
    q(f'<i>{txt}</i>', nx(71) + 0.3 + k * 0.6, nx(72) - 0.1, (cx, 190 + (k % 5) * 150, cx + 620, 190 + (k % 5 + 1) * 150), size=46, dur=0.8)
lclip([(K('t7b17', 6.7, 10.6), nx(72)), (K('bcash7', 0.2, 2.35), nx(72) + 3.5), (K('bcash7', 7.1, 10.1), nx(72) + 6.0)], nx(73))
q('You don&#8217;t need a new coat.', nx(72) + 0.3, at(72, 'You just need') - 0.2, QL, size=64)
q('Just the scarf<br><i>you already own.</i>', at(72, 'You just need'), en(72) + 0.3, QL, size=70)
cfull([(K('bcoat29', 0.4, 9.1), nx(73))], nx(74))
q('Polished, confident<br><i>and at ease.</i>', at(73, 'you step outside') - 0.1, at(73, 'Those little') - 0.2, LOW, size=66, cls='over')
q('Little moments of intention<br><i>add up, and they show.</i>', at(73, 'Those little'), en(73) + 0.3, LOW, size=60, cls='over')
lclip([(K('t7a26', 3.4, 8.6), nx(74)), (K('t7b6', 10.75, 12.8), at(74, 'and which one') - 0.1)], nx(75))
q('A part two?<br><i>Let us know.</i>', at(74, 'So let us') - 0.1, at(74, 'and which one') - 0.3, QL, size=66)
q('Which one will you<br><i>try first?</i>', at(74, 'and which one'), en(74) + 0.3, QL, size=66)
cfull([(K('bleave6', 0.3, 8.9), nx(75))], nx(76))
q(GUIDE, at(75, 'be sure') - 0.2, en(75) + 0.3, QC, cls='over')
# the outro runs over clips, as on the channel (this ending was rendered as its own short composition and joined on)
cfull([(K('bsnow8', 5.1, 8.6), nx(76) - 0.25), (K('bcoat13', 12.8, 14.3), nx(76) + 5.2), (K('bgrey0', 23.5, 29.3), nx(76) + 7.3)], total - 3.2)
q('<span style="font-size:58px">Thank you for spending your time with us.</span><br><i style="font-size:70px">A like or comment means the world to us.</i>',
  nx(76) + 0.3, at(77, 'Until') - 0.35, LOW, cls='over')
q('Until next time.<br><i>Bye, my loves.</i>', at(77, 'Until') - 0.05, total - 3.2, LOW, size=70, cls='over')
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
