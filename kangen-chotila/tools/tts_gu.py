# tts_gu.py voice rate  -> tts/cNNN.wav (48k mono) + words.json {line: [[word, start, end], ...]} from beats_tts.txt
import asyncio, edge_tts, os, sys, json, subprocess
V = sys.argv[1] if len(sys.argv) > 1 else 'gu-IN-NiranjanNeural'; RATE = sys.argv[2] if len(sys.argv) > 2 else '+0%'
lines = [l.strip() for l in open('beats_tts.txt') if l.strip()]
os.makedirs('tts', exist_ok=True); W = {}
async def one(i, t):
    c = edge_tts.Communicate(t, V, rate=RATE, proxy=os.environ.get('HTTPS_PROXY'), boundary='WordBoundary')
    mp3 = f'tts/c{i:03d}.mp3'; ev = []
    with open(mp3, 'wb') as f:
        async for ch in c.stream():
            if ch['type'] == 'audio': f.write(ch['data'])
            elif ch['type'] == 'WordBoundary': ev.append([ch['text'], ch['offset'] / 1e7, (ch['offset'] + ch['duration']) / 1e7])
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', mp3, '-ar', '48000', '-ac', '1', f'tts/c{i:03d}.wav'], check=True)
    W[str(i)] = ev
async def main():
    for i, t in enumerate(lines, 1): await one(i, t)
asyncio.run(main())
json.dump(W, open('words.json', 'w'), ensure_ascii=False, indent=0)
tot = 0
for i in range(1, len(lines) + 1):
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'tts/c{i:03d}.wav'], capture_output=True, text=True).stdout); tot += d
    print(i, round(d, 2), lines[i-1][:50])
print('total speech', round(tot, 1))
