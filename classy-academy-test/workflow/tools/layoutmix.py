# layoutmix.py - share of each layout in a video, measured the same way for the original and ours (final review, FAILURE-ANALYSIS.md 7G).
#   python3 layoutmix.py ref <dir with sheet00..03.png from the YouTube storyboard sb0> [v]
#   python3 layoutmix.py p2  <dir with hyperframes snapshots frame-*-at-*s.png> [v]      (v = list every frame)
# Pixel rules only: check the per-frame list by eye (a full-screen clip with a peach wall can read as caramel).
# classify frames by layout with ONE rule set, for both videos (same 160x90 scale):
# white card / cream screen (+ whether a clip is framed on it) / caramel backdrop (+ panel) / full-screen footage
import sys, glob, re
import numpy as np
from PIL import Image

def tiles_ref(d, n):
    out = []
    for s in range(4):
        im = Image.open(f'{d}/sheet{s:02d}.png').convert('RGB')
        for r in range(5):
            for c in range(5):
                out.append(im.crop((c * 160, r * 90, c * 160 + 160, r * 90 + 90)))
    return [(k * 4.948, t) for k, t in enumerate(out[:n])]

def tiles_p2(d):
    fs = glob.glob(f'{d}/frame-*-at-*s.png')
    return sorted((float(re.search(r'at-([\d.]+)s', f).group(1)), Image.open(f).convert('RGB').resize((160, 90))) for f in fs)

def kind(im):
    a = np.asarray(im).astype(int)
    edge = np.concatenate([a[2:8, 20:140].reshape(-1, 3), a[-8:-2, 20:140].reshape(-1, 3), a[20:70, -8:-2].reshape(-1, 3)])
    r, g, b = np.median(edge, 0)
    centre = a[25:70, 20:140].reshape(-1, 3)
    def frac_like(px, col, tol=18): return (np.abs(px - col).max(1) < tol).mean()
    if r > 238 and g > 238 and b > 232 and abs(r - b) < 10:
        bg = 'white'
    elif r > 225 and g > 215 and b > 200 and r - b > 8 and r - b < 35:
        bg = 'cream'
    elif r > 150 and r - b > 55 and g < r - 20:
        bg = 'caramel'
    else:
        return 'full-screen'
    clip = 1 - frac_like(centre, np.array([r, g, b]), 30)
    if bg in ('white', 'cream'):
        return f'{bg}+clip' if clip > 0.25 else f'{bg} (text/blank)'
    return 'caramel+clip' if clip > 0.25 else 'caramel (text/blank)'

if __name__ == '__main__':
    which = sys.argv[1]
    fr = tiles_ref(sys.argv[2], 97) if which == 'ref' else tiles_p2(sys.argv[2])
    from collections import Counter
    ks = [(t, kind(im)) for t, im in fr]
    c = Counter(k for _, k in ks); n = len(ks)
    for k, v in c.most_common(): print(f'{k:24s} {v:4d}  {100 * v / n:5.1f}%')
    if len(sys.argv) > 3:
        for t, k in ks: print(f'{int(t // 60)}:{t % 60:04.1f} {k}')
