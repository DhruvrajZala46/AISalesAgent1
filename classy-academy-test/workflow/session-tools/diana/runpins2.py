import subprocess, sys, os
lines = [l.strip() for l in open(sys.argv[1]) if '=' in l]
lines = [l for l in lines if not os.path.exists(os.path.join('pin', l.split('=')[0] + '.json'))]
for i in range(0, len(lines), 6):
    subprocess.run([sys.executable, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools/pin_search.py'] + lines[i:i+6])
    print('batch', i, flush=True)
print('PINDONE', flush=True)
