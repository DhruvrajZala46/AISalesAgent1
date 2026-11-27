# edit.py - the edit: every scene timed to the voice (beats.json / words.json)
import json, re, os, sys, difflib
sys.path.insert(0, os.path.dirname(__file__))
from scenes import *

ROOTD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = {b['k']: b for b in json.load(open(ROOTD + '/beats.json'))['beats']}
DUR = json.load(open(ROOTD + '/beats.json'))['duration']
WORDS = json.load(open(ROOTD + '/words.json'))
def S(k): return B[k]['s']
def E(k): return B[k]['e']
def Wd(k, word, n=1):
    """time a word starts inside beat k (n-th occurrence)"""
    c = 0
    for w in WORDS:
        ww = re.sub(r'[^a-z]', '', w['w'].lower())
        if S(k) - 0.35 <= w['s'] <= E(k) + 0.2 and (ww == word or (len(word) > 4 and difflib.SequenceMatcher(None, ww, word).ratio() > 0.78)):
            c += 1
            if c == n: return w['s']
    raise KeyError(f'{word} not in {k}')

M = lambda m, s=0: m * 60 + s  # source timecode helper

# ---------------- layout helpers ----------------
FULL = None
def full(key, tin, t0, t1, mode='cover', focus=(0.5, 0.5), crop=None, appear='none'):
    return Clip(key, tin, t0, t1, None, mode, crop, appear, focus=focus)

PANEL3 = [(140, 110, 520, 860), (700, 110, 520, 860), (1260, 110, 520, 860)]
PANEL2 = [(250, 110, 690, 860), (980, 110, 690, 860)]

def card(n, title, t0, t1):
    """White number card; black script writes on left to right (~1.2 s), fades out 0.4 s."""
    txt = f'{n}. {title}'
    T = Text(txt, 'script', 112, INK, W / 2, 0, t0 + 0.30, t1, wdur=1.25, fout=0.4, max_w=1500)
    w, h = T.size(); T.top = H / 2 - h / 2 - 8
    return Scene(t0, t1, 'white', [T], logo=False, trans='cut', name=f'card{n}')

def quote_lines(lines, cx, ytop, col, gap=18, wdur=0.55, t1=None):
    """lines: [(text, kind, size, t_in)] stacked, centred on cx"""
    out = []; y = ytop
    for txt, kind, size, tin in lines:
        T = Text(txt, kind, size, col, cx, y, tin, t1, wdur=wdur, fout=0.0, max_w=1050)
        out.append(T); y += T.size()[1] * (0.62 if kind == 'serif' else 0.7) + gap
    tot = y - ytop
    return out, tot

def centred_quote(lines, cx, cy, col, t1):
    tmp, tot = quote_lines(lines, cx, 0, col, t1=t1)
    Ls, _ = quote_lines(lines, cx, cy - tot / 2 - 20, col, t1=t1)
    return Ls

def split(clips, side_bg, lines, t0, t1, trans='dissolve', out_white=0.0, name='split'):
    """Clip on the left third, caramel (or white) on the right two-thirds with the principle line."""
    layers = list(clips)
    col = WHITE if side_bg == 'caramel' else INK
    layers += centred_quote(lines, 640 + 640, H / 2, col, t1)
    return Scene(t0, t1, side_bg, layers, logo=True, trans=trans, out_white=out_white, name=name)

def L(key, tin, t0, t1, i=0, n=1, appear='none', focus=(0.5, 0.5), crop=None):
    """left-third clip"""
    return Clip(key, tin, t0, t1, (0, 0, 640, 1080), 'cover', crop, appear, focus=focus)

def framed(key, tin, t0, t1, ratio=4 / 3, appear='none', crop=None, focus=(0.5, 0.5), h=780):
    w = int(h * ratio); return Clip(key, tin, t0, t1, ((W - w) // 2, (H - h) // 2 + 10, w, h), 'cover', crop, appear, focus=focus)

def white_quote(lines, t0, t1, trans='cut', out_white=0.0):
    Ls = centred_quote(lines, W / 2, H / 2, INK, t1)
    return Scene(t0, t1, 'white', Ls, logo=False, trans=trans, out_white=out_white, name='wquote')

def swatch(col, label, box, t0, t1):
    x, y, w, h = box
    tex = np.empty((h, w, 3), np.float32); tex[:] = col
    tex += np.random.default_rng(int(col.sum())).normal(0, 3.0, (h, w, 1)).astype(np.float32)
    lab_col = INK if col.mean() > 150 else WHITE
    R = Rect(tex, box, t0, t1, appear='none')
    T = Text(label, 'caps', 46, lab_col, x + w / 2, y + h / 2 - 40, t0 + 0.15, t1, wdur=0.6, fout=0, tracking=9)
    return [R, T]

CH, AR, HW, HP, SP, BC, SS, RW, OE, CN = ('charade_fhd', 'Aristocr1940', 'HowtoBeW1949', 'HabitPat1954', 'SpeechPl1949',
                                          'BodyCare1948', 'story_of_shoes_2', 'royal-wedding-1951', 'OfficeEt1950', 'Careofth1951')
FB = 'fitblur'

def build():
    sc = []
    # ================= HOOK =================
    t_h1b = S('H1b')
    sc.append(Scene(0, 2.9, None, [full(CH, M(90, 41), 0, 2.9)], name='hook1'))
    sc.append(Scene(2.9, t_h1b, None, [full(CH, M(70, 10), 2.9, t_h1b)], trans='dissolve', name='hook2'))
    # two women, same clothes: two panels arrive on "One" / "The other"
    t_one, t_other = Wd('H1b', 'one'), Wd('H1b', 'other')
    sc.append(Scene(t_h1b, t_one - 0.1, None, [full(AR, M(5, 52), t_h1b, t_one, FB)], trans='dissolve', name='twowomen'))
    sc.append(Scene(t_one - 0.1, S('H2') - 0.2, 'caramel', [
        Clip(CH, M(59, 18), t_one - 0.1, S('H2'), PANEL2[0], appear='top'),
        Clip(OE, M(3, 40), t_other - 0.1, S('H2'), PANEL2[1], appear='top', focus=(0.5, 0.3))], trans='cut', name='twopanels'))
    t_happ = Wd('H2', 'everything')
    sc.append(Scene(S('H2') - 0.2, t_happ - 0.1, None, [full(CH, M(19, 12), S('H2') - 0.2, t_happ)], trans='cut', name='redcoat'))
    sc.append(Scene(t_happ - 0.1, S('H3') - 0.1, None, [full(HW, M(1, 16.5), t_happ - 0.1, S('H3'), FB)], trans='dissolve', name='ironclose'))
    # classroom films: their real title cards, framed on cream
    t_cls = Wd('H3', 'classroom')
    sc.append(Scene(S('H3') - 0.1, E('H3') + 0.3, 'cream', [
        framed(HW, 6.0, S('H3') - 0.1, t_cls, appear='grow'),
        framed(HP, 6.5, t_cls, Wd('H3', 'exactly')),
        framed(HW, 45.8, Wd('H3', 'exactly'), E('H3') + 0.3)], trans='dissolve', name='titlecards'))
    # how to press / mend / care: three panels, one per "How to"
    h1, h2, h3 = Wd('H4', 'how', 1), Wd('H4', 'how', 2), Wd('H4', 'how', 3)
    sc.append(Scene(E('H3') + 0.3, S('H5') - 0.1, 'caramel', [
        Clip(HW, M(1, 21), h1, S('H5'), PANEL3[0], appear='top', focus=(0.45, 0.5)),
        Clip(HW, M(2, 16.2), h2, S('H5'), PANEL3[1], appear='top', focus=(0.35, 0.5)),
        Clip(AR, M(4, 15), h3, S('H5'), PANEL3[2], appear='top', focus=(0.5, 0.5))], trans='dissolve', name='howto'))
    t_quiet = Wd('H5', 'quiet')
    sc.append(Scene(S('H5') - 0.1, t_quiet - 0.2, None, [full(CH, M(16, 20), S('H5') - 0.1, t_quiet)], trans='dissolve', name='veil'))
    sc.append(Scene(t_quiet - 0.2, S('H6') - 0.1, None, [full(RW, M(11, 40), t_quiet - 0.2, S('H6'), FB)], trans='dissolve', name='rw_redcoat'))
    # title over film, title holds while the clip changes underneath
    tt = S('H6') - 0.1; tm = Wd('H6', 'they'); te = E('H6') + 0.4
    title_layers = [full(CH, M(57, 44), tt, tm + 0.1), full(CH, M(59, 40), tm, te), Dim(0.22, tt, te)]
    T1 = Text('The Classy Elegance', 'serif', 46, WHITE, W / 2, 330, tt + 0.5, te, wdur=0.3, fout=0.4, shadow=True, fade_in=True)
    T2 = Text('7 Old-Fashioned Habits', 'script', 118, WHITE, W / 2, 400, tt + 0.8, te, wdur=0.7, fout=0.4, shadow=True)
    T3 = Text('That Make Any Outfit Look Expensive', 'script', 96, WHITE, W / 2, 545, tt + 1.4, te, wdur=0.8, fout=0.4, shadow=True, max_w=1600)
    sc.append(Scene(tt, te, None, title_layers + [T1, T2, T3], trans='dissolve', out_white=0.5, name='title'))

    # ================= 1. PRESS =================
    sc.append(card(1, 'They Press Before They Dress', te, E('A1') + 0.45))
    t0 = E('A1') + 0.45
    sc.append(split([L(HP, M(3, 21), t0, S('A3')), L(HW, M(1, 17), S('A3'), S('A4'), appear='fade')], 'caramel',
                    [('A wrinkled shirt looks careless,', 'serif', 54, Wd('A2', 'careless') - 0.3),
                     ('a pressed one looks considered.', 'script', 84, Wd('A3', 'considered') - 0.3)], t0, S('A4') - 0.1, trans='cut'))
    ta = S('A4') - 0.1; tb = Wd('A4', 'a')
    sc.append(Scene(ta, tb, None, [full(HW, M(1, 21.5), ta, tb, FB)], trans='dissolve', name='ironwoman'))
    sc.append(Scene(tb, S('A4b') - 0.1, None, [full(HW, M(2, 21.5), tb, S('A4b'), FB, crop=(80, 0, 480, 480))], trans='dissolve', name='irontrousers'))
    tc = Wd('A4b', 'so')
    sc.append(Scene(S('A4b') - 0.1, S('A5') - 0.1, 'caramel', [
        Clip(AR, M(7, 19), S('A4b') - 0.1, S('A5'), PANEL2[0], appear='top'),
        Clip(AR, M(5, 10), tc, S('A5'), PANEL2[1], appear='top')], trans='dissolve', name='silkwool'))
    c1, c2, c3 = Wd('A5', 'collar'), Wd('A5', 'cuffs'), Wd('A5', 'front')
    sc.append(Scene(S('A5') - 0.1, c1 - 0.1, None, [full(HW, M(6, 21), S('A5') - 0.1, c1, FB)], trans='dissolve', name='busymorning'))
    sc.append(Scene(c1 - 0.1, S('A5b') - 0.1, 'caramel', [
        Clip(OE, M(1, 9), c1 - 0.1, S('A5b'), PANEL3[0], appear='top', focus=(0.5, 0.5)),
        Clip(HW, M(6, 12), c2 - 0.1, S('A5b'), PANEL3[1], appear='top', focus=(0.5, 0.5)),
        Clip(AR, M(1, 25), c3 - 0.1, S('A5b'), PANEL3[2], appear='top', focus=(0.35, 0.5))], trans='cut', name='collarcuffs'))
    sc.append(Scene(S('A5b') - 0.1, S('A6') - 0.1, 'cream', [
        framed(HW, M(5, 50), S('A5b') - 0.1, Wd('A5b', 'so')),
        framed(HW, M(6, 25), Wd('A5b', 'so'), S('A6'))], trans='dissolve', name='hangstraight'))
    tw = Wd('A6', 'than')
    sc.append(Scene(S('A6') - 0.1, tw, None, [full(CH, M(10, 40), S('A6') - 0.1, tw)], trans='dissolve', name='whitecoat'))
    sc.append(Scene(tw, E('A6') + 0.45, None, [full(CH, M(8, 12), tw, E('A6') + 0.5)], trans='dissolve', out_white=0.5, name='whitecoat2'))

    # ================= 2. HANG =================
    sc.append(card(2, 'They Hang It Up the Moment They Take It Off', E('A6') + 0.45, E('B1') + 0.45))
    t0 = E('B1') + 0.45; tm = Wd('B2', 'wake')
    sc.append(Scene(t0, tm, None, [full(HP, M(3, 54), t0, tm, FB)], name='chairpile'))
    sc.append(Scene(tm, S('B3') - 0.1, None, [full(HP, M(3, 33), tm, S('B3'), FB)], trans='dissolve', name='messyroom'))
    sc.append(split([L(HP, M(2, 11), S('B3') - 0.1, S('B4')), L(HP, M(2, 3.6), S('B4'), S('B4b'), appear='fade')], 'caramel',
                    [('Coats on a shaped hanger.', 'serif', 54, Wd('B3', 'jackets') - 0.2),
                     ('Knitwear, gently folded.', 'script', 84, Wd('B4', 'knitwear') - 0.2)], S('B3') - 0.1, S('B4b') - 0.1))
    tw = Wd('B4b', 'over')
    sc.append(Scene(S('B4b') - 0.1, tw, None, [full(HW, M(6, 11.8), S('B4b') - 0.1, tw, FB)], trans='dissolve', name='blouses'))
    sc.append(Scene(tw, S('B5') - 0.1, None, [full(AR, M(3, 30), tw, S('B5'), FB)], trans='dissolve', name='shoulders'))
    sc.append(Scene(S('B5') - 0.1, S('B6') - 0.1, 'cream', [
        framed(HW, M(3, 13.5), S('B5') - 0.1, Wd('B5', 'before')),
        framed(HP, M(12, 36), Wd('B5', 'before'), S('B6'))], trans='dissolve', name='nightair'))
    sc.append(Scene(S('B6') - 0.1, E('B6') + 0.45, None, [full(CH, M(26, 10), S('B6') - 0.1, E('B6') + 0.5)], trans='dissolve', out_white=0.5, name='park'))

    # ================= 3. MEND =================
    sc.append(card(3, 'They Mend Things Right Away', E('B6') + 0.45, E('C1') + 0.45))
    t0 = E('C1') + 0.45; b1, b2, b3 = Wd('C2', 'button'), Wd('C2', 'hem'), Wd('C2', 'tear')
    sc.append(Scene(t0, S('C3') - 0.1, 'caramel', [
        Clip(HW, M(1, 43.2), t0, S('C3'), PANEL3[0], appear='top', focus=(0.5, 0.5)),
        Clip(AR, M(5, 12), b2 - 0.1, S('C3'), PANEL3[1], appear='top', focus=(0.5, 0.7)),
        Clip(CH, M(9, 22), b3 - 0.1, S('C3'), PANEL3[2], appear='top', focus=(0.55, 0.5))], trans='cut', name='button_hem'))
    sc.append(Scene(S('C3') - 0.1, S('C3b') - 0.1, None, [full(CH, M(45, 40), S('C3') - 0.1, S('C3b'))], trans='dissolve', name='eyefinds'))
    sc.append(white_quote([('The fix takes less time', 'serif', 50, S('C3b')),
                           ('than choosing a different outfit.', 'script', 84, Wd('C3b', 'choosing') - 0.2)], S('C3b') - 0.1, S('C4') - 0.1))
    sc.append(Scene(S('C4') - 0.1, S('C5') - 0.1, 'cream', [
        framed(HP, 7.0, S('C4') - 0.1, Wd('C4', 'a')),
        framed(HW, M(2, 13.5), Wd('C4', 'a'), Wd('C4', 'repair')),
        framed(HW, M(2, 16.3), Wd('C4', 'repair'), S('C5'), crop=(0, 60, 480, 360))], trans='dissolve', name='sewingbox'))
    k1, k2, k3, k4 = Wd('C5', 'black'), Wd('C5', 'white'), Wd('C5', 'beige'), Wd('C5', 'buttons')
    sw = [(240, 200, 440, 620), (740, 200, 440, 620), (1240, 200, 440, 620)]
    sl = swatch(INK + 18, 'BLACK', sw[0], k1 - 0.1, S('C6')) + swatch(hx('F4F1EA'), 'WHITE', sw[1], k2 - 0.1, S('C6')) + \
         swatch(hx('D8C3A5'), 'BEIGE', sw[2], k3 - 0.1, S('C6'))
    sc.append(Scene(S('C5') - 0.1, k4 - 0.15, None, [framed(HW, M(2, 18), S('C5') - 0.1, k1, h=1080 - 40)], trans='dissolve', name='needles'))
    sc[-1].t1 = k1 - 0.1
    sc.append(Scene(k1 - 0.1, k4 - 0.1, 'caramel', sl, trans='cut', name='threads'))
    sc.append(Scene(k4 - 0.1, S('C6') - 0.1, None, [full(CN, M(8, 22), k4 - 0.1, S('C6'), FB)], trans='dissolve', name='hands'))
    tt = Wd('C6', 'tailor')
    sc.append(Scene(S('C6') - 0.1, tt, None, [full(AR, M(3, 52), S('C6') - 0.1, tt, FB)], trans='dissolve', name='fitting'))
    sc.append(Scene(tt, E('C6') + 0.45, None, [full(CH, M(70, 45), tt, E('C6') + 0.5)], trans='dissolve', out_white=0.5, name='tailored'))

    # ================= 4. BRUSH =================
    sc.append(card(4, 'They Brush Their Coats', E('C6') + 0.45, E('D1') + 0.45))
    t0 = E('D1') + 0.45
    sc.append(Scene(t0, S('D3') - 0.1, None, [full(CH, M(18, 40), t0, S('D3'))], name='darkcoat'))
    sc.append(Scene(S('D3') - 0.1, S('D3b') - 0.1, 'cream', [
        framed(SP, M(2, 10), S('D3') - 0.1, Wd('D3', 'lifts')),
        framed(SP, M(2, 20), Wd('D3', 'lifts'), S('D3b'), crop=(60, 40, 440, 330))], trans='dissolve', name='brush'))
    sc.append(split([L(CH, M(17, 0), S('D3b') - 0.1, Wd('D3b', 'neglected')), L(OE, M(3, 40.5), Wd('D3b', 'neglected'), S('D4'), appear='fade', focus=(0.5, 0.5))], 'caramel',
                    [('A brushed coat', 'serif', 54, Wd('D3b', 'brushed') - 0.2),
                     ('looks deep and dark.', 'script', 88, Wd('D3b', 'deep') - 0.2)], S('D3b') - 0.1, S('D4') - 0.1))
    sc.append(Scene(S('D4') - 0.1, Wd('D4', 'and'), None, [full(SP, M(2, 30), S('D4') - 0.1, Wd('D4', 'and'), FB)], trans='dissolve', name='brushlength'))
    sc.append(Scene(Wd('D4', 'and'), S('D5') - 0.1, None, [full(CH, M(69, 47), Wd('D4', 'and'), S('D5'))], trans='dissolve', name='richcoat'))
    sc.append(Scene(S('D5') - 0.1, Wd('D5', 'but'), None, [full(HW, M(9, 44), S('D5') - 0.1, Wd('D5', 'but'), FB)], trans='dissolve', name='door'))
    sc.append(Scene(Wd('D5', 'but'), E('D5') + 0.45, None, [full(HW, M(10, 4), Wd('D5', 'but'), E('D5') + 0.5, FB)], trans='dissolve', out_white=0.5, name='doorface'))

    # ================= 5. SHOES =================
    sc.append(card(5, 'They Look After Their Shoes', E('D5') + 0.45, E('E1') + 0.45))
    t0 = E('E1') + 0.45
    sc.append(Scene(t0, S('E3') - 0.1, None, [full(SP, M(5, 54.3), t0, S('E3'), FB)], name='shoesclose'))
    sc.append(Scene(S('E3') - 0.1, S('E4') - 0.1, 'cream', [framed(HW, M(1, 59), S('E3') - 0.1, S('E4'), crop=(200, 140, 440, 330))], trans='dissolve', name='polish'))
    sc.append(Scene(S('E4') - 0.1, S('E4b') - 0.1, 'caramel', [
        Clip(SS, M(1, 6), S('E4') - 0.1, S('E4b'), PANEL2[0], appear='top'),
        Clip(SS, M(2, 43), Wd('E4', 'dry') - 0.1, S('E4b'), PANEL2[1], appear='top')], trans='dissolve', name='shoetrees'))
    sc.append(Scene(S('E4b') - 0.1, S('E5') - 0.1, None, [full(SP, M(5, 40), S('E4b') - 0.1, S('E5'), FB)], trans='dissolve', name='rest'))
    tcb = Wd('E5', 'cobbler')
    sc.append(Scene(S('E5') - 0.1, tcb - 0.1, None, [full(SS, M(7, 24), S('E5') - 0.1, tcb, FB)], trans='dissolve', name='heel'))
    sc.append(Scene(tcb - 0.1, S('E6') - 0.1, None, [full(SS, M(4, 26), tcb - 0.1, S('E6'), FB)], trans='dissolve', name='cobbler'))
    sc.append(Scene(S('E6') - 0.1, E('E6') + 0.45, None, [full(CH, M(8, 14), S('E6') - 0.1, E('E6') + 0.5)], trans='dissolve', out_white=0.5, name='walkwhite'))

    # ================= 6. NIGHT BEFORE =================
    sc.append(card(6, 'They Prepare the Night Before', E('E6') + 0.45, E('F1') + 0.45))
    t0 = E('F1') + 0.45
    sc.append(Scene(t0, S('F3') - 0.1, None, [full(HW, M(3, 38.6), t0, S('F3'), FB)], name='clock'))
    n1, n2, n3 = Wd('F3', 'laid'), Wd('F3', 'nails'), Wd('F3', 'hair')
    sc.append(Scene(S('F3') - 0.1, S('F4') - 0.1, 'caramel', [
        Clip(HP, M(11, 40), S('F3') - 0.1, S('F4'), PANEL3[0], appear='top', focus=(0.4, 0.5)),
        Clip(HW, M(2, 48.8), n2 - 0.1, S('F4'), PANEL3[1], appear='top', focus=(0.5, 0.5)),
        Clip(HW, M(2, 36.5), n3 - 0.1, S('F4'), PANEL3[2], appear='top', focus=(0.62, 0.5))], trans='dissolve', name='nightpanels'))
    sc.append(Scene(S('F4') - 0.1, S('F5') - 0.1, 'cream', [
        framed(HW, M(6, 19), S('F4') - 0.1, Wd('F4', 'check')),
        framed(HW, M(6, 1), Wd('F4', 'check'), S('F5'))], trans='dissolve', name='choose'))
    sc.append(split([L(HW, M(2, 58.6), S('F5') - 0.1, S('F5b'), focus=(0.55, 0.5))], 'caramel',
                    [('Your hair starts the morning', 'serif', 54, Wd('F5', 'starts') - 0.25),
                     ('with shape.', 'script', 96, Wd('F5', 'shape') - 0.2)], S('F5') - 0.1, S('F5b') - 0.1))
    tl = Wd('F5b', 'leaving')
    sc.append(Scene(S('F5b') - 0.1, tl, None, [full(HP, M(4, 22), S('F5b') - 0.1, tl, FB)], trans='dissolve', name='rush'))
    sc.append(Scene(tl, S('F6') - 0.1, None, [full(HP, M(12, 29), tl, S('F6'), FB)], trans='dissolve', name='calmnight'))
    sc.append(white_quote([('The morning becomes calm,', 'serif', 52, S('F6')),
                           ('every decision already made.', 'script', 86, Wd('F6', 'every') - 0.2)], S('F6') - 0.1, E('F6') + 0.45, trans='dissolve'))

    # ================= 7. LAST LOOK & STAND TALL =================
    sc.append(card(7, 'They Take One Last Look, and Stand Tall', E('F6') + 0.45, E('G1') + 0.45))
    sc[-2].out_white = 0.0
    t0 = E('G1') + 0.45
    sc.append(Scene(t0, S('G3') - 0.1, None, [full(HW, M(8, 43.5), t0, S('G3'), FB)], name='mirror'))
    g1, g2, g3 = Wd('G3', 'tag'), Wd('G3', 'lint'), Wd('G3', 'strap')
    sc.append(Scene(S('G3') - 0.1, S('G4') - 0.1, 'caramel', [
        Clip(HW, M(9, 45), S('G3') - 0.1, S('G4'), PANEL3[0], appear='top', focus=(0.45, 0.5)),
        Clip(AR, M(3, 33), g2 - 0.1, S('G4'), PANEL3[1], appear='top', focus=(0.5, 0.5)),
        Clip(HP, M(11, 12), g3 - 0.1, S('G4'), PANEL3[2], appear='top', focus=(0.5, 0.5))], trans='dissolve', name='checks'))
    sc.append(Scene(S('G4') - 0.1, S('G5') - 0.1, None, [full(CH, M(73, 14), S('G4') - 0.1, S('G5'))], trans='dissolve', name='smile'))
    sc.append(Scene(S('G5') - 0.1, S('G6') - 0.1, 'cream', [framed(SP, 8.5, S('G5') - 0.1, S('G6'))], trans='dissolve', name='speechtitle'))
    sc.append(Scene(S('G6') - 0.1, S('G7') - 0.1, None, [full(SP, M(4, 44.6), S('G6') - 0.1, S('G7'), FB)], trans='cut', name='thinktall'))
    tu = Wd('G7', 'that')
    sc.append(Scene(S('G7') - 0.1, tu, None, [full(BC, M(1, 34), S('G7') - 0.1, tu, FB)], trans='dissolve', name='walkbook'))
    sc.append(Scene(tu, S('G7b') - 0.1, None, [full(CH, M(90, 46), tu, S('G7b'))], trans='dissolve', name='walkyellow'))
    sc.append(split([L(CH, M(25, 50), S('G7b') - 0.1, E('G7b') + 0.6, focus=(0.62, 0.5))], 'caramel',
                    [('Good clothes look their best', 'serif', 54, S('G7b') + 0.1),
                     ('on a woman who carries them with ease.', 'script', 80, Wd('G7b', 'woman') - 0.2)], S('G7b') - 0.1, E('G7b') + 0.6))

    # ================= ENDING =================
    sc.append(Scene(E('G7b') + 0.6, S('Z2') - 0.1, None, [full(AR, M(6, 21), E('G7b') + 0.6, S('Z2'), FB)], trans='dissolve', name='group'))
    sc.append(white_quote([('It was never about having more.', 'serif', 50, S('Z2')),
                           ('It was about caring for what you already have.', 'script', 78, Wd('Z2', 'caring') - 0.6)], S('Z2') - 0.1, S('Z2b') - 0.1, trans='dissolve'))
    rec = [('press', HW, M(1, 22.5)), ('hang', HP, M(2, 12.5)), ('mend', HW, M(2, 17)), ('brush', SP, M(2, 15)),
           ('care', SS, M(1, 9)), ('prepare', HP, M(11, 45)), ('one', CH, M(5, 30))]
    times = [S('Z2b') - 0.1] + [Wd('Z2b', w) - 0.1 for w, _, _ in rec[1:]] + [S('Z3') - 0.1]
    for i, (w, key, tin) in enumerate(rec):
        mode = 'cover' if key == CH else FB
        sc.append(Scene(times[i], times[i + 1], None, [full(key, tin, times[i], times[i + 1], mode)], trans='dissolve' if i else 'cut', tdur=0.25, name=f'recap_{w}'))
    tz = Wd('Z3', 'in')
    sc.append(Scene(S('Z3') - 0.1, tz, None, [full(CH, M(59, 42), S('Z3') - 0.1, tz)], trans='dissolve', name='care'))
    sc.append(Scene(tz, S('Z4') - 0.1, None, [full(RW, M(28, 5), tz, S('Z4'), FB)], trans='dissolve', name='rw_phone'))
    sc.append(Scene(S('Z4') - 0.1, S('Z5') - 0.1, None, [full(AR, M(5, 52.5), S('Z4') - 0.1, S('Z5'), FB)], trans='dissolve', name='comments'))
    sc.append(Scene(S('Z5') - 0.1, E('Z5') + 0.5, None, [full(CH, M(73, 40), S('Z5') - 0.1, E('Z5') + 0.5)], trans='dissolve', out_white=0.6, name='welcome'))
    # end card: rose-gold logo on white, held for the end screen
    sc.append(Scene(E('Z5') + 0.5, DUR, 'white', [Logo(E('Z5') + 0.5, DUR, kind='rose', size=360, pos=(W / 2 - 180, H / 2 - 190), opacity=1.0, fade=0.8)],
                    logo=False, trans='cut', name='endcard'))
    # sanity: contiguous, increasing
    for a, b in zip(sc, sc[1:]):
        assert abs(a.t1 - b.t0) < 1e-6 or b.t0 > a.t0, (a.name, b.name)
        b.t0 = max(b.t0, a.t0 + 0.05); a.t1 = b.t0
    return sc

if __name__ == '__main__':
    sc = build()
    for s in sc: print(f'{s.t0:7.2f}-{s.t1:7.2f} {s.t1-s.t0:5.2f} {s.name}')
    print(len(sc), 'scenes; duration', DUR)
