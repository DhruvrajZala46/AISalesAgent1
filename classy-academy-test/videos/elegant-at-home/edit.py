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

# How to Look Effortlessly Elegant at Home - beat map (4 Nov 2026)
# Layouts only from the original "How to Look Elegant & Expensive at Home" (GmiAMO93vFE) and the channel's own videos:
# full screen (vertical reels whole over their blurred copy), white numbered cards, cream backdrop with a framed clip and a
# grey script line, framed rows, rows edge to edge, a clip at the left + the line on caramel, fabric circles, product
# photos, "Check The Description For" over full clips, the CE logo. Every clip once; no zoom crops.

def en_(i): return en(i) + 0.5
CROP['a_chair37'] = (0, 0, 1180)                     # a small timestamp at the bottom right
CROP['a_flatlay24'] = (100, 260, 1020)               # a brand name embroidered on the pillow

def sidecream(shots, t1, html, t0=None, size=58):
    """cream backdrop, a framed clip at the left, the line in grey script/serif at the right (original 0:39-0:44)"""
    cframe(shots, t1, x0=170)
    q(html, (t0 or shots[0][1]) + 0.3, t1 - 0.1, (820, 60, 1820, 1020), size=size, cls='dark')

# ================= HOOK =================
cfull([(C('h_doris2', 0.0, 7.67), 0.0), (C('h_tshirt14', 1.3, 15.9), at(1, 'still in') - 0.2)], nx(2))
cfull([(C('e_claw3', 0.0, 7.46), nx(2)), (C('h_socks24', 0.0, 2.6), at(2, 'mismatched') - 0.1),
       (C('h_cardi21', 3.3, 9.79), at(2, 'and a cardigan'))], at(2, 'It happens') - 0.1)
cfull([(C('h_tshirt47', 0.0, 6.4), at(2, 'It happens') - 0.2)], nx(3))
cfull([(C('a_dress15', 0.0, 6.43), nx(3)), (C('a_ready39', 0.0, 14.02), at(3, 'polished') - 0.1)], at(3, 'without dressing') - 0.1)
frow([C('b_knitdress4', 0.0, 9.36), C('a_flatlay8', 0.0, 18.11), C('c_shawl3', 0.0, 10.54)],
     [at(3, 'without dressing') - 0.2, at(3, 'without spending'), at(3, 'without giving')], nx(4))
ctext('Elegance at home isn&#8217;t about looking perfect.<br>It&#8217;s about a few <i>small choices</i><br>you make for yourself.', st(4) + 0.2, en(4) + 0.3, size=62)
white(en(4) + 0.35, at(5, 'simple') - 0.1); text("in today&#8217;s video...", 'card', en(4) + 0.65, at(5, 'simple') - 0.25, dur=1.0, out=0.4)
cfull([(C('a_dress41', 0.0, 14.6), at(5, 'simple') - 0.3), (C('a_ready7', 0.0, 10.0), at(5, 'whatever')),
       (C('h_marilyn22', 0.0, 6.5), at(5, 'whoever'))], en_(5))
q('<i style="font-size:112px">How to Look Effortlessly<br>Elegant at Home</i>', at(5, 'simple') - 0.1, at(5, 'whatever') - 0.3, QC, cls='over')

# ================= 1. GET DRESSED FOR THE DAY =================
card_at('1. Get Dressed for the Day', 6, at(6, 'staying') + 0.3, size=100)
cframe([(C('a_laptopbed12', 0.0, 7.0), at(6, 'staying') + 0.1)], at(6, 'A coffee') - 0.1)
frow([C('a_pjcoffee13', 0.0, 7.67), C('a_laptopbed40', 0.0, 12.0), C('a_scroll30', 0.0, 2.8)],
     [at(6, 'A coffee') - 0.2, at(6, 'a few emails'), at(6, 'one more scroll')], at(6, 'and suddenly') - 0.1)
cfull([(C('f_sunset10', 0.0, 6.07), at(6, 'and suddenly') - 0.2)], nx(7))
lclip([(C('a_dress45', 0.0, 13.0), nx(7))], nx(8))
q('The moment you change out of your sleepwear<br>is the moment your <i>day truly begins</i>.', at(7, 'The moment') - 0.1, en(7) + 0.3, QL, size=54)
q('Elegant women keep a <i>gentle line</i><br>between night and day.', st(8) + 0.1, en(8) + 0.3, QC, size=66)
cfull([(C('a_chair37', 0.0, 10.3), nx(9)), (C('a_chair42', 2.1, 5.4), at(9, 'lay out'))], at(9, 'Soft trousers') - 0.1)
frow([C('a_flatlay1', 0.0, 19.9), C('b_knitdress10', 0.0, 19.07), C('a_flatlay7', 0.0, 7.55)],
     [at(9, 'Soft trousers') - 0.2, at(9, 'a clean knit'), at(9, 'something you')], at(9, 'In the morning') - 0.1,
     labels=['soft trousers', 'a clean knit', None])
cfull([(C('a_ready13', 0.0, 12.04), at(9, 'In the morning') - 0.2)], nx(10))
cfull([(C('h_marilyn10', 0.0, 9.3), nx(10)), (C('a_robe10', 0.0, 7.47), at(10, 'your robe'))], at(10, 'Once') - 0.1)
frow([C('a_wash1', 0.0, 11.2), C('d_polo4', 1.3, 7.6), C('a_wash8', 0.0, 6.8)],
     [at(10, 'Once') - 0.2, at(10, 'get dressed'), at(10, 'even if')], nx(11), bg='cream')
sidecream([(C('a_robe2', 0.0, 5.13), nx(11))], en_(11), 'It quietly tells you,<br><i>my day matters too</i>.', t0=st(11), size=64)

# ================= 2. THE ONE-PIECE SHORTCUT =================
card_at('2. The One-Piece Shortcut', 12, at(12, 'easiest') + 0.3, size=100)
cframe([(C('b_tights5', 0.0, 18.51), at(12, 'easiest') + 0.1)], nx(13), x0=170)
q('A single piece that&#8217;s<br><i>already an outfit</i>.', at(12, 'A single') - 0.1, en(12) + 0.3, (820, 60, 1820, 1020), size=64, cls='dark')
frow([C('b_knitdress5', 0.0, 10.71), C('b_jersey2', 0.0, 4.5), C('b_housedress0', 0.0, 8.6), C('b_jumpsuit9', 0.0, 9.73)],
     [nx(13), at(13, 'a jersey'), at(13, 'a cotton'), at(13, 'a relaxed')], at(13, 'You put on') - 0.1,
     w=400, h=711, gap=40, labels=['soft knit dress', 'jersey midi', 'house dress', 'jumpsuit'])
cfull([(C('b_housedress4', 0.0, 28.0), at(13, 'You put on') - 0.2)], nx(14))
lrow([C('b_tights6', 4.1, 13.0), C('b_tights15', 0.0, 40.1), C('b_knitdress1', 0.0, 13.21)],
     [nx(14), at(14, 'warm tights'), at(14, 'as comfortable')], at(14, 'In warm') - 0.1)
lrow([C('b_housedress7', 0.0, 18.42), C('b_linen10', 0.0, 13.4), C('b_linen2', 1.5, 8.0)],
     [at(14, 'In warm') - 0.2, at(14, 'linen dress'), at(14, 'moves as')], nx(15))
cfull([(C('b_linen4', 0.0, 12.67), nx(15))], at(15, 'so you can') - 0.1)
frow([C('b_cook14', 0.0, 11.37), C('b_housedress2', 0.0, 6.6), C('b_kids10', 0.0, 10.05), C('b_door4', 0.0, 14.6)],
     [at(15, 'so you can') - 0.2, at(15, 'tidy'), at(15, 'sit on the floor'), at(15, 'answer the door')], nx(16),
     w=400, h=711, gap=40)
cfull([(C('b_housedress9', 3.0, 7.0), nx(16)), (C('b_jersey6', 8.0, 16.0), at(16, 'from affordable')),
       (C('b_tights9', 3.8, 9.1), at(16, 'so you can'))], nx(17))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:116px">Elegant Homewear Options</i></div>', nx(16) + 0.3, en(16) + 0.3, QC, cls='over')
lclip([(C('a_dress49', 0.0, 13.9), nx(17))], en_(17))
q('When getting dressed is this simple,<br>looking lovely stops <i>feeling like effort</i>.', st(17) + 0.2, en(17) + 0.3, QL, size=54)

# ================= 3. WARM WITHOUT THE BULK =================
card_at('3. Warm Without the Bulk', 18, at(18, 'colder') + 0.1, size=100)
cfull([(C('c_cold19', 1.1, 10.08), at(18, 'colder') - 0.1)], nx(19))
cfull([(C('c_cold0', 0.0, 9.4), nx(19))], at(19, 'the biggest') - 0.1)
lrow([C('c_hoodie4', 3.2, 9.4), C('h_socks5', 0.0, 6.13), C('c_hoodie1', 0.0, 19.53)],
     [at(19, 'the biggest') - 0.2, at(19, 'two pairs'), at(19, 'and a blanket')], nx(20))
lclip([(C('c_merino17', 0.0, 7.3), nx(20))], nx(21))
q('Elegant women stay warm in layers<br>that are <i>thin, soft</i><br>and close to the body.', at(20, 'Elegant women') - 0.1, en(20) + 0.3, QL, size=58)
lclip([(C('c_merino8', 0.0, 12.0), nx(21))], at(21, 'Add a soft') - 0.1)
for k, (png, w_, lab) in enumerate([('ph_f_merino.png', 'merino', 'merino'), ('ph_f_modal.png', 'modal', 'modal'), ('ph_f_silk.png', 'a silk', 'silk blend')]):
    circle(png, 900 + k * 360, 470, 150, at(21, w_) - 0.15, at(21, 'Add a soft') - 0.1, label=lab)
lrow([C('c_layer10', 4.0, 17.06), C('c_layer1', 5.0, 15.83)], [at(21, 'Add a soft') - 0.2, at(21, 'a long cardigan')], at(21, 'and keep your') - 0.1)
photo('ph_so_wool.png', 430, 130, 470, 700, at(21, 'and keep your') - 0.2, nx(22), label='wool socks')
photo('ph_so_feet.png', 1020, 130, 470, 700, at(21, 'cashmere blend') - 0.15, nx(22), label='cashmere blend')
lclip([(C('c_shawl0', 0.0, 11.49), nx(22))], at(22, 'Drape it') - 0.1)
photo('ph_w_shawl.png', 900, 160, 560, 700, at(22, 'a knitted wrap') - 0.2, at(22, 'Drape it') - 0.1, label='a knitted wrap')
cfull([(C('g_guide1', 0.0, 11.5), at(22, 'Drape it') - 0.2)], nx(23))
sidecream([(C('c_merino5', 0.0, 8.28), nx(23))], en(23) + 0.35, 'Thin layers hold warmth between them,<br>so you stay <i>cozy</i><br>without feeling bundled up.', size=54)
lrow([C('c_summer10', 0.0, 9.0), C('b_linen0', 0.0, 15.0), C('c_summer3', 0.0, 13.0)],
     [nx(24), at(24, 'breathable'), at(24, 'soft pale')], nx(25))
ctext('Comfort and elegance were <i>never opposites</i>.<br>They just need a little planning.', st(25) + 0.1, en_(25), size=62)

# ================= 4. DRESS FOR THE DAY YOU'RE HAVING =================
card_at('4. Dress for the Day You&#8217;re Having', 26, at(26, 'looks the same') + 0.1, size=92)
cfull([(C('g_guide10', 0.0, 16.2), at(26, 'looks the same') - 0.1)], nx(27))
lclip([(C('d_wfh5', 0.0, 13.77), nx(27))], at(27, 'A soft knit') - 0.1)
q('Dress from <i>top to toe</i>,<br>not just from the waist up.', at(27, 'dress from') - 0.1, at(27, 'A soft knit') - 0.2, QL, size=62)
frow([C('d_polo8', 0.0, 7.07), C('d_call8', 0.0, 13.29), C('e_studs4', 0.0, 8.0), C('g_mirror12', 1.0, 6.0)],
     [at(27, 'A soft knit') - 0.2, at(27, 'a fluid shirt'), at(27, 'small earrings'), at(27, 'and your hair')], at(27, "You'll sit") - 0.1,
     w=400, h=711, gap=40, labels=['knit polo', 'fluid shirt', 'small earrings', 'hair done'])
cfull([(C('d_wfh13', 0.0, 13.73), at(27, "You'll sit") - 0.2)], nx(28))
lrow([C('d_clean2', 0.0, 13.3), C('d_apron13', 0.0, 8.13), C('d_clean10', 5.2, 16.8)],
     [nx(28), at(28, 'cooking'), at(28, 'easy to wash')], at(28, 'A fitted') - 0.1)
frow([C('c_merino2', 0.0, 8.07), C('a_flatlay24', 0.0, 7.1), C('d_apron4', 0.0, 6.8)],
     [at(28, 'A fitted') - 0.2, at(28, 'straight joggers'), at(28, 'and an apron')], nx(29), bg='cream')
cfull([(C('d_guests8', 3.6, 8.0), nx(29)), (C('b_door9', 0.0, 12.4), at(29, 'not when'))], at(29, 'Soft trousers') - 0.1)
lrow([C('a_ready40', 3.5, 8.0), C('b_linen3', 0.0, 5.83)], [at(29, 'Soft trousers') - 0.2, at(29, 'a simple dress')], at(29, 'lets you') - 0.1,
     labels=['soft trousers + silk', 'a simple dress'])
cfull([(C('z_dinner2', 0.0, 10.73), at(29, 'lets you') - 0.2)], nx(30))
lrow([C('d_sunday5', 0.0, 13.47), C('g_guide0', 0.0, 7.57), C('b_knitdress0', 0.0, 7.77)],
     [nx(30), at(30, 'a cashmere'), at(30, 'a long knit')], nx(31))
sidecream([(C('a_dress11', 0.0, 27.15), nx(31))], en_(31), 'It&#8217;s to have one easy answer<br>ready for <i>each kind of day</i>.', t0=at(31, "It's to have") - 0.3, size=58)

# ================= THE GUIDE (over full clips, no website) =================
cfull([(C('g_guide3', 5.6, 9.7), nx(32)), (C('b_jersey4', 0.0, 23.11), at(32, 'necklines')),
       (C('e_scrunchie4', 0.0, 15.5), at(33, "It's a complete"))], en_(33))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(32, 'our personal') - 0.2, en(33) + 0.3, QC, cls='over')

# ================= 5. THE FINISHING TOUCHES =================
card_at('5. The Finishing Touches', 34, at(34, 'often') + 0.1, size=100)
cfull([(C('h_calm30', 0.0, 6.63), at(34, 'often') - 0.1), (C('c_cold13', 0.0, 6.0), at(34, 'the ones we'))], nx(35))
lclip([(C('e_messybun2', 17.0, 23.3), nx(35))], at(35, 'try a smooth') - 0.1, x=330)
q('Instead of the bun that<br>slowly <i>slides to one side</i>', at(35, 'Instead of') - 0.1, at(35, 'try a smooth') - 0.2, QL3, size=56)
frow([C('e_lowbun36', 12.6, 40.1), C('e_claw14', 0.0, 19.07), C('e_scrunchie0', 0.0, 14.3)],
     [at(35, 'try a smooth') - 0.2, at(35, 'a claw clip'), at(35, 'a silk scrunchie')], at(35, 'Brush it') - 0.1,
     labels=['a smooth low bun', 'a claw clip', 'a silk scrunchie'])
cfull([(C('e_brush1', 0.0, 12.6), at(35, 'Brush it') - 0.2)], nx(36))
lrow([C('e_fluffy24', 0.0, 12.0), C('e_slippers4', 0.0, 4.17)], [nx(36), at(36, 'flattened')], at(36, 'Swap them') - 0.1)
cfull([(C('e_slippers3', 0.0, 8.57), at(36, 'Swap them') - 0.2)], at(36, 'soft leather') - 0.1)
for k, (png, w_, lab) in enumerate([('ph_sl_leather.png', 'soft leather', 'soft leather'), ('ph_sl_suede.png', 'suede', 'suede'),
                                    ('ph_sl_knitcream.png', 'knitted', 'cream'), ('ph_sl_camel.png', 'camel', 'camel'), ('ph_sl_grey.png', 'soft grey', 'soft grey')]):
    photo(png, 60 + k * 365, 170, 340, 560, at(36, w_) - 0.2, nx(37), label=lab)
cframe([(C('e_studs1', 0.0, 7.77), nx(37))], at(37, 'Small gold') - 0.1)
for k, (png, w_, lab) in enumerate([('ph_j_studs.png', 'Small gold', 'small gold studs'), ('ph_j_pearls.png', 'tiny pearls', 'tiny pearls'), ('ph_j_chain.png', 'a fine chain', 'a fine chain')]):
    photo(png, 150 + k * 560, 140, 500, 680, at(37, w_) - 0.2, at(37, 'light enough') - 0.1, label=lab)
cfull([(C('e_studs16', 0.0, 5.03), at(37, 'light enough') - 0.2)], nx(38))
sidecream([(C('a_ready6', 0.0, 6.64), nx(38))], en_(38), 'Together, they turn <i>just at home</i><br>into <i>put together</i> at home.', t0=at(38, 'But together') - 0.3, size=58)

# ================= 6. YOUR EVENING AT HOME =================
card_at('6. Your Evening at Home', 39, at(39, 'winds down') + 0.1, size=100)
cfull([(C('f_sunset17', 0.0, 8.03), at(39, 'winds down') - 0.1), (C('z_dinner1', 0.0, 10.37), at(39, 'give your'))], nx(40))
lclip([(C('f_hang7', 3.0, 10.9), nx(40)), (C('f_hang13', 28.0, 34.0), at(40, 'and hang'))], at(40, 'Then slip') - 0.1, x=330)
q('Hang them up <i>straight away</i>,<br>instead of leaving them on the chair.', at(40, 'and hang') - 0.1, at(40, 'Then slip') - 0.2, QL3, size=54)
cfull([(C('a_ready5', 0.0, 9.77), at(40, 'Then slip') - 0.2)], nx(41))
cfull([(C('f_tablesetting3', 1.2, 8.7), nx(41))], at(41, 'Use a real') - 0.1)
frow([C('f_tablesetting12', 1.2, 11.8), C('f_pour3', 0.0, 13.93), C('f_napkin1', 3.0, 23.82)],
     [at(41, 'Use a real') - 0.2, at(41, 'pour your water'), at(41, 'and fold')], at(41, 'Leave your phone') - 0.1,
     labels=['a real plate', 'a glass', 'a cloth napkin'])
cfull([(C('d_sunday7', 0.0, 22.52), at(41, 'Leave your phone') - 0.2)], nx(42))
lclip([(C('z_dinner3', 0.0, 11.16), nx(42))], en(42) + 0.35)
q('Eating this way<br><i>slows you down</i>.', st(42) + 0.2, at(42, 'and dinner') - 0.2, QL, size=62)
q('Dinner feels like <i>a moment</i>,<br>instead of a task.', at(42, 'and dinner') - 0.1, en(42) + 0.3, QL, size=62)
ctext('You don&#8217;t need a guest to set a beautiful table.<br><i style="font-size:1.6em">You&#8217;re reason enough.</i>', st(43) + 0.1, en(43) + 0.6, size=60)

# ================= CLOSE =================
cfull([(C('a_robe1', 0.0, 16.28), nx(44)), (C('a_robe41', 0.0, 9.87), at(44, "It's about small"))], nx(45))
cfull([(C('h_calm1', 0.0, 5.2), nx(45))], at(45, 'The outfit') - 0.1)
lrow([C('a_flatlay41', 0.0, 7.83), C('b_jumpsuit5', 0.0, 9.93), C('f_tablesetting5', 1.2, 12.7)],
     [at(45, 'The outfit') - 0.2, at(45, 'the one-piece'), at(45, 'or dinner')], at(45, 'Tell us') - 0.1)
cfull([(C('d_wfh3', 0.0, 10.62), at(45, 'Tell us') - 0.2)], nx(46))
cfull([(C('g_guide8', 0.0, 11.57), nx(46)), (C('c_summer8', 1.3, 6.7), at(46, "so if you'd"))], nx(47))
cfull([(C('d_sunday13', 0.0, 12.01), nx(47)), (C('f_sunset22', 0.0, 11.16), at(47, 'Be sure')), (C('f_sunset1', 0.0, 8.9), nx(48)), (C('c_shawl10', 0.0, 6.6), nx(49))], total - 2.6)
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:116px">Elegant At-Home Pieces</i></div>', nx(47) + 0.3, en(47) + 0.4, QC, cls='over')
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
