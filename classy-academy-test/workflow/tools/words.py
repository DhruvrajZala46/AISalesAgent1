# words.py - word-level timing of every voice line, so each picture lands on the word it shows.
# usage (inside the video work folder, after the voice is made): python3 words.py <model_dir>
#   -> words.json {"12": [["Fit", 0.0, 0.21], ...]} (seconds from the start of line 12)
# build.py then offers at(12, "navy blazer") = the moment "navy blazer" starts in line 12.
# needs: pip install faster-whisper (the base.en model, ~150 MB, downloads once into <model_dir>)
import os, sys, re, json, difflib
import numpy as np, soundfile as sf
from faster_whisper import WhisperModel

P = os.getcwd(); OUT = os.path.join(P, 'words.json')
beats = [l.strip() for l in open(os.path.join(P, 'beats.txt')) if l.strip()]
model = WhisperModel('base.en', device='cpu', compute_type='int8', download_root=sys.argv[1] if len(sys.argv) > 1 else None)
norm = lambda w: re.sub(r'[^a-z0-9]', '', w.lower().replace('colour', 'color').replace('grey', 'gray').replace('jewellery', 'jewelry'))
res = json.load(open(OUT)) if os.path.exists(OUT) else {}
for i, b in enumerate(beats, 1):
    if str(i) in res: continue
    y, sr = sf.read(os.path.join(P, 'tts', f'c{i:03d}.wav')); y = y.mean(1) if y.ndim > 1 else y
    n = int(len(y) * 16000 / sr); y16 = np.interp(np.linspace(0, len(y) - 1, n), np.arange(len(y)), y).astype(np.float32)
    heard = [(w.word.strip(), w.start, w.end) for s in model.transcribe(y16, word_timestamps=True, language='en')[0] for w in s.words]
    # map the script's own words onto the heard words (the script spelling wins; numbers like "8" match "eight")
    script = b.split(); a = [norm(w) for w in script]; h = [norm(w[0]) for w in heard]
    t = [None] * len(script)
    for blk in difflib.SequenceMatcher(None, a, h, autojunk=False).get_matching_blocks():
        for k in range(blk.size): t[blk.a + k] = heard[blk.b + k][1:]
    dur = len(y) / sr; known = [k for k in range(len(t)) if t[k]]
    for k in range(len(t)):   # words the model misheard: spread them between their matched neighbours
        if t[k]: continue
        lo = max([j for j in known if j < k], default=None); hi = min([j for j in known if j > k], default=None)
        s0 = t[lo][1] if lo is not None else 0.0; s1 = t[hi][0] if hi is not None else dur
        gap_n = (hi if hi is not None else len(t)) - (lo if lo is not None else -1)
        pos = k - (lo if lo is not None else -1); seg = (s1 - s0) / gap_n
        t[k] = (s0 + seg * (pos - 1), s0 + seg * pos)
    res[str(i)] = [[w, round(x[0], 2), round(x[1], 2)] for w, x in zip(script, t)]
    print(i, f'{len(known)}/{len(script)} words matched', flush=True)
    json.dump(res, open(OUT, 'w'), indent=0)
