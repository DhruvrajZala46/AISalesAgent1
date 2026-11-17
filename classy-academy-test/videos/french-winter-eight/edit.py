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
# 8 French-Inspired Winter Essentials (The Classy Elegance) - beat map (14 Nov 2026)
# Layouts: only those read off the channel's own wardrobe videos (videos/age-swaps/VISUAL-ANALYSIS.md, sections 1 and 6):
#   white script card per piece | one whole vertical clip at the left on caramel with the line to remember beside it |
#   rows of whole vertical clips, one per spoken item, small script labels | two framed clips with a label above each |
#   product photos cut out on the caramel with their names | the principle line alone on caramel |
#   full screen (the whole clip over its own blurred copy) only for the hook, the guide and the ending.
# Sound: the voice and ONE soft solo-piano bed, steady, no ducking, NO sound effects (none are in the channel's measured files).
TRACKS_EDIT = ['m711n.mp3']; MUSIC_DB = 15; ENDLOGO = 'logo_ce_dark.png'
MUSIC_CREDIT = 'Music: "Classical 4" by Jonny S. (Mixkit, free license)'
MID = (PW + 1880) // 2
RT = (PW + 40, 30, 1880, 230)
LOW = (180, 740, 1740, 1040)
def qstack(lines, times, t1, box_=QL, size=58, rh=150):
    """lines one under the other beside a clip, each appearing as it is said"""
    x0, y0, x1, y1 = box_; n = len(lines); top = (y0 + y1) // 2 - n * rh // 2
    for k, (txt, tt) in enumerate(zip(lines, times)):
        q(txt, tt, t1, (x0, top + k * rh, x1, top + (k + 1) * rh), size=size, dur=1.0)
def card_from(txt, t0, t_out, size=110):
    white(t0, t_out); text(txt, 'card', t0 + 0.3, t_out - 0.1, dur=1.2, out=0.45, style=f'font-size:{size}px;')
GUIDE = '<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>'
def grid8(items, tin, t1, x0=PW + 40, x1=1900, ytop=36, rowh=516, imh=372):
    """the eight pieces as numbered cut-outs on the caramel (4 x 2), each with its number and name in script"""
    ids = []; cols = 4; cw = (x1 - x0) / cols
    for k, (png, lab) in enumerate(items):
        r, c = divmod(k, cols); left = x0 + cw * c; top = ytop + r * rowh
        im = _PILImage.open(os.path.join(A, png)); ar = im.width / im.height
        h2 = imh; w2 = h2 * ar
        if w2 > cw - 36: w2 = cw - 36; h2 = w2 / ar
        i = nid('g8'); PHOTOS.append(png)
        els.append(f'<div id="{i}" style="position:absolute;z-index:46;left:{left:.0f}px;top:{top}px;width:{cw:.0f}px;height:{rowh}px;opacity:0">'
                   f'<img src="assets/{png}" style="position:absolute;left:{(cw-w2)/2:.0f}px;top:{imh+14-h2:.0f}px;width:{w2:.0f}px;height:{h2:.0f}px;filter:drop-shadow(0 18px 22px rgba(70,35,15,.36))">'
                   f'<div style="position:absolute;left:0;top:{imh+22}px;width:{cw:.0f}px;text-align:center;font-family:Pinyon;font-size:46px;color:#fff;text-shadow:0 2px 14px rgba(60,40,25,.35)">{k+1}. {lab}</div></div>')
        tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.7,ease:"power2.out"}},{tin[k]:.3f});'); fade_out(i, t1, 0.5); ids.append(i)
    return ids
def light(ids, nums, t0, t1):
    """only the pieces in use stay bright while an outfit is named"""
    for k, i in enumerate(ids):
        if k + 1 not in nums:
            tw.append(f'tl.to("#{i}",{{opacity:0.2,duration:0.45,ease:"sine.inOut"}},{t0:.3f});'); tw.append(f'tl.to("#{i}",{{opacity:1,duration:0.45,ease:"sine.inOut"}},{t1:.3f});')
exec(open(os.path.join(P, 'clips.py')).read())      # C: slot -> (key, start, end); every window checked by eye. CROP / MAXSLOW per key.
def c(n): return K(*C[n])
# ==== BODY ====  (dry.py runs everything below this line with stub layouts to list each slot's time on screen)
def two(a, b, t0, tb, t1, la=None, lb=None, tla=None, tlb=None, size=54):
    """two framed clips on caramel, a label above each, each label appearing on its own word"""
    xa, xb, y0, w_, h_ = 300, 1100, 150, 520, 860
    _frames([(a, t0)], t1, xa, y0, w_, h_, radius=6, shadow=True)
    _frames([(b, tb)], t1, xb, y0, w_, h_, radius=6, shadow=True)
    if la: q(la, tla or t0 + 0.3, t1, (xa - 70, 40, xa + w_ + 70, 140), size=size, dur=0.9)
    if lb: q(lb, tlb or tb + 0.3, t1, (xb - 70, 40, xb + w_ + 70, 140), size=size, dur=0.9)
def lab(txt, col, t0, t1):
    """the small script label low on the col-th clip of a row"""
    clabel(txt, PW * col + PW // 2, H - 120, t0, t1)
def lights(ids, steps, t_end):
    """steps = [(set of piece numbers in use, time)]: the pieces of the outfit stay bright, the others dim"""
    for nums, t in steps:
        for k, i in enumerate(ids):
            tw.append(f'tl.to("#{i}",{{opacity:{1 if (not nums or k + 1 in nums) else 0.22},duration:0.45,ease:"sine.inOut"}},{t:.3f});')
def twoph(pa, pb, t0, tb, t1, la, lb, hh=770, y0=96, posa='50% 50%', posb='50% 50%'):
    """two real photos framed on the caramel, a script label under each (used where no true clip exists)"""
    for png, cx, tt, lab_, pos in ((pa, 560, t0, la, posa), (pb, 1360, tb, lb, posb)):
        im = _PILImage.open(os.path.join(A, png)); w_ = int(min(640, max(460, hh * im.width / im.height)))
        photo(png, cx - w_ // 2, y0, w_, hh, tt, t1, label=lab_, pos=pos)
def lphoto(png, t0, t1, pos='50% 50%'):
    """a real photo filling the left column, where no true clip exists"""
    photo(png, 0, 0, PW, H, t0, t1, pos=pos)
RIGHT2 = (2 * PW + 20, 0, 1900, H)          # the caramel beside a row of two clips
TXL = (PW + 40, 60, 1250, 1020)             # the text column when a photo stands at the far right

# ================= HOOK =================
cfull([(c('h1'), 0.0)], nx(2))
q('Before you buy one more thing for winter,<br><i>stop.</i>', 0.3, en(1) + 0.2, LOW, size=64, cls='over')
cfull([(c('h2'), nx(2))], nx(3))
q('Eight pieces can carry you<br><i>through the whole season.</i>', nx(2) + 0.1, at(2, 'How many') - 0.25, LOW, size=64, cls='over')
q('How many of them<br><i>do you already own?</i>', at(2, 'How many'), en(2) + 0.3, LOW, size=64, cls='over')
lclip([(c('i3a'), nx(3)), (c('i3b'), at(3, "But here's") - 0.2)], nx(4))
q('You might think looking elegant in winter<br><i>means buying more.</i>', nx(3) + 0.3, at(3, "But here's") - 0.3, QL, size=58)
q('The best-dressed women<br>often wear less:<br><i>the right pieces, again and again.</i>', at(3, 'The best-dressed'), en(3) + 0.3, QL, size=60)
lclip([(c('i4a'), nx(4))], at(4, 'A long coat') - 0.15)
q('Parisian street style,<br><i>on a cold day</i>', nx(4) + 0.3, at(4, 'A long coat') - 0.3, QL, size=66)
lrow([c('i4b'), c('i4c'), c('i4d')], [at(4, 'A long coat') - 0.1, at(4, 'a fine knit') - 0.1, at(4, 'a good pair') - 0.1], nx(5),
     labels=['A long coat', 'A fine knit', 'Good boots'])
lrow([c('i5a'), c('i5b'), c('i5c')], [nx(5), nx(5) + 1.3, nx(5) + 2.6], at(5, 'fewer pieces') - 0.15)
lclip([(c('i5d'), at(5, 'fewer pieces') - 0.1), (c('i5e'), at(5, 'is one any') - 0.3)], nx(6))
qstack(['Fewer pieces', '<i>Chosen with care</i>', 'Worn often'], [at(5, 'fewer pieces'), at(5, 'chosen with'), at(5, 'and worn')], nx(6) - 0.1, size=68)
lclip([(c('i6a'), nx(6)), (c('i6b'), at(6, 'exactly') - 0.3)], nx(7))
q('<div><span style="font-size:64px;display:block;margin-bottom:26px">8 French-Inspired</span><i style="font-size:96px">Winter Essentials</i></div>',
  at(6, 'eight') - 0.1, en(6) + 0.3, QL)
lclip([(c('i7a'), nx(7)), (c('i7b'), at(7, 'And at the end') - 0.2)], nx(8))
q('One of them, most of us<br><i>pack away in winter</i>', nx(7) + 0.3, at(7, 'And at the end') - 0.3, QL, size=64)
q('And at the end,<br>all eight become<br><i>complete outfits</i>', at(7, 'And at the end'), en(7) + 0.3, QL, size=64)
lclip([(c('i8'), nx(8)), (c('c9'), nx(9))], at(9, 'Number one') - 0.35)
q('So, let&#8217;s <i>get started.</i>', nx(8) + 0.1, en(8) + 0.3, QL, size=72)
q('The piece everyone<br><i>sees first</i>', nx(9) + 0.25, at(9, 'Number one') - 0.5, QL, size=68)

# ================= 1. A LONG WOOL COAT =================
card_from('1. A Long Wool Coat', at(9, 'Number one') - 0.45, en(9) + 0.35)
lclip([(c('c10a'), nx(10)), (c('c10b'), at(10, 'Get it right') - 0.2)], nx(11))
q('In winter, your coat<br><i>is your outfit</i>', nx(10) + 0.3, at(10, 'Get it right') - 0.3, QL, size=68)
q('Get it right,<br><i>and you feel polished</i>', at(10, 'Get it right'), en(10) + 0.3, QL, size=68)
# the rack with price tags -> the wool label inside (a held frame of the label) -> a hand on the cloth of a coat in the shop
lclip([(c('c11a'), nx(11)), (c('c11l'), at(11, 'look at the label') - 0.3), (c('c11b'), at(11, 'many coats') - 0.2)], nx(12))
q('Before the price,<br><i>the label inside</i>', nx(11) + 0.4, at(11, 'many coats') - 0.35, QL, size=68)
photo('ph_lbsyn_c.png', 690, 230, 540, 440, at(11, 'many coats') - 0.1, nx(12) - 0.15, label='Mostly synthetic')
photo('ph_lbcoat_c.png', 1290, 230, 540, 440, at(11, 'As a guide'), nx(12) - 0.15, label='60% wool or more')
q('A good blend is <i>perfectly fine</i>', at(11, 'A good blend'), nx(12) - 0.15, (PW + 50, 840, 1870, 1010), size=58)
lclip([(c('c12a'), nx(12))], at(12, 'because it covers') - 0.15)
q('Then check<br><i>the length</i>', nx(12) + 0.3, at(12, 'feels warmer') - 0.3, QL, size=70)
q('Below the knee:<br><i>warmer, and cleaner</i>', at(12, 'feels warmer'), at(12, 'because it covers') - 0.3, QL, size=66)
two(c('c12b'), c('c12c'), at(12, 'because it covers') - 0.1, at(12, 'No skirt') - 0.15, nx(13), la='It covers the hem', lb='A hem peeking out')
lclip([(c('c13a'), nx(13)), (c('c13b'), at(13, 'or even a blazer') - 0.2)], nx(14))
q('The step<br><i>most people skip</i>', nx(13) + 0.3, at(13, 'Try it on') - 0.3, QL, size=68)
qstack(['Try it on over<br><i>a thick sweater, or a blazer</i>', 'Shoulders <i>flat</i>', 'Arms <i>free</i>'],
       [at(13, 'Try it on'), at(13, 'If the shoulders'), at(13, 'and your arms')], nx(14) - 0.1, size=58, rh=190)
two(c('c14a'), c('c14b'), nx(14), at(14, 'or belted') - 0.15, at(14, 'In a timeless') - 0.15, la='Open, over a knit and jeans', lb='Or belted', size=50)
lrow([c('c14c'), c('c14d')], [at(14, 'In a timeless') - 0.05, at(14, 'or camel') - 0.1], nx(15), labels=['Navy', 'Camel'])
q('It goes with<br><i>everything<br>on this list</i>', at(14, 'it goes with'), en(14) + 0.3, RIGHT2, size=60)

# ================= 2. A FINE TURTLENECK =================
lclip([(c('t15'), nx(15))], at(15, 'A fine turtleneck') - 0.35)
q('So what goes<br><i>underneath?</i>', nx(15) + 0.2, at(15, 'Number two') - 0.3, QL, size=72)
q('The piece that quietly makes<br><i>winter dressing work</i>', at(15, 'Number two'), at(15, 'A fine turtleneck') - 0.5, QL, size=60)
card_from('2. A Fine Turtleneck', at(15, 'A fine turtleneck') - 0.45, en(15) + 0.45)
lclip([(c('t16a'), nx(16))], at(16, 'So instead') - 0.15)
q('Thin layers<br><i>hold warm air between them</i>', nx(16) + 0.3, at(16, 'So instead') - 0.3, QL, size=64)
_t0, _t1 = at(16, 'So instead') - 0.1, at(16, 'It feels just') - 0.15     # one bulky knit (a clip) beside the thin first layer (the piece itself)
_frames([(c('t16b'), _t0)], _t1, 300, 150, 520, 860, radius=6, shadow=True)
q('One bulky knit', _t0 + 0.3, _t1, (230, 40, 890, 140), size=54, dur=0.9)
prod('ph_tt.png', 1360, 950, 740, at(16, 'try a thin') - 0.15, _t1, maxw=600)
q('A thin first layer', at(16, 'try a thin') + 0.15, _t1, (1030, 40, 1690, 140), size=54, dur=0.9)
lclip([(c('t16d'), at(16, 'It feels just') - 0.1)], nx(17))
q('Just as warm,<br><i>and so much sleeker</i>', at(16, 'It feels just') + 0.2, en(16) + 0.3, QL, size=68)
q('<i>And here&#8217;s the part I love</i>', nx(17) + 0.3, at(17, 'In winter') - 0.35, QC, size=84)
_t1 = at(17, 'The coat comes off') - 0.15
lrow([c('t17a'), c('t17b')], [at(17, 'In winter') - 0.1, at(17, 'and a warm') - 0.1], _t1)
lab('A cold street', 0, at(17, 'a cold street') - 0.2, _t1 - 0.05)
lab('A warm caf&eacute;', 1, at(17, 'and a warm') + 0.35, _t1 - 0.05)
q('In winter, you move<br><i>between the two</i>', at(17, 'In winter') + 0.3, _t1 - 0.1, RIGHT2, size=58)
lclip([(c('t17c'), at(17, 'The coat comes off') - 0.1), (c('t17e'), at(17, 'So every layer') - 0.2)], nx(18))
q('The coat comes off.<br>Across the table, they only see<br><i>your top half</i>', at(17, 'The coat comes off') + 0.2, at(17, 'So every layer') - 0.3, QL, size=58)
q('So every layer needs to<br><i>look good on its own</i>', at(17, 'So every layer'), en(17) + 0.3, QL, size=64)
lclip([(c('t18z'), nx(18))], at(18, 'Under a shirt') - 0.15)
q('Bring the rest of your wardrobe<br><i>into winter</i>', nx(18) + 0.3, at(18, 'Under a shirt') - 0.3, QL, size=60)
lrow([c('t18a'), c('t18b')], [at(18, 'Under a shirt') - 0.1, at(18, 'Under a V-neck') - 0.1], nx(19), labels=['Under a shirt', 'Under a V-neck'])
photo('ph_ttdress.jpg', 2 * PW + 46, 96, 516, 804, at(18, 'Even under') - 0.1, nx(19) - 0.05, label='Under a dress')
lclip([(c('t19'), nx(19))], nx(20))
q('The one place<br><i>you don&#8217;t need to spend</i>', nx(19) + 0.3, at(19, 'A simple cotton') - 0.3, QL, size=64)
pieces([('ph_tt.png', 'Black'), ('ph_ttc.png', 'Cream'), ('ph_ttn.png', 'Navy')], [at(19, 'black'), at(19, 'cream'), at(19, 'or navy')], nx(20) - 0.15)
lclip([(c('t20'), nx(20))], en(20) + 0.6)
q('One thin layer,<br><i>and half your closet<br>works in winter</i>', nx(20) + 0.3, at(20, 'And when') - 0.3, QL, size=62)
q('The coat comes off,<br><i>and you still feel at ease</i>', at(20, 'And when'), en(20) + 0.3, QL, size=62)

# ================= 3. A V-NECK SWEATER =================
card_from('3. A V-Neck Sweater', en(20) + 0.35, at(21, 'And the neckline') - 0.1)
lclip([(c('v21'), at(21, 'And the neckline') - 0.25)], nx(22))
q('The neckline is<br><i>the whole point</i>', at(21, 'And the neckline') + 0.1, en(21) + 0.3, QL, size=70)
lclip([(c('v22a'), nx(22)), (c('v22b'), at(22, 'A V-neck frames') - 0.2), (c('v22d'), at(22, 'or one fine') - 0.25)], nx(23))
q('A round neck<br><i>hides what&#8217;s underneath</i>', nx(22) + 0.3, at(22, 'A V-neck frames') - 0.3, QL, size=64)
qstack(['A V-neck <i>frames it</i>', 'The collar of a shirt', 'or one fine necklace'], [at(22, 'A V-neck frames'), at(22, 'the collar'), at(22, 'or one fine')],
       at(22, 'That small glimpse') - 0.3, box_=TXL, size=50)
photo('ph_vnt1.jpg', 1280, 150, 560, 707, at(22, 'the top of') - 0.1, nx(23) - 0.1, label='The top of your turtleneck')
q('That small glimpse<br>makes the plainest knit<br><i>look intentional</i>', at(22, 'That small glimpse'), en(22) + 0.3, TXL, size=50)
two(c('v23a'), c('v23b'), nx(23), at(23, 'not a chunky') - 0.15, nx(24), la='A fine knit', lb='Not a chunky one')
lclip([(c('v24a'), nx(24)), (c('v24b'), at(24, 'while a sweater') - 0.2), (c('v24c'), at(24, "You don't need") - 0.2)], nx(25))
q('Read the label<br><i>here too</i>', nx(24) + 0.3, at(24, 'Wool holds') - 0.3, QL, size=68)
photo('ph_lbwool_c.png', 690, 230, 540, 440, at(24, 'Wool holds'), at(24, "You don't need") - 0.25, label='Wool holds its shape')
photo('ph_lbacr_c.png', 1290, 230, 540, 440, at(24, 'mostly acrylic'), at(24, "You don't need") - 0.25, label='Acrylic loses it')
q('You don&#8217;t need cashmere.<br><i>Plain, good-quality wool.</i>', at(24, "You don't need") + 0.2, en(24) + 0.3, QL, size=62)
twoph('ph_vnt2.jpg', 'ph_vskirt.jpg', nx(25) + 0.15, at(25, 'or on its own') - 0.15, en(25) + 0.4, 'Over the turtleneck, with jeans', 'Tucked into a skirt', posb='50% 22%')

# ================= 4. A WOOL BLAZER =================
card_from('4. A Wool Blazer', en(25) + 0.35, en(26) + 0.4)
lclip([(c('b27a'), nx(27)), (c('b27b'), at(27, 'with something soft') - 0.2)], nx(28))
qstack(['Something <i>tailored</i>', 'with something <i>soft</i>'], [at(27, 'something tailored'), at(27, 'with something soft')], at(27, 'That contrast') - 0.3, size=66)
q('Never too sweet,<br><i>never too severe</i>', at(27, 'That contrast') + 0.2, en(27) + 0.3, QL, size=66)
lclip([(c('b28z'), nx(28)), (c('b28a'), at(28, 'forget', end=True) + 0.25), (c('b28b'), at(28, 'When the coat') - 0.2)], nx(29))
q('A job most people forget:<br><i>wear it under your coat</i>', nx(28) + 0.3, at(28, 'When the coat') - 0.3, QL, size=62)
q('The coat comes off.<br><i>You&#8217;re still wearing a jacket.</i>', at(28, 'When the coat') + 0.1, en(28) + 0.3, QL, size=62)
lclip([(c('b29a'), nx(29)), (c('b29b'), at(29, "because that's") - 0.2)], nx(30))
q('Fit the shoulders<br><i>first</i>', nx(29) + 0.3, at(29, 'The seam') - 0.3, QL, size=70)
q('The seam, right at<br><i>the edge of your shoulder</i>', at(29, 'The seam'), at(29, 'Sleeves and') - 0.3, QL, size=62)
q('Sleeves and waist<br><i>are simple to adjust</i>', at(29, 'Sleeves and'), en(29) + 0.3, QL, size=62)
lrow([c('b30a'), c('b30b'), c('b30c')], [nx(30), at(30, 'Wear it over') - 0.1, at(30, 'Or, for something') - 0.1], nx(31))
lab('Covers your hips', 0, nx(30) + 0.45, nx(31) - 0.05)
lab('Over the turtleneck', 1, at(30, 'Wear it over') + 0.35, nx(31) - 0.05)
lab('Belted over a skirt', 2, at(30, 'belt it') - 0.1, nx(31) - 0.05)
lclip([(c('b31'), nx(31))], en(31) + 0.6)
q('A simple blazer<br>that fits your shoulders<br><i>will always look more refined</i>', nx(31) + 0.3, en(31) + 0.3, QL, size=60)

# ================= THE GUIDE =================
cfull([(c('g32'), nx(32)), (c('g33'), nx(33))], en(33) + 0.5)
q('Well-dressed women<br><i>aren&#8217;t guessing.</i>', at(32, "They aren't") - 0.1, en(32) + 0.3, LOW, size=66, cls='over')
q(GUIDE, at(33, 'you can access') - 0.2, en(33) + 0.3, QC, cls='over')

# ================= 5. DARK STRAIGHT-LEG JEANS =================
card_from('5. Dark Straight-Leg Jeans', en(33) + 0.4, en(34) + 0.4, size=100)
lclip([(c('j35'), nx(35))], nx(36))
q('In a deep, even blue,<br><i>as refined as tailored trousers</i>', nx(35) + 0.3, at(35, 'And in winter') - 0.3, QL, size=60)
q('In winter,<br><i>two small details</i>', at(35, 'And in winter'), en(35) + 0.3, QL, size=68)
two(c('j36a'), c('j36b'), nx(36), at(36, 'choose a full') - 0.15, at(36, 'With no bare') - 0.15, la='Cropped, for spring', lb='Full length, for winter',
    tla=at(36, 'Instead of') + 0.1)
lclip([(c('j36c'), at(36, 'With no bare') - 0.1)], nx(37))
q('No bare ankle:<br><i>neater, and warmer</i>', at(36, 'With no bare') + 0.2, en(36) + 0.3, QL, size=66)
lclip([(c('j37a'), nx(37)), (c('j37b'), at(37, 'Dark jeans with') - 0.2)], nx(38))
q('Match your boots<br><i>to your denim</i>', nx(37) + 0.3, at(37, 'Dark jeans with') - 0.3, QL, size=66)
q('One unbroken line,<br><i>and your legs look longer</i>', at(37, 'create one'), en(37) + 0.3, QL, size=64)
lclip([(c('j38a'), nx(38)), (c('j38b'), at(38, 'A pair of') - 0.2), (c('j38c'), at(38, 'Nobody sees') - 0.2)], nx(39))
q('For the coldest days,<br><i>a trick from French winter dressing</i>', nx(38) + 0.3, at(38, 'A pair of') - 0.3, QL, size=58)
q('Thin tights<br><i>under your jeans</i>', at(38, 'A pair of'), at(38, 'Nobody sees') - 0.3, QL, size=70)
q('Nobody sees them.<br><i>You&#8217;ll feel the difference.</i>', at(38, 'Nobody sees'), en(38) + 0.3, QL, size=64)
lclip([(c('j39'), nx(39))], nx(40))
q('You don&#8217;t need<br><i>expensive denim</i>', nx(39) + 0.3, at(39, 'When the colour') - 0.3, QL, size=68)
q('The right colour, the right length:<br><i>wear them anywhere</i>', at(39, 'When the colour'), en(39) + 0.3, QL, size=58)

# ================= 6. A WOOL MIDI SKIRT =================
lclip([(c('s40'), nx(40))], at(40, 'Number six') - 0.35)
q('The piece<br><i>I promised</i>', nx(40) + 0.3, at(40, 'The one most') - 0.3, QL, size=70)
q('The one most of us<br><i>pack away for winter</i>', at(40, 'The one most'), at(40, 'Number six') - 0.5, QL, size=64)
card_from('6. A Wool Midi Skirt', at(40, 'Number six') - 0.45, en(40) + 0.45)
lclip([(c('s41a'), nx(41)), (c('s41b'), at(41, 'But in Parisian') - 0.2), (c('s41c'), at(41, 'The fabric') - 0.2)], nx(42))
q('When it&#8217;s cold, a skirt is<br><i>the last thing you reach for</i>', nx(41) + 0.5, at(41, 'But in Parisian') - 0.3, QL, size=60)
q('In Parisian winter style,<br><i>skirts don&#8217;t disappear</i>', at(41, 'But in Parisian'), at(41, 'The fabric') - 0.3, QL, size=62)
qstack(['The fabric gets <i>heavier</i>', 'What&#8217;s underneath gets <i>warmer</i>'], [at(41, 'The fabric'), at(41, "and what's")], nx(42) - 0.1, size=60)
lclip([(c('s42a'), nx(42)), (c('s42m'), at(42, 'Aim for') - 0.15), (c('s42b'), at(42, 'a soft A-line') - 0.3)], at(43, 'Tuck in') - 0.15)
q('Wool or a wool blend,<br><i>new or secondhand</i>', nx(42) + 0.3, at(42, 'ideally lined') - 0.3, QL, size=62)
photo('ph_lining.png', 980, 190, 560, 620, at(42, 'ideally lined'), at(42, 'Aim for') - 0.25, label='Ideally lined')
qstack(['A hem around <i>mid-calf</i>', 'A soft <i>A-line</i>'], [at(42, 'Aim for') + 0.1, at(42, 'a soft A-line')], nx(43) - 0.1, box_=TXL, size=54)
photo('ph_slit.jpg', 1290, 150, 540, 720, at(42, 'or a straight') - 0.1, nx(43) - 0.1, label='Or straight, with a back slit')
q('Then, two ways<br><i>to wear it</i>', nx(43) + 0.25, at(43, 'Tuck in') - 0.3, QL, size=70)
two(c('s43a'), c('s43b'), at(43, 'Tuck in') - 0.1, at(43, 'Or wear') - 0.15, nx(44), la='The turtleneck, tucked in', lb='Or a sweater, over the top', size=50)
lclip([(c('s44a'), nx(44)), (c('s44b'), at(44, 'And a skirt') - 0.2)], nx(45))
q('Underneath,<br><i>opaque tights keep you warm</i>', nx(44) + 0.3, at(44, 'And a skirt') - 0.3, QL, size=62)
q('A skirt moves<br><i>with a quiet grace</i>', at(44, 'And a skirt'), at(44, 'It makes') - 0.3, QL, size=68)
q('The same sweater,<br><i>a completely different outfit</i>', at(44, 'It makes'), en(44) + 0.3, QL, size=62)

# ================= 7. TALL LEATHER BOOTS =================
lclip([(c('o45'), nx(45))], at(45, 'Number seven') - 0.35)
q('And what you<br><i>wear with it</i>', nx(45) + 0.25, at(45, 'Number seven') - 0.5, QL, size=68)
card_from('7. Tall Leather Boots', at(45, 'Number seven') - 0.45, en(45) + 0.45)
lclip([(c('o46a'), nx(46))], at(46, 'No gap') - 0.15)
q('The detail that makes it<br><i>look so polished</i>', nx(46) + 0.3, at(46, 'The top of') - 0.3, QL, size=62)
q('The top of the boot disappears<br><i>under the hem of the skirt</i>', at(46, 'The top of'), at(46, 'No gap') - 0.3, QL, size=58)
two(c('o46b'), c('o46c'), at(46, 'No gap') - 0.1, at(46, 'Just one line') - 0.15, nx(47), la='A strip of leg', lb='One line, waist to floor')
lclip([(c('o47'), nx(47))], nx(48))
qstack(['Just <i>below your knee</i>', 'Close to your leg', 'A heel <i>you can walk in</i>'], [at(47, 'just below'), at(47, 'with a shaft'), at(47, 'and a heel')], nx(48) - 0.1, size=62)
lclip([(c('o48a'), nx(48)), (c('o48b'), at(48, 'They look like') - 0.2)], nx(49))
q('The same boots,<br><i>worn underneath</i>', nx(48) + 0.3, at(48, 'They look like') - 0.3, QL, size=64)
q('A simple ankle boot,<br><i>with a hidden layer of warmth</i>', at(48, 'They look like'), en(48) + 0.3, QL, size=60)
# the two colours as the boots themselves (the only brown-boot clips left showed bare legs or a man's shoe)
q('Smooth <i>leather</i>', nx(49) + 0.3, at(49, 'because it copes') - 0.35, (260, 24, 1660, 170), size=80)
pieces([('ph_boots2.png', 'Black'), ('ph_bootsbr.png', 'Dark brown')], [at(49, 'black') - 0.15, at(49, 'or dark brown') - 0.05], at(49, 'because it copes') - 0.35,
       x0=330, x1=1590, ybot=900, hh=680, lsize=58)
lclip([(c('o49b'), at(49, 'because it copes') - 0.2), (c('o49c'), at(49, 'And let a cobbler') - 0.2), (c('o49d'), at(49, 'Caring for') - 0.2)], nx(50))
q('It copes with rain<br><i>far better than suede</i>', at(49, 'because it copes'), at(49, 'And let a cobbler') - 0.3, QL, size=62)
q('Let a cobbler<br><i>keep them going for years</i>', at(49, 'And let a cobbler'), at(49, 'Caring for') - 0.3, QL, size=62)
q('Caring for the pieces you own is<br><i>a quiet way of respecting yourself</i>', at(49, 'Caring for'), en(49) + 0.3, QL, size=56)

# ================= 8. LEATHER GLOVES =================
lclip([(c('g50'), nx(50))], at(50, 'Number eight') - 0.35)
q('The smallest piece<br><i>on the list</i>', nx(50) + 0.3, at(50, 'Number eight') - 0.5, QL, size=68)
card_from('8. Leather Gloves', at(50, 'Number eight') - 0.45, en(50) + 0.45)
two(c('g51a'), c('g51b'), nx(51), at(51, 'try a slim') - 0.15, at(51, 'They finish') - 0.15, la='Thick knitted gloves', lb='A slim leather pair')
lphoto('ph_glvcoat.jpg', at(51, 'They finish') - 0.1, nx(52) - 0.05)
q('They finish a coat the way<br><i>jewellery finishes a dress</i>', at(51, 'They finish') + 0.2, en(51) + 0.3, QL, size=60)
lclip([(c('g52a'), nx(52)), (c('g52b'), at(52, 'and long enough') - 0.3)], nx(53))
q('Fit matters<br><i>most</i>', nx(52) + 0.3, at(52, 'Leather gives') - 0.3, QL, size=70)
qstack(['<i>Snug:</i> leather gives a little', 'Long enough to<br><i>slip under your sleeve</i>'], [at(52, 'Leather gives'), at(52, 'and long enough')], at(52, 'A wool or') - 0.3, size=58, rh=190)
photo('ph_glvlin.png', 1000, 150, 520, 640, at(52, 'A wool or'), nx(53) - 0.15, label='A wool or cashmere lining')
q('If they get wet, dry them away from heat', at(52, 'A wool or') + 1.6, nx(53) - 0.15, (PW + 50, 930, 1870, 1030), size=38, dur=1.0)
twoph('ph_glvbag.jpg', 'ph_glvburg.jpg', nx(53) + 0.15, at(53, 'Or let them') - 0.15, nx(54) - 0.05, 'Matched, for a quiet look', 'One touch of colour', posb='50% 60%')
lclip([(c('g54a'), nx(54)), (c('g54b'), at(54, 'So if your') - 0.2)], at(54, 'True elegance') - 0.2)
q('Wearing too much<br><i>at once</i>', nx(54) + 0.4, at(54, 'looking like') - 0.3, QL, size=66)
q('&#8220;Looking like<br><i>a Christmas tree</i>&#8221;', at(54, 'looking like') - 0.1, at(54, 'So if your') - 0.3, QL, size=74)
q('If your gloves are the colour,<br><i>keep your scarf and hat quiet</i>', at(54, 'So if your'), at(54, 'True elegance') - 0.35, QL, size=58)
q('True elegance whispers.<br><i>It doesn&#8217;t shout.</i>', at(54, 'True elegance'), en(54) + 0.45, QC, size=86)

# ================= THE OUTFITS =================
G8 = [('ph_coat.png', 'Long coat'), ('ph_tt.png', 'Turtleneck'), ('ph_vn.png', 'V-neck'), ('ph_blz.png', 'Blazer'),
      ('ph_jeans.png', 'Jeans'), ('ph_skirt.png', 'Midi skirt'), ('ph_boots2.png', 'Tall boots'), ('ph_glove.png', 'Gloves')]
lclip([(c('x55'), nx(55)), (c('x56a'), nx(56)), (c('x56b'), nx(56) + 4.6), (c('x57a'), nx(57)), (c('x57b'), at(57, 'with the jeans') - 0.2),
       (c('x58'), nx(58)), (c('x59'), nx(59))], nx(60))
ids = grid8(G8, [nx(55) + 0.5 + 0.3 * k for k in range(8)], nx(60) - 0.15)
lights(ids, [({2, 3, 5, 7, 1}, nx(56) + 0.25), ({2, 4, 5, 7, 1}, nx(57) + 0.25), ({3, 6, 4, 7, 1, 8}, nx(58) + 0.25), ({2, 3, 6, 7, 1}, nx(59) + 0.25),
             (set(), at(59, 'Every piece') - 0.1)], nx(60))
lab('The market, or a walk', 0, nx(56) + 0.5, nx(57) - 0.2)
lab('Lunch with a friend', 0, nx(57) + 0.5, nx(58) - 0.2)
lab('Dinner', 0, nx(58) + 0.5, nx(59) - 0.2)
lab('And a fourth', 0, nx(59) + 0.5, at(59, 'Every piece') - 0.3)

# ================= RECAP + CLOSE =================
# the eight pieces themselves, each appearing as it is named (no clip can be truer to this line)
q('So, those are <i>our eight</i>', nx(60) + 0.25, at(60, 'A long wool') - 0.35, QC, size=92)
RT_ = [at(60, 'A long wool'), at(60, 'a fine turtleneck'), at(60, 'a V-neck'), at(60, 'a wool blazer'),
       at(60, 'dark straight-leg'), at(60, 'a wool midi'), at(60, 'tall leather'), at(60, 'and leather gloves')]
grid8(G8, RT_, nx(61) - 0.15, x0=130, x1=1790, ytop=44, rowh=506, imh=366)
lclip([(c('r61a'), nx(61)), (c('r61b'), at(61, 'and the confidence') - 0.2)], at(61, 'Elegance was') - 0.2)
qstack(['The care you take<br><i>in choosing them</i>', 'The confidence to wear<br><i>what you love, again and again</i>'],
       [nx(61) + 0.4, at(61, 'and the confidence')], at(61, 'Elegance was') - 0.35, size=58, rh=230)
q('Elegance was never about having more.<br><i>It&#8217;s about choosing with intention.</i>', at(61, 'Elegance was'), en(61) + 0.4, QC, size=70)
lclip([(c('r62'), nx(62))], nx(63))
qstack(['Which of the eight<br><i>do you already own?</i>', 'Which one would you add first?<br><i>Let us know in the comments.</i>'], [nx(62) + 0.3, at(62, 'which one would') - 0.2], en(62) + 0.3, size=58, rh=250)
cfull([(c('r63'), nx(63))], nx(64))
q(GUIDE, at(63, 'our personal') - 0.3, en(63) + 0.3, QC, cls='over')
# the outro runs over one clip, as on the channel
cfull([(c('r64'), nx(64) - 0.25)], total - 3.2)
q('<span style="font-size:58px">Thank you for spending your time with us.</span><br><i style="font-size:70px">A like or comment means the world to us.</i>',
  nx(64) + 0.3, at(65, 'Until') - 0.35, LOW, cls='over')
q('Until next time.<br><i>Bye, my loves.</i>', at(65, 'Until') - 0.05, total - 3.2, LOW, size=70, cls='over')
# every clip once: no clip comes back. One exception, on purpose: two different shots of the same market film, shown one after the other.
_multi = {k: v for k, v in SEGS.items() if len(v) > 1 and k != 'market1'}
assert not _multi, f'clips used more than once: {_multi}'
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
