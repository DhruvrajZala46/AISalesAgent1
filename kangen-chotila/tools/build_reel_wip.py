# build.py - Kangen Chotila reel #1 (health signals). Writes index.html, assets/*.mp4 cuts, assets/mix.wav
import json, os, subprocess, re
P = os.path.dirname(os.path.abspath(__file__)); os.chdir(P)
B = json.load(open('beats.json')); DUR = 86.2
W, H = 1080, 1920
def sh(c): subprocess.run(c, shell=True, check=True)

def at(i, word, k=0, end=False):
    """start (or end) time of the k-th word in line i that contains `word`"""
    hits = [w for w in B[i - 1]['words'] if word in w[0]]
    assert hits, (i, word)
    return hits[k][2] if end else hits[k][1]
st = lambda i: B[i - 1]['start']; en = lambda i: B[i - 1]['end']

# ---------------- clip cuts (cover-cropped, 30 fps, silent) ----------------
CUTS = {}
def cut(name, src, a, b, w=W, h=H, speed=1.0, extra=''):
    out = f'assets/{name}.mp4'; CUTS[name] = (src, a, b, speed)
    if not os.path.exists(out):
        vf = f"setpts=PTS/{speed},scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},fps=30{extra}"
        sh(f'ffmpeg -y -v error -ss {a} -t {b - a} -i raw/{src}.mp4 -an -vf "{vf}" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p {out}')
    return f'assets/{name}.mp4'

els, tw = [], []
def T(s): tw.append(s)
n = [0]
def nid(p='e'): n[0] += 1; return f'{p}{n[0]}'

def video(src, t0, t1, style='', cls='vid'):
    i = nid('v'); els.append(f'<video id="{i}" class="{cls}" src="{src}" muted playsinline data-start="{t0:.3f}" data-duration="{t1 - t0:.3f}" style="{style}"></video>'); return i

def scene(t0, t1, inner, fade=0.22, cls='scene', pop=False):
    i = nid('s'); els.append(f'<div id="{i}" class="{cls}">{inner}</div>')
    T(f'tl.set("#{i}",{{autoAlpha:0}},0);')
    if pop: T(f'tl.fromTo("#{i}",{{autoAlpha:0,scale:1.06}},{{autoAlpha:1,scale:1,duration:{fade},ease:"power2.out"}},{t0:.3f});')
    else: T(f'tl.fromTo("#{i}",{{autoAlpha:0}},{{autoAlpha:1,duration:{fade},ease:"none"}},{t0:.3f});')
    T(f'tl.to("#{i}",{{autoAlpha:0,duration:0.18,ease:"none"}},{t1 - 0.18:.3f});')
    return i

def popin(sel, t, dur=0.35, frm='scale:0.6', ease='back.out(2)'):
    T(f'tl.fromTo("{sel}",{{autoAlpha:0,{frm}}},{{autoAlpha:1,scale:1,x:0,y:0,duration:{dur},ease:"{ease}"}},{t:.3f});')

SFX = []   # (time, file, gain_db)
def sfx(t, f, g=-14): SFX.append((t, f, g))

def badge(num, label, red=False):
    c = 'badge red' if red else 'badge'
    return f'<div class="{c}"><div class="num">{num}</div><div class="lab">{label}</div></div>'
def src(text): return f'<div class="src">{text}</div>'

# ---------------- background (always) ----------------
els.append('<div id="bg" class="bg"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div></div>')
v = video(cut('bubbles', 'mk44766', 0.0, 17.5, speed=0.2 if False else 1.0), 0, 17.4, cls='vid tex')
v2 = video(cut('bubbles2', 'mk51960', 0.0, 16.4), 17.4, 33.8, cls='vid tex')
v3 = video(cut('bubbles3', 'mk44763', 0.0, 17.1), 33.8, 50.9, cls='vid tex')
v4 = video(cut('bubbles4', 'mk44766', 0.5, 17.9), 50.9, 68.3, cls='vid tex')
v5 = video(cut('bubbles5', 'mk51960', 0.0, 16.4), 68.3, DUR, cls='vid tex')

# ---------------- S1 hook: elder at dusk + "માથું ભારે?" ----------------
s = scene(0.0, st(2) + 0.05, f'''
  <video class="vid full" src="{cut('hook_elder', 'dada9', 0.8, 3.9)}" muted playsinline data-start="0" data-duration="3.0"></video>
  <div class="shade top"></div><div class="shade bot"></div>
  <div class="clock" id="clk"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="none" stroke="#FFD84A" stroke-width="7"/><path id="clkh" d="M50 50 L50 24" stroke="#fff" stroke-width="7" stroke-linecap="round"/><path d="M50 50 L70 50" stroke="#fff" stroke-width="7" stroke-linecap="round"/></svg><span>બપોરે 3 વાગે</span></div>
  <div class="hook1" id="hk1">બપોર પડે ને…</div>
  <div class="hook2" id="hk2"><span class="yl">માથું ભારે</span> થઈ જાય?</div>
  <div class="pulse" id="pls"></div>
''', fade=0.01)
T('tl.fromTo("#hk1",{autoAlpha:0,y:40},{autoAlpha:1,y:0,duration:.3,ease:"power3.out"},0.30);')
popin('#clk', 0.35, 0.4)
T('tl.fromTo("#clkh",{rotation:-90,transformOrigin:"50px 50px"},{rotation:0,duration:.8,ease:"power2.out"},0.4);')
popin('#hk2', at(1, 'માથું') - 0.05, 0.35, 'scale:1.6', 'power4.out')
T(f'tl.fromTo("#pls",{{autoAlpha:0,scale:.4}},{{autoAlpha:.9,scale:1.4,duration:.45,ease:"power2.out",repeat:2,yoyo:true}},{at(1, "ભારે"):.3f});')
T(f'tl.fromTo("#{s} .full",{{scale:1.0}},{{scale:1.12,duration:3,ease:"none"}},0);')
sfx(0.25, 'sfx1490', -16); sfx(at(1, 'માથું') - 0.05, 'sfx2364', -12)

# ---------------- S2: two problem cards ----------------
stomach = '<svg viewBox="0 0 120 120"><path d="M38 18 C30 40 26 52 34 66 C44 84 30 96 44 104 C62 112 92 104 96 82 C100 62 86 54 74 58 C62 62 60 48 66 36 C70 26 62 16 52 16" fill="#FF8A65" stroke="#fff" stroke-width="5"/><path d="M50 72 q10 -8 20 0 t20 0" stroke="#7a2b12" stroke-width="5" fill="none" stroke-linecap="round"/></svg>'
drop = '<svg viewBox="0 0 120 120"><path d="M60 10 C60 10 22 56 22 78 A38 38 0 0 0 98 78 C98 56 60 10 60 10 Z" fill="#E8B21C" stroke="#fff" stroke-width="5"/><ellipse cx="46" cy="76" rx="8" ry="14" fill="#fff" opacity=".45"/></svg>'
s = scene(st(2) - 0.05, st(3) - 0.02, f'''
  <div class="qcard" id="q1"><div class="ico">{stomach}</div><div class="qt">પેટ સાફ<br>ન આવે?</div></div>
  <div class="qcard" id="q2"><div class="ico">{drop}</div><div class="qt">પેશાબ<br><span class="yl">પીળો</span> આવે?</div></div>
''')
T(f'tl.fromTo("#q1",{{autoAlpha:0,x:-500}},{{autoAlpha:1,x:0,duration:.38,ease:"power3.out"}},{at(2, "પેટ") - 0.05:.3f});')
T(f'tl.fromTo("#q2",{{autoAlpha:0,x:500}},{{autoAlpha:1,x:0,duration:.38,ease:"power3.out"}},{at(2, "પેશાબ") - 0.05:.3f});')
sfx(at(2, 'પેટ') - 0.05, 'sfx1490', -18); sfx(at(2, 'પેશાબ') - 0.05, 'sfx1490', -18)

# ---------------- S3: not illness - the body's cry for water ----------------
s = scene(st(3) - 0.02, st(4) - 0.02, f'''
  <video class="vid full" src="{cut('splash', 'mk51960', 2.0, 7.0)}" muted playsinline data-start="{st(3) - 0.02:.3f}" data-duration="4.7"></video>
  <div class="shade all"></div>
  <div class="big1" id="b1">આ <span class="strike" id="stk">બીમારી</span> નહીં…</div>
  <div class="big2" id="b2">શરીરની<br><span class="cy">પાણી માટેની બૂમ!</span></div>
''', fade=0.12, pop=True)
popin('#b1', at(3, 'ઘણી'), 0.3, 'y:40')
T(f'tl.fromTo("#stk",{{"--sx":0}},{{"--sx":1,duration:.35,ease:"power2.out"}},{at(3, "નહીં"):.3f});')
popin('#b2', at(3, 'શરીરની') - 0.05, 0.4, 'scale:0.5', 'back.out(2.2)')
sfx(st(3), 'sfx1311', -14); sfx(at(3, 'બૂમ'), 'sfx3005', -10)

# ---------------- S4: 4 signals, the 4th a warning ----------------
tiles = ''.join(f'<div class="tile{" warn" if k == 4 else ""}" id="t{k}"><div class="tn">{k}</div><div class="tq">{"?" if k < 4 else "⚠"}</div></div>' for k in range(1, 5))
s = scene(st(4) - 0.02, st(5) - 0.02, f'''
  <div class="ttl" id="t4t">શરીર પાણી માંગે ત્યારે<br><span class="yl">4 સંકેત</span> આપે છે</div>
  <div class="grid">{tiles}</div>
  <div class="warnline" id="wl">ચોથો = <span class="rd">આખા ગુજરાત</span> માટે ચેતવણી</div>
''')
popin('#t4t', st(4), 0.35, 'y:30')
for k in range(1, 5):
    popin(f'#t{k}', at(4, 'ચાર') + (k - 1) * 0.14, 0.32)
    sfx(at(4, 'ચાર') + (k - 1) * 0.14, 'sfx3005', -16)
T(f'tl.to("#t1,#t2,#t3",{{opacity:.35,duration:.3}},{at(4, "ચોથો"):.3f});')
T(f'tl.fromTo("#t4",{{scale:1}},{{scale:1.18,duration:.35,ease:"power2.out",yoyo:true,repeat:3}},{at(4, "ચોથો"):.3f});')
popin('#wl', at(4, 'ગુજરાત') - 0.05, 0.35, 'y:30')
sfx(at(4, 'ચોથો'), 'sfx2364', -12)

# ---------------- S5: signal 1 - head (1.5% water loss) ----------------
head = '''<svg viewBox="0 0 200 220"><path d="M100 14 C52 14 30 50 30 88 C30 116 42 132 50 146 L50 196 L132 196 L132 168 L152 168 C160 168 164 160 162 150 L160 132 L172 124 L158 98 C158 50 140 14 100 14 Z" fill="#163a5a" stroke="#9fe3f5" stroke-width="5"/>
<g id="rays" stroke="#FF5A5A" stroke-width="7" stroke-linecap="round"><path d="M64 40 L48 22"/><path d="M96 26 L96 4"/><path d="M128 40 L146 22"/></g>
<circle id="ache" cx="96" cy="70" r="26" fill="#FF5A5A" opacity=".85"/></svg>'''
s = scene(st(5) - 0.02, st(6) - 0.02, f'''
  {badge(1, 'માથું')}
  <div class="headwrap">{head}</div>
  <div class="tank"><div class="tankfill" id="tf"></div><div class="tankpct"><span id="pct">100</span>%</div><div class="tanklab">શરીરનું પાણી</div></div>
  <div class="minus" id="mn">−1.5%</div>
  <div class="chips">
    <div class="chip" id="c1">માથું દુખે</div><div class="chip" id="c2">થાક લાગે</div><div class="chip" id="c3">ધ્યાન તૂટે</div>
  </div>
  {src('અભ્યાસ: University of Connecticut (USA), 2012')}
''')
popin(f'#{s} .badge', st(5), 0.35)
sfx(st(5), 'sfx1490', -16)
T(f'tl.fromTo("#tf",{{height:"100%"}},{{height:"78%",duration:1.4,ease:"power2.inOut"}},{at(5, "દોઢ") - 0.2:.3f});')
T(f'var o1={{v:100}}; tl.to(o1,{{v:98.5,duration:1.4,ease:"power2.inOut",onUpdate:function(){{document.getElementById("pct").textContent=o1.v.toFixed(1).replace(".0","")}}}},{at(5, "દોઢ") - 0.2:.3f});')
popin('#mn', at(5, 'ટકા'), 0.3, 'scale:2', 'power4.out')
T(f'tl.fromTo("#rays",{{autoAlpha:0}},{{autoAlpha:1,duration:.15,repeat:5,yoyo:true}},{at(5, "માથું", 1):.3f});')
T(f'tl.fromTo("#ache",{{scale:.5,transformOrigin:"96px 70px"}},{{scale:1.25,duration:.4,repeat:5,yoyo:true}},{at(5, "માથું", 1):.3f});')
for k, wd in ((1, 'દુખે'), (2, 'થાક'), (3, 'ધ્યાન')):
    popin(f'#c{k}', at(5, wd) - 0.08, 0.3, 'y:30'); sfx(at(5, wd) - 0.08, 'sfx3005', -16)

# ---------------- S6: signal 2 - urine colour scale ----------------
cols = ['#FFFBE0', '#FFF4B0', '#FCE97A', '#F7DA4A', '#EDC32A', '#D9A51F', '#C08418', '#9C6214']
sw = ''.join(f'<div class="sw" style="background:{c}"></div>' for c in cols)
s = scene(st(6) - 0.02, st(7) - 0.02, f'''
  {badge(2, 'પેશાબનો રંગ')}
  <div class="scale">{sw}</div>
  <div class="marker" id="mk"><svg viewBox="0 0 60 40"><path d="M30 38 L4 4 L56 4 Z" fill="#fff"/></svg></div>
  <div class="verdict bad" id="vb">✗ ઘાટો પીળો = <b>પાણી ઓછું</b></div>
  <div class="verdict good" id="vg">✓ આછો પીળો = <b>બરાબર</b></div>
  {src('સ્રોત: NHS (UK) - પેશાબનો રંગ ચાર્ટ')}
''')
popin(f'#{s} .badge', st(6), 0.35); sfx(st(6), 'sfx1490', -16)
T(f'tl.fromTo("#{s} .sw",{{autoAlpha:0,y:60}},{{autoAlpha:1,y:0,duration:.3,stagger:.06,ease:"back.out(2)"}},{at(6, "રંગ") - 0.3:.3f});')
T(f'tl.fromTo("#mk",{{autoAlpha:0,x:820}},{{autoAlpha:1,x:820,duration:.2}},{at(6, "ઘાટો") - 0.1:.3f});')
popin('#vb', at(6, 'ઘાટો'), 0.3, 'y:30'); sfx(at(6, 'ઘાટો'), 'sfx2364', -14)
T(f'tl.to("#mk",{{x:95,duration:.7,ease:"power3.inOut"}},{at(6, "આછો") - 0.15:.3f});')
T(f'tl.to("#vb",{{autoAlpha:.3,duration:.3}},{at(6, "આછો") - 0.15:.3f});')
popin('#vg', at(6, 'બરાબર') - 0.05, 0.3, 'y:30'); sfx(at(6, 'બરાબર') - 0.05, 'sfx3005', -12)

# ---------------- S7: signal 3 - stomach ----------------
gut = '''<svg viewBox="0 0 240 240"><path d="M70 30 C40 34 34 70 52 82 C30 92 30 126 54 132 C30 146 40 184 72 182 C96 190 108 170 120 176 C134 188 170 194 186 168 C206 140 186 120 170 118 C194 108 196 76 172 66 C190 50 176 24 150 30 C132 18 108 22 100 34 C92 24 80 28 70 30 Z" fill="#FF9E80" stroke="#fff" stroke-width="6"/>
<path d="M78 70 q20 18 44 0 t44 0 M70 112 q24 18 50 0 t50 0 M80 152 q22 14 40 0 t44 0" stroke="#8c3a1e" stroke-width="7" fill="none" stroke-linecap="round"/>
<g id="cracks" stroke="#5a1c08" stroke-width="5" fill="none" stroke-linecap="round"><path d="M96 92 l10 10 l-6 10 l12 8"/><path d="M146 132 l-10 8 l8 10 l-10 10"/></g></svg>'''
s = scene(st(7) - 0.02, st(8) - 0.02, f'''
  {badge(3, 'પેટ')}
  <div class="gut">{gut}</div>
  <div class="flow"><span id="f1" class="fl">પાણી ઓછું</span><span id="f2" class="ar">➜</span><span id="f3" class="fl rd">પેટ સાફ ન આવે</span></div>
  {src('સ્રોત: NHS (UK) - કબજિયાતનાં કારણો')}
''')
popin(f'#{s} .badge', st(7), 0.35); sfx(st(7), 'sfx1490', -16)
popin(f'#{s} .gut', at(7, 'પેટ.') - 0.1, 0.4)
T(f'tl.fromTo("#cracks",{{autoAlpha:0}},{{autoAlpha:1,duration:.3}},{at(7, "ઓછું"):.3f});')
popin('#f1', at(7, 'પાણી') - 0.05, 0.3, 'y:20'); popin('#f2', at(7, 'પડે'), 0.25, 'x:-30'); popin('#f3', at(7, 'પેટ', 1) - 0.05, 0.3, 'y:20')
sfx(at(7, 'પેટ', 1) - 0.05, 'sfx3005', -14)

# ---------------- S8: signal 4 - kidney stones + stone belt ----------------
kid = '''<svg viewBox="0 0 220 260"><path d="M120 16 C60 10 22 64 26 130 C30 200 76 248 132 240 C172 234 176 196 158 176 C140 158 138 138 156 118 C176 96 186 66 170 40 C160 24 142 18 120 16 Z" fill="#c2185b" stroke="#fff" stroke-width="6"/>
<path d="M150 130 C120 130 104 120 96 100 M150 130 C120 134 104 150 98 170" stroke="#f8bbd0" stroke-width="7" fill="none" stroke-linecap="round"/>
<g id="stones" fill="#d7ccc8" stroke="#5d4037" stroke-width="4"><path d="M84 84 l14 -6 l12 8 l-2 14 l-14 4 l-12 -8 z"/><path d="M70 150 l10 -8 l12 4 l2 12 l-10 8 l-12 -4 z"/><path d="M104 192 l10 -6 l10 6 l-2 10 l-12 4 l-8 -6 z"/></g></svg>'''
states = ['રાજસ્થાન', 'પંજાબ', 'હરિયાણા', 'દિલ્હી', 'મહારાષ્ટ્ર', 'ગુજરાત']
stchips = ''.join(f'<div class="st{" gj" if s_ == "ગુજરાત" else ""}" id="st{k}">{s_}</div>' for k, s_ in enumerate(states))
s = scene(st(8) - 0.02, st(9) - 0.02, f'''
  {badge(4, 'પથરી', red=True)}
  <div class="kid">{kid}</div>
  <div class="belt" id="belt">ભારતનો <span class="rd">સ્ટોન બેલ્ટ</span></div>
  <div class="states">{stchips}</div>
  {src('સ્રોત: Foods (MDPI) રિવ્યુ, 2019 - ભારતનો સ્ટોન બેલ્ટ')}
''')
popin(f'#{s} .badge', st(8), 0.35); sfx(st(8), 'sfx2364', -12)
popin(f'#{s} .kid', at(8, 'પથરી.') - 0.1, 0.45)
T(f'tl.fromTo("#stones path",{{autoAlpha:0,scale:0,transformOrigin:"50% 50%"}},{{autoAlpha:1,scale:1,duration:.3,stagger:.12,ease:"back.out(3)"}},{at(8, "પથરી."):.3f});')
popin('#belt', at(8, 'સ્ટોન') - 0.1, 0.35, 'y:30')
for k in range(5): popin(f'#st{k}', at(8, 'બેલ્ટ') + k * 0.1, 0.25)
popin('#st5', at(8, 'ગુજરાત') - 0.05, 0.4, 'scale:2', 'power4.out')
T(f'tl.to("#st5",{{scale:1.12,duration:.3,yoyo:true,repeat:3}},{at(8, "ગુજરાત") + 0.4:.3f});')
sfx(at(8, 'ગુજરાત') - 0.05, 'sfx2364', -12)

# ---------------- S9: NIH - the biggest protection: enough water ----------------
s = scene(st(9) - 0.02, st(10) - 0.02, f'''
  <div class="authority" id="au"><b>NIH</b><span>અમેરિકાની રાષ્ટ્રીય આરોગ્ય સંસ્થા</span></div>
  <div class="kid small">{kid.replace('id="stones"', 'id="stones2"')}</div>
  <div class="wave" id="wave"></div>
  <div class="answer" id="ans">પથરીથી બચવાનો<br>સૌથી મોટો ઉપાય:<br><span class="cy big">પૂરતું પાણી</span></div>
  {src('સ્રોત: NIH / NIDDK - Kidney stones: Eating, diet & nutrition')}
''')
popin('#au', st(9), 0.35, 'y:-30'); sfx(st(9), 'sfx1490', -16)
popin(f'#{s} .kid', st(9) + 0.2, 0.35)
T(f'tl.fromTo("#wave",{{y:500}},{{y:0,duration:1.2,ease:"power2.out"}},{at(9, "પૂરતું") - 0.6:.3f});')
T(f'tl.to("#stones2 path",{{autoAlpha:0,y:120,duration:.6,stagger:.1,ease:"power2.in"}},{at(9, "પૂરતું") - 0.2:.3f});')
popin('#ans', at(9, 'પથરીથી') - 0.05, 0.4, 'y:40')
T(f'tl.fromTo("#ans .big",{{scale:.6}},{{scale:1,duration:.35,ease:"back.out(3)"}},{at(9, "પૂરતું"):.3f});')
sfx(at(9, 'પૂરતું'), 'sfx1311', -14)

# ---------------- S10: elders + winter: thirst drops ----------------
s = scene(st(10) - 0.02, st(11) - 0.02, f'''
  <video class="vid full" src="{cut('elder_well', 'village39', 0.3, 8.9)}" muted playsinline data-start="{st(10) - 0.02:.3f}" data-duration="8.6"></video>
  <div class="shade top"></div><div class="shade bot"></div>
  <div class="eld" id="ed">વડીલો <span class="yl">ધ્યાન રાખજો</span></div>
  <div class="echip" id="e1">ઉંમર <span class="up">▲</span>&nbsp;&nbsp;તરસ <span class="dn">▼</span></div>
  <div class="echip cold" id="e2">❄ ઠંડીમાં તરસ <span class="rd">−<span id="p40">0</span>%</span></div>
  <div class="echip go" id="e3">તરસની રાહ ન જુઓ!</div>
  <div class="src light">સ્રોત: University of New Hampshire (ઠંડી); Phillips et al. 1984 (ઉંમર)</div>
''')
popin('#ed', st(10), 0.35, 'y:-30'); sfx(st(10), 'sfx1490', -16)
popin('#e1', at(10, 'ઉંમર') - 0.05, 0.3, 'x:-200')
popin('#e2', at(10, 'ઠંડીમાં') - 0.05, 0.3, 'x:200')
T(f'var o2={{v:0}}; tl.to(o2,{{v:40,duration:.8,ease:"power2.out",onUpdate:function(){{document.getElementById("p40").textContent=Math.round(o2.v)}}}},{at(10, "ચાળીસ") - 0.1:.3f});')
popin('#e3', at(10, 'તરસની') - 0.05, 0.35, 'scale:1.5', 'power4.out')
sfx(at(10, 'ચાળીસ'), 'sfx2364', -14); sfx(at(10, 'તરસની'), 'sfx3005', -12)
T(f'tl.fromTo("#{s} .full",{{scale:1.0}},{{scale:1.1,duration:8.6,ease:"none"}},{st(10):.3f});')

# ---------------- S11: bonus - 500 ml before meals, -1.3 kg ----------------
s = scene(st(11) - 0.02, st(12) - 0.02, f'''
  <div class="bonus" id="bn">બોનસ</div>
  <div class="row2">
    <div class="glass"><div class="gfill" id="gf"></div><div class="gl">500 ml</div></div>
    <div class="arrow2" id="a2">➜</div>
    <div class="scalebox" id="sb"><div class="kg"><span id="kg">0.0</span> kg</div><div class="kgl">12 અઠવાડિયામાં<br>વધુ વજન ઘટ્યું</div></div>
  </div>
  <div class="meal" id="ml">દરેક જમણ પહેલાં</div>
  {src('અભ્યાસ: University of Birmingham (UK), 2015 - Obesity જર્નલ')}
''')
popin('#bn', st(11), 0.35, 'scale:1.8', 'power4.out'); sfx(st(11), 'sfx2364', -12)
popin('#ml', at(11, 'જમતાં') - 0.05, 0.3, 'y:20')
T(f'tl.fromTo("#gf",{{height:"0%"}},{{height:"86%",duration:1.0,ease:"power2.out"}},{at(11, "અડધો") - 0.1:.3f});')
sfx(at(11, 'અડધો') - 0.1, 'sfx2826', -18)
popin('#a2', at(11, 'બાર') - 0.1, 0.25, 'x:-30')
popin('#sb', at(11, 'બાર'), 0.35)
T(f'var o3={{v:0}}; tl.to(o3,{{v:1.3,duration:1.0,ease:"power2.out",onUpdate:function(){{document.getElementById("kg").textContent="−"+o3.v.toFixed(1)}}}},{at(11, "સવા") - 0.1:.3f});')
sfx(at(11, 'સવા'), 'sfx3005', -12)

# ---------------- S12: Enagic Kangen - filters, keeps minerals ----------------
s = scene(st(12) - 0.02, st(13) - 0.02, f'''
  <div class="frame"><video class="vid" src="{cut('ionizer', 'ro46', 0.0, 5.5, 860, 1100, speed=0.68)}" muted playsinline data-start="{st(12) - 0.02:.3f}" data-duration="7.9" style="width:100%;height:100%;object-fit:cover"></video></div>
  <div class="kt" id="kt1">પાણી: <span class="cy">ચોખ્ખું + મિનરલ્સવાળું</span></div>
  <div class="jp" id="jp"><svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><circle cx="30" cy="20" r="11" fill="#bc002d"/></svg><span>જાપાન • Enagic Kangen</span></div>
  <div class="kc" id="k1">✓ પાણી ફિલ્ટર કરે</div>
  <div class="kc" id="k2">✓ મિનરલ્સ સાચવે</div>
''')
popin('#kt1', st(12), 0.35, 'y:-30'); sfx(st(12), 'sfx1490', -16)
popin(f'#{s} .frame', st(12) + 0.1, 0.45, 'scale:0.8')
popin('#jp', at(12, 'જાપાનનું') - 0.05, 0.35, 'y:30')
popin('#k1', at(12, 'ફિલ્ટર') - 0.05, 0.3, 'x:-120'); sfx(at(12, 'ફિલ્ટર') - 0.05, 'sfx3005', -14)
popin('#k2', at(12, 'મિનરલ્સ', 1) - 0.05, 0.3, 'x:120'); sfx(at(12, 'મિનરલ્સ', 1) - 0.05, 'sfx3005', -14)

# ---------------- S13: send to elders + follow ----------------
s = scene(st(13) - 0.02, DUR, f'''
  <video class="vid full" src="{cut('elder_cart', 'village39', 16.6, 25.4)}" muted playsinline data-start="{st(13) - 0.02:.3f}" data-duration="{DUR - st(13) + 0.02:.3f}"></video>
  <div class="shade all soft"></div>
  <div class="share" id="sh"><svg viewBox="0 0 100 100"><circle cx="76" cy="22" r="13" fill="#fff"/><circle cx="24" cy="50" r="13" fill="#fff"/><circle cx="76" cy="78" r="13" fill="#fff"/><path d="M26 50 L74 22 M26 50 L74 78" stroke="#fff" stroke-width="7"/></svg><div>ઘરના <span class="yl">વડીલોને</span><br>આ વિડિયો મોકલો</div></div>
  <div class="follow" id="fw">+ ફોલો કરો</div>
  <div class="tag" id="tg">સાચી હેલ્થ ટીપ્સ • ચોટીલા</div>
  <div class="endbrand" id="eb">Enagic Kangen • ચોટીલા</div>
''')
popin('#sh', at(13, 'વડીલોને') - 0.1, 0.4); sfx(at(13, 'વડીલોને') - 0.1, 'sfx1490', -16)
popin('#fw', at(13, 'ફોલો') - 0.1, 0.35, 'scale:1.6', 'power4.out'); sfx(at(13, 'ફોલો') - 0.1, 'sfx3005', -10)
T(f'tl.to("#fw",{{scale:.92,duration:.12,yoyo:true,repeat:1}},{at(13, "ફોલો") + 0.5:.3f});')
popin('#tg', at(13, 'સાચી') - 0.05, 0.3, 'y:30')
popin('#eb', en(13) + 0.1, 0.4, 'y:30')
T(f'tl.fromTo("#{s} .full",{{scale:1.08}},{{scale:1.0,duration:9,ease:"none"}},{st(13):.3f});')

# ---------------- captions (word-by-word) ----------------
def chunks(words):
    out, cur = [], []
    for w in words:
        cur.append(w)
        txt = ' '.join(x[0] for x in cur)
        if len(cur) >= 3 or len(txt) > 17 or w[0][-1] in '.?!:,':
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out
allch = []
for b in B:
    for c in chunks(b['words']): allch.append(c)
for k, c in enumerate(allch):
    t0 = c[0][1] - 0.04
    t1 = (allch[k + 1][0][1] - 0.04) if k + 1 < len(allch) else c[-1][2] + 0.6
    t1 = min(t1, c[-1][2] + 0.7)
    cid = nid('cap')
    spans = ''.join(f'<span class="w" id="{cid}w{j}">{w[0].rstrip(",:")}</span> ' for j, w in enumerate(c))
    els.append(f'<div class="cap" id="{cid}"><div class="cbox">{spans}</div></div>')
    T(f'tl.set("#{cid}",{{autoAlpha:0}},0);tl.fromTo("#{cid} .cbox",{{scale:.86}},{{scale:1,duration:.14,ease:"back.out(3)"}},{t0:.3f});tl.set("#{cid}",{{autoAlpha:1}},{t0:.3f});tl.set("#{cid}",{{autoAlpha:0}},{t1:.3f});')
    for j, w in enumerate(c):
        T(f'tl.set("#{cid}w{j}",{{color:"#FFD84A"}},{w[1]:.3f});tl.set("#{cid}w{j}",{{color:"#ffffff"}},{w[2] + 0.02:.3f});')

# ---------------- page ----------------
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
