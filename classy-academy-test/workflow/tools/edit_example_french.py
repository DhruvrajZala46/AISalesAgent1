# The edit, beat by beat. Every clip was checked frame by frame (see ok.txt); each is used once.
X2 = (W - 2 * PW - 14) // 2

# ================= HOOK =================
# 1 "Before you buy another pair of heels, stop. Which 7 things do elegant French women never wear, and why is number 1 in your closet?"
canvas_full(C('stiletto27', 0, 7.9), 0.0, wd(1, 0.42), fin=0.01)
canvas_full(C('pstreet36', 0, 7.4), wd(1, 0.42), en(1) + 0.3)
# 2 "...a woman in Paris wearing something so simple, a white shirt, jeans and flat shoes, and yet she looks more elegant..."
canvas_full(C('whiteshirt8', 0, 7.3), st(2) - 0.1, wd(2, 0.62))
canvas_full(C('pstreet13', 0, 6.8), wd(2, 0.62), en(2) + 0.3)
# 3 "There's no flashy outfit, no logos, nothing trying too hard. ... isn't accidental. And the secret ... what she knows not to."
pair([C('errands11', 0, 12.3), C('frenchchic0', 0, 5.1)], [st(3), wd(3, 0.2)], wd(3, 0.55))
text('the secret...', 'hint', wd(3, 0.6), wd(3, 0.8), dur=1.0, out=0.4)
canvas_full(C('pstreet15', 0, 3.6), wd(3, 0.8), en(3) + 0.3)
# 4 "Of course, not every French woman dresses the same way. But ... French chic ... at any age, on any budget."
row([C('pcafe16', 0, 15.0), C('jeansknit12', 1.6, 8.0), C('parisold0', 0, 8.1), C('over6011', 0, 7.0)],
    [st(4), wd(4, 0.55), wd(4, 0.72), wd(4, 0.86)], en(4) + 0.35)
# 5 "In today's video, we're revealing seven things ... Some of these may surprise you ... Let's get started."
white(en(4) + 0.45, st(5) + 1.6)
text("in today's video...", 'card', st(5) - 0.05, st(5) + 1.45, dur=1.0, out=0.4)
canvas_full(C('goldenparis5', 0, 5.8), st(5) + 1.5, wd(5, 0.55), fin=0.6)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 9</div><div class="big">7 Things Elegant French Women Never Wear</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.2,ease:"power2.out"}},{st(5)+1.9:.3f});'); fade_out(i, wd(5, 0.55) - 0.1, 0.5)
single(C('trenchwalk24', 0, 13.1), wd(5, 0.56), wd(5, 0.78))
row([C('pstreet20', 0, 7.0), C('pcafe5', 0, 10.6), C('trenchwalk12', 0, 14.1)], [wd(5, 0.78), wd(5, 0.84), wd(5, 0.9)], en(5) + 0.4)

# ================= 1. Heels you can't walk in =================
card("1. Heels you can't walk in", 6)
canvas_full(C('stiletto1', 0, 27.5), en(6) + 0.3, wd(7, 0.55))                                # 7 sky-high heels can feel glamorous
single(C('stilettos32', 0, 3.1), wd(7, 0.55), en(7) + 0.35)                                   # ...beautiful sitting in the closet
# 8 "Paris is a walking city. Cobblestone streets, metro stairs, long walks to the market. ... struggling in your shoes."
row([C('cobble39', 0, 9.4), C('metro13', 0, 5.4), C('market20', 0, 16.7)], [wd(8, 0.12), wd(8, 0.3), wd(8, 0.45)], wd(8, 0.66))
canvas_full(C('heelpain4', 0, 27.5), wd(8, 0.66), en(8) + 0.3)
# 9 Ines favours flats over heels
quote_side(C('parisflats10', 0, 10.2), st(9) - 0.1, en(9) + 0.45, 'Inès de la Fressange', 'favours <i>flats</i> over heels', wd(9, 0.75))
# 10 comfort + structure; when your feet hurt it shows
compare(C('heelpain12', 0, 9.6), C('loafers29', 1.0, 9.2), 'Struggling', 'At ease', st(10) - 0.05, wd(10, 0.45), en(10) + 0.4)
# 11 ballet flats, loafers, kitten heel, block heel
single(C('mflats19', 0, 4.12), st(11) - 0.05, wd(11, 0.29))
row([C('flats214', 0, 6.2), C('loafers37', 0, 5.7), C('kitten23', 0, 9.7), C('blockheel18', 0, 7.0)],
    [wd(11, 0.3), wd(11, 0.42), wd(11, 0.58), wd(11, 0.72)], en(11) + 0.4, labels=['ballet flats', 'loafers', 'kitten heel', 'block heel'])
# 12 "French style isn't against heels ... up to about seven centimetres ... a wider heel feels more classic"
single(C('kitten7', 0, 7.1), st(12) - 0.05, wd(12, 0.58))
text('up to <i>7 cm</i>', 'q1', wd(12, 0.3), wd(12, 0.58), dur=1.1, style='top:880px;font-size:70px')
pair([C('kitten15', 2.5, 9.7), C('blockheel17', 0, 7.0)], [wd(12, 0.6), wd(12, 0.7)], en(12) + 0.4, labels=['thin', 'wider'])
# 13 the opposite: heavy comfort shoes -> elegant comfort
compare(C('chunky44', 0, 16.5), C('walkease21', 0, 8.0), 'Heavy', 'Elegant comfort', st(13), wd(13, 0.5), wd(13, 0.76))
pair([C('camelloafer35', 4.29, 9.0), C('parisflats47', 0, 6.27)], [wd(13, 0.76), wd(13, 0.86)], en(13) + 0.4, labels=['a soft leather loafer', 'a supportive ballet flat'])
# 14 navy ballet flats / camel loafers, you may already own one
pair([C('navyflats1', 0, 10.0), C('camelloafer20', 0, 11.7)], [st(14), wd(14, 0.18)], wd(14, 0.6), labels=['navy ballet flats', 'camel loafers'])
canvas_full(C('navysweater1', 0, 4.7), wd(14, 0.6), en(14) + 0.3)
# 15 walk with ease
canvas_full(C('walkease3', 0, 4.4), st(15) - 0.1, en(15) + 0.45)
text('walk with <i>ease</i>', 'q1', wd(15, 0.45), en(15) + 0.4, dur=1.2)

# ================= 2. Gym clothes as an everyday outfit =================
card('2. Gym clothes as an everyday outfit', 16)
canvas_full(C('leggings13', 0, 14.6), en(16) + 0.3, wd(17, 0.25))
pair([C('yoga18', 0, 15.6), C('sundayhome37', 0, 5.9)], [wd(17, 0.25), wd(17, 0.62)], en(17) + 0.35, labels=['the gym', 'a slow Sunday'])
# 18 most don't wear them out and about ... small effort, even for errands
single(C('market26', 0, 11.5), st(18) - 0.05, wd(18, 0.6))
canvas_full(C('errands10', 0, 4.5), wd(18, 0.6), en(18) + 0.3)
# 19 chosen, not grabbed ... a quiet way of respecting yourself
compare(C('sweats41', 0, 9.0), C('errands27', 0, 12.4), 'Grabbed', 'Chosen', st(19) - 0.05, wd(19, 0.3), wd(19, 0.64))
text('a quiet way of', 'q1', wd(19, 0.68), en(19) + 0.45, dur=1.2); text('<i>respecting yourself</i>', 'q2', wd(19, 0.76), en(19) + 0.45, dur=1.3)
# 20 straight-leg jeans, a soft knit, loafers
row([C('jeansknit0', 0, 6.0), C('jeansknit42', 0, 7.63), C('loafers1', 0, 10.6)], [wd(20, 0.12), wd(20, 0.28), wd(20, 0.42)], en(20) + 0.4,
    labels=['straight-leg jeans', 'a soft knit', 'loafers'])
# 21 matte black leggings + long oatmeal sweater + ankle boots
text('if you love <i>leggings</i>...', 'hint', st(21) - 0.05, wd(21, 0.29), dur=1.0, out=0.4)
pair([C('blackleggings41', 0, 5.0), C('blackleggings16', 0, 5.0)], [wd(21, 0.3), wd(21, 0.6)], en(21) + 0.4)
# 22 from the gym to the café
canvas_full(C('cafesit17', 0, 7.0), st(22) - 0.1, en(22) + 0.45)
text('from the gym to the <i>café</i>', 'q1', wd(22, 0.35), en(22) + 0.4, dur=1.3)

# ================= 3. A perfectly matching outfit =================
card('3. A perfectly matching outfit', 23)
canvas_full(C('matchset1', 0, 22.6), en(23) + 0.3, wd(24, 0.25))
row([C('matchset19', 2.6, 9.0), C('matchbag4', 0, 11.6), C('matchset9', 0, 6.8)], [wd(24, 0.25), wd(24, 0.45), wd(24, 0.68)], en(24) + 0.4,
    labels=['the matching set', 'bag matches shoes', 'all one look'])
quote_side(C('creamblouse0', 0, 21.0), st(25) - 0.1, en(25) + 0.45, 'mix styles,', 'and <i>never</i> coordinate', wd(25, 0.75))
# NOTE: pstreet23 appears twice (two different shots 4.2-6.2 and 6.2-8.23) -> replaced below if a fresh clip is available
canvas_full(C('pstreet1', 0, 9.0), st(26) - 0.1, en(26) + 0.3)
text('harmony, not <i>matching</i>', 'q1', wd(26, 0.2), en(26) + 0.25, dur=1.3)
pair([C('blazerjeans18', 0, 8.4), C('trenchsweater25', 6.47, 10.0)], [st(27) - 0.05, wd(27, 0.62)], en(27) + 0.4,
     labels=['blazer + jeans', 'trench over a sweater'])
canvas_full(C('trenchwalk46', 0, 13.5), st(28) - 0.1, en(28) + 0.45)
text('<i>effortless</i>', 'hint', wd(28, 0.5), en(28) + 0.4, dur=1.0)

# ================= 4. Too much jewellery at once =================
card('4. Too much jewellery at once', 29)
canvas_full(C('stackjewel19', 0, 10.0), en(29) + 0.3, st(30) + 0.2)
row([C('minimaljewel6', 0, 15.0), C('bracelets36', 0, 13.1), C('boldearring8', 0, 5.0), C('stackjewel39', 0, 13.4)],
    [st(30) + 0.2, wd(30, 0.2), wd(30, 0.38), wd(30, 0.55)], en(30) + 0.4, labels=['a necklace', 'a stack of bracelets', 'statement earrings', 'rings on every finger'])
quote_side(C('hoops46', 0, 6.7), st(31) - 0.1, en(31) + 0.45, 'Inès’s second rule:', 'reject <i>bling</i>', wd(31, 0.7))
text('never more than', 'q1', st(32) + 0.2, wd(32, 0.72), dur=1.2); text('<i>three pieces</i>', 'q2', wd(32, 0.3), wd(32, 0.72), dur=1.2)
single(C('boldearring1', 0, 2.58), wd(32, 0.75), en(32) + 0.4, label='a statement piece, alone')
text('True elegance <i>whispers</i>', 'q1', st(33) - 0.05, wd(33, 0.3), dur=1.3); text("it doesn't shout", 'q2', wd(33, 0.14), wd(33, 0.3), dur=1.1)
row([C('hoops29', 0, 10.0), C('watch6', 0, 8.7), C('minimaljewel44', 0, 9.2)], [wd(33, 0.32), wd(33, 0.48), wd(33, 0.6)], en(33) + 0.4,
    labels=['small gold hoops', 'a simple watch', 'one ring'])
pair([C('flats219', 0, 10.2), C('redlip45', 27.53, 41.82)], [st(34) - 0.05, wd(34, 0.62)], en(34) + 0.45, labels=['a white shirt + jeans', 'a red lip'])

# ================= mid-roll: the stylist guide =================
text('the secret...', 'hint', st(35) - 0.05, wd(35, 0.3), dur=1.0, out=0.4)
pair([C('drape35', 0, 7.5), C('drape41', 0, 31.0)], [wd(35, 0.3), wd(35, 0.45)], en(35) + 0.4)
canvas_full(C('dreamy17', 0, 7.4), st(36) - 0.1, en(36) + 0.6, fin=0.8)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, st(36), 0.9); fade_out(i, en(36) + 0.6, 0.55)
text('Check the description for', 'gtx1', st(36) + 0.7, en(36) + 0.55, dur=1.1); text('Elegant women style guide', 'gtx2', st(36) + 1.1, en(36) + 0.55, dur=1.7)

# ================= 5. Clothes that don't fit =================
card("5. Clothes that don't fit", 37)
canvas_full(C('loose25', 0, 29.4), en(37) + 0.3, st(38) + 0.3)
compare(C('baggy32', 0, 10.57), C('tailored12', 0, 13.8), "Doesn't fit", 'Fits perfectly', st(38) + 0.3, wd(38, 0.5), en(38) + 0.4)
row([C('jeansknit14', 0, 12.67), C('steam19', 0, 40.0), C('tailor7', 7.7, 12.8)], [st(39) - 0.05, wd(39, 0.66), wd(39, 0.8)], en(39) + 0.4,
    labels=[None, 'pressed', 'properly tailored'])
pair([C('bodycon35', 0, 9.3), C('trousers5', 0, 9.4)], [st(40), wd(40, 0.35)], wd(40, 0.68), labels=['too tight', 'too loose'])
single(C('tailored18', 0, 6.7), wd(40, 0.68), en(40) + 0.3)
row([C('trousers9', 0, 7.0), C('over6013', 0, 40.0), C('tailored42', 0, 9.04)], [st(41) - 0.05, wd(41, 0.2), wd(41, 0.4)], en(41) + 0.45)
text("It's not about size.", 'q1', wd(41, 0.05), en(41) + 0.4, dur=1.0, style='top:900px;font-size:64px')
row([C('tailor30', 0, 17.0), C('tailor29', 3.2, 22.4), C('sleeve19', 0, 8.03)], [st(42) - 0.05, wd(42, 0.18), wd(42, 0.34)], en(42) + 0.4,
    labels=['a hem', 'a waist', 'sleeves'])
canvas_full(C('myclos27', 0, 10.0), st(43) - 0.1, en(43) + 0.45)

# ================= 6. Shiny, synthetic fabrics =================
card('6. Shiny, synthetic fabrics', 44)
canvas_full(C('polyester27', 0, 12.0), en(44) + 0.3, st(45) + 0.2)
row([C('polyester0', 0, 14.7), C('pvc2', 0, 8.13), C('pill41', 0, 2.96)], [st(45) + 0.2, wd(45, 0.38), wd(45, 0.62)], en(45) + 0.35,
    labels=['polyester blouses', 'plastic-looking leather', 'knits that pill'])
text('no matter their <i>budget</i>', 'hint', st(46) - 0.05, wd(46, 0.21), dur=1.1, out=0.4)
row([C('cotton27', 2.9, 10.8), C('linen4', 1.4, 13.2), C('silk28', 0, 10.0), C('wool24', 0, 5.7), C('cashmere11', 0, 5.8), C('walkease18', 0, 6.4)],
    [wd(46, 0.22), wd(46, 0.3), wd(46, 0.37), wd(46, 0.43), wd(46, 0.49), wd(46, 0.57)], en(46) + 0.4,
    labels=['cotton', 'linen', 'silk', 'wool', 'cashmere', 'leather'])
text("it doesn't have to be <i>expensive</i>", 'hint', st(47) - 0.05, wd(47, 0.24), dur=1.2, out=0.4)
pair([C('shopping36', 0, 20.0), C('shopping1', 0, 26.0)], [wd(47, 0.25), wd(47, 0.6)], en(47) + 0.4, labels=['one good piece', 'only what you need'])
quote_side(C('cashmere19', 0, 26.8), st(48) - 0.1, en(48) + 0.5, "“Don't buy a lot.", 'Buy the <i>good things</i>.”', wd(48, 0.55))
row([C('creamblouse1', 0, 17.8), C('camelcoat1', 1.47, 10.7), C('navysweater11', 0, 19.9)], [st(49) - 0.05, wd(49, 0.17), wd(49, 0.33)], en(49) + 0.4,
    labels=['a cream silk blouse', 'a camel wool coat', 'a navy cashmere sweater'])
canvas_full(C('label5', 0, 11.1), st(50) - 0.1, en(50) + 0.45)

# ================= 7. The same style she wore twenty years ago =================
card('7. The same style she wore twenty years ago', 51)
canvas_full(C('mirror0', 0, 3.3), en(51) + 0.3, st(52) + 0.2)
single(C('over600', 0, 40.1), st(52) + 0.2, en(52) + 0.4)
quote_side(C('over507', 0, 11.0), st(53) - 0.1, en(53) + 0.5, 'never neglect yourself', "don't get <i>stuck</i> in a style", wd(53, 0.45))
row([C('jeans16', 1.1, 6.7), C('scarf9', 0, 10.0), C('mflats44', 1.3, 3.9)], [wd(54, 0.62), wd(54, 0.75), wd(54, 0.88)], en(54) + 0.4,
    labels=['a new cut of jeans', 'a softer colour near your face', 'modern flats'])
canvas_full(C('pstreet30', 0, 9.43), st(54) - 0.1, wd(54, 0.6))
row([C('over5010', 0, 7.1), C('over6031', 1.8, 13.9), C('over7026', 0, 6.6)], [st(55) - 0.05, wd(55, 0.25), wd(55, 0.5)], en(55) + 0.4)
text('Elegance has <i>no age</i>.', 'q1', st(56) - 0.1, en(56) + 1.0, dur=1.2)

# ================= recap 57-64 =================
white(en(56) + 1.15, st(57) + 0.6)
recap_specs = [C('parisflats0', 0, 6.97), C('jeansknit3', 0, 6.0), C('blazerjeans45', 6.5, 9.37), C('minimaljewel28', 0, 8.3),
               C('over605', 0, 6.2), C('silk2', 0, 6.0), C('over6015', 0, 5.5)]
x_ = 170
for k, (s, tt) in enumerate(zip(recap_specs, [st(57) + 0.3] + [st(j) for j in range(59, 65)])):
    te = (st(59 + k) if k < 6 else en(64) + 0.6)
    panel(s, x_, x_ + PW, tt, te, entry='fade')
items = ["heels you can't walk in", 'gym clothes as an outfit', 'a perfectly matching look', 'too much jewellery',
         "clothes that don't fit", 'shiny synthetics', 'a style frozen in time']
for k, (txt, tt) in enumerate(zip(items, [st(j) for j in range(58, 65)])):
    i = nid('ck'); els.append(f'<div id="{i}" class="chk" style="top:{170 + k*108}px;opacity:0"><svg viewBox="0 0 54 54"><path id="{i}p" d="M14 14 L40 40 M40 14 L14 40"/></svg>{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-24}},{{opacity:1,x:0,duration:0.7,ease:"power2.out"}},{tt:.3f});')
    tw.append(f'tl.to("#{i}p",{{strokeDashoffset:0,duration:0.5,ease:"power2.out"}},{tt+0.3:.3f});')
    fade_out(i, en(64) + 0.6, 0.6)
# 65 a blazer, a trench coat, a navy sweater, a little black dress, a perfect pair of jeans
single(C('camelcoat9', 2.07, 12.37), st(65) - 0.05, wd(65, 0.51))
row([C('blazerjeans21', 0, 5.0), C('trenchsweater3', 0, 4.8), C('navysweater9', 0.6, 6.2), C('lbd17', 1.7, 8.9), C('jeans34', 0, 6.0)],
    [wd(65, 0.52), wd(65, 0.6), wd(65, 0.68), wd(65, 0.78), wd(65, 0.88)], en(65) + 0.4,
    labels=['a blazer', 'a trench coat', 'a navy sweater', 'a little black dress', 'perfect jeans'])
quote_side(C('jeans5', 0, 16.1), st(66) - 0.1, en(66) + 0.45, 'Jeans are like <i>salt</i>.', 'They go with everything.', wd(66, 0.5))
canvas_full(C('fold36', 0, 7.3), st(67) - 0.1, en(67) + 0.35)
canvas_full(C('pstreet2', 0, 6.2), st(68) - 0.1, en(68) + 0.35)
text('choosing <i>well</i>', 'hint', wd(68, 0.55), en(68) + 0.3, dur=1.0)
canvas_full(C('mirror36', 0, 4.0), st(69) - 0.1, en(69) + 0.45)
text('with a <i>smile</i>', 'hint', wd(69, 0.6), en(69) + 0.4, dur=1.0)

# ================= close =================
canvas_full(C('coffee1', 0, 5.0), st(70) - 0.1, en(70) + 0.3)
canvas_full(C('cobble42', 0, 11.47), st(71) - 0.1, total - 2.6, fin=0.8)
text('Which will you try <i>first</i>?', 'q1', wd(71, 0.3), total - 2.7, dur=1.3)
