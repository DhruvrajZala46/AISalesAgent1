import json, os, subprocess
from concurrent.futures import ThreadPoolExecutor
cids = json.load(open('cids.json'))
def chan(cid):
    f = f'ch/{cid}.json'
    if os.path.exists(f) and os.path.getsize(f) > 500: return 1
    r = subprocess.run(['yt-dlp', '--flat-playlist', '-J', '--playlist-end', '60', f'https://www.youtube.com/channel/{cid}/videos'], capture_output=True, text=True)
    try:
        if len(json.loads(r.stdout).get('entries') or []) >= 1: open(f, 'w').write(r.stdout); return 1
    except Exception: pass
    return 0
with ThreadPoolExecutor(3) as ex: ok = sum(ex.map(chan, cids))
print('channels', ok, 'of', len(cids)); print('CHANS_DONE', flush=True)
