#!/usr/bin/env python3
"""srt.py - exact captions from the build's beats.json (text = the script, timing = the voice track).

    python3 srt.py beats.json out.srt
"""
import json, sys, textwrap

B = json.load(open(sys.argv[1]))
def ts(t):
    ms = int(round(t * 1000)); return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
out, n = [], 0
for b in B:
    lines = textwrap.wrap(b['text'], 42); chunks = [lines[i:i + 2] for i in range(0, len(lines), 2)]
    step = (b['end'] - b['start']) / len(chunks)
    for k, c in enumerate(chunks):
        n += 1; a = b['start'] + k * step
        out.append(f"{n}\n{ts(a)} --> {ts(a + step)}\n" + "\n".join(c) + "\n")
open(sys.argv[2], 'w').write("\n".join(out)); print(n, 'captions ->', sys.argv[2])
