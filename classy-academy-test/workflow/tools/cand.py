# frames of candidate clip segments: python3 cand.py out.jpg key:a:b ...  (4 frames each across the segment)
import sys, subprocess, io
from PIL import Image, ImageDraw
out = sys.argv[1]; items = sys.argv[2:]; TW, TH = 120, 213
S = Image.new('RGB', (TW * 4 * 2 + 10, (TH + 16) * ((len(items) + 1) // 2)), 'white'); d = ImageDraw.Draw(S)
for n, it in enumerate(items):
    k, a, b = it.split(':'); a, b = float(a), float(b)
    for j in range(4):
        t = a + (b - a) * (0.05 + 0.3 * j)
        p = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f'raw/{k}.mp4', '-frames:v', '1', '-vf', f'scale={TW}:{TH}:force_original_aspect_ratio=decrease,pad={TW}:{TH}:(ow-iw)/2:(oh-ih)/2', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        try: im = Image.open(io.BytesIO(p)).convert('RGB')
        except Exception: continue
        x = (n % 2) * (TW * 4 + 10) + j * TW; y = (n // 2) * (TH + 16)
        S.paste(im, (x, y + 16))
    d.text(((n % 2) * (TW * 4 + 10) + 2, (n // 2) * (TH + 16) + 2), it, fill='red')
S.save(out, quality=82)
