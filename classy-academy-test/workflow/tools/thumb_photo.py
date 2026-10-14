# thumb_photo.py - one real photo on one side, fading into the caramel backdrop, words on the other side, and the tip
# drawn on her (white ring + small white labels, like the video). The "test / question" thumbnail: Glamrs "WHAT'S YOUR
# BODY SHAPE?" 1.48M (90x), Jules Beth hand-on-waist 0.45M (50x), Justine Leconte measuring 1.66M (10x); the hand test
# was the biggest replay moment of the whole topic (Asia Jackson, 10.7x her video's median). Our look: caramel,
# Montserrat + Cormorant SC, red underline, CE logo.
# usage (inside the thumbnail folder):  python3 thumb_photo.py spec.json
# spec.json: {"out": "B.jpg", "photo": "frame.png", "scale": 0.72, "src_y": 20, "side": "right",
#             "top": "WHICH ONE", "big": "ARE YOU?", "small": "*the hand test*",
#             "rings": [[cx, cy, rx, ry]], "tags": [{"text": "short torso", "x": 700, "y": 400}]}   # canvas coords
import os, sys, json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thumb_xo as X
import thumb_shape as S
W, H = X.W, X.H

def build(spec):
    c = X.backdrop().convert('RGBA')
    im = Image.open(spec['photo']).convert('RGB'); s = spec.get('scale', H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    y0 = round(spec.get('src_y', 0) * s); im = im.crop((0, y0, im.width, y0 + H))
    im = ImageEnhance.Brightness(ImageEnhance.Color(im).enhance(0.92)).enhance(0.95)     # the channel's gentle grade
    right = spec.get('side', 'right') == 'right'; pw = im.width; x = W - pw if right else 0
    fade = spec.get('fade', 150)                                                        # soft edge into the caramel
    m = np.full((H, pw), 255, np.float32); ramp = np.linspace(0, 255, fade)
    if right: m[:, :fade] = ramp
    else: m[:, -fade:] = ramp[::-1]
    ph = im.convert('RGBA'); ph.putalpha(Image.fromarray(m.astype(np.uint8))); c.alpha_composite(ph, (x, 0))
    ln = Image.new('RGBA', (W, H), (0, 0, 0, 0)); shd = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    dl, ds = ImageDraw.Draw(ln), ImageDraw.Draw(shd)
    for cx, cy, rx, ry in spec.get('rings', []):
        ds.ellipse((cx - rx + 2, cy - ry + 3, cx + rx + 2, cy + ry + 3), outline=(30, 15, 5, 150), width=10)
        dl.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), outline=(255, 255, 255, 255), width=6)
    for L in spec.get('lines', []):
        pts = [tuple(p) for p in L['pts']]; S.dashed(dl, pts, L.get('w', 6)); S.dashed(ds, [(a + 2, b + 3) for a, b in pts], L.get('w', 6) + 4, fill=(30, 15, 5, 150))
    c.alpha_composite(shd.filter(ImageFilter.GaussianBlur(4))); c.alpha_composite(ln)
    d = ImageDraw.Draw(c)
    for t in spec.get('tags', []):
        f = X.font(X.FD + 'CormorantSC-Regular.ttf', t.get('size', 32)); bb = d.textbbox((t['x'], t['y']), t['text'], font=f, anchor='mm')
        d.rounded_rectangle((bb[0] - 16, bb[1] - 9, bb[2] + 16, bb[3] + 11), radius=22, fill=(255, 255, 255, 240))
        d.text((t['x'], t['y']), t['text'], font=f, fill=(60, 40, 30), anchor='mm')
    # the words, centred in the caramel side
    tw = (W - pw) if right else (W - pw); cxw = tw / 2 + (0 if right else pw)
    block = Image.new('RGBA', (W, H), (0, 0, 0, 0)); S.text_block(block, spec.get('top', ''), spec['big'], spec.get('small', ''), spec.get('text_w', tw - 90))
    # text_block centres on the canvas and adds the logo; shift the words to the caramel side, logo top-left
    lg = Image.open(X.LOGO).convert('RGBA'); lg.thumbnail((92, 92), Image.LANCZOS)
    bx = round(cxw - W / 2); band = block.crop((0, 120, W, H)); c.alpha_composite(band, (bx, 120)) if bx >= 0 else c.alpha_composite(band.crop((-bx, 0, W, H - 120)), (0, 120))
    c.alpha_composite(lg, (24, 18))
    c.convert('RGB').save(spec['out'], quality=95); return spec['out']

if __name__ == '__main__':
    print('ok', build(json.load(open(sys.argv[1]))))
