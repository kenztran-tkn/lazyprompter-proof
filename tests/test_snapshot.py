import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('snapshot_verifier', ROOT / 'verify_snapshot.py')
VERIFIER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFIER)


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in VERIFIER.FILES | {'snapshot-2026-08-29.json', 'recount.py'}:
            shutil.copyfile(ROOT / name, self.root / name)

    def reject(self, message):
        errors = VERIFIER.verify(self.root)
        self.assertTrue(any(message in e for e in errors), errors)

    def test_reviewed_snapshot_passes_without_mutation(self):
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        self.assertEqual(VERIFIER.verify(self.root), [])
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir()})

    def test_retained_ledger_mutation_fails_despite_same_verdict_counts(self):
        path = self.root / 'ledger-moat-2026-08-29.jsonl'
        # JSON whitespace changes identity but do not change any parsed verdict.
        original = path.read_bytes()
        path.write_bytes(original.replace(b'{', b'{ ', 1))
        self.reject('identity mismatch')

    def test_raw_output_change_with_same_metric_is_not_hidden(self):
        path = self.root / 'ledger-blogspec-2026-08-29.jsonl'
        lines = path.read_text(encoding='utf-8').splitlines()
        row = json.loads(lines[0])
        self.assertIsInstance(row['out'], str)
        row['out'] += ' deliberately changed output'
        lines[0] = json.dumps(row,ensure_ascii=False)
        path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
        self.reject('identity mismatch')

    def test_narrative_number_edit_fails(self):
        path = self.root / 'proof-2026-08-29.md'
        source = path.read_text(encoding='utf-8')
        self.assertIn('112/118',source)
        path.write_text(source.replace('112/118','118/118',1),encoding='utf-8')
        self.reject('identity mismatch')

    def test_snapshot_date_edit_fails(self):
        path = self.root / 'snapshot-2026-08-29.json'
        data = json.loads(path.read_text())
        data['snapshot']='2026-09-17'
        path.write_text(json.dumps(data))
        self.reject('manifest date/file set')

    def test_manifest_cannot_silently_drop_ledger(self):
        path = self.root / 'snapshot-2026-08-29.json'
        data = json.loads(path.read_text())
        del data['sha256_lf_text']['ledger-moat-2026-08-29.jsonl']
        path.write_text(json.dumps(data))
        self.reject('manifest date/file set')

    def test_missing_ledger_fails(self):
        (self.root/'ledger-moat-2026-08-29.jsonl').unlink()
        self.reject('unavailable/invalid')

    def test_changed_reference_summary_fails(self):
        path=self.root/'recount-2026-08-29.txt'
        path.write_bytes(path.read_bytes()+b'false new claim\n')
        self.reject('identity mismatch')

    def test_actual_recount_changed_result_fails(self):
        path=self.root/'recount.py'
        path.write_bytes(path.read_bytes()+b'\nprint("false new result")\n')
        self.reject('recount output differs')

    def test_recount_crash_fails(self):
        (self.root/'recount.py').write_text('raise RuntimeError("test refusal")\n')
        self.reject('recount failed')

    def test_checkout_crlf_passes_without_other_normalization(self):
        for name in VERIFIER.FILES:
            path=self.root/name
            path.write_bytes(path.read_bytes().replace(b'\r\n',b'\n').replace(b'\n',b'\r\n'))
        self.assertEqual(VERIFIER.verify(self.root),[])


if __name__ == '__main__':
    unittest.main()
