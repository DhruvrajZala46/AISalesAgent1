# peek.py - 4 frames per clip (10/35/60/85 %) on one sheet: python3 -I peek.py out.jpg raw/A09_p0.mp4 ...
import sys, subprocess, json
from PIL import Image, ImageDraw
out, files = sys.argv[1], sys.argv[2:]
TW, TH = 180, 320; sh = Image.new('RGB', (4 * TW + 230, len(files) * (TH + 4)), 'white'); dr = ImageDraw.Draw(sh)
for r, f in enumerate(files):
    y = r * (TH + 4); dr.text((4, y + 4), f.split('/')[-1], fill='black')
    if f.endswith('.jpg'):
        im = Image.open(f).convert('RGB'); im.thumbnail((4 * TW, TH)); sh.paste(im, (230, y)); continue
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout or 0)
    wh = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout.strip()
    dr.text((4, y + 18), f'{d:.1f}s {wh}', fill='blue')
    for k, p in enumerate((0.1, 0.35, 0.6, 0.85)):
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{d * p:.2f}', '-i', f, '-frames:v', '1', '-vf', f'scale={TW}:{TH}:force_original_aspect_ratio=decrease,pad={TW}:{TH}:(ow-iw)/2:(oh-ih)/2', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        if len(raw) == TW * TH * 3: sh.paste(Image.frombytes('RGB', (TW, TH), raw), (230 + k * TW, y))
sh.save(out, quality=82); print(out, sh.size)
