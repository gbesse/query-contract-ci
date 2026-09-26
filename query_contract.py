"""Verify SQL answers against business-level contracts in SQLite."""
import argparse
import json
from pathlib import Path
import sqlite3
import sys


def check(contract, candidates=None):
    reports = []
    for case in contract['cases']:
        connection = sqlite3.connect(':memory:')
        try:
            connection.executescript(contract['setup_sql'])
            connection.execute('PRAGMA query_only = ON')
            sql = (candidates or {}).get(case['id'], case['sql'])
            try:
                cursor = connection.execute(sql)
                columns = [item[0] for item in cursor.description or []]
                rows = [list(row) for row in cursor.fetchall()]
                passed = columns == case['expected_columns'] and rows == case['expected_rows']
                reports.append({'id': case['id'], 'pass': passed, 'columns': columns, 'rows': rows,
                                'expected_columns': case['expected_columns'], 'expected_rows': case['expected_rows']})
            except sqlite3.Error as exc:
                reports.append({'id': case['id'], 'pass': False, 'error': str(exc)})
        finally:
            connection.close()
    return {'pass': all(item['pass'] for item in reports), 'cases': reports}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('contract', type=Path)
    parser.add_argument('--candidate', type=Path, help='JSON mapping case IDs to candidate SQL')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    contract = json.loads(args.contract.read_text())
    candidates = json.loads(args.candidate.read_text()) if args.candidate else None
    report = check(contract, candidates)
    encoded = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(encoded + '\n')
    print(encoded)
    return 0 if report['pass'] else 2


if __name__ == '__main__':
    sys.exit(main())
