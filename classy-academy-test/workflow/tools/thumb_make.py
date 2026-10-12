# Channel-DNA thumbnails, measured from "8 Things Elegant Ladies Never Wear" (1.24M):
#  panels x: 0-401 | 403-850 | 852-1280, thin light dividers
#  top line: Cormorant SC, cap height 46px, top y=200 | headline: Montserrat Bold, cap height 108px, top y=296
#  red underline (150,22,26) under the FIRST word, y=418-421 | small line: Cormorant SC, cap height 26px, top y=495
#  soft drop shadow on all text, CE logo top-left. Real photos only (Ines de la Fressange, Caroline de Maigret, Jeanne Damas).
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crop import crop
T_ = os.path.dirname(os.path.abspath(__file__)); D = os.getcwd(); FD = T_ + '/../assets/fonts/'; LOGO = T_ + '/../assets/logo_ce.png'
W, H = 1280, 720; XS = [0, 402, 851, W]

def sized(path, cap, var=None, probe='H'):
    """Font size whose capital height is `cap` px."""
    for s in range(10, 400):
        f = ImageFont.truetype(path, s)
        if var:
            try: f.set_variation_by_axes([var])
            except Exception: pass
        b = f.getbbox(probe)
        if b[3] - b[1] >= cap: return f
def finish(im):
    im = ImageEnhance.Color(im).enhance(0.88); im = ImageEnhance.Contrast(im).enhance(1.04)
    im = ImageEnhance.Brightness(im).enhance(0.86); im = ImageEnhance.Sharpness(im).enhance(1.25)
    return Image.blend(im, Image.new('RGB', im.size, (205, 170, 140)), 0.05)
def panel(k, w, fw=0.30, fy=0.22, dx=0):
    import crop as C
    oldPW = C.PW; C.PW = w; c, s = C.crop(k, fw, fy); C.PW = oldPW
    return finish(c)
def build(panels, top, big, small, out):
    c = Image.new('RGB', (W, H))
    for (k, fw, fy), x0, x1 in zip(panels, XS, XS[1:]): c.paste(panel(k, x1 - x0, fw, fy), (x0, 0))
    # gentle darkening behind the text block (as in the channel's thumbnails)
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((150, 150, W - 150, 600), fill=95)
    c.paste(Image.new('RGB', (W, H), (18, 12, 8)), (0, 0), g.filter(ImageFilter.GaussianBlur(90)))
    d = ImageDraw.Draw(c)
    for x in (XS[1], XS[2]): d.rectangle((x - 1, 0, x, H), fill=(236, 228, 220))
    ft = sized(FD + 'CormorantSC-Regular.ttf', 46, probe='E'); fb = sized(FD + 'Montserrat.ttf', 108, 700, 'N'); fs = sized(FD + 'CormorantSC-Regular.ttf', 26, probe='A')
    def top_y(f, txt, ytop): return ytop - f.getbbox(txt)[1]
    lines = [(ft, top, top_y(ft, top, 200)), (fb, big, top_y(fb, big, 296))] + ([(fs, small, top_y(fs, small, 495))] if small else [])
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    for f, t, y in lines: ds.text((W / 2 + 3, y + 5), t, font=f, fill=200, anchor='ma')
    c.paste(Image.new('RGB', (W, H), (12, 8, 6)), (0, 0), sh.filter(ImageFilter.GaussianBlur(7)))
    d = ImageDraw.Draw(c)
    for f, t, y in lines: d.text((W / 2, y), t, font=f, fill=(255, 255, 255), anchor='ma')
    first = big.split()[0]; bb = d.textbbox((W / 2, lines[1][2]), big, font=fb, anchor='ma'); fw_ = d.textlength(first, font=fb)
    fb_ = d.textbbox((bb[0], lines[1][2]), first, font=fb, anchor='la'); uy = max(418, fb_[3] + 8)
    d.rectangle((bb[0] + 14, uy, bb[0] + fw_ + 4, uy + 3), fill=(150, 22, 26))
    lg = Image.open(LOGO).convert('RGBA'); lg.thumbnail((96, 96), Image.LANCZOS); c.paste(lg, (16, 14), lg)
    c.save(f'{D}/{out}', quality=95); return c

if __name__ == '__main__':
    # usage (inside the work folder, after real_search.py filled real/):
    #   python3 thumb_make.py OUT.jpg "Top Line" "Big Words" "*small line*" key1 key2 key3
    # keys are real/<key>.jpg photos (left, centre, right). Faces are found and framed like the channel's thumbnails.
    a = sys.argv[1:]
    build([(k, 0.30, 0.20) for k in a[4:7]], a[1], a[2], a[3], a[0]); print('ok', a[0])
