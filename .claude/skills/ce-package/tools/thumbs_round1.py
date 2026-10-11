# Three 1280x720 thumbnails for YouTube "Test & compare", built in the channel's proven style.
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

D = os.path.dirname(os.path.abspath(__file__)); SRC = D + '/src'
FONTS = D + '/../full/fonts'
LOGO = D + '/../v4/assets/logo_ce.png'
W, H = 1280, 720

def serif(size, weight=700):
    f = ImageFont.truetype(f'{FONTS}/PlayfairDisplay.ttf', size)
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    return f
def script(size): return ImageFont.truetype(f'{FONTS}/PinyonScript-Regular.ttf', size)

def grade(im):
    """The channel's warm, soft, slightly desaturated look."""
    im = ImageEnhance.Contrast(im).enhance(1.06); im = ImageEnhance.Color(im).enhance(0.92)
    warm = Image.new('RGB', im.size, (205, 160, 120)); return Image.blend(im, warm, 0.07)
def fill(path, w, h, fy=0.35, zoom=1.0, fx=0.5):
    """Crop a portrait photo to w x h, keeping the face/upper body (fy = vertical focus)."""
    im = Image.open(path).convert('RGB'); s = max(w / im.width, h / im.height) * zoom
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = int((im.width - w) * fx); y = int((im.height - h) * fy); return grade(im.crop((x, y, x + w, y + h)))
def shadow_text(canvas, xy, txt, font, fill=(255, 255, 255), anchor='mm', blur=10, strength=200, spacing=0):
    sh = Image.new('L', canvas.size, 0); ImageDraw.Draw(sh).text(xy, txt, font=font, fill=strength, anchor=anchor)
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    canvas.paste(Image.new('RGB', canvas.size, (30, 18, 10)), (0, 0), sh)
    ImageDraw.Draw(canvas).text(xy, txt, font=font, fill=fill, anchor=anchor)
def spaced(canvas, cx, y, txt, font, gap=6, fill=(255, 255, 255)):
    d = ImageDraw.Draw(canvas); widths = [d.textlength(c, font=font) for c in txt]; tot = sum(widths) + gap * (len(txt) - 1)
    x = cx - tot / 2
    for c, wd in zip(txt, widths): shadow_text(canvas, (x + wd / 2, y), c, font, anchor='mm', blur=6, strength=170); x += wd + gap
def vignette(canvas, top=0.0, bottom=0.0, mid=0.0):
    """Darken bands so white text holds contrast at feed size."""
    g = Image.new('L', (1, H))
    for y in range(H):
        t = y / H; v = 0
        v = max(v, int(255 * top * max(0, 1 - t / 0.35)))
        v = max(v, int(255 * bottom * max(0, (t - 0.6) / 0.4)))
        v = max(v, int(255 * mid * max(0, 1 - abs(t - 0.5) / 0.22)))
        g.putpixel((0, y), v)
    canvas.paste(Image.new('RGB', canvas.size, (20, 12, 6)), (0, 0), g.resize(canvas.size))
def logo(canvas, size=92, pos=(22, 18)):
    lg = Image.open(LOGO).convert('RGBA'); lg.thumbnail((size, size), Image.LANCZOS); canvas.paste(lg, pos, lg)
def mark(canvas, cx, cy, ok, r=34):
    """A thin, elegant check or cross in a white ring (not a cartoon red X)."""
    d = ImageDraw.Draw(canvas); d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255))
    col = (46, 110, 70) if ok else (150, 30, 40)
    if ok: d.line([(cx - 15, cy + 1), (cx - 4, cy + 13), (cx + 17, cy - 12)], fill=col, width=7, joint='curve')
    else:
        d.line([(cx - 13, cy - 13), (cx + 13, cy + 13)], fill=col, width=7); d.line([(cx + 13, cy - 13), (cx - 13, cy + 13)], fill=col, width=7)

# ---------- A: the channel's own proven formula (3 panels, serif headline) ----------
A = Image.new('RGB', (W, H))
for k, (f, fy) in enumerate([('lc8', 0.2), ('a2', 0.22), ('a3', 0.25)]):
    A.paste(fill(f'{SRC}/{f}.jpg', 427, H, fy), (k * 427, 0))
vignette(A, top=0.25, mid=0.55)
spaced(A, W // 2, 262, 'THIS WINTER', serif(34, 500), gap=7)
shadow_text(A, (W // 2, 352), 'Avoid These', serif(132, 800), blur=14, strength=230)
logo(A); A.save(f'{D}/thumb_A_proven.jpg', quality=95)

# ---------- B: before / after contrast (fleece vs elegant coat) ----------
B = Image.new('RGB', (W, H), (195, 141, 98))
B.paste(fill(f'{SRC}/f14.jpg', 640, H, 0.12), (0, 0)); B.paste(fill(f'{SRC}/cr14.jpg', 640, H, 0.12, fx=0.55), (640, 0))
ImageDraw.Draw(B).rectangle((636, 0, 643, H), fill=(255, 255, 255))
vignette(B, bottom=0.7)
shadow_text(B, (320, 612), 'Cheap', serif(112, 800), blur=12, strength=230)
shadow_text(B, (960, 612), 'Chic', serif(112, 800), blur=12, strength=230)
mark(B, 320, 500, False); mark(B, 960, 500, True)
logo(B); B.save(f'{D}/thumb_B_before_after.jpg', quality=95)

# ---------- C: one hero + curiosity about the hook ("number four is in almost every closet") ----------
C = fill(f'{SRC}/c1.jpg', W, H, 0.3)
C = Image.new('RGB', (W, H), (195, 141, 98))
cd = ImageDraw.Draw(C)
for r_ in range(900, 0, -6):                       # the channel's warm caramel glow
    c_ = int(r_ / 900 * 40); cd.ellipse((900 - r_, 330 - r_ * 0.8, 900 + r_, 330 + r_ * 0.8), fill=(219 - c_, 167 - c_, 120 - c_))
C.paste(fill(f'{SRC}/c1.jpg', 520, H, 0.55, zoom=1.55, fx=0.45), (0, 0))
# the mystery item: a fleece zip-up in a ring with a cross
inset = fill(f'{SRC}/c2.jpg', 300, 300, 0.32); m = Image.new('L', (300, 300), 0); ImageDraw.Draw(m).ellipse((0, 0, 299, 299), fill=255)
ring = Image.new('RGBA', (316, 316), (0, 0, 0, 0)); ImageDraw.Draw(ring).ellipse((0, 0, 315, 315), fill=(255, 255, 255, 255))
C.paste(ring, (812, 64), ring); C.paste(inset, (820, 72), m); mark(C, 1088, 330, False, r=30)
shadow_text(C, (900, 470), '#4 Is', serif(96, 800), blur=12, strength=230)
shadow_text(C, (900, 580), 'Everywhere', serif(96, 800), blur=12, strength=230)
logo(C); C.save(f'{D}/thumb_C_curiosity.jpg', quality=95)

# feed-size preview: how each reads at the size people actually see it
prev = Image.new('RGB', (3 * 360 + 40, 2 * 202 + 260 + 30), (245, 245, 245))
for k, n in enumerate(['thumb_A_proven', 'thumb_B_before_after', 'thumb_C_curiosity']):
    im = Image.open(f'{D}/{n}.jpg')
    prev.paste(im.resize((360, 202), Image.LANCZOS), (10 + k * 370, 10))
    prev.paste(im.resize((168, 94), Image.LANCZOS), (10 + k * 370, 230))
prev.save(f'{D}/preview_feed.jpg', quality=90)
print('ok')
