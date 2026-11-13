# mix.py -> assets/mix.wav : voice + two music beds (tense -> hopeful, with a silence on the emotional line) + sfx, -14 LUFS
import json, subprocess
J = json.load(open('sfx.json')); SFX = J['sfx']; DUR = J['dur']
inp = ['-i', 'assets/voice.wav']; flt = ['[0:a]aresample=48000,aformat=channel_layouts=stereo[v]']; labs = ['[v]']
for k, (name, off, t0, t1, g) in enumerate(J['music']):
    j = len(inp) // 2; inp += ['-i', f'assets/{name}.mp3']; L = t1 - t0
    flt.append(f'[{j}:a]aresample=48000,aformat=channel_layouts=stereo,atrim={off}:{off + L},asetpts=PTS-STARTPTS,'
               f'afade=t=in:d={1.2 if k else 0.8},afade=t=out:st={L - (0.6 if k == 0 else 2.0)}:d={0.6 if k == 0 else 2.0},volume={g}dB,adelay={int(t0 * 1000)}|{int(t0 * 1000)}[m{k}]')
    labs.append(f'[m{k}]')
for k, (t, f, g) in enumerate(SFX):
    j = len(inp) // 2; inp += ['-i', f'assets/{f}.mp3']
    flt.append(f'[{j}:a]aresample=48000,aformat=channel_layouts=stereo,volume={g}dB,adelay={int(t * 1000)}|{int(t * 1000)}[s{k}]'); labs.append(f'[s{k}]')
flt.append(f'{"".join(labs)}amix=inputs={len(labs)}:normalize=0:duration=first,atrim=0:{DUR},loudnorm=I=-14:TP=-1.0:LRA=9[out]')
subprocess.run(['ffmpeg', '-y', '-v', 'error', *inp, '-filter_complex', ';'.join(flt), '-map', '[out]', '-ar', '48000', 'assets/mix.wav'], check=True)
print('mix ok')
