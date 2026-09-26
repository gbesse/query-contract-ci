# query-contract-ci

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

Tests de contrats pour les réponses SQL d'un agent. Un contrat contient une petite base SQLite reproductible, une question métier, la requête de référence et les colonnes/lignes attendues. La CI échoue si une requête candidate change la réponse, notamment à cause d'une jointure qui duplique les montants.

## Démarrage

Python 3.11+, sans dépendance externe.

```bash
python3 query_contract.py examples/contract.json
python3 query_contract.py examples/contract.json --candidate examples/candidate-bug.json
python3 -m unittest discover -s tests -v
```

La première commande passe ; la deuxième sort avec le code `2` et montre `40` au lieu de `30` pour `ada`. `--candidate` accepte un objet JSON `{ "id_du_cas": "SELECT ..." }`. `--output report.json` enregistre le résultat. Les requêtes candidates sont exécutées en mode SQLite lecture seule.

## Périmètre

Le MVP compare les colonnes et lignes exactes, dans leur ordre. Il ne traduit pas le SQL d'autres moteurs, n'exécute pas de LLM et ne définit pas la vérité métier à votre place. Ajoutez vos schémas et réponses attendues avant de l'utiliser comme garde-fou.

Signaux : [EvoOntology](https://github.com/ruc-datalab/EvoOntology) et [dbt-llm-sl-bench](https://github.com/dbt-labs/dbt-llm-sl-bench).

Licence MIT. Contributions et contrats d'exemple bienvenus.
