import sys, re
def clean(path):
    out = []
    for line in open(path, encoding='utf8'):
        line = line.strip()
        if not line or '-->' in line or line.startswith(('WEBVTT', 'Kind:', 'Language:', 'NOTE')) or line.isdigit(): continue
        line = re.sub(r'<[^>]+>', '', line).strip()
        if line and (not out or out[-1] != line): out.append(line)
    # drop rolling duplicates (auto captions repeat the previous line)
    res = []
    for l in out:
        if res and l.startswith(res[-1]): res[-1] = l
        elif res and res[-1].endswith(l): continue
        else: res.append(l)
    return ' '.join(res)
if __name__ == '__main__': print(clean(sys.argv[1]))
