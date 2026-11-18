# 7 Things Princess Diana Loved (18 Nov 2026): tag -> (Pinterest search, what the clip must show). Letters only.
D = "REAL archive film of Princess Diana herself (never an actress from The Crown or Spencer, never AI, never an animated photo, no slideshow)"
Q = {
# ---- Diana archive film (video pins)
'dwed': ("princess diana wedding 1981 glass coach arrival video", D + ": the wedding day 29 July 1981: the glass coach, Diana arriving at St Paul's, the long train"),
'dwedb': ("princess diana wedding dress train st pauls steps video", D + ": Diana in her wedding dress, the train on the steps or in the aisle"),
'dbalmoral': ("lady diana spencer balmoral 1981 engagement video", D + ": Lady Diana in 1981 at Balmoral or in the countryside, ideally in wellies"),
'dsheep': ("princess diana black sheep sweater polo 1981 video", D + ": Diana in the red sheep jumper"),
'dsmile': ("princess diana smiling candid close video", D + ": a close shot of Diana smiling or laughing"),
'dlaugh': ("princess diana laughing happy moments video", D + ": Diana laughing, warm"),
'deyes': ("princess diana eyes close up 1980s video", D + ": a close shot of Diana's face and eyes"),
'dbag': ("princess diana lady dior bag video", D + ": Diana carrying her black Dior handbag (top handle, small, structured)"),
'dnineties': ("princess diana 1990s london walking handbag video", D + ": Diana in the 1990s in London, walking, carrying a bag"),
'dparis': ("princess diana paris 1995 video", D + ": Diana in Paris"),
# ---- everyday scenes (video pins)
'dustbag': ("taking designer handbag out of dust bag video", "a woman taking a good handbag out of its dust bag, or putting it back; close, hands"),
'perfshelf': ("perfume bottles on vanity dresser aesthetic video", "perfume bottles standing on a dresser or vanity, untouched; calm light"),
'jumperdraw': ("folding sweater into drawer video", "hands folding a knit jumper and laying it in a drawer"),
'heelboot': ("woman walking heeled boots cobblestones struggling video", "a woman walking awkwardly in heeled boots on an uneven or wet path"),
'wellwalk': ("woman green wellies walking dog countryside video", "a woman in plain green rubber boots walking (ideally with a dog) through a field or muddy path"),
'wellies': ("green wellington boots walking mud close up video", "rubber rain boots on a woman's feet walking in mud or puddles, close"),
'countrylook': ("woman countryside outfit rubber boots knit coat video", "a woman in rubber boots, dark trousers and a soft knit or coat, outdoors, put together"),
'knitting': ("hands knitting red wool sweater video", "hands knitting with red wool, close"),
'knitstall': ("knitwear market stall sweaters video", "knitted jumpers on a market stall or shop shelf"),
'funjumper': ("woman novelty pattern sweater outfit video", "a woman wearing a playful patterned jumper (animals, hearts, motifs), smiling"),
'redjumper': ("woman red sweater navy trousers outfit video", "a woman in a red jumper with navy trousers or jeans, calm outfit"),
'collarknit': ("woman sweater with white collar outfit video", "a woman in a jumper with a white shirt collar showing at the neck"),
'brightliner': ("woman applying colorful blue eyeliner mirror video", "a woman at a mirror drawing a bright coloured (blue) eyeliner"),
'brownliner': ("smudging brown eyeliner pencil close up video", "a brown or taupe eyeliner pencil smudged along the lash line, close"),
'mascara': ("applying mascara close up natural makeup video", "mascara being applied to the lashes, close"),
'softeyes': ("natural soft eye makeup brown tones woman video", "a woman with soft brown eye make-up and full lashes, smiling at the camera or mirror"),
'shoebox': ("woman trying on shoes many boxes video", "a woman surrounded by shoe boxes, trying shoes on and off"),
'loaferpair': ("loafers in different colors lined up video", "the same flat loafer in two or three colours, lined up"),
'loaferwalk': ("woman suede loafers walking close up video", "soft suede or leather flat loafers on a woman's feet, walking"),
'loaferjean': ("woman loafers jeans outfit video", "a woman in flat loafers and jeans, full body"),
'loaferskirt': ("woman loafers midi skirt outfit video", "a woman in flat loafers and a skirt, full body"),
'loafertrou': ("woman loafers tailored trousers outfit video", "a woman in flat loafers and tailored trousers, full body"),
'bagshelf': ("closet shelf full of handbags video", "a wardrobe shelf full of many handbags; a woman unsure which to take"),
'tote': ("woman tan leather tote bag city outfit video", "a woman carrying a structured tan or brown leather tote in the city"),
'totedress': ("woman leather tote bag dress evening video", "a woman with a leather tote bag wearing a dress"),
'totejeans': ("woman tote bag jeans morning outfit video", "a woman with a tote bag in jeans, morning, out of the house"),
'bamboo': ("bamboo handle bag video", "a handbag with curved bamboo handles, close"),
'tophandle': ("structured top handle handbag black close up video", "a small structured black handbag with a top handle, close"),
'silkscarf': ("folding silk scarf tissue drawer video", "hands folding a silk scarf (or laying it in a drawer or box)"),
'scarfneck': ("woman tying silk scarf neck outfit video", "a woman with a silk scarf at her neck, ordinary day"),
'flowers': ("elegant woman buying flowers market handbag video", "an elegant woman buying flowers at a market or flower stall, handbag on her arm"),
'weekday': ("elegant woman everyday outfit handbag morning street video", "an elegant woman on an ordinary weekday morning with a nice handbag, walking"),
'perfchoose': ("woman choosing perfume testing bottles video", "a woman choosing between perfume bottles, testing them"),
'perfwrist': ("woman spraying perfume on wrist video", "a woman putting perfume on her wrist or neck, ordinary morning"),
'perfbottle': ("perfume bottle on dresser morning light video", "one perfume bottle on a dresser in soft morning light"),
'leavekeys': ("woman picking up keys leaving house morning video", "a woman picking up her keys and leaving her home"),
'drapes': ("color analysis drapes woman face video", "a colour analysis: coloured fabric drapes held under a woman's face"),
'smilewoman': ("elegant woman smiling softly close video", "an elegant woman smiling softly, close; warm light"),
'olderchic': ("elegant older woman style street video", "an elegant woman over 50, well dressed, walking or smiling"),
'mirrorlook': ("woman last look in mirror before leaving video", "a woman giving herself a last calm look in the mirror"),
}
if __name__ == '__main__':
    import re
    assert all(re.fullmatch(r'[a-z]+', t) for t in Q)
    open('q.txt', 'w').write('\n'.join(f'{t}={q}' for t, (q, b) in Q.items()) + '\n')
    open('briefs.py', 'w').write('B = {\n' + ''.join(f'{t!r}: {b!r},\n' for t, (q, b) in Q.items()) + '}\n')
    print(len(Q))
