# build_timeline.py - turns the plan (scenes.json), the narration clock (clock.json), the chosen footage (picks.json) and any
# per-scene edits (overrides.json) into project/timeline.json, the editable project that render.py draws.
#   python3 -I project/build_timeline.py
# Formats are the channel's own (VISUAL-DNA-REPORT.md): FULL, CENTRE, ROW (3 x 608 px with ~22 px gutters / 4-6 touching),
# PAIR, SPLIT (framed clip left, quote right), QUOTE and CUE on the caramel, COLLAGE (product cut-outs popping in), CARD,
# the "in today's video..." white card + title, the guide call-out, and the white end card.
import json, os, subprocess
P = os.path.dirname(os.path.abspath(__file__)); WD = os.path.dirname(P)
scenes = json.load(open(f'{P}/scenes.json')); clock = json.load(open(f'{P}/clock.json'))
picks = json.load(open(f'{P}/picks.json'))
ov = json.load(open(f'{P}/overrides.json')) if os.path.exists(f'{P}/overrides.json') else {}
S = clock['sentences']; TOTAL = clock['total']; END_CARD = clock['end_card']
LEAD_IN = 0.12            # pictures change slightly before the word that names them
MIN_LEN = {'QUOTE': 3.4, 'CUE': 2.8}                   # a quote stays long enough to read (My7: 4-6 s, held into the next words)
GUIDE = dict(style='guide', line1='Check the description for', text='Personal Stylist Guide', line3='')


def media(aid):
    p = picks.get(aid)
    assert p and os.path.exists(os.path.join(WD, p['file'])), f'missing media for {aid}'
    m = {k: v for k, v in p.items() if k in ('file', 'focus', 'zoom', 'in', 'speed', 'cut', 'fit', 'pan')}
    m['asset'] = aid; return m


def word_time(si, word):
    """time the narrator says `word` in sentence si (proportional to its position in the text)"""
    s = S[si]; txt = s['text'].lower(); k = txt.find(word.lower())
    assert k >= 0, f'{word!r} not in sentence {si}'
    return s['start'] + (s['end'] - s['start']) * k / max(len(txt), 1)


for sc in scenes: sc.update(ov.get(str(sc['scene']), {}))
starts = []
for sc in scenes:
    if sc['layout'] == 'END': st = END_CARD
    elif sc.get('first'): st = 0.0
    elif sc['layout'] == 'CARD': st = S[sc['s0']]['start'] - 0.45
    elif sc.get('from_word'): st = word_time(*sc['from_word']) - LEAD_IN
    else: st = S[sc['s0']]['start'] - LEAD_IN
    starts.append(st)
for k, sc in enumerate(scenes):                      # a row never opens on an empty backdrop while the voice talks: when its first
    if k and sc['layout'] in ('ROW', 'PAIR', 'COLLAGE') and sc.get('enter_on') and scenes[k - 1]['layout'] in ('FULL', 'CENTRE', 'SPLIT', 'QUOTE', 'CUE'):
        first = word_time(*sc['enter_on'][0]) - LEAD_IN   # panel waits for a later word, the picture before it holds until then
        if first - starts[k] > 0.2: starts[k] = first - 0.15
ends = starts[1:] + [TOTAL]
for k, sc in enumerate(scenes):                      # cards run into the first second of the point; quotes long enough to read
    if sc['layout'] == 'CARD':
        nxt = S[sc['s0'] + 1]; cut = min(nxt['start'] + 1.0, nxt['end'] - 0.05)
        ends[k] = cut; starts[k + 1] = max(starts[k + 1], cut)
    if sc['layout'] in MIN_LEN and ends[k] - starts[k] < MIN_LEN[sc['layout']] and scenes[k + 1]['layout'] != 'CARD':
        ends[k] = starts[k] + MIN_LEN[sc['layout']]; starts[k + 1] = ends[k]
    if sc.get('until_word'): ends[k] = word_time(*sc['until_word']) - LEAD_IN
segs = []
for k, sc in enumerate(scenes):
    t0, t1 = starts[k], ends[k]; L = sc['layout']; A = sc['assets']
    sg = dict(scene=sc['scene'], kind=L, t0=round(t0, 3), t1=round(t1, 3), trans=sc.get('trans', 'dissolve'), trans_dur=sc.get('trans_dur', 0.5))
    if sc.get('first'): sg.update(trans='black', trans_dur=1.0)       # fade up from black (My7 0:00)
    if L == 'END': sg.update(trans='dissolve', trans_dur=0.6); segs.append(sg); continue
    if L == 'CARD': sg.update(text=sc['text'], trans='white'); segs.append(sg); continue
    if L == 'TITLE':                                   # "in today's video..." on white, then the title over a full clip (My7 0:24-0:34)
        cut = t0 + sc.get('white_len', 2.9)
        segs.append(dict(sg, kind='WHITE', t1=round(cut, 3), text=sc['white'], trans='white', size=96))
        segs.append(dict(sg, kind='FULL', t0=round(cut, 3), trans='fromwhite', trans_dur=0.6, shots=[dict(media(A[0]), t0=cut, t1=t1)],
                         texts=[dict(style='title', text=sc['title'], t0=cut + 0.3, t1=t1 + 0.05)]))
        continue
    if L in ('QUOTE', 'CUE'): sg['text'] = sc['text']
    elif L in ('FULL', 'CENTRE', 'SPLIT'):
        w = sc.get('weights') or [1] * len(A); tot = sum(w); edges = [t0]
        for x in w[:-1]: edges.append(edges[-1] + (t1 - t0) * x / tot)
        edges.append(t1)
        if sc.get('cuts_at'): edges = [t0] + [word_time(*c) - LEAD_IN for c in sc['cuts_at']] + [t1]
        sg['shots'] = [dict(media(a), t0=edges[i], t1=edges[i + 1]) for i, a in enumerate(A)]
        if L == 'SPLIT': sg['text'] = sc['text']
        if L == 'CENTRE' and sc.get('grow'): sg['grow'] = sc['grow']
    else:                                              # ROW / PAIR / COLLAGE: one panel per spoken item
        n = len(A)
        if sc.get('enter_on'): ts = [max(t0 + 0.05, word_time(*e) - LEAD_IN) for e in sc['enter_on']]
        else: ts = [t0 + 0.1 + i * (t1 - t0) * 0.5 / max(n - 1, 1) for i in range(n)]
        sg['panels'] = [dict(media(a), enter=round(ts[i], 3)) for i, a in enumerate(A)]
        if L == 'COLLAGE': sg['bg'] = sc.get('bg', 'caramel')
    if sc.get('guide'): sg['texts'] = [dict(GUIDE, t0=word_time(*sc['guide']) - 0.2, t1=t1)]
    segs.append(sg)
for i in range(1, len(segs)):                          # a card leaves with a hard cut; the white intro card dissolves from white
    if segs[i - 1]['kind'] == 'CARD' and segs[i]['trans'] == 'dissolve': segs[i]['trans'] = 'cut'
for sg in segs:
    for m in sg.get('shots', []): m['t1'] = min(m['t1'], sg['t1'])
tl = dict(fps=30, size=[1920, 1080], duration=TOTAL, segments=segs,
          audio=dict(voice='audio/voice.wav', music='audio/music_bed.wav', sting='audio/sting.wav'),
          note='The Classy Elegance - 8 Things That Make You Look Older. Built by build_timeline.py from scenes.json + clock.json + picks.json + overrides.json.')
_dur = {}
def clip_len(f):
    if f not in _dur:
        _dur[f] = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', os.path.join(WD, f)],
                                       capture_output=True, text=True).stdout or 0)
    return _dur[f]
def source_needed(sg, m):
    if 'enter' in m: return m.get('in', 0) + (sg['t1'] + 0.6 - m['enter']) * m.get('speed', 1.0)
    last = m is sg['shots'][-1]
    return m.get('in', 0) + (m['t1'] + (0.6 if last else 0) - m['t0'] + 0.5) * m.get('speed', 1.0)
for sg in segs:                                       # no shot may run past the end of its clip (it would freeze)
    for m in sg.get('shots', []) + sg.get('panels', []):
        if not m['file'].endswith('.mp4'): continue
        need = source_needed(sg, m)
        if need > clip_len(m['file']) - 0.05:
            print(f"WARNING scene {sg['scene']} {m['asset']}: needs {need:.1f}s of {m['file']} ({clip_len(m['file']):.1f}s)")
json.dump(tl, open(f'{P}/timeline.json', 'w'), indent=1)
used = [m['asset'] for sg in segs for m in sg.get('shots', []) + sg.get('panels', [])]
print('segments', len(segs), '| pictures', len(used), '| unique assets', len(set(used)), '| duration', round(TOTAL, 1), '| end card', round(END_CARD, 1))
