# Stage 1 screen: broad public YouTube search sweep across the niche and adjacent categories.
# Two passes per query: relevance (ytsearch50, all-time) and the "this year" upload filter. No login, no cookies.
import json, subprocess, time, os, sys
Q = {
 'elegant/classy': ["things elegant women never wear", "how to look elegant", "elegant women habits", "classy lady tips", "how to be classy", "signs of an elegant woman", "elegant woman secrets", "how to be a lady", "things elegant ladies never do"],
 'old money/timeless': ["old money style women", "old money outfits", "timeless wardrobe essentials women", "classic capsule wardrobe", "quiet luxury style women", "how to look rich", "how to look expensive on a budget", "outfits that look expensive"],
 'mistakes/instead': ["outfit mistakes that cheapen your look", "fashion mistakes women make", "style mistakes that make you look older", "what not to wear women", "stop wearing these"],
 'grooming/hair/beauty': ["elegant hairstyles", "how to look polished every day", "grooming habits women", "makeup that looks expensive", "elegant natural makeup", "nails that look expensive", "perfume elegant women", "glow up tips women", "hairstyles that make you look younger", "fine thin hair"],
 'feminine/luxury': ["how to be more feminine", "feminine style tips", "how to wear jewelry elegantly", "timeless handbags", "understated luxury", "colors that look expensive", "color combinations outfits elegant"],
 'social grace': ["etiquette tips for women", "modern etiquette", "how to be more confident woman", "elegant body language", "how to speak elegantly", "how to be charming", "how to be magnetic woman", "how to command respect", "high value woman habits"],
 'transformation': ["style transformation women", "makeover over 50", "before and after style makeover", "how to elevate your style", "personal stylist tips"],
 'adjacent': ["french women style secrets", "italian women style", "parisian chic", "style over 50", "style over 60", "dress for your body type", "how to dress for your age", "color analysis", "elegant fall outfits", "elegant winter outfits", "elegant shoes women", "how to walk elegantly", "how to pose in photos", "self care routine elegant woman", "home that looks expensive", "hosting etiquette", "wardrobe declutter", "petite style tips", "how to look put together", "jeans outfits elegant"],
}
out = json.load(open('sweep.json')) if os.path.exists('sweep.json') else {}
YEAR = '&sp=EgIIBQ%253D%253D'
jobs = [(cat, q, mode) for cat, qs in Q.items() for q in qs for mode in ('rel', 'year')]
from concurrent.futures import ThreadPoolExecutor
def run(job):
    cat, q, mode = job; key = f'{q}|{mode}'; t0 = time.time()
    src = f'ytsearch50:{q}' if mode == 'rel' else 'https://www.youtube.com/results?search_query=' + q.replace(' ', '+') + YEAR
    for attempt in range(2):
        r = subprocess.run(['timeout', '180', 'yt-dlp', '--flat-playlist', '-J', '--playlist-end', '50', src], capture_output=True, text=True)
        try:
            ents = json.loads(r.stdout).get('entries') or []
            out[key] = dict(cat=cat, q=q, mode=mode, rows=[dict(id=e['id'], title=e.get('title'), channel=e.get('channel'), channel_id=e.get('channel_id'), views=e.get('view_count'), duration=e.get('duration')) for e in ents if e and e.get('id') and e.get('ie_key', 'Youtube') == 'Youtube'])
            break
        except Exception:
            time.sleep(60)
    print(key, len(out[key]['rows']) if key in out else 'ERR ' + r.stderr[-100:].replace('\n', ' '), round(time.time() - t0), 's', flush=True)
    time.sleep(2)
todo = [j for j in jobs if f'{j[1]}|{j[2]}' not in out]
print(len(todo), 'jobs to run', flush=True)
with ThreadPoolExecutor(4) as ex:
    for n, _ in enumerate(ex.map(run, todo)):
        if n % 5 == 0: json.dump(dict(out), open('sweep.json', 'w'), ensure_ascii=False)
json.dump(out, open('sweep.json', 'w'), ensure_ascii=False)
print('DONE')
