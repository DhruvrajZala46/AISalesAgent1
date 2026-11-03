# Download the original of a picked photo pin and cut the product out of its plain studio background.
# usage: python3 cutout.py name=tag:index[:tol] ...   -> assets/ph_<name>.png (RGBA, trimmed) + cut/<name>_check.jpg
import sys, json, os, urllib.request
import numpy as np, cv2
from PIL import Image, ImageFilter
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
os.makedirs('cut', exist_ok=True); os.makedirs('phraw', exist_ok=True)
log = json.load(open('ph_picks.json')) if os.path.exists('ph_picks.json') else {}
for arg in sys.argv[1:]:
    name, spec = arg.split('='); parts = spec.split(':'); tag, k = parts[0], int(parts[1]); tol = float(parts[2]) if len(parts) > 2 else 16
    p = json.load(open(f'ph/{tag}.json'))[k]; raw = f'phraw/{name}.jpg'
    if not os.path.exists(raw):
        open(raw, 'wb').write(urllib.request.urlopen(urllib.request.Request(p['orig'], headers={'User-Agent': UA}), timeout=60).read())
    im = np.asarray(Image.open(raw).convert('RGB')).astype(np.int16); h, w = im.shape[:2]
    if 'nocut' in parts:
        Image.fromarray(im.astype(np.uint8)).save(f'assets/ph_{name}.png')
    else:
        border = np.concatenate([im[:4].reshape(-1, 3), im[-4:].reshape(-1, 3), im[:, :4].reshape(-1, 3), im[:, -4:].reshape(-1, 3)])
        bgc = np.median(border, 0)
        # background = pixels close to the border colour (allowing a soft gradient) AND connected to the border
        lab = cv2.cvtColor(im.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
        bl = cv2.cvtColor(bgc.reshape(1, 1, 3).astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)[0, 0]
        bord = np.concatenate([lab[:4].reshape(-1, 3), lab[-4:].reshape(-1, 3), lab[:, :4].reshape(-1, 3), lab[:, -4:].reshape(-1, 3)]).astype(np.float32)
        _, lbl, cent = cv2.kmeans(bord, 3, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0), 3, cv2.KMEANS_PP_CENTERS)
        cent = [c for c, n in zip(cent, np.bincount(lbl.ravel(), minlength=3)) if n > 0.04 * len(bord)]
        d = np.min([np.sqrt(((lab - c) ** 2).sum(2)) for c in cent], 0)
        near = (d < tol).astype(np.uint8)
        n, cc = cv2.connectedComponents(near, connectivity=4)
        edge = set(np.unique(np.concatenate([cc[0], cc[-1], cc[:, 0], cc[:, -1]]))) - {0}
        bg = (near > 0) if 'all' in parts else (np.isin(cc, list(edge)) & (near > 0))
        fg = (~bg).astype(np.uint8) * 255
        fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)); fg = cv2.morphologyEx(fg, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
        # keep the biggest blobs only (drops specks)
        n2, cc2, stats, _ = cv2.connectedComponentsWithStats((fg > 0).astype(np.uint8))
        keep = [i for i in range(1, n2) if stats[i, 4] > 0.01 * h * w]
        fg = np.isin(cc2, keep).astype(np.uint8) * 255
        a = Image.fromarray(fg).filter(ImageFilter.GaussianBlur(1.2))
        rgba = Image.fromarray(im.astype(np.uint8)).convert('RGBA'); rgba.putalpha(a)
        bb = a.getbbox(); rgba = rgba.crop(bb)
        rgba.save(f'assets/ph_{name}.png')
        chk = Image.new('RGB', rgba.size, (195, 141, 98)); chk.paste(rgba, (0, 0), rgba); chk.thumbnail((400, 500)); chk.save(f'cut/{name}_check.jpg')
    log[name] = dict(tag=tag, k=k, url=p['url'], link=p['link'], domain=p['domain'], creator=p['creator'], user=p['user'], w=p['w'], h=p['h'])
    print(name, p['domain'], p['w'], p['h'])
json.dump(log, open('ph_picks.json', 'w'), indent=1)
