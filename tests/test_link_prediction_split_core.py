import pytest

from biographbench.splits import build_adjacency, build_link_prediction_split, component_count, spanning_forest_edges


def test_spanning_forest_preserves_component_count_in_train_split():
    edges = {
        ("a", "b"),
        ("b", "c"),
        ("a", "c"),
        ("d", "e"),
        ("d", "f"),
        ("e", "f"),
    }
    nodes = ["a", "b", "c", "d", "e", "f"]

    split = build_link_prediction_split(edges, nodes=nodes, seed=7, val_ratio=0.2, test_ratio=0.2)

    assert split.original_components == 2
    assert split.train_components == 2
    assert component_count(set(split.train_pos), nodes) == component_count(edges, nodes)
    assert set(split.train_pos).issuperset(spanning_forest_edges(edges, nodes))
    assert split.split_errors == []


def test_negative_edges_do_not_overlap_positive_or_each_other():
    edges = {
        ("a", "b"),
        ("b", "c"),
        ("c", "d"),
        ("a", "c"),
        ("b", "d"),
        ("c", "e"),
        ("d", "e"),
        ("e", "f"),
        ("f", "g"),
    }
    split = build_link_prediction_split(edges, seed=11, val_ratio=0.2, test_ratio=0.2)

    positives = set(split.train_pos) | set(split.val_pos) | set(split.test_pos)
    negatives = set(split.train_neg) | set(split.val_neg) | set(split.test_neg)

    assert positives == split.all_pos
    assert positives.isdisjoint(negatives)
    assert len(negatives) == len(split.train_neg) + len(split.val_neg) + len(split.test_neg)


def test_two_hop_negative_edges_share_train_neighbor():
    edges = {
        ("a", "b"),
        ("a", "c"),
        ("a", "d"),
        ("b", "e"),
        ("c", "f"),
        ("d", "g"),
        ("e", "f"),
        ("f", "g"),
        ("b", "h"),
        ("c", "i"),
        ("d", "j"),
        ("h", "i"),
        ("i", "j"),
    }
    split = build_link_prediction_split(edges, seed=13, val_ratio=0.1, test_ratio=0.1, negative_strategy="two_hop")
    train_adjacency = build_adjacency(set(split.train_pos))

    for left, right in split.train_neg + split.val_neg + split.test_neg:
        assert (left, right) not in split.all_pos
        assert train_adjacency[left] & train_adjacency[right]


def test_split_raises_when_holdout_would_break_forest_policy():
    edges = {("a", "b"), ("b", "c")}

    with pytest.raises(RuntimeError, match="Not enough non-forest edges"):
        build_link_prediction_split(edges, seed=1, val_ratio=0.5, test_ratio=0.5)
