#!/usr/bin/env python3
"""collect.py - pull fresh public video lists for every niche channel (yt-viral input).

    python3 collect.py OUT_DIR [--per 60]

Reads ../channels.json (channel IDs), runs `yt-dlp --flat-playlist` on each channel's /videos tab
(public listings only, no login), and writes OUT_DIR/collected.json in the shape yt-viral's swipe.py
expects, plus a publish date (month-accurate) for the recency and season filters.
Shorts (< 3 min) are dropped: they are a different shelf.
"""
import json, os, sys, subprocess, datetime
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
out_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
per = int(sys.argv[sys.argv.index('--per') + 1]) if '--per' in sys.argv else 60
os.makedirs(os.path.join(out_dir, 'ch'), exist_ok=True)
chans = json.load(open(os.path.join(HERE, '..', 'channels.json')))

def fetch(cid):
    f = os.path.join(out_dir, 'ch', f'{cid}.json')
    r = subprocess.run(['yt-dlp', '--flat-playlist', '-J', '--playlist-end', str(per),
                        '--extractor-args', 'youtubetab:approximate_date',
                        f'https://www.youtube.com/channel/{cid}/videos'], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip(): open(f, 'w').write(r.stdout); return cid, True
    return cid, False

with ThreadPoolExecutor(6) as ex: res = list(ex.map(fetch, chans))
failed = [c for c, ok in res if not ok]

rows, good = [], 0
for cid, ok in res:
    if not ok: continue
    d = json.load(open(os.path.join(out_dir, 'ch', f'{cid}.json'))); ch = d.get('channel') or d.get('uploader') or cid; n = 0
    for e in d.get('entries') or []:
        if not e or e.get('view_count') is None or (e.get('duration') or 0) < 180: continue
        ts = e.get('timestamp')
        date = datetime.datetime.fromtimestamp(ts, datetime.UTC).strftime('%Y-%m-%d') if ts else ''
        rows.append(dict(channel=ch, title=e.get('title'), views=e['view_count'], url='https://youtu.be/' + e['id'],
                         duration=e.get('duration') or 0, date=date)); n += 1
    good += n >= 4
json.dump(rows, open(os.path.join(out_dir, 'collected.json'), 'w'))
print(f'{len(rows)} long-form videos from {good} channels (>=4 videos each). Failed channels: {failed or "none"}')
