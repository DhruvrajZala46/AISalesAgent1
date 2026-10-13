# wordsheet.py - the "does the picture match the words" check: one frame every N seconds of the rendered video,
# with the exact words being spoken at that moment printed under it (from beats.json + words.json).
# usage (inside the work folder, after the render): python3 wordsheet.py out/<video>.mp4 [step=2] -> qa/words_N.jpg (60 frames per sheet)
import sys, os, json, subprocess, io
from PIL import Image, ImageDraw, ImageFont
V = sys.argv[1]; STEP = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
B = json.load(open('beats.json')); W = json.load(open('words.json')); os.makedirs('qa', exist_ok=True)
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', V], capture_output=True, text=True).stdout)
def words_at(t, span=1.6):
    out = []
    for b in B:
        for w, a, e in W.get(str(b['i']), []):
            if t - span / 2 <= b['start'] + a <= t + span / 2: out.append(w)
    return ' '.join(out)
FW, FH, cols, rows = 320, 180, 6, 10
try: font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
except Exception: font = None
ts = [round(x * STEP, 2) for x in range(int(dur / STEP))]
for p in range(0, len(ts), cols * rows):
    sh = Image.new('RGB', (cols * (FW + 4), rows * (FH + 40)), 'white'); d = ImageDraw.Draw(sh)
    for n, t in enumerate(ts[p:p + cols * rows]):
        b = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{t}', '-i', V, '-frames:v', '1', '-vf', f'scale={FW}:{FH}', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        x, y = (n % cols) * (FW + 4), (n // cols) * (FH + 40)
        try: sh.paste(Image.open(io.BytesIO(b)).convert('RGB'), (x, y))
        except Exception: pass
        txt = f'{int(t//60)}:{t%60:04.1f} ' + words_at(t)
        d.text((x + 2, y + FH + 2), txt[:52], fill='black', font=font); d.text((x + 2, y + FH + 19), txt[52:104], fill='black', font=font)
    sh.save(f'qa/words_{p // (cols * rows)}.jpg', quality=80); print(f'qa/words_{p // (cols * rows)}.jpg', flush=True)
