# measure.py <jpg...> : brightness (mean luma), warmth (mean R-B), centre/edge luma ratio (centre box x320-960 y180-540 vs the rest), saturation
import sys, numpy as np
from PIL import Image
def m(p):
    a = np.asarray(Image.open(p).convert('RGB').resize((1280, 720))).astype(float); L = a @ [0.299, 0.587, 0.114]
    c = np.zeros(L.shape, bool); c[180:540, 320:960] = True
    hsv = np.asarray(Image.open(p).convert('RGB').resize((1280, 720)).convert('HSV')).astype(float)
    return L.mean(), (a[..., 0] - a[..., 2]).mean(), L[c].mean() / L[~c].mean(), hsv[..., 1].mean()
if __name__ == '__main__':
    import glob
    rows = [(p, *m(p)) for a in sys.argv[1:] for p in sorted(glob.glob(a))]
    for r in rows: print('%-40s bright %5.1f warm %5.1f c/e %4.2f sat %5.1f' % (r[0][-40:], *r[1:]))
    if len(rows) > 3:
        v = np.array([r[1:] for r in rows]); print('MEDIAN bright %5.1f warm %5.1f c/e %4.2f sat %5.1f' % tuple(np.median(v, 0)))
        print('IQR    ', np.percentile(v, 25, 0).round(2), np.percentile(v, 75, 0).round(2))
