# music: CC0 Chopin nocturnes (Musopen), steady bed ~12 dB under voice measured over speech; fade in with first word, out over the end card
import subprocess, json, numpy as np, soundfile as sf
B = json.load(open('beats.json')); DUR = B['duration']; t0 = B['beats'][0]['s'] - 1.0
SR = 48000
def load(f):
    raw = subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.float32).reshape(-1,2).copy()
m = np.concatenate([load('music/NocturneOp.55no.2inEflatmajor.mp3'), load('music/NocturneOp.72No.1InEMinor.mp3')])
v,_ = sf.read('voice.wav', dtype='float32'); 
v = subprocess.run(['ffmpeg','-v','error','-i','voice.wav','-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
v = np.frombuffer(v,np.float32).reshape(-1,2).copy()
N = int(DUR*SR); v = np.pad(v,((0,max(0,N-len(v))),(0,0)))[:N]
mus = np.zeros((N,2),np.float32); a = int(t0*SR); L = min(len(m), N-a); mus[a:a+L] = m[:L]
# gentle compression of the bed so it stays steady (no ducking): even out with a slow RMS leveller
w = SR//2; rms = np.sqrt(np.convolve((mus**2).mean(1), np.ones(w*4)/(w*4), mode='same'))+1e-6
target = np.median(rms[a:a+L]); gain = np.clip(target/rms, 0.5, 2.5); mus *= gain[:,None]
# fades
fin = int(2.0*SR); mus[a:a+fin] *= np.linspace(0,1,fin)[:,None]
fo_s = int((DUR-5.0)*SR); mus[fo_s:] *= np.linspace(1,0,N-fo_s)[:,None]
def lufs_like(x): return 20*np.log10(np.sqrt((x**2).mean())+1e-9)
sp = np.zeros(N,bool)
for b in B['beats']: sp[int(b['s']*SR):int(b['e']*SR)] = True
vl = lufs_like(v[sp]); ml = lufs_like(mus[sp])
mus *= 10**((vl-12.5-ml)/20)
mix = v + mus
pk = np.abs(mix).max(); mix *= min(1.0, 0.89/pk)
sf.write('mix.wav', mix, SR)
print(f'voice rms {vl:.1f} dB, music under speech {lufs_like(mus[sp]):.1f} dB -> gap {vl-lufs_like(mus[sp]):.1f} dB; peak {np.abs(mix).max():.2f}')
