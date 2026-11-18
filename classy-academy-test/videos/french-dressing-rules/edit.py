# 7 French Dressing Rules Everyone Should Learn Once & For All - the edit, beat by beat ("stage" format, the gold standard).
# white number card -> one calm centred frame per rule, pictures change inside it on the exact word, marks beside it,
# a word-timed row only where the script lists things, full-screen only for the hook, the guide and the ending.
after = lambda i: en(i) + 0.1
CROP.update({'jeanstry47': (118, 420, 860), 'jeanstry44': (157, 560, 720), 'jeanstry38': (118, 0, 860), 'stretchjeans40': (34, 120, 1160),
             'floralrail27': (107, 0, 900), 'blackturtle18': (50, 0, 1100), 'whitecollar34': (56, 200, 1080), 'neutralout27': (60, 140, 1060),
             'scarftie8': (98, 0, 930), 'scarfcoat17': (50, 180, 1100), 'scarftie43': (107, 0, 900), 'scarftie46': (118, 0, 860),
             'socksloafers24': (79, 0, 1000), 'curvychic14': (45, 160, 1120), 'navysweater7': (67, 0, 1040)})

# ================= HOOK =================
canvas_full(C('parisjeans2', 0.2, 6.9), 0.0, at(1, 'Which') - 0.1, fin=0.01)
canvas_full(C('parisjeans17', 0.3, 7.0), at(1, 'Which') - 0.1, en(1) + 0.3)
row([C('stripesover8', 3.0, 10.0), C('navysweater25', 0.3, 4.6), C('curvychic14', 0.3, 8.0)],
    [st(2) - 0.1, at(2, 'or a trip'), at(2, "It isn't")], en(2) + 0.35)
stage([(C('mothermirror11', 0.3, 6.0), st(3) - 0.1), (C('mothermirror11', 9.0, 14.5), at(3, 'the kind'))], en(3) + 0.35)
canvas_full(C('curvychic14', 8.3, 12.3), st(4) - 0.2, en(4) + 0.35, fin=0.6)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="big" style="font-size:84px">7 French Dressing Rules Everyone Should Learn</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.0,ease:"power2.out"}},{st(4) + 0.2:.3f});'); fade_out(i, en(4) + 0.2, 0.45)

# ================= 1. Jeans that hold their shape =================
card('1. Jeans that hold their shape', 5)
stage([(C('jeanstry38', 0.3, 5.5), after(5)), (C('stretchjeans26', 1.7, 7.4), at(6, 'softest')),
       (C('jeanstry24', 2.3, 6.2), st(7) - 0.1), (C('jeanstry47', 0.3, 5.0), at(7, "That's the fabric")),
       (C('darkjeans34', 0.3, 8.0), st(8) - 0.1),
       (C('darkjeans6', 0.3, 5.5), st(9) - 0.1), (C('darkjeans0', 7.9, 12.5), at(9, 'A leg')), (C('jeanstry44', 10.8, 14.9), at(9, 'And a fabric')),
       (C('jeanstry38', 27.0, 32.4), st(10) - 0.1), (C('stretchjeans40', 0.3, 9.0), at(10, 'If it stretches')), (C('darkjeans42', 1.9, 3.4), at(10, 'If it barely')),
       (C('fadedjeans2', 1.3, 7.3), st(11) - 0.1), (C('darkjeans1', 1.3, 7.3), at(11, 'Just own')),
       (C('darkjeans0', 13.6, 19.0), st(12) - 0.1), (C('darkjeans13', 0.3, 5.5), at(12, 'With one good pair'))], en(12) + 0.75)
mark('no', 'very stretchy', at(7, 'very stretchy'), at(7, "That's the fabric"))
mark('yes', 'dark', at(9, 'A dark'), at(9, 'A leg') - 0.1)
mark('yes', 'straight', at(9, 'A leg'), at(9, 'And a fabric') - 0.1)
mark('yes', 'firm', at(9, 'And a fabric'), en(9) + 0.3)
mark('yes', 'the pull test', at(10, 'Pinch'), at(10, 'If it stretches') - 0.1)
mark('no', 'stretches a long way', at(10, 'If it stretches'), at(10, 'If it barely') - 0.1)
mark('yes', 'barely moves', at(10, 'If it barely'), en(10) + 0.3)
mark('yes', 'one dark pair', at(11, 'Just own'), en(11) + 0.3)

# ================= 2. Make stripes your print =================
card('2. Make stripes your print', 13)
stage([(C('floralrail27', 1.3, 6.0), after(13)), (C('floralrail48', 0.3, 3.4), at(14, 'and then nothing')),
       (C('breton0', 15.5, 20.5), st(15) - 0.1), (C('breton0', 21.0, 25.0), at(15, 'Because it has')),
       (C('breton17', 0.0, 3.4), st(16) - 0.1), (C('breton2', 6.3, 11.3), at(16, 'The sailor stripe')),
       (C('stripesover38', 0.3, 7.0), st(17) - 0.1), (C('sizeup26', 0.3, 5.0), at(17, 'or black and cream')), (C('sizeup26', 6.3, 9.4), at(17, 'in a thick cotton'))],
      at(18, 'Wear it') + 0.5)
mark('yes', 'two colours, one line', at(15, 'Because it has'), en(15) + 0.3)
mark('yes', 'a true classic', st(16), en(16) + 0.3)
mark('yes', 'thick cotton', at(17, 'in a thick cotton'), en(17) + 0.3)
row([C('stripesover8', 11.0, 19.0), C('stripeblazer0', 16.7, 23.5), C('stripecamel0', 16.3, 21.3), C('stripewhite3', 2.3, 10.0)],
    [at(18, 'Wear it'), at(18, 'Under a navy blazer'), at(18, 'Under a camel coat'), at(18, 'With white trousers')], en(18) + 0.4,
    labels=['dark jeans', 'navy blazer', 'camel coat', 'white trousers'])
pair([C('creamtee20', 8.8, 11.2), C('breton16', 0.3, 4.8)], [st(19) - 0.1, at(19, 'then with the stripes')], en(19) + 0.4, labels=['a plain T-shirt', 'the stripes'])
stage([(C('leopardskirt45', 0.3, 8.0), st(20) - 0.1), (C('leopardskirt45', 10.7, 16.0), at(20, 'Just wear')),
       (C('stripesover37', 0.3, 6.0), st(21) - 0.1), (C('stripecamel14', 12.5, 20.0), at(21, 'and you still'))], en(21) + 0.75)
mark('yes', 'one print at a time', at(20, 'Just wear'), en(20) + 0.3)

# ================= 3. Keep light near your face =================
card('3. Keep light near your face', 22)
stage([(C('blackturtle18', 0.3, 5.3), after(22)), (C('blackturtle33', 9.1, 14.0), at(23, 'It feels safe')),
       (C('creamtee1', 0.3, 5.5), st(24) - 0.1), (C('navysweater8', 0.3, 4.5), at(24, 'A light colour')), (C('blackturtle33', 15.0, 18.5), at(24, 'A very dark')),
       (C('blackturtle33', 18.5, 22.0), st(25) - 0.1),
       (C('navysweater3', 5.7, 12.5), st(26) - 0.1), (C('navysweater10', 0.3, 7.0), at(26, "because it's"))], at(27, 'A white collar') + 0.5)
mark('yes', 'light sends light back', at(24, 'A light colour'), at(24, 'A very dark') - 0.1)
mark('yes', "it's not your face", at(25, "it's not your face"), en(25) + 0.3)
mark('yes', 'navy for black', st(26), en(26) + 0.3)
row([C('whitecollar42', 1.3, 6.5), C('creamtee9', 3.3, 8.0), C('pearlsblack34', 9.7, 13.5)],
    [at(27, 'A white collar'), at(27, 'A cream T-shirt'), at(27, 'A row of pearls')], en(27) + 0.4,
    labels=['a white collar', 'a cream T-shirt', 'a row of pearls'])
stage([(C('pearlsblack34', 0.3, 7.5), st(28) - 0.1),
       (C('creamtee9', 8.3, 14.3), st(29) - 0.1),
       (C('navysweater25', 4.8, 9.3), st(30) - 0.1)], at(31, 'Are you') - 0.1)
mark('yes', 'the window test', st(28), en(28) + 0.3)
mark('yes', 'black, with joy', st(29), en(29) + 0.3)
pair([C('navysweater7', 13.4, 19.0), C('whitecollar34', 0.3, 2.4)], [at(31, 'Are you') - 0.1, at(31, 'or team black')], en(31) + 0.6, labels=['team navy', 'team black'])

# ================= 4. Borrow from the men's side =================
card("4. Borrow from the men's side", 32)
stage([(C('fittedjacket30', 3.0, 11.0), after(32)),
       (C('fittedjacket41', 4.4, 6.4), st(34) - 0.1), (C('mensblazer41', 0.3, 8.0), at(34, "A man's jacket")),
       (C('mensblazer43', 0.2, 4.8), st(35) - 0.1)], at(36, 'Try a classic') + 0.5)
mark('yes', 'falls straight', at(34, 'falls straight'), en(34) + 0.3)
row([C('over70style24', 0.3, 8.0), C('mensblazer16', 6.3, 11.6), C('sizeup27', 4.2, 9.5)],
    [at(36, 'Try a classic'), at(36, 'A navy blazer'), at(36, 'A fine wool')], en(36) + 0.4,
    labels=["a men's shirt", 'a navy blazer', 'a sweater, one size up'])
stage([(C('mensblazer23', 0.3, 8.3), st(37) - 0.1), (C('mensblazer22', 0.3, 5.5), at(37, "And they're"))], at(38, 'Small earrings') + 0.4)
mark('yes', 'seam on your shoulder', at(37, 'If the seam'), at(37, "And they're") - 0.1)
mark('yes', 'second hand', at(37, "And they're"), en(37) + 0.3)
row([C('curvychic9', 5.5, 7.6), C('highlow18', 10.7, 16.0), C('crosslegs19', 8.8, 11.2)],
    [at(38, 'Small earrings'), at(38, 'a silk blouse'), at(38, 'ballet flats') - 0.3], en(38) + 0.4,
    labels=['small earrings', 'a silk blouse', 'ballet flats'])
stage([(C('fittedjacket30', 13.7, 19.0), st(39) - 0.1), (C('menswatch20', 6.6, 14.5), at(39, 'Borrow just')),
       (C('cafeterrace4', 0.3, 7.4), st(40) - 0.1)], en(40) + 0.3)
mark('yes', 'borrow one thing', at(39, 'Borrow just'), en(39) + 0.3)
canvas_full(C('parismarket1', 4.3, 9.5), st(41) - 0.2, at(41, 'our personal stylist') + 0.2, fin=0.5)
canvas_full(C('parisriver12', 0.3, 8.5), at(41, 'our personal stylist') + 0.2, en(41) + 0.6, fin=0.5)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, at(41, 'our personal stylist'), 0.8); fade_out(i, en(41) + 0.6, 0.5)
text('Check the description for', 'gtx1', at(41, 'our personal stylist') + 0.5, en(41) + 0.55, dur=1.1)
text('Personal stylist guide', 'gtx2', at(41, 'our personal stylist') + 0.9, en(41) + 0.55, dur=1.6)

# ================= 5. One dressy, one casual =================
card('5. One dressy, one casual', 42)
stage([(C('eveningdress3', 0.3, 7.0), after(42)), (C('fadedjeans13', 2.3, 8.5), at(43, 'And on an ordinary')),
       (C('eveningdress14', 1.7, 8.0), st(44) - 0.1), (C('fadedjeans10', 0.3, 4.8), at(44, 'All casual')),
       (C('highlow1', 2.5, 7.8), st(45) - 0.1)], at(46, 'A silk blouse') + 0.5)
mark('no', 'all dressed up', st(44), at(44, 'All casual') - 0.1)
mark('no', 'all casual', at(44, 'All casual'), en(44) + 0.2)
mark('yes', 'one up, one down', at(45, 'Dress one thing up'), en(45) + 0.3)
row([C('highlow18', 0.3, 7.0), C('knitsneakers12', 0.3, 9.5), C('tailoredtee1', 1.3, 5.4)],
    [at(46, 'A silk blouse'), at(46, 'A simple knit dress'), at(46, 'Tailored trousers')], en(46) + 0.4,
    labels=['silk blouse + jeans', 'knit dress + sneakers', 'tailored trousers + T-shirt'])
stage([(C('tailoredtee7', 0.3, 3.4), st(47) - 0.1), (C('tailoredtee4', 21.2, 29.5), at(47, 'Which piece')),
       (C('eveningdress37', 0.3, 8.8), st(48) - 0.1),
       (C('parismarket46', 0.3, 9.5), st(49) - 0.1)], en(49) + 0.75)
mark('yes', 'name them both', st(47), en(47) + 0.3)
mark('yes', 'formal? all the way up', st(48), at(48, 'This one'))

# ================= 6. A scarf carries the colour =================
card('6. A scarf carries the colour', 50)
stage([(C('brightcoat1', 4.8, 9.0), after(50)), (C('brightcoat28', 0.3, 6.5), at(51, "And it's easy")),
       (C('redscarf44', 0.3, 7.8), st(52) - 0.1), (C('scarftie7', 10.8, 14.4), at(52, 'and you can change'))], at(53, 'Navy and cream') - 0.1)
mark('yes', 'right by your face', at(52, 'because it sits'), en(52) + 0.3)
row([C('neutralout27', 0.3, 4.2), C('neutralout27', 5.9, 8.3), C('mensblazer13', 3.3, 5.2)],
    [at(53, 'Navy and cream') - 0.1, at(53, 'Grey and white'), at(53, 'Camel and black')], en(53) + 0.4,
    labels=['navy and cream', 'grey and white', 'camel and black'])
stage([(C('scarftie8', 0.3, 4.3), st(54) - 0.1), (C('scarfcoat22', 0.3, 6.0), at(54, 'Red')),
       (C('scarfcoat17', 6.2, 9.0), st(55) - 0.1), (C('redscarf24', 1.6, 5.2), at(55, 'Tuck it')), (C('scarfbag16', 21.0, 28.0), at(55, 'Or tie it')),
       (C('scarftie43', 11.3, 14.6), st(56) - 0.1),
       (C('brightcoat14', 0.3, 6.0), st(57) - 0.1), (C('brightcoat22', 0.3, 5.5), at(57, 'A scarf is simply')),
       (C('scarftie46', 7.3, 10.8), st(58) - 0.1)], en(58) + 0.75)
mark('yes', 'loop it once', st(55), at(55, 'Tuck it') - 0.1)
mark('yes', 'inside a collar', at(55, 'Tuck it'), at(55, 'Or tie it') - 0.1)
mark('yes', 'on your bag', at(55, 'Or tie it'), en(55) + 0.3)
mark('yes', 'the daylight test', st(56), en(56) + 0.3)

# ================= 7. Socks follow the shoes =================
card('7. Socks follow the shoes', 59)
stage([(C('sockdrawer0', 0.3, 9.0), after(59)), (C('sockdrawer14', 0.3, 3.2), at(60, 'We all do it')),
       (C('socksloafers23', 0.3, 4.2), st(61) - 0.1),
       (C('socksloafers24', 3.3, 6.2), st(62) - 0.1), (C('socksloafers2', 4.9, 6.4), at(62, 'and that makes'))], at(63, 'dark shoes') - 0.1)
mark('no', 'a bright line', at(61, 'a bright line'), en(61) + 0.3)
mark('yes', 'one line', at(62, 'in one line'), en(62) + 0.2)
row([C('crosslegs24', 2.3, 4.3), C('whitesocks30', 2.3, 8.0), C('tightsskirt42', 0.3, 6.5)],
    [at(63, 'dark shoes') - 0.1, at(63, 'Light shoes'), at(63, 'And with a skirt')], en(63) + 0.4,
    labels=['dark shoes, dark socks', 'light shoes, light socks', 'black tights, black shoes'])
stage([(C('crosslegs7', 0.3, 3.5), st(64) - 0.1), (C('crosslegs19', 2.3, 7.5), at(64, 'Whatever shows')),
       (C('redsocks37', 0.2, 1.2), st(65) - 0.1), (C('socksloafers43', 0.3, 6.0), at(65, 'Let it be')),
       (C('socksloafers13', 1.3, 10.3), st(66) - 0.1)], en(66) + 0.75)
mark('yes', 'the sit-down test', st(64), en(64) + 0.3)
mark('yes', 'on purpose', at(65, 'on purpose') - 0.3, en(65) + 0.3)

# ================= recap =================
white(en(66) + 0.35, st(67) + 0.5)
stage([(C('darkjeans6', 14.3, 19.0), st(67) - 0.1), (C('stripesover38', 27.0, 31.0), st(69) - 0.1), (C('navysweater10', 8.5, 12.6), st(70) - 0.1),
       (C('mensblazer16', 2.3, 5.3), st(71) - 0.1), (C('highlow1', 10.0, 14.0), st(72) - 0.1), (C('scarfcoat22', 9.7, 14.0), st(73) - 0.1),
       (C('crosslegs24', 4.3, 6.2), st(74) - 0.1)], en(74) + 0.6, x0=250)
items = ['jeans that hold their shape', 'stripes as your print', 'light near your face', "borrow from the men's side",
         'one dressy, one casual', 'a scarf carries the colour', 'socks follow the shoes']
for k, txt in enumerate(items):
    tt = st(68 + k) - 0.1; i = nid('ck')
    els.append(f'<div id="{i}" class="chk" style="top:{150 + k*112}px;opacity:0"><svg viewBox="0 0 54 54"><path id="{i}p" d="M12 28 L23 39 L42 15"/></svg>{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-24}},{{opacity:1,x:0,duration:0.7,ease:"power2.out"}},{tt:.3f});')
    tw.append(f'tl.to("#{i}p",{{strokeDashoffset:0,duration:0.5,ease:"power2.out"}},{tt+0.3:.3f});')
    fade_out(i, en(74) + 0.6, 0.6)

# ================= close =================
row([C('over70style22', 0.3, 9.0), C('curvychic24', 2.3, 9.5), C('over70style16', 2.2, 10.0)],
    [st(75) - 0.1, at(75, 'or thinner'), at(75, 'They work')], at(75, 'It was never') - 0.1,
    labels=['not younger', 'not thinner', 'any age'])
stage([(C('over70style36', 0.3, 8.0), at(75, 'It was never') - 0.3), (C('navysweater3', 13.9, 19.5), st(76) - 0.1),
       (C('breton2', 0.3, 5.5), at(76, "And if you'd like"))], en(76) + 0.3)
canvas_full(C('parisriver28', 0.2, 5.5), st(77) - 0.2, at(77, 'Until next time'), fin=0.7)
canvas_full(C('parisriver3', 0.2, 4.9), at(77, 'Until next time'), total - 2.6, fin=0.6)
