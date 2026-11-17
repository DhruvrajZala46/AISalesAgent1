# sheets.py - numbered contact sheets of the thumbnails in each view tier (for tagging by eye) + measured brightness / colour
import json, os, numpy as np
from PIL import Image, ImageDraw
T = json.load(open('table.json')); W, H, C, R = 384, 216, 5, 4; meas = {}
def fmt(n): return f'{n/1e6:.1f}M' if n >= 1e6 else f'{n/1e3:.0f}k'
for tier, key in (('D', 'DW'), ('S', 'SW'), ('R', 'RW'), ('M', 'SM'), ('L', 'SL')):
    vs = [v for v in T[key] if os.path.exists(f"img/{v['id']}.jpg")]
    for n in range(0, len(vs), C * R):
        sh = Image.new('RGB', (C * W, R * (H + 26)), 'white'); dr = ImageDraw.Draw(sh)
        for k, v in enumerate(vs[n:n + C * R]):
            try: im = Image.open(f"img/{v['id']}.jpg").convert('RGB')
            except Exception: continue
            if im.size[1] * 16 > im.size[0] * 9 + 16:      # hqdefault 4:3 with bars -> cut to 16:9
                h2 = im.size[0] * 9 // 16; top = (im.size[1] - h2) // 2; im = im.crop((0, top, im.size[0], top + h2))
            a = np.asarray(im.resize((160, 90))).astype(float); lum = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2])
            mx, mn = a.max(2), a.min(2); sat = ((mx - mn) / (mx + 1e-6)).mean()
            meas[v['id']] = dict(tier=tier, n=n + k + 1, lum=round(float(lum.mean()), 1), sat=round(float(sat), 3), light=round(float((lum > 200).mean()), 3), dark=round(float((lum < 50).mean()), 3))
            x, y = (k % C) * W, (k // C) * (H + 26); sh.paste(im.resize((W, H), Image.LANCZOS), (x, y + 26))
            dr.text((x + 3, y + 1), f"{tier}{n + k + 1:03d} {fmt(v['views'])} {v['channel'][:24]}", fill=(200, 0, 0)); dr.text((x + 3, y + 13), v['title'][:62], fill='black')
        sh.save(f'sheets/{tier}_{n // (C * R):02d}.jpg', quality=84)
    print(tier, len(vs), 'thumbnails,', (len(vs) + C * R - 1) // (C * R), 'sheets')
json.dump(meas, open('meas.json', 'w'))
