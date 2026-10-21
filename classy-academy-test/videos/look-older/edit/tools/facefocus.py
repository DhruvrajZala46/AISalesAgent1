# facefocus.py : for every FULL shot cut from a vertical clip (a 16:9 band keeps only ~32 % of its height), finds the face in the
# frames the video actually plays and, for close-ups (face taller than 12 % of the frame), moves the crop so the whole face sits
# in the band (eyes in its upper half). Writes focus_auto into picks/<ID>.json and prints what changed, to check on the sheets.
import json, os, sys, cv2, numpy as np
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tl = json.load(open(f'{L}/project/timeline.json'))
casc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
done = set()
for sg in tl['segments']:
    if sg['kind'] != 'FULL': continue
    for m in sg['shots']:
        a = m['asset']
        if a in done or not m['file'].endswith('.mp4') or m.get('pan') or not os.path.exists(f'{L}/picks/{a}.json'): continue
        done.add(a); cap = cv2.VideoCapture(f"{L}/{m['file']}"); w = cap.get(3); h = cap.get(4)
        if h <= w: continue
        band = (1080 / 1920) * w / h                    # band height as a share of the clip height
        ys, xs, hs = [], [], []
        for u in (0.1, 0.5, 0.9):
            t = m.get('in', 0) + (m['t1'] - m['t0'] + 0.5) * u * m.get('speed', 1.0)
            cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000); ok, fr = cap.read()
            if not ok: continue
            g = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY); f = casc.detectMultiScale(g, 1.1, 6, minSize=(int(w * 0.12), int(w * 0.12)))
            if len(f):
                x, y, fw, fh = max(f, key=lambda r: r[2] * r[3]); ys.append((y + fh * 0.62) / h); xs.append((x + fw / 2) / w); hs.append(fh / h)
        if not ys or np.median(hs) < 0.12: continue
        fy = float(np.clip(np.median(ys), band / 2, 1 - band / 2)); fx = float(np.median(xs))
        p = json.load(open(f'{L}/picks/{a}.json')); old = p.get('focus', [0.5, 0.42])
        p['focus_auto'] = [round(fx, 3), round(fy, 3)]; json.dump(p, open(f'{L}/picks/{a}.json', 'w'), indent=1)
        print(f"{a}: face height {np.median(hs):.2f}; focus {old} -> {p['focus_auto']}")
