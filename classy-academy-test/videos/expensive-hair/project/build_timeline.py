# build_timeline.py - turns the edit plan (scenes.json), the narration clock (clock.json), the chosen footage (picks.json)
# and the per-scene edit (overrides.json) into project/timeline.json, the editable project that render.py draws.
#   python3 -I project/build_timeline.py
# Formats are the channel's own, measured on its 30 uploads (classy-academy-test/channel-deep-study-2026-10-19.md):
#   FULL, CENTRE (caramel + one vertical clip), ROW (3 x 608 px with 48 px gutters / 4 touching / 2 framed), SPLIT (clip left,
#   quote right on caramel), QUOTE (caramel or cream), CARD (white, black script, cut out), WHITE ("In today's video"),
#   the title ("Episode N" + script title over a darkened clip), the guide call-out, and the white CA end card.
# Edit picks.json (which file, in-point, focus, speed) or overrides.json (layout, shots, timing per scene) and run again.
import json, os, re
P = os.path.dirname(os.path.abspath(__file__)); WD = os.path.dirname(P)
scenes = json.load(open(f'{P}/scenes.json')); clock = json.load(open(f'{P}/clock.json'))
picks = json.load(open(f'{P}/picks.json'))
ov = json.load(open(f'{P}/overrides.json')) if os.path.exists(f'{P}/overrides.json') else {}
S = clock['sentences']; TOTAL = clock['total']; END_CARD = clock.get('end_card', S[-1]['end'] + 0.5)
LEAD_IN = 0.12            # pictures change slightly before the word that names them
EPISODE = 'Episode 31'; TITLE = 'Why Her Hair Looks Expensive'
GUIDE = dict(style='guide', line1='Check the description for', text='Personal Stylist Guide', line3='www.classyladyacademy.com')


def media(aid):
    p = picks.get(aid)
    assert p and os.path.exists(os.path.join(WD, p['file'])), f'missing media for {aid}'
    m = {k: v for k, v in p.items() if k in ('file', 'focus', 'zoom', 'in', 'speed', 'credit')}
    m['asset'] = aid; return m


def word_time(si, word):
    """time the narrator says `word` in sentence si (proportional to its position in the text)"""
    s = S[si]; txt = s['text'].lower(); k = txt.find(word.lower())
    assert k >= 0, f'{word!r} not in sentence {si}'
    return s['start'] + (s['end'] - s['start']) * k / max(len(txt), 1)


def sent_start(si): return S[si]['start'] - LEAD_IN


starts = []
for sc in scenes:
    st = sent_start(sc['s0'])
    if sc['layout'] == 'CARD': st = S[sc['s0']]['start'] - 0.45
    if sc['scene'] == 1: st = 0.0
    starts.append(st)
segs = []
for k, sc in enumerate(scenes):
    t0 = starts[k]; t1 = starts[k + 1] if k + 1 < len(scenes) else END_CARD
    o = ov.get(str(sc['scene']), {})
    lay = o.get('layout', sc['layout']); A = o.get('assets', sc['assets'])
    base = dict(scene=sc['scene'], trans='dissolve', trans_dur=0.5)
    if sc['scene'] == 1: base.update(trans='black', trans_dur=0.3)
    if lay == 'CARD':                                   # white card, black script; the first line of the point is spoken over it
        cut = t0 + o.get('card_len', t1 - t0) if A else t1
        segs.append(dict(base, kind='CARD', t0=t0, t1=cut, text=sc['text'], trans='white'))
        if A:
            segs.append(dict(base, kind='FULL', t0=cut, t1=t1, trans='cut', shots=[dict(media(A[0]), t0=cut, t1=t1)]))
        continue
    if lay == 'WHITE' and sc['scene'] == 9:            # "In today's video" card, then the title over a full clip
        cut = t0 + o.get('white_len', 2.8)
        segs.append(dict(base, kind='WHITE', t0=t0, t1=cut, text=sc['text'], trans='white', size=130))
        segs.append(dict(base, kind='FULL', t0=cut, t1=t1, trans='fromwhite', trans_dur=0.6, shots=[dict(media(A[0]), t0=cut, t1=t1)],
                         texts=[dict(style='title', episode=EPISODE, text=TITLE, t0=cut + 0.4, t1=t1 + 0.05)]))
        continue
    if sc['scene'] == 84:                               # goodbye over the opening clip (bookend), then the white CA end card
        segs.append(dict(base, kind='FULL', t0=t0, t1=END_CARD, shots=[dict(media(a), t0=t0, t1=END_CARD) for a in o['assets']]))
        segs.append(dict(base, kind='END', t0=END_CARD, t1=TOTAL, trans='dissolve', trans_dur=0.6))
        continue
    parts = o.get('parts') or [dict(layout=lay, assets=A, **{x: o[x] for x in ('enter_on', 'weights', 'bg', 'text', 'guide', 'guide_text') if x in o})]
    cuts = [t0] + [sent_start(p['from_sentence']) if 'from_sentence' in p else word_time(*p['from_word']) - LEAD_IN for p in parts[1:]] + [t1]
    for j, pt in enumerate(parts):
        a0, a1 = cuts[j], cuts[j + 1]; L = pt['layout']; AA = pt.get('assets', [])
        sg = dict(base, kind=L, t0=a0, t1=a1)
        if j > 0: sg['trans'] = pt.get('trans', 'dissolve')
        if L == 'QUOTE':
            sg['text'] = pt.get('text', sc['text'])
            if pt.get('bg'): sg['bg'] = pt['bg']
        elif L in ('FULL', 'CENTRE', 'SPLIT'):
            w = pt.get('weights') or [1] * len(AA); tot = sum(w); edges = [a0]
            for x in w[:-1]: edges.append(edges[-1] + (a1 - a0) * x / tot)
            edges.append(a1)
            if pt.get('cuts_at'): edges = [a0] + [word_time(*c) - LEAD_IN for c in pt['cuts_at']] + [a1]
            sg['shots'] = [dict(media(a), t0=edges[i], t1=edges[i + 1]) for i, a in enumerate(AA)]
            if L == 'SPLIT': sg['text'] = pt.get('text', sc['text'])
        else:                                            # ROW / PAIR: one panel per spoken item
            n = len(AA)
            if pt.get('enter_on'): ts = [max(a0 + 0.05, word_time(*e) - LEAD_IN) for e in pt['enter_on']]
            else: ts = [a0 + 0.1 + i * (a1 - a0) * 0.5 / max(n - 1, 1) for i in range(n)]
            sg['panels'] = [dict(media(a), enter=ts[i]) for i, a in enumerate(AA)]
        if pt.get('guide') is not None:
            sg['texts'] = [dict(GUIDE, t0=S[pt['guide']]['start'] - 0.2, t1=a1)]
            if pt.get('guide_text'): sg['texts'][0]['text'] = pt['guide_text']   # the name the voice says (Haircuts: "Classy Lady Guides")
        segs.append(sg)
# a card leaves with a hard cut (MNEo, Haircuts); every other change dissolves
for i in range(1, len(segs)):
    if segs[i - 1]['kind'] in ('CARD',) and segs[i]['trans'] == 'dissolve': segs[i]['trans'] = 'cut'
    if segs[i - 1]['kind'] == 'WHITE' and segs[i]['trans'] == 'dissolve': segs[i]['trans'] = 'fromwhite'; segs[i]['trans_dur'] = 0.6
for sg in segs:                                       # nothing may run past its segment
    for m in sg.get('shots', []): m['t1'] = min(m['t1'], sg['t1'])
tl = dict(fps=30, size=[1920, 1080], duration=TOTAL, segments=segs,
          audio=dict(voice='audio/voice.wav', music='audio/music_bed.wav', sting='audio/sting.wav'),
          note=f'Classy Academy - {EPISODE}: Why Her Hair Always Looks Expensive. Built by build_timeline.py from scenes.json + clock.json + picks.json + overrides.json.')
import subprocess
_dur = {}
def clip_len(f):
    if f not in _dur:
        _dur[f] = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', os.path.join(WD, f)],
                                       capture_output=True, text=True).stdout or 0)
    return _dur[f]
def source_needed(sg, m):
    """seconds of the clip a shot/panel plays: shots are drawn from 0.5 s before their start to their end (+0.6 s of
    dissolve into the next segment for the last one); panels from their entry to the end of the segment + 0.6 s"""
    if 'enter' in m: return m.get('in', 0) + (sg['t1'] + 0.6 - m['enter']) * m.get('speed', 1.0)
    last = m is sg['shots'][-1]
    return m.get('in', 0) + (m['t1'] + (0.6 if last else 0) - m['t0'] + 0.5) * m.get('speed', 1.0)
short = []
for sg in segs:                                       # no shot may run past the end of its clip (it would freeze or go black)
    for m in sg.get('shots', []) + sg.get('panels', []):
        if not m['file'].endswith('.mp4'): continue
        need = source_needed(sg, m)
        if need > clip_len(m['file']) - 0.05:
            short.append(m['asset']); print(f"WARNING scene {sg['scene']} {m['asset']}: needs {need:.1f}s of {m['file']} ({clip_len(m['file']):.1f}s)")
json.dump(tl, open(f'{P}/timeline.json', 'w'), indent=1)
used = [m['asset'] for sg in segs for m in sg.get('shots', []) + sg.get('panels', [])]
print('segments', len(segs), '| pictures', len(used), '| unique files', len({picks[a]['file'] for a in used}), '| duration', round(TOTAL, 1),
      '| end card', round(END_CARD, 1))
