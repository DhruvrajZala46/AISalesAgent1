# look.py OUT.jpg ID [ID ...] : 4 frames per downloaded asset (0.1/0.37/0.63/0.9 of the clip) with id, size, fps, length,
# for the by-eye check (right subject, no big text, no AI tells such as waxy skin or objects that change between frames)
import sys, os, json, subprocess, io
from PIL import Image, ImageDraw
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); out = sys.argv[1]; ids = sys.argv[2:]; H = 300; rows = []
for k in ids:
    pk = json.load(open(f'{L}/picks/{k}.json')); f = f"{L}/{pk['file']}"
    if f.endswith('.jpg'):
        im = Image.open(f).convert('RGB'); im.thumbnail((H * 2, H)); ims = [im]
    else:
        d = pk['dur'] or 1; ims = []
        for x in (0.1, 0.37, 0.63, 0.9):
            b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{d * x:.2f}', '-i', f, '-frames:v', '1', '-vf', f'scale=-2:{H}',
                                '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
            if b: ims.append(Image.open(io.BytesIO(b)).convert('RGB'))
    rows.append((f"{k} {pk['w']}x{pk['h']} {pk['fps']}fps {pk['dur']}s {pk['creator_user'][:24]}", ims))
wmax = max(sum(i.width for i in ims) for _, ims in rows) if rows else 100
sh = Image.new('RGB', (wmax, len(rows) * (H + 18)), 'white'); dr = ImageDraw.Draw(sh)
for n, (lab, ims) in enumerate(rows):
    y = n * (H + 18); dr.text((3, y + 3), lab, fill='red'); x = 0
    for im in ims: sh.paste(im, (x, y + 16)); x += im.width
sh.save(out, quality=82); print(out)
