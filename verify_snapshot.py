#!/usr/bin/env python3
"""Verify retained text identities and an actually recomputed, bounded summary."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = {
    'ledger-moat-2026-08-29.jsonl', 'ledger-blogspec-2026-08-29.jsonl',
    'ledger-blogaxes-2026-08-29.jsonl', 'proof-2026-08-29.md',
    'what-changed-2026-08-29.md', 'recount-2026-08-29.txt',
}


def text_bytes(data):
    # Only checkout line endings; escaped newlines inside JSON outputs stay exact.
    return data.replace(b'\r\n', b'\n')


def verify(root=ROOT):
    errors = []
    try:
        manifest = json.loads((root / 'snapshot-2026-08-29.json').read_text(encoding='utf-8'))
        hashes = manifest['sha256_lf_text']
        if manifest['snapshot'] != '2026-08-29' or set(hashes) != FILES:
            return ['snapshot manifest date/file set differs from this verifier contract']
        for name in sorted(FILES):
            actual = hashlib.sha256(text_bytes((root / name).read_bytes())).hexdigest()
            if actual != hashes[name]:
                errors.append(f'snapshot text identity mismatch: {name}')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f'snapshot input unavailable/invalid: {exc}']
    if errors:
        return errors
    try:
        run = subprocess.run([sys.executable, '-X', 'utf8', str(root / 'recount.py')],
            cwd=root, capture_output=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return [f'recount could not complete: {exc}']
    if run.returncode != 0:
        errors.append(f'recount failed with exit{run.returncode}')
    elif run.stderr:
        errors.append('recount emitted unexpected stderr; inspect before accepting')
    elif text_bytes(run.stdout) != text_bytes((root / 'recount-2026-08-29.txt').read_bytes()):
        errors.append('recount output differs from the retained summary')
    return errors


if __name__ == '__main__':
    failures = verify()
    print('SNAPSHOT VERIFY: ' + ('FAIL' if failures else 'PASS'))
    for failure in failures:
        print('- ' + failure)
    if not failures:
        print('Bound: reviewed snapshot text identities and selected stored-verdict summary; no new experiment.')
    raise SystemExit(bool(failures))
