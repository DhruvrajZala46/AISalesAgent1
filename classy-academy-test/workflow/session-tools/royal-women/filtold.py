# comment out picks from creator accounts used in earlier videos (old media gone, so footage cannot be compared); Diana archive tags are checked by frames instead
import json, re
users = set(json.load(open('old_used.json'))['users']); reels = set(json.load(open('old_used.json'))['reels'])
DI = {'rgrace','rgracep','rmargaret','rqm','rqueen','rdiana','rkate','rletizia','rmargfilm','rqmfilm','rgracefilm','rletwalk','rqueenwalk','rmargb','rgraceb','rqueenb'}
out = []; dropped = []
for l in open('picks.md'):
    m = re.match(r'([a-z]+): (.*)', l)
    if not m or m.group(1) in DI: out.append(l.rstrip('\n')); continue
    tag = m.group(1); pins = json.load(open(f'pin/{tag}.json')); keep = []; rej = []
    for k in m.group(2).split():
        p = pins[int(k[len(tag):])]
        if (p.get('creator_user') or '').lower() in users or any(r in (p.get('src_link') or '') for r in reels): rej.append(k)
        else: keep.append(k)
    if keep: out.append(f'{tag}: ' + ' '.join(keep))
    if rej: out.append(f'# rejected after screening ({tag}): ' + ' '.join(rej)); dropped += rej
open('picks.md', 'w').write('\n'.join(out) + '\n'); print(len(dropped), 'picks dropped (accounts used before):', ' '.join(dropped))
