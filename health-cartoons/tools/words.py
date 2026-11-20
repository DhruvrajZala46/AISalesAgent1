"""Word timings for every processed voice line -> words.json (used for captions, lip-sync events and SFX sync).
Usage: python3 -I tools/words.py <proc_dir> <out_json>   (needs: pip install faster-whisper)"""
import sys, glob, json, subprocess, numpy as np
from faster_whisper import WhisperModel
proc, out = sys.argv[1], sys.argv[2]
m = WhisperModel('small', device='cpu', compute_type='int8'); W = {}
for p in sorted(glob.glob(proc + '/*.wav')):
    a = np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
    segs, _ = m.transcribe(a, language='en', word_timestamps=True)
    W[p.split('/')[-1][:-4]] = [(round(w.start,2), round(w.end,2), w.word.strip()) for s in segs for w in s.words]
    print(p.split('/')[-1], '|', ' '.join(w[2] for w in W[p.split('/')[-1][:-4]]))
json.dump(W, open(out, 'w'))
