# B: the channel's two-half "Cheap x / Chic v" layout + a red circle on the mistake (the topic winners' mark)
import json, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, '.')
from pc import pcrop
FD = '/home/user/AISalesAgent1/classy-academy-test/workflow/assets/fonts/'
F = json.load(open('faces.json'))
W, H = 1280, 720; c = Image.new('RGB', (W, H))
L = Image.open('orig/shirttail_12.0.png').convert('RGB').crop((0, 230, 720, 230 + 810)).resize((640, 720), Image.LANCZOS)
R, _ = pcrop('orig/kate1.jpg', 640, fw=0.20, fy=0.12, box=F['kate1'])
c.paste(L, (0, 0)); c.paste(R, (640, 0))
g = Image.new('L', (W, H), 0); dg = ImageDraw.Draw(g)
for y in range(400, H): dg.line((0, y, W, y), fill=int(150 * ((y - 400) / (H - 400)) ** 1.3))
c.paste(Image.new('RGB', (W, H), (16, 10, 6)), (0, 0), g)
d = ImageDraw.Draw(c); d.rectangle((639, 0, 641, H), fill=(236, 228, 220))
# red circle around the shirt hem hanging below the knit (hand-drawn look: two slightly offset strokes)
for off, wdt in ((0, 7), (3, 3)):
    d.ellipse((200 + off, 398 - off, 505 + off, 508 - off), outline=(196, 28, 34), width=wdt)
f = ImageFont.truetype(FD + 'PlayfairDisplay.ttf', 128)
try: f.set_variation_by_axes([700])
except Exception: pass
sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
for cx, w in ((320, 'Cheap'), (960, 'Chic')): ds.text((cx + 3, 640 + 5), w, font=f, fill=220, anchor='ms')
c.paste(Image.new('RGB', (W, H), (10, 6, 4)), (0, 0), sh.filter(ImageFilter.GaussianBlur(8)))
d = ImageDraw.Draw(c)
for cx, w in ((320, 'Cheap'), (960, 'Chic')): d.text((cx, 640), w, font=f, fill=(255, 255, 255), anchor='ms')
for cx, cy, kind in ((568, 452, 'x'), (960, 470, 'v')):
    r = 34; d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(250, 248, 245))
    if kind == 'x':
        d.line((cx - 13, cy - 13, cx + 13, cy + 13), fill=(176, 32, 38), width=8); d.line((cx - 13, cy + 13, cx + 13, cy - 13), fill=(176, 32, 38), width=8)
    else:
        d.line((cx - 15, cy + 1, cx - 4, cy + 13), fill=(40, 96, 72), width=8); d.line((cx - 4, cy + 13, cx + 17, cy - 12), fill=(40, 96, 72), width=8)
lg = Image.open('/home/user/AISalesAgent1/classy-academy-test/workflow/assets/logo_ce.png').convert('RGBA'); lg.thumbnail((96, 96), Image.LANCZOS); c.paste(lg, (16, 14), lg)
c.save('B.jpg', quality=95); print('B.jpg')
