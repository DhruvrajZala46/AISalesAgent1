# render.py - renders project/timeline.json into the finished video, in Classy Academy's own formats
# (re-checked on the storyboards of all 30 uploads, 19 Oct 2026; geometry and motion from the channel's measured build).
#
#   python3 -I project/render.py frames 12.0 95.5 ...    -> qc/frame_<t>.png
#   python3 -I project/render.py video [--scale 0.5] [--jobs 4] [--parts 1,3]   -> out/video_only.mp4 (project/mix.py adds the sound)
#   (--parts re-renders only those quarters of the video, e.g. after a fix, and joins them with the others again)
#
# Formats (each one seen in the channel's own videos):
#   FULL    full-screen clip (vertical clips are cropped to fill, as the channel does), short dissolves between shots
#   CENTRE  one vertical clip, 608 px wide and full height, centred on the drifting caramel background, grows from the centre
#           (scale 0.4 -> 1, 1.2 s); the creator credit "@handle on TikTok" sits bottom right (Hairstyles video)
#   ROW     2-4 full-height panels side by side across the frame, built left to right on each spoken item; every panel grows
#           from its top-left corner (scale 0.58 -> 1, opacity 0 -> 1, 0.8 s)
#   PAIR    two 608-px panels with a 14-px gap, centred, the second grows from its top-right corner
#   QUOTE   the line to remember on caramel: white serif, one word in script, soft left-to-right wipe (1.5 s)
#   CARD    white number card, black script, soft wipe; 0.4 s fade to white before it
#   WHITE   white card with black script ("In today's video", the payoff line)
#   END     white end card with the CA logo, then black with the white CA logo
#   + the title (white script over the title shot) and the guide mention (text over the footage), as in the hair videos.
import json, os, sys, math, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

P = os.path.dirname(os.path.abspath(__file__)); WD = os.path.dirname(P)
TL = json.load(open(os.path.join(P, 'timeline.json')))
SCALE = float(sys.argv[sys.argv.index('--scale') + 1]) if '--scale' in sys.argv else 1.0
W, H = int(1920 * SCALE), int(1080 * SCALE); FPS = TL['fps']
SEG = TL['segments']; DUR = TL['duration']
PW = int(608 * SCALE); GAPX = int(14 * SCALE)
GUT3 = int(48 * SCALE)                                  # 3-panel row: 3 x 608 px panels with 48 px caramel gutters (MNEo 1:26)
PAIR_W, PAIR_H, PAIR_Y = int(853 * SCALE), int(846 * SCALE), int(117 * SCALE)   # 2-panel row: two framed near-squares (MNEo 2:49)
PAIR_X = (int(57 * SCALE), int(1010 * SCALE))
SPLIT_W = int(810 * SCALE)                              # split: clip on the left 42 %, quote on the caramel right (MNEo 1:12)
FONT_SCRIPT = os.path.join(WD, 'fonts', 'PinyonScript-Regular.ttf')
FONT_SERIF = os.path.join(WD, 'fonts', 'PlayfairDisplay.ttf')
CARAMEL = [(203, 149, 96), (228, 182, 136), (172, 110, 66), (200, 130, 70), (212, 168, 142), (219, 166, 88)]   # base / peach / deep / orange / rose beige / amber, sampled from the channel's caramel frames (MNEo 2:28, Hairstyles 1:04)
CARAMEL_Q = [[160, 165, 172, 176, 179, 182, 185, 188, 190, 192, 194, 195, 197, 199, 202, 204, 207, 211, 216, 222, 228],   # 5 %-steps of R, G, B
             [105, 110, 115, 121, 125, 127, 130, 132, 135, 138, 141, 143, 144, 146, 149, 151, 155, 159, 164, 171, 178],   # over the channel's
             [62, 66, 70, 75, 78, 82, 85, 87, 90, 92, 95, 97, 99, 102, 104, 106, 109, 114, 119, 125, 132]]          # caramel frames
CREAM = (239, 237, 233)                                                           # the channel's cream teaching/quote screens (MNEo 1:32)


def ease(x):
    x = min(max(x, 0.0), 1.0); return x * x * (3 - 2 * x)


def ease_out(x):
    x = min(max(x, 0.0), 1.0); return 1 - (1 - x) ** 3


# ---------------------------------------------------------------- caramel backdrop (soft, blurred, slowly drifting)
_BG = None
def backdrop(t):
    global _BG
    if _BG is None:
        rng = np.random.default_rng(7); bw, bh = int(W * 1.35), int(H * 1.35); s = 4
        sw, shh = bw // s, bh // s
        img = np.zeros((shh, sw, 3), np.float32); img[:] = np.array(CARAMEL[0], np.float32) / 255
        yy, xx = np.mgrid[0:shh, 0:sw]
        for k in range(16):
            c = np.array(CARAMEL[[2, 1, 3, 2, 4, 5, 1, 3][k % 8]], np.float32) / 255
            cx, cy, r = rng.uniform(0, sw), rng.uniform(0, shh), rng.uniform(0.18, 0.36) * shh
            m = np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * r * r)))[..., None]
            img = img * (1 - 0.9 * m) + c * 0.9 * m
        img = cv2.GaussianBlur(img, (0, 0), 12)
        for c in range(3):                     # give it the exact colour spread of the channel's own caramel frames
            mine = np.percentile(img[..., c], np.linspace(0, 100, 21))
            img[..., c] = np.interp(img[..., c], mine, np.array(CARAMEL_Q[c], np.float32) / 255)
        _BG = cv2.resize(img, (bw, bh), interpolation=cv2.INTER_CUBIC)
    bh, bw = _BG.shape[:2]
    ox = (bw - W) / 2 + (bw - W) / 2 * 0.8 * math.sin(2 * math.pi * t / 47.0)
    oy = (bh - H) / 2 + (bh - H) / 2 * 0.8 * math.sin(2 * math.pi * t / 61.0 + 1.0)
    return cv2.warpAffine(_BG, np.float32([[1, 0, -ox], [0, 1, -oy]]), (W, H), flags=cv2.INTER_LINEAR)


# ---------------------------------------------------------------- media (stills and video clips)
_MEDIA = {}
class Clip:
    def __init__(self, path):
        self.cap = cv2.VideoCapture(path); self.fps = self.cap.get(cv2.CAP_PROP_FPS) or 30
        self.n = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)); self.pos = -1; self.last = None
    def frame(self, i):
        i = max(0, min(i, self.n - 1))
        if i == self.pos: return self.last
        if i != self.pos + 1 or self.last is None:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ok, f = self.cap.read()
        if not ok:
            return self.last if self.last is not None else np.zeros((16, 9, 3), np.float32)
        self.pos = i; self.last = cv2.cvtColor(f, cv2.COLOR_BGR2RGB).astype(np.float32) / 255
        return self.last


def media_frame(m, tvid):
    path = os.path.join(WD, m['file'])
    if path not in _MEDIA:
        if path.lower().endswith(('.mp4', '.mov', '.webm', '.m4v')): _MEDIA[path] = Clip(path)
        else:
            im = Image.open(path).convert('RGB')
            if max(im.size) > 2600: im.thumbnail((2600, 2600), Image.LANCZOS)
            _MEDIA[path] = np.asarray(im).astype(np.float32) / 255
    src = _MEDIA[path]
    if isinstance(src, Clip):
        sp = m.get('speed', 1.0)
        return src.frame(int(round((m.get('in', 0.0) + tvid * sp) * src.fps)))
    return src


def picture(m, bw, bh, u, tvid):
    """the media cropped to fill a bw x bh box ('cover'), around its focus point, with the clip's own gentle push-in"""
    src = media_frame(m, tvid); ih, iw = src.shape[:2]
    fx, fy = m.get('focus', [0.5, 0.45])
    still = not m['file'].lower().endswith(('.mp4', '.mov', '.webm', '.m4v'))
    z = (1.0 + 0.06 * ease(u)) if still else 1.0
    z *= m.get('zoom', 1.0)
    s = max(bw / iw, bh / ih) * z
    cx, cy = fx * iw, fy * ih; hw, hh = bw / (2 * s), bh / (2 * s)
    cx = min(max(cx, hw), iw - hw); cy = min(max(cy, hh), ih - hh)
    if s < 0.8:
        k = s / 0.95; src = cv2.resize(src, (max(1, int(iw * k)), max(1, int(ih * k))), interpolation=cv2.INTER_AREA)
        cx, cy, s = cx * k, cy * k, s / k
    M = np.float32([[s, 0, bw / 2 - s * cx], [0, s, bh / 2 - s * cy]])
    return cv2.warpAffine(src, M, (bw, bh), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


# ---------------------------------------------------------------- text
_TEXT = {}
def text_image(key, lines, color, max_w):
    """lines: list of lines of (word, style, size); style 'serif' | 'script' (script word in a serif line) | 'scriptbig'"""
    if key in _TEXT: return _TEXT[key]
    sz = lines[0][0][2]
    while True:
        F = {'serif': ImageFont.truetype(FONT_SERIF, int(sz * SCALE)), 'script': ImageFont.truetype(FONT_SCRIPT, int(sz * 1.45 * SCALE)),
             'scriptbig': ImageFont.truetype(FONT_SCRIPT, int(sz * SCALE))}
        space = F['serif'].getlength(' ')
        gap = lambda ln, j: 0 if j == 0 or ln[j][0][:1] in '.,;:!?\u2019' else space   # no space before punctuation
        widths = [sum(F[s].getlength(w) + gap(ln, j) for j, (w, s, *_) in enumerate(ln)) for ln in lines]
        if max(widths) <= max_w * SCALE or sz < 16: break
        sz *= 0.94
    asc = max(F[s].getmetrics()[0] for ln in lines for w, s, *_ in ln); desc = max(F[s].getmetrics()[1] for ln in lines for w, s, *_ in ln)
    lh = int((asc + desc) * 1.02)
    img = Image.new('RGBA', (int(max(widths)) + 40, lh * len(lines) + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    for li, ln in enumerate(lines):
        x = 20 + (max(widths) - widths[li]) / 2; y = 20 + li * lh
        for j, (w, s, *_) in enumerate(ln):
            x += gap(ln, j); f = F[s]; a_, _d = f.getmetrics(); d.text((x, y + asc - a_), w, font=f, fill=tuple(color) + (255,)); x += f.getlength(w)
    a = np.asarray(img).astype(np.float32) / 255; _TEXT[key] = a; return a


def rich_lines(s, size, max_w):
    words = []; style = 'serif'; buf = ''
    for ch in s.replace('<i>', '\x01').replace('</i>', '\x02'):
        if ch in '\x01\x02':
            words += [(w, style, size) for w in buf.split()]; buf = ''; style = 'script' if ch == '\x01' else 'serif'
        else: buf += ch
    words += [(w, style, size) for w in buf.split()]
    F = ImageFont.truetype(FONT_SERIF, int(size * SCALE)); lines, cur, cw = [], [], 0
    for w in words:
        lw = F.getlength(w[0] + ' ') * (1.3 if w[1] == 'script' else 1)
        if cur and cw + lw > max_w * SCALE and w[0][:1] not in '.,;:!?': lines.append(cur); cur, cw = [], 0
        cur.append(w); cw += lw
    return lines + ([cur] if cur else [])


def put(frame, rgba, cx, cy, alpha=1.0, wipe=None):
    h, w = rgba.shape[:2]; x0, y0 = int(cx - w / 2), int(cy - h / 2)
    a = rgba[..., 3:4] * alpha
    if wipe is not None and wipe < 1:
        feather = 0.18 * w; edge = -feather + wipe * (w + feather)
        a = a * np.clip((edge - np.arange(w, dtype=np.float32)) / feather, 0, 1)[None, :, None]
    X0, Y0, X1, Y1 = max(x0, 0), max(y0, 0), min(x0 + w, W), min(y0 + h, H)
    if X1 <= X0 or Y1 <= Y0: return
    aa = a[Y0 - y0:Y1 - y0, X0 - x0:X1 - x0]; cc = rgba[Y0 - y0:Y1 - y0, X0 - x0:X1 - x0, :3]
    frame[Y0:Y1, X0:X1] = frame[Y0:Y1, X0:X1] * (1 - aa) + cc * aa


_LOGO = {}
def logo(kind, width):
    """the CA monogram with its spaced 'Classy Academy' line (width = the whole mark, as measured on the channel's frames)"""
    k = (kind, width)
    if k not in _LOGO:
        im = Image.open(os.path.join(WD, 'assets', f'logo_ca_{kind}.png')).convert('RGBA'); im = im.crop(im.getbbox())
        lw = int(width * SCALE); im = im.resize((lw, int(im.height * lw / im.width)), Image.LANCZOS)
        _LOGO[k] = np.asarray(im).astype(np.float32) / 255
    return _LOGO[k]


def credit(fr, txt, t, t0, t1):
    if not txt: return
    a = ease((t - t0 - 0.6) / 0.5) * (1 - ease((t - (t1 - 0.4)) / 0.4))
    img = text_image(('cr', txt), [[(w, 'scriptbig', 40) for w in txt.split()]], (255, 255, 255), 700)
    put(fr, img, W - int(130 * SCALE) - img.shape[1] / 2 + 20, H - int(60 * SCALE), alpha=a)


# ---------------------------------------------------------------- one segment at time t (no transitions)
def shot_at(shots, t, xf):
    """picture of a sequence of shots at t, with an xf-second dissolve into each next shot -> (shot, blend list)"""
    out = []
    for i, sh in enumerate(shots):
        if sh['t0'] - xf <= t < sh['t1'] or (i == len(shots) - 1 and t >= sh['t0'] - xf):
            out.append((sh, 1.0 if i == 0 or t >= sh['t0'] else ease((t - sh['t0'] + xf) / xf)))
    return out or [(shots[0], 1.0)]


def quote_lines(text, size, max_w, color):
    """the quote as separate line images (each line is revealed on its own, as the channel does)"""
    out = []
    for li, ln in enumerate(rich_lines(text, size, max_w)):
        out.append(text_image(('ql', text, size, li, color), [ln], color, max_w + 400))
    return out


def draw_quote(fr, sg, t, cx, cy, max_w, color):
    size = sg.get('size', 58); lines = quote_lines(sg['text'], size, max_w, color)
    lh = size * 1.32 * SCALE; y0 = cy - lh * (len(lines) - 1) / 2
    step = sg.get('line_step', min(1.1, max(0.5, (sg['t1'] - sg['t0'] - 1.5) / max(len(lines), 1))))
    out_a = 1 - ease((t - (sg['t1'] - 0.35)) / 0.35) if sg.get('fade_out', True) else 1.0
    for li, im in enumerate(lines):
        w = (t - sg['t0'] - 0.25 - li * step) / 0.9
        if w > 0: put(fr, im, cx, y0 + li * lh, alpha=out_a, wipe=min(w, 1))


def render_segment(sg, t):
    k = sg['kind']; t0, t1 = sg['t0'], sg['t1']
    if k == 'END':                                      # white end card, tan CA / Classy Academy (measured: 438 px wide)
        fr = np.ones((H, W, 3), np.float32); put(fr, logo('tan', 454), W / 2, H / 2, alpha=ease((t - t0 - 0.1) / 0.6))
        return fr, False
    if k in ('CARD', 'WHITE'):                          # black script written on left to right in ~1 s, fades before the cut
        fr = np.ones((H, W, 3), np.float32)
        size = sg.get('size', 122 if k == 'CARD' else 128)
        img = text_image(('card', sg['text'], size), [[(w, 'scriptbig', size) for w in sg['text'].split()]], (17, 17, 17), 1500)
        wipe = (t - t0 - sg.get('text_delay', 0.15)) / sg.get('wipe', 1.0)
        out_a = 1 - ease((t - (t1 - 0.35)) / 0.35)
        put(fr, img, W / 2, H / 2, alpha=out_a, wipe=min(max(wipe, 0), 1))
        return fr, False
    if k == 'FULL':
        fr = None
        for sh, a in shot_at(sg['shots'], t, sg.get('xf', 0.5)):
            pic = picture(sh, W, H, (t - sh['t0']) / max(sh['t1'] - sh['t0'], 0.1), max(0.0, t - sh['t0'] + 0.5))
            fr = pic if fr is None else fr * (1 - a) + pic * a
        for tx in sg.get('texts', []): draw_text_overlay(fr, tx, t)
        return fr, True
    if k == 'QUOTE' and sg.get('bg') == 'cream':        # cream quote card: black serif, key words in black script
        fr = np.ones((H, W, 3), np.float32) * (np.array(CREAM, np.float32) / 255)
        draw_quote(fr, sg, t, W / 2, H / 2, 1300, (20, 20, 20)); return fr, True
    fr = backdrop(t)
    if k == 'QUOTE':                                    # quote on the caramel: white serif, key words in script, line by line
        draw_quote(fr, sg, t, W / 2, H / 2, 1300, (255, 255, 255)); return fr, True
    if k == 'SPLIT':                                    # clip on the left 42 % (810 px), quote on the caramel right
        for sh, a in shot_at(sg['shots'], t, 0.5):
            pic = picture(sh, SPLIT_W, H, (t - sh['t0']) / max(sh['t1'] - sh['t0'], 0.1), max(0.0, t - sh['t0'] + 0.5))
            fr[:, :SPLIT_W] = fr[:, :SPLIT_W] * (1 - a) + pic * a
        draw_quote(fr, sg, t, SPLIT_W + (W - SPLIT_W) / 2, H / 2, 1000, (255, 255, 255)); return fr, True
    if k == 'CENTRE':                                   # one vertical clip, 608 px, full height, centred on the caramel
        g = ease_out((t - t0) / 1.0) if sg.get('grow') else 1.0
        panel = None
        for sh, a in shot_at(sg['shots'], t, sg.get('xf', 0.5)):
            pic = picture(sh, PW, H, (t - sh['t0']) / max(sh['t1'] - sh['t0'], 0.1), max(0.0, t - sh['t0'] + 0.5))
            panel = pic if panel is None else panel * (1 - a) + pic * a
        sc = 0.55 + 0.45 * g; pw, ph = max(2, int(PW * sc)), max(2, int(H * sc))
        pp = panel if sc >= 0.999 else cv2.resize(panel, (pw, ph), interpolation=cv2.INTER_AREA)
        x0, y0 = (W - pw) // 2, (H - ph) // 2
        fr[y0:y0 + ph, x0:x0 + pw] = fr[y0:y0 + ph, x0:x0 + pw] * (1 - g) + pp * g
        cur = [sh for sh, a in shot_at(sg['shots'], t, 0.5)][-1]
        credit(fr, cur.get('credit'), t, max(cur['t0'], t0), min(cur['t1'], cur['t0'] + cur.get('credit_len', 8.0)))
        for tx in sg.get('texts', []): draw_text_overlay(fr, tx, t)
        return fr, True
    if k in ('ROW', 'PAIR'):                            # panels fade in one by one in their slots (measured geometry)
        n = len(sg['panels'])
        if k == 'PAIR' or n == 2: boxes = [(PAIR_X[0], PAIR_Y, PAIR_W, PAIR_H), (PAIR_X[1], PAIR_Y, PAIR_W, PAIR_H)]
        elif n == 3: boxes = [(i * (PW + GUT3), 0, PW, H) for i in range(3)]
        else: boxes = [(round(i * W / n), 0, round((i + 1) * W / n) - round(i * W / n), H) for i in range(n)]
        for i, pn in enumerate(sg['panels']):
            te = pn['enter']
            if t < te: continue
            g = ease((t - te) / 0.4); x0, y0, bw, bh = boxes[i]
            pic = picture(pn, bw, bh, (t - te) / max(t1 - te, 0.1), t - te)
            fr[y0:y0 + bh, x0:x0 + bw] = fr[y0:y0 + bh, x0:x0 + bw] * (1 - g) + pic * g
        return fr, True
    raise ValueError(k)


def draw_text_overlay(fr, tx, t):
    if not (tx['t0'] <= t < tx['t1']): return
    a = 1 - ease((t - (tx['t1'] - 0.5)) / 0.5)
    w = min(max((t - tx['t0'] - 0.2) / 1.2, 0), 1)
    if tx['style'] == 'title':                          # "Episode N" small serif over the script title, white, on a darkened clip
        fr *= (1 - 0.25 * ease((t - tx['t0']) / 0.6) * a)
        put(fr, text_image(('ep', tx['episode']), [[(x, 'serif', 44) for x in tx['episode'].split()]], (255, 255, 255), 1400),
            W / 2, H / 2 - 105 * SCALE, alpha=a * ease((t - tx['t0']) / 0.6))
        img = text_image(('title', tx['text']), [[(x, 'scriptbig', 150) for x in tx['text'].split()]], (255, 255, 255), 1650)
        put(fr, img, W / 2, H / 2 + 20 * SCALE, alpha=a, wipe=w)
    elif tx['style'] == 'guide':
        fr *= (1 - 0.38 * ease((t - tx['t0']) / 0.6) * a)
        put(fr, text_image(('g1', tx['line1']), [[(x, 'serif', 44) for x in tx['line1'].split()]], (255, 255, 255), 1400), W / 2, H / 2 - 115 * SCALE, alpha=a, wipe=w)
        put(fr, text_image(('g2', tx['text']), [[(x, 'scriptbig', 120) for x in tx['text'].split()]], (255, 255, 255), 1500), W / 2, H / 2 + 5 * SCALE, alpha=a, wipe=w)
        put(fr, text_image(('g3', tx['line3']), [[(tx['line3'], 'serif', 38)]], (255, 255, 255), 1400), W / 2, H / 2 + 120 * SCALE, alpha=a, wipe=w)


# ---------------------------------------------------------------- full frame at t (transitions + logo)
def frame_at(t):
    i = max(j for j, sg in enumerate(SEG) if sg['t0'] <= t + 1e-6) if t >= SEG[0]['t0'] else 0
    sg = SEG[i]
    fr, logo_on = render_segment(sg, t)
    tr = sg.get('trans', 'dissolve'); td = sg.get('trans_dur', 0.4); la = 1.0 if logo_on else 0.0
    if tr == 'black' and t < sg['t0'] + td:
        a = ease((t - sg['t0']) / td); fr = fr * a; la *= a
    elif tr in ('dissolve', 'fromwhite') and i > 0 and t < sg['t0'] + td:
        if tr == 'fromwhite': prev, plogo = np.ones_like(fr), False
        else: prev, plogo = render_segment(SEG[i - 1], t)
        a = ease((t - sg['t0']) / td); fr = prev * (1 - a) + fr * a; la = (1 - a) * (1.0 if plogo else 0.0) + a * la
    if i + 1 < len(SEG) and SEG[i + 1].get('trans') == 'white' and t > SEG[i + 1]['t0'] - 0.4:
        a = ease((t - (SEG[i + 1]['t0'] - 0.4)) / 0.4); fr = fr * (1 - a) + a; la *= (1 - a)
    if la > 0.001:
        lg = logo('white', 166); put(fr, lg, int(47 * SCALE) + lg.shape[1] / 2, int(51 * SCALE) + lg.shape[0] / 2, alpha=0.92 * la)
    return (np.clip(fr, 0, 1) * 255 + 0.5).astype(np.uint8)


def render_range(args):
    a, b, outp = args
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                           '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p',
                           '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', outp], stdin=subprocess.PIPE)
    for n in range(a, b): ff.stdin.write(frame_at(n / FPS).tobytes())
    ff.stdin.close(); ff.wait(); return outp


if __name__ == '__main__':
    cmd = sys.argv[1]
    os.makedirs(os.path.join(WD, 'qc'), exist_ok=True); os.makedirs(os.path.join(WD, 'out'), exist_ok=True)
    if cmd == 'frames':
        for s in sys.argv[2:]:
            try: tt = float(s)
            except ValueError: continue
            Image.fromarray(frame_at(tt)).save(os.path.join(WD, 'qc', f'frame_{tt:07.2f}.png'))
    elif cmd == 'video':
        jobs = int(sys.argv[sys.argv.index('--jobs') + 1]) if '--jobs' in sys.argv else 4
        N = int(round(DUR * FPS)); step = (N + jobs - 1) // jobs
        parts = [(k, min(k + step, N), os.path.join(WD, 'out', f'part{k // step:02d}.mp4')) for k in range(0, N, step)]
        only = [int(x) for x in sys.argv[sys.argv.index('--parts') + 1].split(',')] if '--parts' in sys.argv else None   # re-render only these
        todo = [pt for i, pt in enumerate(parts) if only is None or i in only]
        from multiprocessing import Pool
        with Pool(min(jobs, len(todo))) as pool: pool.map(render_range, todo)
        done = [pt[2] for pt in parts]
        lst = os.path.join(WD, 'out', 'parts.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in done))
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy',
                        os.path.join(WD, 'out', 'video_only.mp4')], check=True)
        print('video', N, 'frames')
