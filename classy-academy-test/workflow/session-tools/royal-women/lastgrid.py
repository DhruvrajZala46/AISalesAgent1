# lastgrid.py: (1) chk/last.jpg = the last frame of every used window; (2) chk/grid_<key>.jpg = 3 frames with a grid in 720x1280 units
import sys, subprocess, io, json
from PIL import Image, ImageDraw
exec(open('clips.py').read())
def fr(k, t, w=240):
    b = subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',f'{max(t,0):.2f}','-i',f'raw/{k}.mp4','-frames:v','1','-f','image2pipe','-vcodec','mjpeg','-'],capture_output=True).stdout
    im = Image.open(io.BytesIO(b)).convert('RGB'); return im
if sys.argv[1:] == ['last']:
    items = list(C.items()); W = 200
    sh = Image.new('RGB', (8 * W, ((len(items) + 7) // 8) * 380), 'white'); d = ImageDraw.Draw(sh)
    for n, (s, (k, a, b)) in enumerate(items):
        im = fr(k, b - 0.12); im.thumbnail((W, 350)); x, y = (n % 8) * W, (n // 8) * 380
        sh.paste(im, (x, y + 16)); d.text((x + 2, y + 2), f'{s} {k} {b:g}', fill='red')
    sh.save('chk/last.jpg', quality=85)
else:
    for k in sys.argv[1:]:
        ws = [v for v in C.values() if v[0] == k] or [(k, 0.3, json.load(open('dur.json'))[k][0] - 0.3)]; a, b = ws[0][1], ws[0][2]
        ims = []
        for t in (a + 0.2, (a + b) / 2, b - 0.15):
            im = fr(k, t).resize((360, 640)); d = ImageDraw.Draw(im)
            for g in range(0, 1281, 128):
                yy = g / 2; d.line([(0, yy), (360, yy)], fill='red'); d.text((2, yy + 1), str(g), fill='yellow')
            for g in range(0, 721, 144):
                xx = g / 2; d.line([(xx, 0), (xx, 640)], fill='cyan')
            ims.append(im)
        sh = Image.new('RGB', (1080, 660), 'white'); [sh.paste(im, (i * 360, 20)) for i, im in enumerate(ims)]
        ImageDraw.Draw(sh).text((4, 4), f'{k} {a}-{b}', fill='black'); sh.save(f'chk/grid_{k}.jpg', quality=85)
