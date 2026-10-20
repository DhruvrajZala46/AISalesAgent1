# Topic demand table from dataset.json. Multiple = views / median views of the channel's latest <=60 long uploads.
# Windows use approximate (month-accurate) publish dates: last 90 days, 91-365 days, older. "Hit" = 3x or more; "big hit" = 5x or more.
import json, statistics as st, sys
D = json.load(open('dataset.json')); rows = [r for r in D['rows'] if r['multiple'] is not None and r['channel_id'] != 'UCJUn02MVnahA9My9-DUkTBQ']
def hit(r, x):
    return r['multiple'] >= x and (r['views'] or 0) >= 20000 and (r['channel_median'] or 0) >= 3000
def stats(rs):
    if not rs: return dict(n=0)
    m = [r['multiple'] for r in rs]; hits = [r for r in rs if hit(r, 3)]; big = [r for r in rs if hit(r, 5)]
    return dict(n=len(rs), channels=len({r['channel_id'] for r in rs}), median=round(st.median(m), 2), hits3=len(hits), hit_rate=round(len(hits) / len(rs), 3),
                hit_channels=len({r['channel_id'] for r in hits}), big5=len(big), big_channels=len({r['channel_id'] for r in big}))
topics = sorted({t for r in rows for t in r['topics']})
out = {}
for t in topics + ['ALL']:
    rs = rows if t == 'ALL' else [r for r in rows if t in r['topics']]
    a90 = [r for r in rs if r['age_days'] is not None and r['age_days'] <= 90]
    a365 = [r for r in rs if r['age_days'] is not None and 90 < r['age_days'] <= 365]
    old = [r for r in rs if r['age_days'] is not None and r['age_days'] > 365]
    out[t] = dict(all=stats(rs), last90=stats(a90), d91_365=stats(a365), older=stats(old),
                  top=[{k: r[k] for k in ('multiple', 'views', 'channel', 'title', 'date', 'url')} for r in sorted([r for r in rs if (r['channel_median'] or 0) >= 3000], key=lambda r: -r['multiple'])[:15]],
                  top90=[{k: r[k] for k in ('multiple', 'views', 'channel', 'title', 'date', 'url')} for r in sorted([r for r in a90 if (r['channel_median'] or 0) >= 3000], key=lambda r: -r['multiple'])[:10]])
json.dump(out, open('topics.json', 'w'), ensure_ascii=False, indent=1)
print(f"{'topic':38s} {'n':>5} {'ch':>4} {'med':>5} {'3x+':>4} {'ch3':>4} | 90d: {'n':>4} {'med':>5} {'3x+':>4} {'ch3':>4} {'rate':>5} | 91-365: {'n':>4} {'med':>5} {'rate':>5} {'ch3':>4}")
for t in sorted(out, key=lambda t: -(out[t]['last90'].get('hit_channels') or 0)):
    a, b, c = out[t]['all'], out[t]['last90'], out[t]['d91_365']
    print(f"{t[:38]:38s} {a['n']:5d} {a['channels']:4d} {a['median']:5.2f} {a['hits3']:4d} {a['hit_channels']:4d} | 90d: {b.get('n',0):4d} {b.get('median',0):5.2f} {b.get('hits3',0):4d} {b.get('hit_channels',0):4d} {b.get('hit_rate',0):5.3f} | 91-365: {c.get('n',0):4d} {c.get('median',0):5.2f} {c.get('hit_rate',0):5.3f} {c.get('hit_channels',0):4d}")
