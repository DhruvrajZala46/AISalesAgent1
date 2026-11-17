# build.py - Kangen reel 7 (Gujarati): the owner's reference reel ("celebrities choose Kangen"), same order and style,
# re-voiced in Gujarati. Celebrity proof clips come from the reference (its Hindi captions blurred, see README);
# the Akshay segment is swapped for a Kangen pour (the voice never names him).
import json, os, subprocess
P = os.path.dirname(os.path.abspath(__file__)); os.chdir(P)
B = json.load(open('beats.json')); VEND = B[-1]['end']; DUR = round(VEND + 3.2, 2)
W, H = 1080, 1920
def sh(c): subprocess.run(c, shell=True, check=True)
def at(i, word, k=0):
    hits = [w for w in B[i - 1]['words'] if word in w[0]]; assert len(hits) > k, (i, word); return hits[k][1]
st = lambda i: B[i - 1]['start'] - 0.05
def dur(src): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'raw/{src}.mp4'], capture_output=True, text=True).stdout)
def cut(name, src, a, need, w=W, h=H, crop=None):
    out = f'assets/{name}.mp4'
    if not os.path.exists(out):
        avail = max(0.5, dur(src) - a); speed = 1.0
        if avail < need + 0.1: speed = max(0.4, avail / (need + 0.1))
        take = min(avail, (need + 0.1) * speed)
        pre = f"crop=iw*{crop[2]}:ih*{crop[3]}:iw*{crop[0]}:ih*{crop[1]}," if crop else ""
        sh(f'ffmpeg -y -v error -ss {a} -t {take:.3f} -i raw/{src}.mp4 -an -vf "{pre}setpts=PTS/{speed},scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},fps=30" -c:v libx264 -crf 19 -preset veryfast -g 30 -keyint_min 30 -pix_fmt yuv420p -movflags +faststart {out}')
    return out
els, tw, SFX, CUTS = [], [], [], []
def T(s): tw.append(s)
n = [0]
def nid(p='e'): n[0] += 1; return f'{p}{n[0]}'
def sfx(t, f, g=-14): SFX.append((round(t, 3), f, g))
def vis(i, t0, t1=None):
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});')
    if t1 is not None and t1 < DUR: T(f'tl.set("#{i}",{{visibility:"hidden"}},{t1:.3f});')
def key(*a): return '_'.join(str(x) for x in a).replace('.', 'p').replace(' ', '').replace(',', '-').replace('(', '').replace(')', '')
def shot(src, a, t0, t1, crop=None, zoom=(1.0, 1.06), inner=''):
    i = nid('sh'); f = cut(key(src, a, int(t0 * 10), crop), src, a, t1 - t0, crop=crop)
    els.append(f'<div class="shot" id="{i}"><div class="zw" id="{i}z"><video id="{i}v" src="{f}" muted playsinline data-start="{t0:.3f}" data-duration="{t1 - t0 + 0.05:.3f}"></video>{inner}</div></div>')
    vis(i, t0, t1); T(f'tl.fromTo("#{i}z",{{scale:{zoom[0]}}},{{scale:{zoom[1]},duration:{t1 - t0:.3f},ease:"none"}},{t0:.3f});')
    if t0 > 0.1: CUTS.append(t0)
    return i
def el(html, t0, t1, frm='autoAlpha:0,scale:0.6', ease='back.out(2)', d=0.3, s=None, g=-16):
    i = nid('x'); els.append(html.replace('ID', i)); vis(i, t0, t1)
    T(f'tl.fromTo("#{i}",{{{frm}}},{{autoAlpha:1,scale:1,x:0,y:0,duration:{d},ease:"{ease}"}},{t0:.3f});')
    if s: sfx(t0, s, g)
    return i

# ===== L1 hook: beige board, b/w celebrity circle swapping every ~0.45 s, then "a special kind of water" =====
t_k = at(1, 'એક') - 0.08
els.append('<div class="shot" id="hook"><div class="beige"></div></div>'); vis('hook', 0, t_k)
CEL = ['tiger', 'ronaldo', 'virat', 'karan', 'tiger', 'virat', 'ronaldo', 'karan', 'virat', 'tiger']
step = 0.45; k = 0; t = 0.0
while t < t_k - 0.05:
    i = nid('ce'); t2 = min(t + step, t_k)
    els.append(f'<img class="celeb" id="{i}" src="assets/circ_{CEL[k % len(CEL)]}.png" style="left:180px;top:420px;width:720px;height:720px">')
    vis(i, t, t2); T(f'tl.fromTo("#{i}",{{scale:.94}},{{scale:1,duration:.2,ease:"power2.out"}},{t:.3f});')
    if k: sfx(t, 'sfx3005', -22)
    k += 1; t = t2
sfx(0.02, 'sfx1143', -15)
shot('r_balcony', 0.0, t_k, st(2))
# ===== L2 celebrity proof =====
shot('r_saina', 0.0, st(2), at(2, 'એક્ટર') - 0.08, zoom=(1.0, 1.04))
shot('r_sonu', 0.0, at(2, 'એક્ટર') - 0.08, at(2, 'લેજેન્ડ') - 0.08, zoom=(1.0, 1.05))
shot('r_merchant', 0.0, at(2, 'લેજેન્ડ') - 0.08, at(2, 'અને') - 0.08, zoom=(1.0, 1.05))
shot('r_jacq', 0.0, at(2, 'અને') - 0.08, st(3), zoom=(1.0, 1.05))
# ===== L3 Kangen in their lifestyle (Kangen pour instead of the reference's Akshay clip) =====
shot('kangenk85', 3.0, st(3), st(4), zoom=(1.0, 1.1))
# ===== L4 not just filtered water =====
shot('r_tap', 0.0, st(4), st(5))
# ===== L5 alkaline pH / antioxidants / hydration =====
t_p = at(5, 'પાવરફુલ') - 0.08
shot('bubbles35', 0.3, st(5), t_p, zoom=(1.0, 1.15))
shot('r_drinkw', 0.0, t_p, st(6), zoom=(1.0, 1.06))
# ===== L6 curiosity =====
shot('r_smile', 0.0, st(6), st(7), zoom=(1.0, 1.05))
# ===== L7 WhatsApp DEMO =====
shot('r_phone', 0.0, st(7), st(8), zoom=(1.0, 1.06))
el('<div class="wa" id="ID"><div class="h">WhatsApp</div><div class="t">DEMO</div><div class="m">✓✓</div></div>', at(7, 'DEMO') - 0.05, st(8), 'autoAlpha:0,y:120,scale:.6', d=.35, s='sfx1311', g=-14)
# ===== L8 free water test + live demo at home =====
shot('r_machine', 0.0, st(8), VEND + 0.25, zoom=(1.0, 1.06))
el('<div class="chip g" id="ID" style="left:80px;top:300px">ફ્રી વોટર ટેસ્ટ</div>', at(8, 'ફ્રી') - 0.05, VEND + 0.25, 'autoAlpha:0,x:-160', s='sfx3005', g=-15)
el('<div class="chip y" id="ID" style="right:80px;top:440px">લાઇવ ડેમો</div>', at(8, 'લાઇવ') - 0.05, VEND + 0.25, 'autoAlpha:0,x:160', s='sfx3005', g=-15)
# ===== end card, like the reference: pill on top, Enagic distributor logo, the action =====
e = el('<div class="end" id="ID"><div class="pill">DEMO લખી મેસેજ કરો</div><img class="logo" src="assets/enagic_logo.png"><div class="l2">ફ્રી ઘરે ડેમો</div><div class="l3">Enagic Kangen • ચોટીલા</div></div>', VEND + 0.25, DUR, 'autoAlpha:0', 'power2.out', d=.3, s='sfx1143', g=-12)
T(f'tl.fromTo("#{e} .pill",{{scale:.5,autoAlpha:0}},{{scale:1,autoAlpha:1,duration:.4,ease:"back.out(2.4)",immediateRender:false}},{VEND + 0.3:.3f});')
T(f'tl.fromTo("#{e} .logo",{{scale:.6,rotation:-30}},{{scale:1,rotation:0,duration:.5,ease:"back.out(1.8)",immediateRender:false}},{VEND + 0.4:.3f});')
T(f'tl.to("#{e} .pill",{{scale:1.06,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{VEND + 0.9:.3f});')

# ===== captions: 1-2 words, white with black outline, on the strip where the reference's captions were =====
words = [w for b in B for w in b['words']]
chunks, cur = [], []
for k, w in enumerate(words):
    cur.append(w); nxt = words[k + 1] if k + 1 < len(words) else None
    if len(cur) == 2 or nxt is None or nxt[1] - cur[0][1] > 0.6 or w[0].endswith(('.', ',', '?', ':')):
        chunks.append(cur); cur = []
for k, c in enumerate(chunks):
    t0 = max(0.05, c[0][1]); t1c = chunks[k + 1][0][1] if k + 1 < len(chunks) else c[-1][2] + 0.3
    text = ' '.join(w[0].strip('.,:?') for w in c)
    i = nid('cp'); els.append(f'<div class="cap" id="{i}">{text}</div>'); vis(i, t0, t1c)
    T(f'tl.fromTo("#{i}",{{autoAlpha:0,scale:.8}},{{autoAlpha:1,scale:1,duration:.14,ease:"back.out(2.5)"}},{t0:.3f});')
for t in CUTS: sfx(t, 'sfx166', -21)

css = open('style.css').read()
html = f'''<!doctype html>
<html lang="gu"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>Kangen reel 7</title><script src="gsap.min.js"></script><style>{css}</style></head>
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
json.dump(dict(sfx=SFX, dur=DUR), open('sfx.json', 'w'))
print('ok', len(els), 'elements', len(tw), 'tweens', len(SFX), 'sfx', 'DUR', DUR, 'chunks', len(chunks))
