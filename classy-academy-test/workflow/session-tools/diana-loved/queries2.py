Q2 = {
'perfspray': ("spraying perfume getting ready morning vlog video", "a real woman spraying perfume on her wrist or neck while getting ready, ordinary home"),
'perfvanity': ("perfume collection vanity tray aesthetic video", "perfume bottles on a vanity tray or dresser, calm light, no hands or with a hand"),
'perfstore': ("woman testing perfume at department store counter video", "a woman testing perfume at a shop counter, smelling a blotter or her wrist"),
'perfold': ("elegant mature woman perfume routine video", "a woman over 45 putting on perfume, elegant"),
'olderwalk': ("stylish woman over 50 walking street outfit video", "a stylish woman over 50 walking in the street, real"),
'oldersmile': ("woman over 60 style smiling outfit video", "a woman over 60, well dressed, smiling, real"),
'leavehome': ("woman leaving apartment closing door morning outfit video", "a woman walking out of her front door in the morning, outfit"),
'dresstote': ("woman midi dress leather tote bag walking video", "a woman in a dress carrying a leather tote bag, walking"),
'shoetry': ("woman trying on shoes in shop mirror video", "a woman trying on shoes in a shop, looking at her feet in a mirror"),
'commentph': ("woman smiling typing on phone cozy video", "a woman smiling while typing on her phone"),
'diwalkb': ("princess diana walking film 1990s real footage video", "REAL archive film of Princess Diana walking, 1990s, no slideshow, no actress"),
}
open('q2.txt','w').write('\n'.join(f'{t}={q}' for t,(q,b) in Q2.items())+'\n')
open('briefs2.py','w').write('B2 = {\n'+''.join(f'{t!r}: {b!r},\n' for t,(q,b) in Q2.items())+'}\nB.update(B2)\n')
print(len(Q2))
