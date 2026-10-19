# sound_study.py - separates voice and music (Demucs) in each of the channel's videos and measures the mix
#   python3 -I sound_study.py <id> [<id> ...]   -> study/<id>/sound.json
import sys, os, json, subprocess, re
import numpy as np
def lufs(path, extra=''):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', path, '-af', 'ebur128' + extra, '-f', 'null', '-'], capture_output=True, text=True).stderr
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', r); return float(m[-1]) if m else None
for vid in sys.argv[1:]:
    O = f'study/{vid}'; os.makedirs(O, exist_ok=True)
    if os.path.exists(f'{O}/sound.json'): continue
    wav = f'{O}/mix.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'vid/{vid}.mp4', '-ac', '2', '-ar', '44100', wav], check=True)
    subprocess.run(['python3', '-m', 'demucs', '--two-stems', 'vocals', '-n', 'htdemucs', '-j', '4', '-o', f'{O}/sep', wav], capture_output=True)
    v = f'{O}/sep/htdemucs/mix/vocals.wav'; m = f'{O}/sep/htdemucs/mix/no_vocals.wav'
    res = dict(id=vid, mix_lufs=lufs(wav), voice_lufs=lufs(v), music_lufs=lufs(m))
    if res['voice_lufs'] and res['music_lufs']: res['music_under_voice_db'] = round(res['voice_lufs'] - res['music_lufs'], 1)
    # music presence and steadiness per second; sound-effect candidates = sharp transients in the music stem
    pcm = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', m, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    n = len(pcm) // 1600; db = 20 * np.log10(np.sqrt((pcm[:n * 1600].reshape(n, 1600) ** 2).mean(1)) + 1e-9)
    sec = [round(float(db[k:k + 10].mean()), 1) for k in range(0, n, 10)]
    on = [i for i, x in enumerate(sec) if x > -45]
    res.update(music_starts=on[0] if on else None, music_ends=on[-1] if on else None, music_db_per_sec=sec,
               music_db_spread=round(float(np.percentile([x for x in sec if x > -60] or [0], 90) - np.percentile([x for x in sec if x > -60] or [0], 10)), 1))
    jumps = [round(k / 10, 1) for k in range(2, n) if db[k] > db[k - 2] + 14 and db[k] > -35]
    res['transients_in_music'] = jumps[:30]
    # voice: when it starts and ends, speech rate
    vp = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', v, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    vn = len(vp) // 1600; vdb = 20 * np.log10(np.sqrt((vp[:vn * 1600].reshape(vn, 1600) ** 2).mean(1)) + 1e-9)
    von = [k / 10 for k in range(vn) if vdb[k] > -40]
    res.update(voice_starts=von[0] if von else None, voice_ends=von[-1] if von else None)
    if res.get('music_ends') is not None and von: res['music_tail_after_last_word_s'] = round(res['music_ends'] - von[-1], 1)
    json.dump(res, open(f'{O}/sound.json', 'w'))
    for f in (wav, v, m):
        try: os.remove(f)
        except OSError: pass
    print(json.dumps({k: v for k, v in res.items() if k != 'music_db_per_sec'}), flush=True)
