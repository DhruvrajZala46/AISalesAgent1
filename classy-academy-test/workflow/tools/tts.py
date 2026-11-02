# tts.py - Kokoro-82M voice generator (af_heart, calibrated speed)
# usage: python3 tts.py <beats.txt> <out_dir> [speed]
#   reads one spoken paragraph per non-empty line, writes c001.wav, c002.wav, ... (24 kHz mono)
import sys, os, json, soundfile as sf
from kokoro import KPipeline

beats_file, out_dir = sys.argv[1], sys.argv[2]
speed = float(sys.argv[3]) if len(sys.argv) > 3 else float(os.environ.get('KOKORO_SPEED', '0.88'))
os.makedirs(out_dir, exist_ok=True)
pipe = KPipeline(lang_code='a')
lines = [l.strip() for l in open(beats_file) if l.strip()]
total_s = 0.0
total_w = 0
for i, text in enumerate(lines, 1):
    out = os.path.join(out_dir, f'c{i:03d}.wav')
    w_cnt = len(text.split())
    total_w += w_cnt
    if os.path.exists(out):
        info = sf.info(out)
        total_s += info.duration
        continue
    audio = [a for _, _, a in pipe(text, voice='af_heart', speed=speed)]
    import numpy as np
    wav = np.concatenate(audio)
    sf.write(out, wav, 24000)
    dur = len(wav) / 24000
    total_s += dur
    print(f'c{i:03d}.wav  ({dur:.1f}s)  {text[:60]}', flush=True)
print(f'TTS SUMMARY: speed={speed:.2f}, total_words={total_w}, speech_duration={total_s:.1f}s ({total_s/60:.2f}m), spoken_WPM={total_w/(total_s/60):.1f}', flush=True)
