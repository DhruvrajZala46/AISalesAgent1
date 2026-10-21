# Latest <=60 uploads per channel (public flat listing, approximate dates) -> subscribers and median views of long uploads.
import json, subprocess, os, statistics as st, sys
from concurrent.futures import ThreadPoolExecutor
need = json.load(open(sys.argv[1])); os.makedirs('ch', exist_ok=True)
def f(cid):
    p = f'ch/{cid}.json'
    if os.path.exists(p): return
    r = subprocess.run(['timeout', '180', 'yt-dlp', '--flat-playlist', '-J', '--playlist-end', '60', '--extractor-args', 'youtubetab:approximate_date', f'https://www.youtube.com/channel/{cid}/videos'], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip(): open(p, 'w').write(r.stdout)
with ThreadPoolExecutor(4) as ex: list(ex.map(f, need))
print('DONE', len(os.listdir('ch')))
