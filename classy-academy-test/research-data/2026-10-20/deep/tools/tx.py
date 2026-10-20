# English auto-captions (or manual) for a list of videos -> plain text with [mm:ss] markers. Public, no login. Spaced for rate limits.
import json, subprocess, sys, time, os, glob, re
ids = json.load(open(sys.argv[1])); gap = int(sys.argv[2]) if len(sys.argv) > 2 else 60
fails = 0
for vid in ids:
    if fails >= 2: print('STOP: refused twice in a row, leaving YouTube alone', flush=True); break
    if os.path.exists(f'tx/{vid}.txt'): continue
    for attempt in range(2):
        r = subprocess.run(['timeout', '120', 'yt-dlp', '--skip-download', '--write-subs', '--write-auto-subs', '--sub-langs', 'en.*,en', '--sub-format', 'json3', '--no-warnings', '-o', f'tx/{vid}.%(ext)s', f'https://www.youtube.com/watch?v={vid}'], capture_output=True, text=True)
        fs = sorted(glob.glob(f'tx/{vid}*.json3'), key=lambda f: ('orig' not in f, f))
        if fs: break
        print(vid, 'retry', r.stderr[-120:].replace('\n', ' '), flush=True); time.sleep(120)
    if not fs: print(vid, 'NO CAPTIONS', flush=True); fails += 1; continue
    fails = 0
    d = json.load(open(fs[0])); out, last = [], -30
    for ev in d.get('events', []):
        t = ev.get('tStartMs', 0) / 1000; s = ''.join(x.get('utf8', '') for x in ev.get('segs') or []).replace('\n', ' ').strip()
        if not s: continue
        if t - last >= 30: out.append(f'\n[{int(t//60):02d}:{int(t%60):02d}] '); last = t
        out.append(s + ' ')
    open(f'tx/{vid}.txt', 'w').write(re.sub(' +', ' ', ''.join(out)).strip())
    print(vid, 'ok', len(open(f'tx/{vid}.txt').read().split()), 'words', flush=True)
    time.sleep(gap)
print('DONE')
