# Concept sweep: for each concept family, several phrasings, YouTube search sorted by VIEW COUNT (top 50), with approximate upload dates.
import json, subprocess, time, os, datetime
from concurrent.futures import ThreadPoolExecutor
F = {
 'K1 look older / younger (style)': ["fashion mistakes that make you look older", "style mistakes that age you", "clothes that make you look older", "how to dress to look younger", "outfits that make you look older", "what makes you look older", "makeup mistakes that make you look older", "hairstyles that make you look older", "things that age you instantly", "how to look younger with style", "fashion tips to look younger", "mistakes that make you look old"],
 'K2 look expensive / classy': ["how to look expensive on a budget", "how to look rich", "how to look classy on a budget", "how to always look expensive", "how to look elegant", "things that make you look expensive", "how to look classy and elegant", "how to look expensive"],
 'K3 styling mistakes (general)': ["styling mistakes", "outfit mistakes everyone makes", "how to make your outfits better", "fashion mistakes to avoid"],
 'K4 elegant / classy habits': ["habits of elegant women", "classy habits", "how to be elegant", "how to be a classy woman"],
 'K5 capsule / minimalist wardrobe': ["minimalist wardrobe", "how to build a capsule wardrobe"],
 'K6 never wear': ["things you should never wear", "what not to wear", "clothes you should stop wearing"],
}
out = json.load(open('ksweep.json')) if os.path.exists('ksweep.json') else {}
jobs = [(f, q) for f, qs in F.items() for q in qs if f'{f}|{q}' not in out]
def run(job):
    f, q = job
    u = 'https://www.youtube.com/results?search_query=' + q.replace(' ', '+') + '&sp=CAM%253D'
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
    print(f, '|', q, 'ERR', r.stderr[-100:].replace('\n', ' '), flush=True)
with ThreadPoolExecutor(3) as ex: list(ex.map(run, jobs))
json.dump(out, open('ksweep.json', 'w'), ensure_ascii=False)
print('DONE', len(out))
