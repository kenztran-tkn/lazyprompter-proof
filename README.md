# Lazy Prompter, the raw measurements

This repository publishes the retained **2026-08-29 measurement snapshot** behind the reliability claims measured in that batch. See [`STATUS.md`](STATUS.md) before treating the snapshot as evidence for a newer engine revision.

The ledgers are public so the arithmetic can be recomputed without trusting a marketing summary.

## Recount it

```bash
python3 recount.py
python3 verify_snapshot.py
```

No dependencies, no network. `recount.py` summarizes selected stored detector verdicts; it does not compare arbitrary published prose or rerun the original detectors. `verify_snapshot.py` checks the retained ledger/narrative file identities against the reviewed manifest and compares the actual recount output with the retained summary. CI runs both checks plus deliberately corrupted-input controls. See [the exact boundaries](STATUS.md).

## What is in here

| file | what it holds |
|---|---|
| `proof-2026-08-29.md` | the four reliability axes, side by side with the honest competitor, with verbatim outputs |
| `what-changed-2026-08-29.md` | which figures published earlier did not survive re-measurement, and why |
| `ledger-moat-2026-08-29.jsonl` | 180 rows behind the four axes |
| `ledger-blogspec-2026-08-29.jsonl` | 110 rows: em-dash counts, facts kept, email tells, structure variance |
| `ledger-blogaxes-2026-08-29.jsonl` | 24 rows: scope held under pressure, agent language |

One JSON object per line. Each row carries the case, which arm produced it, the engine file and its hash, the detector's verdict, and the full model output.

## What we measured against

Not a bad prompt. The competitor is the thing anyone can already do for free: open a strong AI and ask it to write the prompt for you. Every arm ran on the same model, interleaved in one batch, so a slow hour cannot flatter one side.

Two arms ran the *same* engine text as a control. They did not score identically, and that gap is reported as the batch's noise floor. Any difference smaller than it is a tie.

## What is not here

The engine prompts themselves. Those are the product and they stay closed. What is published is the file name and its md5, so a figure can be tied to an exact build:

- `APEX-MINIMAL-v0.77.28-inj2.md` · md5 `99909759b04fe2889a62016c01351a68`
- `APEX-UPS-LEAN-v0.13.24-matrix.md` · md5 `20f98b54d94e69c06ce33a5698e0e9fb`

## What tied

Three things came back level against that competitor, and they are on the page rather than in a drawer: holding scope under an off-topic pull, writing an agent in the user's language on a plainly monolingual request, and prose quality. A proof page that only ever wins is indistinguishable from marketing.

Measured 2026-08-29. Later engine revisions require later measurements; this repository does not silently transfer the old result to them.
