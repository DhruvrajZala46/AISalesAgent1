# ca_thumb.py - Classy Academy thumbnails in the channel's own measured layout (workflow/4-THUMBNAIL.md,
# measured on "8 Things Elegant Ladies Never Wear", 1.2M, and checked on all 31 CA thumbnails, 8 Nov 2026):
#   3 real photos edge to edge (x 0-401 | 403-850 | 852-1280), thin light dividers, slightly warm / darker grade,
#   gentle darkening behind the words, Cormorant SC top line (cap 46, top y 200), Montserrat Bold headline (cap 108,
#   top y 296), red underline under the first headline word, Cormorant SC small line (cap 26, top y 495), soft drop
#   shadow, and the REAL CA logo (assets/logo_ca.png, extracted from the 31 thumbnails by ca_logo.py) at its own place.
# usage: python3 thumb_ca_real.py spec.json [name ...]   -> <name>.jpg (1280x720) + layers/<name>_*.png (editable layers)
import sys, json, os
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools')
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import types; sys.modules.setdefault('crop', types.SimpleNamespace(crop=None))
from thumb_make import sized, FD
W, H = 1280, 720
LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'logo_ca.png')   # the real CA logo (ca_logo.py)
LOGO_XY = (33, 26)   # where it sits on every CA thumbnail (1280x720)
def finish(im, p):   # the channel's grade (thumb_make.finish), per photo adjustable
    im = ImageEnhance.Color(im).enhance(p.get('color', 0.9)); im = ImageEnhance.Contrast(im).enhance(p.get('contrast', 1.04))
    im = ImageEnhance.Brightness(im).enhance(p.get('bright', 0.9)); im = ImageEnhance.Sharpness(im).enhance(1.2)
    return Image.blend(im, Image.new('RGB', im.size, (205, 170, 140)), 0.05)
def panel(p, pw):
    im = Image.open(p['src']).convert('RGB')
    if p.get('flip'): im = im.transpose(Image.FLIP_LEFT_RIGHT)
    SW, SH = im.size
    if 'box' in p: cx, top, cw = p['box']                       # explicit: centre x, top y, crop width (source px)
    else:
        x, y, w, h = p['face']; cw = w / p.get('fw', 0.3); cx = x + w / 2 + p.get('dx', 0) * cw
        top = y + h / 2 - p.get('fy', 0.2) * cw * H / pw
    ch = cw * H / pw
    if ch > SH: ch = SH; cw = ch * pw / H
    if cw > SW: cw = SW; ch = cw * H / pw
    x0 = min(max(cx - cw / 2, 0), SW - cw); y0 = min(max(top, 0), SH - ch)
    c = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((pw, H), Image.LANCZOS)
    if cw < pw: c = c.filter(ImageFilter.UnsharpMask(1.4, 60, 2))
    return finish(c, p), cw / pw
def build(spec, name, outdir='.'):
    xs = spec.get('xs', [0, 402, 851, W]); photos = Image.new('RGB', (W, H)); info = []
    for p, x0, x1 in zip(spec['panels'], xs, xs[1:]):
        im, s = panel(p, x1 - x0); photos.paste(im, (x0, 0)); info.append(round(s, 2))
    d = ImageDraw.Draw(photos)
    for x in xs[1:-1]: d.rectangle((x - 1, 0, x, H), fill=(236, 228, 220))
    # layer: gentle darkening behind the words
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse(tuple(spec.get('ellipse', (150, 150, W - 150, 600))), fill=spec.get('dark', 95))
    dark = Image.new('RGBA', (W, H), (18, 12, 8, 0)); dark.putalpha(g.filter(ImageFilter.GaussianBlur(90)))
    # words
    top, big, small = spec['top'], spec['big'], spec.get('small', '')
    ft = sized(FD + 'CormorantSC-Regular.ttf', spec.get('top_cap', 46), probe='E')
    cap = spec.get('cap', 108); fb = sized(FD + 'Montserrat.ttf', cap, 700, 'N')
    probe = ImageDraw.Draw(Image.new('L', (8, 8)))
    while probe.textlength(big, font=fb) > spec.get('maxw', 1060): cap -= 2; fb = sized(FD + 'Montserrat.ttf', cap, 700, 'N')
    fs = (sized(FD + 'PinyonScript-Regular.ttf', spec.get('small_cap', 44), probe='E') if spec.get('small_script')   # the channel's script line ("& Eloquently")
          else sized(FD + 'CormorantSC-Regular.ttf', spec.get('small_cap', 26), probe='A'))
    def top_y(f, txt, ytop): return ytop - f.getbbox(txt)[1]
    yb = spec.get('yb', 296)
    lines = [(ft, top, top_y(ft, top, yb - 96)), (fb, big, top_y(fb, big, yb))]
    if small: lines.append((fs, small, top_y(fs, small, yb + cap + spec.get('small_gap', 91))))
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    for f, t, y in lines: ds.text((W / 2 + 3, y + 5), t, font=f, fill=200, anchor='ma', features=['lnum'])   # lining figures: '$60', not Cormorant's old-style '$6o'
    shadow = Image.new('RGBA', (W, H), (12, 8, 6, 0)); shadow.putalpha(sh.filter(ImageFilter.GaussianBlur(7)))
    text = Image.new('RGBA', (W, H), (0, 0, 0, 0)); dt = ImageDraw.Draw(text)
    for f, t, y in lines: dt.text((W / 2, y), t, font=f, fill=(255, 255, 255, 255), anchor='ma', features=['lnum'])
    if spec.get('underline', True):
        first = big.split()[0]; bb = dt.textbbox((W / 2, lines[1][2]), big, font=fb, anchor='ma'); fw_ = dt.textlength(first, font=fb)
        fb_ = dt.textbbox((bb[0], lines[1][2]), first, font=fb, anchor='la'); uy = max(yb + cap + 14, fb_[3] + 8)
        dt.rectangle((bb[0] + 14, uy, bb[0] + fw_ + 4, uy + 3), fill=(150, 22, 26, 255))
    logo = Image.new('RGBA', (W, H), (0, 0, 0, 0)); L = Image.open(LOGO).convert('RGBA')
    lx, ly = LOGO_XY; logo.paste(L, (lx, ly), L)
    lsh = Image.new('RGBA', (W, H), (8, 6, 4, 0)); a = Image.new('L', (W, H), 0); a.paste(L.split()[3].point(lambda v: v * 0.45), (lx + 1, ly + 2))
    lsh.putalpha(a.filter(ImageFilter.GaussianBlur(3)))
    out = photos.convert('RGBA')
    if spec.get('logo_dark'):   # optional: a soft dark patch behind the logo when it lands on blonde hair or a white wall
        gl = Image.new('L', (W, H), 0); ImageDraw.Draw(gl).ellipse((lx - 50, ly - 45, lx + L.width + 50, ly + L.height + 45), fill=spec['logo_dark'])
        ld = Image.new('RGBA', (W, H), (18, 12, 8, 0)); ld.putalpha(gl.filter(ImageFilter.GaussianBlur(38))); out = Image.alpha_composite(out, ld)
    for layer in (dark, shadow, text, lsh, logo): out = Image.alpha_composite(out, layer)
    out = out.convert('RGB'); out.save(f'{outdir}/{name}.jpg', quality=95); out.save(f'{outdir}/{name}.png')
    os.makedirs(f'{outdir}/layers', exist_ok=True)
    for k, layer in (('1_photos', photos), ('2_darkening', dark), ('3_text_shadow', shadow), ('4_text', text), ('5_logo_shadow', lsh), ('6_logo', logo)):
        layer.save(f'{outdir}/layers/{name}_{k}.png')
    print(name, 'panel source px per output px', info, 'headline cap', cap)
    return out
if __name__ == '__main__':
    S = json.load(open(sys.argv[1])); names = sys.argv[2:] or list(S)
    for n in names: build(S[n], n)
