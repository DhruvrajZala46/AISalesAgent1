import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from multiprocessing import Pool
from PIL import Image, ImageDraw
import edit
from scenes import Clip

def one(i, frac=0.6):
    sc = edit.build(); s = sc[i]
    tm = s.t0 + (s.t1 - s.t0) * frac
    for L in s.layers:
        if isinstance(L, Clip) and L.live(tm):
            L.tin += (tm - L.t0); L.t0 = tm; L.appear = 'none'
    f = s.render(tm); s.close()
    im = Image.fromarray(np.clip(f, 0, 255).astype(np.uint8)).resize((480, 270))
    return i, s.name, s.t0, im

if __name__ == '__main__':
    out = sys.argv[1]; idx = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else None
    n = len(edit.build()); idx = idx or list(range(n))
    with Pool(4) as p: res = p.map(one, idx)
    cols = 6; rows = (len(res) + cols - 1) // cols
    sh = Image.new('RGB', (cols * 480, rows * 290), 'black'); d = ImageDraw.Draw(sh)
    for k, (i, name, t0, im) in enumerate(res):
        x, y = (k % cols) * 480, (k // cols) * 290; sh.paste(im, (x, y + 20)); d.text((x + 3, y + 3), f'{i} {name} {int(t0//60)}:{t0%60:04.1f}', fill='yellow')
    sh.save(out, quality=82); print('saved', out)
