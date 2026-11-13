# build.py - Kangen reel 5 (Hindi, 88 s, Mayank style): grandfather vs today -> RO strips minerals -> Enagic Kangen
import json, os, subprocess
P = os.path.dirname(os.path.abspath(__file__)); os.chdir(P)
B = json.load(open('beats.json')); DUR = round(B[-1]['end'] + 1.6, 2)
W, H = 1080, 1920
def sh(c): subprocess.run(c, shell=True, check=True)
def at(i, word, k=0, end=False):
    hits = [w for w in B[i - 1]['words'] if word in w[0]]
    assert len(hits) > k, (i, word)
    return hits[k][2] if end else hits[k][1]
st = lambda i: B[i - 1]['start'] - 0.05
def dur(src): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'raw/{src}.mp4'], capture_output=True, text=True).stdout)

def cut(name, src, a, need, w=W, h=H, crop=None, slow=None):
    """crop = (x0, y0, cw, ch) as fractions of the source frame"""
    out = f'assets/{name}.mp4'
    if not os.path.exists(out):
        avail = max(0.5, dur(src) - a); speed = 1.0
        if avail < need + 0.2: speed = max(0.45, avail / (need + 0.2))
        if slow: speed = slow
        take = min(avail, (need + 0.2) * speed)
        pre = f"crop=iw*{crop[2]}:ih*{crop[3]}:iw*{crop[0]}:ih*{crop[1]}," if crop else ""
        vf = f"{pre}setpts=PTS/{speed},scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},fps=30"
        sh(f'ffmpeg -y -v error -ss {a} -t {take:.3f} -i raw/{src}.mp4 -an -vf "{vf}" -c:v libx264 -crf 19 -preset veryfast -g 30 -keyint_min 30 -pix_fmt yuv420p -movflags +faststart {out}')
    return out

els, tw, SFX = [], [], []
def T(s): tw.append(s)
n = [0]
def nid(p='e'): n[0] += 1; return f'{p}{n[0]}'
def sfx(t, f, g=-14): SFX.append((round(t, 3), f, g))
def vis(i, t0, t1=None):
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});')
    if t1 is not None and t1 < DUR: T(f'tl.set("#{i}",{{visibility:"hidden"}},{t1:.3f});')
def key(*parts): return '_'.join(str(p) for p in parts).replace('.', 'p').replace(' ', '').replace(',', '-').replace('(', '').replace(')', '')

def shot(src, a, t0, t1, cls='', crop=None, zoom=(1.0, 1.08), slow=None, inner='', ease='none'):
    i = nid('sh'); f = cut(key(src, a, int(t0 * 10), crop, slow), src, a, t1 - t0, crop=crop, slow=slow)
    els.append(f'<div class="shot {cls}" id="{i}"><div class="zw" id="{i}z"><video id="{i}v" src="{f}" muted playsinline data-start="{t0:.3f}" data-duration="{t1 - t0 + 0.05:.3f}"></video>{inner}</div></div>')
    vis(i, t0, t1)
    T(f'tl.fromTo("#{i}z",{{scale:{zoom[0]}}},{{scale:{zoom[1]},duration:{t1 - t0:.3f},ease:"{ease}"}},{t0:.3f});')
    return i

def paper(t0, t1, inner, zoom=(1.0, 1.04)):
    i = nid('pa')
    els.append(f'<div class="shot" id="{i}"><div class="zw" id="{i}z"><div class="paper"></div>{inner}</div></div>')
    vis(i, t0, t1)
    T(f'tl.fromTo("#{i}z",{{scale:{zoom[0]}}},{{scale:{zoom[1]},duration:{t1 - t0:.3f},ease:"none"}},{t0:.3f});')
    return i

def printv(src, a, t0, t1, x, y, w, h, rot=-3, cap='', crop=None, cls='', slow=None):
    """a video photo-print pinned on paper; returns (html, id)"""
    i = nid('pr'); f = cut(key('pr', src, a, w, h, int(t0 * 10), slow), src, a, t1 - t0, w, h, crop=crop, slow=slow)
    html = (f'<div class="print {cls}" id="{i}" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)"><div class="tape"></div>'
            f'<video id="{i}v" src="{f}" muted playsinline style="width:{w}px;height:{h}px" data-start="{t0:.3f}" data-duration="{t1 - t0 + 0.05:.3f}"></video>'
            f'<div class="cap">{cap}</div></div>')
    return html, i

def hl(kick, punch, t0, t1, tp=None, color='', big=False):
    i = nid('hl')
    kw = ''.join(f'<span class="w">{w}</span> ' for w in kick.split())
    pw = ''.join(f'<span class="w">{w}</span> ' for w in punch.split())
    els.append(f'<div class="hl" id="{i}"><span class="k">{kw}</span><span class="p {color}"{" style=font-size:150px" if big else ""}>{pw}</span></div>')
    tp = tp if tp is not None else t0 + 0.35
    vis(i, t0, t1)
    if kick: T(f'tl.fromTo("#{i} .k .w",{{autoAlpha:0,y:26}},{{autoAlpha:1,y:0,duration:.22,stagger:.06,ease:"power3.out"}},{t0:.3f});')
    if punch:
        T(f'tl.fromTo("#{i} .p .w",{{autoAlpha:0,y:40,scale:1.25}},{{autoAlpha:1,y:0,scale:1,duration:.28,stagger:.08,ease:"back.out(2)"}},{tp:.3f});')
        sfx(tp, 'sfx3005', -21)
    return i

def el(html, t0, t1, frm='autoAlpha:0,scale:0.6', ease='back.out(2)', d=0.35, s=None, g=-16, to=''):
    i = nid('x'); els.append(html.replace('ID', i))
    vis(i, t0, t1)
    T(f'tl.fromTo("#{i}",{{{frm}}},{{autoAlpha:1,scale:1,x:0,y:0,{to}duration:{d},ease:"{ease}"}},{t0:.3f});')
    if s: sfx(t0, s, g)
    return i

def stamp(text, t0, t1, top=820, cls=''):
    i = nid('st'); els.append(f'<div class="stamp {cls}" id="{i}" style="top:{top}px">{text}</div>')
    vis(i, t0, t1)
    T(f'tl.fromTo("#{i}",{{autoAlpha:0,scale:2.8,rotation:-24}},{{autoAlpha:1,scale:1,rotation:-8,duration:.25,ease:"power4.in"}},{t0:.3f});')
    sfx(t0 + 0.2, 'sfx2364', -11)

def split(t0, t1, top, bot, la, lb, ta=None, tb=None, colb='var(--y)'):
    """top/bot = (src, a, crop, slow, cls); labels pop in at ta/tb"""
    i = nid('sp'); hv = []
    for half, (src, a, crop, slow, cls) in (('a', top), ('b', bot)):
        f = cut(key('h', src, a, int(t0 * 10), crop, slow), src, a, t1 - t0, 1080, 960, crop=crop, slow=slow)
        hv.append((half, f, cls))
    labs = {'a': la, 'b': lb}
    inner = ''.join(f'<div class="half {h} {c}"><video id="{i}{h}" src="{f}" muted playsinline data-start="{t0:.3f}" data-duration="{t1 - t0 + 0.05:.3f}"></video>'
                    f'<div class="lab" id="{i}l{h}" style="visibility:hidden{";color:" + colb if h == "b" else ""}">{labs[h]}</div></div>' for h, f, c in hv)
    els.append(f'<div class="split" id="{i}">{inner}<div class="line"></div></div>')
    vis(i, t0, t1)
    T(f'tl.fromTo("#{i} .half.a",{{x:-1080}},{{x:0,duration:.35,ease:"power3.out"}},{t0:.3f});tl.fromTo("#{i} .half.b",{{x:1080}},{{x:0,duration:.35,ease:"power3.out"}},{t0:.3f});')
    for h, t in (('a', ta if ta is not None else t0 + 0.3), ('b', tb if tb is not None else t0 + 0.5)):
        T(f'tl.set("#{i}l{h}",{{visibility:"visible"}},{t:.3f});tl.fromTo("#{i}l{h}",{{autoAlpha:0,y:30,scale:1.2}},{{autoAlpha:1,y:0,scale:1,duration:.3,ease:"back.out(2)"}},{t:.3f});')
        sfx(t, 'sfx3005', -19)
    sfx(t0, 'sfx166', -19)
    return i

def flash(t):
    i = nid('fl'); els.append(f'<div class="flash" id="{i}"></div>')
    vis(i, t, t + 0.5)
    T(f'tl.fromTo("#{i}",{{opacity:0}},{{opacity:.9,duration:.08}},{t:.3f});tl.to("#{i}",{{opacity:0,duration:.4}},{t + 0.08:.3f});')

CUTS = []  # soft whoosh on scene changes
# ============================ 1. HOOK: grandfather (memory, sepia) ============================
t_a = 0.0; t_b = at(1, 'खेत') - 0.12; t_c = st(2)
shot('kisan1', 2.0, t_a, t_b, 'mem', zoom=(1.12, 1.0))
shot('kisan33', 16.0, t_b, t_c + 0.45, 'mem', crop=(0.12, 0.24, 0.76, 0.76), zoom=(1.0, 1.1))
hl('हमारे दादाजी', '80 में भी हल!', 0.0, t_c, tp=at(1, 'अस्सी') - 0.05, color='y')
sfx(0.0, 'sfx498', -9); sfx(at(1, 'हल'), 'sfx1143', -17); CUTS.append(t_b)
# ============================ 2. today: tired shopkeeper (split then/now) ============================
t_d = st(3)
split(t_c, t_d, ('kisan1', 4.0, None, None, 'mem'), ('shopk31', 3.0, None, None, ''),
      'तब<small>80 में भी मेहनत</small>', 'अब<small>45 में ही थकान</small>', ta=t_c + 0.3, tb=at(2, 'पैंतालीस') - 0.05, colb='var(--r)')
bt = el('<div class="bat" id="ID"><i></i></div>', at(2, 'दुकान') - 0.1, t_d, 'autoAlpha:0,scale:0.5', s='sfx3005', g=-18)
T(f'tl.fromTo("#{bt} i",{{width:"92%",backgroundColor:"#3ddc84"}},{{width:"14%",backgroundColor:"#ff4b3e",duration:1.1,ease:"power2.in",immediateRender:false}},{at(2, "थक") - 0.35:.3f});')
sfx(at(2, 'थक') - 0.3, 'sfx1317', -19)
# ============================ 3. "food changed... one more thing changed" ============================
t_e = at(3, 'पर') - 0.12; t_f = st(4)
shot('fried6', 1.0, t_d, t_e, zoom=(1.0, 1.12)); CUTS.append(t_d)
hl('लोग कहते हैं', 'खाना बदल गया', t_d, t_e, tp=at(3, 'खाना') - 0.05)
shot('glassro16', 0.3, t_e, t_f, 'mystery', zoom=(1.0, 1.22))
hl('पर एक चीज़', 'और बदली है…', t_e, at(3, 'जो') - 0.1, tp=at(3, 'बदली') - 0.1, color='r')
hl('जो', 'हर घर में है!', at(3, 'जो') - 0.1, t_f, tp=at(3, 'हर') - 0.05, color='r')
sfx(t_e, 'sfx498', -10)
# ============================ 4. reveal: drinking water ============================
t_g = st(5)
shot('matka28', 2.0, t_f, t_g + 0.45, 'bright', zoom=(1.18, 1.0))
hl('वो है…', 'आपका पीने का पानी', t_f, t_g, tp=at(4, 'पीने') - 0.1, color='c')
sfx(at(4, 'पानी') - 0.05, 'sfx1143', -10)
# ============================ 5. then: well/matka vs now: RO ============================
t_h = st(6)
split(t_g, t_h, ('well4', 0.3, None, None, 'mem'), ('rokitchen17', 0.0, (0, 0, 1, 0.6), 0.6, ''),
      'तब<small>कुआँ • मटका</small>', 'अब<small>RO</small>', ta=at(5, 'कुएँ') - 0.05, tb=at(5, 'हम') - 0.05, colb='var(--c)')
# ============================ 6-7. the glass: RO sieve takes dirt AND minerals -> clean but empty ============================
t_i = st(8)
GX0, GX1 = 285, 775            # inside of the glass (px) at zoom 1
MY0, MY1, MT0, MT1 = 705, 1350, 20.15, 23.55   # mesh travel
v = (MY1 - MY0) / (MT1 - MT0)
parts = [('d', '', 330, 760), ('d', '', 480, 745), ('d', '', 620, 790), ('d', '', 400, 805), ('d', '', 690, 755),
         ('m', 'Ca', 330, 915), ('m', 'Ca', 500, 950), ('m', 'Ca', 640, 900),
         ('m', 'Mg', 360, 1050), ('m', 'Mg', 560, 1075), ('m', 'Mg', 660, 1030)]
inner = ''; pids = []
for k, (c, lab, x, y) in enumerate(parts):
    i = f'pp{k}'; pids.append((i, y)); inner += f'<div class="pp {c}" id="{i}" style="left:{x}px;top:{y}px">{lab}</div>'
inner += f'<div class="mesh2" id="mesh" style="left:{GX0 - 10}px;width:{GX1 - GX0 + 20}px;top:{MY0}px"></div>'
gs = shot('demo25', 0.5, t_h, t_i, crop=(0.0, 0.08, 1.0, 0.84), zoom=(1.0, 1.06), inner=inner); CUTS.append(t_h)
for k, (i, y) in enumerate(pids):
    T(f'tl.fromTo("#{i}",{{x:-7}},{{x:7,duration:{0.9 + 0.13 * k:.2f},ease:"sine.inOut",yoyo:true,repeat:5}},{t_h:.3f});')
    tc = MT0 + (y - MY0) / v
    T(f'tl.fromTo("#{i}",{{y:0}},{{y:{MY1 - y},duration:{MT1 - tc:.3f},ease:"none",immediateRender:false}},{tc:.3f});')
    T(f'tl.fromTo("#{i}",{{y:{MY1 - y},autoAlpha:1}},{{y:{MY1 - y + 140},autoAlpha:0,duration:.45,ease:"power2.in",immediateRender:false}},{MT1:.3f});')
T(f'tl.set("#mesh",{{visibility:"visible"}},{at(6, "छलनी") - 0.15:.3f});tl.fromTo("#mesh",{{autoAlpha:0,scaleX:0}},{{autoAlpha:1,scaleX:1,duration:.4,ease:"power3.out"}},{at(6, "छलनी") - 0.15:.3f});')
T(f'tl.fromTo("#mesh",{{y:0}},{{y:{MY1 - MY0},duration:{MT1 - MT0:.3f},ease:"none",immediateRender:false}},{MT0:.3f});')
T(f'tl.fromTo("#mesh",{{y:{MY1 - MY0},autoAlpha:1}},{{y:{MY1 - MY0 + 140},autoAlpha:0,duration:.45,ease:"power2.in",immediateRender:false}},{MT1:.3f});')
sfx(at(6, 'छलनी') - 0.15, 'sfx166', -17)
hl('देखो,', 'RO = बारीक छलनी', t_h, at(6, 'गंदगी') - 0.12, tp=at(6, 'बारीक') - 0.1, color='c')
hl('गंदगी के साथ…', 'मिनरल्स भी बाहर!', at(6, 'गंदगी') - 0.12, st(7), tp=at(6, 'मिनरल्स') - 0.1, color='r')
el('<div class="chip g" id="ID" style="left:0;right:0;margin:0 auto;width:fit-content;top:1420px">✓ गंदगी बाहर</div>', at(6, 'गंदगी') + 0.15, st(7), 'autoAlpha:0,y:40', s='sfx3005', g=-17)
el('<div class="chip r" id="ID" style="left:0;right:0;margin:0 auto;width:fit-content;top:1535px">✗ कैल्शियम बाहर</div>', at(6, 'कैल्शियम') + 0.1, st(7), 'autoAlpha:0,y:40', s='sfx3005', g=-17)
el('<div class="chip r" id="ID" style="left:0;right:0;margin:0 auto;width:fit-content;top:1650px">✗ मैग्नीशियम बाहर</div>', at(6, 'मैग्नीशियम') + 0.15, st(7), 'autoAlpha:0,y:40', s='sfx3005', g=-17)
hl('यानी पानी', 'साफ़ तो हुआ…', st(7), t_i, tp=at(7, 'साफ़') - 0.1, color='c')
stamp('पर खाली!', at(7, 'खाली') - 0.2, t_i, top=1380)
# ============================ 8. WHO: more magnesium, fewer heart deaths ============================
t_j = st(9)
shot('heart3d14', 0.5, t_i, t_j, crop=(0, 0, 1, 0.92), zoom=(1.0, 1.1)); CUTS.append(t_i)
hl('और सबसे बड़ी बात:', 'WHO की रिपोर्ट', t_i, at(8, 'जहाँ') - 0.12, tp=at(8, 'WHO') - 0.1, color='y')
hl('जहाँ पानी में मैग्नीशियम ज़्यादा', 'दिल की बीमारी से मौतें कम', at(8, 'जहाँ') - 0.12, t_j, tp=at(8, 'मौतें') - 0.1, color='g')
el('''<div class="doc sm" id="ID" style="top:1240px"><div class="pin"></div><div class="t">WHO</div><div class="s">Calcium and magnesium in drinking-water • 2009</div><div class="l h">पानी में मैग्नीशियम ↑ → दिल की बीमारी से मौतें ↓</div><div class="l" style="width:70%"></div></div>''',
   at(8, 'रिपोर्ट') - 0.1, t_j, 'autoAlpha:0,y:300,rotation:-8', 'back.out(1.4)', d=.45, s='sfx1490', g=-15, to='rotation:-2,')
# ============================ 9. that magnesium goes down the drain ============================
t_k = st(10)
DX, DY = 610, 900
dps = ''.join(f'<div class="dp" id="dp{k}" style="left:{int(330 * __import__("math").cos(k * 0.785))}px;top:{int(330 * __import__("math").sin(k * 0.785))}px">Mg</div>' for k in range(8))
shot('rowaste15', 0.3, t_j, t_k, 'dim', zoom=(1.0, 1.15), inner=f'<div class="spin" id="spin" style="left:{DX}px;top:{DY}px">{dps}</div>'); CUTS.append(t_j)
T(f'tl.set("#spin",{{visibility:"visible"}},{at(9, "मैग्नीशियम") - 0.1:.3f});tl.fromTo("#spin",{{rotation:0}},{{rotation:540,duration:{t_k - at(9, "मैग्नीशियम"):.3f},ease:"power1.in"}},{at(9, "मैग्नीशियम") - 0.1:.3f});')
T(f'tl.fromTo("#spin .dp",{{autoAlpha:0,scale:.4}},{{autoAlpha:1,scale:1,duration:.3,stagger:.05}},{at(9, "मैग्नीशियम") - 0.1:.3f});')
import math
for k in range(8):
    ox, oy = int(330 * math.cos(k * 0.785)), int(330 * math.sin(k * 0.785))
    T(f'tl.fromTo("#dp{k}",{{x:0,y:0,scale:1}},{{x:{-ox},y:{-oy},scale:.15,autoAlpha:0,duration:1.5,ease:"power2.in",immediateRender:false}},{at(9, "नाली") - 0.4 + k * 0.07:.3f});')
hl('और वही मैग्नीशियम', 'रोज़ नाली में!', t_j, t_k, tp=at(9, 'नाली') - 0.1, color='r')
sfx(at(9, 'मैग्नीशियम'), 'sfx1311', -15)
# ============================ 10. the man at the shop falls ill -> the whole house stops ============================
t_l = at(10, 'पूरा') - 0.15; t_m = st(11)
shot('shutlock43', 0.3, t_k, t_l, 'dim', zoom=(1.0, 1.1))
hl('सोचिए, दुकान पर बैठा आदमी', 'बीमार पड़े…', t_k, t_l, tp=at(10, 'बीमार') - 0.1, color='r')
sfx(t_k + 0.02, 'sfx498', -6); sfx(at(10, 'पड़े') - 0.05, 'sfx1143', -12)
ph, pid = printv('familyin21', 3.0, t_l, t_m, 110, 560, 860, 760, rot=-3)
paper(t_l, t_m, ph, zoom=(1.06, 1.0))
vis(pid, t_l, t_m)
T(f'tl.fromTo("#{pid}",{{y:-60,autoAlpha:0}},{{y:0,autoAlpha:1,duration:.4,ease:"power3.out"}},{t_l:.3f});')
T(f'tl.fromTo("#{pid}v",{{filter:"grayscale(0) brightness(1)"}},{{filter:"grayscale(1) brightness(.72)",duration:.9,ease:"power1.inOut",immediateRender:false}},{at(10, "रुक") - 0.25:.3f});')
hl('तो सिर्फ़ वो नहीं…', 'पूरा घर रुक जाता है', t_l, t_m, tp=at(10, 'पूरा') - 0.05, color='r')
sfx(t_l, 'sfx1490', -15)
# ============================ 11. the old well won't come back... but Japan: Enagic Kangen ============================
t_n = at(11, 'पर') - 0.15; t_o = st(12)
ph, pid = printv('well4', 2.0, t_m, t_n, 120, 600, 840, 820, rot=2)
paper(t_m, t_n, ph, zoom=(1.0, 1.05))
vis(pid, t_m, t_n)
T(f'tl.fromTo("#{pid}v",{{filter:"sepia(.8) brightness(.95) contrast(1.05)"}},{{filter:"sepia(1) brightness(1.35) contrast(.55)",duration:{t_n - t_m:.3f},ease:"none"}},{t_m:.3f});')
T(f'tl.fromTo("#{pid}",{{autoAlpha:1,y:0}},{{autoAlpha:.55,y:40,duration:{t_n - t_m:.3f},ease:"power1.in"}},{t_m:.3f});')
hl('पुराना कुआँ तो', 'वापस नहीं आएगा', t_m, t_n, tp=at(11, 'वापस') - 0.1, color='wh')
flash(t_n)
shot('kangenk83', 0.3, t_n, t_o, 'bright', crop=(0, 0.16, 1, 0.84), zoom=(1.14, 1.0), ease='power2.out')
hl('पर जापान में • 50 साल से', 'Enagic Kangen', t_n, t_o, tp=at(11, 'Enagic') - 0.15, color='g', big=True)
sfx(t_n, 'sfx166', -14); sfx(at(11, 'Enagic') - 0.15, 'sfx1143', -10)
BADGE_T = t_n
# ============================ 12. cleans, keeps minerals, adds hydrogen ============================
t_p = at(12, 'और') - 0.15; t_q = st(13)
shot('kangenk85', 3.0, t_o, t_p, zoom=(1.0, 1.1)); CUTS.append(t_o)
hl('ये पानी साफ़ करती है', 'मिनरल्स नहीं निकालती', t_o, t_p, tp=at(12, 'मिनरल्स') - 0.1, color='g')
el('<div class="chip g" id="ID" style="left:90px;top:1150px">✓ साफ़</div>', at(12, 'साफ़') - 0.05, t_p, 'autoAlpha:0,x:-150', s='sfx3005', g=-16)
el('<div class="chip g" id="ID" style="right:90px;top:1280px">✓ मिनरल्स अंदर</div>', at(12, 'मिनरल्स') - 0.05, t_p, 'autoAlpha:0,x:150', s='sfx3005', g=-14)
shot('electro34', 47.0, t_p, t_q, zoom=(1.0, 1.12))
hl('और बिजली से', 'हाइड्रोजन', t_p, t_q, tp=at(12, 'हाइड्रोजन') - 0.1, color='c', big=True)
el('<div class="h2" id="ID">H<sub>2</sub></div>', at(12, 'हाइड्रोजन') - 0.05, t_q, 'autoAlpha:0,scale:0.3', 'back.out(2.5)', d=.5, s='sfx1317', g=-11)
sfx(at(12, 'बिजली') - 0.1, 'sfx1317', -15)
# ============================ 13. scientists: hydrogen picks off the most harmful particles ============================
t_r = st(14)
shot('cells28', 0.0, t_q, t_r, 'dim', zoom=(1.0, 1.12)); CUTS.append(t_q)
hl('वैज्ञानिकों ने पाया', 'हाइड्रोजन…', t_q, at(13, 'सबसे') - 0.12, tp=at(13, 'हाइड्रोजन') - 0.1, color='c')
hl('सबसे नुकसानदेह कण', 'चुन-चुनकर खत्म', at(13, 'सबसे') - 0.12, t_r, tp=at(13, 'चुन') - 0.1, color='r')
el('''<div class="doc sm" id="ID" style="top:1330px"><div class="pin"></div><div class="t" style="color:#b0172b">Nature Medicine</div><div class="s">2007 • Ohsawa et al. • Japan</div><div class="l h">हाइड्रोजन: सबसे नुकसानदेह कणों पर असर</div></div>''',
   at(13, 'वैज्ञानिकों') + 0.1, t_r, 'autoAlpha:0,y:300,rotation:-8', 'back.out(1.4)', d=.45, s='sfx1490', g=-15, to='rotation:-2,')
pts = [(200, 640, 1), (430, 760, 0), (690, 620, 1), (820, 880, 1), (300, 980, 0), (600, 1040, 1), (760, 1180, 0)]
for k, (x, y, bad) in enumerate(pts):
    i = nid('pt'); c = 'background:#e8452f' if bad else 'background:#3ddc84'
    els.append(f'<div class="pt" id="{i}" style="left:{x}px;top:{y}px;{c};width:84px;height:84px;font-size:40px">{"✗" if bad else "✓"}</div>')
    t0 = at(13, 'कणों') - 0.35 + k * 0.07
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});tl.fromTo("#{i}",{{autoAlpha:0,scale:0}},{{autoAlpha:1,scale:1,duration:.25,ease:"back.out(2)"}},{t0:.3f});')
    if bad:
        tb = at(13, 'चुन') + 0.05 + sum(1 for q in pts[:k] if q[2]) * 0.16
        T(f'tl.to("#{i}",{{scale:2,autoAlpha:0,duration:.25,ease:"power2.out"}},{tb:.3f});'); sfx(tb, 'sfx3005', -15)
    T(f'tl.set("#{i}",{{visibility:"hidden"}},{t_r:.3f});')
# ============================ 14. Japan's health ministry: household medical device ============================
t_s = st(15)
shot('kangenk87', 15.0, t_r, t_s, zoom=(1.0, 1.1)); CUTS.append(t_r)
hl('जापान का स्वास्थ्य मंत्रालय भी', 'घरेलू मेडिकल डिवाइस', t_r, t_s, tp=at(14, 'मेडिकल') - 0.1, color='g')
stamp('✓ मान्यता', at(14, 'मानता') - 0.15, t_s, top=1150, cls='g')
# ============================ 15. dream outcome: grandfather's well water, today's cleanliness, whole family ============================
t_t = at(15, 'आज') - 0.12; t_u = st(16)
wv = shot('well4', 0.4, t_s, t_t, 'mem', zoom=(1.0, 1.1))
T(f'tl.fromTo("#{wv}v",{{filter:"sepia(.78) saturate(.75) contrast(1.06) brightness(.92)"}},{{filter:"sepia(0) saturate(1.15) contrast(1.05) brightness(1.02)",duration:.9,ease:"power1.inOut",immediateRender:false}},{at(15, "भरा") - 0.3:.3f});')
hl('दादाजी के कुएँ जैसा', 'भरा पानी', t_s, t_t, tp=at(15, 'भरा') - 0.1, color='y')
shot('familyin4', 2.0, t_t, t_u, 'bright', zoom=(1.0, 1.08)); CUTS.append(t_t)
hl('आज की सफ़ाई के साथ', 'पूरे परिवार के लिए', t_t, t_u, tp=at(15, 'पूरे') - 0.1, color='g')
# ============================ 16. callback: the shopkeeper; RO vs Kangen ============================
t_v = at(16, 'याद') - 0.12; t_w = st(17)
shot('shopk31', 20.0, t_u, t_v + 0.45, zoom=(1.0, 1.1)); CUTS.append(t_u)
hl('तो अगली बार कोई कहे', 'RO है तो सब ठीक!', t_u, t_v, tp=at(16, 'RO') - 0.1, color='c')
split(t_v, t_w, ('rokitchen17', 0.0, (0, 0, 1, 0.6), 0.6, ''), ('kangenk85', 8.0, None, None, ''),
      'RO<small>सिर्फ़ साफ़</small>', 'Kangen ✓<small>साफ़ भी, भरा भी</small>', ta=at(16, 'साफ़') - 0.1, tb=at(16, 'भरा') - 0.1, colb='var(--g)')
# ============================ 17. which water comes to your home? ============================
t_x = st(18)
p1, i1 = printv('rokitchen17', 0.2, t_w, t_x, 50, 520, 380, 400, rot=-6, cap='RO', crop=(0, 0, 1, 0.6), slow=0.45)
p2, i2 = printv('well26', 1.0, t_w, t_x, 590, 560, 380, 400, rot=5, cap='बोरिंग')
p3, i3 = printv('well5', 1.0, t_w, t_x, 330, 1085, 380, 400, rot=-2, cap='नगरपालिका')
paper(t_w, t_x, '<div class="qm" id="qm">?</div>' + p1 + p2 + p3)
T(f'tl.set("#qm",{{visibility:"visible"}},{at(17, "कौन") - 0.1:.3f});tl.fromTo("#qm",{{autoAlpha:0,scale:.4,rotation:-20}},{{autoAlpha:1,scale:1,rotation:0,duration:.35,ease:"back.out(2.2)"}},{at(17, "कौन") - 0.1:.3f});tl.to("#qm",{{autoAlpha:0,scale:1.6,duration:.3}},{at(17, "RO") - 0.25:.3f});')
for pid, w in ((i1, 'RO'), (i2, 'बोरिंग'), (i3, 'नगरपालिका')):
    t = at(17, w) - 0.08; vis(pid, t, t_x)
    T(f'tl.fromTo("#{pid}",{{autoAlpha:0,y:-120,scale:1.25}},{{autoAlpha:1,y:0,scale:1,duration:.3,ease:"power3.out"}},{t:.3f});'); sfx(t, 'sfx1490', -16)
hl('आपके घर में', 'कौन सा पानी आता है?', t_w, t_x, tp=at(17, 'कौन') - 0.1, color='y')
# ============================ 18. we come to your home, test your own water, free ============================
t_y = at(18, 'फ़र्क') - 0.15; t_z = st(19)
shot('demo1', 8.0, t_x, t_z, zoom=(1.0, 1.1), crop=(0, 0.05, 1, 0.95)); CUTS.append(t_x)
hl('हम आपके घर आकर', 'आपके ही पानी से', t_x, t_y, tp=at(18, 'आपके', 1) - 0.1, color='y')
hl('ये फ़र्क दिखाएंगे', 'बिल्कुल मुफ़्त', t_y, t_z, tp=at(18, 'बिल्कुल') - 0.1, color='g')
stamp('मुफ़्त', at(18, 'मुफ़्त') - 0.1, t_z, top=1150, cls='g')
# ============================ 19. CTA ============================
shot('kangenk83', 2.0, t_z, DUR, 'dim', crop=(0, 0.16, 1, 0.84), zoom=(1.0, 1.06)); CUTS.append(t_z)
el('<div class="cta" id="ID"><div class="a">फ़र्क अपनी आँखों से देखिए</div><div class="b">आज ही फ्री डेमो बुक कराएं</div><div class="c">Enagic Kangen • चोटिला</div></div>', t_z, DUR, 'autoAlpha:0,y:120', 'back.out(1.6)', d=.5, s='sfx1143', g=-11)
# brand badge from the Kangen reveal to the CTA
els.append('<div class="badge" id="bdg">Enagic Kangen • चोटिला</div>')
T(f'tl.set("#bdg",{{visibility:"visible"}},{BADGE_T:.3f});tl.fromTo("#bdg",{{autoAlpha:0}},{{autoAlpha:.9,duration:.4}},{BADGE_T:.3f});tl.set("#bdg",{{visibility:"hidden"}},{t_z:.3f});')
for t in CUTS: sfx(t, 'sfx166', -21)

overlays = '<div class="topfade"></div><div class="botfade"></div><div class="vign"></div><svg class="grain" width="1080" height="1920"><filter id="nz"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="3"/></filter><rect width="1080" height="1920" filter="url(#nz)"/></svg>'
css = open('style.css').read()
html = f'''<!doctype html>
<html lang="hi"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>Kangen reel 5</title><script src="gsap.min.js"></script><style>{css}</style></head>
<body><div id="root" data-composition-id="main" data-start="0" data-width="{W}" data-height="{H}" data-duration="{DUR}">
{chr(10).join(els)}
{overlays}
<audio id="mix" src="assets/mix.wav" data-start="0" data-duration="{DUR}"></audio>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tw)}
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl;
</script></body></html>'''
open('index.html', 'w').write(html)
json.dump(dict(sfx=SFX, music=[['m188', 14.0, 0.0, 37.75, -20], ['m543', 22.0, t_n, DUR, -21]], dur=DUR), open('sfx.json', 'w'))
print('ok', len(els), 'elements', len(tw), 'tweens', len(SFX), 'sfx', 'DUR', DUR)
