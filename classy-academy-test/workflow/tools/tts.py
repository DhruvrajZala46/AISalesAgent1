import kokoro_onnx, soundfile as sf, os
C='/root/.cache/hyperframes/tts/'
m=kokoro_onnx.Kokoro(C+'models/kokoro-v1.0.onnx',C+'voices/voices-v1.0.bin')
for n,line in enumerate(open('beats_tts.txt'),1):
    out=f'tts/c{n:03d}.wav'
    if os.path.exists(out) and os.path.getsize(out)>1000: continue
    s,sr=m.create(line.strip(),voice='af_heart',speed=0.80,lang='en-us'); sf.write(out,s,sr); print(n,flush=True)
print('TTSDONE')
