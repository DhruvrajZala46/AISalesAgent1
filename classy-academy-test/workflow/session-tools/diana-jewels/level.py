# level.py in out: even a piano bed's loudness (3 s RMS windows, smoothed gain, limited to +-9 dB)
import sys, numpy as np, soundfile as sf, subprocess
src, dst = sys.argv[1], sys.argv[2]
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i',src,'-ac','2','-ar','44100','/tmp/_lv.wav'],check=True)
y, sr = sf.read('/tmp/_lv.wav'); mono = y.mean(1)
w = int(sr*3); hop = int(sr*0.5)
c = np.arange(0, len(mono), hop); rms = np.array([np.sqrt((mono[max(0,i-w//2):i+w//2]**2).mean()+1e-12) for i in c])
db = 20*np.log10(rms); act = db > db.max()-45; tgt = np.median(db[act])
g = np.clip(tgt-db, -9, 9); g[~act] = 0
k = 9; g = np.convolve(g, np.ones(k)/k, mode='same')
gain = 10**(np.interp(np.arange(len(mono)), c, g)/20)
out = y*gain[:,None]; out /= max(1, np.abs(out).max()/0.95)
sf.write('/tmp/_lv2.wav', out, sr)
subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-i','/tmp/_lv2.wav','-b:a','192k',dst],check=True)
