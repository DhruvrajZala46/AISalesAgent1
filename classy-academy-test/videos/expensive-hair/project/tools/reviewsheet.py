# reviewsheet.py - one row per clip: 7 frames (with their times) so the in-point and the clip itself can be judged by eye
#   python3 -I reviewsheet.py out.jpg raw/A01_0.mp4 raw/A01_1.mp4 ...
import sys, subprocess
from PIL import Image, ImageDraw, ImageFont
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
out, files = sys.argv[1], sys.argv[2:]
TW, TH, N = 112, 199, 7
sh = Image.new('RGB', (2 * (N * TW + 8), ((len(files) + 1) // 2) * (TH + 22)), 'white'); dr = ImageDraw.Draw(sh)
for r, f in enumerate(files):
    x0, y0 = (r % 2) * (N * TW + 8), (r // 2) * (TH + 22)
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout or 0)
    dr.text((x0 + 2, y0 + 2), f"{f.split('/')[-1]}  {d:.1f}s", fill='red', font=F)
    for k in range(N):
        tt = d * (0.03 + 0.94 * k / (N - 1))
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{tt:.2f}', '-i', f, '-frames:v', '1', '-vf',
                              f'scale={TW}:{TH}:force_original_aspect_ratio=decrease,pad={TW}:{TH}:(ow-iw)/2:(oh-ih)/2', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        if len(raw) == TW * TH * 3: sh.paste(Image.frombytes('RGB', (TW, TH), raw), (x0 + k * TW, y0 + 20))
        dr.text((x0 + k * TW + 2, y0 + 22), f'{tt:.1f}', fill='yellow', font=F)
sh.save(out, quality=80); print(out, sh.size)
