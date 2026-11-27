import sys
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools')
import thumb_make as TM
from PIL import Image
TM.LOGO = '/tmp/claude-0/-home-user-AISalesAgent1/0a7f1772-69b5-51de-8eba-81f1bf68cefb/scratchpad/ofh/assets/user_logo.png'
TM.D = '.'
CR = {'navy15': (0.42, 0.10, 1.18), 'suit18': (0.48, 0.08, 1.18), 'black39': (0.40, 0.10, 1.2), 'white25': (0.5, 0.20, 1.55),
      'camel46': (0.45, 0.20, 1.35), 'navy11': (0.38, 0.12, 1.15), 'coat31': (0.42, 0.10, 1.15), 'white17': (0.5, 0.0, 1.0), 'trench41': (0.45, 0.12, 1.1), 'camel48': (0.45, 0.06, 1.15)}
def panel(k, w, fw=0, fy=0, dx=0):
    im = Image.open(f'mreal/{k}.jpg').convert('RGB'); cx, ty, s = CR[k]
    W0, H0 = im.size; sc = max(720 / H0, w / W0) * s
    im = im.resize((round(W0 * sc), round(H0 * sc)), Image.LANCZOS)
    L = min(max(0, round(cx * im.width - w / 2)), im.width - w); T = min(max(0, round(ty * im.height)), im.height - 720)
    return TM.finish(im.crop((L, T, L + w, T + 720)))
TM.panel = panel
a = sys.argv[1:]
TM.build([(k, 0, 0) for k in a[4:7]], a[1], a[2], a[3], a[0]); print('ok', a[0])
