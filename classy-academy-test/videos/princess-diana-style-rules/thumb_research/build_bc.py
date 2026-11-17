# build_bc.py - thumbnails B (one picture, no words) and C (two pictures, the detail ringed) at 1920x1080
import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
W, H = 1920, 1080
CDI = '/tmp/claude-0/-home-user-AISalesAgent1/140e17c2-af15-50d0-a685-731162836c6b/scratchpad/cdi/photos/orig/'
def grade(im, color=1.04, contrast=1.06, bright=0.97, warm=0.04):
    im = ImageEnhance.Color(im).enhance(color); im = ImageEnhance.Contrast(im).enhance(contrast); im = ImageEnhance.Brightness(im).enhance(bright)
    return Image.blend(im, Image.new('RGB', im.size, (205, 170, 140)), warm)
def crop(src, x0, y0, cw, pw, ph=H, sharpen=True):
    im = Image.open(src).convert('RGB'); ch = cw * ph / pw
    c = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((pw, ph), Image.LANCZOS)
    if sharpen: c = c.filter(ImageFilter.UnsharpMask(1.2, 22 if cw < pw else 30, 3))
    return c, round(cw / pw, 2)
def vignette(im, strength=0.42, inner=0.55):
    w, h = im.size; y, x = np.mgrid[0:h, 0:w]; d = np.sqrt(((x - w / 2) / (w / 2)) ** 2 + ((y - h / 2) / (h / 2)) ** 2) / 1.4142
    m = np.clip((d - inner) / (1 - inner), 0, 1) ** 1.6 * strength
    a = np.asarray(im).astype(float) * (1 - m[..., None]); return Image.fromarray(a.clip(0, 255).astype('uint8'))
def logo(im, dark=110):
    L = Image.open('build/logo_ca_hires.png').convert('RGBA'); L = L.resize((round(L.width * 141 / L.height), 141), Image.LANCZOS); lx, ly = 54, 44
    L.putalpha(L.split()[3].point(lambda v: int(v * 0.92))); out = im.convert('RGBA')
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((lx - 75, ly - 68, lx + L.width + 75, ly + L.height + 68), fill=dark)
    ld = Image.new('RGBA', (W, H), (18, 12, 8, 0)); ld.putalpha(g.filter(ImageFilter.GaussianBlur(57))); out = Image.alpha_composite(out, ld)
    a = Image.new('L', (W, H), 0); a.paste(L.split()[3].point(lambda v: v * 0.45), (lx + 2, ly + 3)); sh = Image.new('RGBA', (W, H), (8, 6, 4, 0)); sh.putalpha(a.filter(ImageFilter.GaussianBlur(4.5)))
    out = Image.alpha_composite(out, sh); lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); lay.paste(L, (lx, ly), L); return Image.alpha_composite(out, lay).convert('RGB')
def ring(im, cx, cy, rx, ry=None, width=15, col=(250, 205, 70)):
    ry = ry or rx; out = im.convert('RGBA')
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse((cx - rx + 4, cy - ry + 8, cx + rx + 4, cy + ry + 8), outline=210, width=width + 6)
    s = Image.new('RGBA', (W, H), (10, 6, 4, 0)); s.putalpha(sh.filter(ImageFilter.GaussianBlur(9))); out = Image.alpha_composite(out, s)
    big = Image.new('RGBA', (W * 2, H * 2), (0, 0, 0, 0)); ImageDraw.Draw(big).ellipse(((cx - rx) * 2, (cy - ry) * 2, (cx + rx) * 2, (cy + ry) * 2), outline=col + (255,), width=width * 2)
    return Image.alpha_composite(out, big.resize((W, H), Image.LANCZOS)).convert('RGB')
def B(y0=165, name='B_one_picture'):
    im, s = crop('photos/orig/trev_13.jpg', 0, y0, 1600, W); im = vignette(grade(im)); im = logo(im, 120)
    im.save(name + '.jpg', quality=95); im.save(name + '.png'); print(name, 'source px per output px', s)
def C(name='C_the_detail'):
    out = Image.new('RGB', (W, H))
    a, sa = crop(CDI + 'pclutchb_5.jpg', 20, 130, 1400, 1280); b, sb = crop(CDI + 'pjapan_0.jpg', 20, 40, 600, 640)
    out.paste(grade(a, bright=1.0), (0, 0)); out.paste(grade(b, color=1.0, bright=0.97), (1280, 0))
    ImageDraw.Draw(out).rectangle((1278, 0, 1281, H), fill=(236, 228, 220))
    out = vignette(out, 0.30, 0.6)
    out = ring(out, 585, 612, 158); out = ring(out, 1280 + 480, 864, 128)
    out = logo(out, 120); out.save(name + '.jpg', quality=95); out.save(name + '.png'); print(name, 'source px per output px', sa, sb)
if __name__ == '__main__':
    for n in sys.argv[1:] or ['B', 'C']: globals()[n]()
