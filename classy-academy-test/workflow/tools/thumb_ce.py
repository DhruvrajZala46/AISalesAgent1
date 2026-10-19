# thumb_ce.py - the channel's thumbnail, rebuilt from its own uploads by pixel overlay (19 Oct 2026):
#   3 real photos edge to edge (x 0-402 | 404-851 | 853-1280, thin light dividers), faces in the top third,
#   warm, slightly darker grade; text centred at x=640 in three lines:
#     top   Cormorant SC Regular, cap height 54, letter-spacing 2, top y=193          ("How to Look", "The Most")
#     big   League Spartan Bold, 166 px (smaller only to fit 1110 px), cap top y=296  ("Expensive", "Elegant Hairstyles")
#     small Cormorant SC Regular, cap height 30, letter-spacing 3, top y = big baseline + 84   ("*Instantly*", "All Hair Types")
#   soft drop shadow under all text; logo top-left (the CA box measured x 59-143, y 43-106; we use our CE logo there).
#   Overlays matched: League Spartan 166 = "Expensive" (How to Look Expensive, 698k), 146 = "Elegant Hairstyles" (951k);
#   Cormorant SC cap 55 + tracking 2 = "Elegant Ladies" (Never Wear, 1.25M). Montserrat (thumb_make.py) was the wrong font.
# usage: python3 thumb_ce.py spec.json   spec = {"out": "T.jpg", "top": "Hair That Looks", "big": "Expensive", "small": "*It's Not the Cut*",
#                                         "panels": [{"img": "a.jpg", "face": [x, y, w, h], "fw": 0.32, "fy": 0.17}, x3], "fonts": "<dir>"}
#   face = the face box in the source image (pixels); fw = face width as a share of the panel; fy = face centre height as a share of 720.
import json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
T_ = os.path.dirname(os.path.abspath(__file__)); LOGO = T_ + '/../assets/logo_ce.png'
W, H = 1280, 720; XS = [(0, 402), (404, 851), (853, 1280)]

def finish(im):
    im = ImageEnhance.Color(im).enhance(0.92); im = ImageEnhance.Contrast(im).enhance(1.04)
    im = ImageEnhance.Brightness(im).enhance(0.90); im = ImageEnhance.Sharpness(im).enhance(1.2)
    return Image.blend(im, Image.new('RGB', im.size, (205, 170, 140)), 0.05)

def panel(p, pw):
    im = Image.open(p['img']).convert('RGB'); iw, ih = im.size; x, y, w, h = p['face']
    s = max(pw * p.get('fw', 0.32) / w, pw / iw, H / ih)
    cx, cy = (x + w / 2) * s, (y + h / 2) * s; im = im.resize((round(iw * s), round(ih * s)), Image.LANCZOS)
    L = min(max(0, round(cx - pw / 2 + p.get('dx', 0) * pw)), im.width - pw); T = min(max(0, round(cy - H * p.get('fy', 0.17))), im.height - H)
    return finish(im.crop((L, T, L + pw, T + H)))

def cap_size(path, cap, probe='E'):
    for s in range(8, 400):
        if ImageFont.truetype(path, s).getbbox(probe)[3] - ImageFont.truetype(path, s).getbbox(probe)[1] >= cap: return s
    return 400

def tracked(d, x, y, t, f, track, fill):
    for ch in t: d.text((x, y), ch, font=f, fill=fill); x += d.textlength(ch, font=f) + track

def width(d, t, f, track): return sum(d.textlength(ch, font=f) for ch in t) + track * (len(t) - 1)

def build(spec):
    FD = spec.get('fonts') or (T_ + '/../assets/fonts')
    c = Image.new('RGB', (W, H))
    for p, (x0, x1) in zip(spec['panels'], XS): c.paste(panel(p, x1 - x0), (x0, 0))
    d = ImageDraw.Draw(c)
    for x0, x1 in XS[1:]: d.rectangle((x0 - 2, 0, x0 - 1, H), fill=(236, 228, 220))
    # gentle darkening behind the text block
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((170, 170, W - 170, 590), fill=85)
    c.paste(Image.new('RGB', (W, H), (18, 12, 8)), (0, 0), g.filter(ImageFilter.GaussianBlur(90)))
    serif = FD + '/CormorantSC-Regular.ttf'; bold = FD + '/LeagueSpartan-Bold.ttf'
    ft = ImageFont.truetype(serif, cap_size(serif, 54)); fs = ImageFont.truetype(serif, cap_size(serif, 30, 'A'))
    size = 166
    while size > 90 and ImageDraw.Draw(c).textlength(spec['big'], font=ImageFont.truetype(bold, size)) > 1110: size -= 2
    fb = ImageFont.truetype(bold, size)
    lines = []
    tw = width(d, spec['top'], ft, 2); lines.append((ft, spec['top'], 2, 640 - tw / 2, 193 - ft.getbbox('E')[1]))
    bw = d.textlength(spec['big'], font=fb); btop = 296 - fb.getbbox('E')[1]; lines.append((fb, spec['big'], 0, 640 - bw / 2, btop))
    base = 296 + (fb.getbbox('E')[3] - fb.getbbox('E')[1])
    if spec.get('small'):
        sw = width(d, spec['small'], fs, 3); lines.append((fs, spec['small'], 3, 640 - sw / 2, base + 84 - fs.getbbox('A')[1]))
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    for f, t, tr, x, y in lines: tracked(ds, x + 3, y + 5, t, f, tr, 190)
    c.paste(Image.new('RGB', (W, H), (14, 9, 6)), (0, 0), sh.filter(ImageFilter.GaussianBlur(7)))
    d = ImageDraw.Draw(c)
    for f, t, tr, x, y in lines: tracked(d, x, y, t, f, tr, (255, 255, 255))
    lg = Image.open(LOGO).convert('RGBA'); lg.thumbnail((104, 104), Image.LANCZOS); c.paste(lg, (101 - lg.width // 2, 75 - lg.height // 2), lg)
    c.save(spec['out'], quality=95); return c

if __name__ == '__main__':
    for path in sys.argv[1:]:
        for sp in json.load(open(path)): build(sp); print('ok', sp['out'])
