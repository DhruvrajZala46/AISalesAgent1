def coat_diagram(t0, t1):
    """Two line-art figures: coat shorter than the dress (x) vs coat longer than the hem (check)."""
    def fig(cx, coat_bottom, ok):
        dress = f'<path d="M{cx-70} 360 L{cx+70} 360 L{cx+105} 760 L{cx-105} 760 Z" fill="#6e1f2e" stroke="#fff" stroke-width="3"/>'
        coat = (f'<path d="M{cx-95} 340 Q{cx} 300 {cx+95} 340 L{cx+120} {coat_bottom} L{cx+18} {coat_bottom} L{cx} 420 L{cx-18} {coat_bottom} '
                f'L{cx-120} {coat_bottom} Z" fill="#c69a6d" stroke="#fff" stroke-width="3"/>')
        legs = f'<path d="M{cx-35} 760 L{cx-38} 860 M{cx+35} 760 L{cx+38} 860" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
        head = f'<circle cx="{cx}" cy="262" r="42" fill="none" stroke="#fff" stroke-width="3"/>'
        mark = (f'<path d="M{cx-22} 900 L{cx+22} 944 M{cx+22} 900 L{cx-22} 944" stroke="#fff" stroke-width="5" stroke-linecap="round"/>' if not ok else
                f'<path d="M{cx-26} 922 L{cx-6} 942 L{cx+28} 902" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>')
        return legs + dress + coat + head + mark
    for k, (cx, bottom, ok, label, tt) in enumerate([(640, 610, False, 'coat shorter than the dress', t0 + 0.2),
                                                     (1280, 800, True, 'coat longer than the hem', t0 + (t1 - t0) * 0.45)]):
        i = nid('cd')
        els.append(f'<div id="{i}" class="w" style="left:0;top:0;width:{W}px;height:{H}px;opacity:0;z-index:46">'
                   f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{fig(cx, bottom, ok)}</svg>'
                   f'<div class="tag" style="left:{cx-250}px;top:965px;width:500px">{label}</div></div>')
        tw.append(f'tl.fromTo("#{i}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.7,ease:"power3.out"}},{tt:.3f});')
        fade_out(i, t1, 0.45); sfx('pop', tt, -26)

