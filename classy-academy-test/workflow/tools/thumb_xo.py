# thumb_xo.py - the "same woman, wrong vs right" thumbnail: the format of the biggest winners on rules topics
# (Audrey Coyne "Dressing Rules EVERYONE Should Learn" 8.0M / 71x, 1.2M, 0.84M; Mademoiselle Spends 1.8M),
# drawn in the channel's own look: caramel backdrop, Montserrat + Cormorant SC, red underline, CE logo.
#   left: the mistake, red cross | centre: 2-3 words | right: the same woman done right, green tick
# usage (inside the thumbnail folder):
#   U2NET_HOME=<models dir> python3 thumb_xo.py OUT.jpg left.png right.png "TOP" "BIG" "small line" [caption_y]
#   left/right = full frames (720x1280) of the same clip; caption_y = y of a burned-in caption to erase (or -1)
# needs: pip install rembg (model isnet-general-use.onnx in U2NET_HOME)
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
T_ = os.path.dirname(os.path.abspath(__file__)); FD = T_ + '/../assets/fonts/'; LOGO = T_ + '/../assets/logo_ce.png'
W, H = 1280, 720

def erase_caption(im, cy):
    """A burned-in caption line across the legs: find its rows near cy over the dark trousers only, then rebuild those
    rows in the trouser columns from the pixels just above and below (folds are vertical, so they run on through)."""
    if cy < 0: return im
    a = np.array(im).astype(np.float32); g = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY).astype(int)
    cols = (g[cy - 45] < 85) & (g[cy + 45] < 85)                                  # trouser columns
    cols = cv2.dilate(cols.astype(np.uint8)[None, :], np.ones((1, 7), np.uint8))[0].astype(bool) & (g[cy - 45] < 120) & (g[cy + 45] < 120)
    rows = [y for y in range(cy - 40, cy + 40) if ((g[y] > 140) & cols).sum() > 3]
    if not rows: return im
    y0, y1 = min(rows) - 5, max(rows) + 5
    top = a[y0 - 3:y0].mean(0); bot = a[y1 + 1:y1 + 4].mean(0)
    for y in range(y0, y1 + 1):
        t = (y - y0) / max(1, y1 - y0); a[y, cols] = (top * (1 - t) + bot * t)[cols]
    a[y0:y1 + 1, cols] += np.random.default_rng(1).normal(0, 2.0, a[y0:y1 + 1, cols].shape)   # keep a little grain
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

def cutout(im):
    from rembg import remove, new_session
    out = remove(im, session=new_session('isnet-general-use'))
    al = np.array(out)[:, :, 3]
    _, b = cv2.threshold(al, 128, 255, cv2.THRESH_BINARY)
    n, lab, st, _ = cv2.connectedComponentsWithStats(b)                 # keep the woman only (largest piece)
    keep = (lab == 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    keep = cv2.morphologyEx(keep, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    al = (al * keep).astype(np.float32); al[al < 60] = 0                  # no faint box of the old background
    al = cv2.erode(al, np.ones((3, 3), np.uint8)); al = cv2.GaussianBlur(al, (3, 3), 0)
    rgba = np.array(out); rgba[:, :, 3] = np.clip(al, 0, 255).astype(np.uint8)
    return Image.fromarray(rgba)

def backdrop():
    yy, xx = np.mgrid[0:H, 0:W]; r = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H * 0.45) / (H * 0.85)) ** 2)
    c0, c1 = np.array([216, 164, 120]), np.array([168, 113, 76])            # the video's caramel, lighter in the centre
    t = np.clip(r, 0, 1)[..., None]; return Image.fromarray((c0 * (1 - t) + c1 * t).astype(np.uint8))

def badge(kind, d=118):
    s = 4; D = d * s; im = Image.new('RGBA', (D, D), (0, 0, 0, 0)); g = ImageDraw.Draw(im)
    g.ellipse((0, 0, D - 1, D - 1), fill=(214, 38, 45) if kind == 'no' else (46, 150, 70))
    w = int(D * 0.11)
    if kind == 'no':
        q = D * 0.30; g.line((q, q, D - q, D - q), fill='white', width=w); g.line((q, D - q, D - q, q), fill='white', width=w)
    else:
        g.line((D * 0.26, D * 0.52, D * 0.43, D * 0.69), fill='white', width=w); g.line((D * 0.43, D * 0.69, D * 0.75, D * 0.32), fill='white', width=w)
        for p in ((D * 0.26, D * 0.52), (D * 0.43, D * 0.69), (D * 0.75, D * 0.32)):
            g.ellipse((p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2), fill='white')
    return im.resize((d, d), Image.LANCZOS)

def font(path, size, wght=None):
    f = ImageFont.truetype(path, size)
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f
def fit(path, txt, cap, maxw, wght=None, probe='H'):
    for s in range(10, 500):
        f = font(path, s, wght); b = f.getbbox(probe)
        if b[3] - b[1] >= cap or f.getlength(txt) > maxw: return f

def build(out, left, right, top, big, small, cy=-1, show=0.80, head_y=26):
    c = backdrop().convert('RGBA')
    for k, (path, cx) in enumerate(((left, 205), (right, W - 205))):
        im = cutout(erase_caption(Image.open(path).convert('RGB'), cy))
        bb = im.getbbox(); im = im.crop(bb); s = (H - head_y) / (show * im.height)   # head at the top, cut below the knee
        im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        sh = Image.new('RGBA', im.size, (40, 20, 8, 0)); sh.putalpha(im.getchannel('A').point(lambda v: v * 0.35))
        c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)), (round(cx - im.width / 2) + 10, head_y + 12))
        c.alpha_composite(im, (round(cx - im.width / 2), head_y))
        b = badge('no' if k == 0 else 'yes'); bx = round(cx + (im.width * 0.30 if k == 0 else -im.width * 0.30 - b.width))
        c.alpha_composite(b, (bx, head_y + 30))
    # text block, centred between the two women
    # "THIN|BOLD": two lines like the 8.0M winner (a light word over a huge bold word); otherwise one bold line
    ft = fit(FD + 'CormorantSC-Regular.ttf', top, 50, 600, probe='E') if top else None
    if '|' in big:
        l1, big = big.split('|'); ft, top = fit(FD + 'Montserrat.ttf', l1, 80, 620, 300, 'N'), l1
        fb = fit(FD + 'Montserrat.ttf', big, 168, 620, 800, 'N')
    else:
        fb = fit(FD + 'Montserrat.ttf', big, 132, 600, 800, 'N')
    fs = fit(FD + 'CormorantSC-Regular.ttf', small, 32, 600, probe='A') if small else None
    lines = ([(ft, top, 0)] if top else []) + [(fb, big, 1)] + ([(fs, small, 2)] if small else [])
    hs = [f.getbbox(t)[3] - f.getbbox(t)[1] for f, t, _ in lines]; gap = [26, 34]
    total = sum(hs) + (len(lines) - 1) * 30; y = (H - total) / 2 - 6; pos = []
    for (f, t, k), h in zip(lines, hs): pos.append((f, t, k, y - f.getbbox(t)[1])); y += h + (30 if k == 0 else 44)
    shl = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(shl)
    for f, t, k, yy in pos: ds.text((W / 2 + 3, yy + 5), t, font=f, fill=210, anchor='ma')
    c.alpha_composite(Image.new('RGBA', (W, H), (60, 30, 12, 255)), (0, 0)) if False else None
    dark = Image.new('RGBA', (W, H), (52, 26, 10, 0)); dark.putalpha(shl.filter(ImageFilter.GaussianBlur(8)))
    c.alpha_composite(dark)
    d = ImageDraw.Draw(c)
    for f, t, k, yy in pos: d.text((W / 2, yy), t, font=f, fill=(255, 255, 255), anchor='ma')
    f, t, k, yy = [p for p in pos if p[2] == 1][0]; bb = d.textbbox((W / 2, yy), t, font=f, anchor='ma')
    first = t.split()[0]; fw = d.textlength(first, font=f)
    d.rectangle((bb[0] + 6, bb[3] + 14, bb[0] + fw - 2, bb[3] + 19), fill=(150, 22, 26))         # the channel's red underline
    lg = Image.open(LOGO).convert('RGBA'); lg.thumbnail((92, 92), Image.LANCZOS)
    c.alpha_composite(lg, (W // 2 - lg.width // 2, 18))
    c.convert('RGB').save(out, quality=95); return out

if __name__ == '__main__':
    a = sys.argv[1:]
    build(a[0], a[1], a[2], a[3], a[4], a[5], int(a[6]) if len(a) > 6 else -1); print('ok', a[0])
