# Princess Diana's 8 Timeless Style Rules (The Classy Elegance) - beat map (17 Nov 2026)
# Layouts: only those read off the channel's own videos (VISUAL-EDITING-DNA.md; videos/unforgettable-charm/VISUAL-ANALYSIS.md):
#   full clips (the whole vertical clip over its own blurred copy) | the rule's name on a white card in script |
#   a clip on the caramel with the lesson in white lines beside it, appearing as they are said | rows of clips |
#   a framed clip on cream with the EXACT WORDS in script beside it | two framed pictures under a small label (a comparison) |
#   one sentence alone on the caramel | the NAMED WOMAN shown in real archive film and real press photographs, framed on the
#   caramel with the place and year in script (the channel shows a named woman in photos and archive film: Audrey, Diana, Grace) |
#   the guide over a full clip | the CE logo.
# Sound: the voice and ONE soft solo-piano bed, steady, no ducking, NO sound effects (none are in the channel's measured files).
TRACKS_EDIT = ['m683n.mp3']; MUSIC_DB = 15; ENDLOGO = 'logo_ce_dark.png'
MUSIC_CREDIT = 'Music: "Classical vibes 3" by Grigoriy Nuzhny (Mixkit, free license)'
def en_(i): return en(i) + 0.5
def qstack(lines, times, t1, box_=QL, size=58, rh=150, cls=''):
    """lines one under the other beside a clip, each appearing as it is said"""
    x0, y0, x1, y1 = box_; n = len(lines); top = (y0 + y1) // 2 - n * rh // 2
    for k, (txt, tt) in enumerate(zip(lines, times)):
        q(txt, tt, t1, (x0, top + k * rh, x1, top + (k + 1) * rh), size=size, dur=1.0, cls=cls)
PX = 250                                              # the framed clip of a phrase screen (540 x 960, rounded) on cream
PB = (860, 60, 1850, 1020)                            # the words beside it
def pframe(shots, t1, x0=PX):
    """the speech video's phrase screen: a rounded framed clip at the left of the cream backdrop"""
    return cframe(shots, t1, x0=x0)
def pwords(lines, times, t1, size=60, rh=170, box_=PB):
    """the exact words in dark script beside the framed clip, each line appearing as it is said"""
    qstack(lines, times, t1, box_, size=size, rh=rh, cls='dark')
GUIDE = '<div><span style="font-size:50px">Check The Description For</span><br><i style="font-size:120px">Personal Stylist Guide</i></div>'
exec(open(os.path.join(P, 'clips.py')).read())      # C: slot -> (key, start, end); every window checked by eye. CROP / MAXSLOW per key.
def c(n): return K(*C[n])
def veil(t0, t1, a=0.46):
    """the channel puts its titles over a DARK full clip: a soft dark glow behind the words, the clip still shows round it"""
    i = nid('vl')
    els.append(f'<div id="{i}" style="position:absolute;inset:0;z-index:44;opacity:0;pointer-events:none;'
               f'background:radial-gradient(ellipse 50% 46% at 50% 50%, rgba(22,15,11,{a}) 0%, rgba(22,15,11,{a*0.6:.2f}) 55%, rgba(22,15,11,0) 100%)"></div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0}},{{opacity:1,duration:0.5,ease:"sine.out"}},{max(t0 - 0.2, 0):.3f});'); fade_out(i, t1, 0.5)
_q0 = q
def q(html, t0, t1, box_=(660, 0, 1880, H), size=58, cls='', dur=1.4):
    if 'over' in cls and box_ == QC: veil(t0, t1)
    return _q0(html, t0, t1, box_, size=size, cls=cls, dur=dur)
# ---- real press photographs of Diana: framed on the caramel, a slow push-in so a still never sits dead ----
def pic(name, x0, y0, w, h, t0, t1, label=None, pos='50% 30%', zoom=1.08, lsize=50, origin='50% 35%'):
    i = nid('ph'); j = nid('pi'); PHOTOS.append(name)
    els.append(f'<div id="{i}" class="w" style="left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;opacity:0;border-radius:6px;overflow:hidden;box-shadow:0 24px 56px rgba(60,30,12,.30)">'
               f'<img id="{j}" src="assets/{name}" class="photo" style="object-position:{pos};transform-origin:{origin}"></div>')
    _rise(i, t0, t1); tw.append(f'tl.fromTo("#{j}",{{scale:1}},{{scale:{zoom},duration:{t1-t0+0.6:.2f},ease:"none"}},{t0:.3f});')
    if label: plabel(label, x0 + w // 2, y0 + h + 6, t0 + 0.35, t1, lsize)
    return i
PH_H = 900                                              # a tall photo frame, 60 px above, room for the label below
def pics(items, times, t1, h=PH_H, y0=60, gap=44, x0=None, x1=None, zoom=1.08):
    """a row of framed photographs, centred (or inside x0..x1); items = (file, aspect w/h shown, label, object-position)"""
    ws = [int(h * it[1]) for it in items]; tot = sum(ws) + gap * (len(items) - 1); room = (W if x0 is None else x1 - x0) - 80
    if tot > room: h = int(h * (room - gap * (len(items) - 1)) / sum(ws)); ws = [int(h * it[1]) for it in items]; tot = sum(ws) + gap * (len(items) - 1)
    xa = (W - tot) // 2 if x0 is None else x0 + ((x1 - x0) - tot) // 2
    for it, tt, w_ in zip(items, times, ws):
        pic(it[0], xa, y0, w_, h, tt, t1, label=it[2] if len(it) > 2 else None, pos=it[3] if len(it) > 3 else '50% 30%', zoom=zoom); xa += w_ + gap
def picfull(name, t0, t1, pos='50% 30%', zoom=1.06, wfrac=None):
    """a photograph as a full screen the channel's way: the whole picture in the centre over its own soft blurred copy"""
    im = _PILImage.open(os.path.join(A, name)); r = im.width / im.height; w_ = int(min(W, H * r)) if wfrac is None else int(W * wfrac)
    i = nid('pf'); j = nid('pj'); PHOTOS.append(name)
    els.append(f'<div id="{i}" class="w" style="left:0;top:0;width:{W}px;height:{H}px;opacity:0;overflow:hidden">'
               f'<img src="assets/{name}" style="position:absolute;left:-5%;top:-5%;width:110%;height:110%;object-fit:cover;filter:blur(28px) brightness(.90) saturate(.9)">'
               f'<div style="position:absolute;left:{(W-w_)//2}px;top:0;width:{w_}px;height:{H}px;overflow:hidden"><img id="{j}" src="assets/{name}" class="photo" style="object-position:{pos};transform-origin:50% 35%"></div></div>')
    fade_in(i, t0, 0.5); fade_out(i, t1, 0.55)
    tw.append(f'tl.fromTo("#{j}",{{scale:1}},{{scale:{zoom},duration:{t1-t0+0.6:.2f},ease:"none"}},{t0:.3f});'); return i
def when(txt, t0, t1, size=64, y=930):
    """the place and year of an archive picture, in script along the bottom of a full picture"""
    return q(f'<i>{txt}</i>', t0, t1, (180, y, 1740, y + 130), size=size, cls='over', dur=0.9)
def asp(n): im = _PILImage.open(os.path.join(A, n)); return im.width / im.height
def P_(n, label=None, pos='50% 30%', a=None): return (n + '.jpg', a or asp(n + '.jpg'), label, pos)
QB = (160, 810, 1760, 1050)                              # a line along the bottom of a full picture
R3 = (2 * PW + 40, 60, 1890, 1020)                       # the right third beside two clips
RT = (1250, 60, 1890, 1020)                              # the right column beside two framed photographs
def band(html, t0, t1, size=60): return q(html, t0, t1, QB, size=size, cls='over', dur=1.0)
def cardx(txt, t0, t_out, size=None):
    white(t0, t_out); text(txt, 'card', t0 + 0.3, t_out - 0.1, dur=1.2, out=0.45, style=f'font-size:{size}px;' if size else '')
def capt(html, t0, t1, size=56, y=925): return q(html, t0, t1, (160, y, 1760, y + 130), size=size, dur=1.0)
def look(big, small, lines, times, t0, t1, tsmall, pos_b='50% 20%', pos_s='50% 20%'):
    """one off-duty outfit: a tall photograph at the left, a second one beside it, the pieces named at the right as they are said"""
    ab = asp(big + '.jpg'); hb = 980; wb = int(hb * ab); pic(big + '.jpg', 110, 50, wb, hb, t0, t1, pos=pos_b)
    as_ = asp(small + '.jpg'); ws = 400; hs = int(ws / as_)
    if hs > 640: hs = 640; ws = int(hs * as_)
    xs = 110 + wb + 50; pic(small + '.jpg', xs, (H - hs) // 2, ws, hs, tsmall, t1, pos=pos_s)
    qstack(lines, times, t1, box_=(xs + ws + 30, 60, 1890, 1020), size=54, rh=140)
