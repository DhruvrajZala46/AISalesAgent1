
# ---------------- "8 Things Elegant Ladies Never Wear" - modern creator footage, Classy Academy layouts ----------------
FR = lambda key, tin, t0, t1, **kw: framed('m_' + key, tin, t0, t1, ratio=9 / 16, h=900, **kw)
def FS(key, tin, t0, t1, **kw): return Clip('m_' + key, tin, t0, t1, None, FB, **kw)
def PN(key, tin, t0, t1, box, **kw): return Clip('m_' + key, tin, t0, t1, box, 'cover', kw.pop('crop', None), 'top', **kw)
def LM(key, tin, t0, t1, **kw): return Clip('m_' + key, tin, t0, t1, (0, 0, 640, 1080), 'cover', kw.pop('crop', None), kw.pop('appear', 'none'), **kw)
P4 = [(110, 150, 400, 700), (560, 150, 400, 700), (1010, 150, 400, 700), (1460, 150, 400, 700)]

def words_card(items, times, t0, t1, bg='cream', col=None):
    col = INK if col is None else col
    L = []
    for i, (w, tt) in enumerate(zip(items, times)):
        L.append(Text(w, 'caps', 58, col, W / 2, 250 + i * 150, tt - 0.05, t1, wdur=0.5, fout=0, tracking=12))
    return Scene(t0, t1, bg, L, logo=True, trans='dissolve', name='words')

def swatches(cols, labels, times, t0, t1, name):
    n = len(cols); w = 300 if n > 3 else 420; gap = 40; tot = n * w + (n - 1) * gap; x0 = (W - tot) // 2
    L = []
    for i, (c, lab, tt) in enumerate(zip(cols, labels, times)):
        sw_ = swatch(hx(c), lab or ' x', (x0 + i * (w + gap), 200, w, 620), tt - 0.1, t1)
        L += sw_ if lab else sw_[:1]
    return Scene(t0, t1, 'caramel', L, trans='dissolve', name=name)

def build():
    sc = []
    INTRO = S('H1') - 0.25
    sc.append(Scene(0, INTRO, 'black', [UserLogo(0.0, INTRO + 0.3, width=470, fin=0.5, fout=0.0)], logo=False, name='intro'))
    # ---------- HOOK ----------
    t_ev = Wd('H1', 'somehow')
    sc.append(Scene(INTRO, t_ev - 0.1, None, [FS('camelwalk46', 0.2, INTRO, t_ev)], trans='dissolve', tdur=0.5, name='hook_walk'))
    sc.append(Scene(t_ev - 0.1, S('H1b') - 0.1, None, [FS('simpledress19', 0.3, t_ev - 0.1, S('H1b'))], trans='dissolve', name='hook_notice'))
    t_op = Wd('H1b', 'often')
    sc.append(Scene(S('H1b') - 0.1, t_op - 0.1, None, [FS('simpledress34', 0.3, S('H1b') - 0.1, t_op)], trans='dissolve', name='simple_dress'))
    sc.append(Scene(t_op - 0.1, S('H2') - 0.1, None, [FS('fineknit1', 0.3, t_op - 0.1, S('H2'))], trans='dissolve', name='simple_knit'))
    t_imp = Wd('H2', 'important')
    sc.append(Scene(S('H2') - 0.1, t_imp, 'caramel', [
        PN('simpledress9', 1.0, S('H2') - 0.1, t_imp + 3, PANEL2[0]),
        PN('silk12', 4.6, Wd('H2', 'choices') - 0.1, t_imp + 3, PANEL2[1])], name='quiet_choices'))
    sc.append(Scene(t_imp, S('H3') - 0.1, None, [FS('wardrobe19', 4.4, t_imp, S('H3'))], trans='dissolve', name='leaves_in_shop'))
    tt = S('H3') - 0.1; te = E('H3') + 0.5; tm = Wd('H3', 'and')
    T1 = Text('The Classy Elegance', 'serif', 46, WHITE, W / 2, 330, tt + 0.5, te, wdur=0.3, fout=0.4, shadow=True, fade_in=True)
    T2 = Text('8 Things Elegant Ladies', 'script', 118, WHITE, W / 2, 400, tt + 0.8, te, wdur=0.7, fout=0.4, shadow=True)
    T3 = Text('Never Wear', 'script', 118, WHITE, W / 2, 545, tt + 1.3, te, wdur=0.6, fout=0.4, shadow=True)
    sc.append(Scene(tt, te, None, [FS('simpledress2', 0.5, tt, tm + 0.1), FS('silk12', 0.4, tm, te), Dim(0.25, tt, te), T1, T2, T3],
                    trans='dissolve', name='title'))
    t_fine = Wd('H4', 'fine')
    sc.append(Scene(te, t_fine - 0.1, None, [FS('mirror30', 2.0, te, t_fine)], trans='dissolve', name='your_wardrobe'))
    sc.append(Scene(t_fine - 0.1, E('H4') + 0.45, None, [FS('hanger49', 0.5, t_fine - 0.1, E('H4') + 0.5)], trans='dissolve', out_white=0.5, name='swap'))

    # ---------- 1. LOGOS ----------
    sc.append(card(1, 'Loud, Oversized Logos', E('H4') + 0.45, E('A1') + 0.45))
    t0 = E('A1') + 0.45; tb = Wd('A2', 'brand')
    sc.append(Scene(t0, tb - 0.1, None, [FS('logobag1', 2.2, t0, tb, hold=6.0)], name='logo_bag'))
    sc.append(Scene(tb - 0.1, S('A3') - 0.1, None, [FS('logobag1', 0.2, tb - 0.1, S('A3'), hold=2.0)], trans='dissolve', name='logo_walk'))
    sc.append(white_quote([('Elegance rarely needs', 'serif', 52, S('A3')),
                           ('to announce itself.', 'script', 92, Wd('A3', 'announce') - 0.2)], S('A3') - 0.1, S('A4') - 0.1, trans='dissolve'))
    t_tan = Wd('A4', 'tan')
    sc.append(Scene(S('A4') - 0.1, S('A5') - 0.1, 'caramel', [
        PN('leatherbag23', 0.4, S('A4') - 0.1, S('A5'), PANEL3[0]),
        PN('hardware36', 1.5, t_tan - 0.1, S('A5'), PANEL3[1]),
        PN('leatherbag26', 1.0, Wd('A4', 'cream') - 0.1, S('A5'), PANEL3[2])], trans='dissolve', name='leather_bags'))
    sc.append(Scene(S('A5') - 0.1, S('A5b') - 0.1, None, [FS('fineknit11', 1.0, S('A5') - 0.1, S('A5b'))], trans='dissolve', name='fine_knit'))
    sc.append(Scene(S('A5b') - 0.1, S('A6') - 0.1, 'cream', [
        FR('hardware17', 0.2, S('A5b') - 0.1, Wd('A5b', 'leather'), hold=4.0),
        FR('hardware36', 15.0, Wd('A5b', 'leather'), S('A6'))], trans='dissolve', name='details'))
    sc.append(split([LM('fineknit40', 8.0, S('A6') - 0.1, E('A6') + 0.6)], 'caramel',
                    [('When the quality is in the cut,', 'serif', 52, S('A6')),
                     ('there is nothing left to prove.', 'script', 84, Wd('A6', 'nothing') - 0.2)], S('A6') - 0.1, E('A6') + 0.45, out_white=0.5))

    # ---------- 2. FIT ----------
    sc.append(card(2, 'Clothes That Do Not Fit You', E('A6') + 0.45, E('B1') + 0.45))
    t0 = E('B1') + 0.45; tpool = Wd('B2', 'trousers')
    sc.append(Scene(t0, S('B3') - 0.1, 'caramel', [
        PN('blazerfit11', 0.3, t0, S('B3'), PANEL2[0], crop=(0, 330, 720, 950), hold=2.8),
        PN('trouserhem42', 11.0, tpool - 0.1, S('B3'), PANEL2[1], crop=(0, 0, 720, 1000))], trans='cut', name='fit_problems'))
    sc.append(split([LM('tailor33', 1.0, S('B3') - 0.1, S('B4'), crop=(0, 330, 720, 950))], 'caramel',
                    [('Even a beautiful piece looks inexpensive', 'serif', 50, S('B3')),
                     ('when it fights your body.', 'script', 88, Wd('B3', 'fights') - 0.2)], S('B3') - 0.1, S('B4') - 0.1, trans='dissolve'))
    sc.append(Scene(S('B4') - 0.1, S('B5') - 0.1, None, [FS('tailor34', 0.9, S('B4') - 0.1, S('B5'))], trans='dissolve', name='fits_well'))
    ts, tsl, ttr = Wd('B5', 'shoulder'), Wd('B5', 'sleeves'), Wd('B5', 'trousers')
    sc.append(Scene(S('B5') - 0.1, S('B6') - 0.1, 'caramel', [
        PN('blazerfit30', 9.0, ts - 0.1, S('B6'), PANEL3[0]),
        PN('tailor34', 7.4, tsl - 0.1, S('B6'), PANEL3[1], hold=1.6),
        PN('trouserhem8', 9.4, ttr - 0.1, S('B6'), PANEL3[2])], trans='dissolve', name='fit_rules'))
    tt = Wd('B6', 'tailor')
    sc.append(Scene(S('B6') - 0.1, tt - 0.1, None, [FS('blazerfit4', 16.0, S('B6') - 0.1, tt)], trans='dissolve', name='buy_shoulders'))
    sc.append(Scene(tt - 0.1, S('B7') - 0.1, None, [FS('tailor45', 1.2, tt - 0.1, S('B7'))], trans='dissolve', name='tailor'))
    sc.append(Scene(S('B7') - 0.1, S('B7b') - 0.1, None, [FS('whiteshirt25', 3.0, S('B7') - 0.1, S('B7b'))], trans='dissolve', name='made_for_you'))
    sc.append(Scene(S('B7b') - 0.1, E('B7b') + 0.45, 'cream', [
        FR('trouserhem22', 3.0, S('B7b') - 0.1, Wd('B7b', 'changes')),
        FR('trouserhem22', 10.0, Wd('B7b', 'changes'), E('B7b') + 0.5)], trans='dissolve', out_white=0.5, name='hemming'))

    # ---------- 3. FABRICS ----------
    sc.append(card(3, 'Shiny, Synthetic Fabrics', E('B7b') + 0.45, E('C1') + 0.45))
    t0 = E('C1') + 0.45
    sc.append(Scene(t0, S('C3') - 0.1, 'cream', [FR('shinysatin28', 0.4, t0, S('C3'), speed=0.27)], name='shiny'))
    sc.append(white_quote([('Elegant women reach for', 'serif', 52, S('C3')),
                           ('texture instead.', 'script', 96, Wd('C3', 'texture') - 0.2)], S('C3') - 0.1, S('C4') - 0.1, trans='dissolve'))
    w1, w2, w3, w4 = Wd('C4', 'wool'), Wd('C4', 'crisp'), Wd('C4', 'linen'), Wd('C4', 'silk')
    sc.append(Scene(S('C4') - 0.1, S('C5') - 0.1, 'caramel', [
        Clip('m_woolfabric37', 0.2, S('C4') - 0.1, S('C5'), P4[0], 'cover', None, 'top', hold=6.0),
        Clip('m_darkjeans5', 12.0, w2 - 0.1, S('C5'), P4[1], 'cover', (0, 200, 720, 1080), 'top'),
        Clip('m_linen15', 1.0, w3 - 0.1, S('C5'), P4[2], 'cover', None, 'top'),
        Clip('m_silk0', 19.0, w4 - 0.1, S('C5'), P4[3], 'cover', None, 'top')], trans='dissolve', name='textures'))
    tl = Wd('C5', 'read')
    sc.append(Scene(S('C5') - 0.1, tl - 0.1, None, [FS('woolfabric21', 1.0, S('C5') - 0.1, tl)], trans='dissolve', name='knits'))
    sc.append(Scene(tl - 0.1, S('C6') - 0.1, 'cream', [
        FR('fabriclabel6', 0.2, tl - 0.1, Wd('C5', 'touch'), hold=1.8),
        FR('fabriclabel7', 13.0, Wd('C5', 'touch'), S('C6'))], trans='dissolve', name='label_touch'))
    sc.append(Scene(S('C6') - 0.1, E('C6') + 0.45, None, [FS('silk40', 2.0, S('C6') - 0.1, E('C6') + 0.5)], trans='dissolve', out_white=0.5, name='quality'))

    # ---------- 4. DENIM ----------
    sc.append(card(4, 'Heavily Distressed Denim', E('C6') + 0.45, E('D1') + 0.45))
    t0 = E('D1') + 0.45; tr = Wd('D2', 'rips')
    sc.append(Scene(t0, tr - 0.1, None, [FS('loafers23', 0.6, t0, tr, hold=3.0)], name='denim_belongs'))
    sc.append(Scene(tr - 0.1, S('D3') - 0.1, 'cream', [FR('rippedjeans41', 0.4, tr - 0.1, S('D3'), crop=(0, 560, 720, 720), speed=0.3)],
                    trans='dissolve', name='ripped'))
    sc.append(Scene(S('D3') - 0.1, S('D4') - 0.1, None, [FS('darkjeans1', 0.6, S('D3') - 0.1, S('D4'))], trans='dissolve', name='intentional'))
    d1, d2, d3 = Wd('D4', 'dark'), Wd('D4', 'straight'), Wd('D4', 'clean')
    sc.append(Scene(S('D4') - 0.1, S('D4b') - 0.1, 'caramel', [
        PN('darkjeans1', 7.3, S('D4') - 0.1, S('D4b'), PANEL3[0], crop=(0, 500, 720, 780)),
        PN('cobalt45', 1.0, d2 - 0.1, S('D4b'), PANEL3[1], crop=(0, 0, 720, 1100)),
        PN('trouserhem33', 0.3, d3 - 0.1, S('D4b'), PANEL3[2], crop=(0, 380, 720, 900), hold=1.5)], trans='dissolve', name='dark_wash'))
    sc.append(split([LM('whiteshirt17', 1.8, S('D4b') - 0.1, S('D5'))], 'caramel',
                    [('Dark denim looks dressier,', 'serif', 54, S('D4b')),
                     ('and pairs with almost everything.', 'script', 84, Wd('D4b', 'pairs') - 0.2)], S('D4b') - 0.1, S('D5') - 0.1, trans='dissolve'))
    tk = Wd('D5', 'knit')
    sc.append(Scene(S('D5') - 0.1, tk - 0.1, None, [FS('whiteshirt19', 0.5, S('D5') - 0.1, tk)], trans='dissolve', name='coat_jeans'))
    tx = Wd('D5', 'suddenly')
    sc.append(Scene(tk - 0.1, tx - 0.1, None, [FS('loafers20', 0.5, tk - 0.1, tx)], trans='dissolve', name='knit_loafers'))
    sc.append(Scene(tx - 0.1, E('D5') + 0.45, None, [FS('whiteshirt41', 14.0, tx - 0.1, E('D5') + 0.5)], trans='dissolve', out_white=0.5, name='denim_expensive'))

    # ---------- 5. TRENDS ----------
    sc.append(card(5, 'Every Trend at Once', E('D5') + 0.45, E('E1') + 0.45))
    t0 = E('E1') + 0.45
    items = ['PUFF SLEEVE', 'BOLD PRINT', 'PLATFORM SHOES', 'STATEMENT BAG']
    tms = [Wd('E2', 'puff'), Wd('E2', 'bold'), Wd('E2', 'platform'), Wd('E2', 'statement')]
    sc.append(words_card(items, tms, t0, Wd('E2', 'together') - 0.1))
    sc[-1].trans = 'cut'
    sc.append(Scene(Wd('E2', 'together') - 0.1, S('E3') - 0.1, 'cream', [
        Text('They compete.', 'script', 120, INK, W / 2, 440, Wd('E2', 'compete') - 0.3, S('E3') - 0.1, wdur=0.7, fout=0.3)], logo=False, trans='cut', name='compete'))
    sc.append(Scene(S('E3') - 0.1, S('E4') - 0.1, None, [FS('posture18', 0.2, S('E3') - 0.1, S('E4'), hold=6.5)], trans='dissolve', name='no_chasing'))
    sc.append(split([LM('simpledress9', 6.2, S('E4') - 0.1, S('E5'))], 'caramel',
                    [('Keep one modern piece,', 'serif', 54, S('E4')),
                     ('build the rest from classics.', 'script', 86, Wd('E4', 'build') - 0.2)], S('E4') - 0.1, S('E5') - 0.1, trans='dissolve'))
    sc.append(Scene(S('E5') - 0.1, S('E5b') - 0.1, 'caramel', [
        PN('simpledress30', 1.0, S('E5') - 0.1, S('E5b'), PANEL2[0]),
        PN('slingback14', 0.5, Wd('E5', 'modern') - 0.1, S('E5b'), PANEL2[1])], trans='dissolve', name='one_trend'))
    tl = Wd('E5b', 'only')
    sc.append(Scene(S('E5b') - 0.1, tl - 0.1, None, [FS('simpledress16', 2.5, S('E5b') - 0.1, tl)], trans='dissolve', name='feel_yourself'))
    sc.append(Scene(tl - 0.1, S('E6') - 0.1, None, [FS('simpledress3', 5.5, tl - 0.1, S('E6'))], trans='dissolve', name='let_go'))
    sc.append(Scene(S('E6') - 0.1, E('E6') + 0.45, None, [FS('simpledress40', 0.4, S('E6') - 0.1, E('E6') + 0.5)], trans='dissolve', out_white=0.5, name='five_years'))

    # ---------- 6. COLOUR ----------
    sc.append(card(6, 'Too Many Competing Colours', E('E6') + 0.45, E('F1') + 0.45))
    t0 = E('F1') + 0.45; tst = Wd('F2', 'stunning')
    sc.append(Scene(t0, tst - 0.1, None, [FS('cobalt26', 3.2, t0, tst)], name='colour_beautiful'))
    sc.append(Scene(tst - 0.1, S('F3') - 0.1, None, [FS('colorclash41', 3.0, tst - 0.1, S('F3'))], trans='dissolve', name='colour_stunning'))
    sc.append(white_quote([('The difference is', 'serif', 52, S('F3')),
                           ('harmony.', 'script', 120, Wd('F3', 'harmony') - 0.2)], S('F3') - 0.1, S('F4') - 0.1, trans='dissolve'))
    many = ['D7263D', 'F5A623', '2E86AB', '8FBF3F']
    t4 = [Wd('F4', 'stripes'), Wd('F4', 'florals'), Wd('F4', 'four'), Wd('F4', 'bright')]
    sc.append(swatches(many, ['', '', '', ''], t4, S('F4') - 0.1, S('F5') - 0.1, 'too_many'))
    sc.append(swatches(['1F2A44', 'F1EBDD', 'B98A5E'], ['NAVY', 'CREAM', 'CAMEL'],
                       [S('F5') + 0.6, S('F5') + 1.0, S('F5') + 1.4], S('F5') - 0.1, S('F6') - 0.1, 'three_colours'))
    sc.append(Scene(S('F6') - 0.1, S('F6b') - 0.1, None, [FS('neutralbase18', 2.0, S('F6') - 0.1, S('F6b'))], trans='dissolve', name='calm_base'))
    sc.append(Scene(S('F6b') - 0.1, S('F7') - 0.1, None, [FS('fineknit11', 12.0, S('F6b') - 0.1, S('F7'))], trans='dissolve', name='neutral_frame'))
    sc.append(Scene(S('F7') - 0.1, E('F7') + 0.45, 'caramel', [
        PN('cobalt30', 0.5, S('F7') - 0.1, E('F7') + 0.5, PANEL2[0], hold=3.0),
        PN('floralskirt13', 0.4, Wd('F7', 'floral') - 0.1, E('F7') + 0.5, PANEL2[1])], trans='dissolve', out_white=0.5, name='bold_calm'))

    # ---------- 7. ACCESSORIES ----------
    sc.append(card(7, 'Accessories That Compete', E('F7') + 0.45, E('G1') + 0.45))
    t0 = E('G1') + 0.45
    sc.append(Scene(t0, S('G3') - 0.1, 'caramel', [
        PN('bracelets43', 3.0, t0, S('G3'), PANEL2[0], crop=(0, 0, 720, 1000)),
        PN('bracelets4', 4.0, Wd('G2', 'stacked') - 0.1, S('G3'), PANEL2[1])], trans='cut', name='too_much'))
    sc.append(white_quote([('Accessories are the punctuation', 'serif', 50, S('G3')),
                           ('of an outfit.', 'script', 96, Wd('G3', 'outfit') - 0.3)], S('G3') - 0.1, S('G4') - 0.1, trans='dissolve'))
    tw = Wd('G4', 'watch')
    sc.append(Scene(S('G4') - 0.1, tw - 0.1, 'cream', [FR('goldhoops7', 1.0, S('G4') - 0.1, tw)], trans='dissolve', name='hoops'))
    sc.append(Scene(tw - 0.1, S('G5') - 0.1, None, [FS('watch22', 1.0, tw - 0.1, S('G5'))], trans='dissolve', name='watch'))
    tp, tb2 = Wd('G5', 'belt'), Wd('G5', 'pearls')
    sc.append(Scene(S('G5') - 0.1, S('G6') - 0.1, 'caramel', [
        PN('scarf23', 2.5, S('G5') - 0.1, S('G6'), PANEL3[0]),
        PN('belt19', 0.5, tp - 0.1, S('G6'), PANEL3[1]),
        PN('pearls1', 0.4, tb2 - 0.1, S('G6'), PANEL3[2])], trans='dissolve', name='simple_pieces'))
    tr2 = Wd('G6', 'remove')
    sc.append(Scene(S('G6') - 0.1, tr2 - 0.1, None, [FS('mirror29', 1.5, S('G6') - 0.1, tr2)], trans='dissolve', name='mirror'))
    sc.append(Scene(tr2 - 0.1, E('G6') + 0.45, None, [FS('pearls20', 0.5, tr2 - 0.1, E('G6') + 0.5)], trans='dissolve', out_white=0.5, name='old_rule'))

    # ---------- 8. SHOES ----------
    sc.append(card(8, 'Shoes You Cannot Walk In', E('G6') + 0.45, E('I1') + 0.45))
    t0 = E('I1') + 0.45; tc = Wd('I2', 'carry')
    sc.append(Scene(t0, tc - 0.1, None, [FS('heelswalk26', 0.5, t0, tc, crop=(0, 700, 720, 580), hold=3.6)], name='wobble'))
    sc.append(Scene(tc - 0.1, S('I3') - 0.1, None, [FS('heelswalk38', 0.4, tc - 0.1, S('I3'))], trans='dissolve', name='carry_home'))
    sc.append(split([LM('slingback1', 0.5, S('I3') - 0.1, S('I4'))], 'caramel',
                    [('Elegance is in the way you move.', 'serif', 52, S('I3')),
                     ('It begins with your feet.', 'script', 86, Wd('I3', 'begins') - 0.3)], S('I3') - 0.1, S('I4') - 0.1, trans='dissolve'))
    sc.append(Scene(S('I4') - 0.1, S('I5') - 0.1, None, [FS('heelswalk48', 5.0, S('I4') - 0.1, S('I5'))], trans='dissolve', name='walk_gracefully'))
    f1, f2, f3, f4 = Wd('I5', 'loafers'), Wd('I5', 'ballet'), Wd('I5', 'block'), Wd('I5', 'slingback')
    sc.append(Scene(S('I5') - 0.1, S('I5b') - 0.1, 'caramel', [
        Clip('m_shoetree26', 10.4, S('I5') - 0.1, S('I5b'), P4[0], 'cover', None, 'top'),
        Clip('m_balletflats2', 4.0, f2 - 0.1, S('I5b'), P4[1], 'cover', (0, 600, 720, 680), 'top', hold=4.5),
        Clip('m_blockheel2', 6.0, f3 - 0.1, S('I5b'), P4[2], 'cover', None, 'top'),
        Clip('m_slingback41', 0.5, f4 - 0.1, S('I5b'), P4[3], 'cover', None, 'top')], trans='dissolve', name='good_shoes'))
    sc.append(Scene(S('I5b') - 0.1, S('I7') - 0.1, None, [FS('slingback14', 4.2, S('I5b') - 0.1, S('I7'))], trans='dissolve', name='heel_height'))
    tw2 = Wd('I7', 'walk')
    sc.append(Scene(S('I7') - 0.1, tw2 - 0.1, None, [FS('loafers35', 9.0, S('I7') - 0.1, tw2)], trans='dissolve', name='stand_taller'))
    sc.append(Scene(tw2 - 0.1, E('I7') + 0.6, None, [FS('camelwalk48', 0.5, tw2 - 0.1, E('I7') + 0.6)], trans='dissolve', name='remembered'))

    # ---------- ENDING ----------
    sc.append(white_quote([('None of these things', 'serif', 52, S('Z1')),
                           ('are about money.', 'script', 100, Wd('Z1', 'money') - 0.3)], E('I7') + 0.6, S('Z2') - 0.1, trans='dissolve'))
    sc.append(Scene(S('Z2') - 0.1, S('Z2b') - 0.1, None, [FS('silk40', 20.0, S('Z2') - 0.1, S('Z2b'))], trans='dissolve', name='well_fitted'))
    sc.append(Scene(S('Z2b') - 0.1, S('Z3') - 0.1, None, [FS('simpledress34', 4.4, S('Z2b') - 0.1, S('Z3'), speed=0.35)], trans='dissolve', name='less_better'))
    rec = [('quiet', 'leatherbag23', 9.0), ('fit', 'blazerfit30', 33.0), ('beautiful', 'woolfabric37', 5.2), ('clean', 'darkjeans1', 2.5),
           ('one', 'simpledress30', 0.5), ('calm', 'cobalt30', 0.5), ('simple', 'goldhoops0', 1.0), ('shoes', 'balletflats2', 5.5)]
    times = [S('Z3') - 0.1] + [Wd('Z3', w) - 0.1 for w, _, _ in rec[1:]] + [S('Z4') - 0.1]
    for i, (w, key, tin) in enumerate(rec):
        sc.append(Scene(times[i], times[i + 1], None, [FS(key, tin, times[i], times[i + 1])], trans='dissolve' if i else 'cut', tdur=0.25, name=f'recap_{w}'))
    tcar = Wd('Z4', 'carry')
    sc.append(Scene(S('Z4') - 0.1, tcar - 0.1, None, [FS('posture11', 1.4, S('Z4') - 0.1, tcar)], trans='dissolve', name='not_only_clothes'))
    sc.append(split([LM('pearls20', 7.0, tcar - 0.1, S('Z5'))], 'caramel',
                    [('In how you carry yourself,', 'serif', 52, tcar),
                     ('and how you treat people.', 'script', 86, Wd('Z4', 'treat') - 0.3)], tcar - 0.1, S('Z5') - 0.1, trans='dissolve'))
    sc.append(Scene(S('Z5') - 0.1, S('Z6') - 0.1, None, [FS('silk0', 26.0, S('Z5') - 0.1, S('Z6'))], trans='dissolve', name='comments'))
    sc.append(Scene(S('Z6') - 0.1, E('Z6') + 0.5, None, [FS('camelwalk39', 0.5, S('Z6') - 0.1, E('Z6') + 0.5)], trans='dissolve', name='welcome'))
    sc.append(Scene(E('Z6') + 0.5, DUR, 'black', [UserLogo(E('Z6') + 0.5, DUR, width=470, fin=0.8, fout=0.8)], logo=False, trans='dissolve', tdur=0.8, name='outro'))
    for a, b in zip(sc, sc[1:]):
        assert b.t0 > a.t0, (a.name, b.name)
        a.t1 = b.t0
    return sc

if __name__ == '__main__':
    sc = build()
    for s in sc: print(f'{s.t0:7.2f}-{s.t1:7.2f} {s.t1-s.t0:5.2f} {s.name}')
    print(len(sc), 'scenes; duration', DUR)
