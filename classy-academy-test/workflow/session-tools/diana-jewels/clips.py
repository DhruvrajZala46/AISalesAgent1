# clips.py - Princess Diana's 7 Jewels (19 Nov 2026). slot -> (clip key, start, end). Every clip is used ONCE.
# Windows from the second screening (scr/a_*.txt) and my own reading of the round-two strips (st/b_*.jpg).
C = {
 # ---- hook ----
 'h1a': ('jdsmile7', 1.5, 7.8),        # REAL film: Diana smiling, close, burgundy jacket
 'h2a': ('jewelhands15', 0.3, 7.9),    # hands with rings, close
 'h2b': ('palace2', 0.3, 12.1),        # Buckingham Palace ("went back to the palace")
 'h2c': ('tiarabox1', 0.3, 10.3),      # a tiara on a stand in a case
 'h2d': ('jewelhands39', 3.3, 8.8),    # a woman's hand wearing rings
 'h4a': ('jboxb41', 1.9, 6.0),         # an older woman's hands passing on a jewellery box
 'h4b': ('oldring13', 0.3, 7.4),       # a box of vintage rings
 'h5a': ('jdaus22', 8.6, 21.9),        # REAL film: Diana dancing in a pale gown (title over it)
 'h6a': ('jewelhands11', 0.3, 6.3),    # a pendant at the collarbone, a hoop at the ear (no face)
 'h6b': ('tiarabox23', 4.0, 12.0),     # a tiara, close
 # ---- 1 Spencer tiara ----
 's8a': ('jdwed39', 0.3, 9.0),         # REAL film 29 July 1981: her face under the veil, the Spencer tiara
 's10a': ('jboxb34', 0.3, 12.0),       # an old painted jewellery box full of pieces
 's11b': ('guestb15', 7.5, 16.3),      # a mother helping a bride on her wedding morning
 's11c': ('note49', 0.3, 6.6),         # a hand writing a small card
 's12a': ('smilec18', 0.3, 7.5),       # a woman walking in a cream coat
 # ---- 2 Lover's Knot ----
 'k15a': ('jdtiara13', 6.5, 11.5),     # REAL film: Diana in the Lover's Knot, its pearl drops
 'k17a': ('earfix27', 2.8, 13.4),      # a woman of about 45 touching her earring again and again
 'k18a': ('earringb3', 0.3, 12.9),     # a woman putting on earrings at home, one take
 'k18b': ('earringb9', 0.3, 10.0),     # putting in an earring, then at the mirror
 'k18c': ('earback5', 0.3, 8.3),       # fastening an earring back (captions cropped)
 # ---- 3 emerald ----
 'e24a': ('jboxb37', 8.9, 15.3),       # a wooden jewellery box opened
 'e25a': ('neckwrap25', 0.3, 13.9),     # a long necklace wrapped as a bracelet
 'e25b': ('pendant37', 0.3, 8.3),      # a pendant at the collarbone (labels cropped)
 'e25c': ('pearlchoker4', 1.3, 9.3),   # a strand of pearls fastened close at the neck
 'e26a': ('guestb8', 1.3, 12.3),        # getting ready, putting on her own bracelets
 'g27c': ('mirrorear20', 0.3, 7.5),    # putting on earrings at the mirror
 'g27b': ('vanityb16', 5.6, 16.4),     # getting ready, earrings
 # ---- 4 pearls ----
 'c31a': ('pearlbox6', 22.0, 34.6),    # pearl earrings in a box, held open
 'c32a': ('pearlnightb32', 0.3, 9.9),  # pearl drop earrings, close
 'c32b': ('pearlnightb19', 0.3, 2.6),  # a black dress and gloves, evening
 'c32c': ('pearldayb41', 1.3, 9.2),    # a woman wearing a pearl strand, smiling
 # ---- 5 sapphires ----
 'm37a': ('oldring28', 4.6, 12.1),     # an old ring box opened, rings inside
 'm38a': ('vanityb31', 2.3, 8.2),      # hands taking pieces out of a jewellery tray
 'm38b': ('jeweler17', 8.2, 17.2),     # a jeweller at the bench
 'm38c': ('jeweler48', 46.0, 55.0),    # a jeweller setting a stone
 # ---- 6 the cross ----
 'b44a': ('bridepearl24', 0.3, 10.3),  # a great-grandmother fastens the family pearls on the bride
 'b44b': ('broochb41', 10.5, 16.3),  # a brooch pinned at the neck
 'b44c': ('note45', 0.3, 12.3),        # a hand writing a letter with a dip pen
 # ---- 7 the ring ----
 'r47a': ('counterb27', 0.3, 15.0),    # trying rings on at a jewellery counter
 'r49a': ('counterb39', 6.8, 13.5),    # trying rings from a tray at a jeweller's (counterb18 dropped: brand end card)
 'r50a': ('olderring0', 2.8, 10.5),    # an older woman's hands with her ring
 'r50b': ('jboxb26', 7.9, 20.0),       # an old locket held in her hands
 'r51a': ('jdgala20', 4.6, 15.4),      # REAL film: Diana dancing
 # ---- close ----
 'z52a': ('smilec16', 0.3, 9.9),       # a woman walking in a trench
 'z52a2': ('earringb28', 0.3, 10.8),  # a woman in a trench putting on her earrings, coffee in hand
 'z52b': ('palace47', 2.3, 7.3),       # the palace
 'z53a': ('smileb35', 3.8, 16.3),      # a woman of about 65 laughing with a friend
 'z54b': ('earringb2', 0.3, 8.0),      # putting in an earring, close
}
CROP = {'note45': (40, 0, 1180), 'jdaus22': (65, 0, 1050), 'oldring13': (110, 400, 880), 'earback5': (85, 0, 860), 'pendant37': (107, 0, 900), 'bridepearl24': (120, 430, 850), 'jboxb26': (100, 0, 920), 'vanityb31': (0, 130, 1150)}
MAXSLOW = {'pearlnightb19': 1.85, 'counterb39': 1.6, 'oldring13': 1.55, 'jdtiara13': 1.25, 'earringb2': 1.4, 'pearlbox6': 1.4, 'jewelhands11': 1.4, 'guestb15': 1.45, 'note49': 1.5, 'pendant37': 1.7, 'oldring28': 1.6, 'jboxb41': 1.4, 'smilec16': 1.4}
