# big.py out.jpg key[:a:b[:step]] ...  -> large frames (216x384), 8 per row, time-labelled, to verify a clip by eye
import sys, subprocess, io, json
from PIL import Image, ImageDraw
D = json.load(open('dur.json')); out = sys.argv[1]; TW, TH = 216, 384; rows = []
for it in sys.argv[2:]:
    p = it.split(':'); k = p[0]; a = float(p[1]) if len(p) > 1 else 0.3; b = float(p[2]) if len(p) > 2 else D[k][0] - 0.2; st = float(p[3]) if len(p) > 3 else max(0.5, (b - a) / 15.5)
    ts = []; t = a
    while t <= b + 1e-6: ts.append(t); t += st
    fr = []
    for t in ts:
        r = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t:.2f}', '-i', f'raw/{k}.mp4', '-frames:v', '1', '-vf', f'scale={TW}:{TH}:force_original_aspect_ratio=decrease,pad={TW}:{TH}:(ow-iw)/2:(oh-ih)/2', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-'], capture_output=True).stdout
        try: fr.append((t, Image.open(io.BytesIO(r)).convert('RGB')))
        except Exception: pass
    rows.append((it, fr))
H = sum(20 + ((len(f) + 7) // 8) * (TH + 16) for _, f in rows); S = Image.new('RGB', (TW * 8, H), 'white'); d = ImageDraw.Draw(S); y = 0
for it, fr in rows:
    d.text((4, y + 4), f'{it}  ({D[it.split(":")[0]][0]:.1f}s)', fill=(200, 0, 0)); y += 20
    for i, (t, im) in enumerate(fr):
        x = (i % 8) * TW; yy = y + (i // 8) * (TH + 16); S.paste(im, (x, yy + 16)); d.text((x + 4, yy + 2), f'{t:.1f}', fill='black')
    y += ((len(fr) + 7) // 8) * (TH + 16)
S.save(out, quality=82); print(out, S.size)
