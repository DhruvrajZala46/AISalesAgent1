from faster_whisper import WhisperModel
import json
m=WhisperModel('small.en',device='cpu',compute_type='int8')
import soundfile as sf, numpy as np
a,sr=sf.read('voice.wav',dtype='float32')
from scipy.signal import resample_poly
a=resample_poly(a,2,3).astype(np.float32)
segs,_=m.transcribe(a,word_timestamps=True,beam_size=5,vad_filter=False)
W=[]
for s in segs:
    for w in s.words: W.append({'w':w.word.strip(),'s':round(w.start,3),'e':round(w.end,3)})
json.dump(W,open('words.json','w'))
print(len(W),'words')
