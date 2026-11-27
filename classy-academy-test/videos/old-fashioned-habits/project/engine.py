# engine.py - frame compositor for the Classy-Academy-style edit (PIL + numpy + OpenCV + ffmpeg pipes)
# Layouts follow classy-academy-test/STYLE-DECODE-5-videos.md (palette, fonts, motion timings).
import subprocess, os, json, math, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1920, 1080, 30
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = ROOT + '/fonts'
SRC = ROOT + '/src'

# ---- palette (sampled from the reference videos) ----
def hx(h): h = h.lstrip('#'); return np.array([int(h[i:i+2], 16) for i in (0, 2, 4)], np.float32)
CARAMEL, CARAMEL_LIGHT, CARAMEL_DEEP = hx('C48D5D'), hx('D5A268'), hx('B67D45')
WHITE, CREAM, TAUPE, CHOC, INK, ROSE = hx('FFFFFF'), hx('F7F5F1'), hx('C4AD9F'), hx('332418'), hx('0B0B0B'), hx('C5A789')

def ease(x):  # smooth in-out
    x = min(max(x, 0.0), 1.0); return x * x * (3 - 2 * x)

# ---------------- backgrounds ----------------
_rng = np.random.default_rng(7)
_grain = (_rng.normal(0, 1.6, (H, W, 1))).astype(np.float32)

def caramel_bg(t):
    """Moving blurred-light caramel backdrop: soft blobs drifting slowly (measured: bright patch travels
    about a third of the frame in a few seconds)."""
    w, h = 192, 108
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    img = np.zeros((h, w, 3), np.float32) + CARAMEL
    blobs = [  # (cx0, cy0, ax, ay, speed, phase, radius, colour, strength)
        (0.30, 0.25, 0.22, 0.10, 0.11, 0.0, 0.42, CARAMEL_LIGHT, 0.9),
        (0.75, 0.20, 0.18, 0.12, 0.08, 1.7, 0.35, hx('E2B37C'), 0.7),
        (0.25, 0.85, 0.20, 0.08, 0.09, 3.1, 0.45, CARAMEL_DEEP, 0.8),
        (0.85, 0.80, 0.15, 0.10, 0.07, 4.2, 0.40, hx('A8673E'), 0.6),
        (0.55, 0.55, 0.25, 0.15, 0.06, 2.3, 0.30, hx('C99A76'), 0.5)]
    for cx, cy, ax, ay, sp, ph, r, col, s in blobs:
        x = (cx + ax * math.sin(t * sp * 2 * math.pi / 3 + ph)) * w
        y = (cy + ay * math.cos(t * sp * 2 * math.pi / 3.7 + ph)) * h
        g = np.exp(-(((xx - x) / (r * w)) ** 2 + ((yy - y) / (r * w)) ** 2)) * s
        img = img * (1 - g[..., None]) + col * g[..., None]
    img = cv2.GaussianBlur(img, (0, 0), 6)
    big = cv2.resize(img, (W, H), interpolation=cv2.INTER_CUBIC)
    return np.clip(big + _grain, 0, 255)

def flat_bg(col, grain=True):
    a = np.empty((H, W, 3), np.float32); a[:] = col
    return a + (_grain * 0.5 if grain else 0)

# ---------------- video readers ----------------
class Reader:
    """Sequential frames of a source clip, scaled/cropped by ffmpeg to (w, h).
    mode: cover | fitblur (4:3 centred at full height over a blurred, dimmed copy)
    crop: (x, y, w, h) in source pixels applied first (a static punch-in / reframe)."""
    def __init__(self, key, tin, w, h, mode='cover', crop=None, dur=30, grade=None, focus=(0.5, 0.5)):
        self.w, self.h = w, h; src = f'{SRC}/{key}.mp4'
        pre = f'crop={crop[2]}:{crop[3]}:{crop[0]}:{crop[1]},' if crop else ''
        g = grade or ''
        if mode == 'cover':
            vf = f'{pre}fps={FPS},scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h}:(iw-{w})*{focus[0]}:(ih-{h})*{focus[1]},unsharp=5:5:0.35,setsar=1{g}'
            args = ['-vf', vf]
        else:  # fitblur
            fc = (f'[0:v]{pre}fps={FPS},split[a][b];'
                  f'[a]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},gblur=sigma=40,eq=brightness=-0.10:saturation=0.85[bg];'
                  f'[b]scale=-2:{h}:flags=lanczos,unsharp=5:5:0.45[fg];[bg][fg]overlay=(W-w)/2:0,setsar=1{g}')
            args = ['-filter_complex', fc]
        cmd = ['ffmpeg', '-v', 'error', '-ss', f'{tin:.3f}', '-t', f'{dur:.2f}', '-i', src, *args,
               '-pix_fmt', 'rgb24', '-f', 'rawvideo', '-']
        self.p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=w * h * 3 * 2)
        self.idx = -1; self.last = None
    def get(self, i):
        while self.idx < i:
            b = self.p.stdout.read(self.w * self.h * 3)
            if len(b) < self.w * self.h * 3:
                break  # past the end: hold the last frame
            self.last = np.frombuffer(b, np.uint8).reshape(self.h, self.w, 3); self.idx += 1
        if self.last is None: raise RuntimeError('reader produced no frames')
        return self.last
    def close(self):
        try: self.p.kill()
        except Exception: pass

# ---------------- text sprites ----------------
_fc = {}
def font(name, size):
    k = (name, size)
    if k not in _fc:
        path = {'script': f'{FONTS}/PinyonScript-Regular.ttf', 'serif': f'{FONTS}/Prata-Regular.ttf',
                'caps': f'{FONTS}/Cormorant.ttf'}[name]
        f = ImageFont.truetype(path, size)
        if name == 'caps':
            try: f.set_variation_by_axes([350])
            except Exception: pass
        _fc[k] = f
    return _fc[k]

def text_sprite(txt, kind, size, col, max_w=None, tracking=0, shadow=False):
    """Render one line to an RGBA float sprite (premultiplied by alpha later)."""
    while True:
        f = font(kind, size)
        if tracking:
            widths = [f.getlength(c) for c in txt]; tw = sum(widths) + tracking * (len(txt) - 1)
        else:
            tw = f.getlength(txt)
        if not max_w or tw <= max_w or size < 20: break
        size = int(size * 0.95)
    asc, desc = f.getmetrics(); pad = int(size * 0.5)
    im = Image.new('L', (int(tw) + 2 * pad, asc + desc + 2 * pad), 0); d = ImageDraw.Draw(im)
    if tracking:
        x = pad
        for c, cw in zip(txt, widths): d.text((x, pad), c, font=f, fill=255); x += cw + tracking
    else:
        d.text((pad, pad), txt, font=f, fill=255)
    a = np.asarray(im, np.float32) / 255.0
    bb = np.nonzero(a.max(0) > 0.01)[0]; rb = np.nonzero(a.max(1) > 0.01)[0]
    # keep full ascent box for consistent baselines, trim horizontally
    x0, x1 = max(0, bb[0] - 4), min(a.shape[1], bb[-1] + 5)
    a = a[:, x0:x1]
    rgba = np.zeros(a.shape + (4,), np.float32); rgba[..., :3] = col; rgba[..., 3] = a
    if shadow:
        sh = cv2.GaussianBlur(a, (0, 0), size * 0.12) * 0.28
        rgba = (rgba, sh)
    return rgba

def wipe_alpha(width, p, edge=0.18):
    """left-to-right soft-edged reveal; p 0..1"""
    x = np.linspace(0, 1, width, dtype=np.float32)
    e = edge
    return np.clip((p * (1 + e) - x) / e, 0, 1)

def blend_sprite(frame, spr, cx, top, p=1.0, opacity=1.0, anchor='center'):
    """Draw sprite with its horizontal centre at cx (or left edge at cx if anchor=='left'), top edge at top."""
    sh = None
    if isinstance(spr, tuple): spr, sh = spr
    h, w = spr.shape[:2]
    x0 = int(round(cx - w / 2)) if anchor == 'center' else int(round(cx))
    y0 = int(round(top))
    a = spr[..., 3] * opacity
    if p < 1: a = a * wipe_alpha(w, p)[None, :]
    if sh is not None:
        s = sh * opacity * (wipe_alpha(w, p)[None, :] if p < 1 else 1)
        _comp(frame, np.zeros((h, w, 3), np.float32) + hx('3C2819'), s, x0, y0 + 3)
    _comp(frame, spr[..., :3], a, x0, y0)
    return w, h

def _comp(frame, rgb, a, x0, y0):
    h, w = a.shape
    fx0, fy0 = max(0, x0), max(0, y0); fx1, fy1 = min(W, x0 + w), min(H, y0 + h)
    if fx1 <= fx0 or fy1 <= fy0: return
    sa = a[fy0 - y0:fy1 - y0, fx0 - x0:fx1 - x0][..., None]
    frame[fy0:fy1, fx0:fx1] = frame[fy0:fy1, fx0:fx1] * (1 - sa) + rgb[fy0 - y0:fy1 - y0, fx0 - x0:fx1 - x0] * sa

# ---------------- logo ----------------
_logo = {}
def logo(kind, size):
    k = (kind, size)
    if k not in _logo:
        p = ROOT + ('/assets/logo_ce.png' if kind == 'white' else '/assets/logo_ce_dark.png')
        im = Image.open(p).convert('RGBA').resize((size, size), Image.LANCZOS)
        a = np.asarray(im, np.float32)
        rgba = np.zeros_like(a); rgba[..., 3] = a[..., 3] / 255.0
        rgba[..., :3] = WHITE if kind == 'white' else ROSE
        _logo[k] = rgba
    return _logo[k]
