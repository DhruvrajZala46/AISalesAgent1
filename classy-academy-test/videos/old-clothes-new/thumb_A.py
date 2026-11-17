import sys, types
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools'); sys.modules.setdefault('crop', types.SimpleNamespace(crop=None))
from thumb_make import sized, finish, FD
from PIL import Image, ImageDraw, ImageFilter
W, H = 1280, 720
c = Image.new('RGB', (W, H)); c.paste(finish(Image.open('kA.png')), (0, 0)); c.paste(finish(Image.open('kB.png')), (640, 0))
# soft dark fade at the bottom, where the words sit
g = Image.new('L', (W, H), 0); dg = ImageDraw.Draw(g)
for y in range(380, H): dg.line((0, y, W, y), fill=int(175 * min(1, (y - 380) / 230) ** 1.2))
c.paste(Image.new('RGB', (W, H), (16, 10, 7)), (0, 0), g.filter(ImageFilter.GaussianBlur(12)))
d = ImageDraw.Draw(c); d.rectangle((639, 0, 641, H), fill=(236, 228, 220))
# circles on what changed: the flower shoulder (2019) -> the cape sleeve (2023)
def ring(cx, cy, rx, ry):
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse((cx - rx, cy - ry, cx + rx, cy + ry), outline=200, width=9)
    c.paste(Image.new('RGB', (W, H), (10, 6, 4)), (0, 0), sh.filter(ImageFilter.GaussianBlur(5)))
    ImageDraw.Draw(c).ellipse((cx - rx, cy - ry, cx + rx, cy + ry), outline=(200, 30, 36), width=7)
ring(392, 278, 92, 84); ring(1098, 340, 84, 122)
ft = sized(FD + 'CormorantSC-Regular.ttf', 44, probe='E'); fb = sized(FD + 'Montserrat.ttf', 104, 700, 'N'); fy = sized(FD + 'CormorantSC-Regular.ttf', 34, probe='2')
def ty(f, t, ytop): return ytop - f.getbbox(t)[1]
lines = [(ft, 'Same Gown,', W / 2, ty(ft, 'Same Gown,', 468), 'ma'), (fb, 'Restyled', W / 2, ty(fb, 'Restyled', 530), 'ma'),
         (ft, '*not replaced*', W / 2, ty(ft, '*not replaced*', 664), 'ma'),
         (fy, '2019', 40, ty(fy, '2019', 660), 'la'), (fy, '2023', W - 40, ty(fy, '2023', 660), 'ra')]
sh = Image.new('L', (W, H), 0); ds = ImageDraw.Draw(sh)
for f, t, x, y, a in lines: ds.text((x + 3, y + 5), t, font=f, fill=210, anchor=a)
c.paste(Image.new('RGB', (W, H), (12, 8, 6)), (0, 0), sh.filter(ImageFilter.GaussianBlur(7)))
d = ImageDraw.Draw(c)
for f, t, x, y, a in lines: d.text((x, y), t, font=f, fill=(255, 255, 255), anchor=a)
lg = Image.open('/home/user/AISalesAgent1/classy-academy-test/workflow/assets/logo_ce.png').convert('RGBA'); lg.thumbnail((96, 96), Image.LANCZOS); c.paste(lg, (16, 14), lg)
c.save('A.jpg', quality=95); print('A.jpg')
