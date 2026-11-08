# B (winter expensive): one elegant woman beside the video's own "one outfit, any budget" pieces cut out on its caramel.
# Copies the topic's winners (Anna Bey, "10 Ways To Look Expensive On A Budget In Winter", 830k: the woman beside cut-out
# pieces; "Look Expensive On A Budget", 2.59M) in the channel's own words and fonts (Cormorant SC + Montserrat 800).
import json, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools'); sys.path.insert(0, '.')
import types; sys.modules.setdefault('crop', types.SimpleNamespace(crop=None))
from thumb_make import sized, FD
from pc import pcrop
spec = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}
W, H = 1280, 720; XL = spec.get('xl', 690)
A = '/tmp/claude-0/-home-user-AISalesAgent1/140e17c2-af15-50d0-a685-731162836c6b/scratchpad/cwy/assets/'
F = json.load(open('faces_auto.json'))
c = Image.new('RGB', (W, H))
bg = Image.open(A + 'bg.png').convert('RGB').resize((W, H)); c.paste(bg.crop((0, 0, XL, H)), (0, 0))
who = spec.get('who', 'ines21')
R, s = pcrop(f'orig/{who}.jpg', W - XL, fw=spec.get('fw', 0.2), fy=spec.get('fy', 0.16), dx=spec.get('dx', 0.0), box=F[who])
R = ImageEnhance.Sharpness(R).enhance(1.1); c.paste(R, (XL, 0)); print('photo src px per out px', round(s, 2))
def put(png, cx, ybot, hh, rot=0):
    im = Image.open(A + png).convert('RGBA'); r = im.width / im.height; im = im.resize((int(hh * r), hh), Image.LANCZOS)
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    sh = Image.new('L', c.size, 0); sh.paste(im.split()[3].point(lambda v: v * 0.42), (int(cx - im.width / 2) + 8, ybot - im.height + 14))
    c.paste(Image.new('RGB', c.size, (60, 30, 12)), (0, 0), sh.filter(ImageFilter.GaussianBlur(14)))
    c.paste(im, (int(cx - im.width / 2), ybot - im.height), im)
for png, cx, ybot, hh in spec.get('pieces', [('ph_camelcoat.png', 118, 690, 330), ('ph_creamknit.png', 285, 655, 205),
                                             ('ph_tailtrous.png', 445, 690, 320), ('ph_boots.png', 590, 690, 235)]):
    put(png, cx, ybot, hh)
d = ImageDraw.Draw(c); d.rectangle((XL - 2, 0, XL + 2, H), fill=(246, 242, 236))
# words, centred on the caramel: the same fonts, sizes and double shadow as the 3-photo thumbnails (v3 "bold")
cx = XL / 2
ft = sized(FD + 'CormorantSC-Regular.ttf', spec.get('top_cap', 54), probe='M')
fb = sized(FD + 'Montserrat.ttf', spec.get('cap', 100), 800, 'R')
while d.textlength(spec.get('big', 'Expensive'), font=fb) > XL - 70:
    fb = ImageFont.truetype(FD + 'Montserrat.ttf', fb.size - 2); fb.set_variation_by_axes([800])
fs = sized(FD + 'CormorantSC-Regular.ttf', spec.get('small_cap', 40), probe='W')
top, big, small = spec.get('top', 'Look'), spec.get('big', 'Expensive'), spec.get('small', 'on Any Budget')
yb = spec.get('yb', 128); bh = fb.getbbox('R')[3] - fb.getbbox('R')[1]
lines = [(ft, top, yb - 16 - (ft.getbbox('M')[3] - ft.getbbox('M')[1]), 1), (fb, big, yb, 0), (fs, small, yb + bh + 52, 1)]
def top_of(f, t, y): return y - f.getbbox(t)[1]
for blur, off, alpha in ((22, 0, 170), (5, 4, 235)):
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    for f, tx, y, sw in lines: ds.text((cx + off * 0.6, top_of(f, tx, y) + off), tx, font=f, fill=alpha, anchor='ma', stroke_width=sw + 3)
    c.paste(Image.new('RGB', (W, H), (6, 4, 2)), (0, 0), sh.filter(ImageFilter.GaussianBlur(blur)))
d = ImageDraw.Draw(c)
for f, tx, y, sw in lines: d.text((cx, top_of(f, tx, y)), tx, font=f, fill=(255, 255, 255), anchor='ma', stroke_width=sw, stroke_fill=(255, 255, 255))
yt = top_of(fb, big, yb); bb = d.textbbox((cx, yt), big, font=fb, anchor='ma'); uy = bb[3] + 12
ush = Image.new('L', (W, H), 0); ImageDraw.Draw(ush).rectangle((bb[0] - 4, uy + 3, bb[2] + 8, uy + 11), fill=200)
c.paste(Image.new('RGB', (W, H), (6, 4, 2)), (0, 0), ush.filter(ImageFilter.GaussianBlur(4)))
d = ImageDraw.Draw(c); d.rectangle((bb[0] - 8, uy, bb[2] + 4, uy + 7), fill=(170, 24, 30))
for i in range(6):
    d.line((0, i, W, i), fill=(253, 212, 160)); d.line((0, H - 1 - i, W, H - 1 - i), fill=(250, 214, 166))
    d.line((i, 0, i, H), fill=(253, 244, 229)); d.line((W - 1 - i, 0, W - 1 - i, H), fill=(253, 244, 229))
lg = Image.open(FD + '../logo_ce.png').convert('RGBA'); lg.thumbnail((96, 96), Image.LANCZOS); c.paste(lg, (22, 18), lg)
out = spec.get('out', 'B.jpg'); c.save(out, quality=95); print(out)
