from src.algos.graphs.traversal.bfs import bfs_iterative
from tests.test_helpers import adj_to_graph


def test_bfs():
    adj = [[0, 1], [1, 2], [2, 3], [3, 2], [3, 0]]
    graph = adj_to_graph(adj, 4)
    ans = []
    bfs_iterative(0, graph, ans)
    expected_ans = [[0, 1], [1, 2], [2, 3]]
    assert sorted(ans) == sorted(expected_ans)
