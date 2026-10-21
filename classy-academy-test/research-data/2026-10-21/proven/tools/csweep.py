# Concept sweep: for each concept family, several phrasings, YouTube search sorted by VIEW COUNT (top 50), with approximate upload dates.
import json, subprocess, time, os, datetime
from concurrent.futures import ThreadPoolExecutor
F = {
 'look older (age-appearance mistakes)': ["mistakes that make you look older", "things that make you look older", "makeup mistakes that age you", "hair mistakes that make you look older", "clothes that make you look older"],
 'look younger': ["how to look younger", "how to dress to look younger", "look 10 years younger"],
 'look cheap': ["things that make you look cheap", "mistakes that make you look cheap", "outfits that look cheap"],
 'look expensive / rich / classy': ["how to look expensive", "how to look rich on a budget", "how to look classy", "how to look expensive on a budget"],
 'fashion / style mistakes (general)': ["fashion mistakes women make", "style mistakes", "common outfit mistakes"],
 'never wear / stop wearing': ["things you should never wear", "things classy women never wear", "stop wearing these clothes"],
 'classy habits / behaviour': ["habits of classy women", "how to be classy", "things classy women never do"],
 'capsule / wardrobe essentials': ["capsule wardrobe", "wardrobe essentials every woman needs", "timeless wardrobe essentials"],
 'body type / proportions': ["how to dress for your body type", "how to look taller", "how to look slimmer in clothes"],
 'colour analysis': ["color analysis", "colors that make you look younger", "best colors for your skin tone"],
 'glow up / more attractive': ["glow up tips", "how to be more attractive", "how to look prettier"],
 'feminine': ["how to be more feminine", "feminine energy"],
 'put together / polished (rejected)': ["how to always look put together", "how to look polished"],
 'hairstyles': ["elegant hairstyles", "easy hairstyles for women"],
 'etiquette': ["etiquette tips", "etiquette rules everyone should know"],
}
out = json.load(open('csweep.json')) if os.path.exists('csweep.json') else {}
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
json.dump(out, open('csweep.json', 'w'), ensure_ascii=False)
print('DONE', len(out))
