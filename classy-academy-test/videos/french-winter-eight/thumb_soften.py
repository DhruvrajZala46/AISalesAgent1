# soften.py - the street behind each woman softly out of focus (bystanders become shapes), the woman untouched.
# mask: rembg isnet (soft/<k>_mask.png), only the component under her chin; background blur is mask-normalised so she does not bleed into it.
import numpy as np, cv2, json
from PIL import Image, ImageFilter
F = json.load(open('faces.json'))
STR = {'maigret218': 0.45, 'deneuve11': 0.7, 'ines229': 1.0}          # how strongly the background is softened (1 = width / 130 px)
CUT = {'deneuve11': lambda X, Y: (X > 735) & (Y < 640)}                 # a bystander touching her arm in the mask: not her
def gb(a, r): return cv2.GaussianBlur(a, (0, 0), r)
def soften(k):
    im = np.asarray(Image.open(f'orig/{k}.jpg').convert('RGB')).astype(np.float32); H, W = im.shape[:2]
    m = np.asarray(Image.open(f'soft/{k}_mask.png').convert('L')).copy()
    if k in CUT:
        Y, X = np.mgrid[0:H, 0:W]; m[CUT[k](X, Y)] = 0
    n, lab, stats, _ = cv2.connectedComponentsWithStats((m > 100).astype(np.uint8), connectivity=8)
    x, y, w, h = F[k]['faces'][0]; keep = lab[min(H - 1, y + h), min(W - 1, x + w // 2)] or (1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA])))
    mm = np.where(lab == keep, m, 0).astype(np.float32) / 255
    mm = gb(mm, max(1.2, W / 800)); r = max(4, W / 130) * STR.get(k, 1.0)
    grow = gb((mm > 0.05).astype(np.float32), max(2, W / 400)); bgw = np.clip(1 - grow * 1.6, 0, 1)      # background weights: nothing from her or her edge
    bg = gb(im * bgw[..., None], r) / np.maximum(gb(bgw, r), 1e-3)[..., None]
    far = gb(im, r); wgt = np.clip(gb(bgw, r) * 4, 0, 1)[..., None]; bg = bg * wgt + far * (1 - wgt)        # deep inside her silhouette the normalised blur is undefined
    out = im * mm[..., None] + bg * 0.95 * (1 - mm[..., None])
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(f'soft/{k}.jpg', quality=95); print(k, 'blur', round(r, 1))
if __name__ == '__main__':
    import sys
    for k in sys.argv[1:]: soften(k)
