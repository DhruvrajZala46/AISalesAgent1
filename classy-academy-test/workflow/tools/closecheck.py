# closecheck.py <out.jpg> key[:a-b] ...: 12 larger frames per clip (or per segment), for a close look at captions, faces and the exact garment
import sys, subprocess, io
from PIL import Image, ImageDraw
w, h, N = 150, 267, 12
rows = []
for arg in sys.argv[2:]:
    k, _, r = arg.partition(':')
    d = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'raw/{k}.mp4'],capture_output=True,text=True).stdout)
    a, b = (map(float, r.split('-')) if r else (0, d))
    rows.append((k, [a + (b - a) * (j + 0.5) / N for j in range(N)]))
sh = Image.new('RGB', (N * (w + 2) + 4, len(rows) * (h + 18)), 'white'); dr = ImageDraw.Draw(sh)
for r, (k, ts) in enumerate(rows):
    for j, t in enumerate(ts):
        b = subprocess.run(['ffmpeg','-nostdin','-v','error','-ss',f'{t:.2f}','-i',f'raw/{k}.mp4','-frames:v','1','-vf',f'scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:white','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
        try: sh.paste(Image.open(io.BytesIO(b)).convert('RGB'), (j * (w + 2), r * (h + 18) + 16))
        except Exception: pass
        dr.text((j * (w + 2) + 2, r * (h + 18) + 2), f'{k[:14]} {t:.1f}' if j == 0 else f'{t:.1f}', fill='red')
sh.save(sys.argv[1], quality=85)
