# sound_quick.py - fast sound measurements for every video (no separation):
#   music alone before the first word and after the last word, the floor between words (music under the voice),
#   voice level, loudness, sudden transients in the pauses (sound-effect candidates), how the music ends.
#   python3 -I sound_quick.py <id> ...  -> study/<id>/sound_quick.json ; prints one line per video
import sys, json, subprocess, re
import numpy as np
def lufs(path, ss=None, t=None):
    a = ['ffmpeg', '-hide_banner', '-nostats'] + (['-ss', str(ss)] if ss is not None else []) + (['-t', str(t)] if t else []) + ['-i', path, '-af', 'ebur128', '-f', 'null', '-']
    r = subprocess.run(a, capture_output=True, text=True).stderr
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', r); return float(m[-1]) if m else None
for vid in sys.argv[1:]:
    V = f'vid/{vid}.mp4'
    pcm = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', V, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    B = 800; n = len(pcm) // B; db = 20 * np.log10(np.sqrt((pcm[:n * B].reshape(n, B) ** 2).mean(1)) + 1e-9)   # 50 ms blocks
    t = lambda k: round(k * B / 16000, 2)
    # speech = the caption word times
    words = []
    for e in json.load(open(f'vid/{vid}.en.json3')).get('events', []):
        for s in e.get('segs') or []:
            if s.get('utf8', '').strip(): words.append((e['tStartMs'] + s.get('tOffsetMs', 0)) / 1000)
    w0, w1 = (min(words), max(words)) if words else (0, len(pcm) / 16000)
    k0, k1 = int(w0 * 20), int(w1 * 20)
    mid = db[k0:k1]; mid = mid[mid > -70]
    res = dict(id=vid, duration=round(len(pcm) / 16000, 1), first_word=round(w0, 2), last_word=round(w1, 2),
               lufs_total=lufs(V), voice_p90_db=round(float(np.percentile(mid, 90)), 1),
               floor_between_words_p5_db=round(float(np.percentile(mid, 5)), 1), floor_p15_db=round(float(np.percentile(mid, 15)), 1))
    # audio before the first word / after the last word
    pre = db[:max(1, k0 - 4)]; post = db[k1 + 30:]
    res['before_first_word'] = dict(sec=round(w0, 2), mean_db=round(float(pre.mean()), 1) if len(pre) else None, silent=bool(len(pre) and pre.max() < -55))
    res['after_last_word'] = dict(sec=round(len(pcm) / 16000 - w1, 1), mean_db=round(float(post.mean()), 1) if len(post) > 4 else None)
    if len(post) > 20:
        on = np.where(post > -50)[0]; res['after_last_word']['audible_for_s'] = round(len(on) * B / 16000, 1) if len(on) else 0
        q = post[:len(post) // 4 * 4].reshape(4, -1).mean(1); res['after_last_word']['quarters_db'] = [round(float(x), 1) for x in q]
    # loudness of the music alone at the start and end (if long enough)
    if w0 > 2.5: res['music_alone_start_lufs'] = lufs(V, 0, w0 - 0.3)
    if res['after_last_word']['sec'] > 3: res['music_alone_end_lufs'] = lufs(V, w1 + 1.2)
    res['voice_lufs_est'] = lufs(V, w0, w1 - w0)
    # sudden transients far above the local floor (sound-effect candidates)
    loc = np.convolve(db, np.ones(40) / 40, 'same')
    res['transients'] = [t(k) for k in range(2, n) if db[k] > loc[k] + 15 and db[k] > db[k - 2] + 18][:30]
    json.dump(res, open(f'study/{vid}/sound_quick.json', 'w'), indent=1)
    print(json.dumps(res), flush=True)
