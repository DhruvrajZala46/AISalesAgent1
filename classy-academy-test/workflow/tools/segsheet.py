# every prepared clip segment the edit shows, 3 frames each (start/middle/end), in order of appearance -> segs/sNN.jpg
import re, os, subprocess, io, sys
from PIL import Image, ImageDraw
from concurrent.futures import ThreadPoolExecutor
html = open('index.html').read()
names = []
for m in re.finditer(r'assets/([^"\']+?\.mp4)', html):
    if m.group(1) not in names: names.append(m.group(1))
os.makedirs('segs', exist_ok=True); TW, TH = 112, 200
def frames(n):
    f = 'assets/' + n
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout or 1)
    out = []
    for p in (0.06, 0.5, 0.94):
        b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{d*p:.2f}', '-i', f, '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        im = Image.open(io.BytesIO(b)).convert('RGB') if b else Image.new('RGB', (TW, TH), 'black')
        if im.width > im.height: im = im.crop(((im.width - 608) // 2, 0, (im.width + 608) // 2, im.height))
        im = im.resize((TW, TH)); out.append(im)
    return n, out
with ThreadPoolExecutor(4) as ex: res = list(ex.map(frames, names))
PER = 4; ROWS = 6
for s in range(0, len(res), PER * ROWS):
    chunk = res[s:s + PER * ROWS]
    S = Image.new('RGB', (PER * (3 * TW + 16), ((len(chunk) + PER - 1) // PER) * (TH + 16)), 'white'); d = ImageDraw.Draw(S)
    for j, (n, ims) in enumerate(chunk):
        x, y = (j % PER) * (3 * TW + 16), (j // PER) * (TH + 16)
        for k, im in enumerate(ims): S.paste(im, (x + k * TW, y + 14))
        d.text((x, y + 1), f'{s+j} ' + re.sub(r'^F_', '', n)[:44], fill='red')
    S.save(f'segs/s{s//(PER*ROWS):02d}.jpg', quality=80)
print(len(names), 'segments')
