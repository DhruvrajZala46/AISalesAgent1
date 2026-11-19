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
# The 7 Most Elegant Royal Women Ever, Ranked (The Classy Elegance) - beat map (19 Nov 2026)
# Layouts: only those read off the channel's own videos (VISUAL-EDITING-DNA.md; videos/unforgettable-charm/VISUAL-ANALYSIS.md):
#   full clips (the whole vertical clip over its own blurred copy) | the rule's name on a white card in script |
#   a clip on the caramel with the lesson in white lines beside it, appearing as they are said | rows of clips |
#   a framed clip on cream with the EXACT WORDS in script beside it | two framed pictures under a small label (a comparison) |
#   one sentence alone on the caramel | the NAMED WOMAN shown in real archive film and real press photographs, framed on the
#   caramel with the place and year in script (the channel shows a named woman in photos and archive film: Audrey, Diana, Grace) |
#   the guide over a full clip | the CE logo.
# Sound: the voice and ONE soft solo-piano bed, steady, no ducking, NO sound effects (none are in the channel's measured files).
TRACKS_EDIT = ['gym3e.mp3', 'atreste.mp3']; MUSIC_DB = 13; ENDLOGO = 'logo_ce_dark.png'
MUSIC_CREDIT = 'Music: "Gymnopedie No 3" and "At Rest" by Kevin MacLeod (incompetech.com), licensed under Creative Commons: By Attribution 4.0 (creativecommons.org/licenses/by/4.0/)'
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
# ================= HOOK =================
picfull('pgracewed_24.jpg', 0.0, at(1, 'while most') - 0.1, pos='50% 30%')
q('<i>Grace Kelly, 1956</i>', 1.0, at(1, 'while most') - 0.3, QB, size=60, cls='over')
picfull('pgracewed_16.jpg', at(1, 'while most') - 0.1, nx(2), pos='50% 40%')
q('&#8230;while most outfits from that year<br><i>look like costumes.</i>', at(1, 'while most'), en(1) + 0.3, QC, size=62, cls='over')
pics([P_('pmargbeaton_1', None, '50% 25%'), P_('pqmportrait_41', None, '50% 25%'), P_('pgraceportrait_14', None, '50% 25%')],
     [nx(2), at(2, 'Not because they wore'), at(2, 'Not because they chased')], at(2, 'They simply') - 0.1, h=880, y0=60)
q('They simply <i>chose well.</i>', at(2, 'They simply'), nx(3) - 0.2, QC, size=84)
pics([P_('pmargportrait_9', None, '50% 25%'), P_('pqmportrait_9', None, '50% 25%'), P_('pgraceportrait_41', None, '50% 25%')], [nx(3), at(3, 'sixty'), at(3, 'seventy')], nx(4), h=860, y0=60)
capt('Sixty, seventy, <i>even eighty years later.</i>', at(3, 'sixty'), en(3) + 0.4)
lclip([(c('h4a'), nx(4))], nx(5))
q('That kind of elegance<br><i>isn&#8217;t luck.</i>', st(4), at(4, 'It has almost') - 0.2, QL, size=84)
q('Almost nothing to do<br><i>with a crown,</i>', at(4, 'It has almost'), at(4, 'and everything') - 0.2, QL, size=70)
q('everything to do with<br><i>small choices any woman can make.</i>', at(4, 'and everything'), en(4) + 0.4, QL, size=62)
cfull([(c('h5a'), nx(5))], nx(6))
q('<div><span style="font-size:52px">The 7 Most</span><br><i style="font-size:130px">Elegant Royal Women</i><br><span style="font-size:52px">ranked</span></div>',
  at(5, 'ranking the') - 0.3, en(5) + 0.3, QC, cls='over')
pics([P_('pletportrait_44', None, '50% 15%'), P_('pkatewed_13', None, '50% 20%'), P_('pqueenportrait_12', None, '50% 20%'), P_('pdianavogue_24', None, '50% 20%')],
     [nx(6), at(6, 'You may not'), at(6, 'You may not') + 0.8, at(6, 'And number one')], nx(7) - 0.4, h=780, y0=80)
q('<i>Number one</i> quietly changed royal style forever.', at(6, 'And number one'), en(6) + 0.2, (160, 900, 1760, 1040), size=54)

# ================= 7. PRINCESS MARGARET =================
card_at('7. Princess Margaret', 7, nx(8) - 0.15)
pic('pmargbeaton_4.jpg', 160, 60, 640, 960, nx(8), at(8, 'The photographer') - 0.1, pos='50% 40%')
q('Her 21st birthday, 1951<br><i>a gown by Christian Dior</i>', at(8, 'In 1951'), at(8, 'Cream silk') - 0.2, (900, 60, 1860, 1020), size=62)
q('Cream silk, off the shoulder,<br><i>a full skirt</i>', at(8, 'Cream silk'), at(8, 'The photographer') - 0.2, (900, 60, 1860, 1020), size=62)
picfull('pmargbeaton_39.jpg', at(8, 'The photographer') - 0.1, nx(9), pos='50% 50%')
band('Cecil Beaton&#8217;s birthday portrait, <i>1951</i>', at(8, 'The photographer'), nx(9) - 0.2, size=54)
pics([P_('pmargdress_4', None, '50% 40%'), P_('pmargdress_23', None, '50% 40%')], [nx(9), at(9, 'Today it')], nx(10), h=860, y0=60)
capt('Her favourite dress · <i>today at the London Museum</i>', st(9) + 0.3, nx(10) - 0.2)
pframe([(c('m10a'), nx(10)), (c('m10b'), at(10, 'Will it be comfortable') - 0.1)], nx(11))
pwords(['Dressing for the evening:', '<i>Will it be comfortable?</i>', '<i>Will it be enough?</i>'], [st(10) + 0.2, at(10, 'Will it be comfortable'), at(10, 'Will it be enough')], en(10) + 0.4, size=60)
cfull([(c('m11a'), nx(11)), (c('m11c'), at(11, 'Because what'))], nx(13))
q('Dress for the photograph <i>you&#8217;ll keep.</i>', at(11, 'Elegant women'), at(11, 'For a birthday') - 0.2, QC, size=72, cls='over')
q('One dress, a classic shape,<br><i>a soft colour that won&#8217;t date.</i>', at(11, 'they choose one'), at(11, 'Because what') - 0.2, QC, size=62, cls='over')
q('&#8220;Will I love this photograph<br><i>when I&#8217;m older?&#8221;</i>', at(12, 'will I love'), en(12) + 0.4, QC, size=70, cls='over')
q('Some evenings deserve a dress<br><i>you&#8217;ll want to remember.</i>', st(13), en(13) + 0.4, QC, size=70)

# ================= 6. QUEEN LETIZIA =================
card_at('6. Queen Letizia of Spain', 14, nx(15) - 0.15)
pics([P_('pletvarela_19', None, '50% 20%'), P_('pletvarela_3', None, '50% 20%')], [nx(15), at(15, 'by Felipe')], at(15, 'And she also') - 0.1, h=860, y0=60)
capt('<i>Made-to-measure gowns</i>', at(15, 'made-to-measure'), at(15, 'And she also') - 0.2)
pics([P_('pletmango_1', None, '50% 20%'), P_('pletmango_25', None, '50% 20%'), P_('pletmango_13', None, '50% 20%')],
     [at(15, 'And she also') - 0.1, at(15, 'In 2025'), at(15, 'four times')], nx(16), h=840, y0=60)
capt('The same grey Mango suit · <i>four times in one year</i>', at(15, 'In 2025'), nx(16) - 0.2)
cfull([(c('l16a'), nx(16)), (c('l16b'), at(16, 'A simple dress'))], nx(17))
q('<i>She puts them together.</i>', at(16, 'She puts'), at(16, 'A high-street') - 0.2, QC, size=76, cls='over')
q('A high-street blazer <i>with a beautiful bag</i>', at(16, 'A high-street'), at(16, 'A simple dress') - 0.2, QC, size=60, cls='over')
q('A simple dress <i>with an elegant coat</i>', at(16, 'A simple dress'), en(16) + 0.3, QC, size=60, cls='over')
pframe([(c('l17a'), nx(17))], nx(18))
pwords(['&#8220;Elegance has to be expensive&#8221;', '<i>so you overspend,</i>', '<i>or give up.</i>'], [st(17) + 0.2, at(17, 'so you either'), at(17, 'or give up')], en(17) + 0.4, size=56)
lrow([c('l18a'), c('l18b'), c('l18c')], [at(18, 'A well-made bag'), at(18, 'Leather shoes'), at(18, 'A good coat')], at(18, 'Instead of') - 0.1,
     labels=['<i>a well-made bag</i>', '<i>leather shoes</i>', '<i>a good coat</i>'])
pframe([(c('l18e'), at(18, 'Elegant women') - 0.1)], at(18, 'A well-made bag') - 0.1)
pwords(['Elegant women <i>mix.</i>', 'Classic cuts, quiet colours,', '<i>one good piece to finish.</i>'], [at(18, 'Elegant women'), at(18, 'They choose'), at(18, 'and they let')], at(18, 'A well-made bag') - 0.2, size=58)
cfull([(c('l18d'), at(18, 'Instead of') - 0.1)], nx(19))
q('One special piece,<br><i>simple pieces around it.</i>', at(18, 'Instead of'), en(18) + 0.3, QC, size=66, cls='over')
q('It&#8217;s how well the pieces<br><i>work together.</i>', st(19), en(19) + 0.4, QC, size=72, cls='over')

# ================= 5. THE QUEEN MOTHER =================
card_at('5. The Queen Mother', 20, nx(21) - 0.15)
pic('pqmwhite_2.jpg', 160, 60, 600, 960, nx(21), at(21, 'Then, just before') - 0.1, pos='50% 30%')
q('A state visit to Paris,<br><i>1938</i>', at(21, 'In 1938'), at(21, 'Then, just before') - 0.2, (880, 60, 1860, 1020), size=72)
q('Just before the trip,<br>her mother died.<br><i>The court went into mourning.</i>', at(21, 'Then, just before'), nx(22) - 0.2, QC, size=64)
pic('pqmwhite_3.jpg', 160, 60, 640, 960, nx(22), nx(23), pos='50% 40%', zoom=1.04)
q('Black would have been expected.', st(22) + 0.2, at(22, 'But her') - 0.2, (900, 60, 1860, 1020), size=62)
q('Norman Hartnell<br><i>remade her wardrobe in white.</i>', at(22, 'But her'), nx(23) - 0.2, (900, 60, 1860, 1020), size=64)
pics([P_('pqmwhite_19', None, '50% 25%'), P_('pqmwhite_32', None, '50% 25%'), P_('pqmwhite_0', None, '50% 40%')], [nx(23), at(23, 'dressed entirely'), at(23, 'enchanted')], nx(24), h=860, y0=60)
capt('<i>Dressed entirely in white</i>', st(23) + 0.3, nx(24) - 0.2)
pframe([(c('q24a'), nx(24))], nx(25))
pwords(['We reach for black.', 'Beautiful, but some days', '<i>it feels heavy,</i>', '<i>near the face.</i>'], [st(24) + 0.2, at(24, 'but on some'), at(24, 'it can feel'), at(24, 'especially near')], en(24) + 0.4, size=58, rh=150)
cfull([(c('q25a'), nx(25)), (c('q25b'), at(25, 'Try it')), (c('q25c'), at(25, 'or a white'))], nx(26))
q('Ivory · <i>cream</i> · soft white', at(25, 'Ivory'), at(25, 'look fresh') - 0.2, QC, size=72, cls='over')
q('Fresh and calm,<br><i>they brighten the skin.</i>', at(25, 'look fresh'), at(25, 'Try it') - 0.2, QC, size=66, cls='over')
q('A cream knit <i>with ivory trousers</i>', at(25, 'a cream knit'), at(25, 'or a white') - 0.2, QC, size=60, cls='over')
q('A white shirt <i>under a camel coat</i>', at(25, 'or a white'), en(25) + 0.3, QC, size=60, cls='over')
q('The softest colour in the room<br><i>is the one people remember.</i>', st(26), en(26) + 0.4, QC, size=66)

# ================= GUIDE =================
cfull([(c('g27a'), nx(27)), (c('g27b'), at(27, 'Our personal'))], nx(28) - 0.2)
q('Your shades · <i>your shapes</i> · your hairstyles', at(27, 'which shades'), at(27, 'Our personal') - 0.3, QC, size=56, cls='over')
q(GUIDE, at(27, 'personal stylist guide') - 0.3, nx(28) - 0.3, QC, cls='over')

# ================= 4. CATHERINE =================
card_at('4. Catherine, Princess of Wales', 28, nx(29) - 0.15)
pic('psledge_8.jpg', 160, 60, 340, 960, nx(29), at(29, 'It became') - 0.1, pos='50% 40%')
prod('psledge_1.png', 1300, 900, 560, at(29, 'a nude court'), at(29, 'It became') - 0.1, label='<i>L.K. Bennett &#8220;Sledge&#8221;</i>', maxw=720)
pics([P_('psledge_33', None, '50% 50%'), P_('psledge_15', None, '50% 50%')], [at(29, 'It became'), at(29, 'early years')], nx(30), h=760, y0=80)
capt('Her signature, <i>2011-2014</i>', at(29, 'It became'), nx(30) - 0.2)
cfull([(c('k30a'), nx(30))], at(30, 'And a shoe') - 0.1)
pic('psledge_36.jpg', 160, 60, 362, 960, at(30, 'And a shoe') - 0.1, nx(31), pos='50% 50%')
q('A shoe close to<br><i>the colour of her skin</i>', at(30, 'And a shoe'), at(30, 'made her look') - 0.2, (760, 60, 1860, 1020), size=64)
q('Taller, <i>without a single extra inch.</i>', at(30, 'made her look'), en(30) + 0.3, (760, 60, 1860, 1020), size=64)
pframe([(c('k31a'), nx(31))], nx(32))
pwords(['The perfect dress,', 'and nothing in your shoe rack', '<i>seems to go with it.</i>'], [st(31) + 0.2, at(31, 'and then nothing'), at(31, 'seems to go')], en(31) + 0.4, size=56)
cfull([(c('k32a'), nx(32)), (c('k32b'), at(32, 'Because when'))], nx(33))
q('One pair <i>in your own skin tone.</i>', at(32, 'Elegant women'), at(32, 'Because when') - 0.2, QC, size=66, cls='over')
q('The eye sees <i>one long line.</i>', at(32, 'the eye sees'), at(32, 'Look for') - 0.2, QC, size=70, cls='over')
q('A soft point or almond toe,<br><i>a heel you can walk in.</i>', at(32, 'Look for'), en(32) + 0.3, QC, size=60, cls='over')
q('The most elegant shoe<br><i>is the one nobody notices.</i>', st(33), en(33) + 0.4, QC, size=70)

# ================= 3. QUEEN ELIZABETH II =================
card_at('3. Queen Elizabeth II', 34, nx(35) - 0.15)
pics([P_('pqueencolour_22', None, '50% 20%'), P_('pqueencolour_32', None, '50% 25%'), P_('pqueencolour_40', None, '50% 20%')],
     [nx(35), at(35, 'Lime'), at(35, 'Fuchsia')], at(35, 'And there') - 0.1, h=860, y0=60,)
capt('Cobalt blue · <i>lime green</i> · fuchsia pink', at(35, 'Cobalt'), at(35, 'And there') - 0.2)
cfull([(c('e35a'), at(35, 'And there') - 0.1)], nx(36))
picfull('pqueencolour_9.jpg', nx(36), at(36, 'Her biographer') - 0.1, pos='50% 40%')
band('&#8220;She needs to stand out, <i>for people to say, I saw the Queen.&#8221;</i>', at(36, 'she needs'), at(36, 'Her biographer') - 0.2, size=50)
picfull('pqueencolour_33.jpg', at(36, 'Her biographer') - 0.1, nx(37), pos='50% 25%')
band('&#8220;I can never wear beige&#8230;&#8221;', at(36, 'she could never'), nx(37) - 0.2, size=60)
pframe([(c('e37a'), nx(37))], nx(38))
pwords(['Hiding in neutrals,', '<i>especially as the years go by.</i>'], [st(37) + 0.2, at(37, 'especially')], en(37) + 0.4, size=58)
cfull([(c('e38a'), nx(38)), (c('e38b'), at(38, 'Choose one')), (c('e38d'), at(38, 'an emerald') - 0.1), (c('e38c'), at(38, 'and wear it'))], nx(39))
q('<i>Elegant women aren&#8217;t afraid to be seen.</i>', at(38, 'Elegant women'), at(38, 'One clear') - 0.2, QC, size=64, cls='over')
q('One clear colour says<br><i>you came on purpose.</i>', at(38, 'One clear'), at(38, 'Choose one') - 0.2, QC, size=66, cls='over')
q('A deep blue · <i>a soft red</i> · an emerald green', at(38, 'a deep blue'), at(38, 'and wear it') - 0.2, QC, size=58, cls='over')
q('One bigger piece.<br><i>Everything else simple.</i>', at(38, 'and wear it'), en(38) + 0.3, QC, size=64, cls='over')
q('Being seen isn&#8217;t loud.<br><i>It&#8217;s simply being present.</i>', st(39), en(39) + 0.4, QC, size=70)

# ================= 2. PRINCESS DIANA =================
card_at('2. Princess Diana', 40, nx(41) - 0.15)
cfull([(c('d41a'), nx(41))], at(41, 'She agreed') - 0.1)
q('British Vogue, 1990 · <i>with Sam McKnight</i>', at(41, 'In 1990'), at(41, 'At the end') - 0.2, QB, size=54, cls='over')
q('&#8220;What would you do<br><i>with my hair?&#8221;</i>', at(41, 'she asked'), at(41, 'He said') - 0.2, QC, size=72, cls='over')
q('&#8220;Cut it short.&#8221;', at(41, 'He said'), at(41, 'She agreed') - 0.2, QC, size=84, cls='over')
pics([P_('pdianashort_24', None, '50% 25%'), P_('pdianashort_11', None, '50% 25%'), P_('pdianashort_46', None, '50% 20%')],
     [at(41, 'She agreed') - 0.1, nx(42), at(42, 'Diana later')], at(42, 'it let out') - 0.1, h=860, y0=60)
capt('<i>She agreed.</i>', at(41, 'She agreed'), nx(42) - 0.2)
pic('pdianashort_39.jpg', 160, 60, 600, 960, at(42, 'it let out') - 0.1, nx(43), pos='50% 30%')
q('&#8220;It let out something<br><i>quite different.&#8221;</i>', at(42, 'it let out'), nx(43) - 0.2, (880, 60, 1860, 1020), size=68)
pframe([(c('d43a'), nx(43))], nx(44))
pwords(['The same hairstyle for years.', 'It suited us once,', '<i>and we&#8217;re afraid to change it.</i>'], [st(43) + 0.2, at(43, 'It suited'), at(43, 'and we')], en(43) + 0.4, size=56)
cfull([(c('d44a'), nx(44)), (c('d44b'), at(44, 'At your next')), (c('d44c'), at(44, 'Then listen'))], nx(45))
q('Hair chosen for the face <i>you have now.</i>', at(44, 'chosen for'), at(44, 'At your next') - 0.2, QC, size=64, cls='over')
q('&#8220;If you could do anything with my hair,<br><i>what would you do?&#8221;</i>', at(44, 'if you could'), at(44, 'Then listen') - 0.2, QC, size=56, cls='over')
q('Then listen.', at(44, 'Then listen'), en(44) + 0.3, QC, size=84, cls='over')
cfull([(c('d45a'), nx(45))], nx(46) - 0.4)
q('It makes you look<br><i>like yourself.</i>', at(45, 'It makes you'), en(45) + 0.4, QC, size=76, cls='over')

# ================= 1. GRACE KELLY =================
card_at('1. Grace Kelly', 46, nx(47) - 0.15)
cfull([(c('g47a'), nx(47))], at(47, 'Her wedding') - 0.1)
q('Monaco, <i>April 1956</i>', at(47, 'In April'), at(47, 'Her wedding') - 0.2, QB, size=60, cls='over')
pic('pgracewed_12.jpg', 160, 60, 620, 960, at(47, 'Her wedding') - 0.1, nx(48), pos='50% 30%')
q('Made by Helen Rose of MGM,<br><i>a gift from the studio</i>', at(47, 'Her wedding'), nx(48) - 0.2, (880, 60, 1860, 1020), size=60)
pics([P_('pgracewed_46', None, '50% 25%'), P_('pgracewed_28', None, '50% 30%')], [nx(48), at(48, 'It covered')], at(48, 'Fifty-five') - 0.1, h=860, y0=60)
capt('A high lace neckline · <i>long lace sleeves</i>', at(48, 'It had'), at(48, 'Fifty-five') - 0.2)
pics([P_('pgracewed_21', None, '50% 25%'), P_('pkatewed_30', None, '50% 25%')], [at(48, 'Fifty-five') - 0.1, at(48, 'Catherine')], nx(49), h=860, y0=60)
capt('1956 · <i>2011</i>', at(48, 'Catherine'), nx(49) - 0.2)
pframe([(c('c49a'), nx(49))], nx(50))
pwords(['To look beautiful,', 'we think we need to show more.', '<i>Lower, shorter, tighter.</i>'], [st(49) + 0.2, at(49, 'we need'), at(49, 'Lower')], en(49) + 0.4, size=56)
cfull([(c('c50a'), nx(50)), (c('c50c'), at(50, 'a hem below') - 0.1), (c('c50b'), at(50, 'For your next'))], nx(51))
q('Covering a little more<br><i>often looks more beautiful.</i>', at(50, 'Elegant women'), at(50, 'A high neckline') - 0.2, QC, size=64, cls='over')
q('A high neckline · <i>a sleeve</i> · a hem below the knee', at(50, 'A high neckline'), at(50, 'For your next') - 0.2, QC, size=56, cls='over')
q('One covered element.<br><i>Everything else quiet.</i>', at(50, 'For your next'), en(50) + 0.3, QC, size=64, cls='over')
cfull([(c('c51a'), nx(51))], nx(52) - 0.4)
q('True elegance doesn&#8217;t ask to be looked at.<br><i>It simply is.</i>', st(51), en(51) + 0.4, QC, size=60, cls='over')

# ================= CLOSE =================
lclip([(c('z52a'), nx(52))], at(52, 'Seven royal') - 0.1)
qstack(['A dress for the photograph.', 'One good piece among simple ones.', 'The beauty of white.', 'A shoe in your own skin tone.'],
       [at(52, 'A dress for'), at(52, 'One good piece'), at(52, 'The beauty'), at(52, 'A shoe in')], at(52, 'One clear') - 0.1, size=54, rh=130)
qstack(['One clear colour.', 'A haircut for the woman you are now.', '<i>And the elegance of covering more.</i>'],
       [at(52, 'One clear'), at(52, 'A haircut'), at(52, 'And the elegance')], at(52, 'Seven royal') - 0.1, size=54, rh=130)
pics([P_('pmargbeaton_8', None, '50% 20%'), P_('pletportrait_25', None, '50% 15%'), P_('pqmportrait_26', None, '50% 20%'), P_('pkatewed_12', None, '50% 20%'),
      P_('pqueenportrait_23', None, '50% 15%'), P_('pdianavogue_36', None, '50% 20%'), P_('pgraceportrait_4', None, '50% 20%')],
     [at(52, 'Seven royal') + k * 0.35 for k in range(7)], nx(53), h=560, y0=150)
capt('Not one of their lessons <i>needs a crown.</i>', at(52, 'and not one'), nx(53) - 0.2)
cfull([(c('z53a'), nx(53))], nx(54))
q('Who is <i>your</i> number one?', st(53), en(53) + 0.3, QC, size=84, cls='over')
cfull([(c('z54a'), nx(54)), (c('z54b'), at(54, 'And if')), (c('z54c'), at(54, 'Until next') - 0.1)], total - 3.0)
q(GUIDE, at(54, 'personal stylist guide') - 0.3, at(54, 'Until next time') + 0.6, QC, cls='over')
