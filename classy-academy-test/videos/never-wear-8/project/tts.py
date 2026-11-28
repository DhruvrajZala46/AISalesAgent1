import sys,os,soundfile as sf,numpy as np
from kokoro_onnx import Kokoro
speed=float(sys.argv[1]); voice=sys.argv[2] if len(sys.argv)>2 else 'af_heart'
fix={}
k=Kokoro('/root/.cache/hyperframes/tts/models/kokoro-v1.0.onnx','/root/.cache/hyperframes/tts/voices/voices-v1.0.bin')
os.makedirs('tts',exist_ok=True); tot=0; words=0
for l in open('beats.txt'):
    if not l.strip(): continue
    key,t=l.strip().split('|',1); words+=len(t.split())
    for a,b in fix.items(): t=t.replace(a,b)
    f=f'tts/{key}.wav'
    if not os.path.exists(f):
        s,sr=k.create(t,voice=voice,speed=speed,lang='en-us'); sf.write(f,s,sr)
    d=sf.info(f).duration; tot+=d
print(f'speech {tot:.1f}s {tot/60:.2f} min, {words} words, {words/(tot/60):.0f} wpm raw')
