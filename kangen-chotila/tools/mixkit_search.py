# mixkit_search.py out_dir tag="query words" ...  -> out/<tag>.json + contact sheet of thumbnails with ids
# Only keeps clips whose -1080.mp4 exists (Mixkit "Stock Video Free License"; restricted ones have no 1080 file)
import sys, re, json, os, subprocess, urllib.request, urllib.parse
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0'}
def get(u):
    try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=25).read().decode('utf8', 'ignore')
    except Exception as e: return ''
def head(u):
    try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA, method='HEAD'), timeout=20).status
    except Exception as e: return getattr(e, 'code', 0)
for arg in sys.argv[2:]:
    tag, q = arg.split('=', 1)
    items = {}
    for page in (1, 2):
        slug = urllib.parse.quote(q.strip().replace(' ', '-'))
        u = f'https://mixkit.co/free-stock-video/discover/{slug}/' + (f'?page={page}' if page > 1 else '')
        h = get(u)
        for m in re.finditer(r'href="/free-stock-video/([a-z0-9-]+)-(\d+)/"', h):
            items.setdefault(m.group(2), m.group(1))
    keep = []
    for vid, name in list(items.items())[:36]:
        if head(f'https://assets.mixkit.co/videos/{vid}/{vid}-1080.mp4') == 200:
            keep.append(dict(id=vid, name=name))
    json.dump(keep, open(f'{OUT}/{tag}.json', 'w'), indent=0)
    # contact sheet
    tw, th = 320, 180; cols = 6; rows = (len(keep) + cols - 1) // cols or 1
    sheet = Image.new('RGB', (cols * tw, rows * (th + 26)), 'white'); d = ImageDraw.Draw(sheet)
    for k, it in enumerate(keep):
        try:
            data = urllib.request.urlopen(urllib.request.Request(f"https://assets.mixkit.co/videos/{it['id']}/{it['id']}-thumb-360-0.jpg", headers=UA), timeout=20).read()
            open('/tmp/_t.jpg', 'wb').write(data); im = Image.open('/tmp/_t.jpg').convert('RGB'); im.thumbnail((tw, th))
            x, y = (k % cols) * tw, (k // cols) * (th + 26); sheet.paste(im, (x, y)); d.text((x + 4, y + th + 4), f"{it['id']} {it['name'][:34]}", fill='black')
        except Exception: pass
    sheet.save(f'{OUT}/sheet_{tag}.jpg', quality=82)
    print(tag, len(items), 'found,', len(keep), 'free licence', flush=True)
