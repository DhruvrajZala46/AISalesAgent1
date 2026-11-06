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

# 6 Proportion Mistakes That Cheapen Your Outfits - beat map (6 Nov 2026)
# Layouts of the channel's winners (VISUAL-ANALYSIS.md): white numbered cards, the mistake in a row (bad first), the
# principle on caramel, one clip of the fix, a row of good examples, a full-screen exit; the whole vertical clip over its
# blurred copy for full screen (no crops), product photos on caramel, the CE logo. Every clip once.

def en_(i): return en(i) + 0.5

def sidecream(shots, t1, html, t0=None, size=58):
    cframe(shots, t1, x0=170)
    q(html, (t0 or shots[0][1]) + 0.3, t1 - 0.1, (820, 60, 1820, 1020), size=size, cls='dark')

# ================= HOOK =================
cfull([(C('h_mirror0', 0.0, 9.0), 0.0), (C('h_mirror4', 0.0, 13.1), at(1, 'and something') - 0.1)], nx(2))
lrow([C('h_older10', 0.0, 8.3), C('h_black22', 0.0, 10.3), C('h_mirror3', 0.0, 10.0)],
     [nx(2), at(2, 'The fabric'), at(2, 'And yet')], nx(3))
cfull([(C('h_walk9', 0.0, 6.13), nx(3))], at(3, "It's the lines") - 0.1)
ctext('It isn&#8217;t the clothes.<br>It&#8217;s <i>the lines they draw</i>.', at(3, "It's the lines") - 0.2, en(3) + 0.4, size=70)
lclip([(C('a_coatdress13', 1.3, 11.84), nx(4))], at(4, 'Put a line') - 0.1)
q('Every <i>hem</i>, every <i>seam</i><br>and every <i>strap</i> draws a line.', at(4, 'Every hem') - 0.1, at(4, 'Put a line') - 0.2, QL, size=62)
cfull([(C('h_walk21', 0.0, 5.47), at(4, 'Put a line') - 0.2), (C('h_black33', 0.0, 10.12), at(4, 'Put it in the wrong'))], en(4) + 0.35)
white(en(4) + 0.35, at(5, 'six') - 0.1); text("in today&#8217;s video...", 'card', en(4) + 0.65, at(5, 'six') - 0.25, dur=1.0, out=0.4)
cfull([(C('h_older6', 0.0, 9.37), at(5, 'six') - 0.3)], nx(6))
q('<i style="font-size:108px">6 Proportion Mistakes<br>That Cheapen Your Outfits</i>', at(5, 'six') + 0.1, en(5) + 0.4, QC, cls='over')
lrow([C('z_wardrobe2', 0.0, 9.2), C('h_older0', 0.0, 7.27), C('h_black18', 0.0, 7.93)],
     [nx(6), at(6, 'Some of these'), at(6, "you'll never")], en_(6))

# ================= 1. A LAYER THAT PEEKS OUT =================
card_at('1. A layer that peeks out from underneath', 7, en(7) + 0.3, size=90)
cfull([(C('a_peek9', 2.2, 11.84), st(8) - 0.2), (C('a_shirttail11', 0.0, 15.53), at(8, 'Or a shirt')), (C('a_coatlong2', 0.0, 7.7), at(8, 'or a dress'))], nx(9))
lclip([(C('a_shirttail8', 3.0, 16.32), nx(9))], nx(10))
q('Every extra hem adds<br><i>another line</i> across your middle.', at(9, 'But every') - 0.1, en(9) + 0.3, QL, size=58)
q('Elegant women let <i>one layer</i><br>finish the outfit.', st(10) + 0.1, en(10) + 0.3, QC, size=68)
lclip([(C('a_fronttuck13', 3.0, 20.3), nx(11))], at(11, 'Or choose') - 0.1, x=330)
q('Tuck it in, so the jacket&#8217;s hem<br>draws <i>the only line</i>.', at(11, 'so the jacket') - 0.2, at(11, 'Or choose') - 0.2, QL3, size=54)
lrow([C('a_cropknit7', 0.0, 8.97), C('a_cropknit0', 0.0, 6.67)], [at(11, 'Or choose') - 0.2, at(11, 'short enough')], nx(12))
photo('ph_p_fineknit.png', 1300, 160, 520, 660, at(11, 'a fine knit') - 0.2, nx(12), label='stops at the waist')
lclip([(C('a_coatlong15', 0.0, 6.97), nx(12)), (C('a_shortjacket3', 0.0, 8.89), at(12, 'or choose a short')),
       (C('a_shortjacket9', 0.0, 23.2), at(12, 'so the difference'))], nx(13), x=330)
q('Let the coat <i>cover</i> the dress.', at(12, 'Let the coat') - 0.1, at(12, 'or choose a short') - 0.2, QL3, size=60)
q('Or a short jacket that ends<br><i>well above it</i>.', at(12, 'or choose a short'), en(12) + 0.3, QL3, size=58)
sidecream([(C('g_stylist9', 0.0, 14.43), nx(13))], en_(13), 'Count the <i>hems</i> you can see.', size=64)

# ================= 2. A WAISTLINE THAT SITS TOO LOW =================
card_at('2. A waistline that sits too low', 14, en(14) + 0.3, size=96)
lrow([C('b_dropwaist9', 0.0, 14.7), C('b_jumpsuit9', 0.0, 6.63), C('b_dropcrotch13', 0.0, 10.42)],
     [st(15) - 0.2, at(15, 'jumpsuits'), at(15, 'and soft trousers')], at(15, "They're so") - 0.1)
cfull([(C('b_dropwaist16', 0.0, 13.69), at(15, "They're so") - 0.2)], nx(16))
lclip([(C('b_dropwaist1', 0.0, 9.83), nx(16)), (C('b_dropwaist18', 0.0, 8.8), at(16, 'When that line'))], nx(17))
q('Wherever a seam marks your waist,<br>the eye believes that&#8217;s where<br><i>your legs begin</i>.', at(16, 'But wherever') - 0.1, en(16) + 0.3, QL, size=54)
q('Elegant women keep their waistline<br><i>where nature put it</i>.', st(17) + 0.1, en(17) + 0.3, QC, size=66)
lrow([C('b_waistseam29', 0.0, 22.7), C('b_jumpsuit7', 0.0, 12.0), C('b_jumpsuit1', 0.0, 5.21)],
     [nx(18), at(18, 'the tie'), at(18, 'at your natural')], at(18, 'A wrap dress') - 0.1, labels=['the seam', 'the belt', 'the tie'])
lclip([(C('b_wrap1', 0.0, 18.87), at(18, 'A wrap dress') - 0.2)], nx(19))
photo('ph_p_wrapdress.png', 1150, 120, 420, 840, at(18, 'A wrap dress') + 0.3, nx(19), label='a wrap dress')
lclip([(C('b_highwaist7', 0.0, 9.92), nx(19)), (C('b_highwaist14', 0.0, 15.2), at(19, 'The seam should'))], at(19, 'A straight') - 0.1, x=330)
q('Stand <i>side-on</i> to the mirror.', at(19, 'stand side-on') - 0.1, at(19, 'The seam should') - 0.2, QL3, size=60)
q('The seam follows your body,<br><i>without pulling</i>.', at(19, 'The seam should'), at(19, 'A straight') - 0.2, QL3, size=56)
photo('ph_p_highwaist.png', 380, 110, 420, 860, at(19, 'A straight') - 0.2, nx(20), label='straight, at your waist')
cframe([(C('b_highwaist3', 0.0, 8.4), at(19, 'gives you back') - 0.2)], nx(20), x0=1050, bg=False)
cfull([(C('b_waistseam2', 0.0, 19.34), nx(20))], en_(20))

# ================= 3. SHORT SLEEVES AT THE WIDEST PART OF THE ARM =================
card_at('3. Short sleeves that stop at the widest part of your arm', 21, en(21) + 0.3, size=78)
cfull([(C('c_capsleeve4', 1.2, 12.0), st(22) - 0.1)], nx(23))
lrow([C('c_capsleeve4', 12.0, 36.0), C('c_capsleeve21', 0.0, 9.47)], [nx(23), at(23, 'The hem grips')], nx(24))
q('A tight hem draws a line<br>across the <i>widest point</i>.', at(23, 'The hem grips') + 0.2, nx(24) - 0.2, (1250, 60, 1880, 1020), size=52)
q('Elegant women let a sleeve<br><i>skim, never squeeze</i>.', st(24) + 0.1, en(24) + 0.3, QC, size=68)
lrow([C('c_elbow2', 0.0, 10.0), C('c_flutter15', 0.0, 13.62), C('c_flutter9', 0.0, 6.03)],
     [nx(25), at(25, 'or a soft'), at(25, 'A flutter sleeve')], at(25, 'or an elbow') - 0.1, labels=['above the elbow', 'a soft, wider sleeve', 'a flutter sleeve'])
photo('ph_p_flutter.png', 300, 110, 560, 800, at(25, 'or an elbow') - 0.2, nx(26), label='flutter sleeve')
photo('ph_p_elbow.png', 1060, 110, 560, 800, at(25, 'an elbow-length') - 0.1, nx(26), label='elbow-length tee')
lclip([(C('c_widestrap10', 0.0, 9.0), nx(26))], nx(27))
photo('ph_p_widestrap.png', 1310, 120, 520, 820, at(26, 'two fingers') - 0.1, nx(27), label='two fingers wide')
sidecream([(C('c_arms11', 0.0, 16.3), nx(27))], en(27) + 0.35, 'If it digs in, it&#8217;s the cut,<br><i>not your arm</i>.', t0=at(27, 'If the sleeve') - 0.3, size=62)

# ================= THE GUIDE =================
cfull([(C('a_peek16', 0.0, 14.47), st(28) - 0.1), (C('a_coatdress10', 0.0, 4.48), at(28, 'They know')),
       (C('f_double44', 0.0, 7.5), at(28, 'and the shapes'))], at(29, 'our personal') - 0.3)
cfull([(C('a_cropknit2', 0.0, 7.37), at(29, 'our personal') - 0.4), (C('f_twobutton5', 1.5, 5.8), at(29, "It's sent"))], en_(29))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(29, 'our personal') - 0.2, en(29) + 0.3, QC, cls='over')

# ================= 4. A GAP BETWEEN YOUR SKIRT AND YOUR BOOTS =================
card_at('4. A gap between your skirt and your boots', 30, en(30) + 0.3, size=90)
cfull([(C('d_bootskirt0', 0.0, 6.53), st(31) - 0.1)], nx(32))
lclip([(C('d_bootgap8', 0.0, 22.0), nx(32))], nx(33))
q('A strip of bare leg<br>cuts your leg into <i>short pieces</i>.', at(32, 'a little strip') - 0.1, nx(33) - 0.2, (1250, 60, 1880, 1020), size=52)
q('Elegant women make<br>the skirt and the boot <i>meet</i>.', st(33) + 0.1, en(33) + 0.3, QC, size=68)
lclip([(C('d_bootgap2', 0.0, 6.03), nx(34)), (C('d_bootgap15', 0.0, 6.43), at(34, 'by a few')), (C('d_bootskirt6', 1.7, 7.0), at(34, 'And check the slit'))], nx(35), x=330)
q('Overlap the top of your boots<br>by <i>a few inches</i>.', nx(34) + 0.3, at(34, 'And check the slit') - 0.2, QL3, size=58)
q('And check <i>the slit</i>.', at(34, 'And check the slit'), en(34) + 0.3, QL3, size=64)
lclip([(C('d_bootgap1', 0.0, 6.0), nx(35)), (C('d_brownboots23', 1.4, 11.68), at(35, 'deep brown')), (C('d_brownboots0', 0.0, 8.0), at(35, 'and your leg'))], nx(36))
q('Black tights with <i>black boots</i>.', at(35, 'Black tights') - 0.1, at(35, 'deep brown') - 0.2, QL, size=62)
q('Deep brown with <i>brown</i>.', at(35, 'deep brown'), at(35, 'and your leg') - 0.2, QL, size=62)
q('One long, <i>unbroken line</i>.', at(35, 'and your leg'), en(35) + 0.3, QL, size=62)
cfull([(C('d_brownboots9', 0.0, 10.66), nx(36))], en_(36))

# ================= 5. A LINE ACROSS YOUR ANKLE =================
card_at('5. A line across your ankle', 37, en(37) + 0.3, size=100)
lrow([C('e_anklestrap2', 0.0, 13.23), C('e_socks12', 4.0, 13.62), C('e_anklestrap4', 0.0, 11.12)],
     [st(38) - 0.2, at(38, 'a bright sock'), at(38, 'or pale shoes')], at(38, 'Each one') - 0.1)
cfull([(C('e_anklestrap21', 0.0, 7.7), at(38, 'Each one') - 0.2)], nx(39))
lclip([(C('e_anklestrap0', 0.0, 16.43), nx(39))], nx(40))
q('Your ankle is the <i>slimmest part</i><br>of your leg.', at(39, 'But your ankle') - 0.1, at(39, 'When a strap') - 0.2, QL, size=60)
q('When a line cuts across it,<br>your leg seems to <i>end right there</i>.', at(39, 'When a strap'), en(39) + 0.3, QL, size=56)
q('Elegant women keep the line<br>from the hem to the shoe <i>uninterrupted</i>.', st(40) + 0.1, en(40) + 0.3, QC, size=62)
lrow([C('e_tights11', 0.0, 10.25), C('e_tights4', 0.0, 15.17), C('e_loafers1', 2.5, 10.63)],
     [nx(41), at(41, 'or your socks'), at(41, 'so the colour')], at(41, 'With bare legs') - 0.1, labels=['shoes match the tights', None, 'socks match the trousers'])
lrow([C('e_nude0', 0.0, 10.15), C('e_nude14', 0.0, 8.0)], [at(41, 'With bare legs') - 0.2, at(41, 'a shoe close')], at(41, 'or a low-cut') - 0.1)
photo('ph_p_nudepump.png', 1310, 140, 520, 520, at(41, 'a shoe close') + 0.2, at(41, 'or a low-cut') - 0.1, label='close to your skin tone')
photo('ph_p_loafer.png', 1080, 120, 640, 760, at(41, 'or a low-cut') - 0.2, nx(42), label='a low-cut pump or loafer')
cframe([(C('e_nude3', 0.0, 6.23), at(41, 'or a low-cut') - 0.2)], nx(42), x0=330, bg=False)
lrow([C('e_finestrap0', 0.0, 12.0), C('e_finestrap19', 0.0, 21.17)], [nx(42), at(42, 'in the same colour')], nx(43), labels=['a very fine strap', 'the same colour'])
cfull([(C('e_nude12', 0.0, 7.07), nx(43))], en_(43))

# ================= 6. A JACKET BUTTONED THE WRONG WAY =================
card_at('6. A jacket buttoned the wrong way', 44, en(44) + 0.3, size=96)
cfull([(C('f_twobutton2', 0.0, 9.0), st(45) - 0.1)], nx(46))
lrow([C('f_blazer4', 2.3, 14.14), C('f_blazerpull16', 3.0, 21.7)], [nx(46), at(46, 'or when a fitted')], nx(47))
q('Little creases shaped like an <i>X</i><br>drag across your middle.', at(46, 'little creases') - 0.1, nx(47) - 0.2, (1250, 60, 1880, 1020), size=52)
q('Elegant women let a jacket<br>fall in a <i>clean V</i>.', st(47) + 0.1, en(47) + 0.3, QC, size=68)
lclip([(C('f_blazer14', 0.0, 9.03), nx(48))], at(48, 'A double-breasted') - 0.1)
photo('ph_p_twobutton.png', 820, 120, 560, 780, nx(48) + 0.3, at(48, 'On a one-button') - 0.1, label='close only the top button')
q('On a one-button jacket,<br>close it when you <i>stand</i>,<br>open it when you <i>sit</i>.', at(48, 'On a one-button'), at(48, 'A double-breasted') - 0.2, QL, size=56)
lrow([C('f_double1', 2.3, 10.0), C('f_double30', 0.0, 5.0)], [at(48, 'A double-breasted') - 0.2, at(48, 'so choose one')], nx(49))
photo('ph_p_double.png', 1300, 120, 540, 760, at(48, 'that fastens flat') - 0.3, nx(49), label='fastens flat')
lrow([C('f_double33', 0.0, 14.0), C('f_openblazer8', 0.0, 6.78), C('f_openblazer7', 0.0, 5.27)],
     [nx(49), at(49, 'Two long'), at(49, 'will lengthen')], nx(50))
cfull([(C('f_openblazer10', 0.0, 8.4), nx(50))], en_(50))

# ================= CLOSE =================
lclip([(C('a_coatdress8', 0.0, 22.5), nx(51))], en(51) + 0.35, x=330)
q('The outfit that never felt quite right<br>only needed <i>one line moved</i>.', at(51, 'Very often') - 0.1, en(51) + 0.3, QL3, size=54)
lrow([C('a_tuck8', 3.5, 18.23), C('c_elbow10', 0.0, 6.3), C('d_bootgap19', 1.0, 4.4), C('e_tights9', 0.0, 9.0)],
     [nx(52), at(52, 'lift a sleeve'), at(52, 'close the gap'), at(52, 'match the')], at(52, 'change a button') - 0.1, w=480)
cfull([(C('f_twobutton8', 3.3, 16.32), at(52, 'change a button') - 0.2), (C('h_mirror8', 0.0, 6.57), at(52, 'and notice'))], at(52, 'Because elegance') - 0.1)
ctext('Elegance was never about adding more.<br>It&#8217;s about letting every line<br><i>work with you</i>.', at(52, 'Because elegance') - 0.2, en(52) + 0.4, size=58)
cfull([(C('f_double29', 0.0, 8.03), nx(53)), (C('b_jumpsuit2', 0.0, 20.98), nx(54)), (C('e_loafers9', 3.0, 27.8), at(54, 'A simple like'))], nx(55))
cfull([(C('a_coatlong5', 0.0, 9.2), nx(55)), (C('f_openblazer4', 0.0, 6.23), nx(56))], total - 2.6)
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', nx(55) + 0.3, en(55) + 0.4, QC, cls='over')
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
