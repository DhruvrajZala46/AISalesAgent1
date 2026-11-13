# mix.py -> assets/mix.wav : voice + music bed (ducked, steady) + sfx, master -14 LUFS / -1 dBTP
import json, subprocess
SFX = json.load(open('sfx.json')); DUR = 93.57
inp = ['-i', 'assets/voice.wav', '-i', 'assets/m480.mp3']
flt = ['[0:a]aresample=48000,aformat=channel_layouts=stereo,volume=1.0[v]',
       f'[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{DUR},afade=t=in:d=0.6,afade=t=out:st={DUR-2.2}:d=2.2,volume=-23dB[m]']
labs = ['[v]', '[m]']
for k, (t, f, g) in enumerate(SFX):
    inp += ['-i', f'assets/{f}.mp3']; j = k + 2
    flt.append(f'[{j}:a]aresample=48000,aformat=channel_layouts=stereo,volume={g}dB,adelay={int(t*1000)}|{int(t*1000)}[s{k}]'); labs.append(f'[s{k}]')
flt.append(f'{"".join(labs)}amix=inputs={len(labs)}:normalize=0:duration=first,atrim=0:{DUR},loudnorm=I=-14:TP=-1.0:LRA=9[out]')
subprocess.run(['ffmpeg', '-y', '-v', 'error', *inp, '-filter_complex', ';'.join(flt), '-map', '[out]', '-ar', '48000', 'assets/mix.wav'], check=True)
print('mix ok')
