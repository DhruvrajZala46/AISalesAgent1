# 7 Things Classy Women Never Do in Public - the edit, beat by beat.
# Built ONLY from the layouts of the creator's own "7 Things Elegant Ladies Never Do in Public" (oHh4T67jJNM), read off
# its storyboard (videos/classy-women-public/VISUAL-ANALYSIS.md):
#   A full-screen clip | B title over a clip | C white card | D rounded vertical frame on caramel | E rounded frame left +
#   quote right | F quote over a full clip | G three panels | J quote above a wide rounded frame | K quote alone |
#   L vertical clip on cream | M clip left on cream + dark text right | N guide over clips | O outro over clips | P end card
# Footage: Pinterest video pins (Instagram/TikTok creators' reels) and film scenes found there. No free-stock sites.
# Every clip appears ONCE. No sound effects; soft solo piano ~12 dB under the voice (build.py).

import os as _os

els.append('''<style>
.cream { position:absolute; inset:0; background:#f6f0e9; }
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
FACEFIX = {'p3_conv24': 0.35, 'p2_softcall15': 0.33, 'p2_laughgroup34': 0.45, 'g_hair27': 0.3,       # detector misses, read by eye
           'p5_nail14': 0.5, 'p6_bestfriends24': 0.5, 'p7_alone24': 0.45, 'x_airpods40': 0.5, 'g_mirror2': 0.28,
           'p2_softcall18': 0.5, 'p6_bestfriends8': 0.515}
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

def card_at(txt, i_line, t_out):
    """C: the white card, black script wiping in; it stays over the first words of the point, as in the original"""
    t0 = en(i_line - 1) + 0.35
    white(t0, t_out); text(txt, 'card', t0 + 0.3, t_out - 0.1, dur=1.2, out=0.45)

# ================= HOOK (A: full-screen clips of women in cafes and restaurants, ~5 s each) =================
full([(C('h_cafe0', 0.3, 7.9), 0.0, 0.35), (C('h_cafe39', 0.3, 7.3), at(1, 'who seems'), 0.4)], nx(2))
full([(C('p6_party41', 10.6, 13.8), nx(2), 0.4), (C('h_cafe41', 0.3, 6.8), at(2, 'fussing'), 0.45),
      (C('h_phonedown31', 0.3, 10.0), at(2, 'scrolling'), 0.4)], nx(3))
full([(C('h_film2', 0.3, 4.6), nx(3))], nx(4))                                                   # Casablanca: the one you remember
full([(C('h_walk26', 0.3, 9.2), nx(4), 0.4), (C('p7_alone23', 0.3, 7.8), at(4, 'It comes'), 0.45)], nx(5))

# ================= THE TURN (B: the title over a full-screen clip) =================
full([(C('h_walk40', 0.3, 6.2), nx(5), 0.35), (C('h_public23', 0.3, 9.7), at(5, 'and the gentle'), 0.4)], nx(6))
q('7 Things Classy Women Never Do in <i>Public</i>', at(5, 'seven') - 0.2, at(5, 'and the gentle') - 0.3, QC, size=78, cls='over')
row([C('h_public8', 0.3, 9.4), C('h_public5', 0.3, 7.8), C('h_public29', 5.3, 10.9)],                # G: you'll see them everywhere
    [nx(6), at(6, 'One or two'), at(6, "you'll see")], en(6) + 0.3)

# ================= 1. PUTTING YOURSELF DOWN =================
card_at('1. Putting Yourself Down', 7, st(7) + 3.4)
full([(C('p1_mirror36', 0.3, 9.0), st(7) + 3.2, 0.35)], nx(8))
vframe([(C('p1_photo0', 0.3, 9.0), nx(8))], en(8) + 0.3, x0=40)                                    # E: the three put-downs, word for word
q('&#8220;Ugh, I look awful in that photo.&#8221;', st(8) + 0.05, en(8) + 0.25, (650, 210, 1860, 420), size=54)
q('&#8220;Don&#8217;t mind me, I&#8217;m such a <i>mess</i> today.&#8221;', at(8, "Don't mind"), en(8) + 0.25, (650, 430, 1860, 640), size=54)
q('&#8220;Sorry, I&#8217;m <i>hopeless</i> at this.&#8221;', at(8, 'Sorry'), en(8) + 0.25, (650, 650, 1860, 860), size=54)
full([(C('p1_photoshow24', 0.3, 9.9), nx(9), 0.4)], nx(10))
q('&#8220;Every little put-down is still a sentence about <i>you</i>,<br>said out loud.&#8221;', st(10) + 0.1, en(10) + 0.3, QC)   # K
vframe([(C('p1_laugh25', 2.2, 9.4), nx(11))], nx(12))                                              # D
oncream([(C('z_spill5', 0.3, 5.3), nx(12)), (C('p1_selfie6', 1.4, 5.6), nx(13)),             # M: each swap beside her
         (C('p1_learn36', 0.3, 9.0), nx(14))], en(14) + 0.35, x0=75)
q('Instead of &#8220;I&#8217;m so clumsy,&#8221;<br>just smile: &#8220;<i>Oops.</i>&#8221;', st(12), en(12) + 0.1, MT, size=56, cls='dark')
q('Instead of &#8220;I look awful in this one,&#8221;<br>&#8220;Let&#8217;s take <i>one more</i>.&#8221;', st(13), en(13) + 0.1, MT, size=56, cls='dark')
q('Instead of &#8220;I&#8217;m hopeless at this,&#8221;<br>&#8220;I&#8217;m still <i>learning</i>.&#8221;', st(14), en(14) + 0.3, MT, size=56, cls='dark')
full([(C('p6_bestfriends8', 0.3, 9.4), nx(15), 0.6)], nx(16))
full([(C('p7_leave48', 6.3, 10.8), nx(16), 0.35)], en(16) + 0.35)                                      # F
q('&#8220;That isn&#8217;t vanity.<br>It&#8217;s <i>self-respect</i>, spoken out loud.&#8221;', st(16) + 0.1, en(16) + 0.3, QC, cls='over')

# ================= 2. LOUD PHONE CALLS =================
card_at('2. Loud Phone Calls', 17, st(17) + 3.2)
full([(C('p2_trainphone19', 0.3, 6.4), st(17) + 3.0, 0.4)], nx(18))
row([C('p2_videophone33', 0.3, 9.0), C('p2_queue9', 0.3, 10.3), C('p2_waiting2', 0.2, 2.1)],          # G: train, waiting room, queue
    [nx(18), at(18, 'in the waiting'), at(18, 'in the pharmacy')], at(18, 'The phone') - 0.1)
CROP['x_speaker5'] = (50, 190, 1090)                                                                # past the brand mark top right
vframe([(C('x_speaker5', 0.3, 6.4), at(18, 'The phone') - 0.2), (C('x_loudvideo42', 0.3, 3.4), at(18, 'A video'))], en(18) + 0.3)  # D
wide([(C('p2_videophone2', 0.3, 12.0), nx(19), 0.5)], en(19) + 0.35)                                 # J
q('&#8220;Everyone nearby becomes part of that <i>call</i>,<br>whether they chose to or not.&#8221;', st(19) + 0.1, en(19) + 0.3, QT, size=52)
full([(C('x_whisper19', 0.3, 10.0), nx(20), 0.35)], nx(21))
vframe([(C('p2_trainphone0', 0.3, 9.0), nx(21))], en(21) + 0.3, x0=40)                                # E
q('&#8220;I&#8217;m on the train right now.<br>Can I call you back in <i>ten minutes</i>?&#8221;', at(21, "I'm on"), en(21) + 0.3, QR)
full([(C('x_airpods40', 0.3, 7.3), nx(22), 0.6), (C('p2_softcall15', 2.0, 12.0), at(22, 'And let'), 0.4)], nx(23))
full([(C('p2_laughgroup34', 0.3, 7.9), nx(23), 0.4), (C('p1_laugh42', 4.3, 11.2), at(23, 'Be warm'), 0.45)], nx(24))
full([(C('p2_softcall18', 0.0, 4.2), nx(24), 0.35), (C('h_cafe21', 0.3, 9.4), at(24, 'Discretion'), 0.35)], en(24) + 0.35)
q('&#8220;Discretion is its own quiet kind of <i>confidence</i>.&#8221;', at(24, 'Discretion'), en(24) + 0.3, QC, cls='over')   # F

# ================= 3. ASKING PERSONAL QUESTIONS =================
card_at('3. Asking Personal Questions', 25, st(25) + 3.3)
full([(C('p3_greet0', 2.4, 4.6), st(25) + 3.1, 0.4)], nx(26))
full([(C('p3_conv24', 0.3, 5.7), nx(26), 0.45)], nx(27))
vframe([(C('p3_bag29', 0.3, 9.0), nx(27))], en(27) + 0.3, x0=40)                                     # E: the four questions
for k_, (ph_, txt_) in enumerate([('How much', '&#8220;How much did that cost?&#8221;'), ('What do', '&#8220;What do you earn?&#8221;'),
                                  ('When are', '&#8220;When are you two having a <i>baby</i>?&#8221;'), ('Have you', '&#8220;Have you put on weight?&#8221;')]):
    q(txt_, at(27, ph_) - 0.05, en(27) + 0.25, (650, 170 + k_ * 180, 1860, 350 + k_ * 180), size=52)
full([(C('p3_conv36', 5.3, 14.3), nx(28), 0.45)], at(28, 'A money') - 0.1)
row([C('y_quiet6', 0.0, 3.6), C('y_photos1', 0.3, 8.1), C('y_thought2', 0.3, 5.0)],             # G: the story behind the answer
    [at(28, 'A money') - 0.2, at(28, 'a loss'), at(28, 'a hope')], en(28) - 0.05)
vframe([(C('h_cafe22', 0.3, 6.0), nx(29))], en(29) + 0.3, x0=40)                                     # E
q('&#8220;Elegant women let people decide how much<br>of their life they <i>share</i>, and when.&#8221;', st(29) + 0.1, en(29) + 0.3, QR, size=54)
oncream([(C('p6_listen33', 0.3, 13.0), nx(30))], en(30) + 0.3, x0=75)                                 # M
q('Questions that open a door,<br>without <i>pushing</i> it.', st(30) + 0.2, at(30, 'How have') - 0.25, MT, size=58, cls='dark')
q('&#8220;How have you <i>been</i>?&#8221;', at(30, 'How have'), en(30) + 0.25, (760, 300, 1840, 520), size=60, cls='dark')
q('&#8220;What&#8217;s been keeping you<br><i>busy</i> lately?&#8221;', at(30, "What's been"), en(30) + 0.25, (760, 540, 1840, 800), size=60, cls='dark')
oncream([(C('p3_greet36', 0.3, 5.2), nx(31)), (C('p5_arrive16', 0.3, 6.2), at(31, 'a warm smile'))], en(31) + 0.3)   # L
q('&#8220;Oh, that&#8217;s a story<br>for <i>another day</i>.&#8221;', at(31, "Oh, that's"), en(31) + 0.25, (1270, 60, 1890, 1020), size=52, cls='dark')
full([(C('p3_olderwalk4', 0.3, 8.0), nx(32), 0.45)], en(32) + 0.35)                                 # F
q('&#8220;Elegance gives people <i>room</i>.<br>Room to share, and room not to.&#8221;', st(32) + 0.1, en(32) + 0.3, QC, cls='over')

# ================= THE GUIDE (N: text over full-screen clips) =================
vframe([(C('c_walkold0', 6.3, 14.8), nx(33))], nx(34))                                            # D
full([(C('g_drape0', 0.3, 4.9), nx(34), 0.45), (C('g_mirror2', 0.3, 6.9), at(34, 'the shapes'), 0.4),
      (C('g_hair27', 0.3, 9.0), at(34, 'the hairstyles'), 0.35)], nx(35))
full([(C('g_mirror38', 0.3, 10.2), nx(35), 0.4), (C('p7_leave13', 0.3, 9.9), at(35, 'so getting'), 0.4)], en(36) + 0.35)
q('<div><span style="font-size:44px">Discover Your Best Look</span><br><i style="font-size:120px">Elegance &amp; Style Guides</i><br>'
  '<span style="font-size:34px;letter-spacing:1px">www.classyladyacademy.com</span></div>', at(35, 'our elegance') - 0.2, en(36) + 0.2, QC, cls='over')

# ================= 4. BICKERING IN FRONT OF OTHERS =================
card_at('4. Bickering in Front of Others', 37, st(37) + 3.4)
full([(C('p4_armarm1', 0.3, 10.3), st(37) + 3.2, 0.45)], nx(38))
full([(C('p6_party33', 0.3, 5.0), nx(38), 0.45)], at(38, 'Well, he') - 0.3)
vframe([(C('p4_couplerest16', 0.3, 7.0), at(38, 'Well, he') - 0.3)], at(38, 'Or a') + 0.1, x0=40)     # E: the remark, word for word
q('&#8220;Well, he never <i>listens</i> anyway.&#8221;', at(38, 'Well, he'), at(38, 'Or a'), QR)
full([(C('p3_dinnergroup14', 0.3, 12.0), at(38, 'Or a'), 0.45)], nx(39))
row([C('p6_meet25', 0.3, 5.5), C('h_dinner25', 5.9, 12.0), C('p6_party12', 0.3, 6.0)],                # G: everyone else, their plates
    [nx(39), at(39, 'everyone else'), at(39, 'their plate')], en(39) + 0.3)
full([(C('p4_touch3', 0.3, 7.5), nx(40), 0.45)], nx(41))
vframe([(C('p4_touch40', 0.3, 7.2), nx(41)), (C('p4_touch4', 2.3, 10.0), at(41, 'a light touch'))], en(41) + 0.3, x0=40)   # E
q('&#8220;Gently move the <i>moment</i>.&#8221;', st(41) + 0.3, en(41) + 0.3, (650, 250, 1860, 470), size=56)
q('&#8220;Let&#8217;s talk about this <i>at home</i>.&#8221;', at(41, "Let's talk") - 0.1, en(41) + 0.3, (650, 520, 1860, 760), size=56)
wide([(C('p4_couplerest0', 0.3, 12.5), nx(42), 0.42)], en(42) + 0.35)                                   # J
q('&#8220;It&#8217;s choosing a quieter room<br>for the real <i>conversation</i>.&#8221;', at(42, "That isn't") - 0.2, en(42) + 0.3, QT, size=52)
full([(C('p4_armarm16', 0.3, 10.4), nx(43), 0.4)], en(43) + 0.35)                                   # F
q('&#8220;The people we love should always feel <i>safe</i> beside us.&#8221;', st(43) + 0.1, en(43) + 0.3, QC, cls='over')

# ================= 5. GETTING READY AT THE TABLE =================
card_at('5. Getting Ready at the Table', 44, en(44) + 0.35)
CROP['p5_trainmakeup11'] = (36, 130, 1150); CROP['p5_compact16'] = (40, 175, 1100)                  # past the small captions on top
full([(C('p5_brush36', 0.3, 5.6), nx(45), 0.45), (C('p5_trainmakeup11', 2.0, 10.0), at(45, 'A full face'), 0.42),   # A: one picture per noun
      (C('p5_nail14', 0.3, 4.8), at(45, 'A nail'), 0.5)], en(45) + 0.3)
oncream([(C('p7_alonecafe26', 0.9, 5.5), nx(46)),
         (C('p5_carmirror4', 8.7, 14.0), at(46, 'And while') - 0.2)], en(46) + 0.3, x0=75)   # M
q('&#8220;People are closer<br>than we <i>think</i>.&#8221;', at(46, 'But people') - 0.1, at(46, 'And while') - 0.3, MT, size=58, cls='dark')
q('&#8220;While we&#8217;re fixing ourselves,<br>we&#8217;re only <i>half there</i>.&#8221;', at(46, 'And while') - 0.2, en(46) + 0.3, MT, size=58, cls='dark')
row([C('p5_getready25', 0.0, 4.5), C('p5_carmirror2', 0.3, 9.0), C('p5_compact16', 0.3, 9.5)],         # G: at home, in the car, the powder room
    [at(47, 'At home') - 0.2, at(47, 'in the car'), at(47, 'a quiet minute')], en(47) - 0.6)
full([(C('p5_getready10', 4.3, 9.0), nx(47), 0.4)], at(47, 'At home') - 0.1)
vframe([(C('p5_compact4', 3.3, 10.8), nx(48))], en(48) + 0.3, x0=40)                                 # E
q('&#8220;Excuse me for <i>a moment</i>.&#8221;', at(48, 'A simple') - 0.1, en(48) + 0.3, QR)
full([(C('p5_lipbalm0', 3.3, 6.3), nx(49), 0.5), (C('h_public2', 0.3, 4.5), at(49, 'On a rushed'), 0.4)], nx(50))
full([(C('p5_arrive14', 0.3, 8.5), nx(50), 0.4)], en(50) + 0.35)                                    # F
q('&#8220;All that&#8217;s left is the lovely part:<br>being there, calm and fully <i>present</i>.&#8221;', at(50, "all that's") - 0.1, en(50) + 0.3, QC, cls='over')

# ================= 6. RUSHING TO NICKNAMES =================
card_at('6. Rushing to Nicknames', 51, en(51) + 0.35)
oncream([(C('p6_meet45', 0.1, 6.8), nx(52)), (C('p6_meet6', 3.3, 8.0), at(52, 'Or someone'))], en(52) + 0.3, x0=75)   # M
q('&#8220;Hi, I&#8217;m <i>Elizabeth</i>.&#8221;', at(52, 'Elizabeth') - 0.3, en(52) + 0.25, (760, 200, 1840, 400), size=60, cls='dark')
q('&#8220;Liz!&#8221;', at(52, 'Liz'), en(52) + 0.25, (760, 420, 1840, 560), size=60, cls='dark')
q('&#8220;hun&#8221; &nbsp;&#183;&nbsp; &#8220;sweetie&#8221;', at(52, 'hun'), en(52) + 0.25, (760, 600, 1840, 760), size=56, cls='dark')
vframe([(C('p6_listen1', 0.3, 9.0), nx(53))], en(53) + 0.3, x0=40)                                   # E
q('&#8220;A name is <i>personal</i>.&#8221;', at(53, 'But a name') - 0.1, en(53) + 0.3, QR, size=62)
full([(C('p6_meet16', 8.2, 11.9), nx(54), 0.4), (C('p6_meet14', 0.3, 8.0), at(54, 'and lets'), 0.45)], nx(55))
vframe([(C('p6_listen37', 0.3, 9.0), nx(55))], en(55) + 0.3, x0=40)                                  # E
q('&#8220;Do you prefer <i>Elizabeth</i>,<br>or Liz?&#8221;', at(55, 'Do you') - 0.1, en(55) + 0.3, QR, size=62)
full([(C('p6_waitress6', 1.6, 6.8), nx(56), 0.4),       (C('p3_greet4', 0.3, 3.3), at(56, 'This is only'), 0.4)], nx(57))
full([(C('p6_bestfriends24', 0.3, 8.5), nx(57), 0.45)], en(57) + 0.35)                             # F
q('&#8220;Warmth is in saying someone&#8217;s name<br>as if it <i>matters</i>.&#8221;', at(57, "It's in") - 0.2, en(57) + 0.3, QC, cls='over')

# ================= 7. HIDING BEHIND YOUR PHONE (the one to remember) =================
card_at('7. Hiding Behind Your Phone', 58, st(58) + 3.6)
full([(C('p7_alone24', 0.3, 10.0), st(58) + 3.4, 0.4)], nx(59))
full([(C('p7_alone3', 0.3, 6.5), nx(59), 0.4), (C('p7_alone16', 0.3, 3.0), at(59, 'or eat'), 0.4),
      (C('p7_alone4', 0.3, 6.4), at(59, "there's no"), 0.4)], nx(60))
full([(C('p7_alonecafe32', 0.3, 7.2), nx(60), 0.45), (C('p7_alonecafe28', 0.3, 4.7), at(60, "You're not"), 0.4)], nx(61))
vframe([(C('p7_bag6', 0.3, 5.0), nx(61))], en(61) + 0.3, x0=40)                                      # E
q('&#8220;Let the phone rest in your bag,<br>so they have <i>all of you</i>.&#8221;', st(61) + 0.4, en(61) + 0.3, QR, size=56)
oncream([(C('x_tidy23', 0.3, 5.6), nx(62))], at(62, 'and say') - 0.1, x0=75)   # M
q('Push your chair back in,<br>gather your <i>cup</i>.', at(62, 'push your'), at(62, 'and say') - 0.1, MT, size=58, cls='dark')
full([(C('z_leave8', 0.3, 6.3), at(62, 'and say') - 0.2, 0.3)], nx(63))
q('&#8220;Thank you, that was <i>lovely</i>.&#8221;', at(62, 'Thank you') - 0.1, en(62) + 0.2, QC, cls='over')
full([(C('p7_filmleave38', 0.3, 12.0), nx(63), 0.35)], en(63) + 0.35)                               # F: My Fair Lady
q('&#8220;That&#8217;s exactly the kind of elegance people remember,<br>even when they can&#8217;t quite say <i>why</i>.&#8221;',
  at(63, "And that's") - 0.1, en(63) + 0.3, QC, size=54, cls='over')

# ================= CLOSE =================
oncream([(C('p7_older11', 0.3, 7.1), nx(64))], en(64) + 0.3)                                         # L
full([(C('z_elegant2', 0.3, 8.0), nx(65), 0.35), (C('p7_thanks31', 0.3, 8.0), at(65, 'And tell me'), 0.4)], nx(66))
full([(C('c_rail0', 0.3, 7.2), nx(66), 0.45), (C('p7_leave41', 0.3, 7.3), nx(67), 0.4)], total - 2.6)   # O, then the end card
q('<div><span style="font-size:44px">Check The Description For</span><br><i style="font-size:116px">Personal Stylist Guide</i><br>'
  '<span style="font-size:34px;letter-spacing:1px">www.classyladyacademy.com</span></div>', nx(66) + 0.3, at(66, 'and our favourite') - 0.2, QC, cls='over')
q('<i style="font-size:116px">Elegant Clothing Links</i>', at(66, 'and our favourite'), en(66) + 0.4, QC, cls='over')
