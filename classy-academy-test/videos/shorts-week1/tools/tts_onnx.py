# tts_onnx.py <lines.txt> <out_dir> [speed] - channel voice (Kokoro af_heart) one wav per line, prints durations
import sys, os, soundfile as sf
from kokoro_onnx import Kokoro
K=Kokoro("/root/.cache/hyperframes/tts/models/kokoro-v1.0.onnx","/root/.cache/hyperframes/tts/voices/voices-v1.0.bin")
src,out=sys.argv[1],sys.argv[2]; speed=float(sys.argv[3]) if len(sys.argv)>3 else 0.95
os.makedirs(out,exist_ok=True); lines=[l.strip() for l in open(src) if l.strip()]; tw=ts=0
for i,t in enumerate(lines,1):
    a,sr=K.create(t,voice="af_heart",speed=speed,lang="en-us"); f=f"{out}/v{i:02d}.wav"; sf.write(f,a,sr)
    d=len(a)/sr; tw+=len(t.split()); ts+=d; print(f"v{i:02d} {d:5.2f}s {t}")
print(f"TOTAL {ts:.1f}s {tw} words {tw/(ts/60):.0f} wpm")
