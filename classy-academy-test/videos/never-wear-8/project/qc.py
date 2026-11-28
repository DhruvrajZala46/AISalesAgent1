# qc.py VIDEO : duration, black frames, frozen stretches, loudness, silence in the audio bed
import sys, subprocess, re, json
v = sys.argv[1]
dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',v],capture_output=True,text=True).stdout)
print(f'duration {dur:.2f}s = {int(dur//60)}:{dur%60:05.2f}  ->', 'OK (6:00-7:00)' if 360 <= dur <= 420 else 'OUT OF RANGE')
r = subprocess.run(['ffmpeg','-v','info','-i',v,'-vf','blackdetect=d=0.25:pix_th=0.06,freezedetect=n=0.002:d=4','-an','-f','null','-'],capture_output=True,text=True).stderr
print('black:', re.findall(r'black_start:([\d.]+) black_end:([\d.]+)', r))
fz = re.findall(r'freeze_start: ([\d.]+)', r); fe = re.findall(r'freeze_end: ([\d.]+)', r)
print('freezes >4s:', list(zip(fz, fe)))
r = subprocess.run(['ffmpeg','-v','info','-i',v,'-vn','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
m = re.search(r'Integrated loudness:\s+I:\s+([-\d.]+) LUFS.*?True peak:\s+Peak:\s+([-\d.]+)', r, re.S)
print('loudness', m.group(1) if m else '?', 'LUFS, true peak', m.group(2) if m else '?')
r = subprocess.run(['ffmpeg','-v','info','-i',v,'-vn','-af','silencedetect=n=-50dB:d=1.5','-f','null','-'],capture_output=True,text=True).stderr
print('silences >1.5s below -50 dB:', re.findall(r'silence_start: ([\d.]+)', r))
