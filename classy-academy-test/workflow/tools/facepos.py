# facepos.py - where the faces are in each full-screen / wide shot, so the 16:9 window cut from a vertical clip keeps them.
# usage (work folder): python3 facepos.py -> facepos.json {"key a b": face_y (0..1 of clip height) or null}
import re, json, subprocess, os
import numpy as np, cv2
t = open('edit.py').read()
want = set()
for m in re.finditer(r"(full|wide)\(\[(.*?)\]\s*,", t, re.S):
    for k, a, b in re.findall(r"C\('([a-z0-9_]+)',\s*([\d.]+),\s*([\d.]+)\)", m.group(2)): want.add((k, float(a), float(b)))
fc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
pc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
out = json.load(open('facepos.json')) if os.path.exists('facepos.json') else {}
for k, a, b in sorted(want):
    key = f'{k} {a:g} {b:g}'
    if key in out: continue
    ys = []
    for f in np.linspace(0.1, 0.9, 7):
        tt = a + (b - a) * f
        buf = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-ss', f'{tt:.2f}', '-i', f'raw/{k}.mp4', '-frames:v', '1', '-vf', 'scale=360:-2',
                              '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True).stdout
        im = cv2.imdecode(np.frombuffer(buf, np.uint8), cv2.IMREAD_GRAYSCALE) if buf else None
        if im is None: continue
        h = im.shape[0]; best = None
        for c in (fc, pc):
            for (x, y, w, hh) in c.detectMultiScale(im, 1.1, 5, minSize=(18, 18)):
                if best is None or w * hh > best[2] * best[3]: best = (x, y, w, hh)
        if best is not None: ys.append((best[1] + best[3] / 2) / h)
    out[key] = round(float(np.median(ys)), 3) if len(ys) >= 2 else None
    print(key, out[key], len(ys), flush=True)
json.dump(out, open('facepos.json', 'w'), indent=0)
