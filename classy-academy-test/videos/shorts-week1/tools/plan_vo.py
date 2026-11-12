# plan_vo.py plan.json -> voice track + full spec (segments and text timed to each spoken line)
import json, sys, os, subprocess, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
P=json.load(open(sys.argv[1])); name=P["name"]; speed=P.get("speed",0.9); gap=P.get("gap",0.3); lead=P.get("lead",0.15)
K=Kokoro("/root/.cache/hyperframes/tts/models/kokoro-v1.0.onnx","/root/.cache/hyperframes/tts/voices/voices-v1.0.bin")
os.makedirs(f"tts/{name}",exist_ok=True)
t=lead; voice=[np.zeros(int(lead*24000),dtype=np.float32)]; segs=[]; texts=[]
for i,L in enumerate(P["lines"]):
    if L.get("say"):
        a,sr=K.create(L["say"],voice="af_heart",speed=speed,lang="en-us"); a=a.astype(np.float32); d=len(a)/sr
    else: a=np.zeros(0,dtype=np.float32); d=0
    dur=max(d+gap, L.get("min",0)); pad=int((dur-d)*24000)
    voice+= [a, np.zeros(pad,dtype=np.float32)]
    shots=L["shots"]; wsum=sum(s.get("w",1) for s in shots); acc=0
    for s in shots:
        sd=round(dur*s.get("w",1)/wsum,3)
        seg={k:v for k,v in s.items() if k not in ("w",)}; seg["dur"]=sd; segs.append(seg); acc+=sd
    for x in L.get("screen",[]):
        texts.append({**x,"a":round(t if i>0 else 0,3),"b":round(t+dur,3)})
    print(f"{i:2d} {t:5.2f}-{t+dur:5.2f}  {d:4.2f}s  {L.get('say','(music)')}")
    t+=dur
segs[0]["dur"]=round(segs[0]["dur"]+lead,3)
wav=np.concatenate(voice); sf.write(f"tts/{name}/voice.wav",wav,24000)
spec={"name":name,"segs":segs,"texts":texts,"music":P["music"],"voice":{"file":f"tts/{name}/voice.wav","gain":P.get("voice_gain",2)},
      "check":[round(x,1) for x in np.linspace(0.2,t-0.3,8)]}
json.dump(spec,open(f"{name}.json","w"),indent=1); print("TOTAL",round(t,2),"s")
