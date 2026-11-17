# clips.py - slot -> (clip key, start, end). Every window is checked by eye on large frames before the build (vs/).
C = {
 # ---- Princess Diana: real archive film (Pinterest video pins; fan re-uploads of news film) ----
 'h3a': ('dieighties2', 0.3, 8.2),      # 1981: stepping from the glass coach in the wedding gown
 'h3b': ('dicrowd0', 12.3, 18.0),       # white sleeveless dress: reaching to the hands held out from the crowd
 'h3c': ('dicrowd35', 2.4, 7.9),        # tartan jacket, flowers, waving to a crowd
 'h3d': ('dijewel43', 18.4, 22.4),      # close: black jacket, pearl choker, smiling
 'h4a': ('dinineties12', 8.4, 12.9),    # royal-blue blazer over a black dress, smiling
 'h6a': ('dinineties25', 9.7, 17.0),    # the photographers' stand, then her in sunglasses, waving
 'd10a': ('dicrowd0', 2.4, 12.0),       # the same walkabout, earlier: hands reaching to her
 'r4a': ('diwalk39', 0.3, 3.7),         # pale blue beaded halter dress: out of the car, silver clutch in her hand
 'r4b': ('dicar5', 0.3, 2.35),          # red gown beside the car on a red carpet, clutch held in front
 'r5a': ('dicar2x', 2.4, 6.4),           # the pale blue strapless gown (the re-made Catherine Walker), walking through a reception
 'r8c': ('dicar1', 0.3, 5.4),           # 29 June 1994: across the lawn from the car, the handshake
 'r8d': ('dicar1', 9.6, 14.6),          # close: the dress, the choker, the clutch
 'r8e': ('dicar1', 18.6, 22.6),         # head high, laughing
 'e40a': ('dicrowd21', 22.5, 29.3),     # purple and black suit: talking with people in a crowd
 'e40b': ('dicaring5', 21.0, 27.6),     # hugging a child tightly, no hat
 'e43a': ('dicrowd21', 15.3, 21.5),     # purple and black suit, smiling in a crowd
 'e43b': ('dilaugh6', 12.5, 27.5),      # white shirt, laughing behind her hands

 # ---- everyday scenes (Pinterest video pins: Instagram / TikTok creators' reels) ----
 # hook
 'h1a': ('jeansb1', 0.3, 4.0), 'h1b': ('mirrorg4', 2.3, 9.4),
 'h2a': ('posing38', 0.3, 8.0), 'h2b': ('gardenb2', 4.3, 9.3), 'h2c': ('grandmf40', 16.1, 22.5), 'h2d': ('gownparty36', 0.5, 9.5),
 'h5a': ('agese28', 1.0, 6.5), 'h5b': ('wedguestd24', 0.3, 6.0), 'h5c': ('outfitsb27', 0.3, 6.5), 'h5d': ('navyblazer44', 5.6, 13.7),
 'h6c': ('navyblazer30', 3.3, 9.3), 'h6d': ('rewearb38', 12.8, 19.2), 'h6e': ('softblueb12', 0.3, 8.3), 'h6f': ('agese23', 0.3, 6.3),
 'h7a': ('dieighties1', 2.2, 6.2), 'h7b': ('blackdressb48', 0.3, 4.6), 'h7c': ('knitc20', 0.3, 9.3),
 # what style is
 'd8a': ('gownparty30', 0.3, 8.0), 'd8a2': ('gownparty23', 0.3, 5.1),
 'd8b': ('hugfriend19', 1.3, 9.0), 'd8c': ('sitdownb9', 0.3, 4.2), 'd8d': ('outfitc41', 2.3, 7.3),
 'd9a': ('streetpeople41', 5.4, 14.5), 'd9b': ('sitdownb35', 19.6, 26.0),
 # 1
 'r1a': ('wardrobe11', 3.0, 12.0), 'r1b': ('shirtc9', 4.6, 11.1), 'r1c': ('grandme22', 3.4, 9.5),
 'r1d': ('softblue5', 0.3, 7.3), 'r1e': ('rosec17', 35.0, 39.4), 'r1f': ('brooch2', 30.3, 36.3),
 'r1g': ('comfortb3', 3.0, 7.5), 'r1h': ('knitc17', 0.3, 5.3), 'r1i': ('wedguestb45', 0.3, 7.0),
 # 2
 'r2a': ('stairs47', 0.3, 8.0), 'r2a2': ('redjacketb34', 11.6, 15.4),
 'r2b': ('grandmab19', 1.3, 7.4), 'r2c': ('kneelchild3', 13.9, 18.9), 'r2d': ('holdhands27', 0.3, 6.3),
 # 3
 'r3a': ('wedguestb42', 0.3, 8.9), 'r3b': ('bride46', 4.0, 12.0), 'r3c': ('carout46', 0.3, 6.5), 'r3d': ('posing22', 0.3, 5.7), 'r3e': ('wedguestd20', 0.3, 8.0),
 # 4
 'r4c': ('carouth31', 2.3, 8.5), 'r4d': ('sitdownb32', 0.3, 7.0), 'r4e': ('tryon15', 7.6, 11.0), 'r4f': ('stairs39', 0.3, 6.0), 'r4g': ('rewearb31', 3.3, 11.2),
 'm24a': ('commentb19', 0.3, 5.8), 'm24b': ('dinineties12', 0.5, 7.0),
 # 5
 'r5b': ('samedress12', 3.5, 8.6), 'r5c': ('wedguestb44', 3.5, 12.0),
 'r5d': ('belt22', 16.3, 27.0), 'r5e': ('navyjacketb6', 8.1, 14.8), 'r5f': ('hairup47', 0.3, 6.3),
 'r5g': ('tidyrailb24', 0.3, 7.0), 'r5h': ('gownparty8', 0.3, 8.0), 'r5i': ('commenting32', 0.3, 9.0),
 # guide
 'g29a': ('softblueb24', 5.6, 10.0), 'g29b': ('drapeb19', 0.3, 8.0), 'g29c': ('hairup23', 3.0, 7.3),
 'g29d': ('drapeb47', 21.7, 32.0), 'g29e': ('hairb37', 0.3, 6.0), 'g29f': ('jacketdress29', 6.1, 13.8), 'g29g': ('wedguestb25', 0.3, 6.2),
 # 6
 'r6a': ('wardrobe14', 0.3, 9.0), 'r6b': ('jeansb1', 10.1, 17.4), 'r6c': ('whiteshirt8', 3.3, 11.3), 'r6d': ('camelblazer9', 2.3, 6.3), 'r6e': ('loafers44', 4.3, 8.3),
 'r6f': ('capsule7', 0.3, 4.1), 'r6g': ('navyblazer21', 0.3, 6.2),
 # 7
 'r7a': ('agese44', 7.6, 13.6), 'r7b': ('declutter4', 3.0, 8.3), 'r7c': ('declutterb9', 11.0, 22.0), 'r7d': ('donateb34', 3.0, 11.0),
 # 8
 'r8a': ('blackdress39', 0.3, 5.3), 'r8g': ('agesd9', 21.7, 32.4),
 'r8h': ('blackdress16', 0.3, 9.5), 'r8i': ('redjacketb40', 0.3, 7.0), 'r8j': ('blackhang11', 0.3, 2.4),
 # close
 'e41a': ('shirtc9', 13.5, 26.0), 'e41b': ('rose25', 16.6, 24.8), 'e41c': ('sitdownb45', 10.5, 13.8),
 'e42a': ('commentb7', 9.4, 14.5), 'e42a2': ('commentb19', 15.5, 20.4), 'e42b': ('hairup43', 0.3, 6.3), 'e42c': ('softblueb24', 33.3, 39.9),
}
CROP.update({'dinineties12': (22, 0, 1200), 'dijewel43': (22, 0, 1200), 'diwalk39': (62, 0, 1060), 'dicrowd35': (22, 80, 1200), 'dicar1': (40, 140, 1140)})
CROP.update({'outfitsb27': (70, 250, 1030), 'wedguestb42': (60, 240, 1040), 'drapeb47': (93, 10, 950), 'declutterb9': (150, 0, 930),
             'grandmab19': (34, 0, 1220)})
MAXSLOW.update({'dicar5': 1.5, 'dicar2x': 1.55, 'blackhang11': 1.9, 'softblueb24': 1.5, 'sitdownb9': 1.6, 'rosec17': 1.5})
