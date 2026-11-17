# make_thumbs_v2.py - the three v2 thumbnails for "10 Easy, Elegant 2-Minute Hairstyles" (Classy Academy), 1920x1080 and 1280x720.
# Built on what 262 hair thumbnails with 1M+ views do and 84 low-view ones do not (THUMBNAIL.md, section A):
#   bright, the hair itself large and seen from behind, a step or a set of results, few words in one compact label, no face.
# usage (in a work folder that holds raw/<key>.mp4 of the video's clips, twist3_1.jpg and logo_ca_hires.png):
#   python3 make_thumbs_v2.py            -> V2_A_three_steps / V2_B_the_set / V2_C_one_clip (.jpg .png, both sizes) + layers/
import os, io, sys, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.path.join(HERE, '..', '..', 'workflow', 'assets', 'fonts') + '/'
W, H, SS = 1920, 1080, 2
INK, CREAM, CRIMSON = (23, 17, 14), (250, 246, 240), (166, 24, 40)
# ---------- frames: the sharpest frame of a window of a clip that is in the video (SOURCES-LOG.md)
FRAMES = {'s1b15_b': ('s1b15', 0.9, 2.2), 's1b15_s': ('s1b15', 6.2, 7.0), 's1b15_a': ('s1b15', 8.6, 9.9),    # style 1, the French twist in one clip
          'sleek_a': ('hv_chignon18', 43.0, 44.8), 'chig_a': ('hv_chignon38', 18.6, 20.9), 'pony_a': ('s2b23', 15.2, 16.4)}  # styles 6, 4 and 2
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
# ---------- A. three steps: before -> the clip going in -> after (one woman, one reel, the French twist in one clip)
def thumb_A():
    base = Image.new('RGB', (W, H), CREAM); pw = 640
    for i, (n, box) in enumerate((('s1b15_b', (40, 118, 640)), ('s1b15_s', (40, 118, 640)), ('s1b15_a', (75, 160, 640)))):
        base.paste(cut(frame(n), box, (pw, H), bright=1.09), (i * pw, 0))
    dividers(base, (640, 1280))
    L = arrow((556, 590), (724, 590), 0, 34) + arrow((1196, 590), (1364, 590), 0, 34) + badge(960, 880, 300)
    return finish('V2_A_three_steps', base, L + [logo(True)])
# ---------- B. the set: four finished styles from behind, one band that names the set
def thumb_B():
    base = Image.new('RGB', (W, H), CREAM); pw = 480
    for i, (im, box) in enumerate(((frame('chig_a'), (6, 0, 569)), (frame('sleek_a'), (92, 106, 522)), (frame('pony_a'), (135, 18, 480)), (frame('s1b15_a'), (160, 184, 480)))):
        base.paste(cut(im, box, (pw, H)), (i * pw, 0))
    dividers(base, (480, 960, 1440), 8)
    band = layer(); d = ImageDraw.Draw(band); y0 = 842 * SS; d.rectangle((0, y0, W * SS, H * SS), fill=CREAM + (255,))
    f10 = capfont('Montserrat.ttf', 150 * SS, 800, '1'); fs = capfont('CormorantSC-Regular.ttf', 40 * SS, None, 'E'); fb = capfont('Montserrat.ttf', 92 * SS, 800)
    x = 70 * SS; w10 = put(d, (x, y0 + 44 * SS), '10', f10, CRIMSON + (255,)); x += w10 + 34 * SS
    put(d, (x + 4 * SS, y0 + 44 * SS), 'Easy, Elegant', fs, INK + (255,), track=5 * SS); put(d, (x, y0 + 102 * SS), 'HAIRSTYLES', fb, INK + (255,), track=2 * SS)
    return finish('V2_B_the_set', base, [shadow_of(band, 18, 0, -6, 0.25), band] + badge(1480, 850, 300) + [logo(False)])
# ---------- C. one clip: one large finished French twist, the wall carried on to the left for the words
def thumb_C():
    src = Image.open('twist3_1.jpg').convert('RGB'); s = 0.87; ch = int(H / s); cw = int(ch * 1169 / H) if False else min(src.width - 11, int(1169 / s))
    ph = src.crop((11, 143, 11 + cw, 143 + ch)).resize((round(cw * s), H), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.6, 60, 2)); x0 = W - ph.width + 96
    a = np.asarray(ph, dtype=float); col = np.median(a[:, 2:26, :], axis=1); col = cv2.GaussianBlur(col.reshape(H, 1, 3).astype(np.float32), (1, 0), 40).reshape(H, 3)   # the wall, row by row
    wall = np.repeat(col[:, None, :], W, axis=1); base = Image.fromarray(np.clip(wall, 0, 255).astype(np.uint8)); base.paste(ph, (x0, 0))
    seam = np.asarray(base, dtype=float); k = 90; ramp = np.linspace(0, 1, k)[None, :, None]; seam[:, x0:x0 + k, :] = wall[:, x0:x0 + k, :] * (1 - ramp) + a[:, :k, :] * ramp
    base = grade(Image.fromarray(np.clip(seam, 0, 255).astype(np.uint8)), 1.04, 1.05, 1.04); print('   source px per output px', round(1 / s, 2))
    t = layer(); d = ImageDraw.Draw(t); fs = capfont('CormorantSC-Regular.ttf', 46 * SS, None, 'E'); fb = capfont('Montserrat.ttf', 162 * SS, 800)
    x = 90 * SS; put(d, (x + 6 * SS, 372 * SS), 'Elegant Hair', fs, INK + (255,), track=7 * SS)
    w1 = put(d, (x, 456 * SS), '1 CLIP.', fb, INK + (255,), track=2 * SS); put(d, (x, 668 * SS), '2 MIN.', fb, CRIMSON + (255,), track=2 * SS)
    return finish('V2_C_one_clip', base, [t] + arrow((790, 428), (1470, 292), -0.2, 22, 2.6) + [logo(True)])
if __name__ == '__main__':
    for k in (sys.argv[1:] or 'ABC'): {'A': thumb_A, 'B': thumb_B, 'C': thumb_C}[k]()
