import json
import unittest
from pathlib import Path
from query_contract import check

EXAMPLES = Path(__file__).resolve().parents[1] / 'examples'


class ContractTests(unittest.TestCase):
    def test_golden_query_passes(self):
        contract = json.loads((EXAMPLES / 'contract.json').read_text())
        self.assertTrue(check(contract)['pass'])

    def test_join_fanout_regression_fails(self):
        contract = json.loads((EXAMPLES / 'contract.json').read_text())
        candidate = json.loads((EXAMPLES / 'candidate-bug.json').read_text())
        report = check(contract, candidate)
        self.assertFalse(report['pass'])
        self.assertEqual(report['cases'][0]['rows'][0], ['ada', 40])

    def test_write_is_rejected(self):
        contract = json.loads((EXAMPLES / 'contract.json').read_text())
        report = check(contract, {'revenue_by_customer': 'DELETE FROM orders'})
        self.assertFalse(report['pass'])
