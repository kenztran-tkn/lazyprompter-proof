# Public proof status

**Latest retained public measurement snapshot:** 2026-08-29.

The files in this repository are an immutable measurement package for the exact engine builds identified by filename/hash inside the snapshot. They are **not automatically evidence for a later engine revision**.

## What is current here

- measurement date: 2026-08-29;
- ledgers: `ledger-*-2026-08-29.jsonl`;
- narrative result: `proof-2026-08-29.md`;
- withdrawals/corrections from that run: `what-changed-2026-08-29.md`;
- recomputation program: `recount.py`.

## What CI proves

The GitHub workflow runs `python3 recount.py` on every change. A green run means the published arithmetic is reproducible from the retained ledgers.

It does **not** prove:

- that the 2026-08-29 engine is still deployed;
- that a newer engine retains the same behavior;
- that every product outcome is improved;
- that an old website claim remains valid after an engine change.

## Freshness rule

A current-engine claim needs a measurement package tied to that exact engine build/hash. If the deployed or canonical engine changes, this snapshot remains historical evidence until a new independent run is published; do not relabel the old rows as current.

## Promotion rule

New public proof should arrive as a new dated snapshot rather than overwriting the 2026-08-29 ledgers. Preserve failures, ties, controls, noise-floor measurements, and withdrawn claims.
