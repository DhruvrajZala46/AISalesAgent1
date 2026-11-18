import email, glob, os, subprocess, io, json
from PIL import Image
out = {}
for f in sorted(glob.glob('sb_*.mhtml')):
    vid = f[3:-6]; msg = email.message_from_binary_file(open(f, 'rb')); os.makedirs(f'sbimg/{vid}', exist_ok=True)
    frames = []
    for k, p in enumerate([p for p in msg.walk() if p.get_content_type().startswith('image/')]):
        u = p.get('Content-Location'); dst = f'sbimg/{vid}/M{k}.jpg'
        if not (os.path.exists(dst) and os.path.getsize(dst) > 2000):
            subprocess.run(['curl', '-sS', '-f', '-o', dst, u], capture_output=True)
        try: im = Image.open(dst).convert('RGB')
        except Exception: continue
        for r in range(im.height // 90):
            for c in range(im.width // 160):
                t = im.crop((c*160, r*90, c*160+160, r*90+90))
                if max(t.convert('L').getextrema()) < 8: continue
                frames.append(t)
    os.makedirs(f'fr2/{vid}', exist_ok=True)
    for k, t in enumerate(frames): t.save(f'fr2/{vid}/{k:03d}.jpg', quality=92)
    out[vid] = len(frames)
json.dump(out, open('frames2.json', 'w')); print(sum(out.values()), 'frames from', len(out), 'videos')
