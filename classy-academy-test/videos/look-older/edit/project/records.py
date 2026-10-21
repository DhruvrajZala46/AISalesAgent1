# records.py - the records of what is actually in the final export, built from timeline.json only (an unused candidate can
# never appear): out/SOURCES-LOG.md (asset manifest: source, creator, licence/permission), out/CREDITS.txt (for the
# description), out/SCRIPT-TO-VISUAL-MAP.md (every sentence: picture, layout, motion, timing, checks).
#   python3 -I project/records.py
import json, os, re
P = os.path.dirname(os.path.abspath(__file__)); WD = os.path.dirname(P)
tl = json.load(open(f'{P}/timeline.json')); picks = json.load(open(f'{P}/picks.json'))
clock = json.load(open(f'{P}/clock.json'))['sentences']; scenes = {s['scene']: s for s in json.load(open(f'{P}/scenes.json'))}
briefs = {b['id']: b for b in json.load(open(f'{WD}/plan/briefs.json'))}
def rec(aid): return json.load(open(f'{WD}/picks/{aid}.json'))
def ts(t): return f'{int(t // 60)}:{t % 60:04.1f}'
def tsm(t): return f'{int(t // 60)}:{int(t % 60):02d}'
uses = {}
for sg in tl['segments']:
    for m in sg.get('shots', []) + sg.get('panels', []):
        t0 = m.get('t0', m.get('enter', sg['t0'])); t1 = m.get('t1', sg['t1'])
        uses.setdefault(m['asset'], []).append((t0, t1, sg['scene'], sg['kind']))
def platform(u):
    for k, v in (('instagram.com', 'Instagram'), ('tiktok.com', 'TikTok'), ('youtube.com', 'YouTube'), ('youtu.be', 'YouTube')):
        if u and k in u: return v
    return None
IGV = {}                                               # authors read from Instagram's own public embed (igcheck.js -> plan/ig_verify.jsonl)
if os.path.exists(f'{WD}/plan/ig_verify.jsonl'):
    for ln in open(f'{WD}/plan/ig_verify.jsonl'):
        try: j = json.loads(ln)
        except ValueError: continue
        if j.get('user'): IGV[re.sub(r'\?.*$', '', j['url'])] = j['user'].split('\n')[0].strip()
def source(aid):
    r = rec(aid); orig = r.get('original_post') or (r['src_link'] if platform(r.get('src_link')) else None)
    if orig: orig = re.sub(r'\?.*$', '', orig)
    v = IGV.get(orig) if orig else None
    handle = ('@' + v) if v else (r.get('credit_handle') or None)
    r['verified'] = 'author confirmed by the post\'s own Instagram embed' if v else ('original post given, author not confirmed' if orig else 'no original post found; Pinterest upload only')
    pinner = r.get('pinner') or r.get('creator_user')
    pin = r.get('pin_url') or (f'https://www.pinterest.com/{pinner}/ (uploader profile; numeric pin link not found)' if pinner else '')
    return dict(r=r, orig=orig, plat=platform(orig), handle=handle, pin=pin, pinner=pinner,
                kind='photo' if r['file'].endswith(('.jpg', '.png')) else 'video')
order = sorted(uses, key=lambda a: min(u[0] for u in uses[a]))
# ---------------- SOURCES-LOG (asset manifest)
rows = ['# SOURCES-LOG: "8 Things That Make You Look Older: What to Wear Instead" (The Classy Elegance)', '',
        'Every picture that appears in the final export, built from the final timeline (no unused candidate is listed).',
        'Footage was found the way the channel finds its own: creators\' reels and photos as Pinterest pins, traced to the original post.',
        'Every clip was checked for AI (watermark scan + frames by eye). **No licence is held and no permission has been requested for any',
        'third-party picture.** Credit is not permission. Decision for every row: **unresolved** (see `QC-REPORT.md`, rights).', '',
        '| # | On screen | Script line | What it shows | Original creator / rights holder | Original post | Found via (exact URL) | Licence / permission | Checks | File |',
        '|---|---|---|---|---|---|---|---|---|---|']
for n, a in enumerate(order, 1):
    s = source(a); r = s['r']; us = uses[a]
    when = '; '.join(f'{tsm(u[0])}-{tsm(u[1])}' for u in us)
    line = ' / '.join(sorted({clock[i]['text'] for u in us for i in range(scenes[u[2]]['s0'], scenes[u[2]]['s1'] + 1)}, key=lambda x: x))[:160]
    who = r.get('rights_holder') or s['handle'] or (f"{r.get('creator')} (Pinterest uploader; not confirmed as the creator)" if r.get('creator') else 'not identified')
    orig = f"[{s['orig']}]({s['orig']})" if s['orig'] else (r.get('src_link') or 'not identified')
    via = f"Pinterest {s['kind']} pin {s['pin'] or '(numeric link not found)'} uploaded by {s['pinner']}; search \"{r.get('search_tag', '')}\""
    lic = r.get('rights', 'No licence known; creator permission not requested')
    chk = f"AI scan {r.get('ai_scan', 'n/a')}; eye: {r.get('ai_eye', 'n/a')}; creator: {r['verified']} ({r.get('creator_evidence', 'n/a')})"
    rows.append(f"| {n} | {when} | {line} | {r.get('note', '')} | {who} | {orig} | {via} | {lic} | {chk} | `{r['file']}` ({a}) |")
rows += ['', '## Other material', '',
         '| Material | Use | Source | Licence |', '|---|---|---|---|',
         '| Chopin, Berceuse Op. 57 (Olga Gurevich); Nocturne Op. 9 No. 2 and Nocturne Op. 32 No. 1 (Frank Levy) | music bed and end-card swell | Musopen recordings, archive.org/details/musopen-chopin-complete-works-flac | CC0 1.0 (public domain dedication) |',
         '| Narration | whole voice track | Kokoro-82M, voice af_heart, kokoro-onnx | Apache-2.0 / MIT; synthetic voice, not a clone of a real person |',
         '| Fonts | cards, quotes, title | Pinyon Script, Playfair Display (Google Fonts) | SIL Open Font License |',
         '| Logo | top-left and end card | The Classy Elegance (CE), owner\'s own | owner\'s |',
         '| Clip sound | none | every clip is muted | - |']
os.makedirs(f'{WD}/out', exist_ok=True); open(f'{WD}/out/SOURCES-LOG.md', 'w').write('\n'.join(rows) + '\n')
# ---------------- CREDITS (description)
cred = ['8 Things That Make You Look Older: What to Wear Instead - footage credits, in order of appearance', '',
        'Thank you to the creators whose videos and photos appear in this video:', '']
seen = set()
for a in order:
    s = source(a); r = s['r']; key = (s['handle'] or s['orig'] or s['pin'])
    if key in seen: continue
    seen.add(key); when = tsm(min(u[0] for u in uses[a]))
    if r.get('credit_line'): cred.append(f"{when}  {r['credit_line']}")
    elif s['handle'] and s['orig']: cred.append(f"{when}  {s['handle']} on {s['plat']} - {s['orig']}")
    elif s['orig']: cred.append(f"{when}  {s['plat']} - {s['orig']}")
    else: cred.append(f"{when}  {s['kind']} via Pinterest ({s['pinner']}) - {s['pin'] or r.get('src_link') or ''}")
cred += ['', 'Music: Frederic Chopin, Berceuse Op. 57; Nocturne Op. 9 No. 2; Nocturne Op. 32 No. 1 - Musopen recordings, CC0 1.0.',
         'Narration: synthetic voice (Kokoro TTS, voice af_heart).']
open(f'{WD}/out/CREDITS.txt', 'w').write('\n'.join(cred) + '\n')
# ---------------- SCRIPT-TO-VISUAL MAP
MOTION = {'FULL': 'full-screen clip, soft dissolve in (0.5 s)', 'CENTRE': 'one vertical clip centred on the caramel, dissolve',
          'ROW': 'panels grow from their top-left corner (0.6 s), one per spoken item', 'PAIR': 'two panels, each grows in on its word',
          'COLLAGE': 'product cut-outs pop in one per spoken item (0.35 s)', 'QUOTE': 'white serif + script, written on left to right',
          'CUE': 'white script cue written on', 'SPLIT': 'framed clip left, quote written on at right', 'CARD': 'fade to white, black script written on, hard cut out',
          'WHITE': '"in today\'s video..." written on', 'END': 'dissolve to the white CE end card'}
out = ['# Script-to-visual map: "8 Things That Make You Look Older: What to Wear Instead"', '',
       'Built from the final timeline. Times are the exported video\'s. Sound for every scene: the narration over the soft piano bed',
       '(~20 dB under), no sound effects. Checks: AI scan score (< 0.40 passes) and frames checked by eye; creator traced.', '']
for sg in tl['segments']:
    sc = scenes[sg['scene']]; k = sg['kind']
    said = ' '.join(clock[i]['text'] for i in range(sc['s0'], sc['s1'] + 1)) if k != 'END' else '(end card)'
    if k == 'FULL' and sc['layout'] == 'TITLE': said = '(title) ' + said
    out.append(f"### {ts(sg['t0'])}-{ts(sg['t1'])} ({sg['t1'] - sg['t0']:.1f} s) - scene {sg['scene']}, {k}")
    out.append(f'**Narration:** {said}')
    if sg.get('text'): out.append(f"**On-screen text:** {re.sub('<[^>]+>', '', sg['text'])} ({MOTION.get(k, '')})")
    for tx in sg.get('texts', []): out.append(f"**On-screen text:** {tx.get('line1', '')} / {tx['text']} ({tx['style']})")
    for m in sg.get('shots', []) + sg.get('panels', []):
        a = m['asset']; r = rec(a); b = briefs.get(a, {}); s = source(a)
        at = f"enters {ts(m['enter'])}" if 'enter' in m else f"{ts(m['t0'])}-{ts(m['t1'])}"
        out.append(f"- **{a}** ({at}; clip from {m.get('in', 0):.1f} s, speed {m.get('speed', 1.0)}): {r.get('note', '')}  ")
        out.append(f"  Concept: {b.get('brief', '(reused from earlier)')}  ")
        out.append(f"  Source: {s['handle'] or r.get('creator') or 'not identified'}, {s['orig'] or s['pin'] or r.get('src_link')}  ")
        out.append(f"  Checks: AI scan {r.get('ai_scan', 'n/a')}; {r.get('ai_eye', '')}; licence: {r.get('rights', 'none known')}")
    if k in MOTION and not sg.get('text'): out.append(f'Motion: {MOTION[k]}.')
    out.append('')
open(f'{WD}/out/SCRIPT-TO-VISUAL-MAP.md', 'w').write('\n'.join(out) + '\n')
print('assets', len(order), '| credit lines', len(seen))
