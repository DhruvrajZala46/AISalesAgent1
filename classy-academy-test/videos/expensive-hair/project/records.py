# records.py - writes the attribution and source records for every picture in the final export
#   python3 -I project/records.py  -> out/CREDITS.txt (for the YouTube description), out/SOURCES-LOG.md (where every shot comes from)
# Sources: raw/meta.json (creator posts from CLIP-CANDIDATES.md, downloaded by dl_cands.py) and raw/meta_pin.json (Pinterest pins
# found by pin_gap.py and downloaded by pin_dl.py).
import json, os, re
P = os.path.dirname(os.path.abspath(__file__)); WD = os.path.dirname(P)
tl = json.load(open(f'{P}/timeline.json')); picks = json.load(open(f'{P}/picks.json'))
meta = json.load(open(f'{WD}/raw/meta.json')); pins = json.load(open(f'{WD}/raw/meta_pin.json'))
uses = {}
for sg in tl['segments']:
    for m in sg.get('shots', []) + sg.get('panels', []):
        t = m.get('t0', m.get('enter', sg['t0']))
        uses.setdefault(picks[m['asset']]['file'], []).append((m['asset'], t, sg['scene']))


def ts(t): return f'{int(t // 60)}:{int(t % 60):02d}'


def source(f):
    b = os.path.basename(f)
    if b in pins:
        p = pins[b]; handle = next((h for h in p['handles'] if h.lower() not in ('gmail.com',)), None)
        orig = p['link'] if p['link'] and re.match(r'https://(www\.)?(instagram|tiktok)\.com/', p['link']) else None
        plat = 'Instagram' if orig and 'instagram' in orig else 'TikTok' if orig and 'tiktok' in orig else None
        who = f'@{handle}' if handle else None
        return dict(creator=who, original=orig, platform=plat, pin=p['pin'], pinner=p['pinner'], route='Pinterest video pin' if f.endswith('.mp4') else 'Pinterest photo pin',
                    other_link=None if orig else p['link'])
    k = b.rsplit('.', 1)[0]; m = meta[k]
    who = m['creator'].split(',')[0].split(' (')[0].strip()
    plat = 'TikTok' if 'tiktok.com' in m['url'] else 'Instagram'
    return dict(creator=who, original=m['url'], platform=plat, pin=None, pinner=None, route=f'{plat} post (CLIP-CANDIDATES.md)', other_link=None)


order = sorted(uses, key=lambda f: min(t for _, t, _ in uses[f]))
cred = ["Why Her Hair Always Looks Expensive (It's Not the Cut) - footage credits, in order of appearance", '',
        "Thank you to the creators whose videos appear in this episode:", '']
seen = set()
for f in order:
    s = source(f); when = ts(min(t for _, t, _ in uses[f]))
    if f.endswith('.jpg'): continue
    key = s['creator'] or s['original'] or s['pin']
    if key in seen: continue
    seen.add(key)
    if s['creator'] and s['original']: cred.append(f"{when}  {s['creator']} on {s['platform']} - {s['original']}")
    elif s['original']: cred.append(f"{when}  {s['platform']} creator - {s['original']}")
    else: cred.append(f"{when}  video via Pinterest ({s['pinner']}) - {s['pin']}")
cred += ['', 'Andie MacDowell at the Cannes Film Festival, 2021: press photographs (via Pinterest: '
         + ', '.join(source(f)['pin'] for f in order if f.endswith('.jpg')) + ').', '',
         'Music: Frederic Chopin, Berceuse Op. 57; Nocturne Op. 9 No. 2; Nocturne Op. 32 No. 1 - Musopen recordings, CC0 1.0.',
         'Narration: synthetic voice (Kokoro TTS, voice af_heart).']
os.makedirs(f'{WD}/out', exist_ok=True)
open(f'{WD}/out/CREDITS.txt', 'w').write('\n'.join(cred) + '\n')
rows = ['# SOURCES-LOG - The Classy Elegance: Why Her Hair Always Looks Expensive', '',
        'Every picture in the final export, where it was found, and its permission status. Footage was found the way the channel',
        "finds its own (creators' TikTok / Instagram reels, Pinterest video pins, celebrity press photos via Pinterest); real footage only,",
        'every clip checked by eye for AI (frames of all 198 downloads reviewed). **No creator has been contacted and no permission',
        "has been obtained yet** - nothing was sent without the owner's approval. The permission request template is in",
        '`CLIP-CANDIDATES.md`. The channel itself credits creators on screen only for long tutorial holds (Hairstyles video); this',
        'episode has none that long, so credits are in CREDITS.txt for the description.', '',
        '| First seen | Scenes | Shot | Creator | Original post | Found via | File |', '|---|---|---|---|---|---|---|']
for f in order:
    s = source(f); us = uses[f]
    scenes = ', '.join(sorted({str(sc) for _, _, sc in us}, key=int)); notes = '; '.join(sorted({picks[a]['note'] for a, _, _ in us}))
    via = s['route'] + (f" [{s['pin']}]({s['pin']}) (pinned by {s['pinner']})" if s['pin'] else '')
    orig = f"[{s['original']}]({s['original']})" if s['original'] else (s['other_link'] or 'not identified')
    rows.append(f"| {ts(min(t for _, t, _ in us))} | {scenes} | {notes} | {s['creator'] or 'not identified'} | {orig} | {via} | `{os.path.basename(f)}` |")
open(f'{WD}/out/SOURCES-LOG.md', 'w').write('\n'.join(rows) + '\n')
print('files', len(order), '| credit lines', len(seen))
