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

# v2 beat map (3 Nov 2026, after the creator's review): new intro, every phrase shown as it is said, product photos
# where the script names colours/pieces, no 16:9 crops of vertical clips, the CE logo.
CROP['bag_empty13'] = (0, 0, 1080)                                                          # above her KEEP/REMOVE captions
CROP['t_pool27'] = (56, 100, 1080); CROP['t_pool10'] = (56, 100, 1080)                    # grey screen-record bands                                                          # below her caption
FACEFIX.update({'r_audrey2_22': 0.5})

def en_(i): return en(i) + 0.5                                                              # hand-over just before a white card

# ================= HOOK =================
# 1 "Have you ever seen a woman in her sixties walk into a cafe and thought, 'How does she look so fresh?'"
cfull([(C('v_paris60_9', 0.0, 6.5), 0.0), (C('v_grey23', 0.0, 12.73), at(1, 'walk into') - 0.1),
       (C('h_silver21', 0.0, 3.9), at(1, 'How does') - 0.1)], nx(2))
# 2 "She isn't trying to look younger. No trendy outfit, no designer label in sight. And yet she seems lighter and
#    brighter than women half her age."
lrow([C('v_grey14', 0.3, 12.0), C('v_grey5', 7.2, 11.6), C('v_paris60_44', 0.0, 9.0)],
     [nx(2), at(2, 'No trendy'), at(2, 'no designer')], at(2, 'And yet') - 0.1)
cfull([(C('v_paris60_25', 0.0, 15.5), at(2, 'And yet') - 0.2), (C('v_paris60_9', 6.5, 10.2), at(2, 'half her age') - 0.3)], nx(3))
# 3 "That kind of elegance isn't accidental. More often than not, it comes down to what she has quietly stopped wearing."
lclip([(C('v_grey44', 0.0, 7.4), nx(3))], at(3, 'More often') - 0.1)
q('That kind of elegance<br>isn&#8217;t <i>accidental</i>.', st(3) + 0.2, at(3, 'More often') - 0.2, QL)
cfull([(C('z_closet10', 0.0, 7.8), at(3, 'More often') - 0.2)], en(3) + 0.35)
# 4 "In today's video ..." + the title
white(en(3) + 0.35, at(4, 'eight') - 0.1); text("in today&#8217;s video...", 'card', en(3) + 0.65, at(4, 'eight') - 0.25, dur=1.0, out=0.4)
cfull([(C('v_sixties48', 0.0, 8.77), at(4, 'eight') - 0.3), (C('v_paris60_22', 4.1, 26.5), at(4, 'and the simple') - 0.1)], nx(5))
q('<i style="font-size:116px">8 Things That<br>Quietly Age You</i>', at(4, 'eight') + 0.1, at(4, 'and the simple') - 0.3, QC, cls='over')
# 5 "Most of them are easy to fix, and many need nothing new at all. Some of these may surprise you, but once you see
#    them, you'll never unsee them. Let's get started."
lrow([C('w_tuck22', 0.0, 8.15), C('z_wardrobe32', 0.0, 6.5), C('v_sixties15', 15.0, 18.0)],
     [nx(5), at(5, 'and many'), at(5, 'Some of these')], at(5, "you'll never") - 0.1)
cfull([(C('z_door48', 0.0, 6.2), at(5, "you'll never") - 0.2)], en_(5))

# ================= 1. TROUSERS THAT POOL AROUND YOUR SHOES =================
card_at('1. Trousers that pool around your shoes', 6, en(6) + 0.3, size=96)
lclip([(C('t_wool30', 0.0, 5.28), st(7))], st(8) - 0.35, x=330)                               # a little extra length
lrow([C('t_pool27', 0.0, 8.0), C('t_pool10', 0.0, 6.2)], [st(8) - 0.2, at(8, 'steals length')], nx(9))   # bunches / steals length
q('It makes even good trousers<br>look <i>borrowed</i>.', at(8, 'makes even') - 0.1, en(8) + 0.3, (1256, 60, 1880, 1020), size=54)
lclip([(C('t_straight1', 0.3, 9.0), nx(9))], nx(10))
q('Elegant women keep one clean,<br><i>unbroken line</i> down to the shoe.', st(9) + 0.1, en(9) + 0.3, QL, size=56)
lrow([C('t_straight44', 4.1, 12.0), C('t_wool42', 0.0, 7.9), C('t_straight26', 0.3, 6.0)],      # straight leg / wool / twill
     [nx(10), at(10, 'wool crepe'), at(10, 'cotton twill')], at(10, 'in navy') - 0.15)
for k, (png, w_) in enumerate([('ph_tnavy.png', 'navy'), ('ph_tcream.png', 'cream'), ('ph_tcamel.png', 'camel'), ('ph_tgrey.png', 'grey')]):
    prod(png, 300 + k * 440, 880, 780, at(10, w_) - 0.15, en(10) + 0.45, label=w_, maxw=400)
lclip([(C('t_tailor8', 0.3, 9.0), nx(11)), (C('t_hem18', 0.0, 8.3), at(11, 'wear the shoes')), (C('t_hem0', 8.0, 17.1), at(11, 'and ask'))], en(11) + 0.35)
q('Take your favourite pair<br>to a <i>tailor</i>.', st(11) + 0.2, at(11, 'wear the shoes') - 0.2, QL, size=58)
q('Wear the <i>shoes</i><br>you&#8217;ll pair them with.', at(11, 'wear the shoes'), at(11, 'and ask') - 0.2, QL, size=58)
q('A hem that just meets<br>the <i>top of the shoe</i>.', at(11, 'and ask'), en(11) + 0.3, QL, size=58)
cfull([(C('t_hem0', 0.0, 8.0), nx(12)), (C('t_wool40', 0.3, 8.0), at(12, 'and suddenly'))], en_(12))

# ================= 2. STIFF BLOUSES WITH RUFFLES AT THE NECK =================
card_at('2. Stiff blouses with ruffles at the neck', 13, en(13) + 0.3, size=96)
lrow([C('b_jabot1', 0.3, 8.0), C('b_jabot6', 0.0, 8.0), C('b_bow2', 0.3, 8.0)],               # frilled collar / big bow / on the hanger
     [st(14) - 0.2, at(14, 'big bow'), at(14, 'on the hanger')], nx(15))
lrow([C('b_victorian0', 0.3, 12.0), C('b_victorian3', 0.0, 8.8), C('b_jabot27', 0.0, 7.8)],    # stiff fabric / all those frills / the eye
     [nx(15), at(15, 'all those frills'), at(15, 'The eye')], at(15, 'old-fashioned') - 0.4)
lclip([(C('b_jabot9', 0.0, 6.1), at(15, 'old-fashioned') - 0.5)], en(15) + 0.35, x=330)       # old-fashioned
lclip([(C('b_silk39', 0.0, 5.27), nx(16))], nx(17))
q('Elegant women let <i>softness</i><br>frame the face.', st(16) + 0.1, en(16) + 0.3, QL)
lrow([C('b_silk0', 0.3, 15.0), C('b_satin6', 0.3, 12.0), C('b_silk10', 0.3, 15.2)],           # drapes / satin crepe / moves
     [nx(17), at(17, 'satin crepe'), at(17, 'moves when')], at(17, 'with an open') - 0.15)
lrow([C('b_silk47', 0.0, 8.9), C('b_satin38', 0.3, 3.6)], [at(17, 'open collar') - 0.3, at(17, 'V-neck') - 0.1], nx(18),
     labels=['open collar', 'gentle V-neck'])
cfull([(C('b_satin18', 0.0, 6.0), nx(18))], at(18, 'Cream') - 0.1)                             # the sheen near the face
for k, (png, w_, lab) in enumerate([('ph_bcream.png', 'Cream', 'cream'), ('ph_bblush.png', 'blush', 'blush'), ('ph_bblue.png', 'powder blue', 'powder blue')]):
    prod(png, 420 + k * 540, 860, 700, at(18, w_) - 0.15, en(18) + 0.45, label=lab, maxw=500)
lclip([(C('g_ready45', 1.0, 6.8), nx(19)), (C('b_satin20', 0.3, 11.0), at(19, "If it's your"))], en_(19))
q('Notice what you see first<br>in the <i>mirror</i>.', st(19) + 0.2, at(19, "If it's your") - 0.2, QL, size=58)
q('If it&#8217;s your face, <i>keep it</i>.<br>If it&#8217;s the blouse, let it go.', at(19, "If it's your"), en(19) + 0.3, QL, size=58)

# ================= 3. THE BIG CHUNKY ROLL NECK =================
card_at('3. The big chunky roll neck', 20, en(20) + 0.3)
lclip([(C('r_chunky18', 0.3, 12.0), st(21) - 0.2)], nx(22), x=330)
lrow([C('r_chunky31', 6.1, 14.69), C('r_chunky33', 0.0, 9.1), C('r_chunky4', 0.3, 10.37)],    # thick rolls / under the chin / shortens
     [nx(22), at(22, 'It piles'), at(22, 'shortens')], nx(23) - 0.2)
full([(C('r_audrey2_22', 0.3, 12.0), nx(23))], at(23, 'in a slim') - 0.1)                       # Funny Face, all in black
photo('ph_audrey.png', 150, 75, 698, 930, at(23, 'in a slim') - 0.3, at(23, "That's the version") - 0.1)
q('A slim turtleneck that<br>simply <i>follows the neck</i>.', at(23, 'in a slim'), at(23, "That's the version") - 0.2, (930, 60, 1860, 1020), size=58)
cfull([(C('r_audrey3_0', 0.3, 8.0), at(23, "That's the version") - 0.2)], nx(24))
lrow([C('r_merino24', 0.0, 8.07), C('r_fine32', 0.0, 8.8), C('r_merino9', 0.0, 5.8), C('r_fine7', 1.3, 22.0)],
     [nx(24), at(24, 'in merino'), at(24, 'cashmere'), at(24, 'soft cotton')], at(24, 'folded over') - 0.1, w=480,
     labels=[None, 'merino', 'cashmere', 'soft cotton'])
cfull([(C('r_merino42', 0.0, 8.11), at(24, 'folded over') - 0.2)], nx(25))                    # folded over just once
lclip([(C('r_mock1', 0.3, 8.8), nx(25))], en(25) + 0.35)
prod('ph_mock.png', 960, 880, 760, at(25, 'a mock neck') - 0.2, en(25) + 0.3, label='mock neck', maxw=440)
q('Rises just a little<br>way up the <i>neck</i>.', at(25, 'rises') - 0.1, en(25) + 0.3, (1240, 60, 1890, 1020), size=56)
cfull([(C('r_merino3', 1.5, 15.0), nx(26))], en(26) + 0.4)

# ================= THE GUIDE (text over full-screen clips, no website) =================
cfull([(C('g_ready16', 0.3, 8.0), st(27) - 0.1), (C('g_drape38', 0.3, 9.0), at(27, 'They know')),
       (C('g_drape19', 1.5, 8.6), at(27, 'the necklines')), (C('w_wrap0', 0.3, 9.0), at(27, 'the shapes')),
       (C('g_drape45', 0.3, 12.0), at(28, 'our personal') - 0.3)], en_(28))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(28, 'our personal') - 0.2, en(28) + 0.3, QC, cls='over')

# ================= 4. THE LONG CARDIGAN THAT HAS LOST ITS SHAPE =================
card_at('4. The long cardigan that has lost its shape', 29, en(29) + 0.3, size=90)
lclip([(C('c_long17', 0.3, 11.1), st(30) - 0.2)], nx(31), x=330)
lrow([C('c_long7', 0.0, 16.0), C('c_long10', 0.3, 7.8), C('c_long0', 0.3, 15.2)],           # stretched / past the hips / pockets
     [nx(31), at(31, 'hangs past'), at(31, 'sags at')], nx(32))
lclip([(C('c_fine16', 5.6, 15.0), nx(32))], nx(33))
q('Elegant women still<br><i>love their knits</i>.', st(32) + 0.1, at(32, 'They simply') - 0.2, QL)
q('They simply choose ones that<br><i>hold their shape</i>.', at(32, 'They simply'), en(32) + 0.3, QL)
lclip([(C('c_fine25', 0.0, 15.1), nx(33))], en(33) + 0.35)
prod('ph_cardi.png', 940, 900, 780, at(33, 'fine-knit') - 0.2, en(33) + 0.3, maxw=560)
for k, (txt, w_) in enumerate([('Ends at the <i>hip</i>', 'ends around'), ('Neat <i>cuffs</i>', 'neat cuffs'), ('Buttons that <i>close</i>', 'buttons that')]):
    q(txt, at(33, w_) - 0.1, en(33) + 0.3, (1260, 300 + k * 160, 1890, 440 + k * 160), size=56, dur=0.9)
lrow([C('c_silk24', 0.3, 15.0), C('c_silk30', 0.3, 15.0), C('c_shoulders26', 0.0, 15.47)],     # as a top / over silk / over the shoulders
     [nx(34), at(34, 'leave it'), at(34, 'drape it')], at(34, 'Same comfort') - 0.1)
cfull([(C('c_fine40', 0.0, 7.03), at(34, 'Same comfort') - 0.2)], en_(34))

# ================= 5. WORDS ACROSS YOUR CHEST =================
card_at('5. Words across your chest', 35, en(35) + 0.3)
lrow([C('s_slogan2', 0.3, 13.79), C('s_slogan34', 0.3, 10.79), C('s_slogan7', 0.3, 10.49), C('s_slogan40', 0.0, 7.6)],
     [st(36) - 0.2, at(36, 'the name of'), at(36, 'a big brand'), at(36, 'a cheerful')], nx(37), w=480)
lclip([(C('s_slogan46', 0.3, 16.7), nx(37))], en(37) + 0.35, x=330)
q('The slogan does the talking,<br><i>not you</i>.', at(37, 'and for a moment') - 0.2, en(37) + 0.3, QL3, size=56)
lclip([(C('s_plain13', 0.3, 11.91), nx(38))], en(38) + 0.35)
for k, (png, w_, lab) in enumerate([('ph_teenavy.png', 'navy', 'navy'), ('ph_teeivory.png', 'ivory', 'ivory'), ('ph_teegrey.png', 'heather grey', 'heather grey')]):
    prod(png, 860 + k * 410, 760, 560, at(38, w_) - 0.15, en(38) + 0.3, label=lab, maxw=380)
lclip([(C('s_breton21', 0.0, 13.2), nx(39)), (C('s_breton19', 0.0, 12.27), at(39, "and it's still"))], en(39) + 0.35)
prod('ph_breton.png', 930, 880, 720, at(39, 'a classic') - 0.1, en(39) + 0.3, label='Breton stripe', maxw=520)
photo('ph_sailors.png', 1290, 120, 560, 800, at(39, 'French sailors') - 0.3, en(39) + 0.3, label='French sailors')
lclip([(C('s_breton35', 0.0, 9.89), nx(40))], en_(40))
q('Save the slogans for<br><i>weekends at home</i>.', st(40) + 0.2, at(40, 'and let') - 0.2, QL)
q('Let your <i>face</i> be the first thing<br>people notice.', at(40, 'and let'), en(40) + 0.3, QL)

# ================= 6. THE WIDE BELT WITH AN OVERSIZED BUCKLE =================
card_at('6. The wide belt with an oversized buckle', 41, en(41) + 0.3, size=90)
lclip([(C('w_blazer12', 4.0, 17.1), st(42) - 0.2)], nx(43), x=330)
lrow([C('w_wide21', 0.0, 10.66), C('w_buckle1', 0.3, 11.03), C('w_buckle35', 0.0, 7.5)],      # very wide / shiny buckle / heavy line
     [nx(43), at(43, 'shiny buckle'), at(43, 'heavy line')], at(43, 'It cuts') - 0.1)
lclip([(C('w_buckle29', 0.0, 5.27), at(43, 'It cuts') - 0.2)], nx(44), x=330)                    # two blocks
q('It cuts the outfit<br>into <i>two blocks</i>.', at(43, 'It cuts'), en(43) + 0.3, QL3, size=56)
lclip([(C('w_slim47', 0.0, 14.81), nx(44))], nx(45))
q('Elegant women define the waist<br><i>more softly</i>.', st(44) + 0.1, en(44) + 0.3, QL)
lclip([(C('w_buckle44', 1.3, 24.5), nx(45))], en(45) + 0.35)
prod('ph_beltcog.png', 1260, 420, 300, at(45, 'cognac') - 0.15, en(45) + 0.3, label='cognac with camel', maxw=900)
prod('ph_beltblk.png', 1260, 800, 300, at(45, 'black with') - 0.15, en(45) + 0.3, label='black with charcoal', maxw=900)
lrow([C('w_wrap13', 0.3, 15.17), C('w_blazer21', 0.3, 14.55), C('w_tuck21', 1.5, 11.7)],       # wrap dress / shaped jacket / half-tuck
     [nx(46), at(46, 'a softly'), at(46, 'a half-tuck')], en(46) + 0.3, labels=['a wrap dress', 'a shaped jacket', 'a half-tuck'])
cfull([(C('w_wide34', 5.0, 10.0), nx(47)), (C('w_slim27', 0.0, 3.93), at(47, 'when you catch'))], en_(47))

# ================= 7. HEAVY EARRINGS THAT DANGLE DOWN TO YOUR JAWLINE =================
card_at('7. Heavy earrings that dangle down to your jawline', 48, en(48) + 0.3, size=84)
lclip([(C('e_statement22', 1.2, 9.4), st(49) - 0.2)], nx(50), x=330)
lrow([C('e_dangle1', 0.3, 10.1), C('e_dangle14', 0.3, 9.54), C('e_dangle20', 0.3, 8.63)],      # long heavy drops / jaw / earlobes
     [nx(50), at(50, 'toward the jaw'), at(50, 'pull on')], at(50, 'Add a few') - 0.1)
lrow([C('e_layer23', 0.3, 9.94), C('e_layer14', 0.3, 12.0), C('e_layer18', 0.0, 8.0)],        # a few necklaces / crowded
     [at(50, 'Add a few') - 0.2, at(50, 'on top'), at(50, 'crowded')], nx(51))
lclip([(C('e_hoops18', 3.7, 18.57), nx(51))], nx(52))
q('Elegant women keep that space<br><i>calm and bright</i>.', st(51) + 0.1, en(51) + 0.3, QL)
for k, (png, w_, lab) in enumerate([('ph_hoopg.png', 'small gold', 'gold hoops'), ('ph_hoops.png', 'silver hoops', 'silver hoops'),
                                    ('ph_drop.png', 'a delicate', 'a delicate drop'), ('ph_pearl.png', 'classic pearl', 'pearl studs')]):
    photo(png, 70 + k * 455, 150, 420, 600, at(52, w_) - 0.2, at(52, 'sitting close') - 0.1, label=lab)
cfull([(C('e_pearl25', 0.0, 10.05), at(52, 'sitting close') - 0.2)], nx(53))                 # close to the face
lclip([(C('e_hoops26', 0.0, 8.67), nx(53)), (C('e_layer28', 2.2, 7.75), at(53, 'And if'))], en(53) + 0.35)
q('Gold for <i>warm</i> undertones,<br>silver for cool.', st(53) + 0.2, at(53, 'And if') - 0.2, QL, size=58)
q('One necklace is enough,<br>near the <i>collarbone</i>.', at(53, 'And if'), en(53) + 0.3, QL, size=58)
cfull([(C('e_hoops1', 0.0, 7.07), nx(54))], en_(54))

# ================= 8. THE BAG THAT CARRIES THE WHOLE HOUSE =================
card_at('8. The bag that carries the whole house', 55, en(55) + 0.3, size=96)
lrow([C('bag_big28', 0.0, 12.0), C('bag_heavy2', 0.0, 6.8), C('bag_big3', 1.3, 9.8)],           # enormous tote / heavy bag / packed
     [st(56) - 0.2, at(56, 'a heavy'), at(56, 'packed')], nx(57))
lclip([(C('bag_heavy49', 0.3, 15.2), nx(57)), (C('bag_heavy7', 0.3, 12.0), at(57, 'it pulls'))], en(57) + 0.35, x=330)
q('It pulls one side<br>of your body <i>down</i>.', at(57, 'it pulls'), en(57) + 0.3, QL3, size=56)
lclip([(C('bag_heavy6', 1.1, 6.9), nx(58))], nx(59))
q('Elegant women carry less,<br>and they <i>carry it well</i>.', st(58) + 0.1, en(58) + 0.3, QL)
lclip([(C('bag_mid15', 0.0, 6.07), nx(59)), (C('bag_mid30', 3.3, 19.91), at(59, 'in a colour'))], en(59) + 0.35)
prod('ph_bag.png', 1180, 840, 640, at(59, 'a clear') - 0.2, en(59) + 0.3, label='a clear, structured shape', maxw=560)
lclip([(C('bag_empty13', 0.3, 7.0), nx(60)), (C('bag_pack37', 1.3, 12.0), at(60, 'put back'))], at(60, "You'll be") - 0.1, x=330)
q('Put back only what<br>you&#8217;ll <i>truly use</i>.', at(60, 'put back'), at(60, "You'll be") - 0.2, QL3, size=56)
cfull([(C('t_wool36', 0.0, 8.97), at(60, "You'll be") - 0.2), (C('z_door7', 0.0, 11.2), at(60, 'walking out'))], nx(61))

# ================= CLOSE =================
lclip([(C('z_closet12', 1.0, 5.1), nx(61)), (C('z_closet18', 2.2, 12.0), at(61, 'Very often') - 0.1)], en(61) + 0.35, x=330)
q('The better version is already<br><i>in your closet</i>.', at(61, 'the better'), en(61) + 0.3, QL3, size=54)
lrow([C('z_older14', 0.0, 8.3), C('z_older19', 0.3, 9.0), C('z_older30', 0.0, 9.0)],          # women of every age
     [nx(62), at(62, 'and notice'), at(62, 'the first time')], at(62, 'Because') - 0.1)
lclip([(C('z_older12', 0.0, 5.3), at(62, 'Because') - 0.2), (C('z_older15', 0.3, 11.3), at(62, "It's to let"))], en(62) + 0.35)
q('The goal was never to look younger.<br>It&#8217;s to let your clothes show<br><i>the woman you are today</i>.', at(62, 'Because') - 0.1, en(62) + 0.3, QL, size=50)
cfull([(C('z_door8', 0.0, 5.93), nx(63)), (C('z_older16', 0.3, 12.0), nx(64)), (C('z_older26', 0.0, 7.9), at(64, 'a simple'))], nx(65))
cfull([(C('z_door36', 0.0, 6.6), nx(65)), (C('z_older36', 0.3, 15.0), at(65, 'access to')), (C('z_door14', 0.0, 7.4), nx(66))], total - 2.6)
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', nx(65) + 0.3, en(65) + 0.4, QC, cls='over')

open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
