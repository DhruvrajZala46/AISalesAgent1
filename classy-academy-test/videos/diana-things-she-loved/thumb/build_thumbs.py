# build_thumbs.py - thumbnails B and C for "7 Things Princess Diana Loved That You Can Still Buy Today" (18 Nov 2026)
# Layout of the lane's top thumbnails (94x, 78x, 48x their channel): a photo of her on the left, her things laid out on
# a table on the right, no words. Here with a REAL press photograph and REAL product cut-outs (no AI picture).
# Run inside the work folder:  python3 build_thumbs.py  -> thumb/B_*.jpg, thumb/C_*.jpg (1920x1080)
import sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
W, H = 1920, 1080
SPLIT = 860                                   # photo of her: x 0-860
rng = np.random.default_rng(7)
FD = '/tmp/claude-0/-home-user-AISalesAgent1/e022df48-ce52-5e1c-9920-7b34f523b018/scratchpad/cdl/fonts/'
LOGO = '/home/user/AISalesAgent1/classy-academy-test/workflow/assets/logo_ca.png'

def lerp(c0, c1, t): return tuple(int(a + (b - a) * t) for a, b in zip(c0, c1))

def tabletop():
    """a warm cream studio: wall above, a soft linen-coloured table below, light from the upper right"""
    bg = np.zeros((H, W, 3), float); HOR = 520
    for y in range(H):
        if y < HOR: c = lerp((242, 232, 219), (226, 210, 190), y / HOR)
        else: c = lerp((236, 222, 203), (214, 193, 168), (y - HOR) / (H - HOR))
        bg[y] = c
    xs = np.linspace(0, 1, W)[None, :, None]; ys = np.linspace(0, 1, H)[:, None, None]
    light = np.exp(-(((xs - 0.85) / 0.55) ** 2 + ((ys - 0.15) / 0.7) ** 2))      # a soft window light, upper right
    bg = bg * (0.90 + 0.14 * light)
    im = Image.fromarray(np.clip(bg, 0, 255).astype('uint8'))
    # the table edge: a soft line, not a hard cut
    edge = Image.new('L', (W, H), 0); ImageDraw.Draw(edge).rectangle((0, HOR - 2, W, HOR + 2), fill=70)
    im = Image.composite(Image.new('RGB', (W, H), (205, 186, 162)), im, edge.filter(ImageFilter.GaussianBlur(6)))
    noise = rng.normal(0, 3.2, (H, W, 1)); arr = np.array(im).astype(float) + noise
    return Image.fromarray(np.clip(arr, 0, 255).astype('uint8'))

def place(canvas, path, cx, base, h, lean=0, shadow=1.0):
    """stand a cut-out on the table: contact shadow at its base, a long soft shadow away from the light"""
    ob = Image.open(path).convert('RGBA')
    if lean: ob = ob.rotate(lean, resample=Image.BICUBIC, expand=True)
    bb = ob.getbbox(); ob = ob.crop(bb); w = int(ob.width * h / ob.height); ob = ob.resize((w, h), Image.LANCZOS)
    x0, y0 = int(cx - w / 2), int(base - h)
    a = ob.split()[3]
    # 1) cast shadow: the object's silhouette squashed onto the table, thrown to the lower left, very soft
    sh = Image.new('L', (W, H), 0)
    sq = a.resize((w, max(8, int(h * 0.22))))
    sh.paste(sq, (x0 - int(w * 0.10), base - int(h * 0.22 * 0.55)))
    sh = sh.filter(ImageFilter.GaussianBlur(22)).point(lambda v: int(v * 0.42 * shadow))
    canvas.paste(Image.new('RGB', (W, H), (92, 64, 40)), (0, 0), sh)
    # 2) contact shadow: dark and tight where it touches the table
    ct = Image.new('L', (W, H), 0)
    ImageDraw.Draw(ct).ellipse((x0 + w * 0.06, base - 16, x0 + w * 0.94, base + 12), fill=int(150 * shadow))
    canvas.paste(Image.new('RGB', (W, H), (70, 48, 30)), (0, 0), ct.filter(ImageFilter.GaussianBlur(9)))
    # 3) the object, slightly warmed to sit in the same light
    rgb = ImageEnhance.Brightness(ob.convert('RGB')).enhance(1.02)
    rgb = Image.blend(rgb, Image.new('RGB', rgb.size, (255, 236, 210)), 0.04)
    canvas.paste(rgb, (x0, y0), a)
    return (x0, y0, w, h)

def hero(canvas):
    """the press photograph: Diana in the sheep jumper, smiling at the camera (psheep_1, 1177x2048)"""
    im = Image.open('assets/psheep_1.jpg').convert('RGB')
    cw = 960; ch = int(cw * H / SPLIT); cx = 560; top = 20                 # head and shoulders, the sheep and the bow
    c = im.crop((cx - cw // 2, top, cx + cw // 2, top + ch)).resize((SPLIT, H), Image.LANCZOS)
    c = ImageEnhance.Color(c).enhance(1.06); c = ImageEnhance.Contrast(c).enhance(1.05); c = ImageEnhance.Brightness(c).enhance(1.04)
    c = ImageEnhance.Sharpness(c).enhance(1.15)
    canvas.paste(c, (0, 0))
    # a soft seam: the photo melts into the room instead of a hard cut
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).rectangle((SPLIT - 70, 0, SPLIT + 10, H), fill=255)
    return cw / SPLIT

def logo(canvas):
    lg = Image.open(LOGO).convert('RGBA'); s = 150 / lg.height; lg = lg.resize((int(lg.width * s), 150), Image.LANCZOS)
    pad = Image.new('L', (W, H), 0); ImageDraw.Draw(pad).ellipse((10, 6, 10 + lg.width + 60, 6 + lg.height + 50), fill=110)
    canvas.paste(Image.new('RGB', (W, H), (25, 18, 12)), (0, 0), pad.filter(ImageFilter.GaussianBlur(28)))
    canvas.paste(lg, (40, 30), lg)

def build(name, words=None):
    cv = tabletop()
    things = [  # (cut-out, centre x, table line y, height, lean): back row first, then the front row
        ('thumb/ph_hunterboot.png', 1712, 790, 740, 0),
        ('thumb/ph_ladydior.png', 1470, 815, 520, 0),
        ('thumb/ph_guccitote.png', 1160, 835, 520, 0),
        ('thumb/ph_quelques.png', 1385, 1010, 400, 0),
        ('thumb/ph_gomblue.png', 1125, 1068, 300, 0),
        ('thumb/ph_firstbottle.png', 1660, 1062, 380, 0),
    ]
    for p, cx, base, h, lean in things: place(cv, p, cx, base, h, lean)
    s = hero(cv)
    # soft seam between photo and room
    seam = Image.new('L', (W, H), 0); ImageDraw.Draw(seam).rectangle((SPLIT - 3, 0, SPLIT + 3, H), fill=255)
    cv.paste(Image.new('RGB', (W, H), (246, 238, 228)), (0, 0), seam.filter(ImageFilter.GaussianBlur(2)))
    sd = Image.new('L', (W, H), 0); ImageDraw.Draw(sd).rectangle((SPLIT, 0, SPLIT + 26, H), fill=90)
    cv.paste(Image.new('RGB', (W, H), (60, 40, 25)), (0, 0), sd.filter(ImageFilter.GaussianBlur(16)))
    # vignette: pulls the eye to the face and the things
    v = Image.new('L', (W, H), 0); ImageDraw.Draw(v).rectangle((0, 0, W, H), fill=0)
    yy, xx = np.mgrid[0:H, 0:W]; d = np.sqrt(((xx - W * 0.5) / (W * 0.62)) ** 2 + ((yy - H * 0.48) / (H * 0.62)) ** 2)
    vig = Image.fromarray(np.clip((d - 0.75) * 180, 0, 90).astype('uint8'))
    cv.paste(Image.new('RGB', (W, H), (30, 20, 12)), (0, 0), vig.filter(ImageFilter.GaussianBlur(40)))
    if words:
        tag(cv, words)
    logo(cv)
    cv.save(f'thumb/{name}.jpg', quality=93); print(name, 'photo scale', round(s, 2), 'brightness', round(np.array(cv.convert('L')).mean(), 1))

def tag(cv, words):
    """C: two short lines in the channel's serif, on a soft cream card with a shadow, top right (above the things)"""
    l1, l2 = words
    f1 = ImageFont.truetype(FD + 'PlayfairDisplay.ttf', 66) if os.path.exists(FD + 'PlayfairDisplay.ttf') else ImageFont.truetype(FD + os.listdir(FD)[0], 66)
    f2 = ImageFont.truetype(FD + 'PlayfairDisplay.ttf', 82) if os.path.exists(FD + 'PlayfairDisplay.ttf') else f1
    d = ImageDraw.Draw(cv); w1 = d.textlength(l1, font=f1); w2 = d.textlength(l2, font=f2)
    bw = int(max(w1, w2) + 90); x0 = 1185 - bw // 2; y0 = 58; bh = 220
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle((x0 + 10, y0 + 18, x0 + bw + 10, y0 + bh + 18), 20, fill=120)
    cv.paste(Image.new('RGB', (W, H), (60, 40, 25)), (0, 0), sh.filter(ImageFilter.GaussianBlur(18)))
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 20, fill=(252, 247, 240))
    d.text((x0 + bw / 2, y0 + 70), l1, font=f1, fill=(40, 30, 24), anchor='mm')
    d.text((x0 + bw / 2, y0 + 158), l2, font=f2, fill=(160, 32, 40), anchor='mm')

if __name__ == '__main__':
    os.makedirs('thumb', exist_ok=True)
    build('B_her_things_no_words')
    build('C_her_things_still_sold', ('Things she loved', 'still sold today'))
