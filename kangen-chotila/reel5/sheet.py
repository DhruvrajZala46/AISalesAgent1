import subprocess, sys, os
from PIL import Image, ImageDraw
names = sys.argv[2:]; out = sys.argv[1]; N = 7; W, H = 112, 199
rows = []
for nm in names:
    f = f'raw/{nm}.mp4'
    d = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout or 0)
    wh = subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',f],capture_output=True,text=True).stdout.strip()
    row = Image.new('RGB', (W * N + 150, H), 'black'); dr = ImageDraw.Draw(row)
    dr.text((4, 4), nm, fill='yellow'); dr.text((4, 20), f'{d:.1f}s', fill='white'); dr.text((4, 36), wh, fill='white')
    for k in range(N):
        t = d * (k + 0.5) / N
        subprocess.run(['ffmpeg','-y','-v','error','-ss',f'{t:.2f}','-i',f,'-frames:v','1','-vf',f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}','/tmp/_f.jpg'])
        try: row.paste(Image.open('/tmp/_f.jpg'), (150 + k * W, 0)); dr.text((150 + k * W + 2, 2), f'{t:.1f}', fill='yellow')
        except Exception: pass
    rows.append(row)
sh = Image.new('RGB', (rows[0].width, H * len(rows) + 2 * len(rows)), 'white')
for i, r in enumerate(rows): sh.paste(r, (0, i * (H + 2)))
sh.save(out, quality=82)
