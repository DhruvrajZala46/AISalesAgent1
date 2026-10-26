# Channel-DNA 3-panel thumbnail (tools/thumb_make.py layout, measured on the channel's thumbnails), with two additions the
# channel itself uses: a product/detail panel framed by hand (no face: e.g. the jewelry and shoes thumbnails), and the red
# underline only when asked (the channel draws it on its "Never ..." thumbnails).
import sys, json
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'workflow', 'tools'))
import thumb_make as M, crop as C
from PIL import Image, ImageDraw, ImageFilter
W, H, XS = M.W, M.H, M.XS
def detail(k, w, box, flip=False):
    """a hand-framed panel: box = (x0, y0, x1, y1) of the source photo, scaled to cover the panel"""
    im = Image.open(f'real/{k}.jpg').convert('RGB')
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im = im.crop(box)
    s = max(w / im.width, H / im.height); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    L = (im.width - w) // 2; T = (im.height - H) // 2
    return M.finish(im.crop((L, T, L + w, T + H)))
def build(spec):
    c = Image.new('RGB', (W, H))
    for p, x0, x1 in zip(spec['panels'], XS, XS[1:]):
        c.paste(detail(p['k'], x1 - x0, p['box'], p.get('flip', False)) if 'box' in p else M.panel(p['k'], x1 - x0, p.get('fw', 0.30), p.get('fy', 0.20)), (x0, 0))
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((150, 150, W - 150, 600), fill=spec.get('dark', 95))
    c.paste(Image.new('RGB', (W, H), (18, 12, 8)), (0, 0), g.filter(ImageFilter.GaussianBlur(90)))
    d = ImageDraw.Draw(c)
    for x in (XS[1], XS[2]): d.rectangle((x - 1, 0, x, H), fill=(236, 228, 220))
    ft = M.sized(M.FD + 'CormorantSC-Regular.ttf', 46, probe='E'); fb = M.sized(M.FD + 'Montserrat.ttf', spec.get('cap', 108), 700, 'N'); fs = M.sized(M.FD + 'CormorantSC-Regular.ttf', 26, probe='A')
    top, big, small = spec['top'], spec['big'], spec.get('small', '')
    ty = lambda f, t, y: y - f.getbbox(t)[1]
    lines = [(ft, top, ty(ft, top, 200)), (fb, big, ty(fb, big, 296))] + ([(fs, small, ty(fs, small, 495))] if small else [])
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    for f, t, y in lines: ds.text((W / 2 + 3, y + 5), t, font=f, fill=200, anchor='ma')
    c.paste(Image.new('RGB', (W, H), (12, 8, 6)), (0, 0), sh.filter(ImageFilter.GaussianBlur(7)))
    d = ImageDraw.Draw(c)
    for f, t, y in lines: d.text((W / 2, y), t, font=f, fill=(255, 255, 255), anchor='ma')
    if spec.get('underline'):
        first = big.split()[0]; bb = d.textbbox((W / 2, lines[1][2]), big, font=fb, anchor='ma'); fw_ = d.textlength(first, font=fb)
        fb_ = d.textbbox((bb[0], lines[1][2]), first, font=fb, anchor='la'); uy = max(418, fb_[3] + 8)
        d.rectangle((bb[0] + 14, uy, bb[0] + fw_ + 4, uy + 3), fill=(150, 22, 26))
    for x, y, t in spec.get('labels', []):                      # small year labels, Cormorant SC, like the small line
        fl = M.sized(M.FD + 'CormorantSC-Regular.ttf', 30, probe='0')
        sl = Image.new('L', (W, H), 0); ImageDraw.Draw(sl).text((x + 2, y + 3), t, font=fl, fill=220, anchor='ma')
        c.paste(Image.new('RGB', (W, H), (12, 8, 6)), (0, 0), sl.filter(ImageFilter.GaussianBlur(5)))
        ImageDraw.Draw(c).text((x, y), t, font=fl, fill=(255, 255, 255), anchor='ma')
    lg = Image.open(M.LOGO).convert('RGBA'); lg.thumbnail((96, 96), Image.LANCZOS); c.paste(lg, (16, 14), lg)
    c.save(spec['out'], quality=95); return c
if __name__ == '__main__':
    for f in sys.argv[1:]: build(json.load(open(f))); print('ok', f)
