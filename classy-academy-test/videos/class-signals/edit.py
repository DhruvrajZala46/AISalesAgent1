# 7 Quiet Habits That Show You Have Class - the edit, beat by beat.
# Built ONLY from the layouts of the creator's own Part 1, "7 Behaviors That Quietly Signal You Have Class" (rHI_hcgK39E),
# read off its storyboard (videos/class-signals/VISUAL-ANALYSIS.md):
#   A full-screen clip | B script on white | C title over a clip | D white card | E vertical clip centred on white |
#   G three panels | H two panels | I clip left + quote right on caramel | J rounded frame centred on caramel |
#   K rounded frame left + quote right | M guide over clips | N outro over clips | O end card
# Footage: Pinterest video pins (Instagram/TikTok creators' reels), film scenes and public figures found there.
# No free-stock sites. Every clip appears ONCE; none from Part 1 or from "7 Things Classy Women Never Do in Public".
# No sound effects; soft solo piano ~12 dB under the voice (build.py). No website on screen.

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

FACEFIX.update({'h_alone1': 0.75, 'a5_morning33': 0.6,
                'z_everyday15': 0.75, 'h_lunch34': 0.42})

# ================= HOOK (A: full-screen clips, ~5 s each, as Part 1's first 25 s) =================
full([(C('h_soft2', 0.3, 6.0), 0.0), (C('h_calm19', 0.3, 7.3), at(1, 'never tries') - 0.1),
      (C('h_soft46', 3.03, 9.0), at(1, 'and yet'))], nx(2))                                             # the room softens around her
full([(C('h_film13', 0.3, 5.6), nx(2)), (C('h_quiet41', 0.0, 4.1), at(2, "It isn't their"))], nx(3))     # Grace Kelly; not her clothes
full([(C('h_alone1', 0.3, 6.0), nx(3)), (C('h_alone40', 0.3, 7.6), at(3, 'especially'))], nx(4))          # small things, nobody watching
full([(C('h_lunch41', 3.97, 8.43), nx(4))], at(4, 'But once') - 0.1)
row([C('h_city45', 0.0, 4.0), C('h_lunch5', 0.3, 9.0), C('h_soft45', 0.3, 8.9)],                       # G: you'll see them everywhere
    [at(4, 'But once') - 0.2, at(4, "you'll start"), at(4, 'everywhere')], en(4) + 0.3)

# ================= THE TURN (B: script on white, then C: the title over a full-screen clip) =================
white(nx(5), at(5, 'seven') - 0.1); text("In today&#8217;s video", 'card', nx(5) + 0.3, at(5, 'seven') - 0.25, dur=1.0, out=0.4)
full([(C('h_grace26', 0.3, 8.0), at(5, 'seven') - 0.3)], nx(6))
q('<i style="font-size:116px">7 Quiet Habits That<br>Show You Have Class</i>', at(5, 'seven') + 0.1, en(5) + 0.4, QC, cls='over')
onwhite([(C('h_calm26', 2.03, 7.2), nx(6)), (C('h_calm36', 0.3, 6.4), at(6, 'and how they'))], en(6) + 0.35)   # E: how people feel

# ================= 1. LEAVING PLACES BETTER THAN THEY FOUND THEM =================
card_at('1. Leaving Places Better Than They Found Them', 7, st(7) + 3.0, size=84)
full([(C('a1_leave29', 0.0, 3.35), st(7) + 2.8)], nx(8))
full([(C('a1_fitting4', 0.0, 6.2), nx(8)), (C('a1_hotel23', 0.0, 3.56), at(8, 'The hotel')),             # one picture per place
      (C('a1_trolley3', 0.3, 9.0), at(8, 'The shopping'))], nx(9))
onwhite([(C('a1_tidy1', 0.3, 7.3), nx(9)), (C('a4_waiter1', 1.47, 5.6), at(9, 'Someone else'))], en(9) + 0.3)  # E
side([(C('a1_tidy9', 0.0, 7.4), nx(10))], en(10) + 0.35)                                                  # I
q('&#8220;Elegant people leave a little trace of <i>care</i><br>wherever they go.&#8221;', st(10) + 0.1, en(10) + 0.3, QI, size=56)
full([(C('a1_hangers30', 1.74, 10.05), nx(11)), (C('a1_towels44', 3.6, 9.68), at(11, 'The towels'))], at(11, 'The trolley') - 0.1)
CROP['a1_cart35'] = (110, 400, 880)                                                                      # below her own caption
vframe([(C('a1_cart35', 0.3, 6.3), at(11, 'The trolley') - 0.2)], en(11) + 0.3, x0=40)                    # K
q('The trolley goes back<br>where it <i>belongs</i>.', at(11, 'The trolley'), en(11) + 0.3, QR)
onwhite([(C('a1_towels8', 2.0, 8.9), nx(12)), (C('a1_hotel22', 0.9, 6.3), at(12, 'And usually'))], en(12) + 0.3)  # E
full([(C('z_everyday4', 0.0, 4.2), nx(13)), (C('h_alone3', 3.9, 10.1), at(13, "It's simply") - 0.2)], en(13) + 0.35)   # F
q('&#8220;It&#8217;s simply who they are<br>when <i>no one</i> is watching.&#8221;', at(13, "It's simply"), en(13) + 0.3, QC, cls='over')

# ================= 2. INTRODUCING PEOPLE WELL =================
card_at('2. Introducing People Well', 14, st(15) - 0.1)
full([(C('a2_hello28', 0.3, 9.0), st(15) - 0.3), (C('h_kate3', 2.4, 11.6), at(15, 'and someone'))], at(15, "There's a little") - 0.1)
halves([C('a2_network20', 0.0, 5.9), C('a2_network32', 1.67, 7.2)],                                      # H: the pause, the smiles
       [at(15, "There's a little") - 0.2, at(15, 'Nobody quite')], en(15) + 0.3)
vframe([(C('a2_chat18', 0.3, 8.0), nx(16))], en(16) + 0.3, x0=40)                                        # K: the quick version
q('&#8220;Oh, this is <i>Anna</i>.&#8221;', at(16, 'Oh, this'), en(16) + 0.25, (650, 250, 1860, 500), size=60)
q('And then, <i>silence</i>.', at(16, 'And then'), en(16) + 0.25, (650, 560, 1860, 800), size=56)
side([(C('h_kate29', 0.3, 8.0), nx(17))], en(17) + 0.35)                                                  # I
q('They introduce people with a name<br>and a little <i>bridge</i>.', at(17, 'They introduce'), en(17) + 0.3, QI, size=56)
vframe([(C('a2_hello41', 0.3, 7.0), nx(18)), (C('a2_lisbon26', 0.3, 7.5), at(18, 'Lisbon') - 0.2)], en(18) + 0.3, x0=40)   # K
q('&#8220;Anna, this is <i>Claire</i>.<br>Claire&#8217;s just come back from Lisbon,<br>and Anna has been dying to go.&#8221;', st(18) + 0.05, en(18) + 0.3, QR, size=52)
full([(C('a2_chat40', 0.0, 5.7), nx(19))], nx(20))                                                       # something to talk about
row([C('a2_hello16', 0.3, 8.0), C('a2_welcome14', 0.3, 9.0), C('a2_welcome18', 0.0, 5.6)],                 # G: nobody left standing
    [nx(20), at(20, 'Nobody has'), at(20, 'and nobody')], en(20) + 0.3)
full([(C('a2_network13', 6.3, 11.3), nx(21))], en(21) + 0.35)                                                 # F
q('&#8220;People feel so <i>welcome</i> around them,<br>wherever they are.&#8221;', st(21) + 0.1, en(21) + 0.3, QC, cls='over')

# ================= 3. TAKING NO GRACEFULLY =================
card_at('3. Taking No Gracefully', 22, st(22) + 2.8)
full([(C('h_grace3', 0.3, 6.0), st(22) + 2.6)], nx(23))
full([(C('a3_invite27', 0.3, 4.5), nx(23))], at(23, 'and she says') - 0.1)
vframe([(C('a3_typing20', 0.3, 6.5), at(23, 'and she says') - 0.2)], en(23) + 0.3, x0=40)                  # K
q('&#8220;I&#8217;m so sorry, I can&#8217;t make it<br><i>this time</i>.&#8221;', at(23, "I'm so sorry") - 0.1, en(23) + 0.3, QR)
vframe([(C('a3_typing24', 0.3, 9.0), nx(24))], en(24) + 0.3, x0=40)                                      # K: the three replies
for k_, (ph_, txt_) in enumerate([('Oh, come', '&#8220;Oh, come on! Just one drink.&#8221;'), ('You always', '&#8220;You always say that.&#8221;'),
                                  ('What else', '&#8220;What else are you <i>doing</i>?&#8221;')]):
    q(txt_, at(24, ph_) - 0.05, en(24) + 0.25, (650, 230 + k_ * 210, 1860, 430 + k_ * 210), size=54)
full([(C('a7_walk19', 2.0, 5.7), nx(25)), (C('a3_text12', 10.0, 20.0), at(25, 'But it puts'))], nx(26))   # playful; then explaining herself
vframe([(C('z_older12', 1.97, 8.1), nx(26))], en(26) + 0.3, x0=40)                                       # K
q('&#8220;No problem at all.<br>We&#8217;ll miss you. <i>Another time</i>.&#8221;', at(26, 'No problem') - 0.1, en(26) + 0.3, QR)
full([(C('a3_friends13', 0.0, 4.6), nx(27)), (C('a2_hello9', 1.37, 6.9), at(27, 'the next time') - 0.4)], nx(28))
onwhite([(C('a7_talk13', 0.3, 6.0), nx(28))], en(28) + 0.3)                                              # E
full([(C('a2_welcome13', 0.3, 7.5), nx(29))], en(29) + 0.35)                                             # F
q('&#8220;Theirs are the invitations people<br>most want to say <i>yes</i> to.&#8221;', at(29, 'theirs') - 0.1, en(29) + 0.3, QC, cls='over')

# ================= 4. BEING GRACEFUL WITH THE BILL =================
card_at('4. Being Graceful With the Bill', 30, st(30) + 2.6)
full([(C('b4_check47', 0.0, 4.0), st(30) + 2.4)], nx(31))
full([(C('b4_leather16', 0.3, 7.0), nx(31)), (C('b4_calc8', 1.4, 7.3), at(31, 'Someone opens'))], at(31, 'Well, I') - 0.1)
vframe([(C('a4_dinner47', 1.93, 4.27), at(31, 'Well, I') - 0.2), (C('a4_wine39', 0.3, 6.0), at(31, 'Who had'))], en(31) + 0.3, x0=40)   # K
q('&#8220;Well, I only had the <i>salad</i>.&#8221;', at(31, 'Well, I'), en(31) + 0.25, (650, 280, 1860, 500), size=56)
q('&#8220;Who had the second<br>glass of <i>wine</i>?&#8221;', at(31, 'Who had'), en(31) + 0.25, (650, 540, 1860, 820), size=56)
FACEFIX['b4_transfer13'] = 0.5
full([(C('b4_transfer13', 0.3, 8.0), nx(32)), (C('a5_morning33', 0.0, 5.7), at(32, 'and three weeks'))], en(32) + 0.35)
q('&#8220;I&#8217;ll send you my <i>share</i>.&#8221;', at(32, "I'll send") - 0.1, at(32, 'and three weeks') - 0.2, QC, cls='over')
side([(C('a4_dinner17', 1.0, 8.12), nx(33))], en(33) + 0.35)                                             # I
q('Handling money moments<br><i>gracefully</i> stands out.', at(33, "That's exactly"), en(33) + 0.3, QI, size=58)
full([(C('b4_leather3', 0.3, 8.0), nx(34)), (C('b4_calc1', 0.3, 8.0), at(34, 'If they owe'))], at(34, 'Sent') - 0.1)
vframe([(C('a3_typing31', 0.0, 5.0), at(34, 'Sent') - 0.3)], en(34) + 0.3, x0=40)                         # K
q('&#8220;Sent! Thank you<br>for <i>organising</i>.&#8221;', at(34, 'Sent'), en(34) + 0.3, QR)
full([(C('b4_check38', 3.67, 7.77), nx(35)), (C('a4_waiter10', 7.2, 9.7), at(35, 'often before'))], nx(36))
full([(C('b4_check40', 0.3, 7.8), nx(36))], en(36) + 0.35)                                               # F
q('&#8220;People feel completely at <i>ease</i> with them,<br>even when money is on the table.&#8221;', at(36, 'People feel') - 0.1, en(36) + 0.3, QC, size=54, cls='over')

# ================= THE GUIDE (M: text over full-screen clips, no website) =================
full([(C('g_colour17', 0.0, 5.77), nx(37)), (C('g_style36', 0.0, 5.83), at(37, 'shapes')),
      (C('g_style44', 0.0, 7.0), at(37, 'that truly')), (C('g_style19', 0.0, 5.1), at(37, 'and feel more')),
      (C('h_quiet30', 0.3, 8.8), at(37, 'the personal') - 0.3)], en(38) + 0.35)
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', at(37, 'the personal') - 0.2, en(38) + 0.2, QC, cls='over')

# ================= 5. THE GUEST EVERYONE INVITES BACK =================
card_at('5. The Guest Everyone Invites Back', 39, st(40) - 0.1, size=100)
full([(C('a5_door32', 0.0, 4.07), st(40) - 0.3), (C('a6_family34', 0.5, 4.63), at(40, 'You arrive')),
      (C('a5_table21', 0.3, 6.7), at(40, 'and you leave'))], nx(41))
onwhite([(C('a5_flowers24', 0.0, 6.2), nx(41))], en(41) + 0.3)                                           # E: the guest a host remembers
full([(C('a5_flowers1', 0.0, 5.47), nx(42))], at(42, 'A few') - 0.1)
row([C('a5_flowers12', 3.0, 10.36), C('a5_choc8', 0.0, 5.53), C('a5_bake28', 0.0, 11.0)],                   # G: flowers, chocolate, baked
    [at(42, 'A few') - 0.2, at(42, 'a bar'), at(42, 'something they baked')], en(42) + 0.3)
vframe([(C('a5_help26', 0.0, 5.1), nx(43))], en(43) + 0.3, x0=40)                                        # K
q('&#8220;Can I help with <i>anything</i>?&#8221;', at(43, 'Can I') - 0.1, en(43) + 0.3, QR, size=60)
full([(C('a5_plates12', 4.47, 10.5), nx(44)), (C('a5_plates22', 0.7, 3.2), at(44, 'they carry'))], at(44, 'And the next') - 0.1)
full([(C('a5_morning26', 0.0, 8.0), at(44, 'And the next') - 0.2)], at(44, 'Thank you') - 0.1)
CROP['a5_morning29'] = (40, 0, 1120)                                                                     # above the watermark
vframe([(C('a5_morning29', 0.0, 5.0), at(44, 'Thank you') - 0.3), (C('a5_tart13', 0.0, 3.17), at(44, 'That lemon'))], en(44) + 0.3, x0=40)   # K
q('&#8220;Thank you for last night.<br>That lemon tart was <i>heavenly</i>.&#8221;', at(44, 'Thank you'), en(44) + 0.3, QR, size=56)
side([(C('a5_plates38', 0.0, 7.0), nx(45))], en(45) + 0.35)                                              # I
q('&#8220;I noticed the <i>effort</i><br>you made for us.&#8221;', at(45, 'I noticed') - 0.1, en(45) + 0.3, QI, size=60)
full([(C('a6_family31', 0.0, 6.93), nx(46))], en(46) + 0.35)                                                # F
q('&#8220;Their name is always first<br>on the next guest <i>list</i>.&#8221;', st(46) + 0.2, en(46) + 0.3, QC, cls='over')

# ================= 6. SHARING THE CREDIT =================
card_at('6. Sharing the Credit', 47, at(47, 'at work'))
row([C('a6_office19', 0.0, 5.97), C('a6_family2', 0.3, 9.0), C('b6_trip11', 0.0, 7.0)],                    # G: work, families, friends
    [at(47, 'at work') - 0.2, at(47, 'in families'), at(47, 'among friends')], nx(48))
full([(C('a6_party3', 0.0, 6.47), nx(48)), (C('b6_present29', 0.0, 5.37), at(48, 'The project')),
      (C('b6_trip40', 3.0, 9.36), at(48, 'The trip')), (C('a6_team5', 2.0, 12.0), at(48, 'And everyone'))], en(48) + 0.35)
q('&#8220;Well <i>done</i>!&#8221;', at(48, 'Well done') - 0.1, en(48) + 0.3, QC, size=80, cls='over')
onwhite([(C('a6_smile41', 0.3, 6.5), nx(49))], en(49) + 0.3)                                             # E
vframe([(C('a6_office39', 18.8, 26.67), nx(50))], en(50) + 0.3, x0=40)                                   # K: the two sentences
q('&#8220;Thank you. But honestly,<br>it was <i>Sarah&#8217;s</i> idea.&#8221;', at(50, 'Thank you') - 0.1, en(50) + 0.25, (650, 230, 1860, 520), size=54)
q('&#8220;I couldn&#8217;t have done it<br>without <i>Mark</i>.&#8221;', at(50, "I couldn't") - 0.1, en(50) + 0.25, (650, 580, 1860, 860), size=54)
side([(C('h_film19', 0.0, 5.83), nx(51))], en(51) + 0.35)                                               # I: Grace Kelly
q('&#8220;It makes them look even<br>more <i>gracious</i>.&#8221;', at(51, 'If anything'), en(51) + 0.3, QI, size=60)
full([(C('a6_party41', 0.0, 5.67), nx(52))], nx(53))
FACEFIX['b6_hug1'] = 0.5
full([(C('b6_hug1', 0.0, 5.6), nx(53))], en(53) + 0.35)                                                  # F
q('&#8220;People never forget who said<br>their <i>name</i>.&#8221;', st(53) + 0.2, en(53) + 0.3, QC, cls='over')

# ================= 7. APOLOGISING CLEANLY =================
card_at('7. Apologising Cleanly', 54, st(54) + 3.4)
full([(C('a7_film9', 9.59, 16.93), st(54) + 3.2)], nx(55))                                              # Pride and Prejudice
vframe([(C('a7_serious18', 0.3, 9.6), nx(55))], en(55) + 0.3, x0=40)                                    # K: the three non-apologies
for k_, (ph_, txt_) in enumerate([("I'm sorry if", '&#8220;I&#8217;m sorry if you felt that way.&#8221;'),
                                  ("I'm sorry, but", '&#8220;I&#8217;m sorry, <i>but</i> you have to understand&#8230;&#8221;'),
                                  ('Sorry! Anyway', '&#8220;Sorry! Anyway&#8230;&#8221;')]):
    q(txt_, at(55, ph_) - 0.05, en(55) + 0.25, (650, 230 + k_ * 210, 1860, 430 + k_ * 210), size=50)
FACEFIX['a7_serious34'] = 0.5
full([(C('a7_serious34', 0.3, 8.0), nx(56))], nx(57))
side([(C('a7_film33', 0.0, 7.6), nx(57))], en(57) + 0.35)                                               # I
q('When they really are in the wrong,<br>they say it <i>cleanly</i>.', at(57, 'But when'), en(57) + 0.3, QI, size=56)
vframe([(C('h_lunch14', 0.3, 8.3), nx(58))], en(58) + 0.3, x0=40)                                       # K: the clean apology, word for word
q('&#8220;I&#8217;m sorry. I was wrong to say that.<br>It won&#8217;t happen <i>again</i>.&#8221;', st(58) + 0.05, en(58) + 0.35, QR, size=56)
onwhite([(C('z_everyday21', 0.0, 7.4), nx(59))], en(59) + 0.3)                                          # E
FACEFIX['h_audrey21'] = 0.5
full([(C('h_audrey21', 2.0, 8.0), nx(60))], nx(61))                                                     # Roman Holiday
full([(C('a7_sorry48', 5.5, 12.0), nx(61)), (C('a7_walk3', 0.0, 7.48), at(61, 'A clean') - 0.2)], en(61) + 0.35)   # F
q('&#8220;A clean apology closes a moment that<br>could otherwise stay open for <i>years</i>.&#8221;', at(61, 'A clean'), en(61) + 0.3, QC, size=54, cls='over')

# ================= CLOSE =================
onwhite([(C('z_older31', 0.0, 9.12), nx(62)), (C('z_everyday44', 0.0, 9.53), at(62, "They're small"))], en(62) + 0.3)   # E
row([C('z_older10', 0.0, 9.77), C('z_everyday45', 0.0, 7.23), C('h_lunch33', 1.73, 10.27)],               # G: one or two, any woman
    [nx(63), at(63, 'Even practising'), at(63, 'how people feel')], en(63) + 0.3)
side([(C('z_everyday23', 0.0, 9.17), nx(64))], en(64) + 0.35)                                           # I: as Part 1 at 6:46
q('&#8220;Real class was never about being flawless.<br><i>It&#8217;s about care.</i>&#8221;', st(64) + 0.1, en(64) + 0.3, QI, size=54)
vframe([(C('h_calm18', 9.03, 15.93), nx(65))], en(65) + 0.3)                                            # J: centred on caramel
full([(C('z_everyday15', 0.0, 6.67), nx(66)), (C('h_film35', 5.8, 11.0), at(66, "It's about noticing"))], nx(67))
full([(C('h_lunch34', 0.0, 6.5), nx(67))], nx(68))
full([(C('h_city48', 0.0, 9.0), nx(68)), (C('h_quiet17', 2.0, 12.4), nx(69))], total - 2.6)            # N, then the end card
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>', nx(68) + 0.3, en(68) + 0.4, QC, cls='over')
