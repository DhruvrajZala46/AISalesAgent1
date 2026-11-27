# scenes.py - layers, scenes and the frame loop
import numpy as np, subprocess, sys, json, cv2
from engine import *

class Layer:
    tail = 0.45  # keep drawing a little past t1 so scene dissolves have something to show
    def live(self, t): return self.t0 <= t < self.t1 + self.tail

class Clip(Layer):
    """A footage layer. box=None -> full frame. appear: none | top (reveal from top, the panel move) | fade | grow"""
    def __init__(self, key, tin, t0, t1, box=None, mode='cover', crop=None, appear='none', adur=0.35, speed=1.0, focus=(0.5, 0.5)):
        self.key, self.tin, self.t0, self.t1 = key, tin, t0, t1; self.focus = focus
        self.box = box or (0, 0, W, H); self.mode, self.crop = mode, crop
        self.appear, self.adur = appear, adur; self.r = None; self.speed = speed
    def draw(self, f, t):
        x, y, w, h = self.box
        if self.r is None:
            self.r = Reader(self.key, self.tin, w, h, self.mode, self.crop, dur=(self.t1 - self.t0) * self.speed + 1.5, focus=self.focus)
        img = self.r.get(int((t - self.t0) * FPS * self.speed)).astype(np.float32)
        p = 1.0 if self.appear == 'none' else ease((t - self.t0) / self.adur)
        if self.appear == 'top':
            hv = max(1, int(h * (0.55 + 0.45 * p)))  # grows down from its top edge while fading in
            sub = cv2.resize(img, (max(1, int(w * (0.55 + 0.45 * p))), hv)) if p < 1 else img
            sh, sw = sub.shape[:2]
            _paste(f, sub, x, y, p)
        elif self.appear == 'grow':
            s = 0.92 + 0.08 * p
            if p < 1:
                sub = cv2.resize(img, (int(w * s), int(h * s)))
                _paste(f, sub, x + (w - sub.shape[1]) // 2, y + (h - sub.shape[0]) // 2, p)
            else: _paste(f, img, x, y, 1.0)
        else:
            _paste(f, img, x, y, p if self.appear == 'fade' else 1.0)
    def close(self):
        if self.r: self.r.close(); self.r = None

def _paste(f, img, x, y, a):
    h, w = img.shape[:2]
    fx0, fy0, fx1, fy1 = max(0, x), max(0, y), min(W, x + w), min(H, y + h)
    if fx1 <= fx0 or fy1 <= fy0: return
    src = img[fy0 - y:fy1 - y, fx0 - x:fx1 - x]
    if a >= 1: f[fy0:fy1, fx0:fx1] = src
    else: f[fy0:fy1, fx0:fx1] = f[fy0:fy1, fx0:fx1] * (1 - a) + src * a

class Text(Layer):
    """One line of text. wipe: left-to-right soft reveal over wdur (the channel's text move); fade-out at t1."""
    def __init__(self, txt, kind, size, col, cx, top, t0, t1, wdur=0.8, fout=0.4, max_w=None, tracking=0,
                 shadow=False, anchor='center', fade_in=False):
        self.spr = text_sprite(txt, kind, size, col, max_w, tracking, shadow)
        self.cx, self.top, self.t0, self.t1, self.wdur, self.fout = cx, top, t0, t1, wdur, fout
        self.anchor, self.fade_in = anchor, fade_in; self.tail = 0.0
    def size(self):
        s = self.spr[0] if isinstance(self.spr, tuple) else self.spr; return s.shape[1], s.shape[0]
    def draw(self, f, t):
        p = (t - self.t0) / self.wdur if self.wdur > 0 else 1
        op = 1.0
        if self.fout and t > self.t1 - self.fout: op = max(0.0, (self.t1 - t) / self.fout)
        if self.fade_in: op *= ease(p); p = 1.0
        blend_sprite(f, self.spr, self.cx, self.top, p=min(1, max(0, p)), opacity=op, anchor=self.anchor)

class Dim(Layer):
    def __init__(self, amount, t0, t1): self.a, self.t0, self.t1 = amount, t0, t1
    def draw(self, f, t): f *= (1 - self.a)

class Rect(Layer):
    """flat colour block (swatches / white side of a split)"""
    def __init__(self, col, box, t0, t1, appear='none', adur=0.35):
        self.col, self.box, self.t0, self.t1, self.appear, self.adur = col, box, t0, t1, appear, adur
    def draw(self, f, t):
        x, y, w, h = self.box; p = 1.0 if self.appear == 'none' else ease((t - self.t0) / self.adur)
        blk = np.empty((h, w, 3), np.float32); blk[:] = self.col
        if isinstance(self.col, np.ndarray) and self.col.ndim == 3: blk = self.col
        _paste(f, blk, x, y, p)

class Logo(Layer):
    def __init__(self, t0, t1, kind='white', size=118, pos=(44, 34), opacity=0.82, fade=0.0):
        self.t0, self.t1, self.kind, self.size, self.pos, self.op, self.fade = t0, t1, kind, size, pos, opacity, fade
    def draw(self, f, t):
        spr = logo(self.kind, self.size); op = self.op
        if self.fade: op *= ease((t - self.t0) / self.fade)
        blend_sprite(f, spr, self.pos[0], self.pos[1], opacity=op, anchor='left')

class Scene:
    def __init__(self, t0, t1, bg, layers, logo=True, trans='cut', tdur=0.3, out_white=0.0, name=''):
        self.t0, self.t1, self.bg, self.layers = t0, t1, bg, layers
        self.logo, self.trans, self.tdur, self.out_white, self.name = logo, trans, tdur, out_white, name
    def render(self, t):
        if self.bg == 'caramel': f = caramel_bg(t)
        elif self.bg == 'white': f = flat_bg(WHITE, grain=False)
        elif self.bg == 'cream': f = flat_bg(CREAM)
        elif self.bg == 'taupe': f = flat_bg(TAUPE)
        elif self.bg == 'choc': f = flat_bg(CHOC)
        else: f = np.zeros((H, W, 3), np.float32)
        for L in self.layers:
            if L.live(t): L.draw(f, t)
        if self.logo: blend_sprite(f, logo('white' if self.logo is True else self.logo, 118), 44, 34,
                                   opacity=0.82 if self.logo is True else 0.9, anchor='left')
        return f
    def close(self):
        for L in self.layers:
            if hasattr(L, 'close'): L.close()

def render(scenes, n0, n1, out, preview_every=None):
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17',
                            '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    closed = set()
    for n in range(n0, n1):
        t = n / FPS
        i = max(k for k, s in enumerate(scenes) if s.t0 <= t + 1e-6) if t >= scenes[0].t0 else 0
        s = scenes[i]
        f = s.render(t)
        if s.trans == 'dissolve' and i > 0 and t < s.t0 + s.tdur:
            a = ease((t - s.t0) / s.tdur); g = scenes[i - 1].render(t); f = g * (1 - a) + f * a
        if s.out_white and t > s.t1 - s.out_white:
            a = ease((t - (s.t1 - s.out_white)) / s.out_white); f = f * (1 - a) + 255 * a
        enc.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
        for k in range(0, i - 1):
            if k not in closed: scenes[k].close(); closed.add(k)
        if n % 300 == 0: print(f'{out}: frame {n}/{n1}', flush=True)
    enc.stdin.close(); enc.wait()
    for s in scenes: s.close()
