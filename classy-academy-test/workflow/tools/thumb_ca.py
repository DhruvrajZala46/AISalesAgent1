# Three thumbnails in the channel's own layout (measured on all 31 channel thumbnails, Oct 2026):
# 3 photo panels edge to edge + thin light dividers, CA logo top-left, Cormorant SC top line, Montserrat Bold
# headline, red underline under "Never", Cormorant SC small line, soft shadow and gentle darkening behind the text.
import sys, json
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools')
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from thumb_make import sized, finish, FD
import cv2
casc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def face(path):
    g = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY); h = g.shape[0]
    fs = casc.detectMultiScale(g, 1.1, 6, minSize=(h // 16, h // 16))
    return max(fs, key=lambda f: f[2]) if len(fs) else None
W, H = 1280, 720; XS = [0, 427, 853, W]

def panel(p, pw):
    im = Image.open(p['src']).convert('RGB'); SW, SH = im.size
    if 'box' in p: cx, top, cw = p['box']
    else:
        x, y, w, h = p['face'] if 'face' in p else face(p['src']); cw = p['cw'] if 'cw' in p else w / p.get('fw', 0.30); cx = x + w / 2 + p.get('dx', 0) * cw
        top = y + h / 2 - p.get('fy', 0.27) * cw * H / pw
    ch = cw * H / pw
    if ch > SH: ch = SH; cw = ch * pw / H
    if cw > SW: cw = SW; ch = cw * H / pw
    x0 = min(max(cx - cw / 2, 0), SW - cw); y0 = min(max(top, 0), SH - ch)
    c = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((pw, H), Image.LANCZOS)
    if cw < pw: c = c.filter(ImageFilter.UnsharpMask(1.6, 70, 2))
    if p.get('flip'): c = c.transpose(Image.FLIP_LEFT_RIGHT)
    return finish(c), cw / pw

def logo():
    L = Image.new('RGBA', (230, 160), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    pf = ImageFont.truetype(FD + 'PlayfairDisplay.ttf', 92)
    try: pf.set_variation_by_axes([400])
    except Exception: pass
    d.text((18, 4), 'C', font=pf, fill='white'); d.text((50, 24), 'A', font=pf, fill='white')
    sf = ImageFont.truetype(FD + 'Montserrat.ttf', 11)
    try: sf.set_variation_by_axes([400])
    except Exception: pass
    x = 14
    for ch in 'Classy Academy':
        d.text((x, 124), ch, font=sf, fill=(255, 255, 255, 235)); x += d.textlength(ch, font=sf) + 3.2
    return L

def build(spec, out):
    c = Image.new('RGB', (W, H)); info = []
    for p, x0, x1 in zip(spec['panels'], XS, XS[1:]):
        im, s = panel(p, x1 - x0); c.paste(im, (x0, 0)); info.append(round(s, 2))
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((120, 140, W - 120, 560), fill=spec.get('dark', 100))
    c.paste(Image.new('RGB', (W, H), (18, 12, 8)), (0, 0), g.filter(ImageFilter.GaussianBlur(90)))
    d = ImageDraw.Draw(c)
    for x in XS[1:3]: d.rectangle((x - 1, 0, x + 1, H), fill=(236, 228, 220))
    ft = sized(FD + 'CormorantSC-Regular.ttf', 48, probe='E'); fs = sized(FD + 'CormorantSC-Regular.ttf', 30, probe='A')
    cap = 108
    while True:
        fb = sized(FD + 'Montserrat.ttf', cap, 700, 'N')
        if d.textlength(spec['big'], font=fb) <= 960 and cap <= 92: break
        cap -= 2
    def ty(f, t, ytop): return ytop - f.getbbox(t)[1]
    yb = 296; lines = [(ft, spec['top'], ty(ft, spec['top'], 196)), (fb, spec['big'], ty(fb, spec['big'], yb))]
    ysm = yb + cap + 74
    if spec.get('small'): lines.append((fs, spec['small'], ty(fs, spec['small'], ysm)))
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    for f, t, y in lines: ds.text((W / 2 + 3, y + 5), t, font=f, fill=210, anchor='ma')
    c.paste(Image.new('RGB', (W, H), (12, 8, 6)), (0, 0), sh.filter(ImageFilter.GaussianBlur(7)))
    d = ImageDraw.Draw(c)
    for f, t, y in lines: d.text((W / 2, y), t, font=f, fill=(255, 255, 255), anchor='ma')
    if spec.get('underline'):
        big = spec['big']; first = big.split()[0]; bb = d.textbbox((W / 2, lines[1][2]), big, font=fb, anchor='ma')
        fw_ = d.textlength(first, font=fb); fb_ = d.textbbox((bb[0], lines[1][2]), first, font=fb, anchor='la')
        uy = fb_[3] + 10; d.rectangle((bb[0] - 18, uy, bb[0] + fw_ + 6, uy + 3), fill=(150, 22, 26))
    lg = logo(); lg = lg.resize((172, 120), Image.LANCZOS)
    lsh = Image.new('L', (W, H), 0); lsh.paste(lg.split()[3].point(lambda v: v * 0.6), (40, 22))
    c.paste(Image.new('RGB', (W, H), (10, 8, 6)), (0, 0), lsh.filter(ImageFilter.GaussianBlur(4)))
    c.paste(lg, (38, 20), lg)
    c.save(out, quality=95); print(out, 'panel src px per out px', info)

if __name__ == '__main__':
    # usage: python3 thumb_ca.py spec.json   (spec: {"out.jpg": {top, big, small, underline, panels:[{src, cw|fw, fy, dx, face}]}})
    for k, v in json.load(open(sys.argv[1])).items(): build(v, k)
