# query-contract-ci

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Projets voisins et lacune visée

- [EvoOntology](https://github.com/ruc-datalab/EvoOntology) construit une couche d'ontologie évolutive pour les agents de données. Le besoin adjacent est de vérifier que les réponses métier restent justes quand les relations ou définitions évoluent.
- [dbt-llm-sl-bench](https://github.com/dbt-labs/dbt-llm-sl-bench) compare déjà des stratégies LLM sur des questions métier et des requêtes de référence. Notre MVP en reprend **le principe de comparaison des résultats**, à plus petite échelle : un contrat SQLite local à exécuter à chaque changement de SQL dans la CI.
- **Notre angle :** une régression précise et reproductible par question. Il n'y a encore ni adaptateur EvoOntology, ni adaptateur dbt.

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


Licence MIT. Contributions et contrats d'exemple bienvenus.
