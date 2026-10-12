import subprocess, sys, re, json, os
f = sys.argv[1]; P = os.path.dirname(os.path.abspath(__file__))
def run(c): return subprocess.run(c, shell=True, capture_output=True, text=True)
pr = json.loads(run(f'ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,sample_rate,channels:format=duration,size -of json "{f}"').stdout)
print('PROBE', json.dumps(pr))
# black frames (>0.3 s)
o = run(f'ffmpeg -nostdin -i "{f}" -vf "blackdetect=d=0.3:pix_th=0.08" -an -f null - 2>&1').stdout + run(f'ffmpeg -nostdin -i "{f}" -vf "blackdetect=d=0.3:pix_th=0.08" -an -f null -').stderr
bl = re.findall(r'black_start:([\d.]+) black_end:([\d.]+)', o); print('BLACK', bl)
# frozen picture (>1.2 s with almost no change)
o = run(f'ffmpeg -nostdin -i "{f}" -vf "scale=480:-2,freezedetect=n=0.002:d=1.2" -an -f null -').stderr
fr = re.findall(r'freeze_start: ([\d.]+).*?freeze_duration: ([\d.]+)', o, re.S); print('FREEZE', fr)
# audio: loudness + silence (music must never drop out)
o = run(f'ffmpeg -nostdin -i "{f}" -af ebur128 -f null -').stderr
print('LOUD', re.findall(r'I:\s+(-?[\d.]+) LUFS', o)[-1:], re.findall(r'Peak:\s+(-?[\d.]+)', o)[-1:])
o = run(f'ffmpeg -nostdin -i "{f}" -af silencedetect=n=-45dB:d=1.0 -f null -').stderr
print('SILENCE', re.findall(r'silence_start: ([\d.]+)', o), re.findall(r'silence_end: ([\d.]+)', o))
