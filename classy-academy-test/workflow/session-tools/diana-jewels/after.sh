#!/bin/bash
# after the render: QA, tile sheets of the finished file, the send copy under 400 MiB
cd "$(dirname "$0")"; T=/home/user/AISalesAgent1/classy-academy-test/workflow/tools; F=out/diana_jewels_v1.mp4
python3 $T/qa.py $F > qa.log 2>&1; python3 $T/flash.py > flash.log 2>&1
python3 - <<'PY'
import subprocess, io, os
from PIL import Image, ImageDraw
from concurrent.futures import ThreadPoolExecutor
F = 'out/diana_jewels_v1.mp4'; os.makedirs('qa', exist_ok=True)
d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', F], capture_output=True, text=True).stdout)
ts = [2.0 + 6.0 * k for k in range(int((d - 2) // 6) + 1)]
def fr(t):
    b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', F, '-frames:v', '1', '-vf', 'scale=384:216', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-'], capture_output=True).stdout
    return t, Image.open(io.BytesIO(b)).convert('RGB')
with ThreadPoolExecutor(4) as ex: fs = list(ex.map(fr, ts))
for n in range(0, len(fs), 25):
    sh = Image.new('RGB', (5 * 384, 5 * 232), 'white'); dr = ImageDraw.Draw(sh)
    for k, (t, im) in enumerate(fs[n:n + 25]):
        x, y = (k % 5) * 384, (k // 5) * 232; sh.paste(im, (x, y + 16)); dr.text((x + 4, y + 2), f'{int(t//60)}:{int(t%60):02d}', fill='black')
    sh.save(f'qa/final_{n // 25:02d}.jpg', quality=85)
print(len(fs), 'frames', round(d, 1), 's')
PY
mkdir -p ../deliver
ffmpeg -nostdin -v error -y -i $F -c:v libx264 -preset medium -crf 18 -maxrate 4200k -bufsize 8400k -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart ../deliver/diana_jewels_who_wears_them_v1.mp4
ls -la ../deliver/diana_jewels_who_wears_them_v1.mp4 >> qa.log; echo AFTERDONE >> qa.log
