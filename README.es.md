# query-contract-ci

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Proyectos relacionados y carencia abordada

- [EvoOntology](https://github.com/ruc-datalab/EvoOntology) crea una capa de ontología evolutiva para agentes de datos. La necesidad cercana es verificar que las respuestas de negocio sigan siendo correctas cuando cambian las relaciones o definiciones.
- [dbt-llm-sl-bench](https://github.com/dbt-labs/dbt-llm-sl-bench) ya compara estrategias LLM con preguntas de negocio y consultas de referencia. Nuestro MVP usa **el mismo principio de comparación de resultados** a menor escala: un contrato SQLite local para cada cambio de SQL en CI.
- **Nuestro enfoque:** una regresión precisa y reproducible por pregunta. Todavía no hay adaptadores para EvoOntology ni dbt.

Pruebas de contratos para las respuestas SQL de un agente. Un contrato incluye una base SQLite reproducible, una pregunta de negocio, SQL de referencia y columnas y filas esperadas. La CI falla si el SQL candidato cambia la respuesta, por ejemplo por una unión que duplica ingresos.

## Inicio rápido

Python 3.11+, sin dependencias externas.

```bash
python3 query_contract.py examples/contract.json
python3 query_contract.py examples/contract.json --candidate examples/candidate-bug.json
python3 -m unittest discover -s tests -v
```

La primera orden pasa; la segunda sale con código `2` y muestra `40` en vez de `30` para `ada`. `--candidate` acepta JSON como `{ "id_del_caso": "SELECT ..." }`. `--output report.json` guarda el resultado. Las consultas candidatas se ejecutan en SQLite de solo lectura.

## Alcance

El MVP compara columnas y filas exactas en su orden. No traduce otros dialectos SQL, no ejecuta un LLM ni decide la verdad de negocio. Añade tus esquemas y respuestas esperadas antes de usarlo como control.


Licencia MIT. Se aceptan contratos de ejemplo y contribuciones.
