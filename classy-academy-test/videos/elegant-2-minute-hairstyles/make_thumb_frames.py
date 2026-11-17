# make_thumb_frames.py - the nine stills behind the three Classy Academy thumbnails (12 Nov 2026).
# Every still is a frame of a clip that is in the video itself (SOURCES-LOG.md), so the thumbnail shows what the viewer gets.
# usage (inside a work folder holding raw/<key>.mp4): python3 make_thumb_frames.py
#   then: python3 workflow/tools/thumb_ca_real.py thumb_spec_ca.json   -> H1/H2/H3 .jpg + editable layers
import subprocess, io, numpy as np, cv2
from PIL import Image, ImageFilter
# name: (clip key, first second, last second) - the sharpest frame in that window is kept
FRAMES = {'din13': ('cv_dinner13', 28.4, 29.9), 'pinf': ('s10b30', 0.0, 1.4), 'tw_c': ('hv_twist13', 19.4, 20.9),      # H1
          'chig38': ('hv_chignon38', 18.8, 20.8), 'pony': ('s2b23', 15.0, 16.3), 'din43f': ('cv_dinner43', 0.0, 0.6),  # H2
          'tw_a': ('hv_twist13', 2.3, 3.1), 'tw_b': ('hv_twist13', 8.6, 10.2), 'tw_c2': ('hv_twist13', 17.4, 18.6)}   # H3
# the one retouch: the lettering on a framed wall sign behind the French twist clip is painted out (wall only; hair untouched)
SIGN = {'tw_a': ([(402, 310, 470, 354), (470, 310, 494, 336)], 40), 'tw_b': ([(468, 296, 500, 330)], 30),
        'tw_c2': ([(196, 298, 236, 334)], 30), 'tw_c': ([(190, 282, 214, 312)], 30)}
def sharp(im): return np.asarray(im.convert('L').filter(ImageFilter.FIND_EDGES), dtype=float).var()
for name, (key, a, b) in FRAMES.items():
    best, t = None, a
    while t <= b:
        p = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f'raw/{key}.mp4', '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        try:
            im = Image.open(io.BytesIO(p)).convert('RGB'); s = sharp(im)
            if best is None or s > best[0]: best = (s, t, im)
        except Exception: pass
        t += 0.1
    best[2].save(f'{name}.png'); print(name, key, round(best[1], 2))
for name, (rects, thr) in SIGN.items():
    im = cv2.imread(name + '.png'); g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(int); mask = np.zeros(g.shape, np.uint8)
    for x0, y0, x1, y1 in rects:
        reg = g[y0:y1, x0:x1]; m = (reg < np.percentile(reg, 85) - thr).astype(np.uint8) * 255
        mask[y0:y1, x0:x1] = np.maximum(mask[y0:y1, x0:x1], m)
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8)); cv2.imwrite(name + '_c.png', cv2.inpaint(im, mask, 5, cv2.INPAINT_TELEA))
