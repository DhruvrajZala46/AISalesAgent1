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

FACEFIX.update({'h_film34': 0.4, 'h_silver4': 0.22, 'r_audrey3_4': 0.45, 'r_audrey2_22': 0.5, 'r_audrey3_0': 0.5, 'h_film3': 0.4})
CROP['bag_empty13'] = (0, 0, 1080)                                                          # above her KEEP/REMOVE captions
CROP['w_wide17'] = (56, 190, 1080)                                                          # below her caption

def en_(i): return en(i) + 0.5                                                              # hand-over just before a white card

# ================= HOOK (A full-screen, D centred, E row; as the #1 video's first 45 s) =================
full([(C('h_walk33', 0.0, 5.0), 0.0), (C('h_silver4', 3.0, 12.7), at(1, 'walk into') - 0.1),
      (C('h_silver21', 0.0, 3.9), at(1, 'How does') - 0.1)], nx(2))
centre([(C('h_silver35', 0.3, 9.0), nx(2))], at(2, 'And yet') - 0.1)                          # D: not trying to look younger
prow([C('h_sixty20', 0.3, 9.0), C('h_silver10', 0.3, 9.0), C('h_sixty27', 0.3, 9.0)],          # E: lighter and brighter
     [at(2, 'And yet') - 0.2, at(2, 'lighter'), at(2, 'half her age')], nx(3))
full([(C('h_film3', 0.3, 6.0), nx(3)), (C('h_walk26', 0.3, 6.2), at(3, 'it comes down'))], en(3) + 0.35)   # Audrey (Sabrina); stopped wearing
white(en(3) + 0.35, at(4, 'eight') - 0.1); text("In today&#8217;s video", 'card', en(3) + 0.65, at(4, 'eight') - 0.25, dur=1.0, out=0.4)   # B
full([(C('r_audrey3_4', 0.0, 11.0), at(4, 'eight') - 0.3)], nx(5))                               # C: the title over Malena
q('<i style="font-size:116px">8 Things That<br>Quietly Age You</i>', at(4, 'eight') + 0.1, en(4) + 0.4, QC, cls='over')
centre([(C('h_older23', 1.4, 6.3), nx(5))], at(5, 'Some of these') - 0.1)                    # D
prow([C('h_sixty5', 0.3, 9.0), C('h_silver43', 0.3, 9.0), C('h_walk17', 0.3, 9.0)],          # E: you'll see them
     [at(5, 'Some of these') - 0.2, at(5, 'but once'), at(5, "you'll never")], en_(5))

# ================= 1. TROUSERS THAT POOL AROUND YOUR SHOES =================
card_at('1. Trousers that pool around your shoes', 6, en(6) + 0.3, size=96)
centre([(C('t_pool18', 0.0, 2.8), st(7) - 0.2), (C('t_pool37', 0.0, 2.9), at(7, 'A little'))], at(8, 'bunches') - 0.3)                    # D: a little extra length
prow([C('t_pool10', 0.0, 6.2), C('t_pool27', 0.0, 8.0), C('t_pool32', 0.0, 7.7)],            # E: the mistake, one per phrase
     [at(8, 'bunches') - 0.3, at(8, 'steals length'), at(8, 'makes even')], nx(9))
q('&#8220;Elegant women keep one clean,<br><i>unbroken line</i> down to the shoe.&#8221;', st(9) + 0.1, en(9) + 0.3, QC)   # F
centre([(C('t_straight1', 0.3, 9.0), nx(10))], at(10, 'in navy') - 0.1)                       # D: the swap
prow([C('t_straight23', 0.3, 6.0), C('t_straight26', 0.3, 6.0), C('t_straight44', 4.1, 10.0), C('t_straight16', 0.3, 6.0)],   # E: navy, cream, camel, grey
     [at(10, 'navy') - 0.2, at(10, 'cream'), at(10, 'camel'), at(10, 'grey')], en(10) + 0.3, n=4)
gside([(C('t_tailor8', 0.3, 9.0), nx(11)), (C('t_hem4', 0.3, 8.0), at(11, 'and ask'))], en(11) + 0.35)   # G
q('Take them to a <i>tailor</i>,<br>with the shoes you&#8217;ll wear.', st(11) + 0.2, at(11, 'and ask') - 0.2, QG, size=56)
q('&#8220;A hem that just meets<br>the <i>top of the shoe</i>.&#8221;', at(11, 'and ask'), en(11) + 0.3, QG, size=56)
full([(C('t_wool10', 0.0, 4.2), nx(12)), (C('t_wool40', 0.3, 8.0), at(12, 'and suddenly'))], en_(12))   # A: exit

# ================= 2. STIFF BLOUSES WITH RUFFLES AT THE NECK =================
card_at('2. Stiff blouses with ruffles at the neck', 13, en(13) + 0.3, size=96)
prow([C('b_jabot1', 0.3, 8.0), C('b_jabot2', 0.3, 8.07), C('b_bow2', 0.3, 8.0)],              # E: frilled collar, big bow, on the hanger
     [st(14) - 0.2, at(14, 'big bow'), at(14, 'on the hanger')], nx(15))
centre([(C('b_jabot45', 0.3, 9.5), nx(15))], at(15, 'The eye') - 0.1)                       # D: stiff, crowding the chin
prow([C('b_victorian15', 0.0, 5.8), C('b_jabot27', 0.0, 7.8), C('b_victorian0', 0.3, 12.0)],
     [at(15, 'The eye') - 0.2, at(15, 'instead of'), at(15, 'old-fashioned')], nx(16))
q('&#8220;Elegant women let <i>softness</i><br>frame the face.&#8221;', st(16) + 0.1, en(16) + 0.3, QC)   # F
centre([(C('b_silk0', 0.3, 9.0), nx(17))], at(17, 'in silk') - 0.1)                           # D: the swap
prow([C('b_silk10', 0.3, 9.0), C('b_satin6', 0.3, 9.0), C('b_silk47', 0.3, 8.9)],
     [at(17, 'in silk') - 0.2, at(17, 'satin crepe'), at(17, 'with an open')], en(17) + 0.3)
full([(C('b_satin18', 0.0, 6.0), nx(18))], at(18, 'Cream') - 0.1)                            # A: the sheen near the face
prow([C('b_satin5', 0.3, 8.9), C('b_satin20', 0.3, 9.0), C('b_silk39', 0.0, 5.27)],
     [at(18, 'Cream') - 0.2, at(18, 'blush'), at(18, 'especially')], en(18) + 0.3)
gside([(C('g_ready45', 1.0, 6.8), nx(19)), (C('b_satin38', 0.3, 8.5), at(19, "If it's your"))], en_(19))                                         # G: the mirror test
q('Notice what you see first<br>in the <i>mirror</i>.', st(19) + 0.2, at(19, "If it's your") - 0.2, QG, size=56)
q('&#8220;If it&#8217;s your face, <i>keep it</i>.<br>If it&#8217;s the blouse, let it go.&#8221;', at(19, "If it's your"), en(19) + 0.3, QG, size=56)

# ================= 3. THE BIG CHUNKY ROLL NECK =================
card_at('3. The big chunky roll neck', 20, en(20) + 0.3)
centre([(C('r_chunky18', 0.3, 12.0), st(21) - 0.2)], nx(22))                                   # D
full([(C('r_chunky0', 0.3, 8.0), nx(22))], at(22, 'It piles') - 0.1)                          # A: the thick rolls
prow([C('r_chunky33', 0.0, 9.1), C('r_chunky4', 0.3, 9.0), C('r_mock7', 0.7, 5.2)],
     [at(22, 'It piles') - 0.2, at(22, 'under the chin'), at(22, 'shortens')], nx(23))
full([(C('r_audrey2_22', 0.3, 12.0), nx(23)), (C('r_audrey3_0', 0.3, 8.0), at(23, "That's the version"))], nx(24))   # A: Funny Face, Sabrina
centre([(C('r_merino24', 0.0, 8.07), nx(24))], at(24, 'in merino') - 0.1)                    # D: the swap
prow([C('r_fine12', 1.9, 9.97), C('r_merino9', 0.0, 5.8), C('r_fine21', 0.3, 8.0)],
     [at(24, 'in merino') - 0.2, at(24, 'cashmere'), at(24, 'soft cotton')], at(24, 'folded over') - 0.1)
full([(C('r_fine36', 0.0, 2.1), at(24, 'folded over') - 0.2), (C('r_fine3', 0.0, 8.93), at(24, 'just once'))], nx(25))                        # A: folded over once
gside([(C('r_mock1', 0.3, 8.8), nx(25))], en(25) + 0.35)                                      # G
q('A <i>mock neck</i> rises<br>just a little way.', at(25, 'a mock neck') - 0.1, en(25) + 0.3, QG, size=60)
full([(C('r_merino42', 0.0, 8.11), nx(26))], en(26) + 0.4)                                    # A: exit

# ================= THE GUIDE (K: text over full-screen clips, no website) =================
full([(C('g_drape38', 0.3, 9.0), st(27) - 0.1), (C('g_drape19', 1.5, 5.5), at(27, 'They know')),
      (C('g_ready16', 0.3, 8.0), at(27, 'the necklines')), (C('w_wrap0', 0.3, 9.0), at(27, 'the shapes')),
      (C('g_drape45', 0.3, 12.0), at(28, 'our personal') - 0.3)], en_(28))
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(28, 'our personal') - 0.2, en(28) + 0.3, QC, cls='over')

# ================= 4. THE LONG CARDIGAN THAT HAS LOST ITS SHAPE =================
card_at('4. The long cardigan that has lost its shape', 29, en(29) + 0.3, size=90)
centre([(C('c_long17', 0.3, 9.0), st(30) - 0.2)], nx(31))                                    # D
prow([C('c_long12', 0.3, 15.2), C('c_long10', 0.3, 7.8), C('c_long0', 0.3, 11.0)],            # E: stretched, past the hips, sagging pockets
     [at(31, 'stretched') - 0.2, at(31, 'hangs past'), at(31, 'sags at')], nx(32))
q('They simply choose ones that<br><i>hold their shape</i>.', at(32, 'They simply') - 0.2, en(32) + 0.3, QC)   # F
centre([(C('c_fine12', 1.4, 7.63), nx(33))], at(33, 'that ends') - 0.1)                       # D: the swap
twoframes(C('c_fine33', 0.3, 7.97), C('c_saggy44', 0.3, 9.0), at(33, 'that ends') - 0.2, at(33, 'and buttons'), en(33) + 0.3,   # H
          mid=['Ends at the hip', 'Neat cuffs', 'Buttons that close'], tm=[at(33, 'ends around'), at(33, 'neat cuffs'), at(33, 'buttons that')])
prow([C('c_silk24', 0.3, 9.0), C('c_silk30', 0.3, 9.0), C('c_shoulders1', 0.3, 9.0)],        # E: as a top, over silk, over the shoulders
     [at(34, 'Button it') - 0.2, at(34, 'leave it'), at(34, 'drape it')], at(34, 'Same comfort') - 0.1)
full([(C('c_fine40', 0.0, 7.03), at(34, 'Same comfort') - 0.2)], en_(34))                     # A: exit

# ================= 5. WORDS ACROSS YOUR CHEST =================
card_at('5. Words across your chest', 35, en(35) + 0.3)
prow([C('s_slogan2', 0.3, 9.0), C('s_slogan7', 0.3, 9.0), C('s_slogan40', 0.0, 7.6)],         # E: slogan, big print, a joke
     [st(36) - 0.2, at(36, 'a big brand'), at(36, 'a cheerful')], nx(37))
centre([(C('s_slogan46', 0.3, 9.0), nx(37)), (C('s_slogan34', 0.3, 8.0), at(37, 'and for a moment'))], en(37) + 0.35)   # D
centre([(C('s_plain13', 0.3, 8.0), nx(38))], at(38, 'navy') - 0.1)                            # D: the swap
prow([C('s_plain35', 1.6, 9.4), C('s_plain14', 0.0, 7.0), C('s_vneck12', 0.3, 9.0)],
     [at(38, 'navy') - 0.2, at(38, 'ivory'), at(38, 'with a scoop')], en(38) + 0.3)
centre([(C('s_breton0', 4.0, 12.0), nx(39))], at(39, 'It was worn') - 0.1)                    # D: the Breton
prow([C('s_breton19', 0.3, 9.0), C('s_breton17', 0.3, 9.0), C('s_breton2', 0.3, 9.0)],
     [at(39, 'It was worn') - 0.2, at(39, 'as far back'), at(39, "and it's still")], en(39) + 0.3)
gside([(C('s_breton37', 0.0, 7.7), nx(40))], en_(40))                                          # G
q('Let your <i>face</i> be the first thing<br>people notice.', at(40, 'and let') - 0.1, en(40) + 0.3, QG, size=56)

# ================= 6. THE WIDE BELT WITH AN OVERSIZED BUCKLE =================
card_at('6. The wide belt with an oversized buckle', 41, en(41) + 0.3, size=90)
centre([(C('w_wide13', 0.3, 9.0), st(42) - 0.2)], nx(43))                                      # D
prow([C('w_wide17', 1.2, 12.0), C('w_wide5', 0.3, 10.0), C('w_wide34', 0.3, 10.0)],          # E: wide belt, shiny buckle, heavy line
     [at(43, 'a very wide') - 0.2, at(43, 'shiny buckle'), at(43, 'heavy line')], at(43, 'It cuts') - 0.1)
centre([(C('w_buckle35', 0.0, 7.5), at(43, 'It cuts') - 0.2)], nx(44))                         # D: two blocks
q('Elegant women define the waist<br><i>more softly</i>.', st(44) + 0.1, en(44) + 0.3, QC)   # F
centre([(C('w_buckle44', 1.3, 9.0), nx(45))], at(45, 'cognac') - 0.1)                          # D: the swap
twoframes(C('w_slim32', 0.3, 10.56), C('w_slim12', 0.3, 9.59), at(45, 'cognac') - 0.2, at(45, 'black with'), en(45) + 0.3,   # I
          la='Cognac with camel', lb='Black with charcoal')
prow([C('w_wrap13', 0.3, 9.0), C('w_blazer21', 0.3, 9.0), C('w_tuck21', 1.5, 11.7)],           # E: wrap dress, shaped jacket, half-tuck
     [at(46, 'a wrap dress') - 0.2, at(46, 'a softly'), at(46, 'a half-tuck')], en(46) + 0.3)
centre([(C('w_buckle1', 0.3, 8.0), nx(47)), (C('w_slim27', 0.0, 3.93), at(47, 'when you catch'))], en_(47))   # D

# ================= 7. HEAVY EARRINGS THAT DANGLE DOWN TO YOUR JAWLINE =================
card_at('7. Heavy earrings that dangle down to your jawline', 48, en(48) + 0.3, size=84)
centre([(C('e_statement28', 0.3, 9.0), st(49) - 0.2)], nx(50))                               # D
prow([C('e_dangle1', 0.3, 10.1), C('e_dangle14', 0.3, 9.54), C('e_dangle20', 0.3, 8.63)],     # E: long heavy drops at the jaw
     [at(50, 'long, heavy') - 0.2, at(50, 'toward the jaw'), at(50, 'pull on')], at(50, 'Add a few') - 0.1)
prow([C('e_layer23', 0.3, 9.94), C('e_layer14', 0.3, 9.0), C('e_layer18', 0.0, 8.0)],         # E: a few necklaces, crowded
     [at(50, 'Add a few') - 0.2, at(50, 'on top'), at(50, 'crowded')], nx(51))
q('Elegant women keep that space<br><i>calm and bright</i>.', st(51) + 0.1, en(51) + 0.3, QC)   # F
prow([C('e_hoops31', 0.0, 15.9), C('e_pearl5', 0.0, 9.5), C('e_pearl12', 0.0, 8.1)],             # E: hoops, delicate drop, pearl studs
     [at(52, 'small gold') - 0.2, at(52, 'a delicate'), at(52, 'classic pearl')], en(52) + 0.3)
gside([(C('e_hoops20', 0.0, 6.75), nx(53)), (C('e_layer17', 0.0, 2.7), at(53, 'resting'))], en(53) + 0.35)   # G
q('Gold for warm undertones,<br><i>silver</i> for cool.', st(53) + 0.2, at(53, 'And if') - 0.2, QG, size=58)
q('One necklace is enough,<br>near the <i>collarbone</i>.', at(53, 'And if'), en(53) + 0.3, QG, size=58)
full([(C('e_pearl25', 0.0, 10.05), nx(54))], en_(54))                                         # A: exit

# ================= 8. THE BAG THAT CARRIES THE WHOLE HOUSE =================
card_at('8. The bag that carries the whole house', 55, en(55) + 0.3, size=96)
prow([C('bag_big21', 0.0, 8.9), C('bag_heavy2', 0.0, 6.8), C('bag_big3', 1.3, 9.8)],          # E: enormous tote, heavy shoulder bag, packed
     [at(56, 'An enormous') - 0.2, at(56, 'a heavy'), at(56, 'packed')], nx(57))
centre([(C('bag_heavy7', 0.3, 9.0), nx(57)), (C('bag_heavy49', 0.3, 9.0), at(57, 'it pulls'))], en(57) + 0.35)   # D
q('Elegant women carry less,<br>and they <i>carry it well</i>.', st(58) + 0.1, en(58) + 0.3, QC)   # F
centre([(C('bag_mid15', 0.0, 6.07), nx(59))], at(59, 'in a colour') - 0.1)                    # D: the swap
prow([C('bag_mid45', 0.0, 11.63), C('bag_mid30', 3.3, 12.0), C('bag_heavy37', 0.3, 9.0)],
     [at(59, 'in a colour') - 0.2, at(59, 'one that sits'), at(59, 'or your shoulder')], en(59) + 0.3)
centre([(C('bag_empty13', 0.3, 7.0), nx(60)), (C('bag_pack37', 1.3, 12.0), at(60, 'put back'))], at(60, "You'll be") - 0.1)   # D
full([(C('bag_heavy21', 0.0, 7.8), at(60, "You'll be") - 0.2), (C('z_door14', 0.0, 7.4), at(60, 'walking out'))], nx(61))   # A

# ================= CLOSE =================
centre([(C('z_closet18', 2.2, 12.0), nx(61)), (C('z_wardrobe40', 0.3, 9.0), at(61, 'the better')),
        (C('z_wardrobe42', 0.0, 11.0), at(61, 'just waiting'))], en(61) + 0.35)                   # D
prow([C('z_older14', 0.0, 8.3), C('z_older19', 0.3, 9.0), C('z_older30', 0.0, 9.0)],          # E: women of every age
     [at(62, 'Start with') - 0.2, at(62, 'and notice'), at(62, 'the first time')], at(62, 'Because') - 0.1)
gside([(C('z_older12', 0.0, 5.3), at(62, 'Because') - 0.2), (C('z_older15', 0.3, 9.0), at(62, "It's to let"))], en(62) + 0.35)   # G
q('&#8220;The goal was never to look younger.<br>It&#8217;s to let your clothes show<br><i>the woman you are today</i>.&#8221;', at(62, 'Because') - 0.1, en(62) + 0.3, QG, size=50)
full([(C('z_door8', 0.0, 5.93), nx(63)), (C('z_older16', 0.3, 12.0), nx(64)), (C('z_older26', 0.0, 7.9), at(64, 'a simple'))], nx(65))
full([(C('z_door36', 0.0, 6.6), nx(65)), (C('z_older36', 0.3, 15.0), at(65, 'access to')), (C('z_door7', 0.3, 12.0), nx(66))], total - 2.6)      # L: outro text, then the end card
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', nx(65) + 0.3, en(65) + 0.4, QC, cls='over')
