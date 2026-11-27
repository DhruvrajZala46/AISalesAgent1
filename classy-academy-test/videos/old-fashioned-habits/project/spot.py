# render specific time windows at 2 fps to a sheet (no encode)
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw
import edit, scenes as S
from multiprocessing import Pool
def win(ab):
    a, b = ab; sc = edit.build(); out = []
    for n in range(int(a * 30), int(b * 30)):
        t = n / 30
        i = max(k for k, s in enumerate(sc) if s.t0 <= t + 1e-6); s = sc[i]; f = s.render(t)
        if s.trans == 'dissolve' and i > 0 and t < s.t0 + s.tdur:
            al = S.ease((t - s.t0) / s.tdur); f = sc[i - 1].render(t) * (1 - al) + f * al
        if s.out_white and t > s.t1 - s.out_white:
            al = S.ease((t - (s.t1 - s.out_white)) / s.out_white); f = f * (1 - al) + 255 * al
        if n % 15 == 0: out.append((t, Image.fromarray(np.clip(f, 0, 255).astype(np.uint8)).resize((240, 135))))
    for s in sc: s.close()
    return out
if __name__ == '__main__':
    wins = [tuple(map(float, w.split(':'))) for w in sys.argv[2:]]
    with Pool(4) as p: res = p.map(win, wins)
    fr = [x for r in res for x in r]; cols = 10; rows = (len(fr) + cols - 1) // cols
    sh = Image.new('RGB', (cols * 240, rows * 149), 'black'); d = ImageDraw.Draw(sh)
    for i, (t, im) in enumerate(fr):
        x, y = (i % cols) * 240, (i // cols) * 149; sh.paste(im, (x, y + 14)); d.text((x + 2, y + 1), f'{int(t//60)}:{t%60:04.1f}', fill='yellow')
    sh.save(sys.argv[1], quality=82)
