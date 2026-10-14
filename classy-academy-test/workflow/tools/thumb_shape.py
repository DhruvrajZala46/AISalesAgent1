# thumb_shape.py - the body-shape winners' thumbnail in our look: the same woman, mistake -> fix (red cross / green
# tick), with the shape lines drawn ON her body, words in the middle. Built on thumb_xo.py (caramel backdrop,
# Montserrat + Cormorant SC, red underline, CE logo).
# Proof (body-shape winners, Oct 2026, videos/body-shape/THUMBNAIL.md): same woman mistake -> fix 67.5x her channel's
# median, same woman + lines drawn on her body 56.8x (1.84M median views), shape icons/diagrams 14.0x.
# usage (inside the thumbnail folder):
#   U2NET_HOME=<models dir> python3 thumb_shape.py spec.json
# spec.json: {"out": "A.jpg", "left": "before.png", "right": "after.png", "crop": [y_bottom_left, y_bottom_right],
#             "top": "IT'S NOT", "big": "YOU", "small": "*it's the cut*",
#             "lines": [{"pts": [[x,y],...], "dash": true, "w": 7}, ...],   # canvas coords (1280x720)
#             "tags": [{"text": "hangs straight", "x": 200, "y": 600}], "grid": false}
# Only draw what the woman shows or says herself (her own before/after, her own explanation).
import os, sys, json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thumb_xo as X
W, H = X.W, X.H

def person(path, crop_y, cx, head_y=22):
    im = Image.open(path).convert('RGB')
    if crop_y and crop_y > 0: im = im.crop((0, 0, im.width, crop_y))
    im = X.cutout(im); im = im.crop(im.getbbox())
    s = (H - head_y) / im.height; im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    return im, (round(cx - im.width / 2), head_y)

def dashed(d, pts, w, dash=26, gap=16, fill=(255, 255, 255, 255)):
    seg = []; on = True; left = dash
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        L = float(np.hypot(x1 - x0, y1 - y0)); t = 0.0
        while t < L:
            step = min(left, L - t); a = (x0 + (x1 - x0) * t / L, y0 + (y1 - y0) * t / L)
            b = (x0 + (x1 - x0) * (t + step) / L, y0 + (y1 - y0) * (t + step) / L)
            if on: d.line((a, b), fill=fill, width=w)
            t += step; left -= step
            if left <= 1e-6: on = not on; left = dash if on else gap

def smooth(pts, n=12):
    """Catmull-Rom through the points so a waist curve reads as a body line, not a zig-zag."""
    if len(pts) < 3: return pts
    P = [pts[0]] + pts + [pts[-1]]; out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = map(np.array, P[i - 1:i + 3])
        for t in np.linspace(0, 1, n, endpoint=False):
            out.append(tuple(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3)))
    return out + [pts[-1]]

def build(spec):
    c = X.backdrop().convert('RGBA')
    cl, cr = spec.get('crop', [0, 0])
    for k, (path, cy, cx) in enumerate(((spec['left'], cl, 205), (spec['right'], cr, W - 205))):
        im, (x, y) = person(path, cy, cx)
        c.alpha_composite(X.shadow(im), (x + 10 - X.PAD, y + 12 - X.PAD)); c.alpha_composite(im, (x, y))
    # the shape lines, drawn on her (soft shadow first so they hold on light clothes)
    ln = Image.new('RGBA', (W, H), (0, 0, 0, 0)); shd = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    dl, ds = ImageDraw.Draw(ln), ImageDraw.Draw(shd)
    for L in spec.get('lines', []):
        pts = [tuple(p) for p in L['pts']]; pts = smooth(pts) if L.get('curve') else pts; w = L.get('w', 7)
        col = tuple(L.get('color', (255, 255, 255))) + (255,)
        if L.get('dash', True): dashed(dl, pts, w, fill=col); dashed(ds, [(a + 2, b + 3) for a, b in pts], w + 4, fill=(30, 15, 5, 150))
        else: dl.line(pts, fill=col, width=w, joint='curve'); ds.line([(a + 2, b + 3) for a, b in pts], fill=(30, 15, 5, 150), width=w + 4)
    c.alpha_composite(shd.filter(ImageFilter.GaussianBlur(4))); c.alpha_composite(ln)
    for t in spec.get('tags', []):                       # small white pill labels, like the video's tags
        f = X.font(X.FD + 'PlayfairDisplay-Regular.ttf' if os.path.exists(X.FD + 'PlayfairDisplay-Regular.ttf') else X.FD + 'CormorantSC-Regular.ttf', t.get('size', 30))
        d = ImageDraw.Draw(c); bb = d.textbbox((t['x'], t['y']), t['text'], font=f, anchor='mm')
        d.rounded_rectangle((bb[0] - 16, bb[1] - 9, bb[2] + 16, bb[3] + 11), radius=22, fill=(255, 255, 255, 240))
        d.text((t['x'], t['y']), t['text'], font=f, fill=(60, 40, 30), anchor='mm')
    for k, cx in ((0, 205), (1, W - 205)):
        b = X.badge('no' if k == 0 else 'yes'); bx = spec.get('badge_x', [cx + 70, cx - 70 - 118])[k]
        c.alpha_composite(b, (bx, spec.get('badge_y', 40)))
    tmp = spec['out'] + '.base.png'; c.convert('RGB').save(tmp)
    text_block(c, spec.get('top', ''), spec['big'], spec.get('small', ''), spec.get('text_w', 480))
    if spec.get('grid'):
        d = ImageDraw.Draw(c)
        for v in range(0, W, 50): d.line((v, 0, v, H), fill=(0, 255, 255, 120) if v % 100 == 0 else (255, 255, 0, 80))
        for v in range(0, H, 50): d.line((0, v, W, v), fill=(0, 255, 255, 120) if v % 100 == 0 else (255, 255, 0, 80))
        for v in range(0, W, 100): d.text((v + 2, 2), str(v), fill='red')
        for v in range(0, H, 100): d.text((2, v + 2), str(v), fill='red')
    os.remove(tmp); c.convert('RGB').save(spec['out'], quality=95); return spec['out']

def text_block(c, top, big, small, spec_w=480):
    """The same centred text block as thumb_xo.build (thin line over a huge bold word when big has no top)."""
    FD = X.FD
    if top:
        fb = X.fit(FD + 'Montserrat.ttf', big, 168, spec_w, 800, 'N'); cb = fb.getbbox('N')[3] - fb.getbbox('N')[1]
        ft = X.fit(FD + 'Montserrat.ttf', top, min(74, int(cb * 0.72)), spec_w, 300, 'N')        # the bold word always leads
    else:
        ft = None; fb = X.fit(FD + 'Montserrat.ttf', big, 132, spec_w, 800, 'N')
    fs = X.fit(FD + 'CormorantSC-Regular.ttf', small, 34, spec_w, probe='A') if small else None
    lines = ([(ft, top, 0)] if top else []) + [(fb, big, 1)] + ([(fs, small, 2)] if small else [])
    hs = [f.getbbox(t)[3] - f.getbbox(t)[1] for f, t, _ in lines]
    total = sum(hs) + (len(lines) - 1) * 36; y = (H - total) / 2 + 10; pos = []
    for (f, t, k), h in zip(lines, hs): pos.append((f, t, k, y - f.getbbox(t)[1])); y += h + (28 if k == 0 else 46)
    shl = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(shl)
    for f, t, k, yy in pos: ds.text((W / 2 + 3, yy + 5), t, font=f, fill=210, anchor='ma')
    dark = Image.new('RGBA', (W, H), (52, 26, 10, 0)); dark.putalpha(shl.filter(ImageFilter.GaussianBlur(8))); c.alpha_composite(dark)
    d = ImageDraw.Draw(c)
    for f, t, k, yy in pos: d.text((W / 2, yy), t, font=f, fill=(255, 255, 255), anchor='ma')
    f, t, k, yy = [p for p in pos if p[2] == 1][0]; bb = d.textbbox((W / 2, yy), t, font=f, anchor='ma')
    fw = d.textlength(t.split()[0], font=f)
    d.rectangle((bb[0] + 6, bb[3] + 14, bb[0] + fw - 2, bb[3] + 19), fill=(150, 22, 26))      # the channel's red underline
    lg = Image.open(X.LOGO).convert('RGBA'); lg.thumbnail((92, 92), Image.LANCZOS); c.alpha_composite(lg, (W // 2 - lg.width // 2, 18))

if __name__ == '__main__':
    print('ok', build(json.load(open(sys.argv[1]))))
