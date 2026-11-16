# build.py - Kangen reel 6 (Gujarati, ~40 s): "એક મશીન, પાંચ પાણી" in the style of the owner's reference reel
# (quick cuts, 1-2 word pop captions, opening circle montage) plus a 1/5..5/5 counter, a WhatsApp DEMO reply bubble, end card.
import json, os, subprocess, math
P = os.path.dirname(os.path.abspath(__file__)); os.chdir(P)
B = json.load(open('beats.json')); VEND = B[-1]['end']; DUR = round(VEND + 3.0, 2)
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
        if avail < need + 0.2: speed = max(0.45, avail / (need + 0.2))
        take = min(avail, (need + 0.2) * speed)
        pre = f"crop=iw*{crop[2]}:ih*{crop[3]}:iw*{crop[0]}:ih*{crop[1]}," if crop else ""
        sh(f'ffmpeg -y -v error -ss {a} -t {take:.3f} -i raw/{src}.mp4 -an -vf "{pre}setpts=PTS/{speed},scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},fps=30" -c:v libx264 -crf 19 -preset veryfast -g 30 -keyint_min 30 -pix_fmt yuv420p -movflags +faststart {out}')
    return out
els, tw, SFX = [], [], []
def T(s): tw.append(s)
n = [0]
def nid(p='e'): n[0] += 1; return f'{p}{n[0]}'
def sfx(t, f, g=-14): SFX.append((round(t, 3), f, g))
def vis(i, t0, t1=None):
    T(f'tl.set("#{i}",{{visibility:"visible"}},{t0:.3f});')
    if t1 is not None and t1 < DUR: T(f'tl.set("#{i}",{{visibility:"hidden"}},{t1:.3f});')
def key(*a): return '_'.join(str(x) for x in a).replace('.', 'p').replace(' ', '').replace(',', '-').replace('(', '').replace(')', '')
CUTS = []
def shot(src, a, t0, t1, crop=None, zoom=(1.0, 1.08), inner='', ease='none', whoosh=True):
    i = nid('sh'); f = cut(key(src, a, int(t0 * 10), crop), src, a, t1 - t0, crop=crop)
    els.append(f'<div class="shot" id="{i}"><div class="zw" id="{i}z"><video id="{i}v" src="{f}" muted playsinline data-start="{t0:.3f}" data-duration="{t1 - t0 + 0.05:.3f}"></video>{inner}</div></div>')
    vis(i, t0, t1)
    T(f'tl.fromTo("#{i}z",{{scale:{zoom[0]}}},{{scale:{zoom[1]},duration:{t1 - t0:.3f},ease:"{ease}"}},{t0:.3f});')
    if whoosh and t0 > 0.1: CUTS.append(t0)
    return i
def el(html, t0, t1, frm='autoAlpha:0,scale:0.6', ease='back.out(2)', d=0.3, s=None, g=-16):
    i = nid('x'); els.append(html.replace('ID', i)); vis(i, t0, t1)
    T(f'tl.fromTo("#{i}",{{{frm}}},{{autoAlpha:1,scale:1,x:0,y:0,duration:{d},ease:"{ease}"}},{t0:.3f});')
    if s: sfx(t0, s, g)
    return i

# ============ 0. hook: "એક જ મશીન… અને પાંચ અલગ-અલગ પાણી" - beige board, the machine, then five circles pop ============
t1 = st(2)
els.append('<div class="shot" id="hook"><div class="beige"></div></div>'); vis('hook', 0, t1 + 0.3)
big = nid('c'); fb = cut('c_k8', 'kangenk83', 0.3, t1 + 0.5, 600, 600, crop=(0, 0.16, 1, 0.84))
els.append(f'<div class="circ" id="{big}" style="left:240px;top:520px;width:600px;height:600px"><video id="{big}v" src="{fb}" muted playsinline data-start="0" data-duration="{t1 + 0.35:.3f}"></video></div>')
vis(big, 0.0, t1 + 0.3)
T(f'tl.fromTo("#{big}",{{scale:.4,autoAlpha:0}},{{scale:1,autoAlpha:1,duration:.4,ease:"back.out(1.8)"}},0);')
T(f'tl.to("#{big}",{{scale:.62,y:-330,duration:.45,ease:"power3.inOut"}},{at(1, "અને") - 0.1:.3f});')
sfx(0.02, 'sfx1143', -14)
FIVE = [('kangenk85', 3.0, None), ('chai14', 0.3, None), ('pill14', 0.6, None), ('kangenk849', 13.2, None), ('clean9', 0.4, None)]
pos = [(60, 1000), (400, 1080), (740, 1000), (210, 1380), (590, 1380)]
for k, ((src, a, cr), (x, y)) in enumerate(zip(FIVE, pos)):
    c = nid('c'); f = cut(key('c5', src, a), src, a, t1 + 0.5, 280, 280, crop=cr)
    els.append(f'<div class="circ" id="{c}" style="left:{x}px;top:{y}px;width:280px;height:280px"><video id="{c}v" src="{f}" muted playsinline data-start="0" data-duration="{t1 + 0.35:.3f}"></video><div class="n">{k + 1}</div></div>')
    tp = at(1, 'પાંચ') - 0.05 + k * 0.17
    vis(c, tp, t1 + 0.3)
    T(f'tl.fromTo("#{c}",{{scale:0,autoAlpha:0}},{{scale:1,autoAlpha:1,duration:.3,ease:"back.out(2.4)"}},{tp:.3f});'); sfx(tp, 'sfx3005', -15)
T(f'tl.to("#hook",{{autoAlpha:0,duration:.3}},{t1:.3f});')

# ============ 1-5: the five waters, each with a counter badge ============
def badge(num, label, t0, t1):
    i = nid('cn'); els.append(f'<div class="cnt" id="{i}"><b>{num}/5</b>{label}</div>'); vis(i, t0, t1)
    T(f'tl.fromTo("#{i}",{{autoAlpha:0,y:-40}},{{autoAlpha:1,y:0,duration:.3,ease:"back.out(2)"}},{t0:.3f});'); sfx(t0, 'sfx3005', -17)
shot('kangenk85', 3.0, st(2), st(3), zoom=(1.0, 1.1), whoosh=False); badge(1, 'પીવા માટે', st(2), st(3))
t_d = at(3, 'દાળ') - 0.1
shot('chai14', 0.3, st(3), t_d, zoom=(1.0, 1.1)); shot('dal30', 0.6, t_d, st(4), zoom=(1.05, 1.15)); badge(2, 'રસોઈ માટે', st(3), st(4))
shot('pill14', 0.6, st(4), st(5), zoom=(1.0, 1.08)); badge(3, 'દવા માટે', st(4), st(5))
shot('kangenk849', 13.0, st(5), st(6), zoom=(1.0, 1.12)); badge(4, 'શાક-ફળ ધોવા', st(5), st(6))
shot('clean9', 0.3, st(6), st(7), zoom=(1.0, 1.08)); badge(5, 'સફાઈ માટે', st(6), st(7))
# ============ why: not just a filter, Japan 50 years, medical device ============
t_j = at(7, 'જાપાનમાં') - 0.1
shot('bubbles35', 0.3, st(7), t_j, zoom=(1.0, 1.18))
shot('kangenk83', 0.3, t_j, st(8), crop=(0, 0.16, 1, 0.84), zoom=(1.12, 1.0))
el('<div class="chip y" id="ID" style="left:0;right:0;margin:0 auto;width:fit-content;top:300px">જાપાન • 50 વર્ષથી</div>', at(7, 'પચાસ') - 0.1, st(8), 'autoAlpha:0,y:-40', s='sfx3005', g=-16)
i = nid('st'); els.append(f'<div class="stamp" id="{i}" style="top:760px">✓ મેડિકલ ડિવાઇસ</div>'); vis(i, at(7, 'મેડિકલ') - 0.1, st(8))
T(f'tl.fromTo("#{i}",{{autoAlpha:0,scale:2.6,rotation:-22}},{{autoAlpha:1,scale:1,rotation:-7,duration:.25,ease:"power4.in"}},{at(7, "મેડિકલ") - 0.1:.3f});'); sfx(at(7, 'મેડિકલ') + 0.12, 'sfx2364', -11)
# ============ curiosity: the five buttons, question marks ============
inner = ''.join(f'<div class="qm" id="q{k}" style="left:{x}px;top:{y}px">?</div>' for k, (x, y) in enumerate([(90, 380), (820, 300), (140, 1500), (850, 1420), (480, 240)]))
shot('kangenk87', 15.0, st(8), st(9), zoom=(1.0, 1.1), inner=inner)
for k in range(5):
    t = st(8) + 0.15 + k * 0.18
    T(f'tl.set("#q{k}",{{visibility:"visible"}},{t:.3f});tl.fromTo("#q{k}",{{autoAlpha:0,scale:.3,rotation:-25}},{{autoAlpha:1,scale:1,rotation:{(-1) ** k * 10},duration:.35,ease:"back.out(2)"}},{t:.3f});')
    T(f'tl.fromTo("#q{k}",{{y:0}},{{y:-40,duration:{st(9) - t - 0.35:.3f},ease:"sine.inOut",immediateRender:false}},{t + 0.35:.3f});')
# ============ CTA: reply DEMO to this status ============
shot('phone0', 0.3, st(9), st(10), zoom=(1.0, 1.08))
el('<div class="wa" id="ID"><div class="h">તમારો જવાબ</div><div class="t">DEMO</div><div class="m">✓✓</div></div>', at(9, 'DEMO') - 0.05, st(10), 'autoAlpha:0,y:120,scale:.6', 'back.out(2)', d=.35, s='sfx1311', g=-14)
shot('demo1', 8.0, st(10), VEND + 0.2, crop=(0, 0.05, 1, 0.95), zoom=(1.0, 1.1))
el('<div class="chip g" id="ID" style="left:80px;top:420px">ફ્રી વોટર ટેસ્ટ</div>', at(10, 'ફ્રી') - 0.05, VEND + 0.2, 'autoAlpha:0,x:-160', s='sfx3005', g=-15)
el('<div class="chip y" id="ID" style="right:80px;top:560px">લાઇવ ડેમો</div>', at(10, 'લાઇવ') - 0.05, VEND + 0.2, 'autoAlpha:0,x:160', s='sfx3005', g=-15)
# ============ end card ============
e = el('<div class="end" id="ID"><div class="bub">DEMO</div><div class="l1">આ સ્ટેટસ પર લખીને રિપ્લાય કરો</div><div class="l2">ફ્રી ઘરે ડેમો</div><div class="l3">Enagic Kangen • ચોટીલા</div></div>', VEND + 0.2, DUR, 'autoAlpha:0', 'power2.out', d=.35, s='sfx1143', g=-12)
T(f'tl.fromTo("#{e} .bub",{{scale:.4}},{{scale:1,duration:.45,ease:"back.out(2.4)",immediateRender:false}},{VEND + 0.25:.3f});')
T(f'tl.to("#{e} .bub",{{scale:1.08,duration:.4,yoyo:true,repeat:3,ease:"sine.inOut"}},{VEND + 0.8:.3f});')

# ============ captions: 1-2 words at a time, keywords in yellow ============
KEY = ['પાંચ', 'પીવા', 'હાઇડ્રોજનવાળું', 'ચા,', 'દાળ', 'ભાત', 'દવા', 'ન્યુટ્રલ', 'શાકભાજી-ફળ', 'સ્ટ્રોંગ', 'સફાઈ', 'ફિલ્ટર', 'જાપાનમાં', 'પચાસ', 'મેડિકલ', 'માન્યતા', 'પાંચે', 'DEMO', 'ફ્રી', 'લાઇવ', 'મશીન…']
words = [w for b in B for w in b['words']]
chunks, cur = [], []
for k, w in enumerate(words):
    cur.append(w)
    nxt = words[k + 1] if k + 1 < len(words) else None
    if len(cur) == 2 or nxt is None or nxt[1] - cur[0][1] > 0.6 or w[0].endswith(('.', ',', '?', ':', '…')) or w[0] in KEY or (nxt and nxt[0] in KEY):
        chunks.append(cur); cur = []
for k, c in enumerate(chunks):
    t0 = c[0][1]; t1c = chunks[k + 1][0][1] if k + 1 < len(chunks) else c[-1][2] + 0.3
    if t0 < 0.05: t0 = 0.05
    text = ' '.join(w[0].strip('.,:?…') for w in c)
    hot = any(w[0] in KEY for w in c)
    top = '' if t0 >= st(2) else (' style="top:1180px"' if t0 < at(1, 'અને') - 0.1 else ' style="top:800px"')
    i = nid('cp'); els.append(f'<div class="cap{" k" if hot else ""}{" dark" if t0 < st(2) else ""}" id="{i}"{top}>{text}</div>'); vis(i, t0, t1c)
    T(f'tl.fromTo("#{i}",{{autoAlpha:0,scale:.7,y:20}},{{autoAlpha:1,scale:1,y:0,duration:.16,ease:"back.out(2.5)"}},{t0:.3f});')
for t in CUTS: sfx(t, 'sfx166', -20)

overlays = '<div class="botfade"></div><div class="vign"></div>'
css = open('style.css').read()
html = f'''<!doctype html>
<html lang="gu"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}">
<title>Kangen reel 6</title><script src="gsap.min.js"></script><style>{css}</style></head>
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
json.dump(dict(sfx=SFX, dur=DUR), open('sfx.json', 'w'))
print('ok', len(els), 'elements', len(tw), 'tweens', len(SFX), 'sfx', 'DUR', DUR, 'chunks', len(chunks))
