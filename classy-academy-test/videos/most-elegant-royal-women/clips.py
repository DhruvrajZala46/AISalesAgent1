# clips.py - The 7 Most Elegant Royal Women Ever, Ranked (19 Nov 2026). slot -> (clip key, start, end). Every clip is used ONCE.
# Windows from two screenings (scr/a_*.txt, scr/b_*.txt) and my own reading of the strips (st/a_*.jpg, st/b_*.jpg).
C = {
 # ---- hook ----
     # hands over an old black-and-white family album ("their photographs still look right")
 'h4a': ('creamoutfit34', 2.1, 10.3), # a woman at home in a simple cream knit and white trousers ("small choices")
 'h5a': ('rdiana6', 12.5, 32.1),       # REAL film: Diana in a red jacket greeting a crowd (title over it)
 # ---- 7 Margaret ----
 'm10a': ('dresschoose13', 2.1, 4.75),  # a woman holding a dress up against herself at her wardrobe ("will it be enough?")
 'm11a': ('partyphoto36', 0.3, 19.3),  # two women in long ivory and pale gowns at a celebration
 'm11c': ('albumpage13', 0.3, 13.2),   # an older woman turning the pages of her family album
 # ---- 6 Letizia ----
 'l16a': ('mixlook7', 0.3, 7.5),       # a simple blazer with a leather bag, city street
 'l16b': ('dresscoat34', 0.3, 4.4),    # a simple dress with a coat
 'l17a': ('pricetag15', 0.3, 10.2),    # handling price tags at a clothes rail
 'l18a': ('mixlook41', 7.2, 11.5),     # a cream leather bag with a black blazer
 'l18b': ('nudeheels22', 0.1, 2.4),    # leather heels, walking (size caption cropped)
 'l18c': ('bluecoat25', 0.3, 7.0),     # a long, well-cut coat (no text)
 'l18d': ('camelcoat30', 1.2, 8.3),   # a beige trench, white shirt, black trousers and one good leather bag
 # ---- 5 Queen Mother ----
 'q24a': ('rmirrorblack', 0, 0),        # placeholder, replaced below
 'q25a': ('winterwhite0', 0.3, 11.8),  # a woman over 50 in cream head to toe
 'q25b': ('creamoutfit39', 2.3, 10.3), # a cream knit with cream trousers
 'q25c': ('camelcoat16', 3.1, 6.1),    # a white shirt and cream trousers under a camel trench
 # ---- guide ----
 'g27a': ('colourdrape32', 0.3, 11.7), # colour analysis: drapes held under a client's face
 'g27b': ('winterwhite44', 0.3, 13.7), # an elegant woman in winter white
 # ---- 4 Catherine ----
 'k30a': ('rkate31', 0.3, 9.3),        # REAL film: Catherine walking at an engagement
 
 'k31a': ('shoerack16', 6.3, 12.0),    # shoes on a rack
 'k32a': ('nudepumps36', 17.9, 25.3),  # nude pointed court shoes walking, legs
 'k32b': ('greycoat12', 2.3, 9.3),     # placeholder, replaced below
 # ---- 3 Elizabeth II ----
 'e35a': ('rqueen3', 19.9, 30.5),      # REAL film: the Queen in green, 2022, close
 'e37a': ('greycoat12', 2.3, 9.3),     # a woman in a grey coat on a quiet street
 'e38a': ('bluecoat0', 0.3, 8.3),      # a bold blue coat
 'e38b': ('emeraldcoat6', 0.2, 3.0),   # an emerald green jacket, walking
 'e38c': ('redscarf19', 0.3, 6.3),     # a red scarf near the face
 # ---- 2 Diana ----
 'd41a': ('rdiana8', 0.3, 19.4),       # REAL film: Diana with short hair, lilac jacket, pearls
 'd43a': ('salon5', 21.7, 30.0),       # a client talking in the salon chair
 'd44a': ('shortcut41', 4.8, 12.0),    # a short bob, she turns and smiles
 'd44b': ('shortcut34', 0.3, 12.2),    # hairdresser and a client in her 50s talking
 'd44c': ('salon25', 4.3, 10.9),       # a calm consultation
 'd45a': ('shortcut14', 18.3, 26.9),   # a fresh short cut, she smiles
 # ---- 1 Grace Kelly ----
 'g47a': ('rgrace3', 7.9, 15.1),      # REAL film: Grace and Rainier walking down the cathedral steps, 1956
 'c49a': ('shortdress36', 0.3, 7.8),   # a short pink dress
 'c50a': ('lacedress42', 0.3, 7.0),    # a black long-sleeved high-neck lace dress
 'c50b': ('lacesleeve1', 2.5, 11.6),   # lace sleeves
 'c51a': ('winterwhite8', 17.4, 22.6), # an elegant woman smiles and waves
 # ---- close ----
 'z52a': ('rletwalk5', 17.0, 34.5),    # REAL film: Queen Letizia greeting the public
 'z53a': ('smileolder6', 0.3, 5.0),    # a woman laughing, talking to camera
 'z54a': ('rletizia3', 19.7, 29.4),    # REAL film: Letizia smiles and waves
 'z54b': ('rletwalk6', 12.6, 19.2),   # REAL film: Queen Letizia with King Felipe in a doorway
}
C['m10b'] = ('blackmirror9', 0.2, 3.5)    # a woman in a long black dress checking it in the mirror
C['c50c'] = ('highneck21', 15.7, 19.4)   # a high-neck dress
C['z54c'] = ('rqm0', 0.3, 6.3)           # REAL film: the Queen Mother smiling in her garden
C['e38d'] = ('emeraldcoat26', 16.6, 18.8)  # a woman of about 55 in a bright emerald coat
C['l18e'] = ('shoechoose22', 3.0, 13.7)  # tweed jacket, white shirt, jeans: simple pieces and one good bag
C['q24a'] = ('blackmirror10', 0.3, 7.4)  # a woman in a black dress at the mirror
C['k32b'] = ('coatlook22', 0.3, 17.5)   # the same nude courts with a cream, blue, black, red and blue outfit
CROP = {
 'shoechoose22': (60, 0, 940),    # Russian subtitles at y 975-1010   # (x0, y0, h) in 720x1280 space, measured on gridded frames (chk/grid_*.jpg)
 'salon5': (240, 190, 700),       # word captions at y 980-1010
 'lacedress42': (130, 0, 800),    # word captions from y 830
 'pricetag15': (0, 110, 1170),    # Subastral watermark top right
 'nudeheels22': (60, 230, 1050),  # "Talla 35 a 40" label at y 110-200
 'rkate31': (14, 24, 1230),       # black border
 'bluecoat0': (20, 70, 1210),     # repost handle top left
 'rgrace3': (50, 190, 1090),      # "Extravagant" logo at y 120-170
 'camelcoat16': (110, 0, 900),    # TikTok watermark at y 620-700 left and 1000-1060 right
}
MAXSLOW = {'nudeheels22': 1.6, 'blackmirror10': 1.55, 'camelcoat16': 1.55, 'emeraldcoat6': 1.75, 'shortcut41': 1.55, 'blackmirror9': 1.6, 'albumpage29': 1.6, 'dresschoose13': 1.9, 'highneck21': 1.5, 'albumpage13': 1.55, 'rletwalk6': 1.5, 'redscarf19': 1.5}
