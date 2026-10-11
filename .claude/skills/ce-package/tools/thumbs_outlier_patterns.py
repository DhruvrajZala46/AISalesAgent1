# Round 2: three thumbnails built on the niche's proven outlier patterns
# D: products around a person, cheap (x) vs chic (check)   [girls STOP buying this x9, Avoid These COMBINATIONS x6]
# E: mood board + centre cut-out + spoken statement         [elegant/classy x13, Autumn Trends x15, do less. look better. x8]
# F: eye-contact face + one mistake + short statement       [effortlessly feminine x12, this makes you prettier x9]
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

D = os.path.dirname(os.path.abspath(__file__)); SRC = D + '/src'; V4 = D + '/../v4/assets'
FONTS = D + '/../full/fonts'; W, H = 1280, 720

def serif(size, weight=700, italic=False):
    f = ImageFont.truetype(f'{FONTS}/PlayfairDisplay.ttf', size)
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    return f
def script(size): return ImageFont.truetype(f'{FONTS}/PinyonScript-Regular.ttf', size)
def grade(im):
    im = ImageEnhance.Contrast(im).enhance(1.06); im = ImageEnhance.Color(im).enhance(0.94)
    return Image.blend(im, Image.new(im.mode, im.size, (205, 160, 120) + ((255,) if im.mode == 'RGBA' else ())), 0.05)
def backdrop(light=(222, 172, 125), dark=(176, 116, 74), cx=0.5, cy=0.45):
    """The channel's warm caramel glow."""
    bg = Image.new('RGB', (W, H), dark); d = ImageDraw.Draw(bg)
    for r in range(1100, 0, -8):
        t = r / 1100; col = tuple(int(light[i] * (1 - t) + dark[i] * t) for i in range(3))
        d.ellipse((W * cx - r, H * cy - r * 0.75, W * cx + r, H * cy + r * 0.75), fill=col)
    return bg.filter(ImageFilter.GaussianBlur(30))
def load_cut(name, h=None, w=None):
    im = Image.open(f'{SRC}/{name}_cut.png').convert('RGBA')
    if h: im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
    if w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    rgb = grade(im.convert('RGB')); rgb.putalpha(im.getchannel('A')); return rgb
def clean(im):
    a = im.getchannel('A').point(lambda v: 0 if v < 90 else min(255, int((v - 90) * 255 / 120)))
    a = a.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8)); im = im.copy(); im.putalpha(a)
    return im.crop(a.getbbox())
def sticker(im, border=9):
    """White die-cut outline + soft drop shadow, the look the top outliers use."""
    im = clean(im); a = im.getchannel('A'); P = 2 * border + 24; big = Image.new('L', (im.width + 2 * P, im.height + 2 * P), 0); big.paste(a, (P, P))
    ring = big.filter(ImageFilter.MaxFilter(2 * border + 1))
    out = Image.new('RGBA', big.size, (0, 0, 0, 0))
    sh = Image.new('RGBA', big.size, (40, 20, 8, 0)); sh.putalpha(ring.point(lambda v: int(v * 0.45)).filter(ImageFilter.GaussianBlur(10)))
    sh2 = Image.new('RGBA', big.size, (0, 0, 0, 0)); sh2.paste(sh.crop((0, 0, big.width - 6, big.height - 10)), (6, 10)); out = Image.alpha_composite(out, sh2)
    white = Image.new('RGBA', big.size, (255, 255, 255, 0)); white.putalpha(ring); out = Image.alpha_composite(out, white)
    body = Image.new('RGBA', big.size, (0, 0, 0, 0)); body.paste(im, (P, P)); return Image.alpha_composite(out, body)
def put(canvas, im, x, y): canvas.paste(im, (int(x), int(y)), im)
def soft_shadow_text(c, xy, txt, font, fill=(255, 255, 255), anchor='mm', blur=12, alpha=210):
    sh = Image.new('L', c.size, 0); ImageDraw.Draw(sh).text(xy, txt, font=font, fill=alpha, anchor=anchor)
    c.paste(Image.new('RGB', c.size, (35, 20, 10)), (0, 0), sh.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(c).text(xy, txt, font=font, fill=fill, anchor=anchor)
def mark(c, cx, cy, ok, r=30):
    d = ImageDraw.Draw(c); d.ellipse((cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3), fill=(255, 255, 255))
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(52, 120, 78) if ok else (170, 36, 46))
    if ok: d.line([(cx - 13, cy + 1), (cx - 3, cy + 11), (cx + 14, cy - 10)], fill='white', width=7, joint='curve')
    else: d.line([(cx - 11, cy - 11), (cx + 11, cy + 11)], fill='white', width=7); d.line([(cx + 11, cy - 11), (cx - 11, cy + 11)], fill='white', width=7)
def logo(c, size=88, pos=(20, 16)):
    lg = Image.open(f'{V4}/logo_ce.png').convert('RGBA'); lg.thumbnail((size, size), Image.LANCZOS); c.paste(lg, pos, lg)
def product(name, box):
    """A product cut-out (from the video's assets or the thumbnail sources), fit inside box."""
    p = f'{V4}/{name}.png' if os.path.exists(f'{V4}/{name}.png') else f'{SRC}/{name}_cut.png'
    im = Image.open(p).convert('RGBA'); im.thumbnail(box, Image.LANCZOS); return sticker(im, 6)
def photo(path, w, h, fy=0.3, fx=0.5):
    im = Image.open(path).convert('RGB'); s = max(w / im.width, h / im.height); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = int((im.width - w) * fx); y = int((im.height - h) * fy); return grade(im.crop((x, y, x + w, y + h)))

# ---------------- D: cheap vs chic, products around her ----------------
Dc = backdrop()
d = ImageDraw.Draw(Dc)
left = [('p_fleece', 120, 175), ('p_ugly', 60, 400), ('p_glitter', 260, 330)]
right = [('c_coat', 990, 140), ('c_cream', 1010, 440), ('c_vskirt', 880, 330)]
for n, x, y in left:
    im = product(n, (220, 230)); put(Dc, im, x, y); mark(Dc, int(x + im.width - 30), int(y + 34), False, 26)
for n, x, y in right:
    im = product(n, (200, 250)); put(Dc, im, x, y); mark(Dc, int(x + im.width - 30), int(y + 34), True, 26)
her = sticker(load_cut('fc_cosy8', h=640), 9); put(Dc, her, W // 2 - her.width // 2, H - her.height + 30)
soft_shadow_text(Dc, (250, 80), 'cheap', script(118)); soft_shadow_text(Dc, (1050, 80), 'chic', script(118))
logo(Dc, pos=(20, 616)); Dc.save(f'{D}/thumb_D_cheap_vs_chic.jpg', quality=95)

# ---------------- E: winter mood board + statement ----------------
E = Image.new('RGB', (W, H), (30, 22, 18))
tiles = [('a2.jpg', 0.2), ('cr14.jpg', 0.15), ('a3.jpg', 0.25), ('lc8.jpg', 0.2), ('fc_cosy6.jpg', 0.25), ('c1.jpg', 0.45)]
tw = W // 3; th = H // 2
for k, (f, fy) in enumerate(tiles):
    E.paste(photo(f'{SRC}/{f}', tw - 4, th - 4, fy), ((k % 3) * tw + 2, (k // 3) * th + 2))
E = ImageEnhance.Brightness(E).enhance(0.6); E = E.filter(ImageFilter.GaussianBlur(1.2))
glow = backdrop(); mask = Image.new('L', (W, H), 0); ImageDraw.Draw(mask).ellipse((330, -160, 950, 900), fill=150)
E.paste(glow, (0, 0), mask.filter(ImageFilter.GaussianBlur(90)))
her = sticker(load_cut('fc_cine19', h=600), 9); put(E, her, W // 2 - her.width // 2 + 260, H - her.height + 40)
soft_shadow_text(E, (430, 300), 'cold,', serif(120, 700), blur=14)
soft_shadow_text(E, (430, 430), 'but chic.', script(150), blur=14)
logo(E); E.save(f'{D}/thumb_E_moodboard.jpg', quality=95)

# ---------------- F: eye contact + the one mistake ----------------
F = backdrop(light=(232, 188, 142), cx=0.68)
her = load_cut('fc_tex3', h=1500); her = clean(her).crop((0, 0, clean(her).width, 820))
put(F, sticker(her, 9), 610, 10)
fl = product('p_fleece', (420, 420)); put(F, fl, 90, 250)
mark(F, 90 + fl.width - 40, 290, False, 44)
soft_shadow_text(F, (330, 140), 'looks cheap.', serif(100, 800), blur=14)
logo(F, pos=(20, 616)); F.save(f'{D}/thumb_F_eye_contact.jpg', quality=95)

prev = Image.new('RGB', (3 * 370 + 10, 2 * 210 + 120), (250, 250, 250))
for k, n in enumerate(['thumb_D_cheap_vs_chic', 'thumb_E_moodboard', 'thumb_F_eye_contact']):
    im = Image.open(f'{D}/{n}.jpg'); prev.paste(im.resize((360, 202), Image.LANCZOS), (10 + k * 370, 10)); prev.paste(im.resize((168, 94), Image.LANCZOS), (10 + k * 370, 230))
prev.save(f'{D}/preview_feed2.jpg', quality=90); print('ok')
