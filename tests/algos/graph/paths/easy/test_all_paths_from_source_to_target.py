from src.algos.graphs.paths import all_paths_from_source_to_target


def test_dfs_all_paths_from_source_to_target():
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    visited = [False for _ in range(len(graph))]
    ans = []
    all_paths_from_source_to_target(0, len(graph) - 1, graph, visited, [], ans)
    expected_ans = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    assert sorted(ans) == sorted(expected_ans)
