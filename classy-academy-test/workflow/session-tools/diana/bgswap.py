# after every build: the live-blurred caramel backdrop -> the pre-rendered assets/bg.png (render speed; LEARNINGS row 37)
import re
s = open('index.html').read()
n = re.subn(r'\.bg \{ position: absolute; inset: -180px; filter: blur\(90px\);.*?\}', '.bg { position: absolute; inset: 0; background: url("assets/bg.png") center / cover no-repeat; }', s, count=1, flags=re.S)
assert n[1] == 1, 'bg rule not found'
open('index.html', 'w').write(n[0]); print('bg swapped')
