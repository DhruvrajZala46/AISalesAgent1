# sweep3.py: view-sorted YouTube search (top 50 per phrasing) for new concept families; public search pages only, 3 at a time.
import json, subprocess, time, os, datetime, sys
from concurrent.futures import ThreadPoolExecutor
F = json.load(open(sys.argv[1])); OUT = sys.argv[2]
out = json.load(open(OUT)) if os.path.exists(OUT) else {}
jobs = [(f, q) for f, qs in F.items() for q in qs if f'{f}|{q}' not in out]
def run(job):
    f, q = job
    u = 'https://www.youtube.com/results?search_query=' + q.replace(' ', '+') + '&sp=EgIIBQ%253D%253D'
    for a in range(2):
        r = subprocess.run(['timeout', '180', 'yt-dlp', '--flat-playlist', '-J', '--playlist-end', '50', '--extractor-args', 'youtubetab:approximate_date', u], capture_output=True, text=True)
        try:
            rows = []
            for e in json.loads(r.stdout).get('entries') or []:
                if not e or not e.get('id'): continue
                ts = e.get('timestamp')
                rows.append(dict(id=e['id'], title=e.get('title'), channel=e.get('channel'), channel_id=e.get('channel_id'), views=e.get('view_count'), duration=e.get('duration'),
                                 year_approx=datetime.datetime.fromtimestamp(ts, datetime.UTC).year if ts else None))
            out[f'{f}|{q}'] = dict(family=f, q=q, rows=rows); print(f, '|', q, len(rows), flush=True); return
        except Exception: time.sleep(30)
    print(f, '|', q, 'ERR', r.stderr[-160:].replace('\n', ' '), flush=True)
with ThreadPoolExecutor(3) as ex: list(ex.map(run, jobs))
json.dump(out, open(OUT, 'w'), ensure_ascii=False)
print('DONE', len(out))
