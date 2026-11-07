# B: the channel's two-half "x / v" layout (its "Cheap / Chic" winter thumbnail) + the 600k topic winner's mistakes shown
# as products (Anna Bey, "Holiday Outfits That Don't Look Classy": a reindeer sweater and a sequin mini, "LOOKS CHEAP!")
import json, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, '.')
from pc import pcrop
FD = '/home/user/AISalesAgent1/classy-academy-test/workflow/assets/fonts/'
F = json.load(open('faces_auto.json'))
W, H = 1280, 720; c = Image.new('RGB', (W, H))
# left: the mistakes on the video's own caramel backdrop
bg = Image.open('/tmp/claude-0/-home-user-AISalesAgent1/140e17c2-af15-50d0-a685-731162836c6b/scratchpad/cwx/assets/bg.png').convert('RGB').resize((W, H)).crop((0, 0, 640, H))
c.paste(bg, (0, 0))
def put(png, cx, ybot, hh, rot=0):
    im = Image.open(png).convert('RGBA'); r = im.width / im.height; im = im.resize((int(hh * r), hh), Image.LANCZOS)
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
    sh = Image.new('L', c.size, 0); sh.paste(im.split()[3].point(lambda v: v * 0.45), (int(cx - im.width / 2) + 10, ybot - im.height + 18))
    c.paste(Image.new('RGB', c.size, (60, 30, 12)), (0, 0), sh.filter(ImageFilter.GaussianBlur(16)))
    c.paste(im, (int(cx - im.width / 2), ybot - im.height), im)
put('assets/ph_ugly14.png', 205, 470, 400, rot=6)
put('assets/ph_seqmini6.png', 455, 520, 470, rot=-5)
R, s = pcrop('orig/kate_bow10.jpg', 640, fw=0.24, fy=0.17, box=F['kate_bow10'])
c.paste(R, (640, 0)); print('right panel src px per out px', round(s, 2))
g = Image.new('L', (W, H), 0); dg = ImageDraw.Draw(g)
for y in range(420, H): dg.line((0, y, W, y), fill=int(130 * ((y - 420) / (H - 420)) ** 1.3))
c.paste(Image.new('RGB', (W, H), (16, 10, 6)), (0, 0), g)
d = ImageDraw.Draw(c); d.rectangle((639, 0, 641, H), fill=(236, 228, 220))
f = ImageFont.truetype(FD + 'PlayfairDisplay.ttf', 128)
try: f.set_variation_by_axes([700])
except Exception: pass
sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
for cx, w in ((320, 'Cheap'), (960, 'Chic')): ds.text((cx + 3, 660 + 5), w, font=f, fill=220, anchor='ms')
c.paste(Image.new('RGB', (W, H), (10, 6, 4)), (0, 0), sh.filter(ImageFilter.GaussianBlur(8)))
d = ImageDraw.Draw(c)
for cx, w in ((320, 'Cheap'), (960, 'Chic')): d.text((cx, 660), w, font=f, fill=(255, 255, 255), anchor='ms')
for cx, cy, kind in ((320, 510, 'x'), (960, 510, 'v')):
    r = 34; d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(250, 248, 245))
    if kind == 'x':
        d.line((cx - 13, cy - 13, cx + 13, cy + 13), fill=(176, 32, 38), width=8); d.line((cx - 13, cy + 13, cx + 13, cy - 13), fill=(176, 32, 38), width=8)
    else:
        d.line((cx - 15, cy + 1, cx - 4, cy + 13), fill=(40, 96, 72), width=8); d.line((cx - 4, cy + 13, cx + 17, cy - 12), fill=(40, 96, 72), width=8)
lg = Image.open('/home/user/AISalesAgent1/classy-academy-test/workflow/assets/logo_ce.png').convert('RGBA'); lg.thumbnail((96, 96), Image.LANCZOS); c.paste(lg, (16, 14), lg)
c.save('B.jpg', quality=95); print('B.jpg')
