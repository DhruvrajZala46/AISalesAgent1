# make_shoe.py - three thumbnails for "Understated Winter Footwear Rules", each rebuilt from one proven layout of the
# topic's most-viewed videos (YouTube searches of 11 Nov 2026; THUMBNAIL.md):
#  A  Anna Bey, "10 Boots Elegant Ladies NEVER Wear" (412k; the same layout on her 3.9M, 1.66M, 1.59M shoe videos):
#     a woman's face large at the left on a plain light background, the wrong shoes cut out at the right, a big red X on each.
#  B  Carl Murawski, "How to Make Cheap Boots Look Expensive" (1.28M): the tired boot and the elegant boot side by side,
#     light left / dark right, a white handwritten script line across the middle.
#  C  Elvira Hartwell, "The BIGGEST Shoe MISTAKES Women Over 50 Make" (622k; also Ebony Lifestyle 452k): a photo of the
#     wrong and the right shoe, a red X circle top-left, a green tick circle top-right, huge condensed caps in white and red.
# Real photos only (Pinterest originals), the CE logo top-left.
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W, H = 1280, 720
FD = '/home/user/AISalesAgent1/classy-academy-test/workflow/assets/'
F2 = 'fonts/'
def logo(c, x=22, y=18, s=92):
    lg = Image.open(FD + 'logo_ce.png').convert('RGBA'); lg.thumbnail((s, s), Image.LANCZOS)
    sh = Image.new('L', c.size, 0); sh.paste(lg.split()[3].point(lambda v: v * 0.5), (x + 2, y + 3))
    c.paste(Image.new('RGB', c.size, (20, 14, 10)), (0, 0), sh.filter(ImageFilter.GaussianBlur(4))); c.paste(lg, (x, y), lg)
def put(c, png, cx, ybot, hh, maxw=None, rot=0, shadow=0.35):
    im = Image.open(png).convert('RGBA'); r = im.width / im.height; w2 = int(hh * r); h2 = hh
    if maxw and w2 > maxw: w2 = maxw; h2 = int(maxw / r)
    im = im.resize((w2, h2), Image.LANCZOS)
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    x, y = int(cx - im.width / 2), int(ybot - im.height)
    if shadow:
        sh = Image.new('L', c.size, 0); sh.paste(im.split()[3].point(lambda v: v * shadow), (x + 10, y + 16))
        c.paste(Image.new('RGB', c.size, (40, 30, 24)), (0, 0), sh.filter(ImageFilter.GaussianBlur(16)))
    c.paste(im, (x, y), im); return (x, y, x + im.width, y + im.height)
def red_x(c, cx, cy, s, w=26):
    d = ImageDraw.Draw(c); col = (226, 24, 32)
    for a, b in (((cx - s, cy - s), (cx + s, cy + s)), ((cx - s, cy + s), (cx + s, cy - s))): d.line([a, b], fill=col, width=w)
def cover(img, w, h, cx=0.5, cy=0.5):
    r = max(w / img.width, h / img.height); im = img.resize((int(img.width * r + 0.5), int(img.height * r + 0.5)), Image.LANCZOS)
    x0 = int((im.width - w) * cx); y0 = int((im.height - h) * cy); return im.crop((x0, y0, x0 + w, y0 + h))

def build_a(out='A.jpg'):
    c = Image.new('RGB', (W, H)); g = ImageDraw.Draw(c)
    for y in range(H): g.line((0, y, W, y), fill=(int(238 - 10 * y / H), int(233 - 10 * y / H), int(228 - 10 * y / H)))
    face = Image.open('cut/oliviahead6.png').convert('RGBA'); r = 760 / face.height
    face = face.resize((int(face.width * r), 760), Image.LANCZOS); c.paste(face, (-10, H - 760 + 30), face)
    b1 = put(c, 'cut/wornheel1.png', 640, 400, 330, maxw=380)
    b2 = put(c, 'cut/scuffboot0.png', 1085, 360, 330, maxw=330)
    b3 = put(c, 'cut/buckleboot.png', 905, 705, 330, maxw=320)
    for (x0, y0, x1, y1) in (b1, b2, b3):
        red_x(c, (x0 + x1) // 2 + 30, (y0 + y1) // 2 - 10, 62)
    logo(c); c = ImageEnhance.Sharpness(c).enhance(1.1); c.save(out, quality=95); return c

def build_b(out='B.jpg'):
    c = Image.new('RGB', (W, H)); g = ImageDraw.Draw(c)
    left = cover(Image.open('orig/creaseboot13.jpg').convert('RGB'), 640, 720, 0.5, 0.62)
    left = ImageEnhance.Brightness(left).enhance(0.92); c.paste(left, (0, 0))
    for y in range(H): g.line((640, y, W, y), fill=(int(62 - 18 * y / H), int(44 - 14 * y / H), int(34 - 12 * y / H)))
    put(c, 'cut/shinyboot8.png', 960, 700, 650, maxw=520, shadow=0.55)
    d = ImageDraw.Draw(c); d.rectangle((638, 0, 641, H), fill=(235, 226, 214))
    f = ImageFont.truetype(F2 + 'GreatVibes-Regular.ttf', 150)
    t = Image.new('RGBA', (900, 520), (0, 0, 0, 0)); dt = ImageDraw.Draw(t)
    for txt, (x, y), s in (('Tired', (60, 30), 150), ('to', (360, 165), 100), ('Elegant', (300, 275), 150)):
        ff = ImageFont.truetype(F2 + 'GreatVibes-Regular.ttf', s); dt.text((x, y), txt, font=ff, fill=(255, 255, 255, 255))
    t = t.rotate(14, expand=True, resample=Image.BICUBIC)
    a = t.split()[3]; sh = Image.new('L', c.size, 0); ox, oy = 640 - t.width // 2, 360 - t.height // 2
    sh.paste(a.point(lambda v: v * 0.85), (ox + 4, oy + 6)); c.paste(Image.new('RGB', c.size, (10, 6, 4)), (0, 0), sh.filter(ImageFilter.GaussianBlur(8)))
    c.paste(t, (ox, oy), t)
    logo(c); c.save(out, quality=95); return c

def build_c(out='C.jpg'):
    c = Image.new('RGB', (W, H))
    L = cover(Image.open('orig/wornheel0.jpg').convert('RGB'), 640, 720, 0.45, 0.5)
    R = cover(Image.open('orig/shinyboot3.jpg').convert('RGB'), 640, 720, 0.5, 0.75)
    c.paste(L, (0, 0)); c.paste(R, (640, 0))
    v = Image.new('L', (W, H), 0); ImageDraw.Draw(v).rectangle((330, 0, 950, H), fill=120)
    c.paste(Image.new('RGB', (W, H), (10, 8, 8)), (0, 0), v.filter(ImageFilter.GaussianBlur(70)))
    d = ImageDraw.Draw(c)
    for cx, cy, kind in ((70, 70, 'x'), (W - 70, 70, 'v')):
        r = 46; d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(226, 30, 36) if kind == 'x' else (52, 170, 74), outline=(255, 255, 255), width=5)
        if kind == 'x':
            d.line((cx - 18, cy - 18, cx + 18, cy + 18), fill='white', width=10); d.line((cx - 18, cy + 18, cx + 18, cy - 18), fill='white', width=10)
        else:
            d.line((cx - 22, cy + 2, cx - 6, cy + 18), fill='white', width=10); d.line((cx - 6, cy + 18, cx + 24, cy - 16), fill='white', width=10)
    lines = [('STOP', (255, 255, 255), 150), ('RUINING', (232, 30, 36), 150), ('YOUR', (255, 255, 255), 150), ('BOOTS', (232, 30, 36), 150)]
    fonts = [ImageFont.truetype(F2 + 'Anton-Regular.ttf', s) for _, _, s in lines]
    hs = [f.getbbox(t)[3] - f.getbbox(t)[1] for (t, _, _), f in zip(lines, fonts)]; gap = 6
    y = (H - (sum(hs) + gap * (len(lines) - 1))) // 2
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh); pos = []
    for (t, col, s), f, h in zip(lines, fonts, hs):
        yy = y - f.getbbox(t)[1]; pos.append((t, col, f, yy)); ds.text((W / 2 + 5, yy + 7), t, font=f, fill=235, anchor='ma'); y += h + gap
    c.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), sh.filter(ImageFilter.GaussianBlur(6)))
    d = ImageDraw.Draw(c)
    for t, col, f, yy in pos: d.text((W / 2, yy), t, font=f, fill=col, anchor='ma', stroke_width=2, stroke_fill=(20, 10, 10))
    logo(c, x=22, y=H - 108, s=84)
    c.save(out, quality=95); return c

if __name__ == '__main__':
    for n in (sys.argv[1:] or ['A', 'B', 'C']): {'A': build_a, 'B': build_b, 'C': build_c}[n]()
    S = Image.new('RGB', (1280, 2184), 'white')
    for i, f in enumerate(['A.jpg', 'B.jpg', 'C.jpg']): S.paste(Image.open(f), (0, i * 732))
    S.save('ABC.jpg', quality=85)
