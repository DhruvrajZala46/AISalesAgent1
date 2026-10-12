# 8 Dressing Rules Every Woman Should Know - the edit, beat by beat (the "stage" format).
# Every rule follows the replay study of 79 videos (research/edit-evidence):
#   white number card -> ONE calm centred frame for the whole rule, the pictures change inside it on the exact word
#   (words.json), the same woman goes from the mistake (red cross) to the fix (green tick) where the footage allows,
#   one word-timed row only where the script lists 2-4 things, full-screen only for the hook, the title, the guide and
#   the ending, no quote overlays: text is the rule card, a mark word, or a row label.
# Every segment was checked on the strips (st/*.jpg); no AI clips (aiscan.json: max 0.12).
after = lambda i: en(i) + 0.1        # the first picture of a rule sits under the white card and is revealed as it fades

# ================= HOOK (0-31 s) =================
# 1 "Before you buy one more piece, stop. Which 8 dressing rules make some women look elegant in anything, and why do they cost nothing?"
canvas_full(C('camelwalk14', 0.0, 4.6), 0.0, at(1, 'Which') - 0.1, fin=0.01)
canvas_full(C('camelwalk15', 0.0, 4.0), at(1, 'Which') - 0.1, at(1, 'elegant') + 0.1)
row([C('over60chic14', 8.6, 13.7), C('midivneck39', 2.0, 7.0), C('curvychic44', 3.3, 8.9)],
    [at(1, 'elegant'), at(1, 'anything'), at(1, 'why')], en(1) + 0.4)
# 2 "Some women know quiet rules that nobody ever wrote down, passed on by a mother or a grandmother."
# 3 "If no one passed them on to you, we're passing them on today."
stage([(C('over60chic8', 1.8, 10.2), st(2) - 0.1), (C('mother42', 7.0, 11.8), at(2, 'passed on')),
       (C('mother42', 18.0, 21.2), st(3) - 0.1), (C('over60chic0', 3.0, 9.0), at(3, "we're passing"))], en(3) + 0.35)
# 4 "It isn't money, and it isn't a certain body. Just eight timeless rules, for any age. Let's begin."
pair([C('sleeveless24', 0.0, 6.0), C('curvychic9', 0.0, 6.4)], [st(4) - 0.1, at(4, 'certain body')], at(4, 'Just') - 0.2)
canvas_full(C('camelwalk4', 0.0, 6.6), at(4, 'Just') - 0.2, en(4) + 0.35, fin=0.6)
i = nid('ti'); els.append(f'<div id="{i}" class="title" style="opacity:0"><div class="ep">Episode 11</div><div class="big" style="font-size:88px">8 Dressing Rules Every Woman Should Know</div></div>')
tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:16}},{{opacity:1,y:0,duration:1.1,ease:"power2.out"}},{at(4, "Just") + 0.2:.3f});'); fade_out(i, en(4) + 0.2, 0.45)

# ================= 1. Reveal one, not two =================
card('1. Reveal one, not two', 5)
# 6 "It's easy to put on a lovely dress and feel that something is a little too much, without knowing why."
# 7 "Usually it's simple. When an outfit shows two things at once, the eye doesn't know where to rest, and the look becomes loud instead of graceful."
# 8 "Many of us grew up hearing it at home. If it's revealing on top, cover the bottom. If it's revealing on the bottom, cover the top."
# 9a "So choose one. Instead of a short skirt with a low neckline,"
stage([(C('curvychic43', 0.0, 4.8), after(5)), (C('over60chic28', 4.47, 10.83), at(6, 'something is a little')),
       (C('midivneck16', 0.0, 9.2), st(7) - 0.1), (C('over60chic33', 0.0, 8.0), at(7, 'the eye')),
       (C('mother42', 12.1, 17.4), st(8) - 0.1), (C('sleeveless31', 3.87, 10.6), at(8, "revealing on top")),
       (C('minihigh7', 0.0, 6.6), at(8, 'revealing on the bottom')), (C('curvychic36', 6.5, 13.0), st(9) - 0.1)],
      at(9, 'try') + 0.5)
mark('yes', 'cover the bottom', at(8, 'cover the bottom') - 0.2, at(8, 'revealing on the bottom') - 0.1)
mark('yes', 'cover the top', at(8, 'cover the top') - 0.2, en(8) + 0.3)
mark('yes', 'choose one', st(9), at(9, 'try'))
# 9b "...try a shorter skirt with a high neck and sleeves. Or a soft V-neck with a midi skirt or wide trousers."
row([C('minihigh49', 0.0, 6.8), C('midivneck14', 0.0, 12.0), C('curvychic26', 0.0, 8.1)],
    [at(9, 'try'), at(9, 'soft V-neck'), at(9, 'wide trousers') - 0.3], en(9) + 0.45,
    labels=['high neck, short skirt', 'V-neck, midi skirt', 'V-neck, wide trousers'])
# 10 "And if you love showing your arms, that's beautiful. Just keep the neckline and the length calm."
# 11 "It's not about hiding. It's about letting one thing shine, so you feel graceful and completely at ease all evening."
stage([(C('sleeveless17', 2.3, 13.0), st(10) - 0.15), (C('over60chic2', 5.3, 15.0), at(10, 'keep the neckline')),
       (C('over60chic40', 1.3, 10.8), st(11) - 0.1), (C('over60chic37', 13.89, 18.52), at(11, 'graceful'))], en(11) + 0.75)
mark('yes', 'calm neckline & length', at(10, 'keep the neckline'), en(10) + 0.3)

# ================= 2. Fit first =================
card('2. Fit first', 12)
# 13 "It's tempting to buy a piece because the colour is lovely, or because it was on sale."
# 14 "But fit is what makes clothes look expensive. A simple navy blazer that fits looks more elegant than a beautiful one that doesn't."
# 15 "Fit is what looks expensive, not the label. That's why a classic piece that fits never goes out of style."
# 16 "Look for three things. The shoulder seam sits on your shoulder. The sleeve ends at your wrist bone. And the trouser hem just touches the top of your shoe."
# 17 "If one of them is wrong, take it to a tailor. Shortening a hem or a sleeve often costs less than a new top, and it makes the whole piece look made for you."
#     (the same jeans: too long -> hemmed)
# 18 "And if a tailor isn't in the budget, buy for your shoulders. Almost everything else can be adjusted, but shoulders can't."
# 19 "When your clothes fit, you stop pulling and fixing, and you carry yourself with ease."
stage([(C('fabrictest20', 0.0, 3.93), after(12)), (C('fabrictest20', 7.27, 13.67), at(13, 'colour is lovely')),
       (C('navyblazer4', 0.0, 8.0), st(14) - 0.1), (C('navyblazer1', 5.5, 10.0), at(14, 'navy blazer')),
       (C('navyblazer8', 0.0, 5.0), at(14, 'than a beautiful')),
       (C('navyblazer32', 4.23, 13.2), st(15) - 0.1), (C('navyblazer15', 3.09, 10.1), at(15, 'classic piece')),
       (C('navyblazer12', 4.1, 8.6), st(16) - 0.1), (C('navyblazer26', 0.0, 2.9), at(16, 'shoulder seam')),
       (C('sleevefit12', 9.6, 14.9), at(16, 'The sleeve')), (C('blockheel42', 0.3, 4.4), at(16, 'trouser hem')),
       (C('tailor17', 0.3, 4.6), st(17) - 0.1), (C('tailor4', 1.6, 8.0), at(17, 'take it to a tailor')),
       (C('tailor37', 3.73, 10.0), at(17, 'Shortening')), (C('tailor17', 7.3, 13.0), at(17, 'makes the whole piece')),
       (C('navyblazer12', 0.0, 4.1), st(18) - 0.1), (C('navyblazer5', 0.0, 8.4), at(18, 'Almost')),
       (C('over60chic33', 8.0, 16.0), st(19) - 0.1), (C('over60chic8', 13.83, 17.43), at(19, 'carry yourself'))], en(19) + 0.75)
mark('yes', 'it fits', at(14, 'that fits'), at(14, 'than a beautiful'))
mark('yes', 'shoulder seam', at(16, 'shoulder seam'), at(16, 'The sleeve') - 0.15)
mark('yes', 'wrist bone', at(16, 'The sleeve'), at(16, 'trouser hem') - 0.15)
mark('yes', 'top of the shoe', at(16, 'trouser hem'), en(16) + 0.3)
mark('no', 'too long', st(17) - 0.1, at(17, 'take it to a tailor'))
mark('yes', 'made for you', at(17, 'makes the whole piece'), en(17) + 0.3)
mark('yes', 'buy for your shoulders', at(18, 'buy for your shoulders'), en(18) + 0.3)

# ================= 3. Balance the shape =================
card('3. Balance the shape', 20)
# 21 "Have you ever tried on an outfit you loved on someone else, and on you it just felt wrong?"
# 22 "It's not your body. It's the balance."   (the same woman: everything loose -> one fitted piece)
# 23 "That's because when everything is loose, the body disappears in fabric, and when everything is tight, nothing is left to the imagination. The eye looks for one place where the shape is clear."
# 24a "Elegant women tend to pair one relaxed piece with one fitted piece."
stage([(C('curvychic17', 3.0, 8.87), after(20)), (C('proportion3', 2.3, 6.4), at(21, 'and on you')),
       (C('proportion3', 8.0, 13.0), at(22, 'balance') - 0.3),
       (C('thicktee38', 0.8, 6.1), st(23) - 0.1), (C('proportion40', 0.0, 6.4), at(23, 'when everything is tight')),
       (C('proportion6', 2.3, 11.0), at(23, 'The eye')), (C('proportion27', 2.17, 5.77), at(23, 'shape is clear') - 0.2),
       (C('proportion3', 19.1, 24.3), st(24) - 0.1)], at(24, 'Camel') + 0.5)
mark('no', 'felt wrong', at(21, 'and on you'), at(22, 'balance') - 0.3)
mark('yes', 'the balance', at(22, 'balance') - 0.3, en(22) + 0.3)
mark('no', 'all loose', at(23, 'everything is loose'), at(23, 'when everything is tight'))
mark('yes', 'one clear shape', at(23, 'The eye'), en(23) + 0.3)
mark('yes', 'relaxed + fitted', at(24, 'relaxed piece'), at(24, 'Camel'))
# 24b "Camel wide trousers with a fitted cream knit. Slim black trousers with a soft, relaxed grey sweater or blazer."
row([C('over60chic19', 0.0, 20.0), C('oversized29', 2.5, 11.5), C('blazerfit34', 8.34, 12.64)],
    [at(24, 'Camel'), at(24, 'Slim'), at(24, 'blazer') - 0.4], en(24) + 0.45,
    labels=['wide trousers, fitted top', 'slim trousers, soft sweater', 'or a blazer'])
# 25 "And if you love an oversized look, keep it. Just show one narrow point, your wrists, your ankles or your waist."
# 26a "Tell us in the comments, which do you reach for more often,"
stage([(C('oversized46', 0.0, 9.3), st(25) - 0.15), (C('oversized3', 12.77, 20.5), at(25, 'your wrists')),
       (C('oversized26', 2.0, 9.5), at(25, 'your waist'))], at(26, 'fitted on top') + 0.5)
mark('yes', 'one narrow point', at(25, 'one narrow point'), en(25) + 0.3)
# 26b "...fitted on top, or fitted on the bottom?"
pair([C('proportion27', 10.13, 15.3), C('oversized6', 2.07, 10.4)], [at(26, 'fitted on top'), at(26, 'fitted on the bottom')], en(26) + 0.5,
     labels=['fitted on top', 'fitted on the bottom'])
# 27 "Once the balance is right, the same clothes suddenly look intentional, and you look like yourself."
stage([(C('proportion3', 13.0, 17.6), st(27) - 0.2), (C('curvychic37', 0.3, 8.0), at(27, 'you look like yourself'))], en(27) + 0.75)

# ================= 4. Fabric that holds its shape =================
card('4. Fabric that holds its shape', 28)
# 29 "We've all had a top that looked lovely on the hanger and tired after one hour."
# 30 "Thin, shiny fabrics cling, crease and show every line. Fabrics with a little weight fall smoothly and keep the shape of the cut."
# 31 "The fabric is half the outfit, and it's what makes a classic piece look timeless."
# 32 "Try this in the shop. Squeeze the fabric in your hand for five seconds. If it stays crumpled, it will look crumpled on you. Then hold it up to the light. If you can see through it easily, it will cling."
# 33a "Look for thicker cotton,"
stage([(C('thicktee11', 0.0, 4.6), after(28)), (C('fabrictest11', 18.12, 21.9), at(29, 'tired')),
       (C('fabrictest8', 5.63, 10.0), st(30) - 0.1), (C('fabrictest8', 1.38, 4.34), at(30, 'Fabrics with a little weight')),
       (C('woolcoat33', 0.0, 7.47), at(30, 'keep the shape')),
       (C('fabrictest36', 0.0, 8.0), st(31) - 0.1), (C('woolcoat7', 0.0, 6.8), at(31, 'classic piece')),
       (C('fabrictest9', 0.0, 7.0), st(32) - 0.1), (C('thicktee11', 4.6, 7.4), at(32, 'Squeeze')),
       (C('fabrictest27', 4.3, 8.9), at(32, 'If it stays crumpled')),
       (C('fabriclight8', 3.3, 6.3), at(32, 'hold it up to the light')), (C('fabriclight8', 6.3, 9.43), at(32, 'If you can see through') - 0.3),
       (C('fabriclight45', 0.0, 8.7), at(32, 'it will cling'))],
      at(33, 'thicker cotton') + 0.5)
mark('yes', 'a little weight', at(30, 'Fabrics with a little weight'), at(30, 'keep the shape'))
mark('yes', 'the squeeze test', at(32, 'Squeeze'), at(32, 'hold it up to the light'))
mark('yes', 'the light test', at(32, 'hold it up to the light'), at(32, 'If you can see through') - 0.3)
mark('no', 'see-through', at(32, 'If you can see through') - 0.3, en(32) + 0.3)
# 33b "...wool, linen and silk, ..."
row([C('thicktee37', 0.0, 12.0), C('fabrictest36', 8.5, 21.0), C('fabrictest11', 4.42, 14.25), C('midivneck9', 3.3, 12.4)],
    [at(33, 'thicker cotton'), at(33, 'wool'), at(33, 'linen'), at(33, 'silk')], at(33, 'You may') - 0.1,
    labels=['cotton', 'wool', 'linen', 'silk'])
# 33c "You may already own a few, and many are easy to find second hand."
# 34 "Even swapping one pair of soft, stretchy trousers for a pair with a little structure can change how put together you look."
# 35 "Good fabric quietly takes care of you all day, and you feel polished from morning to evening."
stage([(C('navyblazer30', 1.3, 8.6), at(33, 'You may') - 0.2), (C('fabrictest44', 1.33, 9.0), st(34) - 0.1),
       (C('proportion27', 5.77, 10.13), at(34, 'a pair with a little structure')), (C('woolcoat32', 0.0, 5.5), st(35) - 0.1),
       (C('woolcoat22', 0.0, 7.7), at(35, 'polished'))], en(35) + 0.3)
mark('yes', 'a little structure', at(34, 'a pair with a little structure'), en(34) + 0.3)
# 36 guide plug, 9 s, at the END of the rule, the next number card right after it
canvas_full(C('fabriclight16', 1.0, 7.6), st(36) - 0.2, at(36, 'our personal stylist') + 0.2, fin=0.5)
canvas_full(C('woolcoat46', 0.0, 8.6), at(36, 'our personal stylist') + 0.2, en(36) + 0.6, fin=0.5)
i = nid('hz'); els.append(f'<div id="{i}" class="haze" style="opacity:0"></div>'); fade_in(i, at(36, 'our personal stylist'), 0.8); fade_out(i, en(36) + 0.6, 0.5)
text('Check the description for', 'gtx1', at(36, 'our personal stylist') + 0.5, en(36) + 0.55, dur=1.1)
text('Personal stylist guide', 'gtx2', at(36, 'our personal stylist') + 0.9, en(36) + 0.55, dur=1.6)

# ================= 5. What's underneath stays invisible =================
card("5. What's underneath stays invisible", 37, style='font-size:96px')
# 38 "It's such a small thing, and it's easy to miss in a rush."
# 39 "But a visible strap or line pulls the eye away from everything else you chose so carefully."
# 40 "And here's the one that surprises most women. Under white, wear a shade close to your skin instead of white, or even a soft red. It disappears."
#     (the same two women: a dark bra shows under white, the red one disappears)
# 41 "Check your bra from the side. No overflow at the top, no folds under the arms, and the straps stay hidden."
# 42 "For trousers and fitted skirts, choose smooth underwear, ideally in cotton. And if seamless styles feel too warm, a soft cotton one in your skin tone works just as well."
# 43 "When nothing underneath shows, everything you wear on top looks cleaner, and you move through the day with complete ease."
stage([(C('oversized3', 0.0, 5.8), after(37)),
       (C('whitebra12', 0.0, 3.0), st(39) - 0.1), (C('over60chic0', 12.0, 18.0), at(39, 'pulls')),
       (C('whitebra0', 3.0, 11.0), st(40) - 0.1), (C('whitebra12', 3.0, 6.6), at(40, 'or even a soft red')),
       (C('brafit15', 0.1, 9.9), st(41) - 0.1),
       (C('over60chic19', 27.5, 31.2), st(42) - 0.1), (C('midivneck14', 12.9, 17.0), at(42, 'fitted skirts')),
       (C('thicktee17', 0.0, 7.0), at(42, 'ideally in cotton')), (C('whitebra0', 13.7, 21.7), at(42, 'And if seamless')),
       (C('over60chic0', 20.0, 27.0), st(43) - 0.1), (C('camelwalk12', 0.0, 3.3), at(43, 'you move'))], en(43) + 0.75)
mark('no', 'a visible line', at(39, 'visible strap'), at(39, 'pulls'))
mark('yes', 'skin tone', at(40, 'a shade close'), at(40, 'or even a soft red'))
mark('yes', 'or soft red', at(40, 'or even a soft red'), en(40) + 0.3)
mark('yes', 'check from the side', st(41), en(41) + 0.3)
mark('yes', 'smooth, cotton', at(42, 'choose smooth'), at(42, 'And if seamless'))

# ================= 6. One star per outfit =================
card('6. One star per outfit', 44)
# 45 "Colour is wonderful, and a bold print can be beautiful. There's nothing wrong with either."
stage([(C('redcoat2', 9.1, 16.0), after(44)), (C('printskirt11', 0.0, 10.0), at(45, 'a bold print'))], at(46, 'the print') + 0.5)
# 46 "But when the print, the colour, the shine and the jewellery all speak at once, they compete, and none of them gets to shine."
#     (the screen fills up, one by one: that is what "competing" looks like)
row([C('printskirt42', 0.0, 6.0), C('redcoat24', 3.3, 9.5), C('earrings0', 0.0, 7.0), C('earrings25', 9.0, 15.0)],
    [at(46, 'the print'), at(46, 'the colour'), at(46, 'the shine'), at(46, 'jewellery')], en(46) - 0.15)
# 47 "Let one piece be the star, and let everything else support it."   (busy row -> one calm frame)
# 48 "A red coat over camel, cream and grey. A printed skirt with a plain navy knit. Bold earrings with a simple black dress, and no necklace."
# 49 "So if you love colour, wear it. Just let it be the star."
# 50 "One clear star makes the whole outfit look intentional, and it lets your personality shine through with confidence."
stage([(C('redcoat2', 16.2, 25.0), st(47) - 0.2), (C('redcoat0', 0.0, 7.0), st(48) - 0.1),
       (C('printskirt1', 0.0, 12.0), at(48, 'A printed skirt')), (C('earrings12', 1.3, 12.7), at(48, 'Bold earrings')),
       (C('redcoat19', 2.8, 9.7), st(49) - 0.1), (C('printskirt3', 0.0, 13.0), st(50) - 0.1),
       (C('over60chic37', 18.52, 24.94), at(50, 'personality'))], en(50) + 0.75)
mark('yes', 'one star', st(47), en(47) + 0.3)
mark('yes', 'red coat', at(48, 'red coat'), at(48, 'A printed skirt') - 0.1)
mark('yes', 'printed skirt', at(48, 'A printed skirt'), at(48, 'Bold earrings') - 0.1)
mark('yes', 'bold earrings', at(48, 'Bold earrings'), en(48) + 0.3)

# ================= 7. Shoes first =================
card('7. Spend on your shoes first', 51)
# 52 "It's easy to spend on the top everyone sees and forget the feet."
# 53 "People notice shoes more than we think, because they finish the whole outfit. Worn or shiny plastic shoes can quietly cheapen a lovely look, while one good pair lifts even jeans and a tee."
# 54 "If your budget is small, put it into your shoes first."
# 55a "Instead of three cheap pairs, choose one good pair in your base colour, black, camel or chocolate brown, in real leather or suede, with a comfortable sole."
stage([(C('flats7', 4.17, 8.93), after(51)), (C('loafers24', 6.23, 9.0), at(52, 'the feet') - 0.3),
       (C('loafers3', 8.94, 14.9), st(53) - 0.1), (C('flats22', 0.0, 1.97), at(53, 'finish the whole outfit')),
       (C('loafers18', 0.0, 6.0), at(53, 'Worn or shiny')), (C('loafers0', 1.4, 9.7), at(53, 'one good pair')),
       (C('loafers18', 6.4, 12.0), st(54) - 0.1),
       (C('loafers3', 2.42, 8.9), st(55) - 0.1), (C('loafers24', 0.0, 5.47), at(55, 'chocolate brown')),
       (C('flats22', 1.97, 5.3), at(55, 'real leather or suede')), (C('loafers22', 9.7, 11.87), at(55, 'comfortable sole'))],
      at(55, 'Loafers') + 0.5)
mark('yes', 'one good pair', at(53, 'one good pair'), en(53) + 0.3)
mark('yes', 'shoes first', st(54), en(54) + 0.3)
mark('yes', 'leather or suede', at(55, 'real leather or suede'), at(55, 'Loafers'))
# 55b "Loafers, ballet flats, or a low block heel."  (the row stays into 56a)
row([C('loafers12', 0.0, 5.97), C('flats43', 0.0, 4.12), C('blockheel3', 0.0, 10.0)],
    [at(55, 'Loafers'), at(55, 'ballet flats'), at(55, 'low block heel')], at(56, 'choose comfort') - 0.1,
    labels=['loafers', 'ballet flats', 'low block heel'])
# 56b "...choose comfort, always. Elegant flats are just as graceful, and pain is never elegant."
# 57 "Good shoes carry you with confidence, wherever the day goes."
stage([(C('flats43', 4.12, 7.4), at(56, 'choose comfort') - 0.3), (C('flats7', 0.3, 4.17), at(56, 'Elegant flats')),
       (C('flats7', 8.93, 13.6), at(56, 'pain is never')), (C('blockheel3', 10.0, 20.0), st(57) - 0.1)], en(57) + 0.75)
mark('yes', 'comfort, always', at(56, 'choose comfort'), en(56) + 0.3)

# ================= 8. Hands that look cared for =================
card('8. Hands that look cared for', 58)
# 59 "Your hands are in every handshake, every cup of coffee, every photo."
# 60 "Chipped polish or very long nails pull the eye, and they can make the most elegant outfit feel a little unfinished."
# 61 "Short, clean and softly shaped is classic, and always elegant."
stage([(C('coffeehands0', 0.0, 2.6), after(58)), (C('coffeehands23', 0.0, 7.7), at(59, 'every cup')),
       (C('coffeehands6', 0.0, 8.0), st(60) - 0.1), (C('earrings25', 3.0, 9.0), at(60, 'the most elegant outfit')),
       (C('nails45', 0.0, 8.8), st(61) - 0.1)], at(62, 'soft oval') + 0.5)
mark('yes', 'short, clean, soft', st(61), en(61) + 0.3)
# 62a "Try a soft oval shape, a sheer nude, a pale pink, or simply clean and buffed."
row([C('nails15', 14.2, 20.5), C('nudepolish25', 1.9, 10.8), C('nudepolish4', 2.0, 9.0), C('nails0', 0.0, 6.9)],
    [at(62, 'soft oval'), at(62, 'sheer nude'), at(62, 'pale pink'), at(62, 'clean and buffed')], at(62, 'Keep hand cream') - 0.1,
    labels=['soft oval', 'sheer nude', 'pale pink', 'clean, buffed'])
# 62b "Keep hand cream by the sink, and remove polish the moment it chips."
# 63 "And if you love longer nails, keep them. Just choose a soft shape and a quiet colour."
# 64 "Cared-for hands show that you take care of yourself, and that is quietly elegant."
stage([(C('handcream9', 0.0, 7.8), at(62, 'Keep hand cream') - 0.2), (C('nudepolish36', 0.0, 8.0), st(63) - 0.1),
       (C('handcream17', 0.0, 6.0), st(64) - 0.1), (C('coffeehands48', 0.0, 6.0), at(64, 'quietly elegant'))], en(64) + 0.45)
mark('yes', 'hand cream', at(62, 'Keep hand cream'), en(62) + 0.3)
mark('yes', 'soft shape, quiet colour', at(63, 'soft shape'), en(63) + 0.3)

# ================= recap 65-73: the women come back as their rule is named, a checklist builds =================
white(en(64) + 0.35, st(65) + 0.5)
stage([(C('midivneck14', 18.0, 22.0), st(65) - 0.1), (C('blazerfit3', 8.3, 11.2), st(67) - 0.1),
       (C('proportion3', 36.56, 40.0), st(68) - 0.1), (C('woolcoat46', 8.6, 14.8), st(69) - 0.1),
       (C('over60chic0', 28.0, 35.0), st(70) - 0.1), (C('redcoat0', 7.0, 15.0), st(71) - 0.1),
       (C('loafers24', 9.0, 13.5), st(72) - 0.1), (C('nails7', 0.0, 5.3), st(73) - 0.1)], en(73) + 0.6, x0=250)
items = ['reveal one, not two', 'fit first', 'balance the shape', 'fabric that holds its shape',
         "what's underneath stays invisible", 'one star per outfit', 'shoes first', 'hands that look cared for']
for k, txt in enumerate(items):
    tt = st(66 + k) - 0.1; i = nid('ck')
    els.append(f'<div id="{i}" class="chk" style="top:{118 + k*104}px;opacity:0"><svg viewBox="0 0 54 54"><path id="{i}p" d="M12 28 L23 39 L42 15"/></svg>{txt}</div>')
    tw.append(f'tl.fromTo("#{i}",{{opacity:0,x:-24}},{{opacity:1,x:0,duration:0.7,ease:"power2.out"}},{tt:.3f});')
    tw.append(f'tl.to("#{i}p",{{strokeDashoffset:0,duration:0.5,ease:"power2.out"}},{tt+0.3:.3f});')
    fade_out(i, en(73) + 0.6, 0.6)

# ================= close =================
# 74 "None of them need money, a certain age or a certain body. Elegance was never about that. It's a few small, timeless rules, passed from woman to woman."
row([C('over60chic23', 0.0, 12.0), C('over60chic37', 0.3, 13.0), C('curvychic17', 8.87, 20.0)],
    [st(74) - 0.1, at(74, 'a certain age'), at(74, 'a certain body')], at(74, "It's a few") - 0.1,
    labels=['not money', 'any age', 'any body'])
# 75 "Which rule did the women in your family teach you? Tell us in the comments. We'd love to learn it, and if you'd like a part two, let us know."
stage([(C('mother40', 32.53, 38.3), at(74, "It's a few") - 0.3), (C('over60chic4', 0.0, 10.0), st(75) - 0.1),
       (C('over60chic8', 17.43, 22.6), at(75, "We'd love"))], en(75) + 0.3)
# 76 "A simple like or comment would mean so much to us. Until next time, bye everyone."
canvas_full(C('camelwalk0', 0.0, 4.8), st(76) - 0.2, at(76, 'Until next time'), fin=0.7)
canvas_full(C('woolcoat36', 0.0, 7.9), at(76, 'Until next time'), total - 2.6, fin=0.6)
