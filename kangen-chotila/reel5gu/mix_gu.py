# mix_gu.py -> assets/mix.wav : voice + ONE continuous music bed (ducked under the voice, rises in pauses) + sfx, -14 LUFS
import json, subprocess, sys
J = json.load(open('sfx.json')); SFX = J['sfx']; DUR = J['dur']
TRACK, OFF, GAIN = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])     # e.g. m168 6.0 -9
inp = ['-i', 'assets/voice.wav', '-i', f'assets/{TRACK}.mp3']
flt = ['[0:a]aresample=48000,aformat=channel_layouts=stereo,asplit=2[v][vsc]',
       f'[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim={OFF}:{OFF + DUR},asetpts=PTS-STARTPTS,afade=t=in:d=0.4,afade=t=out:st={DUR - 2.5}:d=2.5,volume={GAIN}dB[mraw]',
       '[mraw][vsc]sidechaincompress=threshold=0.03:ratio=3:attack=30:release=400:makeup=1[m]']
labs = ['[v]', '[m]']
for k, (t, f, g) in enumerate(SFX):
    j = len(inp) // 2; inp += ['-i', f'assets/{f}.mp3']
    flt.append(f'[{j}:a]aresample=48000,aformat=channel_layouts=stereo,volume={g}dB,adelay={int(t * 1000)}|{int(t * 1000)}[s{k}]'); labs.append(f'[s{k}]')
flt.append(f'{"".join(labs)}amix=inputs={len(labs)}:normalize=0:duration=first,atrim=0:{DUR},loudnorm=I=-14:TP=-1.0:LRA=9[out]')
subprocess.run(['ffmpeg', '-y', '-v', 'error', *inp, '-filter_complex', ';'.join(flt), '-map', '[out]', '-ar', '48000', 'assets/mix.wav'], check=True)
print('mix ok')
