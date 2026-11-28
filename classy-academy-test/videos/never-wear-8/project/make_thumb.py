import sys
sys.path.insert(0, '/home/user/AISalesAgent1/classy-academy-test/workflow/tools')
import thumb_make as TM
from PIL import Image
TM.LOGO = '/tmp/claude-0/-home-user-AISalesAgent1/0a7f1772-69b5-51de-8eba-81f1bf68cefb/scratchpad/nw8/assets/user_logo.png'
TM.D = '.'
CR = {'dress2': (0.45, 0.08, 1.1), 'dress34': (0.5, 0.10, 1.1), 'dress40': (0.5, 0.06, 1.1), 'dress9': (0.45, 0.06, 1.05),
      'silk0': (0.45, 0.10, 1.1), 'knit11': (0.55, 0.10, 1.1), 'dress6': (0.5, 0.10, 1.1), 'dress19': (0.55, 0.20, 1.35)}
def panel(k, w, fw=0, fy=0, dx=0):
    im = Image.open(f'mreal/{k}.jpg').convert('RGB'); cx, ty, s = CR[k]
    W0, H0 = im.size; sc = max(720 / H0, w / W0) * s
    im = im.resize((round(W0 * sc), round(H0 * sc)), Image.LANCZOS)
    L = min(max(0, round(cx * im.width - w / 2)), im.width - w); T = min(max(0, round(ty * im.height)), im.height - 720)
    return TM.finish(im.crop((L, T, L + w, T + 720)))
TM.panel = panel
a = sys.argv[1:]
TM.build([(k, 0, 0) for k in a[4:7]], a[1], a[2], a[3], a[0]); print('ok', a[0])
