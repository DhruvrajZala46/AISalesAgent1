# frames of a clip (first second, spread, last seconds) on one sheet, to read watermarks / handles
#   python3 -I wmsheet.py raw/A09_p0.mp4 sheet.jpg
import sys, cv2, numpy as np
src, out = sys.argv[1], sys.argv[2]
cap = cv2.VideoCapture(src); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); fps = cap.get(cv2.CAP_PROP_FPS) or 30
idx = sorted(set([0, int(fps * 0.5), int(fps * 1.5)] + [int(n * k / 7) for k in range(1, 7)] + [max(0, n - int(fps * 2)), max(0, n - int(fps * 0.7)), n - 3]))
tiles = []
for i in idx:
    cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, i)); ok, fr = cap.read()
    if not ok: continue
    h, w = fr.shape[:2]; s = 540 / h; fr = cv2.resize(fr, (int(w * s), 540))
    cv2.putText(fr, f'{i / fps:.1f}s', (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2); tiles.append(fr)
W = max(t.shape[1] for t in tiles); tiles = [cv2.copyMakeBorder(t, 0, 0, 0, W - t.shape[1], cv2.BORDER_CONSTANT) for t in tiles]
rows = [np.hstack(tiles[k:k + 6] + [np.zeros_like(tiles[0])] * (6 - len(tiles[k:k + 6]))) for k in range(0, len(tiles), 6)]
cv2.imwrite(out, np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 85])
