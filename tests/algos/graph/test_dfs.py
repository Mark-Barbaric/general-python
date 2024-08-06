from src.algos.graphs.dfs import dfs_all_paths_from_source_to_target, dfs_iterative, dfs_recursive
from tests.test_helpers import adj_to_graph


def test_dfs_recursive():
    adj = [[0, 1], [1, 2], [2, 3], [3, 2], [3, 0]]
    graph = adj_to_graph(adj, 4)
    visited = [False for _ in range(4)]
    ans = []
    dfs_recursive(-1, 0, graph, visited, ans)
    expected_ans = [[0, 1], [1, 2], [2, 3]]
    assert sorted(ans) == sorted(expected_ans)


def test_dfs_iterative():
    adj = [[0, 1], [1, 2], [2, 3], [3, 2], [3, 0]]
    graph = adj_to_graph(adj, 4)
    ans = []
    dfs_iterative(0, graph, ans)
    expected_ans = [[0, 1], [1, 2], [2, 3]]
    assert sorted(ans) == sorted(expected_ans)


def test_dfs_all_paths_from_source_to_target():
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    visited = [False for _ in range(len(graph))]
    ans = []
    dfs_all_paths_from_source_to_target(0, len(graph) - 1, graph, visited, [], ans)
    expected_ans = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    assert sorted(ans) == sorted(expected_ans)
