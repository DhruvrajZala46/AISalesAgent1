# vttwords.py <file.vtt> -> json list of [word, start] from YouTube auto-caption word tags
import re, sys, json
def ts(s):
    h, m, x = s.split(':'); return int(h) * 3600 + int(m) * 60 + float(x)
words = []; seen = set()
for block in open(sys.argv[1]).read().split('\n\n'):
    lines = block.strip().split('\n')
    if not lines or '-->' not in lines[0]: continue
    t0 = ts(lines[0].split(' --> ')[0])
    for ln in lines[1:]:
        if '<c>' not in ln and not re.search(r'<\d\d:', ln): continue
        first = re.split(r'<', ln, 1)[0].strip()
        if first: words.append([first, t0])
        for tt, w in re.findall(r'<(\d\d:\d\d:\d\d\.\d+)><c>\s*([^<]*)</c>', ln):
            words.append([w.strip(), ts(tt)])
out = []
for w, t in words:
    k = (w, round(t, 2))
    if w and k not in seen: seen.add(k); out.append([w, round(t, 2)])
out.sort(key=lambda x: x[1]); json.dump(out, open(sys.argv[2], 'w'))
print(len(out))
