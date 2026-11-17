# test_build.py - 6 s talking test of the hand-drawn host in the reference Short's layout:
# host on top (lip-sync from the voice's loudness, blinks, head bob, lifts the glass), real footage below, pill + captions.
import json, os, subprocess, numpy as np
from host import host_svg
P = os.path.dirname(os.path.abspath(__file__)); os.chdir(P)
DUR = 6.2; W, H = 1080, 1920; TOP = 720
B = json.load(open('../reel6/beats.json')); words = [w for b in B[:2] for w in b['words']]
def sh(c): subprocess.run(c, shell=True, check=True)
def cut(name, src, a, need, w, h):
    out = f'assets/{name}.mp4'
    if not os.path.exists(out):
        sh(f'ffmpeg -y -v error -ss {a} -t {need + 0.3:.2f} -i raw/{src}.mp4 -an -vf "scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h},fps=30" -c:v libx264 -crf 19 -preset veryfast -g 30 -keyint_min 30 -pix_fmt yuv420p {out}')
    return out
tw = []; T = tw.append
# ---- lip-sync: loudness per 1/15 s -> mouth shape (m0 closed smile, m1 small, m2 wide, m3 "o") ----
y = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', 'assets/tv.wav', '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout, np.float32)
step = 1 / 15; n = int(DUR / step); hop = int(16000 * step)
rms = np.array([np.sqrt((y[i * hop:(i + 1) * hop] ** 2).mean()) if (i + 1) * hop <= len(y) else 0.0 for i in range(n)]); rms = rms / (rms.max() + 1e-9)
prev = None; opens = 0
for i in range(n):
    r = rms[i]
    if r < 0.07: m = 0
    elif r < 0.33: m = 1
    else: opens += 1; m = 3 if opens % 5 == 0 else 2
    if m != prev:
        T('tl.set(["#m0","#m1","#m2","#m3"],{visibility:"hidden"},%.3f);tl.set("#m%d",{visibility:"visible"},%.3f);' % (i * step, m, i * step)); prev = m
# ---- life: blinks, head bob, brows, glass lift ----
for t in (1.15, 3.0, 4.9):
    T('tl.to(["#eyL","#eyR"],{scaleY:.12,duration:.06,ease:"power1.in"},%.3f);tl.to(["#eyL","#eyR"],{scaleY:1,duration:.09,ease:"power1.out"},%.3f);' % (t, t + 0.07))
T('tl.set("#eyL",{svgOrigin:"258 268"},0);tl.set("#eyR",{svgOrigin:"362 268"},0);')
T('tl.fromTo("#hd",{rotation:-2.2,svgOrigin:"310 440"},{rotation:2.2,duration:1.05,ease:"sine.inOut",yoyo:true,repeat:5},0);')
T('tl.fromTo("#hd",{y:0},{y:-7,duration:.26,ease:"sine.inOut",yoyo:true,repeat:23},0);')
for t in (1.34, 3.81):     # emphasis: "પાંચ", "હાઇડ્રોજનવાળું"
    T('tl.to(["#brL","#brR"],{y:-9,duration:.14,ease:"power2.out"},%.3f);tl.to(["#brL","#brR"],{y:0,duration:.25,ease:"power2.inOut"},%.3f);' % (t, t + 0.45))
T('tl.fromTo("#arm",{rotation:6,y:26,svgOrigin:"560 700"},{rotation:0,y:0,duration:.5,ease:"back.out(1.6)"},0.05);')
T('tl.to("#arm",{rotation:-9,y:-34,duration:.4,ease:"back.out(2)"},3.0);tl.to("#arm",{rotation:-4,y:-14,duration:.6,ease:"sine.inOut"},4.4);')
T('tl.fromTo("#hostwrap",{y:60,autoAlpha:0},{y:0,autoAlpha:1,duration:.35,ease:"back.out(1.5)"},0);')
# ---- bottom footage ----
t_c = 2.68
v1 = cut('t_k83', 'kangenk83', 0.3, t_c, 1080, 1200); v2 = cut('t_k85', 'kangenk85', 3.0, DUR - t_c, 1080, 1200)
T('tl.set("#b2",{visibility:"visible"},%.3f);tl.set("#b1",{visibility:"hidden"},%.3f);' % (t_c, t_c))
T('tl.fromTo("#b1 video",{scale:1.0},{scale:1.08,duration:%.2f,ease:"none"},0);tl.fromTo("#b2 video",{scale:1.0},{scale:1.1,duration:%.2f,ease:"none"},%.3f);' % (t_c, DUR - t_c, t_c))
T('tl.fromTo("#pill",{scale:.5,autoAlpha:0},{scale:1,autoAlpha:1,duration:.35,ease:"back.out(2.2)"},0.15);')
# ---- captions (1-2 words) ----
caps = []; cur = []
for k, w in enumerate(words):
    cur.append(w); nxt = words[k + 1] if k + 1 < len(words) else None
    if len(cur) == 2 or nxt is None or w[0].endswith(('.', ',', ':', '…')): caps.append(cur); cur = []
cap_html = ''
for k, c in enumerate(caps):
    t0 = max(0.05, c[0][1]); t1 = caps[k + 1][0][1] if k + 1 < len(caps) else DUR
    cap_html += f'<div class="cap" id="cp{k}">{" ".join(w[0].strip(".,:…") for w in c)}</div>'
    T('tl.set("#cp%d",{visibility:"visible"},%.3f);tl.fromTo("#cp%d",{scale:.8},{scale:1,duration:.14,ease:"back.out(2.5)"},%.3f);' % (k, t0, k, t0))
    if t1 < DUR: T('tl.set("#cp%d",{visibility:"hidden"},%.3f);' % (k, t1))
html = f'''<!doctype html><html lang="gu"><head><meta charset="UTF-8"><meta name="viewport" content="width={W}, height={H}"><title>host test</title><script src="gsap.min.js"></script><style>
@font-face {{ font-family: "Anek"; src: url("fonts/anek-gujarati-gujarati-wdth-normal.woff2") format("woff2"); font-stretch: 75% 125%; font-weight: 100 900; unicode-range: U+0A80-0AFF, U+200C-200D, U+25CC; }}
@font-face {{ font-family: "Anek"; src: url("fonts/anek-devanagari-latin-wdth-normal.woff2") format("woff2"); font-stretch: 75% 125%; font-weight: 100 900; unicode-range: U+0000-00FF, U+2010-2212; }}
body {{ margin: 0; background: #000; }} #root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; font-family: "Anek", sans-serif; font-stretch: 85%; background: #000; }}
.top {{ position: absolute; left: 0; top: 0; width: 1080px; height: {TOP}px; overflow: hidden; background: linear-gradient(#aee0fb 0%, #dff3fd 62%, #cfe9c4 62%, #b9dca0 100%); }}
.sun {{ position: absolute; left: 90px; top: 70px; width: 150px; height: 150px; border-radius: 50%; background: #fff6c9; box-shadow: 0 0 80px 40px rgba(255,246,201,.8); }}
.tree {{ position: absolute; border-radius: 50%; background: #5c9a4e; filter: blur(3px); }}
.field {{ position: absolute; left: 0; right: 0; top: 446px; bottom: 0; background: repeating-linear-gradient(100deg, #b9dca0 0 60px, #a9d18f 60px 120px); filter: blur(2px); }}
.bot {{ position: absolute; left: 0; top: {TOP}px; width: 1080px; height: {H - TOP}px; overflow: hidden; }}
.bot video {{ position: absolute; left: 0; top: 0; width: 1080px; height: {H - TOP}px; object-fit: cover; }}
#pill {{ position: absolute; left: 0; right: 0; margin: 0 auto; width: fit-content; top: 664px; z-index: 9; background: #fff; color: #e8590c; font-weight: 900; font-size: 84px; padding: 10px 46px 20px; border-radius: 70px; box-shadow: 0 12px 30px rgba(0,0,0,.35); visibility: hidden; }}
.cap {{ position: absolute; left: 40px; right: 40px; top: 1480px; text-align: center; z-index: 9; font-weight: 900; font-size: 112px; color: #fff; visibility: hidden; text-shadow: 4px 4px 0 #000, -4px 4px 0 #000, 4px -4px 0 #000, -4px -4px 0 #000, 0 10px 26px rgba(0,0,0,.75); }}
</style></head><body><div id="root" data-composition-id="main" data-start="0" data-width="{W}" data-height="{H}" data-duration="{DUR}">
<div class="top"><div class="sun"></div><div class="field"></div>
<div class="tree" style="left:-60px;top:300px;width:330px;height:240px"></div><div class="tree" style="left:820px;top:250px;width:380px;height:290px;background:#4f8a44"></div><div class="tree" style="left:640px;top:360px;width:220px;height:150px;background:#6aa85a"></div>
<div id="hostwrap" style="position:absolute;left:170px;top:-6px;visibility:hidden">{host_svg(740, 836)}</div></div>
<div class="bot" id="b1"><video id="b1v" src="{v1}" muted playsinline data-start="0" data-duration="{t_c + 0.05:.2f}"></video></div>
<div class="bot" id="b2" style="visibility:hidden"><video id="b2v" src="{v2}" muted playsinline data-start="{t_c:.2f}" data-duration="{DUR - t_c:.2f}"></video></div>
<div id="pill">એક મશીન, પાંચ પાણી 💧</div>
{cap_html}
<audio id="mix" src="assets/mix.wav" data-start="0" data-duration="{DUR}"></audio>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tw)}
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl;
</script></body></html>'''
open('index.html', 'w').write(html); print('ok', len(tw), 'tweens; mouth changes', sum('m0' in t for t in tw))
