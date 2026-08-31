from __future__ import annotations

import random
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

Edge = Tuple[str, str]


@dataclass(frozen=True)
class LinkPredictionSplit:
    nodes: List[str]
    all_pos: Set[Edge]
    train_pos: List[Edge]
    val_pos: List[Edge]
    test_pos: List[Edge]
    train_neg: List[Edge]
    val_neg: List[Edge]
    test_neg: List[Edge]
    forest: Set[Edge]
    split_errors: List[str]
    original_components: int
    train_components: int
    seed: int
    val_ratio: float
    test_ratio: float
    negative_strategy: str

    def manifest(self, dataset_id: str, output_dir: Path) -> Dict[str, object]:
        return {
            "dataset_id": dataset_id,
            "seed": self.seed,
            "val_ratio": self.val_ratio,
            "test_ratio": self.test_ratio,
            "negative_strategy": self.negative_strategy,
            "nodes": len(self.nodes),
            "positive_edges_total_undirected": len(self.all_pos),
            "train_pos": len(self.train_pos),
            "val_pos": len(self.val_pos),
            "test_pos": len(self.test_pos),
            "train_neg": len(self.train_neg),
            "val_neg": len(self.val_neg),
            "test_neg": len(self.test_neg),
            "spanning_forest_edges_protected": len(self.forest),
            "original_components": self.original_components,
            "train_components": self.train_components,
            "train_components_preserved_by_construction": self.original_components == self.train_components,
            "split_errors": self.split_errors,
            "output_dir": str(output_dir),
        }


def normalize_edge(a: str, b: str) -> Edge:
    if a == b:
        raise ValueError("self-loops cannot be normalized as benchmark edges")
    return tuple(sorted((a, b)))


def infer_nodes(edges: Iterable[Edge]) -> List[str]:
    return sorted({node for edge in edges for node in edge})


def build_adjacency(edges: Set[Edge]) -> Dict[str, Set[str]]:
    adjacency: Dict[str, Set[str]] = defaultdict(set)
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    return adjacency


def spanning_forest_edges(edges: Set[Edge], nodes: List[str]) -> Set[Edge]:
    adjacency = build_adjacency(edges)
    seen: Set[str] = set()
    forest: Set[Edge] = set()
    for node in nodes:
        if node in seen:
            continue
        seen.add(node)
        queue: deque[str] = deque([node])
        while queue:
            current = queue.popleft()
            for neighbor in sorted(adjacency[current]):
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)
                forest.add(normalize_edge(current, neighbor))
    return forest


def component_count(edges: Set[Edge], nodes: List[str]) -> int:
    adjacency = build_adjacency(edges)
    seen: Set[str] = set()
    count = 0
    for node in nodes:
        if node in seen:
            continue
        count += 1
        seen.add(node)
        queue: deque[str] = deque([node])
        while queue:
            current = queue.popleft()
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
    return count


def sample_negative_edges(
    nodes: List[str],
    forbidden_edges: Set[Edge],
    count: int,
    rng: random.Random,
    max_attempt_factor: int = 100,
) -> List[Edge]:
    sampled: Set[Edge] = set()
    attempts = 0
    max_attempts = max(count * max_attempt_factor, 1)
    while len(sampled) < count:
        if attempts > max_attempts:
            raise RuntimeError("Too many attempts while sampling negative edges.")
        attempts += 1
        edge = normalize_edge(*rng.sample(nodes, 2))
        if edge in forbidden_edges or edge in sampled:
            continue
        sampled.add(edge)
    return sorted(sampled)


def log_degree_bin(degree: int, max_bin: int = 16) -> int:
    value = 0
    x = max(int(degree), 0) + 1
    while x > 1:
        x //= 2
        value += 1
    return min(value, max_bin)


def nodes_by_degree_bin(nodes: List[str], positive_edges: Set[Edge], max_bin: int = 16) -> Tuple[Dict[str, int], Dict[int, List[str]]]:
    adjacency = build_adjacency(positive_edges)
    bins_by_node: Dict[str, int] = {}
    grouped: Dict[int, List[str]] = defaultdict(list)
    for node in nodes:
        degree = len(adjacency.get(node, set()))
        degree_bin = log_degree_bin(degree, max_bin=max_bin)
        bins_by_node[node] = degree_bin
        grouped[degree_bin].append(node)
    return bins_by_node, {key: sorted(value) for key, value in grouped.items()}


def sample_degree_matched_negative_edges(
    nodes: List[str],
    positive_edges: Set[Edge],
    positive_template_edges: List[Edge],
    forbidden_edges: Set[Edge],
    count: int,
    rng: random.Random,
    max_bin: int = 16,
    max_attempt_factor: int = 300,
) -> List[Edge]:
    """Sample non-edges whose endpoint log-degree bins follow positive examples.

    Matching is approximate and uses degree bins from the complete observed
    positive graph. This controls the most direct degree-distribution shortcut
    while preserving a simple auditable sampler.
    """

    bins_by_node, grouped = nodes_by_degree_bin(nodes, positive_edges, max_bin=max_bin)
    sampled: Set[Edge] = set()
    templates = list(positive_template_edges)
    rng.shuffle(templates)
    attempts = 0
    max_attempts = max(count * max_attempt_factor, 1)

    def candidate_nodes(target_bin: int) -> List[str]:
        if target_bin in grouped and len(grouped[target_bin]) > 1:
            return grouped[target_bin]
        for radius in range(1, max_bin + 1):
            nearby = [b for b in (target_bin - radius, target_bin + radius) if b in grouped]
            candidates = [node for b in nearby for node in grouped[b]]
            if len(candidates) > 1:
                return candidates
        return nodes

    template_index = 0
    while len(sampled) < count:
        if attempts > max_attempts:
            raise RuntimeError("Too many attempts while sampling degree-matched negative edges.")
        attempts += 1
        if not templates:
            template = rng.choice(tuple(positive_edges))
        else:
            template = templates[template_index % len(templates)]
            template_index += 1
        left_bin = bins_by_node[template[0]]
        right_bin = bins_by_node[template[1]]
        if rng.random() < 0.5:
            left_bin, right_bin = right_bin, left_bin
        left_nodes = candidate_nodes(left_bin)
        right_nodes = candidate_nodes(right_bin)
        left = rng.choice(left_nodes)
        right = rng.choice(right_nodes)
        if left == right:
            continue
        edge = normalize_edge(left, right)
        if edge in forbidden_edges or edge in sampled:
            continue
        sampled.add(edge)

    return sorted(sampled)


def sample_two_hop_negative_edges(
    nodes: List[str],
    reference_edges: Set[Edge],
    forbidden_edges: Set[Edge],
    count: int,
    rng: random.Random,
    max_attempt_factor: int = 1000,
) -> List[Edge]:
    """Sample hard non-edges at distance two in a reference graph.

    The sampler draws pairs that share at least one neighbor in
    ``reference_edges`` but are absent from ``forbidden_edges``. For benchmark
    splits, the reference graph should be the training-positive graph to avoid
    using validation/test positives to define negative hardness.
    """

    adjacency = build_adjacency(reference_edges)
    centers = [node for node in nodes if len(adjacency.get(node, set())) >= 2]
    if not centers:
        raise RuntimeError("Cannot sample two-hop negatives without degree-2 centers.")

    sampled: Set[Edge] = set()
    attempts = 0
    max_attempts = max(count * max_attempt_factor, 1)
    while len(sampled) < count:
        if attempts > max_attempts:
            raise RuntimeError("Too many attempts while sampling two-hop negative edges.")
        attempts += 1
        center = rng.choice(centers)
        left, right = rng.sample(sorted(adjacency[center]), 2)
        edge = normalize_edge(left, right)
        if edge in forbidden_edges or edge in sampled:
            continue
        sampled.add(edge)
    return sorted(sampled)


def validate_split_sets(split_edges: Dict[str, Set[Edge]]) -> List[str]:
    errors: List[str] = []
    names = sorted(split_edges)
    for name, edges in split_edges.items():
        if any(a == b for a, b in edges):
            errors.append(f"{name} contains self-loops")
        if any(a > b for a, b in edges):
            errors.append(f"{name} contains unordered edges")
    for i, left in enumerate(names):
        for right in names[i + 1 :]:
            overlap = split_edges[left] & split_edges[right]
            if overlap:
                errors.append(f"{left} overlaps {right}: {len(overlap)} edges")
    return errors


def build_link_prediction_split(
    positive_edges: Iterable[Edge],
    nodes: Optional[Iterable[str]] = None,
    seed: int = 42,
    val_ratio: float = 0.10,
    test_ratio: float = 0.10,
    negative_strategy: str = "random",
) -> LinkPredictionSplit:
    all_pos = {normalize_edge(a, b) for a, b in positive_edges if a != b}
    node_list = sorted(nodes) if nodes is not None else infer_nodes(all_pos)
    rng = random.Random(seed)

    forest = spanning_forest_edges(all_pos, node_list)
    eligible = sorted(all_pos - forest)
    rng.shuffle(eligible)

    n_total = len(all_pos)
    n_val = int(n_total * val_ratio)
    n_test = int(n_total * test_ratio)
    if n_val + n_test > len(eligible):
        raise RuntimeError("Not enough non-forest edges for validation/test splits.")

    val_pos = sorted(eligible[:n_val])
    test_pos = sorted(eligible[n_val : n_val + n_test])
    holdout = set(val_pos) | set(test_pos)
    train_pos = sorted(all_pos - holdout)

    if negative_strategy == "random":
        train_neg = sample_negative_edges(node_list, all_pos, len(train_pos), rng)
        val_neg = sample_negative_edges(node_list, all_pos | set(train_neg), len(val_pos), rng)
        test_neg = sample_negative_edges(node_list, all_pos | set(train_neg) | set(val_neg), len(test_pos), rng)
    elif negative_strategy == "degree_matched":
        train_neg = sample_degree_matched_negative_edges(node_list, all_pos, train_pos, all_pos, len(train_pos), rng)
        val_neg = sample_degree_matched_negative_edges(
            node_list,
            all_pos,
            val_pos,
            all_pos | set(train_neg),
            len(val_pos),
            rng,
        )
        test_neg = sample_degree_matched_negative_edges(
            node_list,
            all_pos,
            test_pos,
            all_pos | set(train_neg) | set(val_neg),
            len(test_pos),
            rng,
        )
    elif negative_strategy == "two_hop":
        train_reference = set(train_pos)
        train_neg = sample_two_hop_negative_edges(node_list, train_reference, all_pos, len(train_pos), rng)
        val_neg = sample_two_hop_negative_edges(
            node_list,
            train_reference,
            all_pos | set(train_neg),
            len(val_pos),
            rng,
        )
        test_neg = sample_two_hop_negative_edges(
            node_list,
            train_reference,
            all_pos | set(train_neg) | set(val_neg),
            len(test_pos),
            rng,
        )
    else:
        raise ValueError(f"unknown negative_strategy: {negative_strategy}")

    split_sets = {
        "train_pos": set(train_pos),
        "val_pos": set(val_pos),
        "test_pos": set(test_pos),
        "train_neg": set(train_neg),
        "val_neg": set(val_neg),
        "test_neg": set(test_neg),
    }
    original_components = component_count(all_pos, node_list)
    train_components = component_count(set(train_pos), node_list)

    return LinkPredictionSplit(
        nodes=node_list,
        all_pos=all_pos,
        train_pos=train_pos,
        val_pos=val_pos,
        test_pos=test_pos,
        train_neg=train_neg,
        val_neg=val_neg,
        test_neg=test_neg,
        forest=forest,
        split_errors=validate_split_sets(split_sets),
        original_components=original_components,
        train_components=train_components,
        seed=seed,
        val_ratio=val_ratio,
        test_ratio=test_ratio,
        negative_strategy=negative_strategy,
    )
