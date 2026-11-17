# shrink.py - re-encode every raw clip once to a moderate bitrate (same size, max 30 fps, no audio): Pinterest serves
# some 720p reels at 20 Mbps, which fills the disk and slows every later step. Keeps a list in shrunk.txt.
import os, subprocess, json
from concurrent.futures import ThreadPoolExecutor
done = set(open('shrunk.txt').read().split()) if os.path.exists('shrunk.txt') else set()
keys = sorted(f[:-4] for f in os.listdir('raw') if f.endswith('.mp4') and f[:-4] not in done)
def one(k):
    src = f'raw/{k}.mp4'; tmp = f'raw/{k}.tmp.mp4'
    try:
        pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate,color_transfer:format=duration,bit_rate', '-of', 'json', src], capture_output=True, text=True).stdout)
        br = float(pr['format'].get('bit_rate') or 0); tr = pr['streams'][0].get('color_transfer', '')
        if br < 2.6e6 or tr in ('arib-std-b67', 'smpte2084'): return k, 'kept'
        num, den = pr['streams'][0]['r_frame_rate'].split('/'); fps = float(num) / float(den)
        vf = 'fps=30,' if fps > 31 else ''
        r = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', src, '-an', '-vf', vf + 'scale=trunc(iw/2)*2:trunc(ih/2)*2', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', tmp], capture_output=True, text=True)
        if r.returncode == 0 and os.path.getsize(tmp) > 20000:
            os.replace(tmp, src); return k, 'shrunk'
        if os.path.exists(tmp): os.remove(os.path.abspath(tmp))
        return k, 'failed ' + r.stderr[:80]
    except Exception as e:
        return k, 'error ' + str(e)[:80]
n = 0
with ThreadPoolExecutor(6) as ex:
    for k, s in ex.map(one, keys):
        if s in ('kept', 'shrunk'): open('shrunk.txt', 'a').write(k + '\n')
        if s == 'shrunk': n += 1
        elif s != 'kept': print(k, s, flush=True)
print('SHRINKDONE', n, 'of', len(keys), flush=True)
