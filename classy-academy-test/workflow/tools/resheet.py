# resheet.py - readable half-minute sheets (30 frames, 5 x 6, 1460 px wide: no downscaling when viewed)
#   python3 -I resheet.py <id> [...]  -> study/<id>/half_MM_a.jpg (0-29 s of minute MM) and half_MM_b.jpg (30-59 s)
import sys, json, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 12)
for vid in sys.argv[1:]:
    O = f'study/{vid}'; secs = json.load(open(f'{O}/seconds.json'))
    p = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'vid/{vid}.mp4', '-vf', 'fps=1,scale=288:162', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    F1 = np.frombuffer(p, np.uint8).reshape(-1, 162, 288, 3)
    for h0 in range(0, len(F1), 30):
        part = range(h0, min(h0 + 30, len(F1)))
        sh = Image.new('RGB', (5 * 292, 6 * 222 + 22), 'white'); dr = ImageDraw.Draw(sh)
        dr.text((4, 4), f'{vid}  {h0 // 60}:{h0 % 60:02d} - {(h0 + 29) // 60}:{(h0 + 29) % 60:02d}', fill='red', font=FB)
        for k, s in enumerate(part):
            x, y = (k % 5) * 292, 22 + (k // 5) * 222
            sh.paste(Image.fromarray(F1[s]), (x + 2, y))
            r = secs[s] if s < len(secs) else {'layout': '', 'words': '', 'change': ''}
            ch = r['change']; tag = ('CUT ' if 'c' in ch else '') + ('DISS' if 'd' in ch else '')
            dr.text((x + 2, y + 163), f"{s // 60}:{s % 60:02d}  {r['layout'][:20]}", fill='blue', font=FB)
            if tag: dr.text((x + 225, y + 163), tag, fill='red', font=FB)
            w = r['words']
            for j in range(3): dr.text((x + 2, y + 178 + j * 14), w[j * 44:(j + 1) * 44], fill='black', font=F)
        sh.save(f'{O}/half_{h0 // 60:02d}_{"ab"[(h0 % 60) // 30]}.jpg', quality=85)
    print(vid, 'ok', flush=True)
