# package.py : the delivery files in deliver/ - the editable project zip (code, records, fonts, logo, music, narration, cut-outs)
# and the footage used by the final timeline in parts under ~330 MB (stored, not recompressed). Media never goes to git.
import json, os, zipfile
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(L)
os.makedirs('deliver', exist_ok=True)
tl = json.load(open('project/timeline.json')); picks = json.load(open('project/picks.json'))
used = sorted({m['asset'] for sg in tl['segments'] for m in sg.get('shots', []) + sg.get('panels', [])})
music = ['music/BerceuseinD-flatmajorOp.57.flac', 'music/NocturneinEflatmajorOp.9no.2.flac', 'music/NocturnesOp.32-No.1.NocturneinBmajor.flac']
P = 'TheClassyElegance_look_older_project'
with zipfile.ZipFile(f'deliver/{P}.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for root in ('project', 'tools', 'plan', 'fonts', 'assets', 'tts'):
        for dp, dn, fn in os.walk(root):
            dn[:] = [d for d in dn if d != '__pycache__']
            for f in fn: z.write(os.path.join(dp, f), f'{P}/{os.path.join(dp, f)}')
    for a in used: z.write(f'picks/{a}.json', f'{P}/picks/{a}.json')
    for f in music: z.write(os.path.realpath(f), f'{P}/{f}')
    for f in ('audio/voice.wav', 'audio/voice24.wav'): z.write(f, f'{P}/{f}')
    for f in sorted({picks[a]['file'] for a in used if picks[a]['file'].startswith('media/cut/')}): z.write(f, f'{P}/{f}')
    for f in ('out/SOURCES-LOG.md', 'out/CREDITS.txt', 'out/SCRIPT-TO-VISUAL-MAP.md'): z.write(f, f'{P}/{f}')
    z.write('project/README.txt', f'{P}/README.txt')
clips = sorted({picks[a]['file'] for a in used if picks[a]['file'].startswith('media/clips/')})
parts, cur, size = [], [], 0
for f in clips:
    s = os.path.getsize(f)
    if cur and size + s > 330e6: parts.append(cur); cur, size = [], 0
    cur.append(f); size += s
if cur: parts.append(cur)
for i, fs in enumerate(parts, 1):
    with zipfile.ZipFile(f'deliver/look_older_footage_part{i}of{len(parts)}.zip', 'w', zipfile.ZIP_STORED) as z:
        for f in fs: z.write(f, f'{P}/{f}')
for f in sorted(os.listdir('deliver')): print(f, round(os.path.getsize(f'deliver/{f}') / 2**20, 1), 'MiB')
