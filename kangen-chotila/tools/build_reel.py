# build.py - Kangen Chotila reel v6 (alkaline water explainer, 60 s). Writes index.html, assets/*.mp4 cuts, sfx.json
import json, os, subprocess
P = os.path.dirname(os.path.abspath(__file__)); os.chdir(P)
B = json.load(open('beats.json')); DUR = 59.94
W, H = 1080, 1920
def sh(c): subprocess.run(c, shell=True, check=True)
def at(i, word, k=0, end=False):
    hits = [w for w in B[i - 1]['words'] if word in w[0]]
    assert hits, (i, word)
    return hits[k][2] if end else hits[k][1]
st = lambda i: B[i - 1]['start']; en = lambda i: B[i - 1]['end']

def cut(name, src, a, b, w=W, h=H, speed=1.0, top=1.0):
    out = f'assets/{name}.mp4'
    if not os.path.exists(out):
        pre = f"crop=iw:ih*{top}:0:0," if top < 1 else ""
        vf = f"{pre}setpts=PTS/{speed},scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},fps=30"
        sh(f'ffmpeg -y -v error -ss {a} -t {b - a} -i raw/{src}.mp4 -an -vf "{vf}" -c:v libx264 -crf 18 -preset veryfast -g 30 -keyint_min 30 -pix_fmt yuv420p -movflags +faststart {out}')
    return out

els, tw, SFX = [], [], []
def T(s): tw.append(s)
n = [0]
def nid(p='e'): n[0] += 1; return f'{p}{n[0]}'
def sfx(t, f, g=-14): SFX.append((round(t, 3), f, g))
def video(src, t0, t1, cls='vid', style=''):
    i = nid('v'); els.append(f'<video id="{i}" class="{cls}" src="{src}" muted playsinline data-start="{t0:.3f}" data-duration="{t1 - t0:.3f}" style="{style}"></video>'); return i
def scene(t0, t1, inner, fade=0.2):
    i = nid('s'); els.append(f'<div id="{i}" class="scene">{inner}</div>')
    T(f'tl.set("#{i}",{{autoAlpha:0}},0);')
    T(f'tl.fromTo("#{i}",{{autoAlpha:0}},{{autoAlpha:1,duration:{fade},ease:"none"}},{t0:.3f});')
    if t1 < DUR: T(f'tl.to("#{i}",{{autoAlpha:0,duration:0.16,ease:"none"}},{t1 - 0.16:.3f});')
    return i
def pop(sel, t, dur=0.35, frm='scale:0.6', ease='back.out(2)', to=''):
    T(f'tl.fromTo("{sel}",{{autoAlpha:0,{frm}}},{{autoAlpha:1,scale:1,x:0,y:0,{to}duration:{dur},ease:"{ease}"}},{t:.3f});')
def srcchip(t): return f'<div class="src"><span>{t}</span></div>'

# ---------------- background ----------------
els.append('<div id="bg" class="bg"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div></div>')
video(cut('tex1', 'mk44766', 0.0, 17.5), 0, 17.4, 'vid tex')
video(cut('tex2', 'mk51960', 0.0, 16.4), 17.4, 33.8, 'vid tex')
video(cut('tex3', 'mk44763', 0.0, 17.1), 33.8, 50.9, 'vid tex')
video(cut('tex4', 'mk44766', 1.0, 5.0), 50.9, DUR, 'vid tex')

KID = '''<svg viewBox="0 0 220 260"><path d="M120 16 C60 10 22 64 26 130 C30 200 76 248 132 240 C172 234 176 196 158 176 C140 158 138 138 156 118 C176 96 186 66 170 40 C160 24 142 18 120 16 Z" fill="#d63a6e" stroke="#fff" stroke-width="6"/>
<path d="M150 130 C120 130 104 120 96 100 M150 130 C120 134 104 150 98 170" stroke="#f8bbd0" stroke-width="7" fill="none" stroke-linecap="round"/>
<g class="stones" fill="#e8ddd5" stroke="#5d4037" stroke-width="4"><path d="M84 84 l14 -6 l12 8 l-2 14 l-14 4 l-12 -8 z"/><path d="M70 150 l10 -8 l12 4 l2 12 l-10 8 l-12 -4 z"/><path d="M104 192 l10 -6 l10 6 l-2 10 l-12 4 l-8 -6 z"/></g></svg>'''

# ---------------- scenes v6 ----------------
def ph_scale(marker_id='phm'):
    cols = ['#e53935','#f4511e','#fb8c00','#fdd835','#c0ca33','#7cb342','#43a047','#26a69a','#00acc1','#1e88e5','#3949ab','#5e35b1','#7b1fa2','#6a1b9a','#4a148c']
    cells = ''.join(f'<div class="phc" style="background:{c}"><span>{k}</span></div>' for k, c in enumerate(cols))
    return f'<div class="phbar">{cells}</div><div class="phmark" id="{marker_id}"><svg viewBox="0 0 60 40"><path d="M30 38 L4 4 L56 4 Z" fill="#fff"/></svg><b id="{marker_id}t">7</b></div>'

# S1 hook: celebrities pay hundreds of rupees a bottle for alkaline water - why?
s = scene(0.0, st(2) - 0.05, f'''
  <video id="vsplash" class="vid full" src="{cut('bw_splash', 'blackwater13', 0.0, 3.3)}" muted playsinline data-start="0" data-duration="3.3"></video>
  <video id="vblk" class="vid full" src="{cut('bw_hand', 'blackwater5', 0.2, 3.9)}" muted playsinline data-start="3.25" data-duration="3.7"></video>
  <div class="shade top"></div><div class="shade bot"></div>
  <div class="hookA" id="ha">સેલિબ્રિટી ને ક્રિકેટરો</div>
  <div class="hookB" id="hb"><span class="yl">₹ સેંકડો</span>ની એક બોટલ!</div>
  <div class="hookC" id="hc">આલ્કલાઇન વોટર</div>
  <div class="why" id="why">કેમ?</div>
''', fade=0.01)
pop('#ha', 0.28, 0.35, 'y:-50', 'power3.out')
pop('#hb', at(1, 'સેંકડો') - 0.05, 0.35, 'scale:1.7', 'power4.out')
pop('#hc', at(1, 'આલ્કલાઇન') - 0.05, 0.35, 'y:40', 'back.out(2)')
T(f'tl.to("#ha,#hb,#hc",{{autoAlpha:0,duration:.15}},{at(1, "કેમ") - 0.25:.3f});')
pop('#why', at(1, 'કેમ') - 0.1, 0.4, 'scale:3', 'power4.out')
T(f'tl.fromTo("#vsplash",{{scale:1.15}},{{scale:1,duration:3.3,ease:"power1.out"}},0);tl.fromTo("#vblk",{{scale:1}},{{scale:1.12,duration:3.7,ease:"none"}},3.25);')
sfx(0.0, 'sfx1311', -12); sfx(at(1, 'સેંકડો') - 0.05, 'sfx2364', -12); sfx(at(1, 'કેમ') - 0.1, 'sfx3005', -9)

# S2 pH explained
s = scene(st(2) - 0.05, st(3) - 0.05, f'''
  <div class="ttl" id="pht">પાણીનું <span class="cy">pH</span></div>
  <div class="phwrap">{ph_scale('phm')}
    <div class="phlab l" id="pl1">એસિડિક<br><small>લીંબુ જેવું</small></div><div class="phlab m" id="pl2">ન્યુટ્રલ</div><div class="phlab r" id="pl3">આલ્કલાઇન</div></div>
  <div class="lemon" id="lem"><svg viewBox="0 0 120 120"><ellipse cx="60" cy="60" rx="50" ry="38" fill="#ffe14d" stroke="#fff" stroke-width="5"/><ellipse cx="60" cy="60" rx="34" ry="24" fill="#fff59d"/></svg></div>
''')
pop('#pht', st(2), 0.35, 'y:-40', 'power3.out')
T(f'tl.fromTo("#{s} .phc",{{autoAlpha:0,y:60}},{{autoAlpha:1,y:0,duration:.25,stagger:.035,ease:"back.out(2)"}},{at(2, "પાણીનું") - 0.1:.3f});')
T(f'tl.fromTo("#phm",{{autoAlpha:0,x:450}},{{autoAlpha:1,x:450,duration:.2}},{at(2, "સાત") - 0.05:.3f});')
pop('#pl2', at(2, 'ન્યુટ્રલ') - 0.1, 0.3, 'y:20')
T(f'tl.to("#phm",{{x:130,duration:.5,ease:"power2.inOut"}},{at(2, "નીચે"):.3f});tl.call(function(){{}},null,{at(2, "નીચે"):.3f});')
T(f'var p1={{v:7}}; tl.to(p1,{{v:2,duration:.5,ease:"power2.inOut",onUpdate:function(){{document.getElementById("phmt").textContent=Math.round(p1.v)}}}},{at(2, "નીચે"):.3f});')
pop('#pl1', at(2, 'એસિડિક') - 0.1, 0.3, 'y:20'); pop('#lem', at(2, 'એસિડિક'), 0.35, 'scale:0.3', 'back.out(3)')
T(f'tl.to("#phm",{{x:770,duration:.6,ease:"power2.inOut"}},{at(2, "ઉપર"):.3f});')
T(f'var p2={{v:2}}; tl.to(p2,{{v:12,duration:.6,ease:"power2.inOut",onUpdate:function(){{document.getElementById("phmt").textContent=Math.round(p2.v)}}}},{at(2, "ઉપર"):.3f});')
pop('#pl3', at(2, 'આલ્કલાઇન') - 0.1, 0.3, 'y:20')
sfx(st(2), 'sfx1490', -17); sfx(at(2, 'એસિડિક'), 'sfx3005', -15); sfx(at(2, 'આલ્કલાઇન') - 0.1, 'sfx3005', -15)

# S3 blood pH 7.4 -> the craze
BLOOD = '<svg viewBox="0 0 120 150"><path d="M60 6 C60 6 14 70 14 96 A46 46 0 0 0 106 96 C106 70 60 6 60 6 Z" fill="#e53935" stroke="#fff" stroke-width="6"/><ellipse cx="42" cy="96" rx="9" ry="16" fill="#fff" opacity=".4"/></svg>'
s = scene(st(3) - 0.05, st(4) - 0.05, f'''
  <div class="ttl" id="bt1">આપણા <span class="rd">લોહીનું</span> pH?</div>
  <div class="blood" id="bl">{BLOOD}</div>
  <div class="bignum" id="bn"><span id="bnv">0.0</span></div>
  <div class="phwrap low">{ph_scale('phm2')}</div>
  <div class="tag2" id="tg2">થોડું <span class="cy">આલ્કલાઇન</span></div>
  <div class="craze" id="cz">એટલે આ પાણીનો <span class="yl">ક્રેઝ!</span></div>
''')
pop('#bt1', st(3), 0.35, 'y:-40', 'power3.out'); pop('#bl', at(3, 'લોહીનું') - 0.1, 0.4, 'scale:0.3', 'back.out(2.5)')
T(f'tl.fromTo("#{s} .phc",{{autoAlpha:0}},{{autoAlpha:1,duration:.3,stagger:.02}},{at(3, "pH") :.3f});')
pop('#bn', at(3, 'સાત') - 0.1, 0.3, 'scale:0.5')
T(f'var b1={{v:0}}; tl.to(b1,{{v:7.4,duration:1.1,ease:"power2.out",onUpdate:function(){{document.getElementById("bnv").textContent=b1.v.toFixed(1)}}}},{at(3, "સાત") - 0.1:.3f});')
T(f'tl.fromTo("#phm2",{{autoAlpha:0,x:450}},{{autoAlpha:1,x:476,duration:.8,ease:"power2.out"}},{at(3, "સાત"):.3f});tl.set("#phm2t",{{textContent:"7.4"}},0);')
pop('#tg2', at(3, 'થોડું') - 0.05, 0.3, 'y:30')
T(f'tl.to("#bl,#bn",{{autoAlpha:.25,duration:.3}},{at(3, "એટલે") - 0.1:.3f});')
pop('#cz', at(3, 'એટલે') - 0.05, 0.4, 'scale:1.6', 'power4.out')
sfx(st(3), 'sfx1490', -17); sfx(at(3, 'સાત'), 'sfx2364', -14); sfx(at(3, 'ક્રેઝ') - 0.1, 'sfx3005', -12)

# S4 the twist: made at home, with electricity
BOLT = '<svg viewBox="0 0 100 140"><path d="M58 4 L14 80 L48 80 L36 136 L88 52 L54 52 Z" fill="#ffd84a" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></svg>'
s = scene(st(4) - 0.05, st(5) - 0.05, f'''
  <video id="vbat" class="vid full" src="{cut('elec_battery', 'electro0', 6.8, 10.6)}" muted playsinline data-start="{st(4) - 0.05:.3f}" data-duration="3.8"></video>
  <div class="shade top"></div><div class="shade bot"></div>
  <div class="ttl" id="tw">હવે <span class="yl">મજાની વાત</span></div>
  <div class="bolt" id="bo">{BOLT}</div>
  <div class="twist" id="tw2">ઘરે, <span class="yl">વીજળીથી</span> બને!</div>
''')
pop('#tw', st(4), 0.3, 'y:-40', 'power3.out'); pop('#bo', at(4, 'વીજળીથી') - 0.15, 0.35, 'scale:0.2', 'back.out(3)')
pop('#tw2', at(4, 'ઘરે') - 0.05, 0.35, 'y:40')
T(f'tl.fromTo("#bo",{{rotation:-8}},{{rotation:8,duration:.08,repeat:7,yoyo:true}},{at(4, "વીજળીથી") + 0.2:.3f});')
sfx(st(4), 'sfx2364', -14); sfx(at(4, 'વીજળીથી') - 0.15, 'sfx1317', -10)

# S5 electrolysis: minus side alkaline, plus side acidic
s = scene(st(5) - 0.05, st(6) - 0.05, f'''
  <video id="velec" class="vid full" src="{cut('elec_bubbles', 'electro34', 47.5, 54.3, speed=0.95)}" muted playsinline data-start="{st(5) - 0.05:.3f}" data-duration="7.2"></video>
  <div class="shade top"></div><div class="shade bot"></div>
  <div class="pole minus" id="pm"><b>−</b><span>આલ્કલાઇન</span></div>
  <div class="pole plus" id="pp"><b>+</b><span>એસિડિક</span></div>
  <div class="ttl small" id="el">ઇલેક્ટ્રોલિસિસ</div>
''')
pop('#pm', at(5, 'માઇનસ') - 0.05, 0.35, 'x:-200', 'back.out(2)'); pop('#pp', at(5, 'પ્લસ') - 0.05, 0.35, 'x:200', 'back.out(2)')
pop('#el', at(5, 'ઇલેક્ટ્રોલિસિસ') - 0.15, 0.4, 'scale:1.6', 'power4.out')
sfx(st(5), 'sfx1490', -17); sfx(at(5, 'માઇનસ'), 'sfx3005', -14); sfx(at(5, 'પ્લસ'), 'sfx3005', -14); sfx(at(5, 'ઇલેક્ટ્રોલિસિસ') - 0.15, 'sfx2364', -13)

# S6 Enagic Kangen does exactly this; recognised in Japan as a medical device
JP = '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><circle cx="30" cy="20" r="11" fill="#bc002d"/></svg>'
s = scene(st(6) - 0.05, st(7) - 0.05, f'''
  <video id="vk8" class="vid full" src="{cut('k8_screen', 'kangen2', 13.0, 20.4)}" muted playsinline data-start="{st(6) - 0.05:.3f}" data-duration="7.3"></video>
  <div class="shade top"></div><div class="shade bot"></div>
  <div class="jp top" id="jp1">{JP}<span>જાપાનનું Enagic Kangen</span></div>
  <div class="med" id="md"><svg viewBox="0 0 100 100"><rect x="6" y="6" width="88" height="88" rx="22" fill="#fff"/><path d="M40 22h20v18h18v20H60v18H40V60H22V40h18z" fill="#e53935"/></svg><div>જાપાનમાં<br><span class="yl">મેડિકલ ડિવાઇસ</span>ની માન્યતા</div></div>
''')
pop('#jp1', at(6, 'જાપાનનું') - 0.1, 0.4, 'y:-60', 'back.out(2)')
pop('#md', at(6, 'જાપાનમાં') - 0.1, 0.45, 'scale:0.5', 'back.out(2)')
T(f'tl.fromTo("#vk8",{{scale:1.0}},{{scale:1.12,duration:7.3,ease:"none"}},{st(6):.3f});')
sfx(st(6), 'sfx1490', -17); sfx(at(6, 'જાપાનનું') - 0.1, 'sfx1317', -11); sfx(at(6, 'મેડિકલ') - 0.1, 'sfx2364', -12)

# S7 filter: dirt & chlorine out, minerals in; alkaline to drink, acidic to clean
s = scene(st(7) - 0.05, st(8) - 0.05, f'''
  <video id="vpour" class="vid full" src="{cut('k8_pour', 'phtest3', 0.6, 5.6, speed=1.0)}" muted playsinline data-start="{st(7) - 0.05:.3f}" data-duration="4.9"></video>
  <video id="vspray" class="vid full" src="{cut('k8_spray2', 'phtest20', 11.8, 15.2, speed=1.0, top=0.6)}" muted playsinline data-start="{at(7, 'પીવા') + 0.9:.3f}" data-duration="{st(8) - at(7, 'પીવા') - 0.85:.3f}"></video>
  <div class="shade top"></div><div class="shade bot"></div>
  <div class="fl1" id="fo1">✗ ગંદકી</div><div class="fl1 b" id="fo2">✗ ક્લોરિન</div><div class="fl1 g" id="fo3">✓ મિનરલ્સ</div>
  <div class="use u1" id="u1">પીવા માટે: <b>આલ્કલાઇન</b></div>
  <div class="use u2" id="u2">સફાઈ માટે: <b>એસિડિક</b></div>
''')
pop('#fo1', at(7, 'ગંદકી') - 0.05, 0.3, 'x:-160'); pop('#fo2', at(7, 'ક્લોરિન') - 0.05, 0.3, 'x:-160'); pop('#fo3', at(7, 'મિનરલ્સ') - 0.05, 0.3, 'x:160')
T(f'tl.to("#fo1,#fo2,#fo3",{{autoAlpha:0,duration:.2}},{at(7, "પીવા") - 0.15:.3f});')
pop('#u1', at(7, 'પીવા') - 0.05, 0.35, 'y:40'); pop('#u2', at(7, 'સફાઈ') - 0.05, 0.35, 'y:40')
sfx(at(7, 'ગંદકી') - 0.05, 'sfx3005', -15); sfx(at(7, 'મિનરલ્સ') - 0.05, 'sfx3005', -13); sfx(at(7, 'પીવા') - 0.05, 'sfx1490', -17)

# S8 free pH demo at home
s = scene(st(8) - 0.05, st(9) - 0.05, f'''
  <div class="ttl" id="dm">pH ટેસ્ટ સાથે <span class="yl">ડેમો</span></div>
  <div class="glasses"><div class="gls" id="g1"><div class="gw" id="gw1"></div><span>નળનું પાણી</span></div><div class="gls" id="g2"><div class="gw" id="gw2"></div><span>Kangen</span></div></div>
  <div class="dropper" id="dp"><svg viewBox="0 0 60 160"><rect x="20" y="0" width="20" height="40" rx="8" fill="#333"/><path d="M18 40h24v80l-12 24l-12-24z" fill="#e0f7fa" stroke="#fff" stroke-width="4"/></svg></div>
  <div class="chips2"><div class="c2" id="c21">તમારા ઘરે</div><div class="c2 free" id="c22">એકદમ ફ્રી</div></div>
''')
pop('#dm', st(8), 0.35, 'y:-40', 'power3.out'); pop('#g1', st(8) + 0.1, 0.3, 'y:80'); pop('#g2', st(8) + 0.2, 0.3, 'y:80')
T(f'tl.fromTo("#dp",{{autoAlpha:0,x:-180,y:-60}},{{autoAlpha:1,x:-180,y:0,duration:.3}},{at(8, "pH") - 0.4:.3f});')
T(f'tl.to("#gw1",{{backgroundColor:"#d9e85a",duration:.5}},{at(8, "pH") - 0.05:.3f});')
T(f'tl.to("#dp",{{x:180,duration:.4,ease:"power2.inOut"}},{at(8, "ટેસ્ટ") - 0.05:.3f});')
T(f'tl.to("#gw2",{{backgroundColor:"#7b3fc4",duration:.6}},{at(8, "સાથે"):.3f});')
pop('#c21', at(8, 'તમારા') - 0.05, 0.3, 'y:30'); pop('#c22', at(8, 'એકદમ') - 0.05, 0.4, 'scale:1.8', 'power4.out')
sfx(st(8), 'sfx1490', -17); sfx(at(8, 'સાથે'), 'sfx1317', -11); sfx(at(8, 'એકદમ') - 0.05, 'sfx2364', -11)

# S9 CTA: call Hardevsinh
PHONE = '<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="#34d67f"/><path d="M34 26c4-2 8 6 9 10s-4 6-3 9c2 6 7 11 13 13c3 1 5-4 9-3s12 5 10 9c-2 6-8 10-14 9C40 71 27 58 25 40c-1-6 3-12 9-14z" fill="#fff"/></svg>'
s = scene(st(9) - 0.05, DUR, f'''
  <video id="vcta" class="vid full" src="{cut('k8_cta2', 'kangen2', 56.5, 62.5, speed=1.0)}" muted playsinline data-start="{st(9) - 0.05:.3f}" data-duration="{DUR - st(9) + 0.05:.3f}"></video>
  <div class="shade all"></div>
  <div class="phone" id="ph">{PHONE}</div>
  <div class="cta1" id="ct1">ફ્રી ડેમો માટે<br>અત્યારે જ ફોન કરો</div>
  <div class="who" id="who">હરદેવસિંહ</div>
  <div class="endbrand" id="eb">Enagic Kangen Water • ચોટીલા</div>
''')
pop('#ph', st(9), 0.35, 'scale:0.3', 'back.out(3)')
T(f'tl.fromTo("#ph",{{rotation:-12}},{{rotation:12,duration:.07,repeat:13,yoyo:true}},{st(9) + 0.4:.3f});')
pop('#ct1', st(9) + 0.05, 0.35, 'y:40'); pop('#who', at(9, 'હરદેવસિંહને') - 0.05, 0.4, 'scale:1.8', 'power4.out')
pop('#eb', at(9, 'Enagic') - 0.1, 0.4, 'y:40', 'back.out(2)')
sfx(st(9), 'sfx2364', -12); sfx(at(9, 'હરદેવસિંહને'), 'sfx3005', -10)
# ---------------- captions (word by word) ----------------
def chunks(words):
    out, cur = [], []
    for w in words:
        cur.append(w); txt = ' '.join(x[0] for x in cur)
        if len(cur) >= 3 or len(txt) > 16 or w[0][-1] in '.?!:,':
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out
allch = [c for b in B for c in chunks(b['words'])]
for k, c in enumerate(allch):
    t0 = c[0][1] - 0.04
    t1 = (allch[k + 1][0][1] - 0.04) if k + 1 < len(allch) else c[-1][2] + 0.6
    t1 = min(t1, c[-1][2] + 0.5)
    cid = nid('cap')
    spans = ''.join(f'<span class="w" id="{cid}w{j}">{w[0].rstrip(",:.")}</span> ' for j, w in enumerate(c))
    els.append(f'<div class="cap" id="{cid}"><div class="cbox">{spans}</div></div>')
    T(f'tl.set("#{cid}",{{autoAlpha:0}},0);tl.set("#{cid}",{{autoAlpha:1}},{t0:.3f});tl.fromTo("#{cid} .cbox",{{scale:.88}},{{scale:1,duration:.12,ease:"back.out(3)"}},{t0:.3f});tl.set("#{cid}",{{autoAlpha:0}},{t1:.3f});')
    for j, w in enumerate(c):
        T(f'tl.set("#{cid}w{j}",{{color:"#FFD84A"}},{w[1]:.3f});tl.set("#{cid}w{j}",{{color:"#ffffff"}},{w[2] + 0.02:.3f});')

css = open('style.css').read()
html = f'''<!doctype html>
<html lang="gu"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>Kangen reel 1</title><script src="gsap.min.js"></script><style>{css}</style></head>
<body><div id="root" data-composition-id="main" data-start="0" data-width="{W}" data-height="{H}" data-duration="{DUR}">
{chr(10).join(els)}
<audio id="mix" src="assets/mix.wav" data-start="0" data-duration="{DUR}"></audio>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
tl.fromTo(".b1",{{x:-120,y:-80}},{{x:160,y:140,duration:{DUR},ease:"sine.inOut"}},0);
tl.fromTo(".b2",{{x:140,y:100}},{{x:-160,y:-120,duration:{DUR},ease:"sine.inOut"}},0);
tl.fromTo(".b3",{{x:0,y:200}},{{x:-60,y:-200,duration:{DUR},ease:"sine.inOut"}},0);
{chr(10).join(tw)}
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl;
</script></body></html>'''
open('index.html', 'w').write(html)
json.dump(SFX, open('sfx.json', 'w'))
print('ok', len(els), 'elements', len(tw), 'tweens', len(SFX), 'sfx')
