# facecheck.py <dir> '<json fixes>' : applies manual face boxes and writes <dir>/facefix.jpg (each box drawn on a crop around it)
import json, sys
from PIL import Image, ImageDraw
D = sys.argv[1]; fix = json.loads(sys.argv[2]); F = f'{D}/faces.json'; d = json.load(open(F))
for k, v in fix.items(): d[k]['face'] = v; d[k]['kind'] = 'manual'
json.dump(d, open(F, 'w'), indent=1); tiles = []
for k in fix:
    im = Image.open(f'{D}/{k}').convert('RGB'); x, y, w, h = d[k]['face']; m = int(max(w, h) * 0.8)
    c = im.crop((x - m, y - m, x + w + m, y + h + m)); dr = ImageDraw.Draw(c); dr.rectangle((m, m, m + w, m + h), outline=(255, 0, 0), width=max(3, w // 60)); c.thumbnail((360, 360)); tiles.append(c)
S = Image.new('RGB', (360 * len(tiles), 360), 'white')
for i, t in enumerate(tiles): S.paste(t, (i * 360, 0))
S.save(f'{D}/facefix.jpg')
