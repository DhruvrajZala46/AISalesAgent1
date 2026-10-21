# range_sheet.py T0 T1 [STEP] [OUT] : the edit between T0 and T1 as a contact sheet, a frame every STEP s (quarter size), with the
# time, the scene and the words spoken (checks a stretch before rendering it)
import sys, json, os
t0, t1 = float(sys.argv[1]), float(sys.argv[2]); step = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
out = sys.argv[4] if len(sys.argv) > 4 else f'qc/range_{int(t0)}_{int(t1)}.jpg'
sys.argv = ['render.py', '--scale', '0.25']; sys.path.insert(0, 'project')
import render as R
from PIL import Image, ImageDraw, ImageFont
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
S = json.load(open('project/clock.json'))['sentences']
def words(t):
    for s in S:
        if s['start'] <= t < s['end']:
            k = int(len(s['text']) * (t - s['start']) / (s['end'] - s['start'])); return s['text'][max(0, k - 22):k + 22]
    return '(pause)'
def scene(t):
    sg = [g for g in R.SEG if g['t0'] <= t + 1e-6][-1]; return f"{sg['scene']} {sg['kind']}"
ts = []; t = t0
while t <= t1 + 1e-6: ts.append(round(t, 2)); t += step
cols = 6; rows = (len(ts) + cols - 1) // cols
sh = Image.new('RGB', (cols * 484, rows * 300), 'white'); d = ImageDraw.Draw(sh)
for k, t in enumerate(ts):
    x, y = (k % cols) * 484, (k // cols) * 300
    sh.paste(Image.fromarray(R.frame_at(t)), (x + 2, y))
    d.text((x + 4, y + 272), f'{int(t // 60)}:{t % 60:04.1f}  sc {scene(t)}', fill='blue', font=F)
    d.text((x + 4, y + 285), words(t), fill='black', font=F)
sh.save(out, quality=80); print(out)
