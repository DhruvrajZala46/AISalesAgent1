import sys, numpy as np, librosa
for f in sys.argv[1:]:
    y, sr = librosa.load(f, sr=22050, mono=True)
    on = librosa.onset.onset_detect(y=y, sr=sr, units='time'); dur = len(y)/sr
    S = np.abs(librosa.stft(y))**2; fr = librosa.fft_frequencies(sr=sr)
    low = S[fr < 120].sum()/S.sum(); high = S[fr > 4000].sum()/S.sum()
    w = int(5*sr); lv = [10*np.log10(np.mean(y[i:i+w]**2)+1e-12) for i in range(0, len(y)-w, w)]
    lv = np.array(lv); act = lv[lv > lv.max()-40]
    tempo = librosa.beat.beat_track(y=y, sr=sr)[0]
    print(f"{f}: {dur:.0f}s onsets/s {len(on)/dur:.2f} low<120Hz {100*low:.1f}% high>4k {100*high:.1f}% 5s-level spread {act.max()-act.min():.1f} dB (p10-p90 {np.percentile(act,90)-np.percentile(act,10):.1f}) tempo {float(np.atleast_1d(tempo)[0]):.0f}")
