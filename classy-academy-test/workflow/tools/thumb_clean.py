# thumb_clean.py - the Classy Academy / Classy Elegance 3-photo thumbnail, measured on the creator's own examples (7 Nov 2026):
# clean bright photos (no darkening, no colour wash), white dividers, a thin warm gold-cream frame, Cormorant SC top line,
# Montserrat SemiBold headline, a Cormorant SC or Pinyon script bottom line, soft shadow behind the words, logo top-left.
# usage: python3 thumb_clean.py spec.json   spec: {"out.jpg": {top, big, small, script(bool), logo, panels:[{src, face, fw, fy, dx, xs}]}}
import sys, json
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools')
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import types; sys.modules.setdefault('crop', types.SimpleNamespace(crop=None))
from thumb_make import sized, FD
W, H = 1280, 720
def panel(p, pw):
    im = Image.open(p['src']).convert('RGB'); SW, SH = im.size
    x, y, w, h = p['face']; cw = w / p.get('fw', 0.30); ch = cw * H / pw
    if ch > SH: ch = SH; cw = ch * pw / H
    if cw > SW: cw = SW; ch = cw * H / pw
    cx = x + w / 2 + p.get('dx', 0) * cw; top = y + h / 2 - p.get('fy', 0.25) * ch
    x0 = min(max(cx - cw / 2, 0), SW - cw); y0 = min(max(top, 0), SH - ch)
    c = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((pw, H), Image.LANCZOS)
    c = ImageEnhance.Sharpness(c).enhance(1.15); c = ImageEnhance.Contrast(c).enhance(1.03)
    if p.get('bright'): c = ImageEnhance.Brightness(c).enhance(p['bright'])
    return c, cw / pw
def build(spec, out):
    xs = spec.get('xs', [0, 420, 860, W]); c = Image.new('RGB', (W, H), (250, 244, 232)); info = []
    for p, x0, x1 in zip(spec['panels'], xs, xs[1:]):
        im, s = panel(p, x1 - x0); c.paste(im, (x0, 0)); info.append(round(s, 2))
    if spec.get('dark'):     # a very light veil behind the words only if a photo is too bright for white text
        g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((200, 180, W - 200, 540), fill=spec['dark'])
        c.paste(Image.new('RGB', (W, H), (18, 12, 8)), (0, 0), g.filter(ImageFilter.GaussianBlur(90)))
    d = ImageDraw.Draw(c)
    for x in xs[1:-1]: d.rectangle((x - 2, 0, x + 2, H), fill=(246, 242, 236))
    hw = spec.get('weight', 800); cap = spec.get('cap', 112)
    ft = sized(FD + 'CormorantSC-Regular.ttf', spec.get('top_cap', 56), probe='M'); fb = sized(FD + 'Montserrat.ttf', cap, hw, 'R')
    while d.textlength(spec['big'], font=fb) > 1120:
        fb = ImageFont.truetype(FD + 'Montserrat.ttf', fb.size - 2); fb.set_variation_by_axes([hw])
    fs = sized(FD + 'CormorantSC-Regular.ttf', spec.get('small_cap', 42), probe='W')
    yb = spec.get("yb", 278); bh = fb.getbbox('R')[3] - fb.getbbox('R')[1]
    lines = [(ft, spec['top'], yb - 18 - (ft.getbbox('M')[3] - ft.getbbox('M')[1]), 1), (fb, spec['big'], yb, 0), (fs, spec['small'], yb + bh + 62, 1)]
    def top_of(f, t, y): return y - f.getbbox(t)[1]
    # two shadows so the words stand out on any photo: a wide soft glow and a tight dark drop
    for blur, off, alpha in ((22, 0, 200), (5, 4, 245)):
        sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
        for f, tx, y, sw in lines: ds.text((W / 2 + off * 0.6, top_of(f, tx, y) + off), tx, font=f, fill=alpha, anchor='ma', stroke_width=sw + 3)
        c.paste(Image.new('RGB', (W, H), (6, 4, 2)), (0, 0), sh.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(c)
    for f, tx, y, sw in lines: d.text((W / 2, top_of(f, tx, y)), tx, font=f, fill=(255, 255, 255), anchor='ma', stroke_width=sw, stroke_fill=(255, 255, 255))
    if spec.get('underline'):   # the channel's own highlight: a red line under the first word of the headline
        big = spec['big']; first = big.split()[0]; yt = top_of(fb, big, yb)
        bb = d.textbbox((W / 2, yt), big, font=fb, anchor='ma'); fw_ = d.textbbox((bb[0], yt), first, font=fb, anchor='la')[2] - bb[0]
        uy = bb[3] + 12
        ush = Image.new('L', (W, H), 0); ImageDraw.Draw(ush).rectangle((bb[0] - 4, uy + 3, bb[0] + fw_ + 8, uy + 11), fill=200)
        c.paste(Image.new('RGB', (W, H), (6, 4, 2)), (0, 0), ush.filter(ImageFilter.GaussianBlur(4)))
        d = ImageDraw.Draw(c); d.rectangle((bb[0] - 8, uy, bb[0] + fw_ + 4, uy + 7), fill=(170, 24, 30))
    # thin warm frame: gold top and bottom, cream sides (as measured: ~6 px)
    for i in range(6):
        d.line((0, i, W, i), fill=(253, 212, 160)); d.line((0, H - 1 - i, W, H - 1 - i), fill=(250, 214, 166))
        d.line((i, 0, i, H), fill=(253, 244, 229)); d.line((W - 1 - i, 0, W - 1 - i, H), fill=(253, 244, 229))
    lg = Image.open(FD + '../logo_ce.png').convert('RGBA'); lg.thumbnail((104, 104), Image.LANCZOS); c.paste(lg, (26, 22), lg)
    c.save(out, quality=95); print(out, 'panel src px per out px', info)
if __name__ == '__main__':
    for k, v in json.load(open(sys.argv[1])).items(): build(v, k)
