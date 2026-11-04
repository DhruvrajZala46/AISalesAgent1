# B: the channel's two-panel "Cheap x / Chic v" layout (7 Things Elegant Ladies Never Wear in Winter), CE logo top-left
import json, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools')
from pc import pcrop
FD = '/home/user/AISalesAgent1/classy-academy-test/workflow/assets/fonts/'
B = json.load(open('fr/best.json'))
def build(out, left, right, wl, wr, fwl=0.42, fwr=0.42, fyl=0.24, fyr=0.24):
    W, H = 1280, 720; c = Image.new('RGB', (W, H))
    a, _ = pcrop(f'fr/{left}.png', 640, fw=fwl, fy=fyl, box=B[left]['face']); b, _ = pcrop(f'fr/{right}.png', 640, fw=fwr, fy=fyr, box=B[right]['face'])
    c.paste(a, (0, 0)); c.paste(b, (640, 0))
    g = Image.new('L', (W, H), 0); dg = ImageDraw.Draw(g)
    for y in range(380, H): dg.line((0, y, W, y), fill=int(150 * ((y - 380) / (H - 380)) ** 1.3))
    c.paste(Image.new('RGB', (W, H), (16, 10, 6)), (0, 0), g)
    d = ImageDraw.Draw(c); d.rectangle((639, 0, 641, H), fill=(236, 228, 220))
    f = ImageFont.truetype(FD + 'PlayfairDisplay.ttf', 128)
    try: f.set_variation_by_axes([700])
    except Exception: pass
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    for cx, w in ((320, wl), (960, wr)): ds.text((cx + 3, 640 + 5), w, font=f, fill=220, anchor='ms')
    c.paste(Image.new('RGB', (W, H), (10, 6, 4)), (0, 0), sh.filter(ImageFilter.GaussianBlur(8)))
    d = ImageDraw.Draw(c)
    for cx, w in ((320, wl), (960, wr)): d.text((cx, 640), w, font=f, fill=(255, 255, 255), anchor='ms')
    # the marks: white disc, red cross / dark green tick (as on the channel's winter thumbnail)
    for cx, kind in ((320, 'x'), (960, 'v')):
        cy = 470; r = 34
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(250, 248, 245))
        if kind == 'x':
            d.line((cx - 13, cy - 13, cx + 13, cy + 13), fill=(176, 32, 38), width=8); d.line((cx - 13, cy + 13, cx + 13, cy - 13), fill=(176, 32, 38), width=8)
        else:
            d.line((cx - 15, cy + 1, cx - 4, cy + 13), fill=(40, 96, 72), width=8); d.line((cx - 4, cy + 13, cx + 17, cy - 12), fill=(40, 96, 72), width=8)
    lg = Image.open('/home/user/AISalesAgent1/classy-academy-test/workflow/assets/logo_ce.png').convert('RGBA'); lg.thumbnail((96, 96), Image.LANCZOS); c.paste(lg, (16, 14), lg)
    c.save(out, quality=95); print(out)
build('B.jpg', 'b_jabot26', 'b_silk39', 'Ages You', 'Ageless', fwl=0.40, fwr=0.40, fyl=0.26, fyr=0.26)
