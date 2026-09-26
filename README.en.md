# query-contract-ci

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Related projects and target gap

- [EvoOntology](https://github.com/ruc-datalab/EvoOntology) builds an evolving ontology layer for data agents. The adjacent need is to check that business answers remain correct as relationships or definitions change.
- [dbt-llm-sl-bench](https://github.com/dbt-labs/dbt-llm-sl-bench) already compares LLM strategies on business questions and reference queries. Our MVP uses **the same result-comparison principle** on a smaller scale: a local SQLite contract for each SQL change in CI.
- **Our angle:** one precise, reproducible regression per question. EvoOntology and dbt adapters do not exist yet.

Contract tests for an agent's SQL answers. A contract contains a reproducible SQLite database, a business question, reference SQL, and expected columns and rows. CI fails when candidate SQL changes the answer, including join fanout that duplicates revenue.

## Quick start

Python 3.11+, no external dependencies.

```bash
python3 query_contract.py examples/contract.json
python3 query_contract.py examples/contract.json --candidate examples/candidate-bug.json
python3 -m unittest discover -s tests -v
```

The first command passes; the second exits `2` and shows `40` instead of `30` for `ada`. `--candidate` accepts JSON shaped like `{ "case_id": "SELECT ..." }`. `--output report.json` saves the result. Candidate queries run in SQLite read-only mode.

## Scope

The MVP compares exact columns and rows in order. It does not translate other SQL dialects, run an LLM, or decide business truth for you. Add your own schema and expected answers before relying on it as a gate.


MIT licensed. Example contracts and contributions are welcome.
