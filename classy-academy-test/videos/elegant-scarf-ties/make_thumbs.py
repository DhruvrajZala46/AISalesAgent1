# make_thumbs.py - the three thumbnails for "10 Elegant Ways to Tie a Scarf" (Classy Academy), 1920x1080 and 1280x720.
# Built on what 54 scarf thumbnails with 1M+ views do and 78 low-view ones from the same searches do not (THUMBNAIL.md):
#   many finished looks at once (5 or more: 17% against 1%), the head cropped so the scarf is the subject (31% against 15%),
#   a white or very light ground (37% against 15%), few words, the scarf held open by one woman (20% against 13%).
# usage (in a work folder that holds raw/<key>.mp4 of the video's clips and logo_ca_hires.png):
#   python3 make_thumbs.py [A B C]   -> S_A_the_set / S_B_one_scarf / S_C_one_knot (.jpg .png, both sizes) + layers/
import os, io, sys, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.environ.get('CA_FONTS', os.path.join(HERE, '..', '..', 'workflow', 'assets', 'fonts')) + '/'   # the fonts live in the repo
W, H, SS = 1920, 1080, 2
INK, CREAM, CRIMSON = (23, 17, 14), (250, 246, 240), (166, 24, 40)
# ---------- frames: the sharpest frame of a window of a clip that is in the video (SOURCES-LOG.md)
FRAMES = {'hero': ('t2c42', 1.0, 1.6), 'p1': ('t2c42', 10.3, 11.8), 'p1a': ('t2c42', 9.55, 9.66), 'p4': ('t2c42', 20.9, 22.2), 'p7': ('t2c42', 27.5, 28.5),     # one woman, one scarf: held open, ties 1, 4 and 7
          'k2': ('t1c32', 13.2, 14.2), 'k3': ('x5b5', 7.2, 7.9), 'k4': ('t5c27', 11.3, 12.5), 'k5': ('x6c9', 8.2, 8.9), 'k6': ('t1c30', 21.9, 24.2),
          'k8': ('t7a30', 8.7, 9.1), 'k9': ('t9a41', 6.4, 8.6), 'k10': ('t10b34', 36.0, 39.2)}                                        # the other finished ties
def sharp(im): return np.asarray(im.convert('L').filter(ImageFilter.FIND_EDGES), dtype=float).var()
def frame(name):
    f = name + '.png'
    if not os.path.exists(f):
        key, a, b = FRAMES[name]; best, t = None, a
        while t <= b:
            p = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f'raw/{key}.mp4', '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
            try:
                im = Image.open(io.BytesIO(p)).convert('RGB'); s = sharp(im)
                if best is None or s > best[0]: best = (s, t, im)
            except Exception: pass
            t += 0.1
        best[2].save(f); print(name, key, round(best[1], 2))
    return Image.open(f).convert('RGB')
def grade(im, bright=1.05, contrast=1.05, color=1.03):
    im = ImageEnhance.Brightness(im).enhance(bright); im = ImageEnhance.Contrast(im).enhance(contrast); return ImageEnhance.Color(im).enhance(color)
def cut(im, box, size, **g):       # box = (x0, y0, width) in source px; the height follows the panel's shape
    x0, y0, w = box; h = w * size[1] / size[0]; c = im.crop((int(x0), int(y0), int(x0 + w), int(y0 + h))).resize(size, Image.LANCZOS)
    s = w / size[0]; c = c.filter(ImageFilter.UnsharpMask(1.6, 70 if s < 0.95 else 35, 2)); print('   source px per output px', round(s, 2)); return grade(c, **g)
# ---------- drawn parts (all at 2x, then reduced)
def font(name, size, wght=None):
    f = ImageFont.truetype(FD + name, size)
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f
def capfont(name, cap, wght=None, probe='H'):
    for s in range(10, 900):
        f = font(name, s, wght); b = f.getbbox(probe)
        if b[3] - b[1] >= cap: return f
def text_w(d, t, f, track=0): return sum(d.textlength(c, font=f) for c in t) + track * (len(t) - 1)
def put(d, xy, t, f, fill, track=0, anchor='l'):   # baseline-free: xy = left (or centre) x and CAP TOP y
    x, y = xy; w = text_w(d, t, f, track); top = f.getbbox('H')[1]
    if anchor == 'm': x -= w / 2
    if anchor == 'r': x -= w
    for c in t: d.text((x, y - top), c, font=f, fill=fill); x += d.textlength(c, font=f) + track
    return w
def layer(): return Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0))
def down(l): return l.resize((W, H), Image.LANCZOS)
def shadow_of(l, blur=14, dx=0, dy=8, strength=0.45):
    a = l.split()[3].point(lambda v: int(v * strength)); a = ImageChops.offset(a, dx * SS, dy * SS).filter(ImageFilter.GaussianBlur(blur * SS))
    s = Image.new('RGBA', l.size, (10, 6, 4, 0)); s.putalpha(a); return s
def badge(cx, cy, d, big='2', small='MIN'):       # the black disc with a fine ring: the one time promise, the same on all three
    l = layer(); dr = ImageDraw.Draw(l); r = d / 2 * SS; cx, cy = cx * SS, cy * SS
    dr.ellipse((cx - r, cy - r, cx + r, cy + r), fill=INK + (255,))
    rr = r * 0.9; dr.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=CREAM + (255,), width=max(2, int(r * 0.022)))
    fb = capfont('Montserrat.ttf', int(r * 0.80), 800, '2'); fs = capfont('Montserrat.ttf', int(r * 0.23), 700)
    put(dr, (cx, cy - r * 0.62), big, fb, CREAM + (255,), anchor='m'); put(dr, (cx + r * 0.02, cy + r * 0.34), small, fs, CREAM + (255,), track=r * 0.07, anchor='m')
    return [shadow_of(l, 16, 0, 10, 0.5), l]
def arrow(p0, p1, bend=0.0, width=30, head=2.5, color=CRIMSON, edge=7):   # a curved arrow, cream edge, soft shadow
    (x0, y0), (x1, y1) = [(p[0] * SS, p[1] * SS) for p in (p0, p1)]; w = width * SS
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2; nx, ny = -(y1 - y0), (x1 - x0); cxp, cyp = mx + nx * bend, my + ny * bend
    pts = [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * cxp + t * t * x1, (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cyp + t * t * y1) for t in np.linspace(0, 1, 120)]
    tx, ty = pts[-1][0] - pts[-8][0], pts[-1][1] - pts[-8][1]; n = (tx * tx + ty * ty) ** 0.5; tx, ty = tx / n, ty / n; hl = w * head
    bx, by = pts[-1][0] - tx * hl * 0.9, pts[-1][1] - ty * hl * 0.9; body = [p for p in pts if (p[0] - pts[-1][0]) ** 2 + (p[1] - pts[-1][1]) ** 2 > (hl * 0.85) ** 2] + [(bx, by)]
    m = Image.new('L', (W * SS, H * SS), 0); dm = ImageDraw.Draw(m); dense = []
    for (ax, ay), (bx2, by2) in zip(body, body[1:]):
        n2 = max(2, int(((bx2 - ax) ** 2 + (by2 - ay) ** 2) ** 0.5 / 2)); dense += [(ax + (bx2 - ax) * i / n2, ay + (by2 - ay) * i / n2) for i in range(n2 + 1)]
    for qx, qy in dense: dm.ellipse((qx - w / 2, qy - w / 2, qx + w / 2, qy + w / 2), fill=255)
    px, py = -ty, tx; dm.polygon([(pts[-1][0] + tx * hl * 0.1, pts[-1][1] + ty * hl * 0.1), (bx + px * hl * 0.62, by + py * hl * 0.62), (bx - px * hl * 0.62, by - py * hl * 0.62)], fill=255)
    out = m.filter(ImageFilter.MaxFilter(2 * edge * SS // 2 * 2 + 1)); e = Image.new('RGBA', m.size, CREAM + (0,)); e.putalpha(out); f = Image.new('RGBA', m.size, color + (0,)); f.putalpha(m)
    return [shadow_of(e, 10, 0, 6, 0.4), e, f]
def logo(dark, xy=(57, 48), h=141):
    L = Image.open('logo_ca_hires.png').convert('RGBA'); L = L.resize((round(L.width * h / L.height), h), Image.LANCZOS)
    c = Image.new('RGBA', L.size, (INK if dark else CREAM) + (0,)); c.putalpha(L.split()[3].point(lambda v: int(v * 0.95))); l = Image.new('RGBA', (W, H), (0, 0, 0, 0)); l.paste(c, xy, c); return l
def finish(name, base, layers):
    out = base.convert('RGBA'); os.makedirs('layers', exist_ok=True); base.save(f'layers/{name}_1_photos.png')
    for i, l in enumerate(layers):
        if l.size != (W, H): l = down(l)
        l.save(f'layers/{name}_{i + 2}.png'); out = Image.alpha_composite(out, l)
    out = out.convert('RGB'); out.save(name + '_1920x1080.png'); out.save(name + '_1920x1080.jpg', quality=93)
    out.resize((1280, 720), Image.LANCZOS).save(name + '_1280x720.jpg', quality=93); print(name, 'done'); return out
def dividers(base, xs, w=10):
    d = ImageDraw.Draw(base)
    for x in xs: d.rectangle((x - w // 2, 0, x + w // 2 - 1, H), fill=CREAM)

def logo_shade(strength=0.42):      # a soft dark corner behind the cream logo, as on the channel's own thumbnails
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).ellipse((-170, -190, 420, 330), fill=int(255 * strength)); m = m.filter(ImageFilter.GaussianBlur(70))
    s = Image.new('RGBA', (W, H), INK + (0,)); s.putalpha(m); return s
def hlines(base, ys, w=8):
    d = ImageDraw.Draw(base)
    for y in ys: d.rectangle((0, y - w // 2, W, y + w // 2 - 1), fill=CREAM)
# every crop starts at the lips: the scarf is the subject, no eyes (31% of the 1M+ thumbnails against 15% of the low-view ones)
# ---------- A. the set: all ten finished ties, five by two; one small disc gives the count
GRID = [('p1a', (168, 318, 384)), ('k4', (40, 140, 620)), ('k5', (60, 180, 620)), ('k3', (130, 430, 400)), ('k2', (160, 60, 560)),
        ('p7', (110, 360, 460)), ('k6', (80, 385, 420)), ('k9', (100, 0, 620)), ('k8', (40, 275, 440)), ('k10', (50, 470, 560))]
def thumb_A(disc=True):
    base = Image.new('RGB', (W, H), CREAM); pw, ph = 384, 540
    for i, (n, box) in enumerate(GRID):
        base.paste(cut(frame(n), box, (pw, ph), bright=1.04), ((i % 5) * pw, (i // 5) * ph))
    dividers(base, (384, 768, 1152, 1536), 8); hlines(base, (540,), 8)
    return finish('S_A_the_set', base, (badge(960, 540, 250, '10', 'WAYS') if disc else []) + [logo_shade(), logo(False)])
# ---------- B. one scarf: one woman holds it open, then wears it three ways; a cream band names the promise
def thumb_B():
    base = Image.new('RGB', (W, H), CREAM)
    base.paste(cut(frame('hero'), (0, 0, 720), (720, H), bright=1.03), (0, 0))
    for i, (n, x0) in enumerate((('p1', 20), ('p4', 160), ('p7', 170))):
        base.paste(cut(frame(n), (x0, 0, 400), (400, H), bright=1.03), (720 + i * 400, 0))
    dividers(base, (720,), 12); dividers(base, (1120, 1520), 8)
    band = layer(); d = ImageDraw.Draw(band); y0 = 834 * SS; d.rectangle((0, y0, W * SS, H * SS), fill=CREAM + (255,))
    fb = capfont('Montserrat.ttf', 106 * SS, 800)
    x = 74 * SS; w1 = put(d, (x, y0 + 70 * SS), '1 SCARF.', fb, INK + (255,), track=2 * SS); put(d, (x + w1 + 56 * SS, y0 + 70 * SS), '10 WAYS.', fb, CRIMSON + (255,), track=2 * SS)
    return finish('S_B_one_scarf', base, [shadow_of(band, 18, 0, -6, 0.25), band] + arrow((648, 452), (796, 452), 0, 28) + [logo(True)])
# ---------- C. three knots: three finished ties, large, in the channel's own three tall panels; no words
def thumb_C():
    base = Image.new('RGB', (W, H), CREAM); pw = 640
    for i, (n, box) in enumerate((('k5', (50, 180, 640)), ('k4', (40, 140, 640)), ('k2', (80, 60, 640)))):
        base.paste(cut(frame(n), box, (pw, H), bright=1.09, contrast=1.03), (i * pw, 0))
    dividers(base, (640, 1280), 10)
    return finish('S_C_three_knots', base, [logo_shade(0.5), logo(False)])
if __name__ == '__main__':
    for k in (sys.argv[1:] or 'ABC'): {'A': thumb_A, 'B': thumb_B, 'C': thumb_C}[k]()
