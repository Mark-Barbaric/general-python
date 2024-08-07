from src.algos.graphs.paths import valid_path_in_bidirection_graph


def test_single_connected_graph():
    edges = [[0, 1], [1, 2], [2, 0]]
    assert valid_path_in_bidirection_graph(3, edges, 0, 2)
    edges = [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]]
    assert valid_path_in_bidirection_graph(10, edges, 7, 5)
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    assert not valid_path_in_bidirection_graph(10, edges, 0, 5)
