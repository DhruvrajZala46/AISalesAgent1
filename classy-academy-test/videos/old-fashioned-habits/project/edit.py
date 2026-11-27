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
def full(key, tin, t0, t1, mode='cover', focus=(0.5, 0.5), crop=None, appear='none', **kw):
    return Clip(key, tin, t0, t1, None, mode, crop, appear, focus=focus, **kw)

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

def L(key, tin, t0, t1, i=0, n=1, appear='none', focus=(0.5, 0.5), crop=None, **kw):
    """left-third clip"""
    return Clip(key, tin, t0, t1, (0, 0, 640, 1080), 'cover', crop, appear, focus=focus, **kw)

def framed(key, tin, t0, t1, ratio=4 / 3, appear='none', crop=None, focus=(0.5, 0.5), h=780, **kw):
    w = int(h * ratio); return Clip(key, tin, t0, t1, ((W - w) // 2, (H - h) // 2 + 10, w, h), 'cover', crop, appear, focus=focus, **kw)

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
FH, HB, GO, DF = 'FashionH1940', 'HarpersBazaa', 'Girlonth1940', 'Designfo1956'


# ---------------- MODERN EDIT: creator clips (vertical 720x1280), Classy Academy layouts ----------------
FR = lambda key, tin, t0, t1, **kw: framed('m_' + key, tin, t0, t1, ratio=9 / 16, h=900, **kw)   # framed vertical on cream
def FS(key, tin, t0, t1, **kw):   # vertical clip centred over a soft blur of itself (the reference's full-screen move)
    return Clip('m_' + key, tin, t0, t1, None, FB, **kw)
def PN(key, tin, t0, t1, box, **kw):
    return Clip('m_' + key, tin, t0, t1, box, 'cover', None, 'top', **kw)
def LM(key, tin, t0, t1, **kw):
    return Clip('m_' + key, tin, t0, t1, (0, 0, 640, 1080), 'cover', None, kw.pop('appear', 'none'), **kw)

def build():
    sc = []
    INTRO = S('H1') - 0.25
    sc.append(Scene(0, INTRO, 'black', [UserLogo(0.0, INTRO + 0.3, width=470, fin=0.5, fout=0.0)], logo=False, name='intro'))
    # ================= HOOK =================
    t_h1b = S('H1b'); hk = INTRO + (t_h1b - INTRO) * 0.5
    sc.append(Scene(INTRO, hk, None, [FS('camelwalk46', 0.2, INTRO, hk)], trans='dissolve', tdur=0.5, name='hook_walk'))
    sc.append(Scene(hk, t_h1b - 0.1, None, [FS('camelwalk48', 9.2, hk, t_h1b)], trans='dissolve', name='hook_walk2'))
    t_camel, t_one = Wd('H1b', 'camel'), Wd('H1b', 'one')
    sc.append(Scene(t_h1b - 0.1, t_one - 0.1, 'caramel', [
        PN('whiteshirt25', 3.2, t_h1b - 0.1, t_one, PANEL2[0]),
        PN('whiteshirt17', 2.2, t_camel - 0.1, t_one, PANEL2[1])], name='same_outfit'))
    sc.append(Scene(t_one - 0.1, S('H2') - 0.1, None, [FS('coatbutton31', 0.3, t_one - 0.1, S('H2'))], trans='dissolve', name='one_expensive'))
    t_ev = Wd('H2', 'everything')
    sc.append(Scene(S('H2') - 0.1, t_ev - 0.1, 'cream', [FR('coatbutton28', 0.4, S('H2') - 0.1, t_ev, hold=2.0)], trans='dissolve', name='coat_detail'))
    sc.append(Scene(t_ev - 0.1, S('H3') - 0.1, None, [FS('steamer13', 0.4, t_ev - 0.1, S('H3'))], trans='dissolve', name='steam_hook'))
    t_cls = Wd('H3', 'classroom')
    sc.append(Scene(S('H3') - 0.1, E('H3') + 0.3, None, [FS('ironing0', 11.0, S('H3') - 0.1, E('H3') + 0.3)], trans='dissolve', name='ironing_woman'))
    h1, h2, h3 = Wd('H4', 'how', 1), Wd('H4', 'how', 2), Wd('H4', 'how', 3)
    sc.append(Scene(E('H3') + 0.3, S('H5') - 0.1, 'caramel', [
        PN('ironing0', 30.0, h1 - 0.1, S('H5'), PANEL3[0]),
        PN('hem28', 13.5, h2 - 0.1, S('H5'), PANEL3[1]),
        PN('shoepolish4', 1.5, h3 - 0.1, S('H5'), PANEL3[2])], trans='dissolve', name='three_lessons'))
    t_q = Wd('H5', 'quiet')
    sc.append(Scene(S('H5') - 0.1, t_q - 0.1, None, [FS('posture18', 0.2, S('H5') - 0.1, t_q)], trans='dissolve', name='walk_black_suit'))
    sc.append(Scene(t_q - 0.1, S('H6') - 0.1, None, [FS('posture11', 1.4, t_q - 0.1, S('H6'))], trans='dissolve', name='walk_khaki'))
    tt = S('H6') - 0.1; tm = Wd('H6', 'they'); te = E('H6') + 0.4
    T1 = Text('The Classy Elegance', 'serif', 46, WHITE, W / 2, 330, tt + 0.5, te, wdur=0.3, fout=0.4, shadow=True, fade_in=True)
    T2 = Text('7 Old-Fashioned Habits', 'script', 118, WHITE, W / 2, 400, tt + 0.8, te, wdur=0.7, fout=0.4, shadow=True)
    T3 = Text('That Make Any Outfit Look Expensive', 'script', 96, WHITE, W / 2, 545, tt + 1.4, te, wdur=0.8, fout=0.4, shadow=True, max_w=1600)
    sc.append(Scene(tt, te, None, [FS('polished21', 0.5, tt, tm + 0.1), FS('navycoat15', 1.4, tm, te), Dim(0.25, tt, te), T1, T2, T3],
                    trans='dissolve', out_white=0.5, name='title'))

    # ================= 1. PRESS =================
    sc.append(card(1, 'They Press Before They Dress', te, E('A1') + 0.45))
    t0 = E('A1') + 0.45
    sc.append(split([LM('ironing0', 60.0, t0, S('A3')), LM('ironing12', 3.8, S('A3'), S('A4'), appear='fade')], 'caramel',
                    [('A wrinkled shirt looks careless,', 'serif', 54, Wd('A2', 'careless') - 0.3),
                     ('a pressed one looks considered.', 'script', 84, Wd('A3', 'considered') - 0.3)], t0, S('A4') - 0.1, trans='cut'))
    ta = S('A4') - 0.1; tb = Wd('A4', 'a')
    sc.append(Scene(ta, tb, None, [FS('ironing0', 100.0, ta, tb)], trans='dissolve', name='iron_not_everything'))
    sc.append(Scene(tb, S('A4b') - 0.1, None, [FS('steamer5', 5.4, tb, S('A4b'))], trans='dissolve', name='handheld_steamer'))
    tc = Wd('A4b', 'so')
    sc.append(Scene(S('A4b') - 0.1, S('A5') - 0.1, 'caramel', [
        PN('ironing38', 8.0, S('A4b') - 0.1, S('A5'), PANEL2[0]),
        PN('foldsweater43', 2.6, tc - 0.1, S('A5'), PANEL2[1])], trans='dissolve', name='silk_wool'))
    c1, c2, c3 = Wd('A5', 'collar'), Wd('A5', 'cuffs'), Wd('A5', 'front')
    sc.append(Scene(S('A5') - 0.1, c1 - 0.1, None, [FS('mirror12', 0.4, S('A5') - 0.1, c1)], trans='dissolve', name='busy_morning'))
    sc.append(Scene(c1 - 0.1, S('A5b') - 0.1, 'caramel', [
        PN('clothesbrush36', 4.2, c1 - 0.1, S('A5b'), PANEL3[0]),
        PN('tailor34', 7.4, c2 - 0.1, S('A5b'), PANEL3[1], hold=1.6),
        PN('ironing0', 140.0, c3 - 0.1, S('A5b'), PANEL3[2])], trans='cut', name='collar_cuffs_front'))
    sc.append(Scene(S('A5b') - 0.1, S('A6') - 0.1, 'cream', [FR('hanger14', 1.6, S('A5b') - 0.1, S('A6'))], trans='dissolve', name='hang_straight'))
    tw = Wd('A6', 'than')
    sc.append(Scene(S('A6') - 0.1, tw, None, [FS('whiteshirt41', 14.0, S('A6') - 0.1, tw)], trans='dissolve', name='pressed_result'))
    sc.append(Scene(tw, E('A6') + 0.45, None, [FS('loafers20', 0.4, tw, E('A6') + 0.5)], trans='dissolve', out_white=0.5, name='trench_result'))

    # ================= 2. HANG =================
    sc.append(card(2, 'They Hang It Up the Moment They Take It Off', E('A6') + 0.45, E('B1') + 0.45))
    t0 = E('B1') + 0.45; tm = Wd('B2', 'wake')
    sc.append(Scene(t0, tm, None, [FS('chairpile5', 0.2, t0, tm, hold=3.0)], name='chair_pile'))
    sc.append(Scene(tm, S('B3') - 0.1, None, [FS('chairpile1', 0.2, tm, S('B3'))], trans='dissolve', name='chair_pile2'))
    sc.append(split([LM('hanger49', 0.5, S('B3') - 0.1, S('B4')), LM('foldsweater21', 5.4, S('B4'), S('B4b'), appear='fade')], 'caramel',
                    [('Coats on a shaped hanger.', 'serif', 54, Wd('B3', 'jackets') - 0.2),
                     ('Knitwear, gently folded.', 'script', 84, Wd('B4', 'knitwear') - 0.2)], S('B3') - 0.1, S('B4b') - 0.1))
    tw = Wd('B4b', 'over')
    sc.append(Scene(S('B4b') - 0.1, tw, None, [FS('hanger2', 0.2, S('B4b') - 0.1, tw, hold=4.8)], trans='dissolve', name='wooden_hangers'))
    sc.append(Scene(tw, S('B5') - 0.1, None, [FS('hanger33', 0.3, tw, S('B5'), hold=2.2)], trans='dissolve', name='shoulders'))
    sc.append(Scene(S('B5') - 0.1, S('B6') - 0.1, 'cream', [
        FR('morning24', 0.3, S('B5') - 0.1, Wd('B5', 'before')),
        FR('morning29', 4.2, Wd('B5', 'before'), S('B6'))], trans='dissolve', name='fresh_air'))
    sc.append(Scene(S('B6') - 0.1, E('B6') + 0.45, None, [FS('wardrobe19', 4.4, S('B6') - 0.1, E('B6') + 0.5)], trans='dissolve', out_white=0.5, name='wardrobe'))

    # ================= 3. MEND =================
    sc.append(card(3, 'They Mend Things Right Away', E('B6') + 0.45, E('C1') + 0.45))
    t0 = E('C1') + 0.45; b2, b3 = Wd('C2', 'hem'), Wd('C2', 'tear')
    sc.append(Scene(t0, S('C3') - 0.1, 'caramel', [
        PN('sewing17', 0.4, t0, S('C3'), PANEL3[0]),
        PN('hem28', 7.4, b2 - 0.1, S('C3'), PANEL3[1]),
        PN('tailor9', 0.4, b3 - 0.1, S('C3'), PANEL3[2])], trans='cut', name='button_hem_tear'))
    sc.append(Scene(S('C3') - 0.1, S('C3b') - 0.1, None, [FS('mirror29', 1.5, S('C3') - 0.1, S('C3b'))], trans='dissolve', name='eye_finds'))
    sc.append(white_quote([('The fix takes less time', 'serif', 50, S('C3b')),
                           ('than choosing a different outfit.', 'script', 84, Wd('C3b', 'choosing') - 0.2)], S('C3b') - 0.1, S('C4') - 0.1))
    k1, k2, k3 = Wd('C5', 'black'), Wd('C5', 'white'), Wd('C5', 'beige')
    sc.append(Scene(S('C4') - 0.1, k1 - 0.1, 'cream', [
        FR('sewing20', 61.0, S('C4') - 0.1, Wd('C4', 'repair')),
        FR('sewing20', 75.0, Wd('C4', 'repair'), k1)], trans='dissolve', name='sewing_evening'))
    sw = [(240, 200, 440, 620), (740, 200, 440, 620), (1240, 200, 440, 620)]
    sl = swatch(INK + 18, 'BLACK', sw[0], k1 - 0.1, S('C6')) + swatch(hx('F4F1EA'), 'WHITE', sw[1], k2 - 0.1, S('C6')) + \
         swatch(hx('D8C3A5'), 'BEIGE', sw[2], k3 - 0.1, S('C6'))
    sc.append(Scene(k1 - 0.1, S('C6') - 0.1, 'caramel', sl, trans='cut', name='threads'))
    tt = Wd('C6', 'tailor')
    sc.append(Scene(S('C6') - 0.1, tt, None, [FS('tailor45', 1.2, S('C6') - 0.1, tt)], trans='dissolve', name='tailor_fit'))
    sc.append(Scene(tt, E('C6') + 0.45, None, [FS('tailor34', 1.8, tt, E('C6') + 0.5)], trans='dissolve', out_white=0.5, name='tailored_suit'))

    # ================= 4. BRUSH =================
    sc.append(card(4, 'They Brush Their Coats', E('C6') + 0.45, E('D1') + 0.45))
    t0 = E('D1') + 0.45
    sc.append(Scene(t0, S('D3') - 0.1, None, [FS('navycoat15', 9.5, t0, S('D3'))], name='dark_coat'))
    sc.append(Scene(S('D3') - 0.1, S('D3b') - 0.1, 'cream', [
        FR('clothesbrush36', 0.4, S('D3') - 0.1, Wd('D3', 'lifts'), hold=3.6),
        FR('brush219', 1.0, Wd('D3', 'lifts'), S('D3b'))], trans='dissolve', name='coat_closeup'))
    sc.append(split([LM('navycoat11', 0.4, S('D3b') - 0.1, Wd('D3b', 'neglected')),
                     LM('navycoat24', 0.4, Wd('D3b', 'neglected'), S('D4'), appear='fade')], 'caramel',
                    [('A brushed coat', 'serif', 54, Wd('D3b', 'brushed') - 0.2),
                     ('looks deep and dark.', 'script', 88, Wd('D3b', 'deep') - 0.2)], S('D3b') - 0.1, S('D4') - 0.1))
    ta = Wd('D4', 'and')
    sc.append(Scene(S('D4') - 0.1, ta, None, [FS('brush219', 12.5, S('D4') - 0.1, ta)], trans='dissolve', name='grey_coat'))
    sc.append(Scene(ta, S('D5') - 0.1, None, [FS('coatbutton37', 0.4, ta, S('D5'), hold=2.4)], trans='dissolve', name='rich_coat'))
    tb = Wd('D5', 'but')
    sc.append(Scene(S('D5') - 0.1, tb, None, [FS('lintroller1', 0.3, S('D5') - 0.1, tb, hold=4.0)], trans='dissolve', name='lint_roller'))
    sc.append(Scene(tb, E('D5') + 0.45, None, [FS('loafers20', 5.5, tb, E('D5') + 0.5)], trans='dissolve', out_white=0.5, name='coat_care'))

    # ================= 5. SHOES =================
    sc.append(card(5, 'They Look After Their Shoes', E('D5') + 0.45, E('E1') + 0.45))
    t0 = E('E1') + 0.45
    sc.append(Scene(t0, S('E3') - 0.1, None, [FS('loafers28', 0.3, t0, S('E3'))], name='shoes_walk'))
    sc.append(Scene(S('E3') - 0.1, S('E4') - 0.1, 'cream', [
        FR('shoepolish4', 6.5, S('E3') - 0.1, Wd('E3', 'polish')),
        FR('shoepolish0', 40.0, Wd('E3', 'polish'), S('E4'))], trans='dissolve', name='wipe_polish'))
    sc.append(Scene(S('E4') - 0.1, S('E4b') - 0.1, 'caramel', [
        PN('shoetree26', 10.4, S('E4') - 0.1, S('E4b'), PANEL2[0]),
        PN('shoetree7', 14.4, Wd('E4', 'dry') - 0.1, S('E4b'), PANEL2[1])], trans='dissolve', name='shoe_shape'))
    sc.append(Scene(S('E4b') - 0.1, S('E5') - 0.1, None, [FS('shoepolish13', 29.0, S('E4b') - 0.1, S('E5'))], trans='dissolve', name='shoes_rest'))
    tcb = Wd('E5', 'cobbler')
    sc.append(Scene(S('E5') - 0.1, tcb - 0.1, None, [FS('cobbler41', 4.6, S('E5') - 0.1, tcb)], trans='dissolve', name='heel_tip'))
    sc.append(Scene(tcb - 0.1, S('E6') - 0.1, None, [FS('cobbler42', 5.5, tcb - 0.1, S('E6'))], trans='dissolve', name='cobbler'))
    sc.append(Scene(S('E6') - 0.1, E('E6') + 0.45, None, [FS('loafers35', 0.3, S('E6') - 0.1, E('E6') + 0.5)], trans='dissolve', out_white=0.5, name='cared_shoes'))

    # ================= 6. NIGHT BEFORE =================
    sc.append(card(6, 'They Prepare the Night Before', E('E6') + 0.45, E('F1') + 0.45))
    t0 = E('F1') + 0.45
    sc.append(Scene(t0, S('F3') - 0.1, None, [FS('wardrobe42', 0.3, t0, S('F3'), hold=2.2)], name='evening_wardrobe'))
    n2, n3 = Wd('F3', 'nails'), Wd('F3', 'hair')
    sc.append(Scene(S('F3') - 0.1, S('F4') - 0.1, 'caramel', [
        PN('outfitlaid40', 1.4, S('F3') - 0.1, S('F4'), PANEL3[0], hold=2.6),
        PN('nails14', 0.3, n2 - 0.1, S('F4'), PANEL3[1]),
        PN('silkscarf46', 3.2, n3 - 0.1, S('F4'), PANEL3[2])], trans='dissolve', name='night_panels'))
    sc.append(Scene(S('F4') - 0.1, S('F5') - 0.1, 'cream', [
        FR('mirror30', 2.0, S('F4') - 0.1, Wd('F4', 'check')),
        FR('whiteshirt41', 5.5, Wd('F4', 'check'), S('F5'))], trans='dissolve', name='choose_check'))
    sc.append(split([LM('silkscarf46', 9.5, S('F5') - 0.1, S('F5b'), focus=(0.5, 0.3))], 'caramel',
                    [('Your hair starts the morning', 'serif', 54, Wd('F5', 'starts') - 0.25),
                     ('with shape.', 'script', 96, Wd('F5', 'shape') - 0.2)], S('F5') - 0.1, S('F5b') - 0.1))
    tl = Wd('F5b', 'leaving')
    sc.append(Scene(S('F5b') - 0.1, tl, None, [FS('coatbutton37', 15.5, S('F5b') - 0.1, tl, hold=3.6)], trans='dissolve', name='out_the_door'))
    sc.append(Scene(tl, S('F6') - 0.1, None, [FS('morning13', 3.0, tl, S('F6'))], trans='dissolve', name='calm_morning'))
    sc.append(white_quote([('The morning becomes calm,', 'serif', 52, S('F6')),
                           ('every decision already made.', 'script', 86, Wd('F6', 'every') - 0.2)], S('F6') - 0.1, E('F6') + 0.45, trans='dissolve'))

    # ================= 7. LAST LOOK & STAND TALL =================
    sc.append(card(7, 'They Take One Last Look, and Stand Tall', E('F6') + 0.45, E('G1') + 0.45))
    t0 = E('G1') + 0.45
    sc.append(Scene(t0, S('G3') - 0.1, None, [FS('mirror29', 9.0, t0, S('G3'))], name='mirror'))
    g2, g3 = Wd('G3', 'lint'), Wd('G3', 'strap')
    sc.append(Scene(S('G3') - 0.1, S('G4') - 0.1, 'caramel', [
        PN('whiteshirt17', 0.3, S('G3') - 0.1, S('G4'), PANEL3[0], hold=1.6),
        PN('lintroller1', 5.0, g2 - 0.1, S('G4'), PANEL3[1]),
        PN('mirror30', 12.0, g3 - 0.1, S('G4'), PANEL3[2])], trans='dissolve', name='last_details'))
    sc.append(Scene(S('G4') - 0.1, S('G5') - 0.1, None, [FS('polished21', 5.2, S('G4') - 0.1, S('G5'))], trans='dissolve', name='no_money'))
    sc.append(Scene(S('G5') - 0.1, S('G6') - 0.1, None, [FS('camelwalk39', 0.3, S('G5') - 0.1, S('G6'))], trans='dissolve', name='walk_tall'))
    ws = [Wd('G6', w) for w in ('think', 'talk', 'stand', 'walk')]
    lines = [Text(t, 'script', 104, INK, W / 2, 200 + i * 150, ws[i] - 0.1, S('G7') - 0.1, wdur=0.6, fout=0.3)
             for i, t in enumerate(['Think tall.', 'Talk tall.', 'Stand tall.', 'Walk tall.'])]
    sc.append(Scene(S('G6') - 0.1, S('G7') - 0.1, 'white', lines, logo=False, trans='cut', name='four_lines'))
    tu = Wd('G7', 'that')
    sc.append(Scene(S('G7') - 0.1, tu, None, [FS('navycoat15', 18.0, S('G7') - 0.1, tu)], trans='cut', name='posture_coat'))
    sc.append(Scene(tu, S('G7b') - 0.1, None, [FS('camelwalk48', 0.5, tu, S('G7b'))], trans='dissolve', name='finish_walk'))
    sc.append(split([LM('loafers28', 9.0, S('G7b') - 0.1, E('G7b') + 0.6)], 'caramel',
                    [('Good clothes look their best', 'serif', 54, S('G7b') + 0.1),
                     ('on a woman who carries them with ease.', 'script', 80, Wd('G7b', 'woman') - 0.2)], S('G7b') - 0.1, E('G7b') + 0.6))

    # ================= ENDING =================
    sc.append(Scene(E('G7b') + 0.6, S('Z2') - 0.1, None, [FS('wardrobe19', 14.0, E('G7b') + 0.6, S('Z2'))], trans='dissolve', name='no_bigger_wardrobe'))
    sc.append(white_quote([('It was never about having more.', 'serif', 50, S('Z2')),
                           ('It was about caring for what you already have.', 'script', 78, Wd('Z2', 'caring') - 0.6)], S('Z2') - 0.1, S('Z2b') - 0.1, trans='dissolve'))
    rec = [('press', 'ironing12', 0.3), ('hang', 'hanger49', 5.5), ('mend', 'sewing17', 8.5), ('brush', 'brush219', 15.5),
           ('care', 'shoepolish4', 20.0), ('prepare', 'outfitlaid40', 0.2), ('one', 'mirror30', 21.0)]
    times = [S('Z2b') - 0.1] + [Wd('Z2b', w) - 0.1 for w, _, _ in rec[1:]] + [S('Z3') - 0.1]
    for i, (w, key, tin) in enumerate(rec):
        sc.append(Scene(times[i], times[i + 1], None, [FS(key, tin, times[i], times[i + 1])], trans='dissolve' if i else 'cut', tdur=0.25, name=f'recap_{w}'))
    tz = Wd('Z3', 'every', 1)
    sc.append(Scene(S('Z3') - 0.1, tz - 0.1, None, [FS('whiteshirt41', 22.0, S('Z3') - 0.1, tz)], trans='dissolve', name='care_shows'))
    sc.append(Scene(tz - 0.1, S('Z4') - 0.1, None, [FS('whiteshirt17', 5.1, tz - 0.1, S('Z4'))], trans='dissolve', name='every_button'))
    sc.append(Scene(S('Z4') - 0.1, S('Z5') - 0.1, None, [FS('whiteshirt41', 25.8, S('Z4') - 0.1, S('Z5'))], trans='dissolve', name='comments'))
    sc.append(Scene(S('Z5') - 0.1, E('Z5') + 0.5, None, [FS('coatbutton37', 6.0, S('Z5') - 0.1, E('Z5') + 0.5)], trans='dissolve', name='welcome'))
    sc.append(Scene(E('Z5') + 0.5, DUR, 'black', [UserLogo(E('Z5') + 0.5, DUR, width=470, fin=0.8, fout=0.8)],
                    logo=False, trans='dissolve', tdur=0.8, name='outro'))
    for a, b in zip(sc, sc[1:]):
        assert b.t0 > a.t0, (a.name, b.name)
        a.t1 = b.t0
    return sc

if __name__ == '__main__':
    sc = build()
    for s in sc: print(f'{s.t0:7.2f}-{s.t1:7.2f} {s.t1-s.t0:5.2f} {s.name}')
    print(len(sc), 'scenes; duration', DUR)
