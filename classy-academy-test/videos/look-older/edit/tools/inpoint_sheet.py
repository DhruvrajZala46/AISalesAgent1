# inpoint_sheet.py OUT.jpg ID [ID ...] : for each pick, 3 frames from the part the video will actually play
# (in-point, middle and end of the needed window at the pick's speed), 2 picks per row, with id / creator / brief
import sys, os, json, subprocess, io
from PIL import Image, ImageDraw, ImageFont
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = {b['id']: b for b in json.load(open(f'{L}/plan/briefs.json'))}
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
out = sys.argv[1]; ids = sys.argv[2:]; H = 260; cells = []
for k in ids:
    pk = json.load(open(f'{L}/picks/{k}.json'))
    if pk.get('gap'): cells.append((f'{k} GAP', [])); continue
    f = f"{L}/{pk['file']}"; ims = []
    if f.endswith(('.jpg', '.png')):
        im = Image.open(f).convert('RGB'); im.thumbnail((H * 2, H)); ims = [im]
    else:
        need = B.get(k, {}).get('need_s', 6); i0 = pk.get('in', 0); sp = pk.get('speed', 1.0)
        for x in (0.05, 0.5, 0.95):
            t = min(i0 + need * sp * x, max(0, (pk.get('dur') or 99) - 0.1))
            b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f, '-frames:v', '1', '-vf', f'scale=-2:{H}',
                                '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
            if b: ims.append(Image.open(io.BytesIO(b)).convert('RGB'))
    lab = f"{k} | {(pk.get('creator_user') or pk.get('creator') or '')[:20]} | in {pk.get('in', 0)} x{pk.get('speed', 1)} | {B.get(k, {}).get('slot', '')}: {B.get(k, {}).get('brief', '')[:70]}"
    cells.append((lab, ims))
CW = 3 * 200 + 20; cols = 2
sh = Image.new('RGB', (cols * CW, ((len(cells) + cols - 1) // cols) * (H + 40)), 'white'); d = ImageDraw.Draw(sh)
for n, (lab, ims) in enumerate(cells):
    x0, y0 = (n % cols) * CW, (n // cols) * (H + 40); d.text((x0 + 3, y0 + 2), lab[:95], fill='red', font=F); x = x0
    for im in ims:
        if CW - (x - x0) < 40: break
        if im.width > CW - (x - x0): im = im.resize((max(1, CW - (x - x0)), int(im.height * (CW - (x - x0)) / im.width)))
        sh.paste(im, (x, y0 + 20)); x += im.width + 4
sh.save(out, quality=80); print(out)
