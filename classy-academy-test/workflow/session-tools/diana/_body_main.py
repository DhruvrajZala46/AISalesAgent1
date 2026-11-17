# ================= HOOK =================
cfull([(c('h1a'), 0.0), (c('h1b'), at(1, 'When you get'))], nx(2))
q('Are your clothes saying<br><i>what you want them to say?</i>', at(1, 'are your clothes'), en(1) + 0.3, QC, size=78, cls='over')
lrow([c('h2a'), c('h2b')], [nx(2), at(2, 'to be looked')], at(2, 'Almost no one') - 0.1)
q('Most of us dress<br><i>to be looked at.</i>', nx(2) + 0.3, at(2, 'Almost no one') - 0.2, R3, size=66)
lclip([(c('h2c'), at(2, 'Almost no one') - 0.2)], at(2, "And that's why") - 0.1)
q('Almost no one dresses<br><i>to be close to people.</i>', at(2, 'Almost no one'), at(2, "And that's why") - 0.2, QL, size=70)
cfull([(c('h2d'), at(2, "And that's why") - 0.2)], nx(3))
q('Admired for a second,<br><i>forgotten by dinner.</i>', at(2, 'admired'), en(2) + 0.3, QC, size=80, cls='over')
cfull([(c('h3a'), nx(3)), (c('h3b'), at(3, 'Not because')), (c('h3c'), at(3, 'Because every')), (c('h3d'), at(3, 'You know'))], nx(4))
band('Almost thirty years later,<br><i>people still talk about her clothes.</i>', at(3, 'whose clothes'), at(3, 'Not because') - 0.2, size=58)
band('Not the most expensive.', at(3, 'Not because'), at(3, 'Because every') - 0.2, size=64)
band('<i>Every outfit said something.</i>', at(3, 'Because every'), at(3, 'You know') - 0.2, size=84)
cfull([(c('h4a'), nx(4))], nx(5) + 0.4)
band('<i>Princess Diana</i>', st(4) - 0.1, st(5) + 0.2, size=120)
pframe([(c('h5a'), nx(5) + 0.3), (c('h5b'), at(5, 'How will people') - 0.4)], at(5, "Because that's") - 0.1)
pwords(['The real question is not', '<i>&#8220;Do I look good?&#8221;</i>'], [st(5) + 0.5, at(5, 'Do I look')], at(5, 'How will people') - 0.6, size=62)
pwords(['The real question is', '<i>&#8220;How will people feel</i>', '<i>when I walk in?&#8221;</i>'], [at(5, 'How will people') - 0.4, at(5, 'How will people'), at(5, 'when I walk')],
       at(5, "Because that's") - 0.2, size=62)
lclip([(c('h5c'), at(5, "Because that's") - 0.2), (c('h5d'), at(5, "It's the message"))], en_(5))
q('That&#8217;s what style<br><i>actually is.</i>', at(5, "Because that's"), at(5, "It isn't a label") - 0.2, QL, size=72)
qstack(['It isn&#8217;t a label.', '<i>It isn&#8217;t a trend.</i>'], [at(5, "It isn't a label"), at(5, "It isn't a trend")], at(5, "It's the message") - 0.2, size=74)
q('It&#8217;s the message your clothes give<br><i>to the people in front of you.</i>', at(5, "It's the message"), at(5, 'And almost nobody') - 0.2, QL, size=56)
q('And almost nobody<br><i>teaches this.</i>', at(5, 'And almost nobody'), en(5) + 0.4, QL, size=74)
cfull([(c('h6a'), nx(6))], at(6, 'in a way') - 0.1)
band('&#8220;The most photographed woman<br><i>in the world&#8221;</i>', at(6, 'often called'), at(6, 'in a way') - 0.2, size=60)
lrow([c('h6c'), c('h6d'), c('h6e')], [at(6, 'in a way') - 0.2, at(6, 'a little surprising'), at(6, 'and easy to wear')], at(6, 'By the end') - 0.1,
     labels=['practical', 'a little surprising', 'any age, any budget'])
pics([P_('pnineties_19'), P_('pnineties_32'), P_('pnineties_11')], [at(6, 'By the end') - 0.2, at(6, 'exactly why'), at(6, 'still feel')], at(6, 'and how to use') - 0.1, h=820, y0=50)
capt('Why her clothes still feel <i>timeless</i>', at(6, 'exactly why'), at(6, 'and how to use') - 0.2)
lclip([(c('h6f'), at(6, 'and how to use') - 0.2)], en_(6))
q('The same rules,<br><i>without spending more,</i><br>or dressing like a royal', at(6, 'and how to use'), en(6) + 0.4, QL, size=62)
cfull([(c('h7a'), nx(7)), (c('h7b'), at(7, 'And the last one')), (c('h7c'), at(7, "And if you'd"))], en(7) + 0.35)
q('<div><span style="font-size:54px">Princess Diana&#8217;s</span><br><i style="font-size:118px">8 Timeless Style Rules</i></div>',
  at(7, 'eight rules') - 0.4, at(7, 'And the last one') - 0.2, QC, cls='over')
q('The last one changes<br><i>how you walk into any room.</i>', at(7, 'And the last one'), at(7, "And if you'd") - 0.2, QC, size=70, cls='over')
q(GUIDE, at(7, 'our personal stylist') - 0.3, en(7) + 0.2, QC, cls='over')

# ================= WHAT STYLE IS =================
lclip([(c('d8a'), nx(8)), (c('d8a2'), at(8, "That's a costume") - 0.1)], at(8, 'Real style') - 0.1)
q('Elegance isn&#8217;t wearing<br><i>the most beautiful dress in the room.</i>', at(8, "Elegance isn't"), at(8, "That's a costume") - 0.2, QL, size=58)
q('That&#8217;s<br><i>a costume.</i>', at(8, "That's a costume"), at(8, 'Real style') - 0.2, QL, size=96)
q('Real style is when your clothes<br><i>make other people feel something.</i>', at(8, 'Real style'), at(8, 'Welcome') - 0.2, QC, size=68)
lrow([c('d8b'), c('d8c'), c('d8d')], [at(8, 'Welcome') - 0.2, at(8, 'Calm'), at(8, 'Respected')], at(9, "You don't remember") - 0.3, labels=['welcome', 'calm', 'respected'])
cfull([(c('d9a'), at(9, "You don't remember") - 0.2), (c('d9b'), at(9, 'But you remember'))], en_(9))
q('You don&#8217;t remember<br><i>what most people wore last week.</i>', at(9, "You don't remember"), at(9, 'But you remember') - 0.2, QC, size=66, cls='over')
q('But you remember the woman<br><i>whose outfit fitted the moment.</i>', at(9, 'But you remember'), en(9) + 0.4, QC, size=66, cls='over')
cfull([(c('d10a'), nx(10))], en(10) + 0.7)
band('A rule for almost<br><i>every moment of her day</i>', at(10, 'And she had'), en(10) + 0.5, size=64)

# ================= 1. DRESS FOR THE PEOPLE YOU'RE ABOUT TO MEET =================
card_at('1. Dress for the People You&#8217;re About to Meet', 11, at(11, 'Most of us') - 0.15, size=88)
pframe([(c('r1a'), at(11, 'Most of us') - 0.2)], at(11, 'Diana asked') - 0.1)
pwords(['Most of us ask:', '<i>&#8220;What do I feel like wearing?&#8221;</i>'], [at(11, 'Most of us'), at(11, 'What do I')], at(11, 'Diana asked') - 0.2, size=56)
pic('pnohat_3.jpg', 170, 70, 632, 940, at(11, 'Diana asked') - 0.2, en_(11), pos='50% 30%')
qstack(['Diana asked:', '<i>&#8220;Who am I</i>', '<i>going to see?&#8221;</i>'], [at(11, 'Diana asked'), at(11, 'Who am I'), at(11, 'going to see')], en(11) + 0.4, box_=(860, 60, 1850, 1020), size=72, rh=160)
pics([P_('pcaring_28'), P_('pcaring_2')], [nx(12), at(12, 'one cheerful')], at(12, 'With it') - 0.15, h=880, y0=100, x0=40, x1=1250)
q('Visiting children<br><i>in hospital</i>', nx(12) + 0.3, at(12, 'one cheerful') + 1.6, RT, size=58)
q('One cheerful,<br><i>brightly patterned dress</i>', at(12, 'one cheerful') + 1.8, at(12, 'so often') + 0.9, RT, size=54)
q('Her<br><i>&#8220;caring dress&#8221;</i>', at(12, 'it became known'), at(12, 'With it') - 0.25, RT, size=84)
pic('pnohat_20.jpg', 70, 150, 1040, 780, at(12, 'With it') - 0.15, at(12, 'as a Kensington') - 0.1, pos='50% 40%')
q('With it:<br><i>big costume jewellery</i>', at(12, 'With it') + 0.1, at(12, 'as a Kensington') - 0.2, (1150, 60, 1890, 1020), size=62)
pic('pnohat_2.jpg', 150, 70, 752, 940, at(12, 'as a Kensington') - 0.1, en_(12), pos='50% 30%')
q('She picked children up,<br><i>and they played with it.</i>', at(12, 'she would pick'), en(12) + 0.4, (950, 250, 1880, 700), size=60)
q('as a Kensington Palace curator explained', at(12, 'as a Kensington') + 0.2, en(12) + 0.4, (950, 700, 1880, 800), size=34)
pframe([(c('r1b'), nx(13))], at(13, 'Visiting your') - 0.1)
pwords(['Ask one question first:', '<i>&#8220;Who will I see today,</i>', '<i>and what would make them</i>', '<i>feel at ease?&#8221;</i>'],
       [at(13, 'ask one question'), at(13, 'Who will I'), at(13, 'and what would'), at(13, 'feel at ease')], at(13, 'Visiting your') - 0.2, size=58, rh=150)
lclip([(c('r1c'), at(13, 'Visiting your') - 0.2)], at(13, 'try a soft blue') - 0.1)
q('Visiting your mother<br><i>or your grandmother?</i>', at(13, 'Visiting your'), at(13, 'Instead of') - 0.2, QL, size=66)
q('Instead of<br><i>something stiff&#8230;</i>', at(13, 'Instead of'), at(13, 'try a soft blue') - 0.2, QL, size=76)
lrow([c('r1d'), c('r1e'), c('r1f')], [at(13, 'try a soft blue') - 0.2, at(13, 'or a warm rose'), at(13, 'and a brooch')], at(13, 'A friend') - 0.1,
     labels=['a soft blue', 'a warm rose', 'a brooch to look at'])
lclip([(c('r1g'), at(13, 'A friend') - 0.2), (c('r1h'), at(13, 'Something warm'))], at(13, 'Your clothes become') - 0.1)
q('A friend who&#8217;s had<br><i>a hard week?</i>', at(13, 'A friend'), at(13, 'Something warm') - 0.2, QL, size=70)
q('Something warm,<br><i>simple and unfussy</i>', at(13, 'Something warm'), at(13, 'Your clothes become') - 0.2, QL, size=70)
cfull([(c('r1i'), at(13, 'Your clothes become') - 0.2)], en_(13))
q('Your clothes become a welcome<br><i>before you even say hello.</i>', at(13, 'Your clothes become'), en(13) + 0.4, QC, size=68, cls='over')

# ================= 2. NEVER LET YOUR CLOTHES BECOME A BARRIER =================
card_at('2. Never Let Your Clothes Become a Barrier', 14, en(14) + 0.3, size=92)
pics([P_('phats_7', pos='50% 20%'), P_('phats_0', pos='50% 20%'), P_('phats_2', pos='50% 20%')], [nx(15), st(15) + 1.0, st(15) + 2.0], at(15, 'But on visits') - 0.15, h=800, y0=50)
capt('On royal occasions, <i>a hat was expected.</i>', st(15) + 0.4, at(15, 'But on visits') - 0.25)
pics([P_('pnohat_11'), P_('pnohat_17', pos='50% 25%')], [at(15, 'But on visits') - 0.15, at(15, 'Diana left')], at(15, 'Her reason') - 0.15, h=900, y0=90, x0=40, x1=1330)
q('With children,<br><i>the hat stayed off.</i>', at(15, 'Diana left'), at(15, 'Her reason') - 0.25, (1330, 60, 1890, 1020), size=58)
pic('pnohat_23.jpg', 150, 70, 743, 940, at(15, 'Her reason') - 0.15, en_(15), pos='50% 30%')
q('&#8220;You can&#8217;t cuddle a child<br><i>in a hat.&#8221;</i>', at(15, "You can't cuddle") - 0.1, en(15) + 0.4, (950, 250, 1880, 700), size=68)
q('her reason, as the palace curator tells it', at(15, 'Her reason'), en(15) + 0.4, (950, 700, 1880, 800), size=34)
pic('paids_0.jpg', 110, 60, 700, 700, nx(16), en_(16), pos='50% 50%')
pic('paids_1.jpg', 1010, 50, 575, 880, at(16, 'she shook') - 0.2, en_(16), label='Middlesex Hospital, London', pos='50% 40%', lsize=46)
q('<i>April 1987</i>', nx(16) + 0.4, at(16, 'she shook') - 0.3, (60, 790, 860, 1040), size=92)
q('She shook the patients&#8217; hands<br><i>without gloves.</i>', at(16, 'she shook'), at(16, 'That photograph') - 0.2, (60, 790, 860, 1040), size=50)
q('That photograph<br><i>travelled around the world.</i>', at(16, 'That photograph'), en(16) + 0.4, (60, 790, 860, 1040), size=52)
lclip([(c('r2a'), nx(17)), (c('r2a2'), at(17, "It's armour") - 0.1)], at(17, "if you can't hug") - 0.1)
q('Elegance that keeps people<br>at a distance<br><i>isn&#8217;t elegance.</i>', at(17, 'Elegance that'), at(17, "It's armour") - 0.2, QL, size=62)
q('It&#8217;s<br><i>armour.</i>', at(17, "It's armour"), at(17, "if you can't hug") - 0.2, QL, size=104)
lrow([c('r2b'), c('r2c'), c('r2d')], [at(17, "if you can't hug") - 0.2, at(17, 'sit down with'), at(17, 'or reach for')], at(17, "it isn't the right") - 0.1,
     labels=['hug someone', 'sit down with a child', 'reach for a hand'])
q('It isn&#8217;t the right outfit<br><i>for that day.</i>', at(17, "it isn't the right"), en(17) + 0.5, QC, size=80)

# ================= 3. HONOUR YOUR HOST =================
card_at('3. Honour Your Host', 18, en(18) + 0.3, size=120)
pics([P_('pjapan_0', pos='50% 20%'), P_('pjapan_1', pos='50% 20%')], [nx(19), at(19, 'a white outfit')], at(19, "She didn't say") - 0.15, h=880, y0=100, x0=40, x1=1250)
q('<i>Japan, 1986</i>', nx(19) + 0.4, at(19, 'a white outfit') + 1.0, RT, size=84)
q('White, with large<br><i>red polka dots</i>', at(19, 'a white outfit') + 1.2, at(19, 'a quiet echo') - 0.2, RT, size=58)
q('A quiet echo<br><i>of the Japanese flag</i>', at(19, 'a quiet echo'), at(19, "She didn't say") - 0.25, RT, size=58)
pic('pjapan_11.jpg', 110, 110, 905, 860, at(19, "She didn't say") - 0.15, en_(19), pos='50% 40%')
q('She didn&#8217;t say<br>a word about it.', at(19, "She didn't say"), at(19, 'The outfit said') - 0.2, (1080, 60, 1890, 1020), size=60)
q('The outfit said it for her:<br><i>&#8220;I thought about you.&#8221;</i>', at(19, 'The outfit said'), en(19) + 0.4, (1080, 60, 1890, 1020), size=58)
lrow([c('r3a'), c('r3b')], [nx(20), at(20, 'and leave white') - 0.2], at(20, 'Invited to dinner') - 0.1)
q('You can do this<br><i>in a much smaller way.</i>', nx(20) + 0.3, at(20, 'Going to') - 0.2, R3, size=54)
q('A friend&#8217;s wedding?<br><i>Ask about the colours<br>of the day.</i>', at(20, 'Going to'), at(20, 'and leave white') - 0.2, R3, size=56)
q('Leave white and ivory<br><i>to the bride.</i>', at(20, 'and leave white'), at(20, 'Invited to dinner') - 0.2, R3, size=60)
pframe([(c('r3c'), at(20, 'Invited to dinner') - 0.2), (c('r3d'), at(20, 'It tells your host'))], at(20, 'Your outfit becomes') - 0.1)
pwords(['Invited to dinner?', 'Dress one step more carefully', 'than you need to.'], [at(20, 'Invited to dinner'), at(20, 'Dress one step'), at(20, 'than you need')], at(20, 'It tells your host') - 0.2, size=58)
pwords(['It tells your host:', '<i>&#8220;This evening</i>', '<i>matters to me.&#8221;</i>'], [at(20, 'It tells your host'), at(20, 'This evening'), at(20, 'matters to me')], at(20, 'Your outfit becomes') - 0.2, size=66)
cfull([(c('r3e'), at(20, 'Your outfit becomes') - 0.2)], en_(20))
q('Your outfit becomes<br><i>a gift.</i>', at(20, 'Your outfit becomes'), en(20) + 0.5, QC, size=92, cls='over')

# ================= 4. PLAN FOR THE AWKWARD MOMENT =================
card_at('4. Plan for the Awkward Moment', 21, en(21) + 0.3, size=104)
cfull([(c('r4a'), nx(22)), (c('r4b'), st(22) + 2.4)], at(22, 'So in low-cut') - 0.1)
band('Photographed stepping out of cars,<br><i>constantly</i>', st(22) + 0.4, at(22, 'So in low-cut') - 0.2, size=58)
pics([P_('pclutchb_0', pos='50% 30%'), P_('pclutchb_1', pos='50% 25%'), P_('pclutchb_2', pos='50% 30%')],
     [at(22, 'So in low-cut') - 0.15, at(22, 'she held'), at(22, 'close to her chest')], at(22, 'Her handbag') - 0.15, h=840, y0=40)
capt('A small clutch bag, <i>held close to her chest</i>', at(22, 'she held'), at(22, 'Her handbag') - 0.25)
pic('pclutchb_5.jpg', 170, 70, 627, 940, at(22, 'Her handbag') - 0.15, en_(22), pos='50% 30%')
q('She called them her<br><i>&#8220;cleavage bags&#8221;.</i>', at(22, 'Diana called') - 0.1, en(22) + 0.4, (860, 250, 1870, 700), size=72)
q('as her handbag designer later said', at(22, 'Her handbag'), en(22) + 0.4, (860, 700, 1870, 800), size=34)
lclip([(c('r4c'), nx(23))], at(23, 'Before you leave') - 0.1)
q('Elegance isn&#8217;t<br>only the outfit.', nx(23) + 0.2, at(23, "It's thinking") - 0.2, QL, size=70)
q('It&#8217;s thinking<br><i>one step ahead.</i>', at(23, "It's thinking"), at(23, 'Before you leave') - 0.2, QL, size=84)
pframe([(c('r4d'), at(23, 'Before you leave') - 0.2), (c('r4e'), at(23, 'Lift your arms') - 0.1), (c('r4f'), at(23, 'Walk up') - 0.1)], at(23, 'If the skirt') - 0.1)
pwords(['Before you leave the house:', '<i>Sit down in it.</i>', '<i>Bend.</i>', '<i>Lift your arms.</i>', '<i>Walk up a stair.</i>'],
       [at(23, 'Before you leave'), at(23, 'sit down in'), at(23, 'Bend'), at(23, 'Lift your arms'), at(23, 'Walk up')], at(23, 'If the skirt') - 0.2, size=60, rh=140)
lclip([(c('r4g'), at(23, 'If the skirt') - 0.2)], en_(23))
q('If the skirt rides up<br>or the neckline gapes&#8230;', at(23, 'If the skirt'), at(23, "you'll know") - 0.2, QL, size=60)
q('You&#8217;ll know<br><i>before anyone else does.</i>', at(23, "you'll know"), en(23) + 0.4, QL, size=70)

cfull([(c('m24a'), nx(24)), (c('m24b'), at(24, 'Most people click'))], en_(24))
q('If you&#8217;re still here,<br><i>you think about style more deeply than most.</i>', nx(24) + 0.3, at(24, 'Most people click') - 0.2, QC, size=60, cls='over')
q('So let&#8217;s go<br><i>a little deeper.</i>', at(24, "So let's"), en(24) + 0.5, QC, size=88, cls='over')

# ================= 5. RE-WEAR WHAT WORKS =================
card_at('5. Re-wear What Works', 25, en(25) + 0.3, size=120)
cfull([(c('r5a'), nx(26))], at(26, 'She wore that') - 0.1)
band('Her favourite pieces,<br><i>again and again</i>', at(26, 'wore her favourite'), at(26, 'She wore that') - 0.2, size=64)
pics([P_('pjapanb_29', 'Japan', pos='50% 15%', a=0.62), P_('pbalcony_0', 'the palace balcony, later that year', pos='50% 15%')],
     [at(26, 'She wore that') - 0.15, at(26, 'again later')], at(26, 'And some of her') - 0.15, h=850, y0=50, gap=120)
pics([P_('ppink83_17', '1983', pos='50% 10%', a=0.58), P_('ppink83_22', '1986: the ruffles are gone', pos='50% 10%', a=0.66)],
     [at(26, 'And some of her') - 0.15, at(26, 'quietly altered')], at(26, 'so they looked') - 0.15, h=850, y0=50, gap=80, x0=40, x1=1300)
q('Quietly altered,<br><i>so they looked new</i>', at(26, 'quietly altered') + 0.3, at(26, 'One fashion') - 0.2, (1300, 60, 1890, 1020), size=58)
pics([P_('plisbon_30', '1987', pos='50% 10%'), P_('plisbon_13', '1989: the sleeves are gone', pos='50% 10%', a=0.56)],
     [at(26, 'so they looked') - 0.15, at(26, 'One fashion')], en_(26), h=850, y0=50, gap=80, x0=40, x1=1300)
q('&#8220;Both fancy<br><i>and frugal&#8221;</i>', at(26, 'both fancy') - 0.4, en(26) + 0.4, (1300, 250, 1890, 700), size=70)
q('as one fashion journalist described her', at(26, 'One fashion') + 0.2, en(26) + 0.4, (1300, 700, 1890, 820), size=32)
lclip([(c('r5b'), nx(27)), (c('r5c'), at(27, 'They need a few'))], at(27, 'So instead of') - 0.1)
q('Elegant women don&#8217;t need<br><i>a new outfit for every occasion.</i>', at(27, 'Elegant women'), at(27, 'They need a few') - 0.2, QL, size=58)
q('A few pieces they love,<br><i>and the confidence<br>to wear them again</i>', at(27, 'They need a few'), at(27, 'So instead of') - 0.2, QL, size=60)
q('Instead of buying something new,<br><i>try changing one thing.</i>', at(27, 'So instead of'), at(27, 'A camel belt') - 0.2, QC, size=70)
lrow([c('r5d'), c('r5e'), c('r5f')], [at(27, 'A camel belt') - 0.2, at(27, 'A navy jacket'), at(27, 'Your hair up')], at(27, 'You probably') - 0.1,
     labels=['a camel belt', 'a navy jacket', 'your hair up'])
cfull([(c('r5g'), at(27, 'You probably') - 0.2)], en_(27))
q('You probably already own<br><i>the outfit for your next event.</i>', at(27, 'You probably'), en(27) + 0.4, QC, size=66, cls='over')
pframe([(c('r5h'), nx(28)), (c('r5i'), at(28, 'Tell me') - 0.1)], en_(28))
pwords(['Be honest:', '<i>What&#8217;s one piece you love,</i>', '<i>but rarely wear?</i>', 'Tell me in the comments.'],
       [at(28, 'Be honest'), at(28, "What's one piece"), at(28, 'but rarely wear'), at(28, 'Tell me')], en(28) + 0.4, size=60, rh=150)

# ================= THE GUIDE =================
cfull([(c('g29a'), nx(29)), (c('g29b'), at(29, "If you're watching"))], at(29, 'our personal stylist') - 0.1)
q('&#8220;I&#8217;d love to know which colours<br><i>and shapes are truly mine.&#8221;</i>', at(29, "I'd love"), at(29, 'our personal stylist') - 0.2, QC, size=62, cls='over')
cfull([(c('g29c'), at(29, 'our personal stylist') - 0.2)], at(29, 'Your best colours') - 0.1)
q(GUIDE, at(29, 'our personal stylist') - 0.1, at(29, 'Your best colours') - 0.2, QC, cls='over')
lrow([c('g29d'), c('g29e'), c('g29f')], [at(29, 'Your best colours') - 0.2, at(29, 'your most flattering'), at(29, 'and outfit formulas')], at(29, 'The link is') - 0.1,
     labels=['your best colours', 'flattering hairstyles', 'outfit formulas'])
cfull([(c('g29g'), at(29, 'The link is') - 0.2)], en_(29))
q('The link is<br><i>in the description.</i>', at(29, 'The link is'), en(29) + 0.3, QC, size=80, cls='over')

# ================= 6. KEEP AN OFF-DUTY UNIFORM =================
card_at('6. Keep an Off-Duty Uniform', 30, at(30, 'When Diana') - 0.15, size=110)
pics([P_('ppolo_0', pos='50% 20%'), P_('pwhitejeans_19', pos='50% 20%'), P_('pbosnia_4', pos='50% 20%')],
     [at(30, 'When Diana') - 0.2, at(30, "she didn't reinvent"), at(30, 'She went back')], en_(30), h=820, y0=50)
capt('Off duty: <i>the same few pieces</i>', at(30, 'She went back'), en(30) + 0.4)
look('ppolo_1', 'ppolo_14', ['a blazer', 'jeans', 'a sweatshirt', '<i>a polo match, 1988</i>'],
     [nx(31) + 0.3, at(31, 'with jeans'), at(31, 'and a sweatshirt'), at(31, 'at a polo')], nx(31), at(31, 'White jeans') - 0.15, at(31, 'and a sweatshirt'))
look('pwhitejeans_22', 'pwhitejeans_21', ['white jeans', 'loafers', 'a tailored blazer', '<i>London, 1994</i>'],
     [at(31, 'White jeans'), at(31, 'loafers'), at(31, 'and a tailored'), at(31, 'for shopping')], at(31, 'White jeans') - 0.15, at(31, 'A white shirt') - 0.15, at(31, 'and a tailored'))
look('pbosnia_0', 'pbosnia_5', ['a white shirt', 'jeans', 'loafers', '<i>Bosnia, 1997</i>'],
     [at(31, 'A white shirt'), at(31, 'jeans and loafers'), at(31, 'jeans and loafers') + 0.7, at(31, 'on her visit')], at(31, 'A white shirt') - 0.15, en_(31), at(31, 'jeans and loafers'))
lclip([(c('r6a'), nx(32))], at(32, 'So choose') - 0.1)
q('Women who always look put together<br><i>aren&#8217;t making more decisions.</i>', at(32, 'Women who'), at(32, "They're making") - 0.2, QL, size=54)
q('They&#8217;re making<br><i>fewer.</i>', at(32, "They're making"), at(32, 'So choose') - 0.2, QL, size=96)
q('Choose your own<br><i>uniform.</i>', at(32, 'So choose'), at(32, "Maybe it's") - 0.2, QC, size=96)
lrow([c('r6b'), c('r6c'), c('r6d'), c('r6e')], [at(32, "Maybe it's") - 0.2, at(32, 'a crisp white'), at(32, 'a navy or'), at(32, 'and one pair')], at(32, 'You probably') - 0.1,
     w=480, labels=['dark jeans', 'a white shirt', 'a camel jacket', 'loafers'])
lclip([(c('r6f'), at(32, 'You probably') - 0.2), (c('r6g'), at(32, 'Then wear it'))], en_(32))
q('You probably already own<br><i>most of it.</i>', at(32, 'You probably'), at(32, 'Then wear it') - 0.2, QL, size=68)
q('Wear it, again and again,<br><i>until it feels like you.</i>', at(32, 'Then wear it'), en(32) + 0.4, QL, size=64)

# ================= 7. EDIT AS YOU GROW =================
card_at('7. Edit as You Grow', 33, en(33) + 0.3, size=120)
pics([P_('peightiesb_14', pos='50% 25%'), P_('peightiesb_19', pos='50% 30%'), P_('peightiesb_24', pos='50% 20%')],
     [nx(34), at(34, 'many of her'), at(34, 'ruffles and bows')], at(34, 'But in the 1990s') - 0.15, h=800, y0=50)
capt('The 1980s: <i>ruffles and bows</i>', st(34) + 0.4, at(34, 'But in the 1990s') - 0.25)
pics([P_('pnineties_12', pos='50% 15%'), P_('pnineties_0', pos='50% 20%'), P_('pnineties_24', pos='50% 20%')],
     [at(34, 'But in the 1990s') - 0.15, at(34, 'her style became'), at(34, 'Clean lines')], en_(34), h=800, y0=50)
capt('The 1990s: <i>simpler, and more chic</i>', at(34, 'her style became'), at(34, 'Clean lines') - 0.2)
capt('Clean lines. <i>Plain colours.</i> Beautifully cut.', at(34, 'Clean lines'), en(34) + 0.4)
pic('pauctionb_0.jpg', 80, 190, 700, 700, nx(35), en_(35), pos='50% 50%', zoom=1.05)
pic('pauction_7.jpg', 840, 140, 534, 800, at(35, 'They were sold') - 0.2, en_(35), label='New York, June 1997', pos='50% 30%', lsize=44)
qstack(['<i>June 1997</i>', '79 of her dresses', 'sold at auction', '<i>for cancer and<br>AIDS charities</i>'],
       [nx(35) + 0.4, at(35, 'seventy-nine'), at(35, 'They were sold'), at(35, 'and the money')], en(35) + 0.4, box_=(1420, 60, 1900, 1020), size=46, rh=170)
lclip([(c('r7a'), nx(36)), (c('r7b'), at(36, 'Instead of keeping'))], at(36, 'So this season') - 0.1)
q('Your wardrobe should look like<br><i>the woman you are now,</i>', at(36, 'Your wardrobe'), at(36, 'not the woman') - 0.2, QL, size=58)
q('not the woman you were<br><i>ten years ago.</i>', at(36, 'not the woman'), at(36, 'Instead of keeping') - 0.2, QL, size=62)
q('Instead of keeping everything<br>&#8220;just in case&#8221;&#8230;', at(36, 'Instead of keeping'), at(36, 'try keeping') - 0.2, QL, size=58)
q('Keep only what you would<br><i>wear this month.</i>', at(36, 'try keeping'), at(36, 'So this season') - 0.2, QL, size=64)
lrow([c('r7c'), c('r7d')], [at(36, 'So this season') - 0.2, at(36, 'Give it to')], en(36) + 0.75, labels=['take out one thing', 'give it away'])
q('Make<br><i>room.</i>', at(36, 'Make room') - 0.1, en(36) + 0.7, R3, size=110)

# ================= 8. KEEP ONE OUTFIT FOR COURAGE =================
cfull([(c('r8a'), st(37) - 0.3)], at(37, 'Keep one outfit') - 0.2)
q('The eighth rule:<br><i>the one that changes how you walk into any room</i>', st(37) + 0.3, at(37, 'Keep one outfit') - 0.4, QC, size=58, cls='over')
cardx('8. Keep One Outfit for Courage', at(37, 'Keep one outfit') - 0.4, en(37) + 0.45, size=104)
pic('prevengeb_22.jpg', 300, 70, 391, 940, nx(38), at(38, 'On the 29th') - 0.1, pos='50% 30%', zoom=1.1)
q('For about three years,<br><i>this black silk dress hung<br>in her wardrobe.</i>', nx(38) + 0.3, at(38, 'She had bought') - 0.2, (880, 60, 1860, 1020), size=60)
q('Bought, then judged<br><i>too daring.</i>', at(38, 'She had bought'), at(38, 'On the 29th') - 0.2, (880, 60, 1860, 1020), size=80)
q('<i>29 June 1994</i>', at(38, 'On the 29th'), at(38, 'the same night') + 0.9, QC, size=130)
cfull([(c('r8c'), at(38, 'the same night') + 1.0), (c('r8d'), at(38, 'she put it on')), (c('r8e'), at(38, 'head high') - 0.3)], at(38, 'The newspapers') - 0.1)
band('The night her husband&#8217;s television<br>interview was broadcast', at(38, 'the same night') + 1.2, at(38, 'she put it on') - 0.2, size=48)
band('<i>The Serpentine Gallery, London</i>', at(38, 'walked into'), at(38, 'head high') - 0.4, size=64)
band('Head high, <i>smiling</i>', at(38, 'head high') - 0.2, at(38, 'The newspapers') - 0.2, size=72)
pics([P_('prevenge_4', pos='50% 20%'), P_('prevenge_19', pos='50% 25%'), P_('prevenge_16', pos='50% 20%')],
     [at(38, 'The newspapers') - 0.15, at(38, 'The newspapers') + 0.9, at(38, 'the revenge dress')], en(38) + 0.45, h=820, y0=50)
capt('<i>&#8220;The revenge dress&#8221;</i>', at(38, 'the revenge dress') - 0.1, en(38) + 0.35, size=84)
picfull('prevengeb_17.jpg', nx(39), at(39, 'So find your') - 0.1, pos='50% 20%', zoom=1.07)
band('The lesson isn&#8217;t revenge.', st(39) + 0.2, at(39, 'The lesson is that') - 0.2, size=66)
band('She decided<br><i>how she would walk into that room.</i>', at(39, 'The lesson is that'), at(39, 'So find your') - 0.2, size=62)
lclip([(c('r8g'), at(39, 'So find your') - 0.2)], at(39, "Maybe it's") - 0.1)
qstack(['Find your <i>courage outfit.</i>', 'Not the newest thing you own.', '<i>The one that makes you<br>stand a little taller</i>'],
       [at(39, 'So find your'), at(39, 'Not the newest'), at(39, 'The one that')], at(39, "Maybe it's") - 0.2, size=58, rh=190)
lrow([c('r8h'), c('r8i'), c('r8j')], [at(39, "Maybe it's") - 0.2, at(39, 'maybe a deep red'), at(39, 'And keep it')], en_(39),
     labels=['a classic black dress', 'a deep red jacket', 'kept ready'])

# ================= CLOSE =================
cfull([(c('e40a'), nx(40)), (c('e40b'), at(40, 'It was a language'))], at(40, 'I thought about') - 0.15)
band('Never a costume.', at(40, "Diana's style"), at(40, 'It was a language') - 0.2, size=70)
band('<i>A language</i>', at(40, 'It was a language'), at(40, 'Every outfit') - 0.2, size=110)
band('Every outfit said something<br><i>to the people in front of her.</i>', at(40, 'Every outfit'), at(40, 'I thought about') - 0.25, size=56)
pics([P_('pjapan_20', '&#8220;I thought about you.&#8221;', pos='50% 20%'), P_('pnohat_10', '&#8220;I&#8217;m here.&#8221;', pos='50% 20%'), P_('prevengeb_14', '&#8220;I&#8217;m not afraid.&#8221;', pos='50% 20%')],
     [at(40, 'I thought about') - 0.15, at(40, "I'm here") - 0.1, at(40, "I'm not afraid") - 0.1], en(40) + 0.6, h=830, y0=50)
q('After this video:', nx(41) + 0.3, at(41, 'Before you get') - 0.2, QC, size=90)
lrow([c('e41a'), c('e41b'), c('e41c')], [at(41, 'Before you get') - 0.2, at(41, 'Choose one piece'), at(41, 'And find your')], en_(41),
     labels=['1. Who will I see?', '2. Re-wear one piece', '3. Your courage outfit'])
pframe([(c('e42a'), nx(42)), (c('e42a2'), at(42, 'which of') - 0.1)], at(42, "And if you'd") - 0.1)
pwords(['Tell me in the comments:', '<i>Which of Diana&#8217;s eight rules</i>', '<i>will you try first?</i>', 'I read every comment.'],
       [at(42, 'tell me in'), at(42, 'which of'), at(42, 'will you try'), at(42, 'I read every')], at(42, "And if you'd") - 0.2, size=60, rh=150)
cfull([(c('e42b'), at(42, "And if you'd") - 0.2), (c('e42c'), at(42, 'the personal stylist') - 0.5)], en_(42))
q(GUIDE, at(42, 'the personal stylist') - 0.4, en(42) + 0.3, (180, 620, 1740, 1040), cls='over')
cfull([(c('e43a'), nx(43)), (c('e43b'), at(43, 'They were remembered'))], total - 2.6)
band('Not because they were expensive.', at(43, "weren't remembered"), at(43, 'They were remembered') - 0.2, size=60)
band('Because of how she made people <i>feel</i>', at(43, 'They were remembered') + 0.3, at(43, 'Thank you') - 0.2, size=62)
open(os.path.join(P, 'used.txt'), 'w').write('\n'.join(USED) + '\n')
json.dump(USED, open(os.path.join(P, 'used_times.json'), 'w'), indent=0)
