# get_scripts.py out_dir id1 id2 ... -> <id>.txt transcripts (Hindi auto/orig captions) slowly, with the user's cookies
import sys, os, subprocess, time, glob, json, random
sys.path.insert(0, os.path.dirname(__file__)); from vtt2txt import clean
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
CK = '/tmp/claude-0/-home-user-AISalesAgent1/6a304440-e6c6-51d4-84cb-2bb7e64aeb34/scratchpad/secret/yt_cookies.txt'
for vid in sys.argv[2:]:
    if os.path.exists(f'{OUT}/{vid}.txt'): continue
    r = subprocess.run(['yt-dlp', '--js-runtimes', 'node', '--cookies', CK, '--skip-download', '--ignore-no-formats-error', '--write-auto-subs', '--write-subs',
                        '--sub-langs', 'hi-orig,hi,en-orig,en', '--sub-format', 'vtt', '--write-info-json', '-o', f'{OUT}/%(id)s', f'https://www.youtube.com/shorts/{vid}'],
                       capture_output=True, text=True, timeout=180)
    if 'Sign in to confirm' in r.stderr: print('BLOCKED', vid, flush=True); break
    fs = sorted(glob.glob(f'{OUT}/{vid}.hi-orig.vtt')) or sorted(glob.glob(f'{OUT}/{vid}.hi.vtt')) or sorted(glob.glob(f'{OUT}/{vid}.en*.vtt'))
    txt = clean(fs[0]) if fs else ''
    info = {}
    if os.path.exists(f'{OUT}/{vid}.info.json'):
        j = json.load(open(f'{OUT}/{vid}.info.json')); info = dict(title=j.get('title'), views=j.get('view_count'), likes=j.get('like_count'), dur=j.get('duration'), ch=j.get('channel'), subs=j.get('channel_follower_count'), date=j.get('upload_date'))
        os.remove(f'{OUT}/{vid}.info.json')
    open(f'{OUT}/{vid}.txt', 'w').write(json.dumps(info, ensure_ascii=False) + '\n' + txt)
    print('ok', vid, info.get('views'), len(txt.split()), 'words', flush=True)
    time.sleep(random.uniform(4, 8))
