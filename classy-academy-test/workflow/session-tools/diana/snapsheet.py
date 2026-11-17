# snapsheet.py [dir] -> <dir>/sheet_NN.jpg : 12 snapshots per sheet (3 x 4 at 640x360), each labelled with its time
import glob, re, sys, os
from PIL import Image, ImageDraw
d = sys.argv[1] if len(sys.argv) > 1 else 'snaps'
fs = sorted(glob.glob(f'{d}/frame-*.png'), key=lambda f: float(re.search(r'at-([\d.]+)s', f).group(1)))
for n in range(0, len(fs), 12):
    sh = Image.new('RGB', (1920, 4 * 376), 'white'); dr = ImageDraw.Draw(sh)
    for k, f in enumerate(fs[n:n + 12]):
        im = Image.open(f).convert('RGB').resize((640, 360), Image.LANCZOS); x, y = (k % 3) * 640, (k // 3) * 376
        sh.paste(im, (x, y + 16)); dr.text((x + 4, y + 2), re.search(r'at-([\d.]+)s', f).group(1) + ' s', fill='black')
    sh.save(f'{d}/sheet_{n // 12:02d}.jpg', quality=85)
print(len(fs), 'snapshots')
