# qc_sheet.py - the whole edit as contact sheets: a frame every STEP seconds (quarter size) with time, scene and the words spoken
#   python3 -I qc_sheet.py [step] -> qc/sheet_NN.jpg (40 frames per sheet)
import sys, json, os
step = float(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 2.0
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
ts = [round(i * step, 2) for i in range(int(R.DUR / step) + 1)]
os.makedirs('qc', exist_ok=True)
for n0 in range(0, len(ts), 40):
    sh = Image.new('RGB', (5 * 484, 8 * 300), 'white'); d = ImageDraw.Draw(sh)
    for k, t in enumerate(ts[n0:n0 + 40]):
        x, y = (k % 5) * 484, (k // 5) * 300
        sh.paste(Image.fromarray(R.frame_at(t)), (x + 2, y))
        d.text((x + 4, y + 272), f'{int(t // 60)}:{t % 60:04.1f}  sc {scene(t)}', fill='blue', font=F)
        d.text((x + 4, y + 285), words(t), fill='black', font=F)
    sh.save(f'qc/sheet_{n0 // 40:02d}.jpg', quality=80); print('sheet', n0 // 40, flush=True)
