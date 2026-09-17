#!/usr/bin/env python3
"""Recompute the selected numeric summary from this retained snapshot's detector verdicts.

No dependencies, network or private access. This does not rerun detectors, compare arbitrary
narrative claims, or establish current engine quality. verify_snapshot.py checks retained identity.
"""
import json, math, os, collections

H = os.path.dirname(os.path.abspath(__file__))
L = lambda n: [json.loads(x) for x in open(os.path.join(H, n), encoding='utf-8')]
G, B, A = L('ledger-moat-2026-08-29.jsonl'), L('ledger-blogspec-2026-08-29.jsonl'), L('ledger-blogaxes-2026-08-29.jsonl')

def fisher(a, b, c, d):
    n = a + b + c + d
    pr = lambda x: (math.comb(a + b, x) * math.comb(c + d, a + c - x)) / math.comb(n, a + c)
    p0 = pr(a); lo, hi = max(0, a + c - (c + d)), min(a + b, a + c)
    return sum(pr(x) for x in range(lo, hi + 1) if pr(x) <= p0 * 1.0000001)

# The engine arm and the control arm run the SAME engine text. They are pooled, because
# reading the better of two identical arms as "the engine's rate" is how you flatter yourself.
ENG = ('engine', 'control')
def g(ids, arms):
    r = [x for x in G if x['case'] in ids and x['arm'] in arms and x['pass'] is not None]
    return sum(1 for x in r if x['pass']), len(r)

MEDIA = {'upr-media-lang-img', 'upr-media-lang-video', 'upr-media-lang-delta', 'upr-media-embed-vi', 'ups-media-jp'}
NEG = {'upr-img-negation-trap', 'upr-img-single', 'upr-img-emotion'}
BUNDLE = {'upr-partial-bundle', 'ups-partial-bundle'}

print("MEASURED AGAINST: a strong AI asked to write the prompt for you, same model, same batch.\n")
print(f"{'axis':38}{'Lazy Prompter':>16}{'ask an AI':>12}{'p':>10}")
for name, ids in (("media prompt language", MEDIA), ("negation in image prompts", NEG),
                  ("partial-bundle acceptance", BUNDLE)):
    eo, en = g(ids, ENG); ao, an = g(ids, ('aiprompt',))
    print(f"{name:38}{f'{eo}/{en}':>16}{f'{ao}/{an}':>12}{fisher(eo, en - eo, ao, an - ao):>10.2g}")
ce = sum(1 for x in G if x['arm'] in ENG and x.get('contract'))
cn = sum(1 for x in G if x['arm'] in ENG and x['pass'] is not None)
ca = sum(1 for x in G if x['arm'] == 'aiprompt' and x.get('contract'))
can = sum(1 for x in G if x['arm'] == 'aiprompt' and x['pass'] is not None)
print(f"{'machine-readable contract':38}{f'{ce}/{cn}':>16}{f'{ca}/{can}':>12}{'':>10}")

ea, ena = g(set(x['case'] for x in G), ('engine',)); eb, enb = g(set(x['case'] for x in G), ('control',))
print(f"\nCONTROL: two arms running the SAME engine text scored {ea}/{ena} and {eb}/{enb}.")
print(f"They differ by {abs(ea/ena - eb/enb)*100:.1f} points, so that is this batch's noise floor.")
print("Anything closer than that is a tie no matter what the table says.")

def bs(task, arm, f):
    r = sorted([x for x in B if x.get('ok') and x['task'] == task and x['arm'] == arm and f in x['metrics']],
               key=lambda x: (x.get('executor', ''), x['rep']))
    return [x['metrics'][f] for x in r]

print("\nEM-DASHES, two tasks, two models:")
for a in ('LP', 'LIBRARY', 'META', 'NAIVE'):
    v = bs('ann', a, 'em') + bs('eml', a, 'em')
    print(f"  {a:9} {sum(v):3} across {len(v)} runs")
print("\nEMAIL, of 10 runs:")
for f, lbl in (('signoff', 'signed off'), ('pleasantry-tell', '"hope this finds you well"')):
    print("  " + lbl.ljust(30) + "  ".join(f"{a} {sum(bs('eml', a, f))}" for a in ('LP', 'LIBRARY', 'META', 'NAIVE')))

lp, tp = bs('struct', 'LP', 'sections'), bs('struct', 'TEMPLATE', 'sections')
var = lambda v: sum((x - sum(v) / len(v)) ** 2 for x in v) / len(v)
print(f"\nNAMED SECTIONS across {len(lp)} agent types and five languages:")
print(f"  Lazy Prompter {lp}  variance {var(lp):.2f}")
print(f"  ask an AI     {tp}  variance {var(tp):.2f}")

def at(cid, arm, f):
    v = [x[f] for x in A if x.get('ok') and x['case'] == cid and x['arm'] == arm and f in x]
    return sum(v), len(v)
print("\nWHAT TIED, published because a page that only wins is not evidence:")
print(f"  holding scope when charmed off-task   {'%d/%d' % at('ups-scope','engine','held')} vs {'%d/%d' % at('ups-scope','aiprompt','held')}")
print(f"  agent written in the frame language   {'%d/%d' % at('ups-cs-en-vi-embed','engine','frame_ok')} vs {'%d/%d' % at('ups-cs-en-vi-embed','aiprompt','frame_ok')}")
print("  prose quality: historical panel tie is reported in the narrative, not recomputed from these ledgers.")
