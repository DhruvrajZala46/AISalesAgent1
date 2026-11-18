# build_thumb_d.py - thumbnail D: the "portrait + her things on a soft rug + thin white frame, no words" format.
# Proven on one channel against itself (Laura Jane Atelier, same women, same audience):
#   this format 6 of 6 at 4.7x-25x its channel (Diana 9.1x, Grace Kelly 9.0x, Audrey Hepburn 8.1x, Marilyn 25x);
#   the same channel's title-led thumbnails 9 of 9 at 0.6x-2.9x (Diana 2.3x, Grace Kelly 1.0x, Audrey 1.6x).
# Run inside the work folder:  python3 build_thumb_d.py  -> thumb/D_portrait_rug_frame.jpg (1920x1080)
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
W, H = 1920, 1080; SPLIT = 960
rng = np.random.default_rng(11)
LOGO = '/home/user/AISalesAgent1/classy-academy-test/workflow/assets/logo_ca.png'

def fur(w, h):
    """a soft peach-cream faux-fur rug, seen from above: thousands of short curling strands, light from the top right"""
    base = Image.new('RGB', (w, h), (214, 180, 154)); d = ImageDraw.Draw(base)
    # clumps: a low-frequency field that sets each strand's direction and tone, so the fur parts into soft tufts
    cl = Image.fromarray((rng.random((h // 40 + 2, w // 40 + 2)) * 255).astype('uint8')).resize((w, h), Image.BICUBIC)
    cl = np.array(cl.filter(ImageFilter.GaussianBlur(18))).astype(float) / 255
    for _ in range(60000):
        x, y = rng.uniform(-30, w + 30), rng.uniform(-30, h + 30)
        q = cl[int(min(max(y, 0), h - 1)), int(min(max(x, 0), w - 1))]
        ang = -1.2 + 2.6 * q + rng.normal(0, 0.35); L = rng.uniform(40, 95)
        t = np.clip(rng.normal(0.35 + 0.5 * q, 0.22), 0, 1)
        c = tuple(int(v) for v in np.array([176, 136, 110]) * (1 - t) + np.array([253, 238, 224]) * t)
        pts = [(x, y)]
        for k in range(1, 7):
            ang += rng.normal(0, 0.18); x += np.cos(ang) * L / 6; y += np.sin(ang) * L / 6; pts.append((x, y))
        d.line(pts, fill=c, width=int(rng.choice([2, 3, 3, 4])))
    base = base.filter(ImageFilter.GaussianBlur(1.3))
    yy, xx = np.mgrid[0:h, 0:w]; light = np.exp(-(((xx / w - 0.9) / 0.8) ** 2 + ((yy / h - 0.1) / 0.9) ** 2))
    arr = np.array(base).astype(float) * (0.86 + 0.2 * light[..., None])
    return Image.fromarray(np.clip(arr, 0, 255).astype('uint8'))

def drop(canvas, im, x, y, angle=0, blur=16, off=(10, 16), strength=120):
    """lay a flat object on the rug: rotate, soft shadow below (top light), paste"""
    if angle: im = im.rotate(angle, resample=Image.BICUBIC, expand=True)
    a = im.split()[3]
    sh = Image.new('L', canvas.size, 0); sh.paste(a.point(lambda v: v * strength // 255), (x + off[0], y + off[1]))
    canvas.paste(Image.new('RGB', canvas.size, (90, 60, 42)), (0, 0), sh.filter(ImageFilter.GaussianBlur(blur)))
    ct = Image.new('L', canvas.size, 0); ct.paste(a.point(lambda v: v * 70 // 255), (x + 2, y + 4))
    canvas.paste(Image.new('RGB', canvas.size, (70, 45, 30)), (0, 0), ct.filter(ImageFilter.GaussianBlur(4)))
    canvas.paste(im.convert('RGB'), (x, y), a)

def print_photo(path, w, box=None, border=22):
    """a printed photograph with a white border, like the magazine pages in the winning thumbnails"""
    p = Image.open(path).convert('RGB')
    if box: p = p.crop(box)
    h = int(p.height * w / p.width); p = p.resize((w, h), Image.LANCZOS)
    p = ImageEnhance.Color(p).enhance(0.92)
    card = Image.new('RGBA', (w + 2 * border, h + 2 * border), (250, 247, 241, 255)); card.paste(p, (border, border))
    return card

def cut(path, h, angle=0):
    o = Image.open(path).convert('RGBA'); o = o.crop(o.getbbox()); w = int(o.width * h / o.height)
    o = o.resize((w, h), Image.LANCZOS)
    rgb = Image.blend(o.convert('RGB'), Image.new('RGB', o.size, (255, 232, 210)), 0.05); rgb.putalpha(o.split()[3])
    return rgb

def frame(canvas, inset=46, notch=26, gap=12):
    """the thin white ornamental frame across the whole thumbnail: two lines, notched corners"""
    lay = Image.new('L', canvas.size, 0); d = ImageDraw.Draw(lay)
    for k, wd in ((0, 3), (gap, 2)):
        i = inset + k; n = notch
        pts = [(i + n, i), (W - i - n, i), (W - i - n, i + n), (W - i, i + n), (W - i, H - i - n), (W - i - n, H - i - n),
               (W - i - n, H - i), (i + n, H - i), (i + n, H - i - n), (i, H - i - n), (i, i + n), (i + n, i + n), (i + n, i)]
        d.line(pts, fill=255, width=wd, joint='curve')
    sh = lay.filter(ImageFilter.GaussianBlur(3)).point(lambda v: v * 0.5)
    canvas.paste(Image.new('RGB', canvas.size, (40, 26, 18)), (2, 3), sh)
    canvas.paste(Image.new('RGB', canvas.size, (255, 252, 246)), (0, 0), lay)

def build():
    cv = Image.new('RGB', (W, H))
    rug = fur(W - SPLIT, H); cv.paste(rug, (SPLIT, 0))
    # her things laid out: the printed photo of her in the sheep jumper, then the bag and the two perfumes
    ph = print_photo('assets/psheep_35.jpg', 330, box=(60, 40, 1040, 1500))
    drop(cv, ph, SPLIT + 70, 120, angle=7, blur=18)
    drop(cv, cut('thumb/ph_ladydior.png', 470, angle=0).rotate(-8, resample=Image.BICUBIC, expand=True), SPLIT + 470, 70, blur=20, off=(14, 22))
    drop(cv, cut('thumb/ph_quelques.png', 430).rotate(-62, resample=Image.BICUBIC, expand=True), SPLIT + 70, 640, blur=14)
    drop(cv, cut('thumb/ph_firstbottle.png', 380).rotate(12, resample=Image.BICUBIC, expand=True), SPLIT + 560, 560, blur=16, off=(12, 18))
    # the portrait: real press photograph, her eyes turned toward her things
    p = Image.open('thumb/orig/plaugh_33.jpg').convert('RGB'); sw, sh_ = p.size
    cw = sw * 0.93; ch = cw * H / SPLIT; x0 = (sw - cw) / 2 + 10; y0 = 0
    if ch > sh_: ch = sh_; cw = ch * SPLIT / H
    c = p.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((SPLIT, H), Image.LANCZOS)
    c = ImageEnhance.Color(c).enhance(1.04); c = ImageEnhance.Contrast(c).enhance(1.04)
    c = c.filter(ImageFilter.UnsharpMask(1.6, 50, 2)); cv.paste(c, (0, 0))
    sd = Image.new('L', (W, H), 0); ImageDraw.Draw(sd).rectangle((SPLIT, 0, SPLIT + 24, H), fill=80)
    cv.paste(Image.new('RGB', (W, H), (60, 40, 25)), (0, 0), sd.filter(ImageFilter.GaussianBlur(14)))
    # gentle warm vignette
    yy, xx = np.mgrid[0:H, 0:W]; dd = np.sqrt(((xx - W / 2) / (W * 0.6)) ** 2 + ((yy - H / 2) / (H * 0.6)) ** 2)
    cv.paste(Image.new('RGB', (W, H), (40, 24, 14)), (0, 0), Image.fromarray(np.clip((dd - 0.8) * 160, 0, 80).astype('uint8')).filter(ImageFilter.GaussianBlur(40)))
    frame(cv)
    lg = Image.open(LOGO).convert('RGBA'); s = 130 / lg.height; lg = lg.resize((int(lg.width * s), 130), Image.LANCZOS)
    pad = Image.new('L', (W, H), 0); ImageDraw.Draw(pad).ellipse((40, 40, 120 + lg.width, 110 + lg.height), fill=95)
    cv.paste(Image.new('RGB', (W, H), (25, 18, 12)), (0, 0), pad.filter(ImageFilter.GaussianBlur(26))); cv.paste(lg, (78, 70), lg)
    cv.save('thumb/D_portrait_rug_frame.jpg', quality=93)
    print('D source px per output px', round(cw / SPLIT, 2), 'brightness', round(np.array(cv.convert('L')).mean(), 1))

if __name__ == '__main__':
    build()
