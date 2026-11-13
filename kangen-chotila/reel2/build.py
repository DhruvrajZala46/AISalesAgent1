# build.py - Kangen Chotila reel 2: "ટામેટાંથી પથરી?" myth-buster in the Meanwhile Mayank editorial style
import json, os, subprocess
P = os.path.dirname(os.path.abspath(__file__)); os.chdir(P)
B = json.load(open('beats.json')); DUR = 93.57
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
def scene(t0, t1, inner, cls='scene paper', move=True):
    i = nid('s'); first = t0 <= 0.001
    els.append(f'<div id="{i}" class="{cls}"{" style=\"visibility:visible\"" if first else ""}><div class="cam" id="{i}c">{inner}</div></div>')
    if not first: T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});')
    if t1 < DUR: T(f'tl.set("#{i}",{{visibility:"hidden"}},{t1:.3f});')
    if not first: T(f'tl.fromTo("#{i}c",{{y:40}},{{y:0,duration:.22,ease:"power2.out"}},{t0:.3f});')
    if move: T(f'tl.fromTo("#{i}c",{{scale:1.0}},{{scale:1.06,duration:{t1 - t0:.3f},ease:"none",immediateRender:{"true" if first else "false"}}},{t0:.3f});')
    return i
def pop(sel, t, dur=0.35, frm='scale:0.6', ease='back.out(2)'):
    T(f'tl.fromTo("{sel}",{{autoAlpha:0,{frm}}},{{autoAlpha:1,scale:1,x:0,y:0,rotation:0,duration:{dur},ease:"{ease}"}},{t:.3f});')
def stamp(sel, t):
    T(f'tl.fromTo("{sel}",{{autoAlpha:0,scale:2.6,rotation:-25}},{{autoAlpha:1,scale:1,rotation:-8,duration:.25,ease:"power4.in"}},{t:.3f});')
def shake(sel, t, k=7):
    T(f'tl.fromTo("{sel}",{{x:-10}},{{immediateRender:false,x:10,duration:.05,repeat:{k},yoyo:true,ease:"none"}},{t:.3f});tl.set("{sel}",{{x:0}},{t + 0.06 * (k + 1):.3f});')
def src(t): return f'<div class="src"><span>{t}</span></div>'
INK = '#2a1f17'

# ---------------- reusable illustrations ----------------
TOMATO = f'''<svg viewBox="0 0 300 300"><ellipse cx="150" cy="282" rx="105" ry="12" fill="#00000022"/>
<circle cx="150" cy="168" r="112" fill="#d9442f" stroke="{INK}" stroke-width="7"/>
<path d="M95 120 Q120 92 160 98" stroke="#ff9a7a" stroke-width="14" fill="none" stroke-linecap="round" opacity=".8"/>
<path d="M150 62 L126 38 L140 72 L94 66 L132 88 L100 116 L148 96 L156 132 L168 96 L214 116 L178 88 L214 66 L166 72 L176 38 Z" fill="#3f7d3a" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
<path d="M150 62 L150 30" stroke="{INK}" stroke-width="9" stroke-linecap="round"/></svg>'''
SEED = lambda x, y, r=0: f'<ellipse class="seed" cx="{x}" cy="{y}" rx="9" ry="6" transform="rotate({r} {x} {y})" fill="#f3e3a0" stroke="{INK}" stroke-width="2.5"/>'
HALF = f'''<svg viewBox="0 0 300 300"><circle cx="150" cy="150" r="128" fill="#d9442f" stroke="{INK}" stroke-width="7"/>
<circle cx="150" cy="150" r="108" fill="#ef6a4f"/>
<g fill="#f59a7c" stroke="#b8341f" stroke-width="4"><path d="M150 150 L150 52 A98 98 0 0 1 235 199 Z"/><path d="M150 150 L235 199 A98 98 0 0 1 65 199 Z"/><path d="M150 150 L65 199 A98 98 0 0 1 150 52 Z"/></g>
<circle cx="150" cy="150" r="26" fill="#f7b49a" stroke="#b8341f" stroke-width="4"/>
<g id="seeds">{SEED(175,95,30)}{SEED(200,120,60)}{SEED(198,160,100)}{SEED(178,185,140)}{SEED(125,95,-30)}{SEED(100,120,-60)}{SEED(102,160,-100)}{SEED(122,185,-140)}{SEED(150,205,0)}{SEED(140,215,20)}{SEED(160,215,-20)}</g></svg>'''
KIDNEY = lambda extra='', fill='#c4505f': f'''<svg viewBox="0 0 240 280"><path d="M130 14 C64 6 22 66 26 140 C30 214 82 268 142 260 C188 254 192 212 172 190 C152 170 150 148 170 126 C192 102 202 70 186 42 C174 24 154 16 130 14 Z" fill="{fill}" stroke="{INK}" stroke-width="7"/>
<path d="M168 140 C136 140 116 128 106 106 M168 140 C134 146 116 162 110 186 M168 140 C140 140 120 140 92 146" stroke="#f4c7cf" stroke-width="9" fill="none" stroke-linecap="round"/>{extra}</svg>'''
CRYST = '<g class="cry" fill="#f6f1e4" stroke="#2a1f17" stroke-width="3"><path d="M0 -14 L12 -6 L12 8 L0 15 L-12 8 L-12 -6 Z"/><path d="M0 -14 L0 15 M-12 -6 L12 8 M12 -6 L-12 8" stroke-width="1.5" opacity=".6"/></g>'
GLASS = lambda gid: f'''<svg viewBox="0 0 260 360"><path d="M30 20 L230 20 L206 340 L54 340 Z" fill="#dff1f2" fill-opacity=".55" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
<path d="M44 90 L216 90 L206 336 L54 336 Z" fill="#7fc4cc" fill-opacity=".75"/><path d="M60 110 L72 300" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".55"/>
<g id="{gid}"></g></svg>'''
PERSON = lambda cls='p', fill='#7b6a58': f'<svg class="{cls}" viewBox="0 0 60 110"><circle cx="30" cy="20" r="16" fill="{fill}" stroke="{INK}" stroke-width="4"/><path d="M8 108 L8 62 Q8 40 30 40 Q52 40 52 62 L52 108 Z" fill="{fill}" stroke="{INK}" stroke-width="4"/></svg>'

# ---------------- background: paper ----------------
els.append('''<div id="bg" class="bgpaper"></div>
<svg class="grain" width="1080" height="1920"><filter id="nz"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" seed="4"/><feColorMatrix values="0 0 0 0 .16  0 0 0 0 .12  0 0 0 0 .08  0 0 0 .55 0"/></filter><rect width="1080" height="1920" filter="url(#nz)"/></svg>
<div class="vign"></div>''')

# S1 - "ટામેટાં ખાવાથી પથરી થાય?" (0.25-5.9)
s = scene(0.0, st(2) - 0.05, f'''
  <div class="kick" id="k1">MYTH?</div>
  <div class="h1" id="h1">ટામેટાં ખાવાથી<br><span class="rd">પથરી?</span></div>
  <div class="tom" id="tm">{TOMATO}</div>
  <div class="half" id="hf">{HALF}</div>
  <div class="note" id="nt">બીજ કાઢી નાખો છો?</div>
''')
pop('#k1', 0.2, 0.3, 'y:-30'); pop('#h1', 0.3, 0.4, 'scale:1.4', 'power4.out'); pop('#tm', 0.5, 0.5, 'y:300', 'back.out(1.6)')
T(f'tl.to("#tm",{{x:-210,rotation:-12,duration:.5,ease:"power2.inOut"}},{at(1, "એટલે") - 0.2:.3f});')
pop('#hf', at(1, 'ટામેટાનાં') - 0.1, 0.45, 'x:300', 'back.out(1.8)')
import random as _r; _r.seed(7)
for _k in range(11):
    T(f'tl.to("#seeds .seed:nth-child({_k + 1})",{{y:{_r.randint(160, 320)},x:{_r.randint(-120, 120)},rotation:{_r.randint(-180, 180)},opacity:0,duration:.8,ease:"power2.in"}},{at(1, "કાઢી") - 0.05 + _k * 0.03:.3f});')
pop('#nt', at(1, 'બીજ') - 0.05, 0.3, 'y:30')
sfx(0.2, 'sfx1490', -15); sfx(0.5, 'sfx3005', -14); sfx(at(1, 'ટામેટાનાં') - 0.1, 'sfx1490', -17); sfx(at(1, 'કાઢી'), 'sfx1317', -12)

# S2 - "બીજ ક્યારેય પથરી બનતાં જ નથી" + stamp ગેરસમજ (6.2-12.2)
s = scene(st(2) - 0.05, st(3) - 0.05, f'''
  <div class="kick" id="k2">FACT</div>
  <div class="h1" id="h2">બીજ ક્યારેય<br><span class="rd">પથરી નથી બનતાં</span></div>
  <div class="half big" id="hf2">{HALF.replace('id="seeds"', 'id="seeds2"')}</div>
  <div class="stamp" id="sp">ગેરસમજ</div>
''')
pop('#k2', st(2), 0.3, 'y:-30'); pop('#h2', at(2, 'બીજ') - 0.1, 0.4, 'scale:1.4', 'power4.out'); pop('#hf2', st(2) + 0.1, 0.45, 'scale:0.5')
stamp('#sp', at(2, 'ગેરસમજ') - 0.1); shake('#' + s + 'c', at(2, 'ગેરસમજ') + 0.15, 5)
sfx(st(2), 'sfx1490', -16); sfx(at(2, 'ગેરસમજ') + 0.1, 'sfx2364', -9)

# S3 - kidney crystal "મીઠાના દાણા જેવો" (12.7-20.3)
BODYF = f'''<svg viewBox="0 0 420 760"><g fill="#e2cfa8" stroke="{INK}" stroke-width="6" stroke-linejoin="round">
<circle cx="210" cy="78" r="60"/><path d="M118 160 Q210 128 302 160 L326 360 Q330 440 298 470 L282 740 L232 740 L218 500 L202 500 L188 740 L138 740 L122 470 Q90 440 94 360 Z"/>
<path d="M116 168 L64 400 L90 410 L140 236"/><path d="M304 168 L356 400 L330 410 L280 236"/></g>
<g id="kids"><path d="M168 300 C150 300 140 316 142 334 C144 352 160 362 174 356 C184 352 182 340 176 334 C172 328 176 320 180 314 C184 306 178 300 168 300Z" fill="#c4505f" stroke="{INK}" stroke-width="4"/>
<path d="M252 300 C270 300 280 316 278 334 C276 352 260 362 246 356 C236 352 238 340 244 334 C248 328 244 320 240 314 C236 306 242 300 252 300Z" fill="#c4505f" stroke="{INK}" stroke-width="4"/></g>
<path id="ure" d="M176 344 C190 380 196 420 204 452 M244 344 C230 380 224 420 216 452" stroke="#c4505f" stroke-width="6" fill="none"/>
<ellipse cx="210" cy="460" rx="22" ry="16" fill="#d8a0a8" stroke="{INK}" stroke-width="4"/></svg>'''
s = scene(st(3) - 0.05, st(4) - 0.05, f'''
  <div class="kick" id="k3">STONE = CRYSTAL</div>
  <div class="h1 sm" id="h3">પથરી ખાધેલી વસ્તુ નથી</div>
  <div class="bodyf" id="bf">{BODYF}</div>
  <div class="lens" id="ln"><div class="lensin">{KIDNEY(''.join(f'<g transform="translate({x},{y}) scale({k})">{CRYST}</g>' for x, y, k in [(90,120,1.3),(70,170,1.0),(118,206,1.1)]))}</div></div>
  <div class="tagp" id="tp">કિડનીની અંદર બનતો <b class="rd">ક્રિસ્ટલ</b></div>
  <div class="salt" id="sl"><svg viewBox="0 0 120 120"><g transform="translate(60 60) scale(3)">{CRYST}</g></svg><span>મીઠાના દાણા જેવો</span></div>
''')
pop('#k3', st(3), 0.3, 'y:-30'); pop('#h3', at(3, 'પથરી') - 0.1, 0.35, 'y:-20'); pop('#bf', st(3) + 0.1, 0.45, 'y:200', 'back.out(1.4)')
T(f'tl.fromTo("#kids path",{{scale:1,transformOrigin:"50% 50%"}},{{scale:1.25,duration:.3,repeat:3,yoyo:true}},{at(3, "કિડનીની") - 0.05:.3f});')
T(f'tl.to("#bf",{{x:-230,scale:.8,duration:.5,ease:"power2.inOut"}},{at(3, "કિડનીની") + 0.2:.3f});')
pop('#ln', at(3, 'ક્રિસ્ટલ') - 0.35, 0.45, 'scale:0.2', 'back.out(1.8)'); pop('#tp', at(3, 'ક્રિસ્ટલ') - 0.1, 0.3, 'y:30')
pop('#sl', at(3, 'મીઠાના') - 0.05, 0.35, 'scale:0.4', 'back.out(2.5)')
sfx(st(3), 'sfx1490', -16); sfx(at(3, 'ક્રિસ્ટલ') - 0.35, 'sfx1317', -11); sfx(at(3, 'મીઠાના'), 'sfx3005', -13)

# S4 - sugar in water: dissolves, then settles (20.6-27.2)
s = scene(st(4) - 0.05, st(5) - 0.05, f'''
  <div class="kick" id="k4">SIMPLE TEST</div>
  <div class="h1 sm" id="h4">પાણીમાં <span class="rd">ખાંડ</span> નાખતા જાઓ…</div>
  <div class="glass" id="gl">{GLASS('sug')}</div>
  <div class="spoon" id="spn"><svg viewBox="0 0 220 80"><ellipse cx="50" cy="40" rx="44" ry="26" fill="#cfd6db" stroke="{INK}" stroke-width="5"/><ellipse cx="50" cy="36" rx="30" ry="14" fill="#fff"/><path d="M94 40 L214 30" stroke="{INK}" stroke-width="12" stroke-linecap="round"/><path d="M94 40 L214 30" stroke="#cfd6db" stroke-width="6" stroke-linecap="round"/></svg></div>
  <div class="grains" id="gr">{''.join(f'<i style="left:{l}px;top:{t}px"></i>' for l, t in [(0,0),(14,6),(28,0),(8,14),(22,14),(36,8),(4,26),(30,24)])}</div>
  <div class="heap" id="hp"></div>
  <div class="lab ok" id="o1">✓ ઓગળી ગઈ</div><div class="lab bad" id="o2">✗ ઓગળે જ નહીં — તળિયે!</div>
''')
pop('#k4', st(4), 0.3, 'y:-30'); pop('#h4', st(4) + 0.05, 0.35, 'y:-20'); pop('#gl', st(4) + 0.1, 0.4, 'y:200', 'back.out(1.4)')
for j, t in enumerate([at(4, 'ખાંડ') - 0.1, at(4, 'નાખતા'), at(4, 'જાઓ') - 0.05]):
    T(f'tl.fromTo("#spn",{{rotation:0}},{{rotation:-35,duration:.25,yoyo:true,repeat:1,ease:"power1.inOut",immediateRender:{"true" if j == 0 else "false"}}},{t:.3f});')
    T(f'tl.fromTo("#gr",{{autoAlpha:1,y:0}},{{y:330,autoAlpha:0,duration:.4,ease:"power1.in",immediateRender:{"true" if j == 0 else "false"}}},{t + 0.12:.3f});')
    sfx(t + 0.15, 'sfx3005', -19)
T(f'tl.set("#spn",{{autoAlpha:0}},0);tl.set("#spn",{{autoAlpha:1}},{st(4):.3f});')
pop('#o1', at(4, 'જાઓ') + 0.4, 0.3, 'y:20')
T(f'tl.to("#o1",{{autoAlpha:0,duration:.2}},{at(4, "ખાંડ", 1) - 0.3:.3f});')
T(f'tl.fromTo("#spn",{{rotation:0}},{{rotation:-40,duration:.25,yoyo:true,repeat:3,immediateRender:false}},{at(4, "ખાંડ", 1) - 0.2:.3f});')
T(f'tl.fromTo("#hp",{{autoAlpha:0,scaleY:0,transformOrigin:"50% 100%"}},{{autoAlpha:1,scaleY:1,duration:1.4,ease:"power1.out"}},{at(4, "ઓગળે") - 0.2:.3f});')
pop('#o2', at(4, 'તળિયે') - 0.1, 0.35, 'scale:1.4', 'power4.out')
sfx(at(4, 'તળિયે') - 0.1, 'sfx2364', -13)

# S5 - same in the kidney: low water -> salts can't dissolve -> stone (27.5-36.1)
s = scene(st(5) - 0.05, st(6) - 0.05, f'''
  <div class="kick" id="k5">INSIDE YOUR KIDNEY</div>
  <div class="h1 sm" id="h5">કિડનીમાં પણ <span class="rd">આવું જ</span></div>
  <div class="kbig" id="kb">{KIDNEY(''.join(f'<g class="cg" transform="translate({x},{y}) scale(.8)">{CRYST}</g>' for x, y in [(70,90),(110,70),(60,150),(100,130),(80,200),(120,190),(56,110),(96,170)]) + '<path id="stone" d="M74 128 l22 -14 l26 6 l10 22 l-8 24 l-26 10 l-22 -10 l-8 -20 z" fill="#d9cdb6" stroke="#2a1f17" stroke-width="5"/>', '#c4505f')}</div>
  <div class="gauge" id="ga"><div class="gfill" id="gf"></div><span>પાણી</span></div>
  <div class="steps"><div class="stp" id="q1">પાણી ઓછું</div><div class="arr" id="q2">➜</div><div class="stp" id="q3">ક્ષાર ભેગા</div><div class="arr" id="q4">➜</div><div class="stp red" id="q5">પથ્થર</div></div>
''')
pop('#k5', st(5), 0.3, 'y:-30'); pop('#h5', st(5) + 0.05, 0.35, 'y:-20'); pop('#kb', st(5) + 0.1, 0.45, 'scale:0.4', 'back.out(1.6)'); pop('#ga', st(5) + 0.3, 0.3, 'x:120')
T(f'tl.set("#stone",{{autoAlpha:0}},0);tl.set("#kb .cg",{{autoAlpha:0}},0);')
T(f'tl.fromTo("#gf",{{height:"85%"}},{{height:"18%",duration:1.2,ease:"power2.inOut"}},{at(5, "પાણી") - 0.1:.3f});')
pop('#q1', at(5, 'પાણી') - 0.05, 0.3, 'y:20')
T(f'tl.fromTo("#kb .cg",{{autoAlpha:0,scale:0}},{{autoAlpha:1,scale:.8,duration:.25,stagger:.08,ease:"back.out(3)"}},{at(5, "ક્ષાર") - 0.1:.3f});')
pop('#q2', at(5, 'ક્ષાર') - 0.2, 0.2, 'x:-20'); pop('#q3', at(5, 'ક્ષાર') - 0.05, 0.3, 'y:20')
T(f'tl.to("#kb .cg",{{x:96,y:140,scale:.3,duration:.8,ease:"power2.in",stagger:.04}},{at(5, "ભેગા") - 0.1:.3f});')
T(f'tl.fromTo("#stone",{{autoAlpha:0,scale:.2,transformOrigin:"100px 140px"}},{{autoAlpha:1,scale:1.2,duration:.35,ease:"back.out(3)"}},{at(5, "પથ્થર") - 0.15:.3f});')
pop('#q4', at(5, 'પથ્થર') - 0.3, 0.2, 'x:-20'); pop('#q5', at(5, 'પથ્થર') - 0.1, 0.35, 'scale:1.6', 'power4.out')
sfx(at(5, 'ક્ષાર'), 'sfx3005', -15); sfx(at(5, 'પથ્થર') - 0.15, 'sfx2364', -11)

# S6 - "ખતરો ટામેટામાં નહીં, ઓછા પાણીમાં" (36.4-39.8)
s = scene(st(6) - 0.05, st(7) - 0.05, f'''
  <div class="kick" id="k6">SO THE REAL DANGER?</div>
  <div class="vs">
    <div class="vsc" id="v1"><div class="mini">{TOMATO}</div><div class="vl gr">✓ ટામેટાં</div></div>
    <div class="vsc" id="v2"><div class="mini">{GLASS('g6').replace('fill-opacity=".75"', 'fill-opacity=".75" transform="translate(0 200) scale(1 .3)"')}</div><div class="vl rd">✗ ઓછું પાણી</div></div>
  </div>
  <div class="h1 low" id="h6">ખતરો <span class="rd">ઓછા પાણીમાં</span> છે</div>
''', cls='scene dark')
pop('#k6', st(6), 0.3, 'y:-30'); pop('#v1', at(6, 'ટામેટામાં') - 0.1, 0.35, 'x:-200'); pop('#v2', at(6, 'ઓછા') - 0.1, 0.35, 'x:200')
pop('#h6', at(6, 'ઓછા') + 0.1, 0.35, 'scale:1.4', 'power4.out')
sfx(st(6), 'sfx1490', -16); sfx(at(6, 'ઓછા') - 0.1, 'sfx2364', -12)

# S7 - the stone travels down a tube a few mm wide; sand-grain stone, top-level pain (40.2-53.6)
s = scene(st(7) - 0.05, st(8) - 0.05, f'''
  <div class="kick" id="k7">THE JOURNEY</div>
  <div class="bodyf2" id="b7">{BODYF.replace('id="kids"', 'id="kids7"').replace('id="ure"', 'id="ure7"')}</div>
  <div class="mover" id="mv"><svg viewBox="0 0 40 40"><path d="M8 18 l10 -8 l12 4 l4 12 l-8 10 l-12 0 l-6 -8z" fill="#d9cdb6" stroke="#2a1f17" stroke-width="4"/></svg></div>
  <div class="tube" id="tb"><div class="tubein"></div><div class="mm"><b>થોડા mm</b></div></div>
  <div class="sand" id="sd"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="10" fill="#d9cdb6" stroke="#2a1f17" stroke-width="4"/></svg><span>રેતીના દાણા જેવડી</span></div>
  <div class="pain" id="pn"><svg viewBox="0 0 200 200"><g fill="#c0392b" stroke="#2a1f17" stroke-width="4"><path d="M100 10 L118 70 L180 60 L130 100 L170 150 L110 125 L100 190 L88 125 L28 150 L70 100 L20 60 L82 70 Z"/></g></svg></div>
  <div class="h1 low" id="h7">સૌથી <span class="rd">તીવ્ર દુખાવામાં</span> ગણાય</div>
''')
pop('#k7', st(7), 0.3, 'y:-30'); pop('#b7', st(7) + 0.05, 0.4, 'y:200', 'back.out(1.4)')
T(f'tl.fromTo("#mv",{{autoAlpha:0,x:0,y:0}},{{autoAlpha:1,duration:.2}},{at(7, "પથ્થર") - 0.1:.3f});')
T(f'tl.to("#mv",{{x:28,y:150,duration:1.6,ease:"power1.inOut"}},{at(7, "નીચે") - 0.1:.3f});')
T(f'tl.to("#b7",{{x:-220,duration:.5,ease:"power2.inOut"}},{at(7, "નીચે") + 1.55:.3f});tl.to("#mv",{{x:-192,duration:.5,ease:"power2.inOut"}},{at(7, "નીચે") + 1.55:.3f});')
pop('#tb', at(7, 'નળી') - 0.1, 0.45, 'scale:0.3', 'back.out(1.6)')
T(f'tl.to("#b7,#mv,#tb",{{autoAlpha:.15,duration:.3}},{at(7, "રેતીના") - 0.2:.3f});')
pop('#sd', at(7, 'રેતીના') - 0.05, 0.4, 'scale:0.2', 'back.out(2.5)')
T(f'tl.to("#sd",{{autoAlpha:0,duration:.2}},{at(7, "દુખાવો") - 0.2:.3f});')
pop('#pn', at(7, 'દુખાવો') - 0.1, 0.3, 'scale:0.1', 'power4.out')
T(f'tl.to("#pn",{{scale:1.25,duration:.12,yoyo:true,repeat:9,ease:"none"}},{at(7, "દુખાવો") + 0.25:.3f});')
shake('#' + s + 'c', at(7, 'દુખાવો'), 9)
T(f'tl.fromTo("#{s}",{{backgroundColor:"rgba(192,57,43,0)"}},{{backgroundColor:"rgba(192,57,43,.35)",duration:.15,yoyo:true,repeat:3}},{at(7, "દુખાવો"):.3f});')
pop('#h7', at(7, 'સૌથી') - 0.1, 0.35, 'y:30')
sfx(st(7), 'sfx1490', -16); sfx(at(7, 'નળી') - 0.1, 'sfx3005', -14); sfx(at(7, 'રેતીના'), 'sfx1317', -12); sfx(at(7, 'દુખાવો') - 0.1, 'sfx2364', -8)

# S8 - India stone belt map, Gujarat red (54.0-61.1)
MAP = open('assets/india.svgfrag').read()
s = scene(st(8) - 0.05, st(9) - 0.05, f'''
  <div class="kick" id="k8">THE STONE BELT</div>
  <div class="h1 sm" id="h8">ભારતનો <span class="rd">"સ્ટોન બેલ્ટ"</span></div>
  <div class="map" id="mp">{MAP}</div>
  <div class="mtag" id="mt">ગુજરાત</div>
  <div class="c3"><div class="ch" id="ch1">☀ ગરમી</div><div class="ch" id="ch2">પરસેવો</div><div class="ch red" id="ch3">ઓછું પાણી</div></div>
  {src('સ્રોત: Foods (MDPI) રિવ્યુ, 2019 • નકશો: Wikimedia Commons')}
''')
pop('#k8', st(8), 0.3, 'y:-30'); pop('#mp', st(8) + 0.05, 0.5, 'scale:0.7', 'power3.out')
T(f'tl.fromTo("#mp .belt",{{fill:"#d8ccb4"}},{{fill:"#d9a441",duration:.4,stagger:.06}},{at(8, "ભારતના") :.3f});')
T(f'tl.fromTo("#mp .gj",{{fill:"#d8ccb4"}},{{fill:"#c0392b",duration:.3}},{at(8, "ગુજરાત") - 0.1:.3f});')
T(f'tl.to("#mp .gj",{{opacity:.55,duration:.3,yoyo:true,repeat:9}},{at(8, "ગુજરાત") + 0.4:.3f});')
pop('#mt', at(8, 'ગુજરાત') - 0.05, 0.4, 'scale:1.8', 'power4.out'); pop('#h8', at(8, 'સ્ટોન') - 0.2, 0.35, 'y:-20')
pop('#ch1', at(8, 'ગરમી') - 0.05, 0.3, 'y:30'); pop('#ch2', at(8, 'પરસેવો') - 0.05, 0.3, 'y:30'); pop('#ch3', at(8, 'ઓછું') - 0.05, 0.35, 'scale:1.5', 'power4.out')
sfx(st(8), 'sfx1490', -16); sfx(at(8, 'ગુજરાત') - 0.05, 'sfx2364', -11); sfx(at(8, 'ઓછું'), 'sfx3005', -13)

# S9 - "સૌથી અજીબ વાત": about half get it again (61.5-68.2)
ppl = ''.join(f'<div class="pp" id="pp{k}">{PERSON()}</div>' for k in range(10))
s = scene(st(9) - 0.05, st(10) - 0.05, f'''
  <div class="kick" id="k9">THE STRANGEST PART</div>
  <div class="h1 sm" id="h9">સૌથી <span class="rd">અજીબ</span> વાત</div>
  <div class="ppl">{ppl}</div>
  <div class="half2" id="hh">લગભગ <span class="rd">અડધા</span> લોકોને</div>
  <div class="again" id="ag"><svg viewBox="0 0 100 100"><path d="M80 50 A30 30 0 1 1 64 23" stroke="#c0392b" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M56 8 L70 24 L50 32 Z" fill="#c0392b"/></svg><span>ફરી થાય છે</span></div>
  {src('સ્રોત: NIDDK-funded study (Duke Health) • પથરી ફરી થવાનો દર')}
''', cls='scene dark')
pop('#k9', st(9), 0.3, 'y:-30'); pop('#h9', st(9) + 0.05, 0.4, 'scale:1.5', 'power4.out')
T(f'tl.fromTo(".pp",{{autoAlpha:0,y:60}},{{autoAlpha:1,y:0,duration:.25,stagger:.06,ease:"back.out(2)"}},{at(9, "જેને") - 0.1:.3f});')
T(f'tl.to(["#pp0 svg *","#pp2 svg *","#pp4 svg *","#pp6 svg *","#pp8 svg *"],{{fill:"#c0392b",duration:.25,stagger:.05}},{at(9, "અડધા") - 0.1:.3f});')
pop('#hh', at(9, 'લગભગ') - 0.05, 0.35, 'y:30'); pop('#ag', at(9, 'ફરી') - 0.1, 0.4, 'scale:0.3', 'back.out(2.5)')
T(f'tl.fromTo("#ag svg",{{rotation:0}},{{rotation:360,duration:1.2,ease:"power2.inOut"}},{at(9, "ફરી"):.3f});')
sfx(st(9), 'sfx2364', -12); sfx(at(9, 'અડધા') - 0.1, 'sfx3005', -12); sfx(at(9, 'ફરી') - 0.1, 'sfx1490', -16)

# S10 - NIH: biggest protection = enough water (68.6-74.8)
s = scene(st(10) - 0.05, st(11) - 0.05, f'''
  <div class="kick" id="k10">NIH, USA</div>
  <div class="doc" id="dc"><div class="dh">NIH</div><div class="ds">National Institutes of Health • NIDDK</div><div class="dl"></div><div class="dl s"></div><div class="dq">"…the most important thing you can do to prevent kidney stones"</div><div class="dl"></div><div class="dl s"></div></div>
  <div class="stamp blue" id="sp2">પૂરતું પાણી</div>
  <div class="h1 low" id="h10">પથરીથી બચવાનો<br><span class="rd">સૌથી મોટો ઉપાય</span></div>
''')
pop('#k10', st(10), 0.3, 'y:-30'); pop('#dc', st(10) + 0.1, 0.45, 'y:300', 'back.out(1.3)'); pop('#h10', at(10, 'પથરીથી') - 0.1, 0.35, 'y:30')
stamp('#sp2', at(10, 'પૂરતું') - 0.12); shake('#dc', at(10, 'પૂરતું') + 0.15, 3)
sfx(st(10), 'sfx1490', -16); sfx(at(10, 'પૂરતું') + 0.1, 'sfx2364', -9)

# S11 - callback: eat tomatoes in peace (75.2-80.8)
s = scene(st(11) - 0.05, st(12) - 0.05, f'''
  <div class="tom c" id="t11">{TOMATO}</div>
  <div class="okb" id="ok">✓</div>
  <div class="h1 sm" id="h11">ટામેટાં <span class="gr">નિરાંતે ખાજો</span></div>
  <div class="h1 low" id="h11b">ડર ટામેટાથી નહીં,<br><span class="rd">ઓછા પાણીથી</span></div>
''')
pop('#t11', st(11), 0.45, 'scale:0.3', 'back.out(2)'); pop('#h11', at(11, 'ટામેટાં') - 0.05, 0.35, 'y:-20'); pop('#ok', at(11, 'નિરાંતે') - 0.05, 0.35, 'scale:3', 'power4.out')
pop('#h11b', at(11, 'ડર') - 0.1, 0.4, 'scale:1.4', 'power4.out')
sfx(st(11), 'sfx1490', -16); sfx(at(11, 'નિરાંતે'), 'sfx3005', -11); sfx(at(11, 'ડર') - 0.1, 'sfx2364', -13)

# S12 - free demo: Enagic Kangen, call Hardevsinh (81.2-87.4)
PHONE = '<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="#2e8b57" stroke="#2a1f17" stroke-width="4"/><path d="M34 26c4-2 8 6 9 10s-4 6-3 9c2 6 7 11 13 13c3 1 5-4 9-3s12 5 10 9c-2 6-8 10-14 9C40 71 27 58 25 40c-1-6 3-12 9-14z" fill="#fff"/></svg>'
s = scene(st(12) - 0.05, st(13) - 0.05, f'''
  <div class="kick" id="k12">FREE DEMO • CHOTILA</div>
  <div class="polaroid" id="pl"><video id="vk" class="vid" src="{cut('k8_pour2', 'phtest3', 0.6, 6.6, 760, 760)}" muted playsinline data-start="{st(12) - 0.05:.3f}" data-duration="{st(13) - st(12) + 0.1:.3f}" style="width:760px;height:760px;object-fit:cover"></video><div class="pcap">Enagic Kangen</div></div>
  <div class="stamp green" id="sp3">ફ્રી ડેમો</div>
  <div class="callbar" id="cb">{PHONE}<div><b>હરદેવસિંહ</b><span>Enagic Kangen • ચોટીલા</span></div></div>
''')
pop('#k12', st(12), 0.3, 'y:-30'); pop('#pl', st(12) + 0.05, 0.5, 'rotation:-12', 'back.out(1.6)')
T(f'tl.set("#pl",{{rotation:-3}},{st(12) + 0.56:.3f});')
stamp('#sp3', at(12, 'ફ્રી') - 0.1)
pop('#cb', at(12, 'હરદેવસિંહને') - 0.15, 0.4, 'y:120', 'back.out(1.8)')
T(f'tl.fromTo("#cb svg",{{rotation:-12}},{{rotation:12,duration:.07,repeat:11,yoyo:true}},{at(12, "ફોન"):.3f});')
sfx(st(12), 'sfx1490', -16); sfx(at(12, 'ફ્રી') + 0.1, 'sfx2364', -10); sfx(at(12, 'હરદેવસિંહને') - 0.1, 'sfx3005', -10)

# S13 - share with every family member + end (87.7-end)
fam = ''.join(f'<div class="fm" id="fm{k}">{PERSON("p", c)}</div>' for k, c in enumerate(['#7b6a58', '#a0522d', '#5f7f6f', '#8a6d9e', '#b07d48']))
s = scene(st(13) - 0.05, DUR, f'''
  <div class="family">{fam}</div>
  <div class="h1" id="h13">ઘરના <span class="rd">દરેક સભ્ય</span><br>સુધી પહોંચાડો</div>
  <div class="endcard" id="ec"><b>હરદેવસિંહ</b><span>Enagic Kangen Water • ચોટીલા</span></div>
''', cls='scene paper', move=False)
T(f'tl.fromTo(".fm",{{autoAlpha:0,y:80}},{{autoAlpha:1,y:0,duration:.3,stagger:.1,ease:"back.out(2)"}},{st(13) + 0.1:.3f});')
pop('#h13', at(13, 'ઘરના') - 0.05, 0.4, 'scale:1.3', 'power4.out'); pop('#ec', en(13) - 0.3, 0.45, 'y:80', 'back.out(1.6)')
sfx(st(13), 'sfx1490', -16); sfx(en(13) - 0.3, 'sfx1317', -11)

# ---------------- captions ----------------
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
    T(f'tl.set("#{cid}",{{autoAlpha:0}},0);tl.set("#{cid}",{{autoAlpha:1}},{t0:.3f});tl.set("#{cid}",{{autoAlpha:0}},{t1:.3f});')
    for j, w in enumerate(c):
        T(f'tl.set("#{cid}w{j}",{{color:"#c0392b"}},{w[1]:.3f});tl.set("#{cid}w{j}",{{color:"#2a1f17"}},{w[2] + 0.02:.3f});')

css = open('style.css').read()
html = f'''<!doctype html>
<html lang="gu"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>Kangen reel 2</title><script src="gsap.min.js"></script><style>{css}</style></head>
<body><div id="root" data-composition-id="main" data-start="0" data-width="{W}" data-height="{H}" data-duration="{DUR}">
{chr(10).join(els)}
<audio id="mix" src="assets/mix.wav" data-start="0" data-duration="{DUR}"></audio>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tw)}
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl;
</script></body></html>'''
open('index.html', 'w').write(html)
json.dump(SFX, open('sfx.json', 'w'))
print('ok', len(els), 'elements', len(tw), 'tweens', len(SFX), 'sfx')
