# split each 640x480 YouTube auto-frame (letterboxed 16:9) into its picture panels: python3 -I panels.py sd/ panels/
import sys, os, glob
import numpy as np
from PIL import Image
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
n = 0
for f in sorted(glob.glob(src + '/*_sd[123].jpg')):
    im = Image.open(f).convert('RGB').crop((0, 60, 640, 420)); a = np.asarray(im).astype(float)
    g = np.abs(np.diff(a.mean(2), axis=1))            # horizontal gradient
    strong = (g > 18).mean(0)                          # share of rows with an edge at each column
    cuts = [0] + [x + 1 for x in range(4, 635) if strong[x] > 0.55 and strong[x] >= strong[max(0, x - 3):x + 4].max()] + [640]
    segs = []
    for x0, x1 in zip(cuts, cuts[1:]):
        if x1 - x0 < 60: continue
        seg = a[:, x0:x1]
        busy = np.abs(np.diff(seg.mean(2), axis=0)).mean()   # caramel backdrop is smooth
        if busy < 2.0: continue
        segs.append((x0, x1))
    if not segs: segs = [(0, 640)]
    base = os.path.basename(f)[:-4]
    for k, (x0, x1) in enumerate(segs):
        im.crop((x0, 0, x1, 360)).save(f'{out}/{base}_p{k}.png'); n += 1
print(n, 'panels')
