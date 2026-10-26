# The topic's proven thumbnail: ONE garment, before | after, side by side, a few words across the split
# (JairWoo 197x, Ramya Vasudev 77x, Just Marina 330x: faded -> black; Jordan O'Brien 121x "TIGHT -> LOOSE";
#  Miarti 219x / FashionByAlly 347x: red cross / green tick), drawn in the channel's type: Montserrat Bold, Cormorant SC, CE logo.
import sys, json
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'workflow', 'tools'))
import thumb_make as M, thumb_xo as X
from PIL import Image, ImageDraw, ImageFilter
W, H = 1280, 720; MID = 640
def half(path, box, w):
    im = Image.open(path).convert('RGB').crop(box)
    s = max(w / im.width, H / im.height); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    L = (im.width - w) // 2; T = (im.height - H) // 2
    from PIL import ImageEnhance as E
    im = im.crop((L, T, L + w, T + H)); im = E.Color(im).enhance(0.92); im = E.Contrast(im).enhance(1.05); im = E.Sharpness(im).enhance(1.3)
    return Image.blend(im, Image.new('RGB', im.size, (205, 170, 140)), 0.04)
def build(sp):
    c = Image.new('RGB', (W, H))
    c.paste(half(sp['before'], sp['bbox'], MID - 2), (0, 0)); c.paste(half(sp['after'], sp['abox'], W - MID - 2), (MID + 2, 0))
    ImageDraw.Draw(c).rectangle((MID - 2, 0, MID + 1, H), fill=(236, 228, 220))
    g = Image.new('L', (W, H), 0); gd = ImageDraw.Draw(g)                      # soft darkening behind the words
    for y in range(H): gd.line((0, y, W, y), fill=int(max(0, (y - sp.get('dark_from', 380)) / (H - sp.get('dark_from', 380))) * 170))
    c.paste(Image.new('RGB', (W, H), (14, 9, 6)), (0, 0), g.filter(ImageFilter.GaussianBlur(20)))
    c = c.convert('RGBA')
    if sp.get('marks'):
        for k, x in (('no', sp.get('mx', [470, 1150])[0]), ('yes', sp.get('mx', [470, 1150])[1])):
            b = X.badge(k, 120); c.alpha_composite(b, (x - 60, sp.get('my', 40)))
    fb = M.sized(M.FD + 'Montserrat.ttf', sp.get('cap', 96), 700, 'N')
    words = sp['big']; y = sp.get('y', 560)
    ft = M.sized(M.FD + 'CormorantSC-Regular.ttf', 40, probe='E') if sp.get('top') else None
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    ds.text((W / 2 + 3, y + 5), words, font=fb, fill=210, anchor='ms')
    if ft: ds.text((W / 2 + 2, y - fb.getbbox('N')[3] - 30 + 3), sp['top'], font=ft, fill=200, anchor='ms')
    dk = Image.new('RGBA', (W, H), (12, 8, 6, 0)); dk.putalpha(sh.filter(ImageFilter.GaussianBlur(7))); c.alpha_composite(dk)
    d = ImageDraw.Draw(c)
    d.text((W / 2, y), words, font=fb, fill=(255, 255, 255), anchor='ms')
    if sp.get('arrow'):
        ax0, ax1, ay = sp['arrow']
        for dx, dy, col in ((3, 5, (20, 12, 8)), (0, 0, (255, 255, 255))):
            d.line((ax0 + dx, ay + dy, ax1 - 26 + dx, ay + dy), fill=col, width=20)
            d.polygon([(ax1 + dx, ay + dy), (ax1 - 52 + dx, ay - 38 + dy), (ax1 - 52 + dx, ay + 38 + dy)], fill=col)
    if ft: d.text((W / 2, y - fb.getbbox('N')[3] - 30), sp['top'], font=ft, fill=(255, 255, 255), anchor='ms')
    if sp.get('underline'):
        first = words.split()[0]; bb = d.textbbox((W / 2, y), words, font=fb, anchor='ms'); fw = d.textlength(first, font=fb)
        d.rectangle((bb[0] + 8, y + 20, bb[0] + fw - 4, y + 24), fill=(150, 22, 26))
    lg = Image.open(M.LOGO).convert('RGBA'); lg.thumbnail((96, 96), Image.LANCZOS); c.alpha_composite(lg, (16, 14))
    c.convert('RGB').save(sp['out'], quality=95)
if __name__ == '__main__':
    for f in sys.argv[1:]: build(json.load(open(f))); print('ok', f)
