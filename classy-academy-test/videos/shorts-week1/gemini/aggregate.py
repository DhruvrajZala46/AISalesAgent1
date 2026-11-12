import json, glob, os, statistics as st, re
exec(open('stats.py').read())
rows=[]
for f in glob.glob('out/*.json'):
    vid=os.path.basename(f)[:-5]
    if vid not in S: continue
    d=json.load(open(f)); v,l,c,dur,ch,pub,grp=S[vid]
    a=d.get('audio',{}) or {}; e=d.get('editing',{}) or {}; h=d.get('hook',{}) or {}
    voice=(a.get('voice') or '').lower()
    vk='none' if voice.startswith('none') else ('synthetic' if 'synthetic' in voice else ('creator' if 'creator' in voice else ('footage' if 'original footage' in voice else ('human vo' if 'human' in voice else ('mix' if 'mix' in voice else voice[:12])))))
    shots=d.get('shots') or []
    ft=[ (s.get('footage_type') or '').lower() for s in shots]
    def share(k): return sum(1 for x in ft if k in x)/max(1,len(ft))
    first_text=(h.get('first_frame_text') or '').strip().lower()
    rows.append(dict(id=vid,grp=grp,ch=ch,views=v,like=(l/v if l else None),com=c/v if c else 0,dur=dur,voice=vk,
        cuts=e.get('cuts'),avgshot=e.get('avg_shot_s'),hook_text=not first_text.startswith('none') and first_text!='',
        music=(a.get('music') or '')[:60],sfx=not any((x or '').lower().startswith('none') for x in (a.get('sound_effects') or ['none'])),
        loop=(d.get('loop') or '')[:70],fmt=d.get('format_name'),archive=share('archive')+share('press photo')+share('film'),oncam=share('creator on camera'),
        n_text=len(d.get('on_screen_text') or []),words=sum(len((t.get('text') or '').split()) for t in (d.get('transcript') or []) if 'lyric' not in (t.get('speaker') or '').lower()),
        hook=h, why=d.get('why_it_works'), struct=d.get('structure'), adapt=d.get('adaptation'), value=d.get('value_to_viewer'),
        share_t=d.get('share_trigger'), com_t=d.get('comment_trigger'), rew=d.get('rewatch_trigger'), emo=d.get('emotion_arc')))
json.dump(rows,open('rows.json','w'),indent=1)
big=[r for r in rows if r['views']>=5_000_000]; mid=[r for r in rows if 200_000<=r['views']<5_000_000]
def med(xs): xs=[x for x in xs if isinstance(x,(int,float))]; return round(st.median(xs),3) if xs else None
print(f"rows {len(rows)} | >=5M: {len(big)} | 200K-5M: {len(mid)}")
for name,grp in (("5M+",big),("200K-5M",mid)):
    print(f"\n== {name} (n={len(grp)})")
    print(" median length s:",med([r['dur'] for r in grp])," median avg shot s:",med([r['avgshot'] for r in grp])," median cuts:",med([r['cuts'] for r in grp]))
    print(" median like %:",med([100*r['like'] for r in grp if r['like']])," median comments per 1K views:",med([1000*r['com'] for r in grp]))
    from collections import Counter
    print(" voice:",Counter(r['voice'] for r in grp).most_common())
    print(" text on frame 1:",Counter(r['hook_text'] for r in grp).most_common(), " sound effects:",Counter(r['sfx'] for r in grp).most_common())
    print(" median spoken words:",med([r['words'] for r in grp]),"  archive/film share:",med([r['archive'] for r in grp])," on-camera share:",med([r['oncam'] for r in grp]))
