# ca_logo.py - extract the REAL Classy Academy logo from the channel's own thumbnails (8 Nov 2026).
# The logo sits at the same place on every CA thumbnail, over different photos. Its white strokes are the pixels that stay
# bright in (almost) all of them: the 15th percentile of the top-left corner across all thumbnails, minus the local
# background, is the logo's alpha. Output: assets/logo_ca.png (white, transparent) + its position on a 1280x720 canvas.
# usage: python3 ca_logo.py thumbs/*.jpg      (the channel's thumbnails, maxres, e.g. fetched with yt-dlp --flat-playlist)
import sys, os, numpy as np
from PIL import Image, ImageFilter
fs = sys.argv[1:]
A = np.stack([np.asarray(Image.open(f).convert('L').resize((1280, 720)))[:240, :300].astype(np.float32) for f in fs])
p = np.percentile(A, 15, axis=0)
bgl = np.asarray(Image.fromarray(p.astype(np.uint8)).filter(ImageFilter.MedianFilter(15))).astype(np.float32)
a = np.clip((p - bgl - 18) / (255 - bgl - 18), 0, 1); m = np.zeros_like(a); m[18:132, 28:196] = 1; a *= m
ys, xs = np.where(a > 0.12); x0, x1, y0, y1 = xs.min() - 3, xs.max() + 4, ys.min() - 3, ys.max() + 4
L = Image.new('RGBA', (x1 - x0, y1 - y0), (255, 255, 255, 0)); L.putalpha(Image.fromarray((np.clip(a[y0:y1, x0:x1] * 1.15, 0, 1) * 255).astype(np.uint8)))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'logo_ca.png'); L.save(out)
print(len(fs), 'thumbnails -> logo at', (int(x0), int(y0)), 'size', L.size, '->', out)
