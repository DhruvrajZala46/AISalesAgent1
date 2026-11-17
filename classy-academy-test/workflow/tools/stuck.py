import re
t = open('index.html').read(); ins, outs = {}, {}
for m in re.finditer(r'tl\.fromTo\("#([a-z]+\d+)",\{opacity:0[^}]*\},\{[^}]*\},([\d.]+)\)', t): ins.setdefault(m.group(1), []).append(float(m.group(2)))
for m in re.finditer(r'tl\.to\("#([a-z]+\d+)",\{opacity:0[^}]*\},([\d.]+)\)', t): outs.setdefault(m.group(1), []).append(float(m.group(2)))
print('stuck:', [(i, max(v)) for i, v in ins.items() if not i.startswith('v') and i[:2] not in ('ew', 'el') and max(v) > max(outs.get(i, [-1])) - 0.3])
