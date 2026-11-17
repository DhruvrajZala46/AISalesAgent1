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
# Princess Diana's 8 Timeless Style Rules (The Classy Elegance) - beat map (17 Nov 2026)
# Layouts: only those read off the channel's own videos (VISUAL-EDITING-DNA.md; videos/unforgettable-charm/VISUAL-ANALYSIS.md):
#   full clips (the whole vertical clip over its own blurred copy) | the rule's name on a white card in script |
#   a clip on the caramel with the lesson in white lines beside it, appearing as they are said | rows of clips |
#   a framed clip on cream with the EXACT WORDS in script beside it | two framed pictures under a small label (a comparison) |
#   one sentence alone on the caramel | the NAMED WOMAN shown in real archive film and real press photographs, framed on the
#   caramel with the place and year in script (the channel shows a named woman in photos and archive film: Audrey, Diana, Grace) |
#   the guide over a full clip | the CE logo.
# Sound: the voice and ONE soft solo-piano bed, steady, no ducking, NO sound effects (none are in the channel's measured files).
TRACKS_EDIT = ['m683n.mp3']; MUSIC_DB = 15; ENDLOGO = 'logo_ce_dark.png'
MUSIC_CREDIT = 'Music: "Classical vibes 3" by Grigoriy Nuzhny (Mixkit, free license)'
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
cfull([(c('h1a'), 0.0), (c('h1b'), at(1, 'When you get'))], nx(2))
q('Are your clothes saying<br><i>what you want them to say?</i>', at(1, 'are your clothes'), en(1) + 0.3, QC, size=78, cls='over')
lrow([c('h2a'), c('h2b')], [nx(2), at(2, 'to be looked')], at(2, 'Almost no one') - 0.1)
q('Most of us dress<br><i>to be looked at.</i>', nx(2) + 0.3, at(2, 'Almost no one') - 0.2, R3, size=66)
lclip([(c('h2c'), at(2, 'Almost no one') - 0.2)], at(2, "And that's why") - 0.1)
q('Almost no one dresses<br><i>to be close to people.</i>', at(2, 'Almost no one'), at(2, "And that's why") - 0.2, QL, size=70)
cfull([(c('h2d'), at(2, "And that's why") - 0.2)], nx(3))
q('Admired for a second,<br><i>forgotten by dinner.</i>', at(2, 'admired'), en(2) + 0.3, QC, size=80, cls='over')
cfull([(c('h3a'), nx(3)), (c('h3b'), at(3, 'Not because')), (c('h3c'), at(3, 'Because every')), (c('h3d'), at(3, 'You know'))], nx(4))
band('Almost thirty years later,<br><i>people still talk about her clothes.</i>', at(3, 'whose clothes'), at(3, 'Not because') - 0.2, size=58)
band('Not the most expensive.', at(3, 'Not because'), at(3, 'Because every') - 0.2, size=64)
band('<i>Every outfit said something.</i>', at(3, 'Because every'), at(3, 'You know') - 0.2, size=84)
cfull([(c('h4a'), nx(4))], nx(5) + 0.4)
band('<i>Princess Diana</i>', st(4) - 0.1, st(5) + 0.2, size=120)
pframe([(c('h5a'), nx(5) + 0.3), (c('h5b'), at(5, 'How will people') - 0.4)], at(5, "Because that's") - 0.1)
pwords(['The real question is not', '<i>&#8220;Do I look good?&#8221;</i>'], [st(5) + 0.5, at(5, 'Do I look')], at(5, 'How will people') - 0.6, size=62)
pwords(['The real question is', '<i>&#8220;How will people feel</i>', '<i>when I walk in?&#8221;</i>'], [at(5, 'How will people') - 0.4, at(5, 'How will people'), at(5, 'when I walk')],
       at(5, "Because that's") - 0.2, size=62)
lclip([(c('h5c'), at(5, "Because that's") - 0.2), (c('h5d'), at(5, "It's the message"))], en_(5))
q('That&#8217;s what style<br><i>actually is.</i>', at(5, "Because that's"), at(5, "It isn't a label") - 0.2, QL, size=72)
qstack(['It isn&#8217;t a label.', '<i>It isn&#8217;t a trend.</i>'], [at(5, "It isn't a label"), at(5, "It isn't a trend")], at(5, "It's the message") - 0.2, size=74)
q('It&#8217;s the message your clothes give<br><i>to the people in front of you.</i>', at(5, "It's the message"), at(5, 'And almost nobody') - 0.2, QL, size=56)
q('And almost nobody<br><i>teaches this.</i>', at(5, 'And almost nobody'), en(5) + 0.4, QL, size=74)
cfull([(c('h6a'), nx(6))], at(6, 'in a way') - 0.1)
band('&#8220;The most photographed woman<br><i>in the world&#8221;</i>', at(6, 'often called'), at(6, 'in a way') - 0.2, size=60)
lrow([c('h6c'), c('h6d'), c('h6e')], [at(6, 'in a way') - 0.2, at(6, 'a little surprising'), at(6, 'and easy to wear')], at(6, 'By the end') - 0.1,
     labels=['practical', 'a little surprising', 'any age, any budget'])
pics([P_('pnineties_19'), P_('pnineties_32'), P_('pnineties_11')], [at(6, 'By the end') - 0.2, at(6, 'exactly why'), at(6, 'still feel')], at(6, 'and how to use') - 0.1, h=820, y0=50)
capt('Why her clothes still feel <i>timeless</i>', at(6, 'exactly why'), at(6, 'and how to use') - 0.2)
lclip([(c('h6f'), at(6, 'and how to use') - 0.2)], en_(6))
q('The same rules,<br><i>without spending more,</i><br>or dressing like a royal', at(6, 'and how to use'), en(6) + 0.4, QL, size=62)
cfull([(c('h7a'), nx(7)), (c('h7b'), at(7, 'And the last one')), (c('h7c'), at(7, "And if you'd"))], en(7) + 0.35)
q('<div><span style="font-size:54px">Princess Diana&#8217;s</span><br><i style="font-size:118px">8 Timeless Style Rules</i></div>',
  at(7, 'eight rules') - 0.4, at(7, 'And the last one') - 0.2, QC, cls='over')
q('The last one changes<br><i>how you walk into any room.</i>', at(7, 'And the last one'), at(7, "And if you'd") - 0.2, QC, size=70, cls='over')
q(GUIDE, at(7, 'our personal stylist') - 0.3, en(7) + 0.2, QC, cls='over')

# ================= WHAT STYLE IS =================
lclip([(c('d8a'), nx(8)), (c('d8a2'), at(8, "That's a costume") - 0.1)], at(8, 'Real style') - 0.1)
q('Elegance isn&#8217;t wearing<br><i>the most beautiful dress in the room.</i>', at(8, "Elegance isn't"), at(8, "That's a costume") - 0.2, QL, size=58)
q('That&#8217;s<br><i>a costume.</i>', at(8, "That's a costume"), at(8, 'Real style') - 0.2, QL, size=96)
q('Real style is when your clothes<br><i>make other people feel something.</i>', at(8, 'Real style'), at(8, 'Welcome') - 0.2, QC, size=68)
lrow([c('d8b'), c('d8c'), c('d8d')], [at(8, 'Welcome') - 0.2, at(8, 'Calm'), at(8, 'Respected')], at(9, "You don't remember") - 0.3, labels=['welcome', 'calm', 'respected'])
cfull([(c('d9a'), at(9, "You don't remember") - 0.2), (c('d9b'), at(9, 'But you remember'))], en_(9))
q('You don&#8217;t remember<br><i>what most people wore last week.</i>', at(9, "You don't remember"), at(9, 'But you remember') - 0.2, QC, size=66, cls='over')
q('But you remember the woman<br><i>whose outfit fitted the moment.</i>', at(9, 'But you remember'), en(9) + 0.4, QC, size=66, cls='over')
cfull([(c('d10a'), nx(10))], en(10) + 0.7)
band('A rule for almost<br><i>every moment of her day</i>', at(10, 'And she had'), en(10) + 0.5, size=64)

# ================= 1. DRESS FOR THE PEOPLE YOU'RE ABOUT TO MEET =================
card_at('1. Dress for the People You&#8217;re About to Meet', 11, at(11, 'Most of us') - 0.15, size=88)
pframe([(c('r1a'), at(11, 'Most of us') - 0.2)], at(11, 'Diana asked') - 0.1)
pwords(['Most of us ask:', '<i>&#8220;What do I feel like wearing?&#8221;</i>'], [at(11, 'Most of us'), at(11, 'What do I')], at(11, 'Diana asked') - 0.2, size=56)
pic('pnohat_3.jpg', 170, 70, 632, 940, at(11, 'Diana asked') - 0.2, en_(11), pos='50% 30%')
qstack(['Diana asked:', '<i>&#8220;Who am I</i>', '<i>going to see?&#8221;</i>'], [at(11, 'Diana asked'), at(11, 'Who am I'), at(11, 'going to see')], en(11) + 0.4, box_=(860, 60, 1850, 1020), size=72, rh=160)
pics([P_('pcaring_28'), P_('pcaring_2')], [nx(12), at(12, 'one cheerful')], at(12, 'With it') - 0.15, h=880, y0=100, x0=40, x1=1250)
q('Visiting children<br><i>in hospital</i>', nx(12) + 0.3, at(12, 'one cheerful') + 1.6, RT, size=58)
q('One cheerful,<br><i>brightly patterned dress</i>', at(12, 'one cheerful') + 1.8, at(12, 'so often') + 0.9, RT, size=54)
q('Her<br><i>&#8220;caring dress&#8221;</i>', at(12, 'it became known'), at(12, 'With it') - 0.25, RT, size=84)
pic('pnohat_20.jpg', 70, 150, 1040, 780, at(12, 'With it') - 0.15, at(12, 'as a Kensington') - 0.1, pos='50% 40%')
q('With it:<br><i>big costume jewellery</i>', at(12, 'With it') + 0.1, at(12, 'as a Kensington') - 0.2, (1150, 60, 1890, 1020), size=62)
pic('pnohat_2.jpg', 150, 70, 752, 940, at(12, 'as a Kensington') - 0.1, en_(12), pos='50% 30%')
q('She picked children up,<br><i>and they played with it.</i>', at(12, 'she would pick'), en(12) + 0.4, (950, 250, 1880, 700), size=60)
q('as a Kensington Palace curator explained', at(12, 'as a Kensington') + 0.2, en(12) + 0.4, (950, 700, 1880, 800), size=34)
pframe([(c('r1b'), nx(13))], at(13, 'Visiting your') - 0.1)
pwords(['Ask one question first:', '<i>&#8220;Who will I see today,</i>', '<i>and what would make them</i>', '<i>feel at ease?&#8221;</i>'],
       [at(13, 'ask one question'), at(13, 'Who will I'), at(13, 'and what would'), at(13, 'feel at ease')], at(13, 'Visiting your') - 0.2, size=58, rh=150)
lclip([(c('r1c'), at(13, 'Visiting your') - 0.2)], at(13, 'try a soft blue') - 0.1)
q('Visiting your mother<br><i>or your grandmother?</i>', at(13, 'Visiting your'), at(13, 'Instead of') - 0.2, QL, size=66)
q('Instead of<br><i>something stiff&#8230;</i>', at(13, 'Instead of'), at(13, 'try a soft blue') - 0.2, QL, size=76)
lrow([c('r1d'), c('r1e'), c('r1f')], [at(13, 'try a soft blue') - 0.2, at(13, 'or a warm rose'), at(13, 'and a brooch')], at(13, 'A friend') - 0.1,
     labels=['a soft blue', 'a warm rose', 'a brooch to look at'])
lclip([(c('r1g'), at(13, 'A friend') - 0.2), (c('r1h'), at(13, 'Something warm'))], at(13, 'Your clothes become') - 0.1)
q('A friend who&#8217;s had<br><i>a hard week?</i>', at(13, 'A friend'), at(13, 'Something warm') - 0.2, QL, size=70)
q('Something warm,<br><i>simple and unfussy</i>', at(13, 'Something warm'), at(13, 'Your clothes become') - 0.2, QL, size=70)
cfull([(c('r1i'), at(13, 'Your clothes become') - 0.2)], en_(13))
q('Your clothes become a welcome<br><i>before you even say hello.</i>', at(13, 'Your clothes become'), en(13) + 0.4, QC, size=68, cls='over')

# ================= 2. NEVER LET YOUR CLOTHES BECOME A BARRIER =================
card_at('2. Never Let Your Clothes Become a Barrier', 14, en(14) + 0.3, size=92)
pics([P_('phats_7', pos='50% 20%'), P_('phats_0', pos='50% 20%'), P_('phats_2', pos='50% 20%')], [nx(15), st(15) + 1.0, st(15) + 2.0], at(15, 'But on visits') - 0.15, h=800, y0=50)
capt('On royal occasions, <i>a hat was expected.</i>', st(15) + 0.4, at(15, 'But on visits') - 0.25)
pics([P_('pnohat_11'), P_('pnohat_17', pos='50% 25%')], [at(15, 'But on visits') - 0.15, at(15, 'Diana left')], at(15, 'Her reason') - 0.15, h=900, y0=90, x0=40, x1=1330)
q('With children,<br><i>the hat stayed off.</i>', at(15, 'Diana left'), at(15, 'Her reason') - 0.25, (1330, 60, 1890, 1020), size=58)
pic('pnohat_23.jpg', 150, 70, 743, 940, at(15, 'Her reason') - 0.15, en_(15), pos='50% 30%')
q('&#8220;You can&#8217;t cuddle a child<br><i>in a hat.&#8221;</i>', at(15, "You can't cuddle") - 0.1, en(15) + 0.4, (950, 250, 1880, 700), size=68)
q('her reason, as the palace curator tells it', at(15, 'Her reason'), en(15) + 0.4, (950, 700, 1880, 800), size=34)
pic('paids_0.jpg', 110, 60, 700, 700, nx(16), en_(16), pos='50% 50%')
pic('paids_1.jpg', 1010, 50, 575, 880, at(16, 'she shook') - 0.2, en_(16), label='Middlesex Hospital, London', pos='50% 40%', lsize=46)
q('<i>April 1987</i>', nx(16) + 0.4, at(16, 'she shook') - 0.3, (60, 790, 860, 1040), size=92)
q('She shook the patients&#8217; hands<br><i>without gloves.</i>', at(16, 'she shook'), at(16, 'That photograph') - 0.2, (60, 790, 860, 1040), size=50)
q('That photograph<br><i>travelled around the world.</i>', at(16, 'That photograph'), en(16) + 0.4, (60, 790, 860, 1040), size=52)
lclip([(c('r2a'), nx(17)), (c('r2a2'), at(17, "It's armour") - 0.1)], at(17, "if you can't hug") - 0.1)
q('Elegance that keeps people<br>at a distance<br><i>isn&#8217;t elegance.</i>', at(17, 'Elegance that'), at(17, "It's armour") - 0.2, QL, size=62)
q('It&#8217;s<br><i>armour.</i>', at(17, "It's armour"), at(17, "if you can't hug") - 0.2, QL, size=104)
lrow([c('r2b'), c('r2c'), c('r2d')], [at(17, "if you can't hug") - 0.2, at(17, 'sit down with'), at(17, 'or reach for')], at(17, "it isn't the right") - 0.1,
     labels=['hug someone', 'sit down with a child', 'reach for a hand'])
q('It isn&#8217;t the right outfit<br><i>for that day.</i>', at(17, "it isn't the right"), en(17) + 0.5, QC, size=80)

# ================= 3. HONOUR YOUR HOST =================
card_at('3. Honour Your Host', 18, en(18) + 0.3, size=120)
pics([P_('pjapan_0', pos='50% 20%'), P_('pjapan_1', pos='50% 20%')], [nx(19), at(19, 'a white outfit')], at(19, "She didn't say") - 0.15, h=880, y0=100, x0=40, x1=1250)
q('<i>Japan, 1986</i>', nx(19) + 0.4, at(19, 'a white outfit') + 1.0, RT, size=84)
q('White, with large<br><i>red polka dots</i>', at(19, 'a white outfit') + 1.2, at(19, 'a quiet echo') - 0.2, RT, size=58)
q('A quiet echo<br><i>of the Japanese flag</i>', at(19, 'a quiet echo'), at(19, "She didn't say") - 0.25, RT, size=58)
pic('pjapan_11.jpg', 110, 110, 905, 860, at(19, "She didn't say") - 0.15, en_(19), pos='50% 40%')
q('She didn&#8217;t say<br>a word about it.', at(19, "She didn't say"), at(19, 'The outfit said') - 0.2, (1080, 60, 1890, 1020), size=60)
q('The outfit said it for her:<br><i>&#8220;I thought about you.&#8221;</i>', at(19, 'The outfit said'), en(19) + 0.4, (1080, 60, 1890, 1020), size=58)
lrow([c('r3a'), c('r3b')], [nx(20), at(20, 'and leave white') - 0.2], at(20, 'Invited to dinner') - 0.1)
q('You can do this<br><i>in a much smaller way.</i>', nx(20) + 0.3, at(20, 'Going to') - 0.2, R3, size=54)
q('A friend&#8217;s wedding?<br><i>Ask about the colours<br>of the day.</i>', at(20, 'Going to'), at(20, 'and leave white') - 0.2, R3, size=56)
q('Leave white and ivory<br><i>to the bride.</i>', at(20, 'and leave white'), at(20, 'Invited to dinner') - 0.2, R3, size=60)
pframe([(c('r3c'), at(20, 'Invited to dinner') - 0.2), (c('r3d'), at(20, 'It tells your host'))], at(20, 'Your outfit becomes') - 0.1)
pwords(['Invited to dinner?', 'Dress one step more carefully', 'than you need to.'], [at(20, 'Invited to dinner'), at(20, 'Dress one step'), at(20, 'than you need')], at(20, 'It tells your host') - 0.2, size=58)
pwords(['It tells your host:', '<i>&#8220;This evening</i>', '<i>matters to me.&#8221;</i>'], [at(20, 'It tells your host'), at(20, 'This evening'), at(20, 'matters to me')], at(20, 'Your outfit becomes') - 0.2, size=66)
cfull([(c('r3e'), at(20, 'Your outfit becomes') - 0.2)], en_(20))
q('Your outfit becomes<br><i>a gift.</i>', at(20, 'Your outfit becomes'), en(20) + 0.5, QC, size=92, cls='over')

# ================= 4. PLAN FOR THE AWKWARD MOMENT =================
card_at('4. Plan for the Awkward Moment', 21, en(21) + 0.3, size=104)
cfull([(c('r4a'), nx(22)), (c('r4b'), st(22) + 2.4)], at(22, 'So in low-cut') - 0.1)
band('Photographed stepping out of cars,<br><i>constantly</i>', st(22) + 0.4, at(22, 'So in low-cut') - 0.2, size=58)
pics([P_('pclutchb_0', pos='50% 30%'), P_('pclutchb_1', pos='50% 25%'), P_('pclutchb_2', pos='50% 30%')],
     [at(22, 'So in low-cut') - 0.15, at(22, 'she held'), at(22, 'close to her chest')], at(22, 'Her handbag') - 0.15, h=840, y0=40)
capt('A small clutch bag, <i>held close to her chest</i>', at(22, 'she held'), at(22, 'Her handbag') - 0.25)
pic('pclutchb_5.jpg', 170, 70, 627, 940, at(22, 'Her handbag') - 0.15, en_(22), pos='50% 30%')
q('She called them her<br><i>&#8220;cleavage bags&#8221;.</i>', at(22, 'Diana called') - 0.1, en(22) + 0.4, (860, 250, 1870, 700), size=72)
q('as her handbag designer later said', at(22, 'Her handbag'), en(22) + 0.4, (860, 700, 1870, 800), size=34)
lclip([(c('r4c'), nx(23))], at(23, 'Before you leave') - 0.1)
q('Elegance isn&#8217;t<br>only the outfit.', nx(23) + 0.2, at(23, "It's thinking") - 0.2, QL, size=70)
q('It&#8217;s thinking<br><i>one step ahead.</i>', at(23, "It's thinking"), at(23, 'Before you leave') - 0.2, QL, size=84)
pframe([(c('r4d'), at(23, 'Before you leave') - 0.2), (c('r4e'), at(23, 'Lift your arms') - 0.1), (c('r4f'), at(23, 'Walk up') - 0.1)], at(23, 'If the skirt') - 0.1)
pwords(['Before you leave the house:', '<i>Sit down in it.</i>', '<i>Bend.</i>', '<i>Lift your arms.</i>', '<i>Walk up a stair.</i>'],
       [at(23, 'Before you leave'), at(23, 'sit down in'), at(23, 'Bend'), at(23, 'Lift your arms'), at(23, 'Walk up')], at(23, 'If the skirt') - 0.2, size=60, rh=140)
lclip([(c('r4g'), at(23, 'If the skirt') - 0.2)], en_(23))
q('If the skirt rides up<br>or the neckline gapes&#8230;', at(23, 'If the skirt'), at(23, "you'll know") - 0.2, QL, size=60)
q('You&#8217;ll know<br><i>before anyone else does.</i>', at(23, "you'll know"), en(23) + 0.4, QL, size=70)

cfull([(c('m24a'), nx(24)), (c('m24b'), at(24, 'Most people click'))], en_(24))
q('If you&#8217;re still here,<br><i>you think about style more deeply than most.</i>', nx(24) + 0.3, at(24, 'Most people click') - 0.2, QC, size=60, cls='over')
q('So let&#8217;s go<br><i>a little deeper.</i>', at(24, "So let's"), en(24) + 0.5, QC, size=88, cls='over')

# ================= 5. RE-WEAR WHAT WORKS =================
card_at('5. Re-wear What Works', 25, en(25) + 0.3, size=120)
cfull([(c('r5a'), nx(26))], at(26, 'She wore that') - 0.1)
band('Her favourite pieces,<br><i>again and again</i>', at(26, 'wore her favourite'), at(26, 'She wore that') - 0.2, size=64)
pics([P_('pjapanb_29', 'Japan', pos='50% 15%', a=0.62), P_('pbalcony_0', 'the palace balcony, later that year', pos='50% 15%')],
     [at(26, 'She wore that') - 0.15, at(26, 'again later')], at(26, 'And some of her') - 0.15, h=850, y0=50, gap=120)
pics([P_('ppink83_17', '1983', pos='50% 10%', a=0.58), P_('ppink83_22', '1986: the ruffles are gone', pos='50% 10%', a=0.66)],
     [at(26, 'And some of her') - 0.15, at(26, 'quietly altered')], at(26, 'so they looked') - 0.15, h=850, y0=50, gap=80, x0=40, x1=1300)
q('Quietly altered,<br><i>so they looked new</i>', at(26, 'quietly altered') + 0.3, at(26, 'One fashion') - 0.2, (1300, 60, 1890, 1020), size=58)
pics([P_('plisbon_30', '1987', pos='50% 10%'), P_('plisbon_13', '1989: the sleeves are gone', pos='50% 10%', a=0.56)],
     [at(26, 'so they looked') - 0.15, at(26, 'One fashion')], en_(26), h=850, y0=50, gap=80, x0=40, x1=1300)
q('&#8220;Both fancy<br><i>and frugal&#8221;</i>', at(26, 'both fancy') - 0.4, en(26) + 0.4, (1300, 250, 1890, 700), size=70)
q('as one fashion journalist described her', at(26, 'One fashion') + 0.2, en(26) + 0.4, (1300, 700, 1890, 820), size=32)
lclip([(c('r5b'), nx(27)), (c('r5c'), at(27, 'They need a few'))], at(27, 'So instead of') - 0.1)
q('Elegant women don&#8217;t need<br><i>a new outfit for every occasion.</i>', at(27, 'Elegant women'), at(27, 'They need a few') - 0.2, QL, size=58)
q('A few pieces they love,<br><i>and the confidence<br>to wear them again</i>', at(27, 'They need a few'), at(27, 'So instead of') - 0.2, QL, size=60)
q('Instead of buying something new,<br><i>try changing one thing.</i>', at(27, 'So instead of'), at(27, 'A camel belt') - 0.2, QC, size=70)
lrow([c('r5d'), c('r5e'), c('r5f')], [at(27, 'A camel belt') - 0.2, at(27, 'A navy jacket'), at(27, 'Your hair up')], at(27, 'You probably') - 0.1,
     labels=['a camel belt', 'a navy jacket', 'your hair up'])
cfull([(c('r5g'), at(27, 'You probably') - 0.2)], en_(27))
q('You probably already own<br><i>the outfit for your next event.</i>', at(27, 'You probably'), en(27) + 0.4, QC, size=66, cls='over')
pframe([(c('r5h'), nx(28)), (c('r5i'), at(28, 'Tell me') - 0.1)], en_(28))
pwords(['Be honest:', '<i>What&#8217;s one piece you love,</i>', '<i>but rarely wear?</i>', 'Tell me in the comments.'],
       [at(28, 'Be honest'), at(28, "What's one piece"), at(28, 'but rarely wear'), at(28, 'Tell me')], en(28) + 0.4, size=60, rh=150)

# ================= THE GUIDE =================
cfull([(c('g29a'), nx(29)), (c('g29b'), at(29, "If you're watching"))], at(29, 'our personal stylist') - 0.1)
q('&#8220;I&#8217;d love to know which colours<br><i>and shapes are truly mine.&#8221;</i>', at(29, "I'd love"), at(29, 'our personal stylist') - 0.2, QC, size=62, cls='over')
cfull([(c('g29c'), at(29, 'our personal stylist') - 0.2)], at(29, 'Your best colours') - 0.1)
q(GUIDE, at(29, 'our personal stylist') - 0.1, at(29, 'Your best colours') - 0.2, QC, cls='over')
lrow([c('g29d'), c('g29e'), c('g29f')], [at(29, 'Your best colours') - 0.2, at(29, 'your most flattering'), at(29, 'and outfit formulas')], at(29, 'The link is') - 0.1,
     labels=['your best colours', 'flattering hairstyles', 'outfit formulas'])
cfull([(c('g29g'), at(29, 'The link is') - 0.2)], en_(29))
q('The link is<br><i>in the description.</i>', at(29, 'The link is'), en(29) + 0.3, QC, size=80, cls='over')

# ================= 6. KEEP AN OFF-DUTY UNIFORM =================
card_at('6. Keep an Off-Duty Uniform', 30, at(30, 'When Diana') - 0.15, size=110)
pics([P_('ppolo_0', pos='50% 20%'), P_('pwhitejeans_19', pos='50% 20%'), P_('pbosnia_4', pos='50% 20%')],
     [at(30, 'When Diana') - 0.2, at(30, "she didn't reinvent"), at(30, 'She went back')], en_(30), h=820, y0=50)
capt('Off duty: <i>the same few pieces</i>', at(30, 'She went back'), en(30) + 0.4)
look('ppolo_1', 'ppolo_14', ['a blazer', 'jeans', 'a sweatshirt', '<i>a polo match, 1988</i>'],
     [nx(31) + 0.3, at(31, 'with jeans'), at(31, 'and a sweatshirt'), at(31, 'at a polo')], nx(31), at(31, 'White jeans') - 0.15, at(31, 'and a sweatshirt'))
look('pwhitejeans_22', 'pwhitejeans_21', ['white jeans', 'loafers', 'a tailored blazer', '<i>London, 1994</i>'],
     [at(31, 'White jeans'), at(31, 'loafers'), at(31, 'and a tailored'), at(31, 'for shopping')], at(31, 'White jeans') - 0.15, at(31, 'A white shirt') - 0.15, at(31, 'and a tailored'))
look('pbosnia_0', 'pbosnia_5', ['a white shirt', 'jeans', 'loafers', '<i>Bosnia, 1997</i>'],
     [at(31, 'A white shirt'), at(31, 'jeans and loafers'), at(31, 'jeans and loafers') + 0.7, at(31, 'on her visit')], at(31, 'A white shirt') - 0.15, en_(31), at(31, 'jeans and loafers'))
lclip([(c('r6a'), nx(32))], at(32, 'So choose') - 0.1)
q('Women who always look put together<br><i>aren&#8217;t making more decisions.</i>', at(32, 'Women who'), at(32, "They're making") - 0.2, QL, size=54)
q('They&#8217;re making<br><i>fewer.</i>', at(32, "They're making"), at(32, 'So choose') - 0.2, QL, size=96)
q('Choose your own<br><i>uniform.</i>', at(32, 'So choose'), at(32, "Maybe it's") - 0.2, QC, size=96)
lrow([c('r6b'), c('r6c'), c('r6d'), c('r6e')], [at(32, "Maybe it's") - 0.2, at(32, 'a crisp white'), at(32, 'a navy or'), at(32, 'and one pair')], at(32, 'You probably') - 0.1,
     w=480, labels=['dark jeans', 'a white shirt', 'a camel jacket', 'loafers'])
lclip([(c('r6f'), at(32, 'You probably') - 0.2), (c('r6g'), at(32, 'Then wear it'))], en_(32))
q('You probably already own<br><i>most of it.</i>', at(32, 'You probably'), at(32, 'Then wear it') - 0.2, QL, size=68)
q('Wear it, again and again,<br><i>until it feels like you.</i>', at(32, 'Then wear it'), en(32) + 0.4, QL, size=64)

# ================= 7. EDIT AS YOU GROW =================
card_at('7. Edit as You Grow', 33, en(33) + 0.3, size=120)
pics([P_('peightiesb_14', pos='50% 25%'), P_('peightiesb_19', pos='50% 30%'), P_('peightiesb_24', pos='50% 20%')],
     [nx(34), at(34, 'many of her'), at(34, 'ruffles and bows')], at(34, 'But in the 1990s') - 0.15, h=800, y0=50)
capt('The 1980s: <i>ruffles and bows</i>', st(34) + 0.4, at(34, 'But in the 1990s') - 0.25)
pics([P_('pnineties_12', pos='50% 15%'), P_('pnineties_0', pos='50% 20%'), P_('pnineties_24', pos='50% 20%')],
     [at(34, 'But in the 1990s') - 0.15, at(34, 'her style became'), at(34, 'Clean lines')], en_(34), h=800, y0=50)
capt('The 1990s: <i>simpler, and more chic</i>', at(34, 'her style became'), at(34, 'Clean lines') - 0.2)
capt('Clean lines. <i>Plain colours.</i> Beautifully cut.', at(34, 'Clean lines'), en(34) + 0.4)
pic('pauctionb_0.jpg', 80, 190, 700, 700, nx(35), en_(35), pos='50% 50%', zoom=1.05)
pic('pauction_7.jpg', 840, 140, 534, 800, at(35, 'They were sold') - 0.2, en_(35), label='New York, June 1997', pos='50% 30%', lsize=44)
qstack(['<i>June 1997</i>', '79 of her dresses', 'sold at auction', '<i>for cancer and<br>AIDS charities</i>'],
       [nx(35) + 0.4, at(35, 'seventy-nine'), at(35, 'They were sold'), at(35, 'and the money')], en(35) + 0.4, box_=(1420, 60, 1900, 1020), size=46, rh=170)
lclip([(c('r7a'), nx(36)), (c('r7b'), at(36, 'Instead of keeping'))], at(36, 'So this season') - 0.1)
q('Your wardrobe should look like<br><i>the woman you are now,</i>', at(36, 'Your wardrobe'), at(36, 'not the woman') - 0.2, QL, size=58)
q('not the woman you were<br><i>ten years ago.</i>', at(36, 'not the woman'), at(36, 'Instead of keeping') - 0.2, QL, size=62)
q('Instead of keeping everything<br>&#8220;just in case&#8221;&#8230;', at(36, 'Instead of keeping'), at(36, 'try keeping') - 0.2, QL, size=58)
q('Keep only what you would<br><i>wear this month.</i>', at(36, 'try keeping'), at(36, 'So this season') - 0.2, QL, size=64)
lrow([c('r7c'), c('r7d')], [at(36, 'So this season') - 0.2, at(36, 'Give it to')], en(36) + 0.75, labels=['take out one thing', 'give it away'])
q('Make<br><i>room.</i>', at(36, 'Make room') - 0.1, en(36) + 0.7, R3, size=110)

# ================= 8. KEEP ONE OUTFIT FOR COURAGE =================
cfull([(c('r8a'), st(37) - 0.3)], at(37, 'Keep one outfit') - 0.2)
q('The eighth rule:<br><i>the one that changes how you walk into any room</i>', st(37) + 0.3, at(37, 'Keep one outfit') - 0.4, QC, size=58, cls='over')
cardx('8. Keep One Outfit for Courage', at(37, 'Keep one outfit') - 0.4, en(37) + 0.45, size=104)
pic('prevengeb_22.jpg', 300, 70, 391, 940, nx(38), at(38, 'On the 29th') - 0.1, pos='50% 30%', zoom=1.1)
q('For about three years,<br><i>this black silk dress hung<br>in her wardrobe.</i>', nx(38) + 0.3, at(38, 'She had bought') - 0.2, (880, 60, 1860, 1020), size=60)
q('Bought, then judged<br><i>too daring.</i>', at(38, 'She had bought'), at(38, 'On the 29th') - 0.2, (880, 60, 1860, 1020), size=80)
q('<i>29 June 1994</i>', at(38, 'On the 29th'), at(38, 'the same night') + 0.9, QC, size=130)
cfull([(c('r8c'), at(38, 'the same night') + 1.0), (c('r8d'), at(38, 'she put it on')), (c('r8e'), at(38, 'head high') - 0.3)], at(38, 'The newspapers') - 0.1)
band('The night her husband&#8217;s television<br>interview was broadcast', at(38, 'the same night') + 1.2, at(38, 'she put it on') - 0.2, size=48)
band('<i>The Serpentine Gallery, London</i>', at(38, 'walked into'), at(38, 'head high') - 0.4, size=64)
band('Head high, <i>smiling</i>', at(38, 'head high') - 0.2, at(38, 'The newspapers') - 0.2, size=72)
pics([P_('prevenge_4', pos='50% 20%'), P_('prevenge_19', pos='50% 25%'), P_('prevenge_16', pos='50% 20%')],
     [at(38, 'The newspapers') - 0.15, at(38, 'The newspapers') + 0.9, at(38, 'the revenge dress')], en(38) + 0.45, h=820, y0=50)
capt('<i>&#8220;The revenge dress&#8221;</i>', at(38, 'the revenge dress') - 0.1, en(38) + 0.35, size=84)
picfull('prevengeb_17.jpg', nx(39), at(39, 'So find your') - 0.1, pos='50% 20%', zoom=1.07)
band('The lesson isn&#8217;t revenge.', st(39) + 0.2, at(39, 'The lesson is that') - 0.2, size=66)
band('She decided<br><i>how she would walk into that room.</i>', at(39, 'The lesson is that'), at(39, 'So find your') - 0.2, size=62)
lclip([(c('r8g'), at(39, 'So find your') - 0.2)], at(39, "Maybe it's") - 0.1)
qstack(['Find your <i>courage outfit.</i>', 'Not the newest thing you own.', '<i>The one that makes you<br>stand a little taller</i>'],
       [at(39, 'So find your'), at(39, 'Not the newest'), at(39, 'The one that')], at(39, "Maybe it's") - 0.2, size=58, rh=190)
lrow([c('r8h'), c('r8i'), c('r8j')], [at(39, "Maybe it's") - 0.2, at(39, 'maybe a deep red'), at(39, 'And keep it')], en_(39),
     labels=['a classic black dress', 'a deep red jacket', 'kept ready'])

# ================= CLOSE =================
cfull([(c('e40a'), nx(40)), (c('e40b'), at(40, 'It was a language'))], at(40, 'I thought about') - 0.15)
band('Never a costume.', at(40, "Diana's style"), at(40, 'It was a language') - 0.2, size=70)
band('<i>A language</i>', at(40, 'It was a language'), at(40, 'Every outfit') - 0.2, size=110)
band('Every outfit said something<br><i>to the people in front of her.</i>', at(40, 'Every outfit'), at(40, 'I thought about') - 0.25, size=56)
pics([P_('pjapan_20', '&#8220;I thought about you.&#8221;', pos='50% 20%'), P_('pnohat_10', '&#8220;I&#8217;m here.&#8221;', pos='50% 20%'), P_('prevengeb_14', '&#8220;I&#8217;m not afraid.&#8221;', pos='50% 20%')],
     [at(40, 'I thought about') - 0.15, at(40, "I'm here") - 0.1, at(40, "I'm not afraid") - 0.1], en(40) + 0.6, h=830, y0=50)
q('After this video:', nx(41) + 0.3, at(41, 'Before you get') - 0.2, QC, size=90)
lrow([c('e41a'), c('e41b'), c('e41c')], [at(41, 'Before you get') - 0.2, at(41, 'Choose one piece'), at(41, 'And find your')], en_(41),
     labels=['1. Who will I see?', '2. Re-wear one piece', '3. Your courage outfit'])
pframe([(c('e42a'), nx(42)), (c('e42a2'), at(42, 'which of') - 0.1)], at(42, "And if you'd") - 0.1)
pwords(['Tell me in the comments:', '<i>Which of Diana&#8217;s eight rules</i>', '<i>will you try first?</i>', 'I read every comment.'],
       [at(42, 'tell me in'), at(42, 'which of'), at(42, 'will you try'), at(42, 'I read every')], at(42, "And if you'd") - 0.2, size=60, rh=150)
cfull([(c('e42b'), at(42, "And if you'd") - 0.2), (c('e42c'), at(42, 'the personal stylist') - 0.5)], en_(42))
q(GUIDE, at(42, 'the personal stylist') - 0.4, en(42) + 0.3, (180, 620, 1740, 1040), cls='over')
cfull([(c('e43a'), nx(43)), (c('e43b'), at(43, 'They were remembered'))], total - 2.6)
band('Not because they were expensive.', at(43, "weren't remembered"), at(43, 'They were remembered') - 0.2, size=60)
band('Because of how she made people <i>feel</i>', at(43, 'They were remembered') + 0.3, at(43, 'Thank you') - 0.2, size=62)
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
