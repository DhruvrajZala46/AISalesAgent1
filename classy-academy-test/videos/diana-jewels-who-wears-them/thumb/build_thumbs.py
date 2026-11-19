# build_thumbs.py - thumbnails for "Princess Diana's 7 Jewels: Who Wears Them Now?" (19 Nov 2026)
# A: her face | the jewel, huge, in the centre | the woman who wears it now. No words.
#    (the formula of "The 15 Most Beautiful Royal Necklaces", 898,000 views, 816x its channel, and "The 10 Most EXPENSIVE
#    Royal Jewelry", 126x: two faces at the edges, one giant jewel in the middle, dark rich background, no words)
# B: the same formula with the Lover's Knot tiara and three words.
# C: Diana in the centre with her jewels laid out around her on dark velvet, two words
#    (the formula of "Princess Diana's Most Legendary Jewels", 789,806 views, 259x, and Elizabeth Taylor's jewels, 301x).
# Run inside the work folder (cdj):  python3 build_thumbs.py  -> thumb/A_ring.jpg, B_tiara.jpg, C_her_jewels.jpg (1920x1080)
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
W, H = 1920, 1080
FD = 'fonts/'
LOGO = '/home/user/AISalesAgent1/classy-academy-test/workflow/assets/logo_ca.png'
os.makedirs('thumb', exist_ok=True)

def bg(c0=(14, 20, 44), c1=(2, 3, 10), glow=(60, 90, 170), gpos=(0.5, 0.5), gsize=0.42):
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    d = np.sqrt(((xx / W - gpos[0]) / 0.75) ** 2 + ((yy / H - gpos[1]) / 0.75) ** 2)
    base = np.array(c0)[None, None] * (1 - np.clip(d, 0, 1)[..., None]) + np.array(c1)[None, None] * np.clip(d, 0, 1)[..., None]
    g = np.exp(-(((xx / W - gpos[0]) / gsize) ** 2 + ((yy / H - gpos[1]) / (gsize * 1.25)) ** 2))
    base = base + np.array(glow)[None, None] * g[..., None] * 0.9
    noise = np.random.default_rng(3).normal(0, 2.2, (H, W, 1))
    return Image.fromarray(np.clip(base + noise, 0, 255).astype('uint8'))

def cut_plain(path, crop=None, tol=28, dark=False):
    """cut a jewel off a plain white (or dark) studio background"""
    im = Image.open(path).convert('RGB')
    if crop: w, h = im.size; im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
    a = np.array(im).astype(float)
    refs = [np.median(x.reshape(-1, 3), 0) for x in (a[:6], a[-6:], a[:, :6], a[:, -6:], a[:6, :len(a[0]) // 3], a[-6:, :len(a[0]) // 3])]
    d = np.min([np.sqrt(((a - r) ** 2).sum(2)) for r in refs], 0)
    # also accept a smooth vertical gradient: compare each pixel with the left/right border colour of its own row
    rowref = (a[:, :8].mean(1) + a[:, -8:].mean(1)) / 2
    d = np.minimum(d, np.sqrt(((a - rowref[:, None, :]) ** 2).sum(2)))
    from scipy import ndimage
    near = d < tol
    lab, n = ndimage.label(near)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bgm = np.isin(lab, list(edge))
    alpha = (~bgm).astype(float)
    if dark: alpha[np.array(im.convert('L')) < 70] = 0
    alpha = ndimage.binary_opening(alpha > 0, iterations=1)
    lab2, n2 = ndimage.label(alpha)
    if n2 > 1:
        sizes = ndimage.sum(alpha, lab2, range(1, n2 + 1)); big = sizes.max()
        alpha = np.isin(lab2, [i + 1 for i, z in enumerate(sizes) if z > 0.2 * big])
    alpha = alpha.astype(float)
    al = Image.fromarray((alpha * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2))
    out = im.copy(); out.putalpha(al)
    return out.crop(out.getbbox())

def feathered(path, box):
    im = Image.open(path).convert('RGB'); sw, sh_ = im.size
    c = im.crop((int(box[0] * sw), int(box[1] * sh_), int(box[2] * sw), int(box[3] * sh_)))
    w, h = c.size; yy, xx = np.mgrid[0:h, 0:w]
    m = np.clip(1.25 - np.sqrt(((xx - w / 2) / (w * 0.5)) ** 2 + ((yy - h * 0.45) / (h * 0.55)) ** 2) * 1.25, 0, 1) ** 1.2
    c = c.convert('RGBA'); c.putalpha(Image.fromarray((m * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(8))); return c

def face_panel(path, box, w, h, fade='right', strength=1.0):
    im = Image.open(path).convert('RGB'); sw, sh_ = im.size
    c = im.crop((int(box[0] * sw), int(box[1] * sh_), int(box[2] * sw), int(box[3] * sh_)))
    c = c.resize((w, h), Image.LANCZOS)
    c = ImageEnhance.Contrast(c).enhance(1.06); c = ImageEnhance.Color(c).enhance(1.08); c = ImageEnhance.Sharpness(c).enhance(1.2)
    m = np.ones((h, w))
    ramp = np.linspace(0, 1, int(w * 0.38))
    if fade == 'right': m[:, w - len(ramp):] = ramp[::-1][None, :] ** 1.4
    else: m[:, :len(ramp)] = ramp[None, :] ** 1.4
    vb = np.linspace(0, 1, int(h * 0.18)); m[h - len(vb):, :] *= vb[::-1][:, None] ** 0.8 * 0.6 + 0.4
    return c, Image.fromarray((m * 255 * strength).astype('uint8'))

def hero(canvas, jewel, cx, cy, hh, glow=(120, 160, 255), rot=0):
    j = jewel.rotate(rot, resample=Image.BICUBIC, expand=True) if rot else jewel
    s = hh / j.height; j = j.resize((int(j.width * s), hh), Image.LANCZOS)
    x0, y0 = int(cx - j.width / 2), int(cy - j.height / 2)
    a = j.split()[3]
    # glow behind the jewel
    gl = Image.new('L', (W, H), 0); gl.paste(a, (x0, y0)); gl = gl.filter(ImageFilter.GaussianBlur(60)).point(lambda v: int(v * 0.85))
    canvas.paste(Image.new('RGB', (W, H), glow), (0, 0), gl)
    # soft drop shadow
    sh = Image.new('L', (W, H), 0); sh.paste(a, (x0 + 14, y0 + 26)); sh = sh.filter(ImageFilter.GaussianBlur(22)).point(lambda v: int(v * 0.7))
    canvas.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), sh)
    rgb = ImageEnhance.Contrast(j.convert('RGB')).enhance(1.12); rgb = ImageEnhance.Brightness(rgb).enhance(1.05)
    rgb = ImageEnhance.Sharpness(rgb).enhance(1.4)
    canvas.paste(rgb, (x0, y0), a)
    return (x0, y0, j.width, j.height)

def sparkle(canvas, pts, r=46):
    lay = Image.new('L', (W, H), 0); d = ImageDraw.Draw(lay)
    for x, y, k in pts:
        rr = int(r * k)
        d.polygon([(x, y - rr), (x + rr * 0.12, y - rr * 0.12), (x + rr, y), (x + rr * 0.12, y + rr * 0.12), (x, y + rr), (x - rr * 0.12, y + rr * 0.12), (x - rr, y), (x - rr * 0.12, y - rr * 0.12)], fill=255)
        d.ellipse((x - rr * 0.18, y - rr * 0.18, x + rr * 0.18, y + rr * 0.18), fill=255)
    canvas.paste(Image.new('RGB', (W, H), (255, 255, 255)), (0, 0), lay.filter(ImageFilter.GaussianBlur(1.6)))
    canvas.paste(Image.new('RGB', (W, H), (200, 220, 255)), (0, 0), lay.filter(ImageFilter.GaussianBlur(9)).point(lambda v: v // 2))

def vignette(canvas, k=90):
    yy, xx = np.mgrid[0:H, 0:W]; d = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H / 2) / (H * 0.62)) ** 2)
    canvas.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), Image.fromarray(np.clip((d - 0.78) * 300, 0, k).astype('uint8')).filter(ImageFilter.GaussianBlur(50)))

def words(canvas, txt, cx, y, size=150, color=(255, 255, 255), stroke=(10, 10, 25), font='Montserrat.ttf', weight=None):
    f = ImageFont.truetype(FD + font, size)
    try:
        if weight: f.set_variation_by_axes([weight])
    except Exception: pass
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).text((cx + 6, y + 10), txt, font=f, fill=230, anchor='ma')
    canvas.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), sh.filter(ImageFilter.GaussianBlur(12)))
    ImageDraw.Draw(canvas).text((cx, y), txt, font=f, fill=color, anchor='ma', stroke_width=4, stroke_fill=stroke)

def logo(canvas):
    lg = Image.open(LOGO).convert('RGBA'); s = 120 / lg.height; lg = lg.resize((int(lg.width * s), 120), Image.LANCZOS)
    canvas.paste(lg, (36, 26), lg)

def build_A():
    cv = bg()
    d, dm = face_panel('assets/pengage_2.jpg', (0.0, 0.02, 0.86, 0.80), 760, 1080, 'right')
    cv.paste(d, (0, 0), dm)
    k, km = face_panel('assets/pwkengage_17.jpg', (0.44, 0.10, 1.0, 0.68), 740, 1080, 'left')
    cv.paste(k, (W - 740, 0), km)
    ring = cut_plain('assets/pengage_46.jpg', crop=(0.0, 0.0, 1.0, 0.64), tol=24)
    x0, y0, w, h = hero(cv, ring, W / 2, H / 2 + 20, 820, glow=(70, 110, 255), rot=-8)
    sparkle(cv, [(x0 + w * 0.30, y0 + h * 0.12, 1.0), (x0 + w * 0.78, y0 + h * 0.30, 0.7), (x0 + w * 0.20, y0 + h * 0.62, 0.55)])
    vignette(cv); logo(cv)
    cv.save('thumb/A_ring.jpg', quality=94); return cv

def build_B():
    cv = bg(c0=(26, 22, 30), glow=(150, 140, 120), gsize=0.40)
    d, dm = face_panel('assets/pknot_16.jpg', (0.02, 0.0, 1.0, 0.72), 720, 1080, 'right')
    cv.paste(d, (0, 0), dm)
    k, km = face_panel('assets/pkateknot_12.jpg', (0.0, 0.0, 1.0, 0.75), 720, 1080, 'left')
    cv.paste(k, (W - 720, 0), km)
    tiara = feathered('assets/pknot_3.jpg', (0.0, 0.12, 1.0, 0.86))
    x0, y0, w, h = hero(cv, tiara, W / 2 - 20, 500, 560, glow=(200, 190, 170))
    sparkle(cv, [(x0 + w * 0.5, y0 + h * 0.05, 0.9), (x0 + w * 0.18, y0 + h * 0.35, 0.6), (x0 + w * 0.84, y0 + h * 0.30, 0.6)])
    vignette(cv)
    words(cv, 'NOW HERS', W / 2 - 40, 830, size=170, color=(255, 236, 190), weight=850)
    logo(cv)
    cv.save('thumb/B_tiara.jpg', quality=94); return cv

def build_C():
    cv = bg(c0=(40, 10, 18), c1=(6, 2, 4), glow=(120, 40, 60), gpos=(0.5, 0.45), gsize=0.5)
    # velvet table at the bottom
    t = Image.new('L', (W, H), 0); ImageDraw.Draw(t).rectangle((0, 760, W, H), fill=120)
    cv.paste(Image.new('RGB', (W, H), (20, 4, 10)), (0, 0), t.filter(ImageFilter.GaussianBlur(30)))
    d, dm = face_panel('assets/pdsmile_29.jpg', (0.0, 0.0, 1.0, 0.82), 680, 820, 'right')
    m = np.array(dm).astype(float) / 255
    yy, xx = np.mgrid[0:820, 0:640]; ell = np.clip(1.4 - np.sqrt(((xx - 320) / 330) ** 2 + ((yy - 400) / 440) ** 2) * 1.4, 0, 1)
    yy, xx = np.mgrid[0:820, 0:680]; ell = np.clip(1.5 - np.sqrt(((xx - 340) / 350) ** 2 + ((yy - 380) / 470) ** 2) * 1.5, 0, 1)
    cv.paste(d, (W // 2 - 340, 150), Image.fromarray((ell * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(20)))
    ring = cut_plain('assets/pengage_46.jpg', crop=(0.0, 0.0, 1.0, 0.64), tol=24)
    cross = cut_plain('assets/pattallah_15.jpg', tol=24)
    pearls = cut_plain('assets/pcoll_29.jpg', tol=40)
    hero(cv, ring, 1620, 640, 330, glow=(70, 110, 255), rot=-6)
    hero(cv, cross, 400, 830, 440, glow=(150, 90, 220))
    hero(cv, pearls, 1500, 900, 260, glow=(230, 220, 210))
    vignette(cv, 70)
    words(cv, 'WHERE ARE THEY NOW?', W / 2 + 60, 40, size=104, color=(255, 236, 190), weight=850)
    logo(cv)
    cv.save('thumb/C_her_jewels.jpg', quality=94); return cv

if __name__ == '__main__':
    for f in (build_A, build_B, build_C):
        im = f(); print(f.__name__, 'brightness', round(np.array(im.convert('L')).mean(), 1))
