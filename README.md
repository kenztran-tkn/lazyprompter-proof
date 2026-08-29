# Lazy Prompter, the raw measurements

Every reliability figure Lazy Prompter publishes comes from the ledgers in this repository.
They are here so you do not have to take our arithmetic on faith.

## Recount it

```
python3 recount.py
```

No dependencies, no network. It reads the ledgers next to it and recomputes every published
figure. If a number it prints differs from a number on our blog, the blog is wrong and we
want to know.

## What is in here

| file | what it holds |
|---|---|
| `proof-2026-08-29.md` | the four reliability axes, side by side with the honest competitor, with verbatim outputs |
| `what-changed-2026-08-29.md` | which figures we published earlier did not survive re-measurement, and why |
| `ledger-moat-2026-08-29.jsonl` | 180 rows behind the four axes |
| `ledger-blogspec-2026-08-29.jsonl` | 110 rows: em-dash counts, facts kept, email tells, structure variance |
| `ledger-blogaxes-2026-08-29.jsonl` | 24 rows: scope held under pressure, agent language |

One JSON object per line. Each row carries the case, which arm produced it, the engine file
and its hash, the detector's verdict, and the full model output.

## What we measured against

Not a bad prompt. The competitor is the thing anyone can already do for free: open a strong
AI and ask it to write the prompt for you. Every arm ran on the same model, interleaved in
one batch, so a slow hour cannot flatter one side.

Two arms ran the *same* engine text as a control. They did not score identically, and that
gap is reported as the batch's noise floor. Any difference smaller than it is a tie.

## What is not here

The engine prompts themselves. Those are the product and they stay closed. What is published
is the file name and its md5, so a figure can be tied to an exact build:

- `APEX-MINIMAL-v0.77.28-inj2.md` · md5 `99909759b04fe2889a62016c01351a68`
- `APEX-UPS-LEAN-v0.13.24-matrix.md` · md5 `20f98b54d94e69c06ce33a5698e0e9fb`

## What tied

Three things came back level against that competitor, and they are on the page rather than
in a drawer: holding scope under an off-topic pull, writing an agent in the user's language
on a plainly monolingual request, and prose quality. A proof page that only ever wins is
indistinguishable from marketing.

Measured 2026-08-29.
