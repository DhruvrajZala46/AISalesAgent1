# make_v2.py - footwear thumbnails v2, each built on one formula from the 38 videos with 1M+ views in the lane (THUMBNAIL.md v2):
#  T1  BEFORE / AFTER  - the same boots, tired and cared for, filling the frame, red tag / green tag, red arrows
#      (Rose Anvil 12.56M, Hacked Life 5.37M, LS Maker 2.35M, Real Men Real Style 1.78M + 1.69M, Carl Murawski 1.28M)
#  T2  WRONG / RIGHT   - one detail seen the same way twice, red label + arrow, green label + tick
#      (Mademoiselle Spends 1.86M, What To Wear 1.16M, Emily Elizabeth May 1.06M, Shea Whitney 1.00M)
#  T3  crossed out + "LOOKS CHEAP!" - three cut-outs, a red X on each, thin + black sans
#      (Anna Bey 8.72M / 3.90M / 1.77M / 1.73M / 1.66M / 1.59M, Mademoiselle Spends 1.49M, The Intentional Woman 1.19M)
# Real photos only (Pinterest originals, orig_meta.json), the CE logo.
import sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W, H = 1280, 720
FD = '/home/user/AISalesAgent1/classy-academy-test/workflow/assets/'
RED, GREEN = (226, 26, 34), (36, 168, 66)
def font(name, size, var=None):
    f = ImageFont.truetype('fonts/' + name, size)
    if var: f.set_variation_by_name(var)
    return f
def cover(img, w, h, cx=0.5, cy=0.5):
    r = max(w / img.width, h / img.height); im = img.resize((int(img.width * r + 0.5), int(img.height * r + 0.5)), Image.LANCZOS)
    x0 = int((im.width - w) * cx); y0 = int((im.height - h) * cy); return im.crop((x0, y0, x0 + w, y0 + h))
def grade(im, col=1.12, con=1.08, sharp=1.35, bri=1.0):
    im = ImageEnhance.Color(im).enhance(col); im = ImageEnhance.Contrast(im).enhance(con)
    im = ImageEnhance.Brightness(im).enhance(bri); return ImageEnhance.Sharpness(im).enhance(sharp)
def shadow(c, rgba, xy, off=(8, 12), blur=14, op=0.45, col=(30, 20, 16)):
    sh = Image.new('L', c.size, 0); sh.paste(rgba.split()[3].point(lambda v: int(v * op)), (xy[0] + off[0], xy[1] + off[1]))
    c.paste(Image.new('RGB', c.size, col), (0, 0), sh.filter(ImageFilter.GaussianBlur(blur)))
def paste(c, rgba, xy, **kw):
    shadow(c, rgba, xy, **kw); c.paste(rgba, xy, rgba)
def logo(c, x=20, y=16, s=88):
    lg = Image.open(FD + 'logo_ce.png').convert('RGBA'); lg.thumbnail((s, s), Image.LANCZOS); paste(c, lg, (x, y), off=(2, 3), blur=4, op=0.5)
def tag(text, bg, size=118, pad=(30, 8), tilt=0, border=7, fg=(255, 255, 255), fname='Anton-Regular.ttf'):
    f = font(fname, size); b = f.getbbox(text); tw, th = b[2] - b[0], b[3] - b[1]
    w, h = tw + 2 * pad[0] + 2 * border, th + 2 * pad[1] + 2 * border
    t = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(t)
    d.rectangle((0, 0, w - 1, h - 1), fill=(255, 255, 255, 255)); d.rectangle((border, border, w - 1 - border, h - 1 - border), fill=bg + (255,))
    d.text((border + pad[0] - b[0], border + pad[1] - b[1]), text, font=f, fill=fg + (255,))
    return t.rotate(tilt, expand=True, resample=Image.BICUBIC) if tilt else t
def arrow(c, pts, col=RED, w=20, head=58, outline=7):
    # a curved arrow through three points (quadratic bezier), white outline, red body, a filled head at the last point
    (x0, y0), (x1, y1), (x2, y2) = pts
    P = [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t * t * x2, (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t * t * y2) for t in [i / 40 for i in range(41)]]
    a = math.atan2(P[-1][1] - P[-4][1], P[-1][0] - P[-4][0])
    tip = (x2 + math.cos(a) * head * 0.55, y2 + math.sin(a) * head * 0.55)
    hd = [tip, (x2 + math.cos(a + 2.45) * head, y2 + math.sin(a + 2.45) * head), (x2 + math.cos(a - 2.45) * head, y2 + math.sin(a - 2.45) * head)]
    L = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    for ww, cc, grow in ((w + 2 * outline, (255, 255, 255, 255), outline), (w, col + (255,), 0)):
        d.line(P, fill=cc, width=ww, joint='curve')
        for p in (P[0],): d.ellipse((p[0] - ww / 2, p[1] - ww / 2, p[0] + ww / 2, p[1] + ww / 2), fill=cc)
        if grow:
            cxh = sum(p[0] for p in hd) / 3; cyh = sum(p[1] for p in hd) / 3
            d.polygon([(cxh + (p[0] - cxh) * 1.28, cyh + (p[1] - cyh) * 1.28) for p in hd], fill=cc)
        else: d.polygon(hd, fill=cc)
    paste(c, L, (0, 0), off=(4, 6), blur=6, op=0.45)
def mark(kind, r=74):
    t = Image.new('RGBA', (2 * r + 8, 2 * r + 8), (0, 0, 0, 0)); d = ImageDraw.Draw(t); cx = cy = r + 4
    d.ellipse((4, 4, 2 * r + 4, 2 * r + 4), fill=(RED if kind == 'x' else GREEN) + (255,), outline=(255, 255, 255, 255), width=8)
    k = r * 0.42; lw = int(r * 0.26)
    if kind == 'x':
        d.line((cx - k, cy - k, cx + k, cy + k), fill='white', width=lw); d.line((cx - k, cy + k, cx + k, cy - k), fill='white', width=lw)
    else:
        d.line((cx - k * 1.15, cy + k * 0.05, cx - k * 0.3, cy + k * 0.85), fill='white', width=lw); d.line((cx - k * 0.3, cy + k * 0.85, cx + k * 1.2, cy - k * 0.8), fill='white', width=lw)
    return t
def red_x(c, cx, cy, s, w=34):
    L = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    for a, b in (((cx - s, cy - s), (cx + s, cy + s)), ((cx - s, cy + s), (cx + s, cy - s))): d.line([a, b], fill=RED + (255,), width=w)
    paste(c, L, (0, 0), off=(4, 6), blur=7, op=0.4)
def sticker(png, hh, maxw=None, rot=0, stroke=9):
    im = Image.open(png).convert('RGBA'); r = im.width / im.height; w2, h2 = int(hh * r), hh
    if maxw and w2 > maxw: w2 = maxw; h2 = int(maxw / r)
    im = im.resize((w2, h2), Image.LANCZOS); im = ImageEnhance.Sharpness(im).enhance(1.3)
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    pad = stroke + 4; big = Image.new('RGBA', (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0)); big.paste(im, (pad, pad), im)
    a = big.split()[3]; grown = a.filter(ImageFilter.MaxFilter(2 * stroke + 1)).filter(ImageFilter.GaussianBlur(1.2)).point(lambda v: 255 if v > 110 else int(v * 2.3))
    out = Image.new('RGBA', big.size, (255, 255, 255, 0)); out.putalpha(grown); out.alpha_composite(big); return out

def build_1(out='T1.jpg'):
    src = Image.open('orig/ba7_2.jpg').convert('RGB'); c = Image.new('RGB', (W, H), 'white')
    for k, x in enumerate((0, 644)):
        half = src.crop((k * 512, 0, k * 512 + 512, 768)); p = half.resize((640, 960), Image.LANCZOS).crop((2, 240, 638, 960)); c.paste(grade(p, 1.18, 1.1, 1.5), (x, 0))
    arrow(c, [(160, 230), (55, 370), (140, 470)]); arrow(c, [(1120, 230), (1235, 365), (1155, 465)], col=GREEN)
    t = tag('BEFORE', RED, 124, pad=(34, 14), tilt=2); paste(c, t, (318 - t.width // 2, 541), blur=10)
    t = tag('AFTER', GREEN, 124, pad=(34, 14), tilt=-2); paste(c, t, (935 - t.width // 2, 541), blur=10)
    logo(c); c.save(out, quality=95); return c

def build_2(out='T2.jpg'):
    c = Image.new('RGB', (W, H), 'white')
    L = Image.open('orig/wh1_13.jpg').convert('RGB'); L = L.resize((640, int(L.height * 640 / L.width)), Image.LANCZOS); L = L.crop((2, L.height - 720, 638, L.height)); c.paste(grade(L, 1.12, 1.1, 1.5, 1.04), (0, 0))
    R = Image.open('orig/bk1_4.jpg').convert('RGB'); R = cover(R.crop((150, 500, 850, 1290)), 636, 720, 0.5, 0.5); c.paste(grade(R, 1.0, 1.06, 1.3), (644, 0))
    t = tag('WRONG', RED, 112, tilt=3); paste(c, t, (120, 20), blur=10)
    t = tag('RIGHT', GREEN, 112, tilt=-3); paste(c, t, (1260 - t.width, 20), blur=10)
    arrow(c, [(250, 250), (60, 430), (150, 590)])
    m = mark('v', 78); paste(c, m, (668, 30), blur=8)
    logo(c, x=18, y=18, s=84); c.save(out, quality=95); return c

def build_3(out='T3.jpg'):
    c = Image.new('RGB', (W, H)); g = ImageDraw.Draw(c)
    for y in range(H): g.line((0, y, W, y), fill=(int(244 - 10 * y / H), int(226 - 14 * y / H), int(218 - 16 * y / H)))
    items = [('cut/sc1_4.png', 290, 505, -7, 5, -70), ('cut/lb2_3.png', 655, 510, 3, -20, -75), ('cut/ba5_9.png', 1040, 505, 7, 5, -95)]
    for png, cx, hh, rot, xo, yo in items:
        s = sticker(png, hh, rot=rot); x, y = cx - s.width // 2, 262 - s.height // 2; paste(c, s, (x, y), off=(10, 14), blur=16, op=0.4)
        red_x(c, cx + xo, 262 + yo, 74, 36)
    f1 = font('Montserrat.ttf', 140, 'Light'); f2 = font('Montserrat.ttf', 140, 'Black'); d = ImageDraw.Draw(c)
    w1 = d.textlength('LOOKS ', font=f1); w2 = d.textlength('CHEAP!', font=f2); x = (W - (w1 + w2)) // 2 - 45; y = 512
    d.text((x, y), 'LOOKS', font=f1, fill=(18, 14, 14)); d.text((x + w1, y), 'CHEAP!', font=f2, fill=(18, 14, 14))
    logo(c, x=18, y=16, s=88); c.save(out, quality=95); return c

if __name__ == '__main__':
    for n in (sys.argv[1:] or ['1', '2', '3']): {'1': build_1, '2': build_2, '3': build_3}[n]()
    S = Image.new('RGB', (1280, 2184), 'white')
    for i, f in enumerate(['T1.jpg', 'T2.jpg', 'T3.jpg']): S.paste(Image.open(f), (0, i * 732))
    S.save('T123.jpg', quality=85)
