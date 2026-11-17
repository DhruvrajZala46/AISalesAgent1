# Reel 8 plan (Gujarati, about 40 s): "સવાર-સવારમાં કયું પાણી પીવું?"

Waiting for the owner's approval. It copies the proven Short "5 Best water drink for morning by Nitesh Soni"
(6.83M views, 103x its channel's median; teardown in `../research/nitesh-soni-5-waters-teardown.md`).

## What is copied, what changes
- **Copied:** the hook sentence, the "if you drink X, you get Y" line shape, kitchen drinks everyone knows, the
  layout (a talking face on the top third, the drink being made below), a pill title, the fast pace.
- **Changed:** after four drinks comes a twist that makes Kangen the hero: every one of those drinks is about 99%
  water, so the real question is which water. Then the same "if … then" line shape compares bore, RO/jar and
  Kangen water, and the video ends on the approved free-demo line.

## Hook
- **Words** (the reference's hook in Gujarati): "સવાર-સવારમાં કયું પાણી પીવું? કોઈને સમજાતું જ નથી."
- **Picture at second 0:** the host on top, thinking, with a steel glass; the pill "સવારે કયું પાણી પીવું? 🤔"; below,
  water pouring onto lemon slices.
- **Mid-video hook (the twist, about second 17):** a full-screen glass of lemon water; the lemon shrinks to a tiny
  "1%" tag and the rest of the glass fills with the label "99% પાણી".

## Script (12 lines, about 105 words)
| # | Voice | Picture |
|---|---|---|
| 1 | સવાર-સવારમાં કયું પાણી પીવું? કોઈને સમજાતું જ નથી. | host top + lemon water pour below, pill title |
| 2 | સવારે ઊઠીને લીંબુ પાણી પીઓ, તો વિટામિન C મળે. | lemon squeezed into a glass |
| 3 | જીરાનું પાણી પીઓ, તો પાચનમાં મદદ મળે, ગેસ ઓછો થાય. | jeera in a steel pot, strained into a glass |
| 4 | વરિયાળીનું પાણી પીઓ, તો પેટને ઠંડક મળે. | variyali soaking, strained |
| 5 | આદુવાળું પાણી પીઓ, તો શરદી-કફમાં રાહત મળે. | ginger slices in hot water |
| 6 | પણ એક વાત કોઈ નથી કહેતું: આ ચારેયમાં લગભગ નવ્વાણું ટકા તો પાણી જ છે! | full screen: the 1% / 99% glass |
| 7 | લીંબુ બદલ્યું, જીરું બદલ્યું… પણ પાણી તો એ જ. | four glasses in a row; the ingredients swap, the water stays |
| 8 | બોરનું હોય, તો ઘણી જગ્યાએ ક્ષાર વધારે. | host back on top; a bore pipe gushing |
| 9 | RO કે જારનું હોય, તો મોટે ભાગે મિનરલ્સ નીકળી ગયેલાં. | RO purifier, 20-litre jar |
| 10 | અને જો એ પાણી Kangen હોય: તો ક્લોરિન બહાર, મિનરલ્સ અંદર, ને ઉપરથી હાઇડ્રોજન. | Kangen pour; three chips pop on the words |
| 11 | જાપાનમાં આવા મશીનને, પેટની તકલીફમાં સુધારા માટે, ઘરેલુ મેડિકલ ડિવાઇસની માન્યતા છે. | K8 machine, green stamp "✓ જાપાન: મેડિકલ ડિવાઇસ" |
| 12 | તમારા ઘરના પાણીથી ફરક જોવો હોય, તો આજે જ ફ્રી ડેમો બુક કરાવો. | end card: આજે જ ફ્રી ડેમો બુક કરાવો • Enagic Kangen • ચોટીલા |

## Host character
`../reel8/host.py` draws the host in code (SVG): a friendly young Gujarati man with a short beard, a checked
shirt and a steel glass. He is original, so nothing is borrowed. `../reel8/test_build.py` makes a 6-second talking
test: the mouth follows the loudness of the voice, and he blinks, bobs his head and lifts the glass. No outside tool
or key is needed. He is a flat 2D cartoon, not 3D or photoreal. There are no view numbers behind a cartoon host
(Dr. Pickle's median is 1,700 views a Short); the proven host is a real desi face. The same edit can take a phone
clip of a real person in the top panel in place of the drawing.

## Facts and sources
- Lemon gives vitamin C; cumin, fennel and ginger lines are traditional kitchen uses, worded as "helps".
- A glass of lemon or jeera water is about 99% water by composition.
- Bore water: CGWB lists Surendranagar among Gujarat districts with saline groundwater (EC above 3000 µS/cm) and
  fluoride above 1.5 mg/l in places: https://cgwb.gov.in/old_website/State-Profiles/Gujarat.pdf
- RO removes dissolved minerals with the dirt (NGT expert committee 2019; WHO, Kozisek 2005). 20-litre jars are
  usually RO water.
- Kangen: the carbon filter takes out chlorine, the minerals stay, and electrolysis adds dissolved hydrogen. It does
  not remove salts, so very salty bore water needs a pre-filter; the free demo tests the home's water first.
- Japan: household alkaline electrolysed-water generators are controlled medical devices whose stated purpose is
  "generation of alkaline electrolytic drinking water for improving gastrointestinal symptoms":
  https://www.3aaa.gr.jp/english/faq.html . The studies behind it are debated, so the script states the Japanese
  recognition only and makes no cure claim.

## Footage
For WhatsApp, Pinterest clips of each drink work (as before, credited but not licensed). For a public YouTube or
Instagram post, the owner can film six 5-second phone clips (lemon water, jeera water, variyali water, ginger
water, the bore or tap at home, the Kangen machine pouring). With the drawn host, the whole video is then original.
