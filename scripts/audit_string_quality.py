"""Quality audit for the downloaded STRING human physical network.

This script performs structural checks for the first BioGraphBench pilot:
- directed raw rows vs undirected collapsed pairs
- self-loops and duplicates
- connected components
- density and degree summary
- candidate link-prediction split policy notes
"""

from __future__ import annotations

import csv
import gzip
import json
from collections import Counter, deque
from pathlib import Path
from statistics import mean, median


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "9606.protein.physical.links.v12.0.txt.gz"
REPORTS_DIR = ROOT / "reports"


def quantile(values: list[int], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = (len(ordered) - 1) * q
    lower = int(idx)
    upper = min(lower + 1, len(ordered) - 1)
    weight = idx - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def connected_components(adjacency: dict[str, set[str]]) -> list[int]:
    seen: set[str] = set()
    sizes: list[int] = []
    for node in adjacency:
        if node in seen:
            continue
        queue: deque[str] = deque([node])
        seen.add(node)
        size = 0
        while queue:
            current = queue.popleft()
            size += 1
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def audit() -> dict[str, object]:
    directed_edges: Counter[tuple[str, str]] = Counter()
    undirected_scores: dict[tuple[str, str], int] = {}
    adjacency: dict[str, set[str]] = {}
    self_loops = 0
    raw_rows = 0
    scores: list[int] = []

    with gzip.open(RAW_PATH, "rt", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter=" ")
        for row in reader:
            a = row["protein1"]
            b = row["protein2"]
            score = int(row["combined_score"])
            raw_rows += 1
            scores.append(score)
            directed_edges[(a, b)] += 1
            if a == b:
                self_loops += 1
                continue
            pair = tuple(sorted((a, b)))
            undirected_scores[pair] = max(score, undirected_scores.get(pair, score))
            adjacency.setdefault(a, set()).add(b)
            adjacency.setdefault(b, set()).add(a)

    nodes = set(adjacency)
    components = connected_components(adjacency)
    degrees = [len(adjacency[node]) for node in nodes]
    possible_undirected_edges = len(nodes) * (len(nodes) - 1) / 2
    density = len(undirected_scores) / possible_undirected_edges if possible_undirected_edges else 0.0

    directed_duplicates = sum(count - 1 for count in directed_edges.values() if count > 1)
    symmetric_excess = len(directed_edges) - len(undirected_scores) - self_loops

    return {
        "dataset_id": "string_human_physical_v12",
        "raw_rows": raw_rows,
        "directed_unique_edges": len(directed_edges),
        "directed_duplicate_edges": directed_duplicates,
        "self_loops": self_loops,
        "undirected_edges_after_collapse": len(undirected_scores),
        "symmetric_excess_rows": symmetric_excess,
        "nodes": len(nodes),
        "connected_components": len(components),
        "largest_component_nodes": components[0] if components else 0,
        "largest_component_ratio": components[0] / len(nodes) if nodes else 0.0,
        "density": density,
        "average_degree": mean(degrees) if degrees else 0.0,
        "median_degree": median(degrees) if degrees else 0.0,
        "min_degree": min(degrees) if degrees else 0,
        "max_degree": max(degrees) if degrees else 0,
        "degree_q25": quantile(degrees, 0.25),
        "degree_q75": quantile(degrees, 0.75),
        "score_min": min(scores) if scores else 0,
        "score_q25": quantile(scores, 0.25),
        "score_median": quantile(scores, 0.50),
        "score_q75": quantile(scores, 0.75),
        "score_max": max(scores) if scores else 0,
    }


def write_reports(result: dict[str, object]) -> None:
    json_path = REPORTS_DIR / "string_quality_audit.json"
    json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    csv_path = REPORTS_DIR / "string_quality_audit.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(result))
        writer.writeheader()
        writer.writerow(result)

    md = f"""# STRING Human Physical v12.0 - Quality Audit

Fecha de auditoria: 2026-08-04

## Resumen

| Medida | Valor |
|---|---:|
| Filas crudas dirigidas | {result['raw_rows']} |
| Aristas dirigidas unicas | {result['directed_unique_edges']} |
| Duplicados dirigidos exactos | {result['directed_duplicate_edges']} |
| Self-loops | {result['self_loops']} |
| Aristas no dirigidas tras colapsar A-B/B-A | {result['undirected_edges_after_collapse']} |
| Filas simetricas excedentes | {result['symmetric_excess_rows']} |
| Nodos | {result['nodes']} |
| Componentes conectados | {result['connected_components']} |
| Nodos en componente principal | {result['largest_component_nodes']} |
| Ratio componente principal | {result['largest_component_ratio']:.6f} |
| Densidad no dirigida | {result['density']:.8f} |
| Grado medio | {result['average_degree']:.4f} |
| Grado mediano | {result['median_degree']} |
| Grado maximo | {result['max_degree']} |
| Score minimo | {result['score_min']} |
| Score mediano | {result['score_median']} |
| Score maximo | {result['score_max']} |

## Interpretacion

STRING physical viene como tabla de asociaciones proteina-proteina con pares simetricos. Para una tarea PPI no dirigida, el grafo debe colapsar `A-B` y `B-A` en una sola arista, conservando el mayor `combined_score` observado.

No se observan self-loops ni duplicados dirigidos exactos en la tabla cruda. La red es muy conectada: el componente principal contiene casi todos los nodos, por lo que es viable construir splits de link prediction preservando conectividad.

## Propuesta de tarea sin leakage

Tarea inicial: link prediction no dirigida en STRING human physical v12.0.

Politica propuesta:

1. Colapsar pares simetricos antes de construir el grafo final.
2. Remover self-loops si aparecieran en futuras versiones.
3. Separar aristas positivas de validacion/test antes de calcular cualquier feature estructural.
4. Mantener una version de entrenamiento conectada, evitando que el split fragmente excesivamente el componente principal.
5. Generar negativos solo entre pares de proteinas no conectadas en el grafo completo auditado.
6. Usar los mismos negativos para todos los modelos comparables dentro de cada seed.
7. Reportar AUROC y AUPRC; por desbalance, priorizar AUPRC.

## Riesgos abiertos

- STRING es una red de asociaciones con evidencia integrada, no interacciones experimentales puras.
- Los scores derivan de multiples fuentes de evidencia; si se usan como features o pesos, deben separarse de la etiqueta de existencia de arista.
- Hay que decidir si el umbral minimo de confianza sera 150, 400, 700 u otro, y reportarlo como ablacion o configuracion fija.
"""
    (REPORTS_DIR / "string_quality_audit.md").write_text(md, encoding="utf-8")


def main() -> int:
    result = audit()
    write_reports(result)
    print(
        "STRING audit complete: "
        f"{result['nodes']} nodes, "
        f"{result['undirected_edges_after_collapse']} undirected edges, "
        f"{result['connected_components']} components"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
