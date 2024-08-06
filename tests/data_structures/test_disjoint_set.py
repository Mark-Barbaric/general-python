from src.data_structures.graphs.disjoint_set import DisjointSet, DisjointSet2


def test_disjoint_set():
    adj = [[0, 1], [0, 2], [1, 3], [4, 8], [5, 6], [5, 7]]
    size = 9
    disjoint_set = DisjointSet(size=size)
    assert disjoint_set.size == size

    for i, j in adj:
        disjoint_set.union(i, j)

    assert disjoint_set.connected(0, 1)
    assert not disjoint_set.connected(2, 4)


def test_disjoint_set2():
    adj = [[0, 1], [1, 2], [2, 3], [3, 4], [2, 5], [5, 6], [6, 7]]
    size = 8
    disjoint_set = DisjointSet2(size=size)
    assert disjoint_set.size == size

    for i, j in adj:
        disjoint_set.union(i, j)

    assert disjoint_set.connected(0, 1)
    assert disjoint_set.connected(2, 7)
