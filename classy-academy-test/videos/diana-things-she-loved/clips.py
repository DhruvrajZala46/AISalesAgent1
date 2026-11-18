# clips.py - slot -> (clip key, start, end). Every clip is used ONCE. Windows from the second screening (scr/a_*.txt),
# then checked by me on the segment sheet before the build.
C = {
 # ---- hook ----
 'h1a': ('jumperdraw23', 6.4, 13.9),    # folding a knit away
 'h1b': ('tophandle14', 0.3, 7.3),      # the good bag (a structured top-handle bag)
 'h1c': ('perfshelf23', 0.3, 8.6),      # perfume bottles on a shelf
 'h1d': ('funjumper38', 13.7, 19.0),    # a jumper that makes her smile
 'h4a': ('scarfneck0', 0.3, 13.0),      # an elegant woman, silk scarf
 'h5a': ('dlaugh18', 12.3, 29.0),       # REAL film: Diana in a red jacket leaving a building (title over it)
 'h6a': ('weekday29', 8.1, 12.5),       # walking with her handbag
 'h6b': ('flowers40', 0.3, 9.9),        # at a flower stall, tote on her shoulder
 'h6c': ('dsmile20c', 0.3, 4.8),        # REAL film: Diana smiling, close (pre-cropped out of its black letterbox) ("the most personal of all")
 # ---- 1 wellies ----
 'w10a': ('wellwalk27', 0.3, 7.6),      # green wellies, walking a dog (shop logo appears near 8 s)
 'w10b': ('wellwalk15', 6.4, 13.6),     # green wellies, field, dog
 'w11a': ('wellies21', 0.3, 12.0),      # plain rubber boots in a puddle
 'w11b': ('wellies4', 0.3, 8.0),        # green rubber boots
 'w12a': ('dbalmoral3', 0.3, 8.3),      # REAL film: Lady Diana, 1981, heather behind
 # ---- 2 jumper ----
 's15a': ('knitting3', 5.6, 13.7),      # hands knitting red wool
 's15b': ('knitstall19', 0.3, 8.0),     # knitted jumpers on a stall
 's17a': ('knitstall0', 11.5, 16.2),    # knitted jumpers ("still knitted today")
 's18a': ('jumperdraw36', 0.3, 10.3),   # folding a jumper away (caption only from 11 s; heart icon cropped)
 's19a': ('funjumper44', 29.0, 37.0),   # a playful jumper
 's19b': ('redjumper37', 5.5, 14.5),    # red jumper, calm outfit
 's20a': ('redjumper6', 6.5, 16.0),     # red jumper
 # ---- 3 eyes ----
 'e25a': ('brightliner42', 0.3, 8.4),   # a bright coloured liner being drawn
 'e26a': ('brownliner4', 0.3, 4.1),     # brown pencil along the upper lashes, close (brownliner15 dropped: caption naming a brand)
 'e26a2': ('brownliner2', 1.9, 4.4),    # a brown (umber) pencil drawn along the upper lashes (caption ends at 1.5 s)
 'e26b': ('brownliner22', 1.4, 7.0),    # smudged
 'e26c': ('mascara45', 2.3, 8.3),       # mascara (cheek caption cropped away with CROP)
 'e26d': ('smilewoman4', 0.3, 12.0),    # a woman smiling, soft eyes
 'e27a': ('deyes9', 0.7, 8.1),          # REAL film: Diana's eyes, then her smile
 # ---- guide ----
 'g28a': ('drapes40', 0.3, 18.0),       # colour draping, one take
 'g28b': ('drapes36', 14.0, 23.0),      # colour draping
 'g28d': ('oldersmile14', 0.3, 8.0),    # a woman of about 65 in a camel knit, smiling (guide over it)
 # ---- 4 loafers ----
 'l31a': ('shoetry26', 18.0, 31.0),    # in a shoe shop, trying loafers on, white shirt and jeans
 'l32a': ('loaferpair1', 0.3, 12.9),    # a shop shelf of the same loafer in many colours
 'l32b': ('loaferskirt42', 0.3, 7.8),   # loafers with a skirt
 'l32c': ('loaferjean16', 4.7, 10.0),   # loafers with dark jeans
 'l33a': ('loaferjean14', 0.3, 4.7),    # loafers + jeans, full body
 'l33b': ('loaferskirt20', 0.3, 9.5),   # loafers + midi skirt
 'l33c': ('loafertrou35', 0.3, 10.0),   # loafers + trousers
 'l34a': ('weekday40', 0.3, 6.5),       # walking, at ease
 # ---- 5 tote ----
 't37a': ('bagshelf0', 0.3, 18.2),      # a shelf of many bags
 't38a': ('tote9', 0.3, 5.9),           # tan tote, brick street
 't38b': ('tote1', 10.1, 17.2),         # dark tote
 't38c': ('totejeans8', 0.7, 6.3),      # tote with jeans
 't38d': ('bamboo15', 0.3, 8.1),        # a bamboo-handle bag carried, loafers
 't38e': ('tophandle20', 6.2, 12.3),    # a structured black bag
 't39a': ('smilewoman17', 13.0, 20.2),  # smiling, at ease
 # ---- 6 Lady Dior ----
 'b43a': ('silkscarf27', 3.0, 11.1),    # a silk scarf laid away in a box (lid label cropped away with CROP)
 'b44a': ('scarfneck27', 3.2, 11.6),    # a woman at her mirror trying on her own silk scarves, one take (scarfneck11 dropped: brand end card)
 'b44b': ('leavehome15', 0.3, 6.7),     # leaving her building with her best (burgundy) bag
 'b44c': ('dresstote11', 0.3, 11.2),    # black dress, the good bag on her arm
 'b44d': ('scarfneck34', 1.3, 13.3),    # a silk scarf worn on an ordinary day
 'b44e': ('silkscarf0', 0.3, 12.0),     # a scarf knotted on a handbag she owns
 'b45a': ('weekday23', 0.3, 10.2),      # her good black bag and a cream trench on an ordinary day, coffee in hand
 # ---- 7 perfume ----
 'p48a': ('dwed32', 0.3, 5.5),          # REAL film 29 July 1981: the coach arrives at St Paul's
 'p48b': ('dwedb10', 0.3, 7.8),         # REAL film: the dress and the train, one take
 'p48c': ('dwed35', 0.3, 7.3),          # REAL film: up the cathedral steps, the long train
 'p50a': ('perfold19', 0.3, 7.4),       # a woman of about 50, eyes closed, a perfume bottle in her hands
 'p51a': ('perfstore19', 0.3, 6.0),     # testing perfume at a counter
 'p51b': ('perfvanity19', 0.3, 9.9),    # bottles set out on a mirrored tray on a dresser
 'p51c': ('perfwrist1', 0.3, 6.5),      # perfume on her wrist
 'p51d': ('olderwalk30', 0.3, 7.1),     # a woman of about 60 walking a city street, straw bag
 'p52a': ('dlaugh36', 20.8, 26.3),      # REAL film: Diana smiling, shaking hands
 'c53a': ('perfvanity15', 0.3, 8.3),    # perfume bottles placed on a gold tray
 'c54a': ('smilewoman36', 0.3, 9.6),    # a woman smiling, close (commentph16 dropped: an ad with a company end card)
 'c55a': ('oldersmile31', 0.3, 8.1),    # a woman of about 60 smiling, sunlit porch
 'c55b': ('perfvanity14', 0.3, 11.7),   # a perfume tray in sunlight
}
CROP = {'silkscarf27': (176, 600, 680), 'mascara45': (170, 0, 700), 'jumperdraw23': (62, 0, 1060), 'dlaugh18': (36, 0, 1150), 'dlaugh36': (64, 0, 1050), 'jumperdraw36': (36, 130, 1150)}
MAXSLOW = {'brownliner2': 1.5, 'brownliner4': 1.6, 'silkscarf27': 1.45, 'oldersmile31': 1.45}
