# mix.py - the sound of the video, as measured on the channel's 30 uploads (study/<id>/sound*.json):
#   a very soft bed ~20 dB under the voice (separated stems of the Hairstyles video: 15.7 dB; mix floor of the others ~20 dB),
#   starting with the first word (no music intro) and stopping with the last word; no ducking, no sound effects;
#   then 0.5 s of silence and the channel's own logo sting on the white end card, ~6.5 LU louder than the programme,
#   decaying to digital silence. Master -18 LUFS (median of the four most-viewed uploads: -16.6 to -19.3), true peak -1 dBTP.
#   python3 project/mix.py            -> audio/music_bed.wav, audio/mix.wav
#   python3 project/mix.py mux        -> out/<final>.mp4 (video_only.mp4 + mix.wav)
import json, os, re, subprocess, sys
P = os.path.dirname(os.path.abspath(__file__)); WD = os.path.dirname(P)
clock = json.load(open(f'{P}/clock.json')); TOTAL = clock['total']; last_word = clock['sentences'][-1]['end']
MUSIC = ['music/BerceuseinD-flatmajorOp.57.flac', 'music/NocturneinEflatmajorOp.9no.2.flac',
         'music/NocturnesOp.32-No.1.NocturneinBmajor.flac']          # Chopin, Musopen recordings, CC0
VOICE_LUFS = -18.0; UNDER = 20.0; MASTER = -18.0; STING_OVER = 6.5
END_CARD = clock.get('end_card', last_word + 0.5)
STING = 'assets/own/end_sting_MNEo.wav'   # cut from the channel's own upload MNEoQmJU96M (end card, 8:13.5-8:19.6)


def run(cmd): return subprocess.run(cmd, capture_output=True, text=True, check=True)


def loudness(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', path, '-af', 'loudnorm=print_format=json', '-f', 'null', '-'],
                       capture_output=True, text=True)
    j = json.loads(re.findall(r'\{[^{}]*\}', r.stderr, re.S)[-1]); return float(j['input_i']), float(j['input_tp'])


if len(sys.argv) > 1 and sys.argv[1] == 'mux':
    out = sys.argv[2] if len(sys.argv) > 2 else 'out/Why_Her_Hair_Always_Looks_Expensive.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{WD}/out/video_only.mp4', '-i', f'{WD}/audio/mix.wav', '-map', '0:v', '-map', '1:a',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-movflags', '+faststart', '-shortest', f'{WD}/{out}'], check=True)
    print('muxed', out); sys.exit()

os.makedirs(f'{WD}/audio', exist_ok=True)
# 1. music bed: the three pieces joined with 6 s crossfades, 48 kHz stereo, gently compressed so it sits steady
fc = ''.join(f'[{i}:a]aresample=48000:resampler=soxr,aformat=sample_fmts=fltp:channel_layouts=stereo[a{i}];' for i in range(len(MUSIC)))
fc += '[a0][a1]acrossfade=d=6:c1=tri:c2=tri[x1];[x1][a2]acrossfade=d=6:c1=tri:c2=tri[x2];'
bed_end = last_word + 0.3
fc += (f'[x2]atrim=0:{bed_end:.3f},asetpts=N/SR/TB,highpass=f=60,'
       f'acompressor=threshold=-28dB:ratio=3:attack=80:release=900:makeup=1,'
       f'afade=t=in:st=0:d=0.3,afade=t=out:st={bed_end - 1.2:.3f}:d=1.2,apad=whole_dur={TOTAL:.3f}[m]')
cmd = ['ffmpeg', '-v', 'error', '-y']
for m in MUSIC: cmd += ['-i', f'{WD}/{m}']
run(cmd + ['-filter_complex', fc, '-map', '[m]', f'{WD}/audio/music_raw.wav'])
# 2. levels: voice to -18 LUFS, music 20 LU under it (measured over the part under the voice)
vi, _ = loudness(f'{WD}/audio/voice.wav')
run(['ffmpeg', '-v', 'error', '-y', '-i', f'{WD}/audio/voice.wav', '-af', f'volume={VOICE_LUFS - vi:.2f}dB,aformat=channel_layouts=stereo',
     f'{WD}/audio/voice_lev.wav'])
mi, _ = loudness(f'{WD}/audio/music_raw.wav')
run(['ffmpeg', '-v', 'error', '-y', '-i', f'{WD}/audio/music_raw.wav', '-af', f'volume={VOICE_LUFS - UNDER - mi:.2f}dB',
     f'{WD}/audio/music_bed.wav'])
# 3. the channel's logo sting on the end card, STING_OVER LU above the voice
si, _ = loudness(f'{WD}/{STING}')
run(['ffmpeg', '-v', 'error', '-y', '-i', f'{WD}/{STING}', '-af', f'volume={VOICE_LUFS + STING_OVER - si:.2f}dB,adelay={int((END_CARD + 0.1) * 1000)}:all=1,'
     f'apad=whole_dur={TOTAL:.3f},atrim=0:{TOTAL:.3f}', '-ar', '48000', '-ac', '2', f'{WD}/audio/sting.wav'])
# 4. sum and master to MASTER LUFS integrated, true peak -1 dBTP (two-pass loudnorm, linear)
run(['ffmpeg', '-v', 'error', '-y', '-i', f'{WD}/audio/voice_lev.wav', '-i', f'{WD}/audio/music_bed.wav', '-i', f'{WD}/audio/sting.wav', '-filter_complex',
     '[0:a][1:a][2:a]amix=inputs=3:normalize=0:duration=longest,atrim=0:' + f'{TOTAL:.3f}[s]', '-map', '[s]', '-ar', '48000', f'{WD}/audio/sum.wav'])
r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', f'{WD}/audio/sum.wav', '-af', f'loudnorm=I={MASTER}:TP=-1:LRA=11:print_format=json',
                    '-f', 'null', '-'], capture_output=True, text=True)
j = json.loads(re.findall(r'\{[^{}]*\}', r.stderr, re.S)[-1])
ln = (f"loudnorm=I={MASTER}:TP=-1:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
      f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
run(['ffmpeg', '-v', 'error', '-y', '-i', f'{WD}/audio/sum.wav', '-af', ln, '-ar', '48000', '-c:a', 'pcm_s24le', f'{WD}/audio/mix.wav'])
fi, ft = loudness(f'{WD}/audio/mix.wav')
vm, _ = loudness(f'{WD}/audio/voice_lev.wav'); mm, _ = loudness(f'{WD}/audio/music_bed.wav')
print(json.dumps(dict(voice_lufs=round(vm, 1), music_lufs=round(mm, 1), music_under_voice_db=round(vm - mm, 1),
                      master_lufs=round(fi, 1), master_true_peak=round(ft, 1), duration=TOTAL)))
