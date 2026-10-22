# sheet.py <tsv> <thumbdir> <out.jpg> [cols] : labelled contact sheet (id + photographer) of the thumbnails listed in the tsv
import sys
from PIL import Image, ImageDraw
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[1]) if l.strip()]; cols = int(sys.argv[4]) if len(sys.argv) > 4 else 10
TW, TH = 250, 380; tiles = []
for r in rows:
    try: im = Image.open(f'{sys.argv[2]}/{r[0]}.jpg').convert('RGB')
    except Exception: continue
    im.thumbnail((TW, TH - 30)); t = Image.new('RGB', (TW, TH), 'white'); t.paste(im, ((TW - im.width) // 2, 0))
    d = ImageDraw.Draw(t); d.text((3, TH - 28), r[0], fill=(0, 0, 0)); d.text((3, TH - 15), r[2][:34], fill=(90, 60, 0)); tiles.append(t)
n = len(tiles); rr = (n + cols - 1) // cols; S = Image.new('RGB', (cols * TW, rr * TH), 'white')
for i, t in enumerate(tiles): S.paste(t, ((i % cols) * TW, (i // cols) * TH))
S.save(sys.argv[3], quality=85); print(n, S.size)
