# ===== points 2-7, recap, close. Every clip used once. Rule per line: what must she SEE to learn this?
def card(label, i):
    white(en(i - 1) + 0.5, en(i) + 0.5)
    text(label, 'card', st(i) + 0.1, en(i) + 0.35)
def compare2(a, b, ha, hb, t_a, t_b, t1):
    x0 = (W - 2 * PW2 - 40) // 2
    panel(a, x0, x0 + PW2, t_a, t1, y0=PH0 + 20, y1=PH1 + 20); header(ha, x0 + PW2 // 2, t_a + 0.2, t1)
    panel(b, x0 + PW2 + 40, x0 + 2 * PW2 + 40, t_b, t1, y0=PH0 + 20, y1=PH1 + 20, origin='100% 0%'); header(hb, x0 + PW2 + 40 + PW2 // 2, t_b + 0.2, t1)
def recipe(left, right, items, t_in, t1, size=(200, 420), step=215):
    """Two looks at 85% height with the pieces floating in between, one per spoken item."""
    lt = left if isinstance(left, tuple) else (left, (), t_in); rt = right if isinstance(right, tuple) else (right, (), t_in + 0.3)
    panel(lt[0], 110, 110 + PW2, lt[2], t1, y0=PH0, y1=PH1, swaps=lt[1])
    panel(rt[0], W - 110 - PW2, W - 110, rt[2], t1, y0=PH0, y1=PH1, origin='100% 0%', swaps=rt[1])
    n = len(items); x = W // 2 - (n - 1) * step // 2
    for k, (png, lb, tt) in enumerate(items): cutout(png, x + k * step, 440, size[0], size[1], tt, t1, lb, lbs=38)
def product_between(png, lb, left, right, t0, t1, tp, tr=None):
    """One product centred between two women wearing it (their shoe/sneaker layout)."""
    panel(left, 150, 150 + PW, t0, t1); panel(right, W - 150 - PW, W - 150, tr or t0 + 0.35, t1, origin='100% 0%')
    cutout(png, W // 2, 430, 360, 480, tp, t1, lb)

# ---------------- 2. Pilled, tired knitwear ----------------
card('2. Pilled, tired knitwear', 38)
# 39 "might be beautiful, but covered in fuzz balls..." -> a lovely knit, then the pilling up close
canvas_full('n03.mp4', en(38) + 0.45, en(39) - 2.2)
single('n02.mp4', en(39) - 2.2, en(39) + 0.25, label='pilling')
# 40 "you may not notice, but others do" -> before / after on the same kind of knit
compare2('b40.mp4', 'n08.mp4', 'Uncared for', 'Cared for', st(40) - 0.05, wd(40, 0.45), en(40) + 0.45)
# 41 "Instead, take two minutes with a fabric shaver" -> hint, the shaver itself, then the shaver working
text('instead...', 'hint', st(41), wd(41, 0.25), dur=0.9, out=0.35)
cutout('c_shaver.png', 560, 470, 380, 520, wd(41, 0.25), en(41) + 0.4, 'fabric shaver')
panel('n01.mp4', 1000, 1000 + PW, wd(41, 0.3), en(41) + 0.4, entry='centre')
# 42 fold your knits instead of hanging them
single('n05.mp4', st(42) - 0.05, en(42) + 0.35, label='fold, never hang')
# 43 merino, wool, cashmere blends that hold their shape -> the fibre, close; then the knit that keeps its shape
row(['n06.mp4', 'n07.mp4', 'n09.mp4'], [st(43), wd(43, 0.35), wd(43, 0.62)], en(43) + 0.45, labels=['merino', 'wool', 'cashmere'])
# 44 key line beside a simple, well-kept knit
quote_side('n10.mp4', st(44) - 0.1, en(44) + 0.45, 'A simple, well-kept knit', 'always looks more <i>expensive</i>', wd(44, 0.55))
# 45-48 "The same goes for your winter basics." gloves / scarf / boots
single('n16.mp4', st(45) - 0.05, en(45) + 0.3)
row(['n11.mp4', 'n12.mp4', 'n13.mp4'], [st(46), st(47), st(48)], en(48) + 0.45, labels=['gloves', 'scarf', 'boots'])
# 49 wipe boots when you come home + rest your knits
pair(['n14.mp4', 'n15.mp4'], [st(49) - 0.05, wd(49, 0.5)], en(49) + 0.45)
# 50 closing line
canvas_full('n86.mp4', st(50) - 0.1, en(50) + 0.6)
text('Small moments of care', 'q1', st(50) + 0.4, en(50) + 0.5, dur=1.2, out=0.5)
text('they <i>show</i>', 'q2', wd(50, 0.6), en(50) + 0.5, dur=0.9, out=0.5)

# ---------------- 3. Novelty holiday sweaters ----------------
card('3. Novelty holiday sweaters', 51)
# 52 reindeer sweater -> wear it with joy (show novelty sweaters, lightly)
pair(['n18.mp4', 'n19.mp4'], [en(51) + 0.45, wd(52, 0.45)], en(52) + 0.35)
# 53 let the season show through colour and fabric, not cartoons
compare2('n20.mp4', 'n21.mp4', 'Cartoons', 'Colour & fabric', st(53) - 0.05, wd(53, 0.45), en(53) + 0.45)
# 54-56 burgundy knit / emerald silk blouse / velvet midi skirt: worn on the left, piece joins the lineup
panel('n22.mp4', 150, 150 + PW, st(54) - 0.1, en(56) + 0.5, entry='fade', swaps=[('n23.mp4', st(55)), ('n24.mp4', st(56))])
for k, (png, lb, tt) in enumerate([('c_burg.png', 'burgundy knit', st(54)), ('c_emerald.png', 'emerald silk', st(55)), ('c_vskirt.png', 'velvet midi skirt', st(56))]):
    cutout(png, 1000 + k * 300, 440, 280, 460, tt, en(56) + 0.5, lb)
# 57 colours of the season, rich without a word
row(['n25.mp4', 'n26.mp4', 'n27.mp4'], [st(57) - 0.05, wd(57, 0.3), wd(57, 0.55)], en(57) + 0.45)
# 58 key line
quote_side('n28.mp4', st(58) - 0.1, en(58) + 0.45, "Festive doesn't have to mean loud", 'it just has to feel like <i>you</i>', wd(58, 0.55))
# 59 if you love colour, this is your season
canvas_full('n17.mp4', st(59) - 0.1, en(59) + 0.2)
# 60-63 burgundy / emerald / plum / navy, one panel each in that colour
row(['n29.mp4', 'n30.mp4', 'n31.mp4', 'n32.mp4'], [st(60), st(61), st(62), st(63)], en(63) + 0.45, labels=['burgundy', 'emerald', 'plum', 'navy'])
# 64 joyful and elegant
quote_side('n33.mp4', st(64) - 0.1, en(64) + 0.45, 'Joyful and elegant', 'you can be <i>both</i>', wd(64, 0.6))
# 65-66 the secret: they know which colours flatter them -> colour draping
text('the secret...', 'hint', st(65), wd(65, 0.35), dur=1.0, out=0.4)
pair(['n34.mp4', 'n35.mp4'], [wd(65, 0.4), st(66)], en(66) + 0.45)
# 67 stylist guide, their dreamy overlay
canvas_full('n36.mp4', st(67) - 0.1, st(67) + 4.6, fin=0.8)
canvas_full('a36.mp4', st(67) + 4.6, en(67) + 0.5, fin=0.8)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, st(67), 0.9); fade_out(i, en(67) + 0.5, 0.55)
text('Check the description for', 'gtx1', st(67) + 0.6, en(67) + 0.45, dur=1.1); text('Elegant women style guide', 'gtx2', st(67) + 1.0, en(67) + 0.45, dur=1.7)
sfx('chime', st(67) + 0.6, -24)

# ---------------- 4. The fleece zip-up ----------------
card('4. The fleece zip-up', 68)
# 69-70 in almost every closet; warm and comfortable
canvas_full('n37.mp4', en(68) + 0.45, en(69) + 0.2)
row(['n38.mp4', 'n39.mp4', 'n40.mp4'], [st(70) - 0.05, wd(70, 0.3), wd(70, 0.55)], en(70) + 0.45)
# 71 sporty by nature, makes the outfit look casual -> before / after
compare2('n41.mp4', 'n42.mp4', 'Sporty', 'Polished', st(71) - 0.05, wd(71, 0.5), en(71) + 0.45)
# 72 key line
quote_side('n43.mp4', st(72) - 0.1, en(72) + 0.45, 'Thin layers', 'not <i>thick</i> ones', wd(72, 0.5))
# 73-76 the layering recipe: thermal -> soft knit -> structured coat
text('try this...', 'hint', st(73) - 0.9, st(73) - 0.05, dur=0.7, out=0.3)
recipe(('n44.mp4', [('a44.mp4', st(73) + 4.3)], st(73)), ('n88.mp4', [('a88.mp4', st(73) + 9.2)], st(73) + 0.3), [('c_thermal.png', 'merino thermal', st(73)), ('c_cream.png', 'a soft knit', st(74)), ('c_coat.png', 'a structured coat', st(75))],
       st(73), en(76) + 0.45, size=(200, 420), step=225)
# 77-79 comfort, elegantly: cardigan / long coatigan / quilted jacket
panel('n45.mp4', 0, 641, st(77), en(79) + 0.5, swaps=[('a45.mp4', st(77) + 11.8)]); clabel('cashmere cardigan', 320, H - 120, st(77) + 0.5, en(79) + 0.5)
panel('n46.mp4', 639, 1281, st(78), en(79) + 0.5, swaps=[('a46.mp4', st(78) + 6.25)]); clabel('knit coatigan', 960, H - 120, st(78) + 0.5, en(79) + 0.5)
panel('n47.mp4', 1279, W, max(st(79), en(79) + 0.5 - 6.9), en(79) + 0.5); clabel('quilted jacket', 1600, H - 120, max(st(79), en(79) - 6.8), en(79) + 0.5)

# ---------------- 5. Too much sparkle at once ----------------
card('5. Too much sparkle at once', 80)
canvas_full('n48.mp4', en(80) + 0.45, en(80) + 3.4)
single('a48.mp4', en(80) + 3.4, en(81) + 0.3)
# 82 sequins, glitter heels, statement earrings, metallic bag all at once -> pieces pile up over one busy look
single('n55.mp4', st(82) - 0.05, en(82) + 0.45, x0=200, swaps=[('n56.mp4', st(82) + 6.0)])
for k, (png, tt) in enumerate([('c_sequin.png', wd(82, 0.12)), ('c_heels.png', wd(82, 0.3)), ('c_earring.png', wd(82, 0.5)), ('c_metal.png', wd(82, 0.68))]):
    cutout(png, [1050, 1450, 1050, 1450][k], [290, 290, 700, 700][k], 300, 300, tt, en(82) + 0.45)
# 83 principle
quote_side('n49.mp4', st(83) - 0.1, en(83) + 0.45, 'One moment of <i>sparkle</i>', 'everything else stays calm', wd(83, 0.55))
# 84 satin/velvet dress + simple gold earrings
product_between('c_hoops.png', 'simple gold earrings', 'n51.mp4', 'n52.mp4', st(84) - 0.05, en(84) + 0.45, wd(84, 0.5), tr=en(84) + 0.45 - 2.9)
# 85 sequin skirt + soft cashmere knit
pair(['n53.mp4', 'n89.mp4'], [st(85) - 0.05, wd(85, 0.4)], en(85) + 0.45)
# 86 one focal point
quote_side('n50.mp4', st(86) - 0.1, en(86) + 0.45, 'One focal point', 'everything else <i>quietly</i> supporting it', wd(86, 0.45))
# 87 office party: velvet blazer, silk camisole, tailored trousers, one pair of earrings
canvas_full('f87.mp4', st(87) - 0.1, en(87) - 4.45)
recipe(('n58.mp4', [], en(87) - 4.75), ('a57.mp4', [('a58.mp4', en(87) - 2.35)], en(87) - 4.7), [], st(87), en(87) + 0.45)
for k, (png, lb, tt) in enumerate([('c_navyv.png', 'velvet blazer', max(wd(87, 0.3), en(87) - 4.3)), ('c_ivcami.png', 'silk camisole', max(wd(87, 0.48), en(87) - 3.4)),
                                   ('c_tailor.png', 'tailored trousers', max(wd(87, 0.64), en(87) - 2.5)), ('c_hoops.png', 'one pair of earrings', max(wd(87, 0.82), en(87) - 1.6))]):
    cutout(png, [850, 1070, 850, 1070][k], [250, 250, 640, 640][k], 200, 270, tt, en(87) + 0.45, lb, lbs=34)
# 88 elegance whispers
canvas_full('n59.mp4', st(88) - 0.1, en(88) + 0.4); snow(st(88), en(88) + 0.5, 0.4)
text('True elegance <i>whispers</i>', 'q1', wd(88, 0.45), en(88) + 0.3, dur=1.3, out=0.45)
text('even in December', 'q2', wd(88, 0.72), en(88) + 0.3, dur=0.9, out=0.45)

# ---------------- 6. A coat that fights your outfit ----------------
card('6. A coat that fights your outfit', 89)
canvas_full('n60.mp4', en(89) + 0.45, en(90) + 0.2)
# 91 shorter than your skirt / sleeves past your hands -> drawn diagram
coat_diagram(st(91), en(91) + 0.45)
# 92 longer than your hemline; wool; camel / charcoal / navy / chocolate
text('instead...', 'hint', st(92) - 0.05, wd(92, 0.2), dur=0.8, out=0.35)
row(['a62.mp4', 'n64.mp4', 'n65.mp4', 'n61.mp4'], [wd(92, 0.22), wd(92, 0.55), wd(92, 0.72), wd(92, 0.88)], en(92) + 0.4,
    labels=['camel', 'charcoal', 'navy', 'chocolate'])
# 93 belted
single('n67.mp4', st(93) - 0.05, en(93) + 0.35, label='belted')
# 94 the tailor
quote_side('n68.mp4', st(94) - 0.1, en(94) + 0.45, 'A simple sleeve adjustment', 'changes <i>everything</i>', wd(94, 0.55))
# 95 key line
quote_side('n63.mp4', st(95) - 0.1, en(95) + 0.45, 'Not many coats', 'one that <i>fits</i>', wd(95, 0.5))
# 96-98 scarf / gloves / boots: product between two women
panel('n70.mp4', 150, 150 + PW, st(96) - 0.05, en(98) + 0.5, swaps=[('n66.mp4', st(98))])
for k, (png, lb, tt) in enumerate([('c_scarf.png', 'cashmere scarf', wd(96, 0.5)), ('c_bgloves.png', 'leather gloves', st(97)), ('c_boots.png', 'knee-high boots', st(98))]):
    cutout(png, 1000 + k * 300, 440, 270, 460, tt, en(98) + 0.5, lb)
# 99 every cold morning and evening out
canvas_full('n72.mp4', st(99) - 0.1, en(99) + 0.3)

# ---------------- 7. An overpowering winter scent ----------------
card('7. An overpowering winter scent', 100)
canvas_full('n73.mp4', en(100) + 0.45, en(101) + 0.2)
# 102 heated rooms, crowded parties
x_ = (W - 2 * PW - 14) // 2
panel('n76.mp4', x_, x_ + PW, st(102) - 0.05, en(102) + 0.45, swaps=[('a76.mp4', st(102) + 5.0)])
panel('n77.mp4', x_ + PW + 14, x_ + 2 * PW + 14, max(wd(102, 0.45), en(102) + 0.45 - 5.6), en(102) + 0.45)
# 103 discovered, not announced
quote_side('n84.mp4', st(103) - 0.1, en(103) + 0.45, 'Let your scent be <i>discovered</i>', 'not announced', wd(103, 0.6))
# 104 one or two sprays
single('n78.mp4', st(104) - 0.05, en(104) + 0.35, label='one or two sprays')
# 105 vanilla, amber, sandalwood
panel('n79.mp4', 150, 150 + PW, st(105) - 0.05, en(105) + 0.45, entry='fade', swaps=[('n74.mp4', st(105) + 4.6)])
for k, (png, lb, tt) in enumerate([('c_vanilla.png', 'vanilla', wd(105, 0.3)), ('c_amber.png', 'amber', wd(105, 0.42)), ('c_sandal.png', 'sandalwood', wd(105, 0.55))]):
    cutout(png, 1000 + k * 300, 450, 270, 300, tt, en(105) + 0.45, lb)
# 106 walk into a room
canvas_full('n80.mp4', st(106) - 0.1, en(106) + 0.3)
# 107-110 lips / hands / hair
canvas_full('f107.mp4', st(107) - 0.1, en(107) - 1.95)
single('n81.mp4', en(107) - 2.25, en(107) + 0.4, label='lips')
x_ = (W - 2 * PW - 14) // 2
panel('n82.mp4', x_, x_ + PW, st(108) + 0.4, en(110) + 0.45, label='hands')
panel('n83.mp4', x_ + PW + 14, x_ + 2 * PW + 14, en(110) + 1.0 - 8.1, en(110) + 0.45, label='hair', swaps=[('a83.mp4', en(110) + 1.0 - 3.95)])

# ---------------- recap 111-118 ----------------
white(en(110) + 0.5, en(110) + 1.4)
panel('n85.mp4', 170, 170 + PW, en(110) + 1.1, en(117) + 0.5, entry='fade',
      swaps=[('n87.mp4', st(113)), ('n90.mp4', st(115)), ('n91.mp4', st(117))])
items = ['give black some texture', 'care for your knits', 'let colour be your festive touch', 'trade fleece for thin layers',
         'choose one moment of sparkle', 'find a coat that fits', 'keep your scent soft']
for k, (txt, tt) in enumerate(zip(items, [st(j) for j in range(111, 118)])):
    i = nid('ck'); els.append(f'<div id="{i}" class="chk" style="top:{180 + k*108}px;opacity:0"><svg viewBox="0 0 54 54"><path id="{i}p" d="M10 28 L22 40 L44 14"/></svg>{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-24}},{{opacity:1,x:0,duration:0.7,ease:"power2.out"}},{tt:.3f});')
    tw.append(f'tl.to("#{i}p",{{strokeDashoffset:0,duration:0.5,ease:"power2.out"}},{tt+0.3:.3f});')
    fade_out(i, en(117) + 0.5, 0.6); sfx('click-soft', tt + 0.3, -20)
canvas_full('n92.mp4', st(118) - 0.1, en(118) + 0.2)
# ---------------- close ----------------
x_ = (W - 2 * PW - 14) // 2
panel('n93.mp4', x_, x_ + PW, st(119) - 0.05, wd(119, 0.62), swaps=[('a93.mp4', st(119) + 2.45)])
panel('n94.mp4', x_ + PW + 14, x_ + 2 * PW + 14, wd(119, 0.35), wd(119, 0.62))
text('Part two?', 'hint', wd(119, 0.65), en(119) + 0.2, dur=0.9, out=0.4)
canvas_full('n95.mp4', st(120) - 0.1, total - 2.6, fin=0.8)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, st(120), 0.9); fade_out(i, total - 2.6, 0.55)
text('Check the description for', 'gtx1', st(120) + 0.8, total - 2.65, dur=1.1); text('Elegant women style guide', 'gtx2', st(120) + 1.2, total - 2.65, dur=1.7)
i = nid('ew'); els.append(f'<div id="{i}" class="endwhite" style="opacity:0"></div>'); fade_in(i, total - 2.8, 0.9)
j = nid('el'); els.append(f'<img id="{j}" class="endlogo" src="assets/logo_ce_dark.png" style="opacity:0">')
tw.append(f'tl.fromTo("#{j}",{{opacity:0,scale:0.96}},{{opacity:1,scale:1,duration:1.3,ease:"power2.out"}},{total-2.2:.3f});')
