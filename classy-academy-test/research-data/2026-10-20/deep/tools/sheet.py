# Contact sheet of YouTube thumbnails: python3 sheet.py items.json out.jpg [cols]
# items: [{"id":..., "label":...}]. Images are fetched from i.ytimg.com into thumbs/ (media, never committed).
import json, sys, os, urllib.request, textwrap
from PIL import Image, ImageDraw, ImageFont
items = json.load(open(sys.argv[1])); out = sys.argv[2]; cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
os.makedirs('thumbs', exist_ok=True)
W, H, LH = 480, 270, 58
try: font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
except Exception: font = ImageFont.load_default()
rows = (len(items) + cols - 1) // cols
sheet = Image.new('RGB', (cols * W, rows * (H + LH)), 'white'); dr = ImageDraw.Draw(sheet)
for i, it in enumerate(items):
    f = f"thumbs/{it['id']}.jpg"
    if not os.path.exists(f):
        for q in ('maxresdefault', 'hqdefault'):
            try: urllib.request.urlretrieve(f"https://i.ytimg.com/vi/{it['id']}/{q}.jpg", f); break
            except Exception: pass
    x, y = (i % cols) * W, (i // cols) * (H + LH)
    try:
        im = Image.open(f).convert('RGB'); r = max(W / im.width, H / im.height); im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1))
        l, t = (im.width - W) // 2, (im.height - H) // 2; sheet.paste(im.crop((l, t, l + W, t + H)), (x, y))
    except Exception: dr.text((x + 10, y + 10), 'no image', fill='red', font=font)
    for j, line in enumerate(textwrap.wrap(it['label'], 58)[:3]): dr.text((x + 4, y + H + 2 + j * 18), line, fill='black', font=font)
sheet.save(out, quality=85); print(out, sheet.size)
