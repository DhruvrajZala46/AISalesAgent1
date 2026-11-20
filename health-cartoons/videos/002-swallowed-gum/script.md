# 002 - What Actually Happens When You Swallow Gum?

Status (20 Nov 2026): **REJECTED by the user** after the 35 s preview ("10%, glitchy, hard to understand"). Kept only as a record of what not to do;
see `../../research/VIRAL-STUDY.md` §11 and LEARNINGS row 7. Lines 12-16 were never generated (no credits spent on them).
**Lines 12-16 are still to generate:** ElevenLabs said "free generations are busy" and nothing was charged.
`build_audio.py` holds placeholders (silence of the estimated length) until `proc/12_stomach.wav` … `proc/16_gum.wav` exist.

**Why this topic** (see `../../research/VIRAL-STUDY.md`): it belongs to the reference channel's strongest family (eating and swallowing habits:
27M, 26M, 22.9M). Almost everyone has swallowed gum, and the 7-year myth is famous, which opens a curiosity gap. Gum is a food-like object that
travels through the body, like their top visuals. There is a twist with mild fear (blockage) near 60%. The reference channel has no video on gum.

**Medical source:** Mayo Clinic expert answer "Swallowing gum: Is it harmful?". The body cannot digest gum, but it does not stay in the stomach;
it passes in stool. Very rarely, large amounts plus constipation have blocked children's intestines.
Milov et al., Pediatrics 1998;102(2):e22, "Chewing gum bezoars of the gastrointestinal tract", describes 3 children.
Duke Health agrees.

## Lines (flow `LtX1TiqVByVgBb5hcNtJ`, eleven_v3)
| # | Role / voice | Text | session / generation |
|---|---|---|---|
| 01 | gum / My Stephanie | `[excited] Wheee! Wait... where am I?!` (pauses trimmed in proc) | DPCzdEDKwGfLTpGYKwuE / gti18rFkchDISDuntNfs |
| 02 | stomach / Liam | `[annoyed] Oh great. He swallowed his gum. Again.` | xEiogSEGVKl67TvckWcZ / XHToKDzXrseSOgHwSS1p |
| 03 | gum | `[cocky] Relax, big guy. I'm moving in. Seven years, baby!` | cCA3V10PyqH9z2NbdDxL / rKXZSB7oDIlRktFXkw3S |
| 04 | stomach | `[confused] Seven years? Says who?` | fKObCcUZKKXuipktG3aH / SFZ7OFnmYGS4WisK5vp6 |
| 05 | gum | `Everybody, bro! It's a classic!` | PIXC2rKoEojCIltmqtnO / zqS2qJI7qTWwxK5lkAlg |
| 06 | stomach | `[smug] Okay. Acid, melt him.` | 0SzCpWXWzBIpxc6pgvfm / FpJUqAriJquht1CMqeO8 |
| 07 | gum | `[laughing] Ha! Your acid can't even touch me!` | wVVMbsYzY2ptFY5KG5M1 / AP1QVpL7qHxnayep3WVa |
| 08 | stomach | `Yeah, I can't digest you. But I can still kick you out.` | Wr72u7GyHReUTdoignx4 / ITGzEOSPeSIwE9PmpASw |
| 09 | gum | `[panicking] No, no, no! I signed a seven-year lease!` | ivoX5TBj7ERXfVXtnC5O / ooYbUvTsuxiOCHGybRfr |
| 10 | intestine / Laura | `[cheerful] Last stop: the toilet!` | N2IrRgjvd28O9bxHFece / 0CGE21LncQwjAYyGIosI |
| 11 | gum | `[sad] Seven years, they said...` | jYbH3gvg3Mi3zEkmN6UE / iqbmyTfLv6gCbrjONyJI |
| 12 | stomach / Liam | `[panicked] Uh-oh. He's swallowing the whole pack!` | **to generate** |
| 13 | gum / My Stephanie | `[evil laugh] We're one big blob now! Nobody gets through!` | **to generate** |
| 14 | patient / Davis | `Doc, my stomach hurts. Does swallowed gum really stay in there for seven years?` | **to generate** |
| 15 | doctor / Hope | `No, that's a myth. Your body can't digest gum, but it just passes through and comes out in a few days. The real danger is swallowing a lot at once, especially for kids. It can clump into a ball called a bezoar and block the gut.` | **to generate** |
| 16 | gum / My Stephanie | `[sulking] Next time... just spit me out.` | **to generate** |

## Beats
0.0 the face chews and blows a bubble · 0.5 POP · 0.7 GULP (lump down the throat) · 0.85 zoom into the mouth → stomach · 0.75 line 01 while falling ·
1.65 splash into the acid · STOMACH label · 03 the gum puts on sunglasses ("moving in") · 06 acid wave, drops and sizzle, steam · 07 sparkle ·
08 peristaltic squeeze pushes the gum to the pylorus, which stretches it, POP, and it goes down the duodenum · "2 DAYS LATER…" card ·
intestines (eyes on the coil), toilet-flush swirl and sad trombone · back in the stomach: the whole pack rains in, merges into a BLOB that plugs the
pylorus, red glow, food piles up, the stomach sweats · clinic at about 62%: the patient holds his stomach; the doctor shakes her head on "myth"
(7-YEAR MYTH label), bubble replay 1 (gum passing), bubble replay 2 (blob), punch-in plus BEZOAR label · stinger: the gum sulks on its foil
wrapper, then FOLLOW.

## Build
`python3 build_audio.py && python3 assemble.py && node ../../tools/render.js && bash ../../tools/mix.sh`
(`assemble.py` builds `scene.html` from the 001 engine plus `parts_world.js`, `parts_face.js` and `parts_timing.js`.)
