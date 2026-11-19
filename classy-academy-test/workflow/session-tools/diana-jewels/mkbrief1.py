# first-pass screening prompts: one file per group of search tags (sel/prompt_N.txt)
exec(open('briefs.py').read())
tags = list(B); G = [tags[i:i + 8] for i in range(0, len(tags), 8)]
P = '/tmp/claude-0/-home-user-AISalesAgent1/e022df48-ce52-5e1c-9920-7b34f523b018/scratchpad/cdj'
HEAD = '''You are choosing video clips for a YouTube video on a calm, elegant women's channel. The video is "Princess Diana's 7 Jewels: Who Wears Them Now?": each jewel is shown with REAL archive footage or photos of Princess Diana, then with an everyday scene of an ordinary elegant woman (any age, 25-70) doing what the script line says with her own jewellery (close-ups of jewellery on the body are welcome). Only REAL camera footage of real people is allowed. Every clip must show exactly what its script line says, so be strict: a pretty clip that shows something else is useless.

For each search tag below, open its contact sheet with the Read tool (absolute path given). Every thumbnail on a sheet is the first frame of one video pin. Its label, in red above it, is "<tag> <index> VIDEO". I tell you what the clip must show.

For each tag choose UP TO 6 thumbnails that fit the brief, best first. Judge only what you can see.

TAGS THAT START WITH "jd" AND ARE LISTED AS "REAL archive film of Princess Diana" ARE ABOUT PRINCESS DIANA HERSELF. For these:
- accept real news film, newsreel and real press photographs of Diana (a clip made of real photos is acceptable: say "stills" in your note);
- REJECT actresses playing her (The Crown: Emma Corrin, Elizabeth Debicki; the film Spencer: Kristen Stewart), lookalikes, AI-generated or AI-animated photos (a still face that blinks or sways, waxy skin), drawings, dolls, wax figures;
- REJECT frames where a large caption, title or sticker covers her (small text at the very top or bottom edge can be cropped: say "small text top" or "small text bottom");
- say which outfit and roughly which year if you can tell (for example "black off-the-shoulder dress, night, 1994"; "white dress with red polka dots and hat"; "Harvard sweatshirt and shorts").

FOR ALL OTHER TAGS reject:
- anything that looks AI-made (waxy or airbrushed skin, a too-perfect face, a dreamy glow, illustration, 3D render), collages and photo slideshows, drawings;
- adverts with big text or a brand logo, product videos, large captions or subtitles covering the subject, meme text, podcast clips with big subtitles;
- film and TV drama scenes with recognisable actors, celebrities and red-carpet footage;
- children as the main subject (unless the brief asks for a child), anything vulgar, drunk or revealing, beach or swimwear;
- dark, blurry or very low-quality frames.
Prefer: vertical video, calm elegant women in neutral clothes (navy, camel, cream, grey, black, chocolate, burgundy), natural light, candid moments that look unposed. Over the whole set, include women of different ages (many viewers are 40 to 70) and skin tones when the choice allows.
If fewer than 6 fit, give fewer. If none fits, say so. Never pad the list.

Write your result to the file given at the end with the Write tool, in EXACTLY this format (one block per tag, plain text):

TAG <tag>
PICK <index> | <what is visible: who, what they are doing, clothes, setting> | text: none / small top / small bottom / large
PICK <index> | ...
NOTE <one line: e.g. "nothing shows the polka dot dress; 12 and 30 show a kimono instead">

Write the file after EVERY FIVE tags (rewrite it with everything so far), so that nothing is lost if you are interrupted.
Then reply to me with at most 8 lines: which tags had no good fit, and anything I should know (for example "most of the Japan pins are photo slideshows").

THE TAGS AND WHAT EACH CLIP MUST SHOW
'''
for n, g in enumerate(G, 1):
    t = HEAD
    for tag in g:
        t += f'\n{tag}: {B[tag]}\n   sheet: {P}/pin/sheet_{tag}.jpg\n'
    t += f'\nWRITE THE RESULT TO: {P}/sel/sel_{n}.txt\n'
    open(f'sel/prompt_{n}.txt', 'w').write(t)
print('prompts', len(G), [len(g) for g in G])
