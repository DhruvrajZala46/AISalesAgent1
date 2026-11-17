# clips.py - slot -> (clip key, start, end). Every window is checked by eye on large frames before the build (vs/).
C = {
 # hook
 'h1a': ('glamb3', 0.3, 7.3), 'h1b': ('fascin42', 0.3, 8.2),
 'h2a': ('alone35', 0.3, 5.9), 'h2b': ('quiet23', 0.3, 5.9),
 'h2d': ('carb36', 3.3, 9.3),
 'h3a': ('warma14', 0.3, 8.1), 'h3b': ('music31', 7.1, 11.8),
 'h4a': ('crowd33', 0.3, 15.8), 'h4b': ('seena49', 0.3, 8.3), 'h4c': ('teapour5', 1.3, 9.3), 'h4d': ('alivea2', 0.3, 5.6),
 'h5b': ('ageda8', 0.3, 12.0), 'h5c': ('ageda5', 24.4, 36.0), 'h5d': ('paint27', 0.3, 5.6),
 'h6a': ('styl24', 1.0, 7.1), 'h6b': ('lookback12', 2.3, 6.9), 'h6c': ('hugc4', 8.5, 14.0),
 # 1
 'a9a': ('wedda3', 4.0, 8.9), 'a9b': ('wedda10', 0.3, 5.3), 'a9c': ('lunch3', 0.3, 6.3),
 'a9d': ('crowd2', 0.3, 7.3), 'a9f': ('lookaway47', 0.3, 6.3),
 'a10a': ('busy2', 5.8, 14.0),
 'a11a': ('boredl0', 0.3, 10.1), 'a11b': ('simpleb29', 0.3, 4.3), 'a11c': ('walkhappy7', 0.3, 3.8),
 'a12a': ('lunch16', 0.3, 10.0), 'a12b': ('fascin1', 0.3, 5.5), 'a12c': ('nod29', 3.3, 6.3),
 'a13a': ('warma42', 0.3, 7.0), 'a13b': ('pour2', 0.3, 5.3), 'a13c': ('window17', 0.3, 11.3),
 'a14a': ('edge11', 0.3, 6.3), 'a14b': ('ease7', 0.3, 3.2),
 'a15a': ('calma29', 0.3, 7.9), 'a15b': ('lookback6', 4.3, 12.3),
 # 2
 'b17d': ('mirror5', 0.3, 4.3), 'b17a': ('quiet15', 0.3, 7.3), 'b17b': ('sensible26', 0.3, 9.5), 'b17c': ('nod19', 0.3, 7.4),
 'b18a': ('four10', 0.3, 7.3), 'b18b': ('compl31', 0.3, 5.7),
 'b19a': ('marilynd39', 0.3, 11.4), 'b19b': ('marilynd14', 1.1, 9.0),
 'b20a': ('dianaa12', 12.6, 22.0), 'b20b': ('dianaf14', 11.0, 18.0), 'b20c': ('dianab4', 14.5, 23.0),
 'b21a': ('weights30', 1.0, 6.6), 'b21b': ('reaction4', 0.3, 6.3), 'b21c': ('ballet0', 13.0, 22.6),
 'b22a': ('mirror38', 16.0, 25.8),
 'b23a': ('planner22', 4.0, 14.9), 'b23b': ('piano32', 0.3, 26.6),
 'b24a': ('alivea5', 8.9, 19.1), 'b24b': ('cinema43x', 0.3, 5.95),
 'b25a': ('softfirm23', 0.3, 22.5),
 # 3
 'c27a': ('ready37', 0.3, 7.3), 'c28a': ('walkhappy30', 0.3, 7.0),
 'c29d': ('lovely1', 0.3, 4.3), 'c29b': ('nervb12', 0.3, 14.3),
 'c30a': ('ask19', 0.3, 12.3), 'c31a': ('seena27', 0.3, 20.2),
 'c33a': ('party43', 0.3, 14.5),
 # guide
 'g34a': ('glamb32', 11.3, 22.3), 'g34b': ('drape4', 2.4, 11.0), 'g34c': ('hairst18', 2.3, 10.3), 'g34e': ('adjustb23', 0.3, 7.3),
 # 4
 'd36a': ('nervb40', 0.3, 14.2), 'd36b': ('glamb16', 1.3, 5.3), 'd36c': ('edge9', 4.3, 13.3),
 'd37a': ('laughb42', 0.3, 14.7), 'd37b': ('calmtable3', 0.3, 9.3), 'd37c': ('slowwalk9', 0.3, 9.3), 'd37d': ('myst10', 5.3, 12.7),
 'd38z': ('journal47', 2.1, 16.3), 'd38a': ('parked25', 8.3, 19.0), 'd38b': ('elev14', 0.3, 4.0), 'd38c': ('frontdoor12', 0.3, 7.3),
 'd39a': ('lunch33', 0.3, 11.0), 'd39b': ('music11', 2.5, 8.2), 'd39c': ('alivea46', 0.3, 3.0),
 'd40a': ('knock33', 0.3, 3.9), 'd40b': ('shoulders30', 0.3, 14.1), 'd40c': ('hello5', 0.3, 12.3), 'd40d': ('shoulders11', 0.3, 6.0),
 'd41a': ('notice24', 8.4, 17.2),
 # 5
 'e43a': ('mystb21', 5.3, 9.1), 'e43b': ('cold10', 10.7, 14.8), 'e43c': ('scroll21', 0.3, 8.3),
 'e44b': ('calma27', 0.3, 12.3),
 'e45a': ('piano41', 10.1, 22.3), 'e45b': ('oldfriend29', 0.3, 18.8),
 'e47b': ('deep1', 0.3, 8.9), 'e47c': ('olderb16', 21.7, 32.4),
 'e48a': ('comfort2', 0.3, 12.4),
 # close
 'f49a': ('paint30', 14.2, 19.8),
 'f50a': ('softfirm37', 11.0, 19.0), 'f50b': ('agedb31', 0.3, 11.3),
 'f51a': ('scroll28', 0.3, 14.3), 'f51b': ('hairst48', 0.3, 6.3),
 'f52b': ('piano45', 5.6, 37.7), 'f52c': ('frontdoor1', 0.3, 9.2),
 'f53a': ('paint0', 36.7, 42.8), 'f53b': ('ballet10', 0.3, 10.9),
 'f54a': ('typing40', 0.3, 7.3), 'f55a': ('glamb30', 0.3, 7.3), 'f56a': ('four1', 0.3, 7.3), 'f57a': ('walkhappy16', 0.3, 4.9),
}

MAXSLOW.update({'weights30': 1.5, 'weddb2': 1.45, 'knock33': 1.55, 'party32': 1.45, 'fascin1': 1.55, 'hugc4': 1.45, 'nod29': 1.6, 'cinema43x': 1.85, 'mirrorsmile34': 1.5})
# crops in the 720x1280 space (x0, y0, h): past burned-in captions and small watermarks, measured on the frame sheets
CROP.update({'dianaa12': (36, 0, 1150), 'hugc4': (36, 0, 1150), 'drape4': (100, 358, 922), 'wedda10': (73, 0, 1020), 'hello5': (108, 384, 896), 'hairst48': (98, 50, 930), 'lovely1': (107, 380, 900)})
