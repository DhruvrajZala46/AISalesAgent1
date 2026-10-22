# faces.py <dir> : finds the biggest face (frontal, then profile both ways) in each jpg; writes <dir>/faces.json and <dir>/faces.jpg
import json, os, sys, cv2
from PIL import Image, ImageDraw
D = sys.argv[1]; C = cv2.data.haarcascades
fr = cv2.CascadeClassifier(C + 'haarcascade_frontalface_default.xml'); pr = cv2.CascadeClassifier(C + 'haarcascade_profileface.xml')
out = {}
for f in sorted(os.listdir(D)):
    if not f.lower().endswith(('.jpg', '.jpeg', '.png')) or f.startswith(('review', 'faces', 'sheet')): continue
    im = cv2.imread(f'{D}/{f}'); h, w = im.shape[:2]; s = 1000 / max(h, w); g = cv2.cvtColor(cv2.resize(im, None, fx=s, fy=s), cv2.COLOR_BGR2GRAY)
    best = None
    for kind, c, flip in (('front', fr, 0), ('profile', pr, 0), ('profile', pr, 1)):
        gg = cv2.flip(g, 1) if flip else g
        r = c.detectMultiScale(gg, 1.08, 5, minSize=(40, 40))
        for x, y, ww, hh in r:
            if flip: x = gg.shape[1] - x - ww
            if best is None or ww * hh > best[2] * best[3]: best = (int(x / s), int(y / s), int(ww / s), int(hh / s), kind)
        if best and kind == 'front': break
    out[f] = {'w': w, 'h': h, 'face': list(best[:4]) if best else None, 'kind': best[4] if best else None}
json.dump(out, open(f'{D}/faces.json', 'w'), indent=1)
tiles = []
for f, v in out.items():
    im = Image.open(f'{D}/{f}').convert('RGB'); im.thumbnail((300, 420)); k = im.width / v['w']; d = ImageDraw.Draw(im)
    if v['face']:
        x, y, ww, hh = [a * k for a in v['face']]; d.rectangle((x, y, x + ww, y + hh), outline=(255, 0, 0), width=3)
    d.text((4, 4), f[:28], fill=(255, 255, 0)); tiles.append(im)
cols = 6; rows = (len(tiles) + cols - 1) // cols; S = Image.new('RGB', (cols * 300, rows * 420), 'white')
for i, t in enumerate(tiles): S.paste(t, ((i % cols) * 300, (i // cols) * 420))
S.save(f'{D}/faces.jpg', quality=85); print(json.dumps(out))
