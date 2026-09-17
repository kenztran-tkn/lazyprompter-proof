# Public proof status

**Latest retained public measurement snapshot:** 2026-08-29.

The three ledgers retain the measurement package for the exact engine builds identified by filename/hash inside the snapshot. They are **not evidence for a later engine revision**. The September17 qualification adds historical labels and accurate checker boundaries; it leaves every ledger byte in Git unchanged.

## What is current here

- measurement date: 2026-08-29;
- ledgers: `ledger-*-2026-08-29.jsonl`;
- narrative result: `proof-2026-08-29.md`;
- withdrawals/corrections from that run: `what-changed-2026-08-29.md`;
- recomputation program: `recount.py`.

## What CI proves

The GitHub workflow runs the recount, `verify_snapshot.py`, and isolated corruption controls. A green run establishes that:

- the three ledgers and two bounded historical narratives match `snapshot-2026-08-29.json`;
- actual recount output matches the retained `recount-2026-08-29.txt` summary;
- the specific deliberate corruptions in the test suite are refused.

File identity uses SHA256 after converting checkout CRLF line endings to LF only. No trimming, JSON reserialization or model-output normalization occurs. This is text identity across Git checkout platforms, not an assertion that arbitrary local disk bytes are identical. The verifier never refreshes the manifest; any deliberate snapshot/reference change requires a separate reviewed diff. Hashes provide consistency with that reviewed reference, not an independent signature of experimental truth.

`recount.py` alone only computes and prints selected totals from stored verdicts. It does not compare the narratives, rerun the detectors, validate every sentence/quote/p-value, or recompute the reported historical prose-quality panel. Narrative identity checks prevent unnoticed edits; they do not independently prove the narrative's interpretation. Original provenance is PR1 head `81cf25e6a19f07970ef7fd5cb56f54d97afd4f82`; the existing failures, ties, withdrawals and sample limits remain in the dated records.

It does **not** prove:

- that the 2026-08-29 engine is still deployed;
- that a newer engine retains the same behavior;
- that every product outcome is improved;
- that an old website claim remains valid after an engine change.
- that GitHub branch checks certify a live deployment or a new model-quality comparison.

## Freshness rule

A current-engine claim needs a measurement package tied to that exact engine build/hash. If the deployed or canonical engine changes, this snapshot remains historical evidence until a new independent run is published; do not relabel the old rows as current.

## Promotion rule

New public proof should arrive as a new dated snapshot rather than overwriting the 2026-08-29 ledgers. Preserve failures, ties, controls, noise-floor measurements, and withdrawn claims.
