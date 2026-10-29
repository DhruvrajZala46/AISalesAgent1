# thumb_spec.py spec.json -> the thumbnail, built in the channel's measured 3-panel look (same text block as thumb_make.py),
# with every panel framed by hand, so the outfit the video is about stays in the picture.
# Also writes <out>_src/: each graded panel as a PNG, the logo, and <out>.svg with live text (editable in Figma/Illustrator).
#
# spec = {"out": "T1.jpg", "top": "Stop", "big": "Covering Up", "small": "*style it instead*", "logo": "logo.png",
#         "panels": [{"src": "real/ag24.jpg", "face": [x, y, w, h], "fh": 0.13, "fy": 0.10, "dx": 0, "t": 0}, ...]}
#   src   a photo, or a video with "t" (seconds) for its frame
#   underline  false drops the red line (her thumbnails use it only in the "Never..." series)
#   face  the face box in source pixels (tools/crop.py finds one); fh = face height as a share of the panel height,
#         fy = where the top of the face sits; dx shifts the crop sideways (share of the crop width). Optional "box":
#         [x0, y0, x1, y1] in source pixels overrides all of that.
import json, os, sys, subprocess, io, base64
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thumb_make import sized, finish, FD, W, H, XS

def load(p):
    if p.get('t') is not None:
        b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', str(p['t']), '-i', p['src'], '-frames:v', '1',
                            '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        return Image.open(io.BytesIO(b)).convert('RGB')
    return Image.open(p['src']).convert('RGB')

def panel(p, pw):
    im = load(p); iw, ih = im.size
    if 'box' in p: x0, y0, x1, y1 = p['box']
    else:
        fx, fyy, fw, fhh = p['face']; hs = min(ih, fhh / p.get('fh', 0.13)); ws = hs * pw / H
        if ws > iw: ws = iw; hs = ws * H / pw
        y0 = min(max(0, fyy - p.get('fy', 0.10) * hs), ih - hs)
        cx = fx + fw / 2 + p.get('dx', 0) * ws; x0 = min(max(0, cx - ws / 2), iw - ws)
        x1, y1 = x0 + ws, y0 + hs
    c = im.crop((round(x0), round(y0), round(x1), round(y1))).resize((pw, H), Image.LANCZOS)
    c = finish(c)
    if p.get('warm'): c = Image.blend(c, Image.new('RGB', c.size, (205, 160, 120)), p['warm'])
    if p.get('bright'): c = ImageEnhance.Brightness(c).enhance(p['bright'])
    return c

def build(spec):
    out = spec['out']; base = os.path.splitext(out)[0]; sd = base + '_src'; os.makedirs(sd, exist_ok=True)
    c = Image.new('RGB', (W, H)); slots = []
    for i, (p, x0, x1) in enumerate(zip(spec['panels'], XS, XS[1:])):
        pc = panel(p, x1 - x0); c.paste(pc, (x0, 0)); pc.save(f'{sd}/panel{i + 1}.png'); slots.append((x0, x1 - x0))
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((150, 150, W - 150, 600), fill=spec.get('dark', 95))
    c.paste(Image.new('RGB', (W, H), (18, 12, 8)), (0, 0), g.filter(ImageFilter.GaussianBlur(90)))
    d = ImageDraw.Draw(c)
    for x in (XS[1], XS[2]): d.rectangle((x - 1, 0, x, H), fill=(236, 228, 220))
    capb = spec.get('cap', 108)
    ft = sized(FD + 'CormorantSC-Regular.ttf', 46, probe='E'); fb = sized(FD + 'Montserrat.ttf', capb, 700, 'N'); fs = sized(FD + 'CormorantSC-Regular.ttf', 26, probe='A')
    def top_y(f, txt, ytop): return ytop - f.getbbox(txt)[1]
    yb = 296 + (108 - capb) // 2
    lines = [(ft, spec['top'], top_y(ft, spec['top'], 200 + (108 - capb) // 2)), (fb, spec['big'], top_y(fb, spec['big'], yb))]
    if spec.get('small'): lines.append((fs, spec['small'], top_y(fs, spec['small'], 495 - (108 - capb) // 2)))
    sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
    for f, t, y in lines: ds.text((W / 2 + 3, y + 5), t, font=f, fill=200, anchor='ma')
    c.paste(Image.new('RGB', (W, H), (12, 8, 6)), (0, 0), sh.filter(ImageFilter.GaussianBlur(7)))
    d = ImageDraw.Draw(c)
    for f, t, y in lines: d.text((W / 2, y), t, font=f, fill=(255, 255, 255), anchor='ma')
    big = spec['big']; first = big.split()[0]; bb = d.textbbox((W / 2, lines[1][2]), big, font=fb, anchor='ma'); fw_ = d.textlength(first, font=fb)
    fb_ = d.textbbox((bb[0], lines[1][2]), first, font=fb, anchor='la'); uy = max(yb + capb + 14, fb_[3] + 8)
    if spec.get('underline', True): d.rectangle((bb[0] + 14, uy, bb[0] + fw_ + 4, uy + 3), fill=(150, 22, 26))   # her "Never..." series only
    lg = Image.open(spec['logo']).convert('RGBA'); ls = spec.get('logo_size', 112); lg = lg.resize((ls, ls), Image.LANCZOS)
    c.paste(lg, tuple(spec.get('logo_xy', (34, 20))), lg); lg.save(f'{sd}/logo.png')
    c.save(out, quality=95); c.save(base + '.png')
    # editable copy: the graded panels + darkening as images, every word as live text
    def emb(path): return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()
    gl = Image.new('RGBA', (W, H), (18, 12, 8, 0)); gl.putalpha(g.filter(ImageFilter.GaussianBlur(90))); gl.save(f'{sd}/darkening.png')
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
           '<defs><filter id="s" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="7"/></filter></defs>']
    for i, (x0, pw) in enumerate(slots): svg.append(f'<image x="{x0}" y="0" width="{pw}" height="{H}" xlink:href="{emb(f"{sd}/panel{i + 1}.png")}"/>')
    svg.append(f'<image x="0" y="0" width="{W}" height="{H}" xlink:href="{emb(f"{sd}/darkening.png")}"/>')
    for x in (XS[1], XS[2]): svg.append(f'<rect x="{x - 1}" y="0" width="2" height="{H}" fill="#ece4dc"/>')
    fam = {id(ft): ('Cormorant SC', 400), id(fb): ('Montserrat', 700), id(fs): ('Cormorant SC', 400)}
    for f, t, y in lines:
        name, wt = fam[id(f)]; asc = f.getmetrics()[0]
        for dx, dy, fill, extra in ((3, 5, '#0c0806', ' opacity="0.78" filter="url(#s)"'), (0, 0, '#ffffff', '')):
            svg.append(f'<text x="{W / 2 + dx}" y="{y + asc + dy}" text-anchor="middle" font-family="{name}" font-weight="{wt}" font-size="{f.size}" fill="{fill}"{extra}>{t.replace("&", "&amp;")}</text>')
    if spec.get('underline', True): svg.append(f'<rect x="{bb[0] + 14}" y="{uy}" width="{fw_ - 10}" height="4" fill="#96161a"/>')
    svg.append(f'<image x="{spec.get("logo_xy", (34, 20))[0]}" y="{spec.get("logo_xy", (34, 20))[1]}" width="{ls}" height="{ls}" xlink:href="{emb(f"{sd}/logo.png")}"/></svg>')
    open(base + '.svg', 'w').write('\n'.join(svg)); json.dump(spec, open(f'{sd}/spec.json', 'w'), indent=1)
    return c

if __name__ == '__main__':
    for f in sys.argv[1:]: build(json.load(open(f))); print('ok', f)
