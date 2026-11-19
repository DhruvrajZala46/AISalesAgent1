# second-pass screening prompts: frame strips of the downloaded clips (st/<prefix>_N.jpg, 7 clips per sheet)
# usage: python3 mkbrief2.py <prefix> [sheets per agent]
import sys, glob, re, os, json
exec(open('briefs.py').read())
if os.path.exists('briefs2.py'): exec(open('briefs2.py').read())
pre = sys.argv[1]; per = int(sys.argv[2]) if len(sys.argv) > 2 else 7
P = '/tmp/claude-0/-home-user-AISalesAgent1/e022df48-ce52-5e1c-9920-7b34f523b018/scratchpad/cdj'
sheets = sorted(glob.glob(f'st/{pre}_*.jpg'), key=lambda f: int(re.findall(r'_(\d+)\.jpg', f)[0]))
keys = [l.split()[0] for l in open(f'strips_{pre}.log') if False]
order = {}
for l in open(f'strips_{pre}.log'):
    m = re.match(r'(st/\S+\.jpg) (\[.*\])', l)
    if m: order[os.path.basename(m.group(1))] = [k.split(':')[0] for k in eval(m.group(2))]
HEAD = '''You are checking downloaded video clips for a YouTube video on a calm, elegant women's channel: "Princess Diana's 7 Jewels: Who Wears Them Now?". Each jewel is shown first with REAL archive pictures or film of Princess Diana, then with an everyday elegant woman (any age 25-70) doing what the line says with her own jewellery: opening an old jewellery box, wearing a family brooch, writing a note, fixing a pinching earring, trying earrings at home, looping a necklace as a bracelet, a pendant at the collarbone, doubled pearls, pearl earrings by day and by night, an old ring in a drawer, a jeweller reshaping a piece, one woman fastening a necklace on another, choosing at a jewellery counter, an older woman's hands with a ring. Only real camera footage of real people may be used, and every clip must show exactly what its script line says. Be strict and never guess.

Read the image sheets listed at the end with the Read tool, one by one.

HOW TO READ A SHEET: each row is one clip. The red text above the row's left edge is the clip key (letters then a number, for example focus12), its length in seconds and the creator. The frames of a row are in time order; the number under each frame is the second it was taken at.

The letters of a key are its search tag. Each tag was searched for one purpose, listed under WHAT EACH TAG MUST SHOW. Judge every clip against its own tag's purpose, and also say if it would serve another purpose on the list better.

FOR EVERY CLIP write ONE line in this exact format:
key | who and what is visible (how many people, women / men, rough ages, clothes with colours, place) | what happens, with seconds (who talks, who listens, who looks where, gestures, laughs, hugs, walks) | fits its purpose: yes / partly / no (and why in a few words) | best seconds a-b (the longest steady stretch that shows the purpose, no cut inside it) | burned-in text, captions, subtitles, logos or watermarks and where they sit (top / middle / bottom / corner; all the time or from second N) | AI or fake: none / suspect (why) | other problems (film or TV scene with actors, celebrity, advert, podcast clip, photo slideshow, dark, blurry, vulgar, child as subject, selfie talking to camera)

RULES
- Report only what you can see in the frames. If you cannot tell, write "unclear". Do not skip any clip.
- AI tells: waxy or airbrushed skin, a too-perfect face, hands, glasses or jewellery that melt or change between frames, garbled lettering, a dreamy glow, motion that looks morphed, the same "perfect" woman in a too-tidy beige room. Content-farm slideshows and animated photographs count as fake.
- For the Princess Diana clips (tags starting with "jd"): for EVERY shot inside the clip say whether it is real moving archive film (grain, period setting, people moving) or a still press photograph shown as a slideshow, and whether anything looks like an actress (The Crown, Spencer), a look-alike, an AI-animated or AI-smoothed photograph (faces that morph, waxy skin, hair or hands that swim). Describe her outfit in each shot exactly (colour, pattern, sleeves, neckline, hat or no hat, bag, jewellery), the setting, and what she does in which seconds. Do not name the year or the event unless a caption in the frame says it. A clip that is a slideshow of stills is usable only shot by shot: give the seconds of each still.
- Captions matter: say exactly where they sit, because a caption over the subject makes the clip unusable while a small one at the edge can be cropped away.
- Seconds must come from the frame times you see. Do not invent precision.
- Length matters: most shots need ONE steady stretch of 4 to 9 seconds from a single take (the red line lists the clip's cuts after "cuts:"). Give the longest stretch that shows the purpose; if the clip is only quick cuts under 3 s, say "quick cuts".
- The same footage often appears under two keys: if two rows look like the same video, say so ("same as <key>").
- A brand advert or a product video with a logo counts as an advert: say so.

Write everything to the file named at the end with the Write tool. Write the file after EVERY sheet (rewrite it with everything so far), so that nothing is lost if you are interrupted. After the per-clip lines add a section "BEST PER TAG": for each tag, the best three clips (key and seconds), best first, or "none".
Then reply to me with at most 8 lines: the tags that have no usable clip, and anything surprising.

WHAT EACH TAG MUST SHOW
'''
def keys_of(sheet):
    return (order or {}).get(os.path.basename(sheet), [])
n = 0
for i in range(0, len(sheets), per):
    part = sheets[i:i + per]; n += 1
    tags = sorted({re.match(r'[a-z]+', k).group(0) for s in part for k in keys_of(s)}) if order else sorted(B)
    t = HEAD + ''.join(f'{tag}: {B.get(tag, "see the tag name")}\n' for tag in tags)
    t += '\nSHEETS TO READ (absolute paths):\n' + ''.join(f'{P}/{s}\n' for s in part)
    t += f'\nWRITE THE RESULT TO: {P}/scr/{pre}_{n}.txt\n'
    open(f'scr/prompt_{pre}_{n}.txt', 'w').write(t)
print(pre, len(sheets), 'sheets ->', n, 'prompts')
