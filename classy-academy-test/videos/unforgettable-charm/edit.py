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
# 5 Quiet Habits That Make a Woman Unforgettable (The Classy Elegance) - beat map (16 Nov 2026)
# Layouts: only those read off the channel's own behaviour and speech videos (VISUAL-ANALYSIS.md):
#   full clips (the whole vertical clip over its own blurred copy) | the habit's name on a white card in script |
#   a clip on the caramel with the lesson in white lines beside it, appearing as they are said | rows of clips |
#   a framed clip on cream with the EXACT WORDS in script beside it | two framed clips under a small label (a comparison) |
#   one sentence alone on the caramel | named women in real archive footage | the guide over a full clip | the CE logo.
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
# ================= HOOK =================
cfull([(c('h1a'), 0.0), (c('h1b'), at(1, 'But why'))], nx(2))
q('Why are some women<br><i>never forgotten?</i>', at(1, 'But why') + 0.1, en(1) + 0.3, QC, size=82, cls='over')
lclip([(c('h2a'), nx(2)), (c('h2b'), at(2, "She doesn't even"))], at(2, 'And yet') - 0.1)
qstack(['Not the prettiest.', 'Not the loudest.', '<i>Not even the best outfit.</i>'], [at(2, "She isn't the prettiest"), at(2, "She isn't the loudest"), at(2, "She doesn't even")], at(2, 'And yet') - 0.2, size=66)
cfull([(c('h2d'), at(2, 'And yet') - 0.2)], nx(3))
lclip([(c('h3a'), nx(3)), (c('h3b'), at(3, 'And real charm'))], at(3, "It's the feeling") - 0.1)
q('It isn&#8217;t luck,<br><i>and it isn&#8217;t looks.</i>', nx(3) + 0.2, at(3, "It's charm") - 0.2, QL, size=66)
q('<i>It&#8217;s charm.</i>', at(3, "It's charm") - 0.2, at(3, 'being bubbly') - 0.2, QL, size=100)
qstack(['Not bubbly,', 'not outgoing,', '<i>not nice to everyone</i>'], [at(3, 'being bubbly'), at(3, 'or outgoing'), at(3, 'or nice')], at(3, "It's the feeling") - 0.2, size=62)
q('The feeling your presence<br><i>leaves behind in other people</i>', at(3, "It's the feeling"), en(3) + 0.4, QC, size=72)
cfull([(c('h4a'), nx(4))], at(4, 'a little more seen') - 0.1)
lrow([c('h4b'), c('h4c'), c('h4d')], [at(4, 'a little more seen') - 0.2, at(4, 'a little calmer'), at(4, 'a little more alive')], en_(4),
     labels=['more seen', 'calmer', 'more alive'])
lrow([c('h5b'), c('h5c')], [nx(5), at(5, 'or age')], at(5, 'And you never') - 0.1)
qstack(['Not money.', 'Not age.', '<i>Not a perfect face.</i>'], [at(5, "It isn't about"), at(5, 'or age'), at(5, 'or a perfect')], at(5, 'And you never') - 0.2, box_=(2 * PW + 40, 60, 1890, 1020), size=64)
cfull([(c('h5d'), at(5, 'And you never') - 0.2)], nx(6))
q('Never <i>loud,</i><br>never <i>fake.</i>', at(5, 'And you never'), en(5) + 0.3, QC, size=84, cls='over')
cfull([(c('h6a'), nx(6)), (c('h6b'), at(6, 'Some of them')), (c('h6c'), at(6, 'the one that makes'))], en(7) + 0.35)
q('<div><span style="font-size:54px">5 Quiet Habits</span><br><i style="font-size:118px">Be Unforgettable</i></div>',
  at(6, 'five quiet') - 0.1, at(6, 'Some of them') - 0.2, QC, cls='over')

# ================= 1. CHOOSE WHERE YOUR ATTENTION GOES =================
card_at('1. Choose Where Your Attention Goes', 8, en(8) + 0.3, size=96)
lrow([c('a9a'), c('a9b'), c('a9c')], [nx(9), at(9, 'a wedding'), at(9, 'a busy family')], at(9, 'Most of us') - 0.1,
     labels=['a party', 'a wedding', 'a family lunch'])
lclip([(c('a9d'), at(9, 'Most of us') - 0.2), (c('a9f'), at(9, 'one eye on'))], en_(9))
q('Everywhere<br><i>at once</i>', at(9, 'Most of us'), at(9, 'A quick hello') - 0.2, QL, size=86)
qstack(['A quick hello here,', '<i>half a conversation there,</i>', 'one eye on whoever walked in'],
       [at(9, 'A quick hello'), at(9, 'half a conversation'), at(9, 'one eye on')], en(9) + 0.4, size=58)
lclip([(c('a10a'), nx(10))], at(10, 'But attention') - 0.1)
q('It comes from<br><i>a kind place.</i>', nx(10) + 0.2, at(10, 'But attention') - 0.2, QL, size=74)
q('Attention shared with the whole room<br><i>is felt by no one.</i>', at(10, 'But attention'), en(10) + 0.5, QC, size=70)
lclip([(c('a11a'), nx(11)), (c('a11b'), at(11, 'They give one')), (c('a11c'), at(11, 'And then they'))], en_(11))
q('Not switched on<br><i>for everyone, all evening</i>', at(11, "They aren't") - 0.1, at(11, 'They give one') - 0.2, QL, size=62)
q('One person, or one small group:<br><i>their full presence</i>', at(11, 'They give one'), at(11, 'And then they') - 0.2, QL, size=60)
q('And then<br><i>they gently step back.</i>', at(11, 'And then they'), en(11) + 0.4, QL, size=66)
cfull([(c('a12a'), nx(12))], at(12, 'Choose one person') - 0.1)
q('Don&#8217;t try to<br><i>work the room.</i>', at(12, "don't try") - 0.1, at(12, 'Choose one person') - 0.2, QC, size=82, cls='over')
pframe([(c('a12b'), at(12, 'Choose one person') - 0.2), (c('a12c'), at(12, 'And stay for'))], en_(12))
pwords(['Choose one person.', '<i>Turn your shoulders towards her.</i>', 'Stay for one whole story.'],
       [at(12, 'Choose one person'), at(12, 'Turn your'), at(12, 'And stay for')], en(12) + 0.4, size=58)
lclip([(c('a13a'), nx(13))], at(13, 'Refill your') - 0.1)
q('Close the conversation warmly,<br><i>then take a quiet moment.</i>', nx(13) + 0.2, at(13, 'Refill your') - 0.2, QL, size=58)
lrow([c('a13b'), c('a13c')], [at(13, 'Refill your') - 0.2, at(13, 'Stand by')], en_(13), labels=['refill your glass', 'stand by the window'])
q('You don&#8217;t have to be<br><i>&#8220;on&#8221; all night.</i>', at(13, "You don't have"), en(13) + 0.4, (2 * PW + 40, 60, 1890, 1020), size=60)
lclip([(c('a14a'), nx(14))], at(14, 'You need two') - 0.1)
cfull([(c('a14b'), at(14, 'You need two') - 0.2)], en_(14))
q('If big rooms tire you,<br><i>this is wonderful news.</i>', nx(14) + 0.2, at(14, "You don't need") - 0.2, QL, size=62)
q('You don&#8217;t need to be<br><i>the life of the party.</i>', at(14, "You don't need"), at(14, 'You need two') - 0.2, QL, size=62)
q('<i>Two or three</i><br>real conversations', at(14, 'You need two'), en(14) + 0.4, QC, size=84, cls='over')
cfull([(c('a15a'), nx(15)), (c('a15b'), at(15, 'who is completely'))], en_(15))
q('Charm grows from<br><i>contrast.</i>', at(15, 'It grows from') - 0.1, at(15, 'a calm woman') - 0.2, QC, size=86, cls='over')

# ================= 2. LET YOUR CONTRASTS SHOW =================
card_at('2. Let Your Contrasts Show', 16, en(16) + 0.3, size=110)
lclip([(c('b17d'), nx(17))], at(17, 'The quiet one') - 0.1)
q('Many of us learned<br><i>to be one thing.</i>', nx(17) + 0.2, at(17, 'The quiet one') - 0.2, QL, size=70)
lrow([c('b17a'), c('b17b'), c('b17c')], [at(17, 'The quiet one') - 0.2, at(17, 'The sensible'), at(17, 'The sweet')], en_(17),
     labels=['the quiet one', 'the sensible one', 'the sweet one'])
cfull([(c('b18a'), nx(18)), (c('b18b'), at(18, 'and then she said'))], en_(18))
q('There was always<br><i>a second side.</i>', at(18, 'There was always') - 0.1, at(18, 'You thought') - 0.2, QC, size=82, cls='over')
cfull([(c('b19a'), nx(19)), (c('b19b'), at(19, 'and then a line'))], en_(19))
q('<i>Marilyn Monroe</i>', at(19, 'Marilyn') - 0.1, at(19, 'That soft') + 1.2, (180, 880, 1740, 1050), size=70, cls='over')
cfull([(c('b20a'), nx(20)), (c('b20b'), at(20, 'And yet she had')), (c('b20c'), at(20, 'the hands of'))], en_(20))
q('<i>Princess Diana</i>', at(20, 'Princess Diana') - 0.1, at(20, 'Gentle') + 1.2, (180, 880, 1740, 1050), size=70, cls='over')
lrow([c('b21a'), c('b21b'), c('b21c')], [nx(21), at(21, 'Quiet, and very'), at(21, 'Feminine, and')], at(21, "It's the contrast") - 0.1,
     labels=['soft, and strong', 'quiet, and very funny', 'feminine, and disciplined'])
q('It&#8217;s the contrast<br><i>that stays in people&#8217;s minds.</i>', at(21, "It's the contrast"), en(21) + 0.3, QC, size=72)
lclip([(c('b22a'), nx(22))], en_(22))
q('The more we smooth ourselves down,<br><i>the easier we are to forget.</i>', nx(22) + 0.2, en(22) + 0.4, QL, size=56)
lclip([(c('b23a'), nx(23)), (c('b23b'), at(23, 'Something'))], en_(23))
t_hum = at(23, 'rarely see', end=True) + 0.15
q('Which side of me<br><i>do people rarely see?</i>', nx(23) + 0.2, t_hum - 0.1, QL, size=66)
qstack(['My humour?', '<i>A strong opinion?</i>', 'Something I&#8217;m quietly very good at?'], [t_hum, at(23, 'A strong'), at(23, 'Something')], en(23) + 0.4, size=58)
lclip([(c('b24a'), nx(24))], at(24, 'When everyone') - 0.1)
q('Let it show,<br><i>just once.</i>', nx(24) + 0.2, at(24, 'When the funny') - 0.2, QL, size=76)
q('When the funny thought comes,<br><i>say it, softly.</i>', at(24, 'When the funny'), at(24, 'When everyone') - 0.2, QL, size=60)
pframe([(c('b24b'), at(24, 'When everyone') - 0.2)], en_(24))
pwords(['When everyone loved the film:', '<i>&#8220;Can I be honest?</i>', 'It wasn&#8217;t my favourite.', '<i>But the music was beautiful.&#8221;</i>'],
       [at(24, 'When everyone'), at(24, 'Can I be'), at(24, "It wasn't my"), at(24, 'But the music')], en(24) + 0.4, size=56, rh=150)
cfull([(c('b25a'), nx(25))], en_(25))
q('An honest opinion, said gently,<br><i>is quiet confidence.</i>', nx(25) + 0.2, at(25, "You don't have") - 0.2, QC, size=66, cls='over')
q('Stop hiding<br><i>the interesting parts.</i>', at(25, 'You only have') - 0.1, en(25) + 0.4, QC, size=78, cls='over')

# ================= 3. MAKE THEM FEEL INTERESTING =================
card_at('3. Make Them Feel Interesting', 26, en(26) + 0.3, size=104)
pframe([(c('c27a'), nx(27)), (c('c28a'), nx(28))], en_(28))
pwords(['Before a dinner,', 'or a first meeting:', '<i>&#8220;Will they like me?&#8221;</i>'], [nx(27) + 0.3, at(27, 'or a first'), at(27, 'Will they')], en(27) + 0.3, size=62)
pwords(['Charming women ask:', '<i>&#8220;How will they feel</i>', '<i>about themselves</i>', '<i>when they&#8217;re with me?&#8221;</i>'],
       [nx(28) + 0.3, at(28, 'How will'), at(28, 'about themselves'), at(28, "when they're")], en(28) + 0.4, size=60, rh=150)
q('Here&#8217;s the truth.<br>People don&#8217;t really<br><i>remember you.</i>', nx(29) + 0.2, at(29, 'They remember who') - 0.2, QC, size=76)
lclip([(c('c29d'), at(29, 'They remember who') - 0.2)], at(29, 'If someone feels') - 0.1)
q('They remember<br><i>who they were</i><br>when they were with you.', at(29, 'They remember who'), at(29, 'If someone feels') - 0.2, QL, size=64)
lclip([(c('c29b'), at(29, 'If someone feels') - 0.2)], at(29, 'And if they feel') - 0.1)
q('If someone feels<br><i>judged or hurried</i><br>beside us, that stays.', at(29, 'If someone feels'), at(29, 'And if they feel') - 0.2, QL, size=62)
q('A little cleverer,<br><i>a little more interesting:</i><br>that stays too.', at(29, 'And if they feel'), en(29) + 0.5, QC, size=72)
lclip([(c('c30a'), nx(30))], en_(30))
q('Not flattery.<br><i>Curiosity.</i>', nx(30) + 0.2, at(30, 'So instead of') - 0.2, QL, size=84)
q('Instead of nodding<br><i>and waiting for your turn...</i>', at(30, 'So instead of'), at(30, 'ask about') - 0.2, QL, size=60)
q('...ask about <i>the choice</i><br>behind what she told you.', at(30, 'ask about'), en(30) + 0.4, QL, size=60)
pframe([(c('c31a'), nx(31))], en_(32))
pwords(['<i>&#8220;What made you choose that?&#8221;</i>', '<i>&#8220;How did you learn to do that?&#8221;</i>', '<i>&#8220;Wait, tell me that part again.&#8221;</i>'],
       [nx(31) + 0.1, at(31, 'How did'), at(31, 'Wait, tell')], en(31) + 0.3, size=54)
pwords(['Not about her dress.', '<i>About her.</i>', '<i>&#8220;I love the way you think.&#8221;</i>', '<i>&#8220;That was a brave decision.&#8221;</i>'],
       [at(32, 'Not about'), at(32, 'About her'), at(32, 'I love the way'), at(32, 'That was a brave')], en(32) + 0.4, size=54, rh=150)
cfull([(c('c33a'), nx(33))], en_(33))
q('It takes real confidence<br><i>to let someone else shine.</i>', at(33, 'In fact') - 0.1, at(33, "You're simply") - 0.2, QC, size=66, cls='over')

# ================= THE GUIDE =================
cfull([(c('g34a'), nx(34))], at(34, 'to discover') - 0.1)
lrow([c('g34b'), c('g34c')], [at(34, 'to discover') - 0.2, at(34, 'hairstyles')], at(34, "you'll find") - 0.1,
     labels=['your best colours', 'hairstyles'])
q('<i>outfit formulas</i><br>and more', at(34, 'outfit formulas') - 0.1, at(34, "you'll find") - 0.2, (2 * PW + 40, 60, 1890, 1020), size=70)
cfull([(c('g34e'), at(34, "you'll find") - 0.2)], en_(34))
q(GUIDE, at(34, "you'll find") - 0.2, en(34) + 0.3, QC, cls='over')

# ================= 4. BE CALM ON THE INSIDE =================
card_at('4. Be Calm on the Inside', 35, en(35) + 0.3, size=110)
lclip([(c('d36a'), nx(36)), (c('d36b'), at(36, 'Where should')), (c('d36c'), at(36, 'We believe'))], en_(36))
q('You walk in, and<br><i>your mind starts racing.</i>', nx(36) + 0.2, at(36, 'How do I') - 0.2, QL, size=62)
qstack(['How do I look?', '<i>Where should I stand?</i>', 'What are they thinking of me?'], [at(36, 'How do I'), at(36, 'Where should'), at(36, 'What are they')], at(36, 'We believe') - 0.2, size=58)
q('We believe we&#8217;re hiding it.', at(36, 'We believe'), at(36, 'But people') - 0.2, QL, size=62)
q('But people feel it,<br><i>even when they can&#8217;t name it.</i>', at(36, 'But people'), en(36) + 0.4, QL, size=60)
cfull([(c('d37a'), nx(37))], at(37, 'So the woman') - 0.1)
q('Most people are<br><i>a little noisy inside.</i>', at(37, 'are a little') - 0.3, at(37, 'So the woman') - 0.2, QC, size=78, cls='over')
lclip([(c('d37b'), at(37, 'So the woman') - 0.2), (c('d37c'), at(37, "She isn't rushing")), (c('d37d'), at(37, 'She seems'))], en_(37))
q('The woman who is quiet inside<br><i>becomes restful to be near.</i>', at(37, 'So the woman'), at(37, 'Not flat') - 0.2, QL, size=56)
qstack(['Not flat.', 'Not cold.', '<i>Just calm and steady.</i>'], [at(37, 'Not flat'), at(37, 'Not cold'), at(37, 'Just calm')], at(37, "She isn't rushing") - 0.2, size=66)
q('She isn&#8217;t rushing.<br>She isn&#8217;t performing.', at(37, "She isn't rushing"), at(37, 'She seems') - 0.2, QL, size=62)
q('She seems to know<br><i>exactly who she is.</i>', at(37, 'She seems'), en(37) + 0.4, QL, size=66)
lclip([(c('d38z'), nx(38))], at(38, 'in the car') - 0.1)
q('A racing mind needs<br><i>something to hold.</i>', at(38, 'A racing') - 0.1, at(38, 'in the car') - 0.2, QL, size=68)
lrow([c('d38a'), c('d38b'), c('d38c')], [at(38, 'in the car') - 0.2, at(38, 'in the lift'), at(38, 'at the door')], at(38, 'finish one') - 0.1,
     labels=['in the car', 'in the lift', 'at the door'])
creambg(at(38, 'finish one') - 0.3, en_(39))
ctext('<i>&#8220;Tonight, I&#8217;d simply like to...&#8221;</i>', at(38, 'finish one'), en(39) + 0.3, size=74, box_=(180, 30, 1740, 300), bg=False)
frow([c('d39a'), c('d39b'), c('d39c')], [nx(39), at(39, 'Enjoy the'), at(39, 'Have one')], en_(39), w=349, h=620, gap=90, y0=330,
     labels=['hear Anna&#8217;s news', 'enjoy the music', 'one lovely conversation'])
cfull([(c('d40a'), nx(40))], at(40, 'Your shoulders') - 0.1)
q('Your attention has somewhere to go,<br><i>and it&#8217;s no longer on you.</i>', nx(40) + 0.2, at(40, 'Your shoulders') - 0.2, QC, size=62, cls='over')
lrow([c('d40b'), c('d40c'), c('d40d')], [at(40, 'Your shoulders') - 0.2, at(40, 'Your hello'), at(40, "There's an ease")], en_(40),
     labels=['your shoulders drop', 'your hello slows down', 'an ease about you'])
cfull([(c('d41a'), nx(41))], en_(41))
q('Not louder.<br><i>Calmer.</i>', at(41, 'Not louder') - 0.1, at(41, 'And funnily') - 0.2, QC, size=92, cls='over')

# ================= 5. LET THEM DISCOVER YOU SLOWLY =================
card_at('5. Let Them Discover You Slowly', 42, en(42) + 0.3, size=100)
lclip([(c('e43a'), nx(43)), (c('e43b'), at(43, "It isn't being")), (c('e43c'), at(43, 'or going quiet'))], en_(43))
q('Mystery,<br><i>but not the fake kind</i>', nx(43) + 0.2, at(43, "It isn't being") - 0.2, QL, size=72)
qstack(['Not cold.', '<i>Not playing games.</i>', 'Not going quiet for three days.'], [at(43, "It isn't being"), at(43, "It isn't playing"), at(43, 'or going quiet')],
       at(43, "It's simply not") - 0.2, size=58)
q('Not your whole life story<br><i>to someone you met ten minutes ago</i>', at(43, "It's simply not"), en(43) + 0.4, QL, size=56)
cfull([(c('e44b'), nx(44))], en_(44))
q('It never tells you everything<br><i>in the first episode.</i>', at(44, 'It never') - 0.1, at(44, "And that's") - 0.2, QC, size=66, cls='over')
lclip([(c('e45a'), nx(45))], at(45, 'When someone new') - 0.1)
q('Let people discover you<br><i>a little at a time.</i>', nx(45) + 0.2, at(45, "So here's") - 0.2, QL, size=64)
q('Here&#8217;s what that looks like<br><i>in real life.</i>', at(45, "So here's"), at(45, 'When someone new') - 0.2, QL, size=62)
pframe([(c('e45b'), at(45, 'When someone new') - 0.2)], en_(46))
pwords(['<i>&#8220;So, how has your year been?&#8221;</i>', 'A true answer, <i>in two sentences.</i>', 'Then <i>hand the conversation back.</i>'],
       [at(45, 'So, how has'), at(45, 'give a true'), at(45, 'Then hand')], en(45) + 0.2, size=56)
pwords(['<i>&#8220;It&#8217;s been a full year.</i>', '<i>A new job, and a move.</i>', '<i>I&#8217;ll tell you the rest another time.</i>', '<i>How about you?&#8221;</i>'],
       [nx(46) + 0.1, at(46, 'A new job'), at(46, "I'll tell you"), at(46, 'How about')], en(46) + 0.4, size=56, rh=150)
qstack(['You&#8217;ve been honest.', 'You&#8217;ve been warm.', '<i>You simply haven&#8217;t said everything.</i>'],
       [nx(47) + 0.1, at(47, "You've been warm"), at(47, 'You simply')], at(47, 'And with the') - 0.2, box_=QC, size=70)
lrow([c('e47b'), c('e47c')], [at(47, 'And with the') - 0.2, at(47, 'an old friend')], en_(47), labels=['your sister', 'an old friend'])
q('Open<br><i>the whole book.</i>', at(47, 'open the whole') - 0.1, en(47) + 0.4, (2 * PW + 40, 60, 1890, 1020), size=80)
lclip([(c('e48a'), nx(48))], at(48, 'So ask yourself') - 0.1)
q('A relief for us,<br><i>a weight for the person listening.</i>', nx(48) + 0.2, at(48, 'Sharing with') - 0.2, QL, size=58)
q('Sharing with intention is<br><i>a quiet form of self-respect.</i>', at(48, 'Sharing with'), at(48, 'So ask yourself') - 0.2, QL, size=58)
q('Do I leave people<br><i>curious,</i><br>or overwhelmed?', at(48, 'So ask yourself'), at(48, 'Charm leaves') - 0.2, QC, size=78)
q('Charm leaves them<br><i>curious.</i>', at(48, 'Charm leaves'), en(48) + 0.5, QC, size=86)

# ================= CLOSE =================
cfull([(c('f49a'), nx(49))], en_(49))
q('Charm isn&#8217;t a template.<br><i>It&#8217;s a blend, and it&#8217;s yours.</i>', at(49, "Charm isn't") - 0.1, en(49) + 0.4, QC, size=68, cls='over')
lclip([(c('f50a'), nx(50)), (c('f50b'), at(50, 'Calm, unhurried'))], en_(50))
qstack(['A soft voice, <i>clear convictions.</i>', 'Calm movements, <i>quick humour.</i>', 'A warm smile, <i>full attention.</i>'], [at(50, 'a soft voice'), at(50, 'Calm, unhurried'), at(50, 'A warm smile')], en(50) + 0.4, size=58)
lclip([(c('f51a'), nx(51)), (c('f51b'), at(51, "It's to stop"))], en_(51))
q('Not someone else,<br><i>not the woman you saw online</i>', nx(51) + 0.2, at(51, "It's to stop") - 0.2, QL, size=62)
q('Stop dimming<br><i>what&#8217;s already there.</i>', at(51, "It's to stop"), en(51) + 0.4, QL, size=76)
pframe([(c('f52b'), nx(52)), (c('f52c'), at(52, 'And before you'))], en_(52))
pwords(['One person, <i>your full presence.</i>', 'One hidden side, <i>shown.</i>', '<i>&#8220;How do I want people</i>', '<i>to feel about themselves?&#8221;</i>'],
       [at(52, 'Give one'), at(52, 'Let one hidden'), at(52, 'How do I want'), at(52, 'to feel about')], en(52) + 0.4, size=54, rh=150)
cfull([(c('f53a'), nx(53)), (c('f53b'), at(53, "It's quiet") - 0.3)], en_(53))
q('Quiet.<br><i>Intentional.</i>', at(53, "It's quiet") - 0.1, at(53, 'And once') - 0.2, QC, size=92, cls='over')
q('People don&#8217;t just notice you.<br><i>They remember you.</i>', at(53, "people don't just") - 0.1, en(53) + 0.5, QC, size=70, cls='over')
cframe([(c('f54a'), nx(54))], en_(54), x0=1260, w=500, h=889)
qstack(['1. Choose where your attention goes', '2. Let your contrasts show', '3. Make them feel interesting', '4. Be calm on the inside', '5. Let them discover you slowly'],
       [nx(54) + 0.2 + 0.35 * k for k in range(5)], en(54) + 0.3, box_=(120, 60, 1200, 1020), size=50, rh=140, cls='dark')
cfull([(c('f55a'), nx(55))], en_(55))
q(GUIDE, nx(55) + 0.3, en(55) + 0.3, QC, cls='over')
cfull([(c('f56a'), nx(56))], nx(57))
cfull([(c('f57a'), nx(57))], total - 2.6)
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
