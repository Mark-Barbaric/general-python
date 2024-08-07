from src.algos.graphs.paths import print_bidirectional_paths


def test_single_connected_graph():
    n = 3
    graph = [[1, 2], [0, 2], [0, 1]]
    ans = print_bidirectional_paths(0, graph, n)
    assert ans == [[0, 1, 2], [0, 2, 1]]
