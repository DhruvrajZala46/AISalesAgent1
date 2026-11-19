R = 'REAL archive film or real news footage of the named royal woman herself (never an actress from The Crown, Spencer, Grace of Monaco or any film; never AI; never an animated photo; no slideshow): '
Q2 = {
'rmargfilm': ("princess margaret newsreel footage 1950s british pathe", R + 'Princess Margaret, 1940s-1950s, moving film'),
'rqmfilm': ("queen elizabeth 1938 paris state visit footage white", R + 'Queen Elizabeth (later the Queen Mother) in the 1930s, ideally in white, moving film'),
'rgracefilm': ("grace kelly wedding footage cathedral 1956 rainier", R + 'Grace Kelly at her wedding, April 1956, in the lace dress, moving film'),
'rletwalk': ("queen letizia arriving engagement walking video", R + 'Queen Letizia of Spain walking or arriving at an engagement, one steady take'),
'rkatewalk': ("kate middleton walking nude heels royal tour video", R + 'Catherine, Princess of Wales, walking at an engagement in nude heels, full length'),
'rqueenwalk': ("queen elizabeth walking bright coat hat crowd footage", R + 'Queen Elizabeth II in a bright single-colour coat and hat, walking or greeting people'),
'dresschoose': ("woman choosing dress in front of mirror holding dresses video", 'a woman holding up two dresses at a mirror or wardrobe, choosing what to wear for an occasion'),
'partyphoto': ("woman posing for photo elegant dress celebration friend taking picture video", 'a woman in a classic dress being photographed at a celebration or dinner'),
'albumpage': ("turning pages old family photo album hands video", 'hands turning the pages of an old family photo album'),
'pricecheck': ("woman checking price tag clothing store video", 'a woman in a clothes shop looking at a price tag'),
'dresscoat': ("woman midi dress long wool coat outfit walking video", 'a woman in a simple dress with a long, well-cut coat over it, walking'),
'camelcoat': ("white shirt camel coat outfit walking street video", 'a woman in a white shirt under a camel coat, walking'),
'nudepumps': ("nude pumps outfit walking street legs video", 'a woman walking in nude or skin-tone court shoes, legs visible'),
'shoechoose': ("woman choosing shoes for outfit at home closet video", 'a woman choosing which shoes to wear with her dress, at home'),
'emeraldcoat': ("woman emerald green coat street style video", 'a woman in one clear colour: an emerald green or deep blue coat or dress, walking'),
'colourdrape': ("color analysis draping fabric face mirror video", 'a woman having colour swatches or fabrics held near her face (colour analysis)'),
'hairlook': ("woman looking at her hair in mirror touching hair video", 'a woman looking at her own hair in the mirror, touching it, thinking'),
'lacesleeve': ("long sleeve lace dress evening event elegant video", 'a woman in a long-sleeved lace dress at an evening event'),
'blackdress': ("woman holding black dress against herself mirror video", 'a woman holding a black dress or top against herself at the mirror'),
'minidress': ("woman pulling down hem short dress uncomfortable video", 'a woman tugging down the hem of a short tight dress'),
'oldersmileb': ("elegant woman over 60 smiling outfit street style video", 'an elegant woman over 55 smiling, natural, real'),
}
Q2.update({
'rmargb': ("princess margaret rare footage video", R + 'Princess Margaret, 1940s-1950s, moving film'),
'rgraceb': ("grace kelly wedding video real footage", R + 'Grace Kelly at her wedding, April 1956, in the lace dress, moving film'),
'rkate2': ("kate middleton nude heels video", R + 'Catherine, Princess of Wales, walking at an engagement in nude heels, full length'),
'rqueenb': ("queen elizabeth ii colourful coat video", R + 'Queen Elizabeth II in a bright single-colour coat and hat, walking or greeting people'),
})
open('q2.txt','w').write('\n'.join(f'{t}={q}' for t,(q,b) in Q2.items())+'\n')
open('briefs2.py','w').write('B2 = {\n'+''.join(f'{t!r}: {b!r},\n' for t,(q,b) in Q2.items())+'}\nB.update(B2)\n')
print(len(Q2))
