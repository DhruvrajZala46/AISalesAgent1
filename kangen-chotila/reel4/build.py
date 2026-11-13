# build.py - Kangen reel 4 (Hindi, Mayank-style): "आपकी रसोई में एक मशीन..." RO vs Enagic Kangen
import json, os, subprocess
P = os.path.dirname(os.path.abspath(__file__)); os.chdir(P)
B = json.load(open('beats.json')); DUR = round(B[-1]['end'] + 2.0, 2)
W, H = 1080, 1920
def sh(c): subprocess.run(c, shell=True, check=True)
def at(i, word, k=0, end=False):
    hits = [w for w in B[i - 1]['words'] if word in w[0]]
    assert hits, (i, word)
    return hits[k][2] if end else hits[k][1]
st = lambda i: B[i - 1]['start']; en = lambda i: B[i - 1]['end']
def dur(src): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'raw/{src}.mp4'], capture_output=True, text=True).stdout)
def cut(name, src, a, need, w=W, h=H, top=1.0, bot=1.0):
    out = f'assets/{name}.mp4'
    if not os.path.exists(out):
        avail = max(0.5, dur(src) - a); speed = 1.0
        if avail < need + 0.2: speed = max(0.45, avail / (need + 0.2))
        take = min(avail, (need + 0.2) * speed)
        pre = f"crop=iw:ih*{top}:0:0," if top < 1 else (f"crop=iw:ih*{bot}:0:ih*{1 - bot:.3f}," if bot < 1 else "")
        vf = f"{pre}setpts=PTS/{speed},scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},fps=30"
        sh(f'ffmpeg -y -v error -ss {a} -t {take:.3f} -i raw/{src}.mp4 -an -vf "{vf}" -c:v libx264 -crf 19 -preset veryfast -g 30 -keyint_min 30 -pix_fmt yuv420p -movflags +faststart {out}')
    return out

els, tw, SFX = [], [], []
def T(s): tw.append(s)
n = [0]
def nid(p='e'): n[0] += 1; return f'{p}{n[0]}'
def sfx(t, f, g=-14): SFX.append((round(t, 3), f, g))

def shot(src, a, t0, t1, cls='', top=1.0, zoom=(1.0, 1.09), inner='', bot=1.0):
    i = nid('sh'); name = f'{src}_{a}_{int(t0 * 10)}_t{top}_b{bot}'.replace('.', 'p')
    f = cut(name, src, a, t1 - t0, top=top, bot=bot)
    els.append(f'<div class="shot {cls}" id="{i}"><video id="{i}v" src="{f}" muted playsinline data-start="{t0:.3f}" data-duration="{t1 - t0 + 0.05:.3f}"></video>{inner}</div>')
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});')
    if t1 < DUR: T(f'tl.set("#{i}",{{visibility:"hidden"}},{t1:.3f});')
    T(f'tl.fromTo("#{i}v",{{scale:{zoom[0]}}},{{scale:{zoom[1]},duration:{t1 - t0:.3f},ease:"none"}},{t0:.3f});')
    return i

def hl(kick, punch, t0, t1, tp=None, color='', big=False):
    i = nid('hl')
    kw = ''.join(f'<span class="w">{w}</span> ' for w in kick.split())
    pw = ''.join(f'<span class="w">{w}</span> ' for w in punch.split())
    els.append(f'<div class="hl" id="{i}"><span class="k">{kw}</span><span class="p {color}"{" style=font-size:150px" if big else ""}>{pw}</span></div>')
    tp = tp if tp is not None else t0 + 0.35
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});')
    T(f'tl.fromTo("#{i} .k .w",{{autoAlpha:0,y:26}},{{autoAlpha:1,y:0,duration:.22,stagger:.07,ease:"power3.out"}},{t0:.3f});')
    T(f'tl.fromTo("#{i} .p .w",{{autoAlpha:0,y:40,scale:1.25}},{{autoAlpha:1,y:0,scale:1,duration:.28,stagger:.09,ease:"back.out(2)"}},{tp:.3f});')
    T(f'tl.set("#{i}",{{visibility:"hidden"}},{t1:.3f});')
    sfx(tp, 'sfx3005', -20)
    return i

def el(html, t0, t1, frm='autoAlpha:0,scale:0.6', ease='back.out(2)', d=0.35, s=None, g=-16):
    i = nid('x'); els.append(html.replace('ID', i))
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});tl.fromTo("#{i}",{{{frm}}},{{autoAlpha:1,scale:1,x:0,y:0,duration:{d},ease:"{ease}"}},{t0:.3f});')
    if t1 < DUR: T(f'tl.set("#{i}",{{visibility:"hidden"}},{t1:.3f});')
    if s: sfx(t0, s, g)
    return i

def stamp(text, t0, t1, top=820, cls=''):
    i = nid('st'); els.append(f'<div class="stamp {cls}" id="{i}" style="top:{top}px">{text}</div>')
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});tl.fromTo("#{i}",{{autoAlpha:0,scale:2.8,rotation:-24}},{{autoAlpha:1,scale:1,rotation:-8,duration:.25,ease:"power4.in"}},{t0:.3f});')
    if t1 < DUR: T(f'tl.set("#{i}",{{visibility:"hidden"}},{t1:.3f});')
    sfx(t0 + 0.2, 'sfx2364', -11)

# ===================== SHOTS + HEADLINES =====================
# L1 - the mystery machine in your kitchen
shot('rokitchen17', 0.5, 0.0, at(1, 'दिन') - 0.1, 'mystery', zoom=(1.18, 1.0), top=0.6)
hl('आपकी रसोई में', 'एक मशीन…', 0.0, at(1, 'दिन') - 0.1, tp=at(1, 'मशीन'))
sfx(0.0, 'sfx498', -8); sfx(at(1, 'मशीन'), 'sfx1143', -16)
shot('glassro16', 0.3, at(1, 'दिन') - 0.1, st(2) - 0.05, 'mystery')
hl('हर दिन चुपचाप', 'कुछ निकाल रही है', at(1, 'दिन') - 0.1, at(1, 'पता') - 0.1, tp=at(1, 'चीज़ें'))
hl('और आपको', 'पता भी नहीं!', at(1, 'पता') - 0.1, st(2) - 0.05, tp=at(1, 'पता'), color='r')
# L2
shot('glassro40', 0.3, st(2) - 0.05, at(2, 'इसके') - 0.1)
hl('ना स्वाद बदले', 'ना रंग', st(2) - 0.05, at(2, 'इसके') - 0.1, tp=at(2, 'ना', 1))
shot('rupee6', 0.5, at(2, 'इसके') - 0.1, st(3) - 0.05)
hl('और इसके पैसे भी', 'आपने ही दिए!', at(2, 'इसके') - 0.1, st(3) - 0.05, tp=at(2, 'आपने'), color='r')
# L3 - reveal
shot('ro27', 104.0, st(3) - 0.05, st(4) - 0.05, zoom=(1.25, 1.05))
hl('वो मशीन है…', 'आपका RO', st(3) - 0.05, st(4) - 0.05, tp=at(3, 'RO') - 0.1, color='r', big=True)
sfx(at(3, 'RO') - 0.1, 'sfx1143', -10)
# L4
shot('glassro3', 0.5, st(4) - 0.05, at(4, 'असली') - 0.15, top=0.8)
hl('पानी तो', 'एकदम साफ़', st(4) - 0.05, at(4, 'तो') - 0.1, tp=at(4, 'एकदम'), color='c')
hl('पर क्या ये', 'सबसे अच्छा भी?', at(4, 'तो') - 0.1, at(4, 'असली') - 0.15, tp=at(4, 'अच्छा') - 0.1)
shot('glassro16', 2.5, at(4, 'असली') - 0.15, st(5) - 0.05, 'mystery', zoom=(1.0, 1.2))
hl('या असली बात', 'कुछ और है?', at(4, 'असली') - 0.15, st(5) - 0.05, tp=at(4, 'कुछ'), color='r')
sfx(at(4, 'असली') - 0.15, 'sfx498', -10)
# L5 - waste (kept short)
shot('rowaste9', 0.4, st(5) - 0.05, at(5, 'तीन-चार') - 0.2, 'dim', top=0.68)
hl('देखिए, सबसे पहले', '1 लीटर पानी के लिए…', st(5) - 0.05, at(5, 'तीन-चार') - 0.2, tp=at(5, 'एक'))
shot('rowaste15', 0.3, at(5, 'तीन-चार') - 0.2, st(6) - 0.05, 'dim')
hl('', '3-4 लीटर नाली में!', at(5, 'तीन-चार') - 0.2, st(6) - 0.05, tp=at(5, 'तीन-चार') - 0.15, color='r')
el('<div class="bott" id="ID"><div class="b1"><i></i></div><div class="eq">=</div><div class="b1 w"><i></i></div><div class="b1 w"><i></i></div><div class="b1 w"><i></i></div><div class="b1 w"><i></i></div></div>', at(5, 'तीन-चार') - 0.1, st(6) - 0.05, 'autoAlpha:0,y:80', 'power3.out', s='sfx1311')
T(f'tl.fromTo(".b1.w i",{{height:"100%"}},{{height:"0%",duration:1.4,stagger:.12,ease:"power1.in"}},{at(5, "नाली") - 0.2:.3f});')
# L6 - RO = very fine sieve
shot('sieve19', 0.3, st(6) - 0.05, st(7) - 0.05, zoom=(1.0, 1.12))
hl('जो पानी बचता है', 'उसमें भी कमी!', st(6) - 0.05, at(6, 'RO') - 0.1, tp=at(6, 'कमी') - 0.15, color='r')
hl('RO मतलब', 'बहुत बारीक छलनी', at(6, 'RO') - 0.1, st(7) - 0.05, tp=at(6, 'बहुत') - 0.1, color='c')
# L7 - stops dirt AND minerals (particle graphic)
shot('sieve2', 0.4, st(7) - 0.05, st(8) - 0.05, 'dim')
hl('गंदगी भी रुकी…', 'मिनरल्स भी रुक गए!', st(7) - 0.05, st(8) - 0.05, tp=at(7, 'कैल्शियम') - 0.1, color='r')
el('<div class="mesh" id="ID"></div>', st(7) + 0.05, st(8) - 0.05, 'autoAlpha:0,scaleX:0', 'power3.out', d=0.4)
parts = [('d', '', 160, st(7) + 0.4), ('d', '', 300, st(7) + 0.7), ('m', 'Ca', 470, at(7, 'कैल्शियम')), ('m', 'Mg', 640, at(7, 'मैग्नीशियम')),
         ('d', '', 800, st(7) + 1.0), ('m', 'Ca', 880, at(7, 'मिनरल्स') - 0.1)]
for k, (c, lab, x, t) in enumerate(parts):
    i = nid('pt'); els.append(f'<div class="pt {c}" id="{i}" style="left:{x}px;top:640px">{lab}</div>')
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t:.3f});tl.fromTo("#{i}",{{autoAlpha:0,y:-200}},{{autoAlpha:1,y:360,duration:.7,ease:"bounce.out"}},{t:.3f});tl.set("#{i}",{{visibility:"hidden"}},{st(8) - 0.05:.3f});')
    sfx(t + 0.45, 'sfx2364', -22)
for k, x in enumerate([230, 420, 560, 760]):
    i = nid('pt'); els.append(f'<div class="pt w" id="{i}" style="left:{x}px;top:700px"></div>')
    t = st(7) + 0.3 + k * 0.5
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t:.3f});tl.fromTo("#{i}",{{autoAlpha:0,y:-160}},{{autoAlpha:1,y:820,duration:1.0,ease:"power1.in"}},{t:.3f});tl.set("#{i}",{{visibility:"hidden"}},{t + 1.0:.3f});')
# L8 - clean but empty
shot('glassro27', 0.4, st(8) - 0.05, st(9) - 0.05, zoom=(1.0, 1.1))
hl('मतलब पानी', 'साफ़ तो हुआ…', st(8) - 0.05, st(9) - 0.05, tp=at(8, 'साफ़'), color='c')
stamp('पर खाली!', at(8, 'पर') - 0.05, st(9) - 0.05, top=900)
# L9 - age & bones need these minerals
shot('oldman0', 0.3, st(9) - 0.05, at(9, 'मिनरल्स') - 0.2, zoom=(1.0, 1.08))
hl('उम्र के साथ', 'हड्डियों को…', st(9) - 0.05, at(9, 'मिनरल्स') - 0.2, tp=at(9, 'उम्र'))
shot('bones38', 0.3, at(9, 'मिनरल्स') - 0.2, at(9, 'हम') - 0.1, zoom=(1.0, 1.1))
hl('इन्हीं', 'मिनरल्स की ज़रूरत', at(9, 'मिनरल्स') - 0.2, at(9, 'हम') - 0.1, tp=at(9, 'मिनरल्स'), color='g')
el('<div class="chip g" id="ID" style="left:90px;top:1180px">कैल्शियम</div>', at(9, 'ज़रूरत') - 0.1, at(9, 'हम') - 0.1, 'autoAlpha:0,x:-120')
el('<div class="chip g" id="ID" style="right:90px;top:1300px">मैग्नीशियम</div>', at(9, 'ज़रूरत') + 0.1, at(9, 'हम') - 0.1, 'autoAlpha:0,x:120')
shot('rowaste15', 4.0, at(9, 'हम') - 0.1, st(10) - 0.05, 'dim', zoom=(1.2, 1.0))
hl('और हम खुद', 'फेंक रहे हैं!', at(9, 'हम') - 0.1, st(10) - 0.05, tp=at(9, 'रहे') - 0.3, color='r')
# L10 - credit twist: looks clean != good for body
shot('ro27', 60.0, st(10) - 0.05, at(10, 'पर') - 0.1, 'dim')
hl('तो क्रेडिट', 'किसे मिलता है?', st(10) - 0.05, at(10, 'को,') - 0.2, tp=at(10, 'किसे'))
hl('RO को…', 'क्योंकि साफ़ दिखता है', at(10, 'को,') - 0.2, at(10, 'पर') - 0.1, tp=at(10, 'दिखता') - 0.3, color='c')
i = nid('sp'); els.append(f'''<div class="split" id="{i}"><div class="half a"><video id="{i}a" src="{cut('glassro16_s', 'glassro16', 1.0, en(10) - at(10, 'पर') + 0.3, 1080, 960)}" muted playsinline data-start="{at(10, 'पर') - 0.1:.3f}" data-duration="{st(11) - at(10, 'पर') + 0.1:.3f}"></video><div class="lab">साफ़ दिखना</div></div>
<div class="half b"><video id="{i}b" src="{cut('bones22_s', 'bones22', 0.5, en(10) - at(10, 'पर') + 0.3, 1080, 960)}" muted playsinline data-start="{at(10, 'पर') - 0.1:.3f}" data-duration="{st(11) - at(10, 'पर') + 0.1:.3f}"></video><div class="lab" style="color:var(--g)">शरीर के लिए अच्छा</div></div><div class="line"></div></div>''')
T(f'tl.set("#{i}",{{visibility:"visible"}},{at(10, "पर") - 0.1:.3f});tl.set("#{i}",{{visibility:"hidden"}},{st(11) - 0.05:.3f});')
T(f'tl.fromTo("#{i} .half.a",{{x:-1080}},{{x:0,duration:.35,ease:"power3.out"}},{at(10, "पर") - 0.1:.3f});tl.fromTo("#{i} .half.b",{{x:1080}},{{x:0,duration:.35,ease:"power3.out"}},{at(10, "पर") - 0.1:.3f});')
el('<div class="stamp" id="ID" style="top:830px;font-size:200px;padding:0 40px 20px;transform:none">≠</div>', at(10, 'अलग') - 0.2, st(11) - 0.05, 'autoAlpha:0,scale:3', 'power4.in', d=.25, s='sfx2364', g=-11)
sfx(at(10, 'पर') - 0.1, 'sfx1490', -15)
# L11 - NGT
shot('oldman41', 0.5, st(11) - 0.05, st(12) - 0.05, 'dim')
hl('हैरानी की बात', 'सरकारी NGT ने कहा', st(11) - 0.05, st(12) - 0.05, tp=at(11, 'NGT') - 0.1, color='y')
el('''<div class="doc" id="ID"><div class="t">NGT</div><div class="s">नेशनल ग्रीन ट्रिब्यूनल • 2019</div><div class="l"></div><div class="l h">पानी ज़्यादा खारा नहीं → RO की ज़रूरत नहीं</div><div class="l"></div><div class="l" style="width:60%"></div></div>''', at(11, 'कहा') - 0.1, st(12) - 0.05, 'autoAlpha:0,y:300,rotation:-8', 'back.out(1.4)', d=.45, s='sfx1490', g=-15)
stamp('ज़रूरत नहीं', at(11, 'ज़रूरत') - 0.05, st(12) - 0.05, top=1230)
# L12 - Japan, 50 years, Enagic
shot('fuji15', 0.3, st(12) - 0.05, at(12, 'जापान') - 0.15, 'dim')
hl('तो फिर', 'सही रास्ता क्या है?', st(12) - 0.05, at(12, 'जापान') - 0.15, tp=at(12, 'सही'), color='y')
shot('fuji7', 0.3, at(12, 'जापान') - 0.15, st(13) - 0.05, zoom=(1.0, 1.12))
hl('जापान • 50 साल से', 'Enagic', at(12, 'जापान') - 0.15, st(13) - 0.05, tp=at(12, 'Enagic') - 0.2, color='y', big=True)
sfx(at(12, 'जापान') - 0.15, 'sfx1143', -12)
# L13 - Kangen machine: filter (dirt/chlorine out, minerals in), then electricity splits water
BADGE_T = st(13) - 0.05
shot('kangen2', 13.5, st(13) - 0.05, at(13, 'बिजली') - 0.15, zoom=(1.0, 1.15))
hl('Enagic की', 'Kangen मशीन', st(13) - 0.05, at(13, 'बिजली') - 0.15, tp=at(13, 'मशीन') - 0.3, color='g')
el('<div class="chip r" id="ID" style="left:80px;top:1120px">✗ गंदगी</div>', at(13, 'गंदगी') - 0.05, at(13, 'बिजली') - 0.15, 'autoAlpha:0,x:-150', s='sfx3005')
el('<div class="chip r" id="ID" style="left:80px;top:1250px">✗ क्लोरीन</div>', at(13, 'क्लोरीन') - 0.05, at(13, 'बिजली') - 0.15, 'autoAlpha:0,x:-150', s='sfx3005')
el('<div class="chip g" id="ID" style="right:80px;top:1185px">✓ मिनरल्स अंदर</div>', at(13, 'अंदर') - 0.3, at(13, 'बिजली') - 0.15, 'autoAlpha:0,x:150', s='sfx3005', g=-12)
shot('electro34', 47.0, at(13, 'बिजली') - 0.15, st(14) - 0.05, zoom=(1.0, 1.1))
hl('बिजली से पानी के', 'दो हिस्से', at(13, 'बिजली') - 0.15, st(14) - 0.05, tp=at(13, 'दो') - 0.1, color='y')
sfx(at(13, 'बिजली') - 0.15, 'sfx1317', -12)
# L14 - why are the Japanese crazy about it? hydrogen
shot('japan5', 0.3, st(14) - 0.05, at(14, 'दरअसल') - 0.15)
hl('जापान के लोग', 'इतने दीवाने क्यों?', st(14) - 0.05, at(14, 'दरअसल') - 0.15, tp=at(14, 'इतने'), color='y')
shot('bubbles35', 0.3, at(14, 'दरअसल') - 0.15, st(15) - 0.05, zoom=(1.0, 1.15))
hl('पीने वाले पानी में', 'हाइड्रोजन घुल जाता है', at(14, 'दरअसल') - 0.15, st(15) - 0.05, tp=at(14, 'हाइड्रो') - 0.2, color='c')
el('<div class="h2" id="ID">H<sub>2</sub></div>', at(14, 'हाइड्रो') - 0.1, st(15) - 0.05, 'autoAlpha:0,scale:0.3', 'back.out(2.5)', d=.5, s='sfx1317', g=-9)
# L15 - rust: iron rusts, the body rusts inside too
shot('rust21', 0.3, st(15) - 0.05, at(15, 'हमारे') - 0.2, zoom=(1.0, 1.12))
hl('जैसे लोहे को', 'जंग लगता है…', st(15) - 0.05, at(15, 'हमारे') - 0.2, tp=at(15, 'जंग') - 0.1, color='r')
shot('bones22', 3.0, at(15, 'हमारे') - 0.2, st(16) - 0.05, 'rust', zoom=(1.0, 1.15))
hl('वैसे ही शरीर के अंदर', 'भी जंग!', at(15, 'हमारे') - 0.2, st(16) - 0.05, tp=at(15, 'जंग', 1) - 0.1, color='r', big=True)
sfx(at(15, 'जंग', 1) - 0.1, 'sfx1143', -11)
# L16 - scientists: big cause of ageing & tiredness
shot('oldman5', 0.5, st(16) - 0.05, st(17) - 0.05, zoom=(1.0, 1.08))
hl('बुढ़ापे और थकान की', 'बड़ी वजह', st(16) - 0.05, st(17) - 0.05, tp=at(16, 'बुढ़ापे'), color='r')
# L17 - 2007: hydrogen removes the most dangerous particles, leaves the good ones
shot('bubbles35', 6.0, st(17) - 0.05, st(18) - 0.05, 'dim', zoom=(1.0, 1.12))
hl('2007 • जापान के वैज्ञानिक', 'सबसे खतरनाक कण खत्म', st(17) - 0.05, at(17, 'शरीर') - 0.2, tp=at(17, 'खतरनाक') - 0.15, color='r')
hl('और अच्छे कण', 'सुरक्षित', at(17, 'शरीर') - 0.2, st(18) - 0.05, tp=at(17, 'अच्छे'), color='g', big=True)
for k, (x, y) in enumerate([(200, 760), (420, 900), (650, 780), (820, 960), (300, 1100), (700, 1150)]):
    bad = k % 2 == 0; i = nid('pt'); c = 'background:#e8452f' if bad else 'background:#3ddc84'
    els.append(f'<div class="pt" id="{i}" style="left:{x}px;top:{y}px;{c}">{"✗" if bad else "✓"}</div>')
    T(f'tl.set("#{i}",{{visibility:"visible"}},{at(17, "कणों") - 0.3 + k * 0.08:.3f});tl.fromTo("#{i}",{{autoAlpha:0,scale:0}},{{autoAlpha:1,scale:1,duration:.25}},{at(17, "कणों") - 0.3 + k * 0.08:.3f});')
    if bad: T(f'tl.to("#{i}",{{scale:1.8,autoAlpha:0,duration:.3}},{at(17, "खत्म") + k * 0.1:.3f});')
    T(f'tl.set("#{i}",{{visibility:"hidden"}},{st(18) - 0.05:.3f});')
sfx(at(17, 'खत्म'), 'sfx1317', -12)
# L18 - Nature Medicine
shot('bubbles47', 0.5, st(18) - 0.05, st(19) - 0.05, 'dim')
el('''<div class="doc" id="ID" style="top:520px"><div class="t" style="color:#b0172b">Nature Medicine</div><div class="s">2007 • Ohsawa et al. • Japan</div><div class="l"></div><div class="l h">हाइड्रोजन: खतरनाक कणों पर असर</div><div class="l"></div><div class="l" style="width:55%"></div></div>''', st(18) - 0.05, st(19) - 0.05, 'autoAlpha:0,y:300,rotation:-8', 'back.out(1.4)', d=.45, s='sfx1490', g=-15)
hl('दुनिया की बड़ी', 'मेडिकल पत्रिका', st(18) - 0.05, st(19) - 0.05, tp=at(18, 'पत्रिका') - 0.2, color='y')
# L19 - athletes less tired
shot('athlete30', 1.0, st(19) - 0.05, st(20) - 0.05, zoom=(1.0, 1.1), top=0.8)
hl('हाइड्रोजन वाला पानी पीने वाले खिलाड़ी', 'थकान कम!', st(19) - 0.05, st(20) - 0.05, tp=at(19, 'उनकी') - 0.1, color='g', big=True)
# L20 - Kangen gives hydrogen; the whole world is watching
shot('phtest3', 0.6, st(20) - 0.05, at(20, 'पूरी') - 0.2, zoom=(1.0, 1.12))
hl('Kangen पानी', 'सिर्फ़ प्यास नहीं बुझाता', st(20) - 0.05, at(20, 'ये') - 0.1, tp=at(20, 'सिर्फ़'), color='y')
hl('ये देता है', 'हाइड्रोजन भी', at(20, 'ये') - 0.1, at(20, 'पूरी') - 0.2, tp=at(20, 'भी') - 0.2, color='c')
shot('bubbles47', 6.0, at(20, 'पूरी') - 0.2, st(21) - 0.05, zoom=(1.0, 1.15))
hl('जिस पर आज', 'पूरी दुनिया की नज़र', at(20, 'पूरी') - 0.2, st(21) - 0.05, tp=at(20, 'पूरी'), color='y')
# L21 - India vs Japan, longest-lived; Japan's health ministry recognition
i = nid('sp'); t_a, t_b = st(21) - 0.05, at(21, 'मंत्रालय') - 0.4
els.append(f'''<div class="split" id="{i}"><div class="half a"><video id="{i}a" src="{cut('india_eld15b', 'oldman15', 0.5, t_b - t_a + 0.3, 1080, 960, top=0.75)}" muted playsinline data-start="{t_a:.3f}" data-duration="{t_b - t_a + 0.1:.3f}"></video><div class="lab">भारत</div></div>
<div class="half b"><video id="{i}b" src="{cut('japan_eld_d', 'japan24', 5.0, t_b - t_a + 0.3, 1080, 960, top=0.66)}" muted playsinline data-start="{t_a:.3f}" data-duration="{t_b - t_a + 0.1:.3f}"></video><div class="lab" style="color:var(--y)">जापान: सबसे लंबी उम्र</div></div><div class="line"></div></div>''')
T(f'tl.set("#{i}",{{visibility:"visible"}},{t_a:.3f});tl.set("#{i}",{{visibility:"hidden"}},{t_b:.3f});')
T(f'tl.fromTo("#{i} .half.a",{{x:-1080}},{{x:0,duration:.35,ease:"power3.out"}},{t_a:.3f});tl.fromTo("#{i} .half.b",{{x:1080}},{{x:0,duration:.35,ease:"power3.out"}},{at(21, "जापान") - 0.1:.3f});')
sfx(t_a, 'sfx1143', -12)
shot('kangen2', 20.0, t_b, st(22) - 0.05, 'dim', zoom=(1.0, 1.1))
hl('जापान का स्वास्थ्य मंत्रालय', 'मेडिकल डिवाइस की मान्यता', t_b, st(22) - 0.05, tp=at(21, 'मंत्रालय') + 0.2, color='g')
stamp('✓ मान्यता', at(21, 'मंत्रालय') + 0.9, st(22) - 0.05, top=1050, cls='g')
# L22 - five kinds of water
shot('veg2', 0.3, st(22) - 0.05, st(23) - 0.05, 'dim', zoom=(1.0, 1.08))
hl('एक ही मशीन से', '5 तरह का पानी', st(22) - 0.05, st(23) - 0.05, tp=at(22, 'तरह') - 0.3, color='y')
ICON = {
 'पीने का': '<svg viewBox="0 0 100 100"><path d="M22 10h56l-8 82H30z" fill="none" stroke="#fff" stroke-width="7"/><path d="M30 46h40l-4 40H34z" fill="#6fd3ff"/></svg>',
 'खाना': '<svg viewBox="0 0 100 100"><path d="M14 44h72v18a26 26 0 0 1-26 26H40a26 26 0 0 1-26-26z" fill="#fff"/><path d="M6 44h88" stroke="#fff" stroke-width="7"/><path d="M36 30q4-10 0-18M52 30q4-10 0-18M68 30q4-10 0-18" stroke="#fff" stroke-width="5" fill="none"/></svg>',
 'दवाई': '<svg viewBox="0 0 100 100"><rect x="14" y="36" width="72" height="30" rx="15" fill="#fff" transform="rotate(-35 50 50)"/><path d="M50 22v56" stroke="#e8452f" stroke-width="8" transform="rotate(-35 50 50)"/></svg>',
 'सब्ज़ी-फल': '<svg viewBox="0 0 100 100"><circle cx="40" cy="58" r="26" fill="#ff5a4a"/><circle cx="66" cy="52" r="22" fill="#3ddc84"/><path d="M40 32q2-14 14-18" stroke="#3ddc84" stroke-width="6" fill="none"/></svg>',
 'सफ़ाई': '<svg viewBox="0 0 100 100"><path d="M36 30h28l6 62H30z" fill="#fff"/><rect x="40" y="10" width="20" height="20" fill="#ffd23f"/><path d="M60 16h22" stroke="#fff" stroke-width="7"/><circle cx="88" cy="30" r="4" fill="#6fd3ff"/><circle cx="92" cy="44" r="4" fill="#6fd3ff"/></svg>'}
icw = {'पीने का': 'पीने', 'खाना': 'बनाने', 'दवाई': 'दवाई', 'सब्ज़ी-फल': 'धोने', 'सफ़ाई': 'सफ़ाई'}
cells_html = ''.join(f'<div class="ic" id="ic{k}"><div class="o">{svg}</div><span>{name}</span></div>' for k, (name, svg) in enumerate(ICON.items()))
els.append(f'<div class="icons">{cells_html}</div>')
for k, name in enumerate(ICON):
    t = at(22, icw[name]) - 0.15
    T(f'tl.set("#ic{k}",{{visibility:"visible"}},{t:.3f});tl.fromTo("#ic{k}",{{autoAlpha:0,y:60,scale:.6}},{{autoAlpha:1,y:0,scale:1,duration:.3,ease:"back.out(2.5)"}},{t:.3f});tl.set("#ic{k}",{{visibility:"hidden"}},{st(23) - 0.05:.3f});')
    sfx(t, 'sfx3005', -14)
# L23 - whole family, one tap
shot('kangenk8_31', 0.3, st(23) - 0.05, st(24) - 0.05, zoom=(1.0, 1.1), bot=0.64)
hl('पूरे परिवार का पानी', 'एक नल से', st(23) - 0.05, st(24) - 0.05, tp=at(23, 'एक') - 0.1, color='y')
el('<div class="chip g" id="ID" style="left:0;right:0;margin:0 auto;width:fit-content;top:1250px">एक बूंद भी बर्बाद नहीं</div>', at(23, 'एक', 1) - 0.05, st(24) - 0.05, 'autoAlpha:0,y:40', s='sfx3005')
# L24 - callback
shot('rokitchen17', 0.5, st(24) - 0.05, st(25) - 0.05, zoom=(1.0, 1.15), top=0.6)
hl('तो अगली बार याद रखिए', 'साफ़ ही नहीं…', st(24) - 0.05, at(24, 'नहीं,') - 0.1, tp=at(24, 'सिर्फ़') - 0.1, color='c')
hl('पानी', 'मिनरल्स से भरा भी!', at(24, 'नहीं,') - 0.1, st(25) - 0.05, tp=at(24, 'से') - 0.3, color='g')
# L25 - which water at your home? we'll show the difference at your home, free
shot('glassro15', 0.4, st(25) - 0.05, at(25, 'आपके', 1) - 0.15, 'dim', top=0.7)
hl('आपके घर में', 'कौन सा पानी?', st(25) - 0.05, at(25, 'आपके', 1) - 0.15, tp=at(25, 'सा') - 0.2, color='y')
for k, (lab, w) in enumerate([('RO', 'RO,'), ('बोरिंग', 'बोरिंग'), ('नगरपालिका', 'नगरपालिका')]):
    try: t = at(25, w) - 0.05
    except AssertionError: t = st(25) + 2.0 + k * 0.5
    el(f'<div class="chip" id="ID" style="left:0;right:0;margin:0 auto;width:fit-content;top:{900 + k * 140}px">{lab}</div>', t, at(25, 'आपके', 1) - 0.15, 'autoAlpha:0,x:-200', s='sfx3005', g=-16)
shot('phtest3', 9.0, at(25, 'आपके', 1) - 0.15, st(26) - 0.05, zoom=(1.0, 1.1))
hl('हम आपके घर आकर', 'फ़र्क दिखाएंगे', at(25, 'आपके', 1) - 0.15, st(26) - 0.05, tp=at(25, 'दिखाएंगे') - 0.3, color='y')
stamp('मुफ़्त', at(25, 'दिखाएंगे') + 0.6, st(26) - 0.05, top=1080, cls='g')
# L26 - CTA
shot('kangen2', 40.0, st(26) - 0.05, DUR, 'dim', zoom=(1.0, 1.08))
el('<div class="cta" id="ID"><div class="a">फ़र्क अपनी आँखों से देखिए</div><div class="b">आज ही फ्री डेमो बुक कराएं</div><div class="c">Enagic Kangen • चोटिला</div></div>', st(26) - 0.05, DUR, 'autoAlpha:0,y:120', 'back.out(1.6)', d=.5, s='sfx1143', g=-10)
# brand badge from the Kangen reveal onwards (not in the first half, so it never looks like an ad)
els.append('<div class="badge" id="bdg">Enagic Kangen • चोटिला</div>')
T(f'tl.set("#bdg",{{visibility:"visible"}},{BADGE_T:.3f});tl.fromTo("#bdg",{{autoAlpha:0}},{{autoAlpha:.9,duration:.4}},{BADGE_T:.3f});tl.set("#bdg",{{visibility:"hidden"}},{st(26) - 0.05:.3f});')
# shot-change whooshes (soft)
for t in [st(k) - 0.05 for k in (2, 4, 6, 9, 12, 14, 15, 17, 19, 20, 22, 23, 24, 25)]: sfx(t, 'sfx166', -21)

overlays = '<div class="topfade"></div><div class="botfade"></div><div class="vign"></div><svg class="grain" width="1080" height="1920"><filter id="nz"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="3"/></filter><rect width="1080" height="1920" filter="url(#nz)"/></svg>'
css = open('style.css').read()
html = f'''<!doctype html>
<html lang="hi"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>Kangen reel 4</title><script src="gsap.min.js"></script><style>{css}</style></head>
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
json.dump(SFX, open('sfx.json', 'w'))
print('ok', len(els), 'elements', len(tw), 'tweens', len(SFX), 'sfx', 'DUR', DUR)
