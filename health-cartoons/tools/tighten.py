"""Shorten long pauses inside each voice line (dialogue edit), like the reference's tight delivery.
usage: python3 -I tools/tighten.py proc [max_pause_s] [keep_list]   (rewrites proc/*.wav in place)
Pauses longer than max_pause (default 0.30 s, below -38 dB) are cut down to max_pause; 'keep' lines (comma list of NN) are skipped."""
import sys,glob,subprocess,re,numpy as np,wave
d=sys.argv[1]; mx=float(sys.argv[2]) if len(sys.argv)>2 else .30; keep=set(sys.argv[3].split(',')) if len(sys.argv)>3 else set()
for f in sorted(glob.glob(d+'/*.wav')):
    nn=f.split('/')[-1][:2]
    if nn in keep: continue
    with wave.open(f) as w: sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)
    win=int(sr*.01); n=len(x)//win; e=np.array([np.sqrt(np.mean(x[i*win:(i+1)*win]**2))+1e-6 for i in range(n)]); db=20*np.log10(e/32768)
    sil=db<-38; out=[]; i=0; cut=0
    while i<n:
        if sil[i]:
            j=i
            while j<n and sil[j]: j+=1
            L=(j-i)*win
            if i>0 and j<n and L>mx*sr:
                k=int(mx*sr/2); out.append(x[i*win:i*win+k]); out.append(x[j*win-k:j*win]); cut+=L-2*k
            else: out.append(x[i*win:j*win])
            i=j
        else:
            j=i
            while j<n and not sil[j]: j+=1
            out.append(x[i*win:j*win]); i=j
    out.append(x[n*win:]); y=np.concatenate(out).astype(np.int16)
    with wave.open(f,'w') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(y.tobytes())
    print(f.split('/')[-1], 'cut %.2fs -> %.2fs'%(cut/sr,len(y)/sr))
