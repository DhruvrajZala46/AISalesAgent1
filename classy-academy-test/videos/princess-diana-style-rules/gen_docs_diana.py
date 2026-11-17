# gen_docs_diana.py - sources log, credits and chapters for "Princess Diana's 8 Timeless Style Rules" (run after the final build)
import json, os, re
m = json.load(open('raw/meta.json')); U = json.load(open('used_times.json')); B = json.load(open('beats.json'))
PM = json.load(open('photos/orig_meta.json')); PICS = json.load(open('pics.json'))
Bd = {d['i']: d for d in B}
CROP = {}; MAXSLOW = {}
exec(open('clips.py').read())
def line_at(t):
    best = B[0]
    for d in B:
        if d['start'] - 0.6 <= t: best = d
    return best
mmss = lambda t: f'{int(t//60)}:{int(t%60):02d}'
# where the picture is true to the idea of the line but not to every word (from eye_notes.txt)
PARTLY = {
 'h1b': 'a woman showing a cream jacket and white trousers; no mirror in shot',
 'h2d': 'a feathered gown at a party with fireworks; no dinner in shot',
 'h5c': 'a woman in white walking through an arcade: stands for "what style actually is"',
 'h5d': 'a woman of about 50 in a navy jacket talking to the camera: stands for "the message your clothes give"',
 'h6c': 'a navy blazer with jeans: stands for "practical"',
 'h6d': 'a belt fastened over a dress: stands for "a little surprising"',
 'h6e': 'a woman of about 60 in a soft blue cardigan: stands for "any age, any budget"',
 'h7b': 'a woman in a black dress walking through a stone arcade, not into a room',
 'd8a': 'a black ball gown climbing the steps of a mansion; no room, no other guests',
 'd8c': 'a woman in a black dress and hat sitting with tea: stands for "calm"',
 'd8d': 'a woman in a cream outfit standing in an arched room: stands for "respected"',
 'd9b': 'a woman in a yellow dress at a terrace table by the sea: stands for "the outfit that fitted the moment"',
 'r1e': 'a pale pink jumper, lighter than a warm dusty rose',
 'r1i': 'a woman with a bouquet of lilies coming down steps, smiling; nobody is greeted in shot',
 'r2a': 'a woman in a long black coat-dress climbing a grand staircase, seen from behind: stands for "at a distance"',
 'r2a2': 'a red suit, long leather gloves and sunglasses: stands for "armour"',
 'r2b': 'footage from a stairlift company advert (the logo is cropped out); an elderly woman hugged close',
 'r3c': 'a woman in a black evening dress stepping out of a car; no dinner table in shot',
 'r3d': 'a woman in a gold slip dress in a studio: stands for "this evening matters to me"',
 'r3e': 'wedding guests in pastel gowns walking away, seen from behind',
 'r4c': 'a woman helped out of a car in a long black dress: the awkward moment itself, not the planning',
 'r4d': 'a woman already seated at a cafe table in a knit dress; the act of sitting down is not shown',
 'r4g': 'a woman re-tying the top of a black wrap dress (the neckline), no gaping shown',
 'm24a': 'a young woman smiling at her phone: stands for the viewer who is still here',
 'r5h': 'a gold ball gown on a staircase: stands for the piece you love but rarely wear',
 'g29a': 'a woman of about 50 showing a light-blue jumper and white trousers',
 'g29g': 'a woman turning in a sage-green dress on a staircase',
 'r6c': 'white shirt with light (not dark) jeans; her head is out of frame',
 'r7a': 'a silver-haired woman in a black dress walking and smiling: stands for "the woman you are now"',
 'r7d': 'a woman packing folded clothes into clear bags on her wardrobe floor; no donation box or person receiving them',
 'r8a': 'a woman in a black dress walking outdoors, not into a room',
 'r8h': 'a long black one-shoulder evening dress (longer than a "classic black dress")',
 'r8i': 'a berry-red trouser suit (jacket and trousers)',
 'r8j': 'a black sequin gown on a hanger, a hand takes it down',
 'e41b': 'a woman in a pink jumper talking to the camera: stands for "wear it again, proudly"',
 'e41c': 'a woman in a cream tweed suit getting up from a cafe table: stands for the courage outfit',
 'e42b': 'a woman pinning her hair up, seen from behind (the guide: hairstyles)',
 'e42c': 'a smiling woman of about 50 in a blue jumper holding her dog (the guide line)',
 'h3b': 'real film of Diana reaching to hands in a crowd; the pin gives no date or place',
 'h3c': 'real film of Diana in a tartan jacket with flowers; the pin gives no date or place',
 'h3d': 'real film, a close view in a black jacket and pearl choker; the pin gives no date or place',
 'h4a': 'real film: a royal-blue blazer over a black dress; the pin gives no date or place',
 'h6a': 'real film: press photographers in a stand, then Diana in sunglasses waving; the pin gives no date or place',
 'h7a': 'real press photographs shown one after another (a blue ruffled ballgown, early 1980s), not moving film',
 'd10a': 'the same walkabout as at 0:31 (earlier seconds of the clip)',
 'm24b': 'real film: Diana walking through a hall in the royal-blue blazer',
 'r4a': 'real film: Diana out of the car in a pale blue halter dress, her clutch in her hand (not held to her chest in this clip)',
 'r4b': 'real film, low resolution: Diana beside a car in a red gown, clutch held in front',
 'r5a': 'real film: the pale blue strapless gown (the re-made one shown in the photographs that follow)',
 'e40a': 'real film: Diana talking with people in a crowd; the pin gives no date or place',
 'e40b': 'real film, low resolution: Diana hugging a child',
 'e43a': 'the same crowd as at 10:46 (earlier seconds of the clip)',
 'e43b': 'real film: Diana in a white shirt, talking, then smiling behind her hands',
}
FILM = {k for k in U if k.startswith('di')}
slot_of = {}
for s_, (k, a, b) in C.items(): slot_of.setdefault(k, []).append((s_, a, b))
rows = []
for n, (k, t) in enumerate(sorted(U.items(), key=lambda z: z[1]), 1):
    d = line_at(t); x = m[k]; who = (x.get('creator') or '').replace('|', '/').strip()
    who = f"{who} (@{x['user']})" if x.get('user') else who
    src = x.get('src') or ''; src = src if ('instagram.com' in src or 'tiktok.com' in src) else ''
    txt = d['text'][:60].replace('|', '/') + ('...' if len(d['text']) > 60 else '')
    how = f'Pinterest video pin -> {src}' if src else 'Pinterest video pin (original post not traced)'
    ss = slot_of.get(k, []); win = '; '.join(f'{a:g}-{b:g} s' for _, a, b in ss)
    note = '; '.join(PARTLY[s_] for s_, _, _ in ss if s_ in PARTLY)
    fit = ('NOTE: ' if k in FILM else 'PARTLY: ') + note if note else 'matches the line'
    if k in CROP: fit += ' (cropped past a caption or a small watermark)'
    holder = who + (' / ARCHIVE film or press photographs of Princess Diana: the original broadcaster, agency or photographer owns it; this pin is a fan re-upload' if k in FILM else '')
    rows.append(f"| {n} | {mmss(t)} | L{d['i']}: {txt} | {k} ({win}) | {holder} | {how} | credited, not licensed | unresolved | {fit} |")
# ---- photographs ----
VER = {  # how each photograph's moment was checked
 'pnineties_19': 'no caption on the pin; a 1990s plain pink suit, used only as "her clothes" (no date shown on screen)',
 'pnineties_32': 'pin says "Princess Diana"; a plain black suit, no date shown on screen',
 'pnineties_11': 'pin says "Princess Diana"; a navy trouser suit, no date shown on screen',
 'pnohat_3': 'pin: "How she loved children and people"; no date shown on screen',
 'pcaring_28': 'the dress matches the published description of the "caring dress" (blue, with bright flowers; David Sassoon): identified by the dress, the pin has no caption',
 'pcaring_2': 'pin: "Diana, Official Visit, 1992"; the same dress',
 'pnohat_20': 'pin links insider.com on her Harlem Hospital visit; she wears the same floral dress and a child holds her necklace',
 'pnohat_2': 'no caption beyond "the princess is surrounded by young children"; the same floral dress',
 'phats_7': 'no caption; a formal hat, shown only as "a hat was expected"', 'phats_0': 'no caption; a formal hat',
 'phats_2': "pin links Harper's Bazaar, \"Princess Diana's Best Hats\"",
 'pnohat_11': 'pin says "Princess Diana"; no hat, hugging a child', 'pnohat_17': 'pin says "Princess Diana"; no hat, hugging a child',
 'pnohat_23': 'no caption; no hat, a child hugging her',
 'paids_0': 'pin: "April 9th/1987 ~ Princess Diana opens the Broderip Ward ... Middlesex Hospital"',
 'paids_1': 'pin: "The Princess of Wales shakes hands with an AIDS patient as she opens a new AIDS ward at the Middlesex Hospital on April 9, 1987"',
 'pjapan_0': 'pin links vogue.co.uk: "Giving a nod to the host country\'s national flag ... Kyoto, Japan. Diana (1986)"',
 'pjapan_1': 'pin says "Princess Diana"; the same dress, a kimono being draped over it',
 'pjapan_11': 'pin: "attend a traditional tea ceremony at Nijo Castle, Kyoto, Japan, 9th May 1986"',
 'pclutchb_0': "pin: Harper's Bazaar UK, \"Diana's cleavage bags\"", 'pclutchb_1': 'pin: cosmopolitan.com, "Princess Diana used clutches to hide her cleavage"',
 'pclutchb_2': 'pin: womansday.com, "Princess Diana\'s Famous \'Cleavage Bags\'"', 'pclutchb_5': 'pin: "Coined by Diana as the \'cleavage bag\', Anya Hindmarch\'s ... clutches"',
 'pjapanb_29': 'pin: "The Hat..."; the same red hat and polka dot dress', 'pbalcony_0': 'pin links tatler.com, "Best ever Trooping the Colour outfits"; the same dress on the balcony',
 'ppink83_17': 'no caption; the ruffled pink gown, the same as in the Town & Country 1983 tour photographs seen on the same search',
 'ppink83_22': 'pin: "Princess Diana attends a dinner at the London Guildhall ... in October 1986"; the same gown without the ruffles',
 'plisbon_30': 'pin links marieclaire.com.au, "Princess Diana\'s Recycled Royal Wardrobe"; the long-sleeved gown (1987 in the article read)',
 'plisbon_13': 'no caption; the same gown without sleeves, as the articles describe for 1989: identified by the gown',
 'ppolo_0': 'pin links whowhatwear.com; the polo look (blazer, sweatshirt, jeans, cap)', 'ppolo_1': 'no caption; the same polo look',
 'ppolo_14': 'pin links nowtolove.com.au, "Princess Diana in casual outfits"; the same polo look',
 'pwhitejeans_19': 'pin from Town & Country (@tandcmag)', 'pwhitejeans_22': 'pin links marieclaire.com, "Princess Diana\'s 32 Best Fashion Moments"',
 'pwhitejeans_21': 'pin links whowhatwear.com, "The Fashion Trends Princess Diana Loved"',
 'pbosnia_4': 'pin: "the princess during her trip to Bosnia, 9 August 1997"', 'pbosnia_0': 'pin links telegraph.co.uk: "taken in August 1997 during a trip to Bosnia"',
 'pbosnia_5': 'pin links whowhatwear.co.uk: "in jeans, a shirt and loafers for a visit to Bosnia ... 1997"',
 'peightiesb_14': 'no caption; an early-1980s sailor collar and hat', 'peightiesb_19': 'no caption; a large lace collar', 'peightiesb_24': 'no caption; a sailor collar and red bow',
 'pnineties_12': 'no caption; a plain white suit (a fan-group mark was cropped off the bottom)', 'pnineties_0': 'pin links vogue.fr, "32 ways Princess Diana wore tailoring"',
 'pnineties_24': 'pin links snippetandink.com; a white dress and jacket',
 'pauctionb_0': 'pin from 1stdibs: the Christie\'s catalogue "Dresses from the Collection of Diana, Princess of Wales", sale of 25 June 1997',
 'pauction_7': 'pin: "23 June 1997 ... attending the auction of her dresses at Christie\'s in New York"',
 'prevengeb_22': 'the left half of a comparison pin ("Princess Diana"): the black dress on a mannequin; the pin names no source',
 'prevenge_4': 'pin: "29 June 1994 ... attending the Serpentine Gallery ... (wearing the \'revenge dress\')"',
 'prevenge_19': 'pin quotes an Instagram post about the Serpentine Gallery gala, June 1994 (it prints "19 June")',
 'prevenge_16': 'pin: "the \'Revenge Dress\' by Christina Stambolian at the Serpentine Gallery in Kensington Gardens 29/6/94"',
 'prevengeb_17': 'pin links marieclaire.co.uk on her "revenge" necklace', 'pjapan_20': 'an Instagram re-pin in Russian; the red hat and polka dot dress',
 'pnohat_10': 'pin says "Diana"; carrying a child', 'prevengeb_14': 'pin links goodhousekeeping.com, "1994", the black dress beside the car',
}
prow = []
for n, (name, a, b) in enumerate(sorted(PICS, key=lambda z: z[1]), 1):
    k = name[:-4]; x = PM[k]; d = line_at(a)
    who = f"pinned by @{x.get('user', '?')}" + (f", links {x['domain']}" if x.get('domain') and 'Uploaded' not in x['domain'] else '')
    prow.append(f"| P{n} | {mmss(a)} | L{d['i']} | {k} | press photograph; the photographer or agency owns it ({who}) | {x.get('pin', '')} | not licensed | unresolved | {VER.get(k, 'not checked')} |")
assert all(p[0][:-4] in VER for p in PICS), [p[0] for p in PICS if p[0][:-4] not in VER]
nfilm = len(FILM)
hdr = f"""# SOURCES-LOG - Princess Diana's 8 Timeless Style Rules (The Classy Elegance, v1, 17 Nov 2026)

In order of appearance: **{len(rows)} video clips** ({nfilm} of them archive film or press stills of Princess Diana, {len(rows) - nfilm} everyday
scenes) and **{len(prow)} press photographs** of Princess Diana. No product cut-outs, no stock sites.

- **Where the footage comes from:** Pinterest video pins of Instagram / TikTok creators' reels and of fan re-uploads of
  news film: 602 clips downloaded and read, from 153 search phrases in five rounds. The photographs: Pinterest photo
  pins from 29 searches, 88 downloaded at full size, 54 used.
- **All new footage.** `oldclash.py` compared every download with the used clips of every earlier video (the charm video
  included): 106 downloads repeat earlier footage; none is used. No clip is repeated inside this video: five clips come
  back with different seconds of the same film (the black-dress evening three times; two Diana clips, a shirt clip and a
  blazer clip twice each), never the same footage.
- **Duplicate check:** every download hashed at 1 frame per second (`tools/dupall.py`): 87 groups of re-pinned copies;
  only one copy of a group may be used; 0 clashes among the used clips.
- **AI checks:** the watermark scan flagged no used clip (highest score among all downloads 0.31, not used). Removed by
  eye or by the two screenings: pins from AI accounts, an "AI clips" animation of a Diana photograph, a clip that looked
  processed (white outline round her), glossy "AI stock" women. Honest limit: a real-looking clip can still be AI, and
  several archive clips are fan re-uploads that have been sharpened or upscaled.
- **Princess Diana is shown only in real archive film and real press photographs.** Never an actress (The Crown and
  Spencer were rejected at the first screening), never an AI clip. A replica of the black dress made for The Crown was
  found and rejected.
- **Every dated moment on screen was checked against the pin's caption or the article it links to** (last column of the
  photograph table). Where a pin has no caption, the photograph was identified by the outfit and this is said.
- **Captions, watermarks and stickers:** every candidate was read on time-labelled strips by a first and a second
  screening, every pick again at large size by me (`eye_notes.txt`), and the finished edit at 179 snapshots.
  {len(CROP)} clips are cropped past a caption or a small watermark (the `CROP` list in `clips.py`); three photographs
  were cropped past a mark; photographs with an agency watermark were not used.
- **"PARTLY" in the last column is said plainly**: the picture is true to the idea of the line but not to every word.

**Rights status.** **Nothing here is licensed.** The everyday clips are creators' reels found on Pinterest; the archive
film belongs to the original broadcasters and news agencies; the photographs belong to press agencies and photographers
(the pins do not name them). Every row is **unresolved**, and credit is not permission. A copyright claim or YouTube's
reused-content rule is a real risk, higher for this video than for earlier ones because of the 54 press photographs.
The creator decides before publishing.
Music: "Classical vibes 3" by Grigoriy Nuzhny, Mixkit Stock Music Free License (cleared). No sound effects.

## Video clips

| # | At | Script line | Clip key (seconds used) | Creator / rights holder | How it was found | Licence basis | Decision | Fit to the line |
|---|---|---|---|---|---|---|---|---|
"""
D = '/home/user/AISalesAgent1/classy-academy-test/videos/princess-diana-style-rules/'
open(D + 'SOURCES-LOG.md', 'w').write(hdr + '\n'.join(rows) + '\n\n## Photographs of Princess Diana\n\n| # | At | Line | File | Rights holder | Pinterest pin | Licence basis | Decision | How the moment was checked |\n|---|---|---|---|---|---|---|---|---|\n' + '\n'.join(prow) + '\n')
handles = []
for k, t in sorted(U.items(), key=lambda z: z[1]):
    h = m[k].get('user')
    if h and '@' + h not in handles: handles.append('@' + h)
open(D + 'CREDITS.txt', 'w').write('VISUAL CREDITS (all footage belongs to its creators, thank you):\n' + ' '.join(handles) +
    '\nArchive film and photographs of Diana, Princess of Wales: the original broadcasters, news agencies and photographers.\n'
    'Music: "Classical vibes 3" by Grigoriy Nuzhny (Mixkit)\n')
secs = [(1, 'What are your clothes saying?'), (8, 'What style really is'), (11, '1. Dress for the people you are about to meet'),
        (14, '2. Never let your clothes become a barrier'), (18, '3. Honour your host'), (21, '4. Plan for the awkward moment'),
        (25, '5. Re-wear what works'), (29, 'Your personal stylist guide'), (30, '6. Keep an off-duty uniform'),
        (33, '7. Edit as you grow'), (37, '8. Keep one outfit for courage'), (40, 'Her style was a language')]
out = [(0 if i == 1 else int(Bd[i]['start']), x) for i, x in secs]
total = Bd[len(Bd)]['end'] + 4.2
assert out[0][0] == 0 and min(b[0] - a[0] for a, b in zip(out, out[1:] + [(int(total), '')])) >= 10
open(D + 'CHAPTERS.txt', 'w').write('\n'.join(f'{t//60:02d}:{t%60:02d} {x}' for t, x in out) + '\n')
missing = [s_ for s_ in PARTLY if s_ not in C]
print(len(rows), 'clip rows', len(prow), 'photo rows', len(handles), 'handles; notes for missing slots:', missing)
print(sum(1 for r in rows if 'PARTLY' in r), 'rows marked PARTLY;', sum(1 for r in rows if 'NOTE:' in r), 'film notes'); print(open(D + 'CHAPTERS.txt').read())
