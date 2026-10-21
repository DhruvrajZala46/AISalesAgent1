# cutout.py ID [ID ...] : product photo raw/ID.jpg -> media/cut/ID.png with a transparent background
# (the IS-Net general-use segmentation model run with onnxruntime, the same model rembg uses; edges softened 1 px)
import sys, os, numpy as np, onnxruntime as ort
from PIL import Image, ImageFilter
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = '/tmp/claude-0/-home-user-AISalesAgent1/73fc3aa5-807d-530d-b865-5c7bcc671679/scratchpad/u2net/isnet-general-use.onnx'
sess = ort.InferenceSession(M, providers=['CPUExecutionProvider']); name = sess.get_inputs()[0].name
os.makedirs(f'{L}/media/cut', exist_ok=True)
for aid in sys.argv[1:]:
    src = os.environ.get('CUT_SRC', f'{L}/raw/{aid}.jpg'); im = Image.open(src).convert('RGB')
    x = np.asarray(im.resize((1024, 1024), Image.LANCZOS)).astype(np.float32); x = x / max(x.max(), 1)
    x = ((x - 0.5) / 1.0).transpose(2, 0, 1)[None].astype(np.float32)
    pred = sess.run(None, {name: x})[0][0, 0]; pred = (pred - pred.min()) / (pred.max() - pred.min() + 1e-6)
    m = Image.fromarray((pred * 255).astype(np.uint8)).resize(im.size, Image.LANCZOS).filter(ImageFilter.GaussianBlur(1))
    a = np.asarray(m).astype(np.float32) / 255; a = np.clip((a - 0.15) / 0.7, 0, 1)
    out = np.dstack([np.asarray(im), (a * 255).astype(np.uint8)]); o = Image.fromarray(out, 'RGBA'); o = o.crop(o.getbbox())
    o.save(f'{L}/media/cut/{aid}.png'); print(aid, o.size)
