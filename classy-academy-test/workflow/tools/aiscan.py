import cv2, numpy as np, json, os, sys
# AI-watermark scan v2: finds the Google Gemini/Veo sparkle (✦) that AI video tools stamp in the bottom-right corner.
# usage (inside the work folder): python3 aiscan.py [clip keys...]   (default: every raw/*.mp4)
#
# v1 matched one median frame and missed AI clips that scored 0.49-0.58 (styling23, cafework0, midiskirt9, Oct 2026).
# v2 looks at 16 frames one by one: the sparkle is PERSISTENT (same spot in most frames) and sits at one of two known
# spots; real footage never is. score = share of frames with a match at a known spot. >= 0.40 = AI: never use it.
# Tested on every clip of the put-together and French videos: AI clips 0.56-1.00, every real clip 0.27 or lower.
# (scarf9, a confirmed AI clip on a pale scarf, scored only 0.56, so the line sits at 0.40, not 0.60.)
F = os.getcwd()
T = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'gemini_star.npy'))
TS = [cv2.resize(T, None, fx=s, fy=s) for s in (0.7, 0.8, 0.9, 1.0, 1.1, 1.25, 1.4)]
KNOWN = [(149, 140), (220, 206)]          # sparkle centres inside the 260x260 bottom-right corner of a 720-wide frame
def hp(a): return a - cv2.GaussianBlur(a, (0, 0), 6)
def corners(path, n=16):
    cap = cv2.VideoCapture(path); N = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); out = []
    for k in range(n):
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(N * (k + 0.5) / n)); ok, im = cap.read()
        if not ok: continue
        h, w = im.shape[:2]; im = cv2.resize(im, (720, round(h * 720 / w)))
        out.append(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32)[-260:, -260:])
    cap.release(); return out
def score(path):
    fr = corners(path)
    if len(fr) < 4: return None
    hits = 0; locs = []
    for g in fr:
        h = hp(g); best, loc = -1, None
        for t in TS:
            r = cv2.matchTemplate(h, t, cv2.TM_CCOEFF_NORMED); _, mx, _, ml = cv2.minMaxLoc(r)
            if mx > best: best, loc = mx, (ml[0] + t.shape[1] / 2, ml[1] + t.shape[0] / 2)
        locs.append(loc)
        if best > 0.45 and min(np.hypot(loc[0] - a, loc[1] - b) for a, b in KNOWN) < 25: hits += 1
    return hits / len(fr)
keys = sys.argv[1:] or sorted(f[:-4] for f in os.listdir(F + '/raw') if f.endswith('.mp4'))
res = {}
for k in keys:
    s = score(f'{F}/raw/{k}.mp4')
    if s is not None: res[k] = round(s, 3)
old = json.load(open('aiscan.json')) if os.path.exists('aiscan.json') and sys.argv[1:] else {}
old.update(res); json.dump(old, open('aiscan.json', 'w'), indent=0)
flag = sorted(k for k, v in res.items() if v >= 0.40)
print('AI WATERMARK - DO NOT USE:', flag if flag else 'none')
for k, v in sorted(res.items(), key=lambda z: -z[1])[:15]: print(f'{k:18} {v:.2f}')
