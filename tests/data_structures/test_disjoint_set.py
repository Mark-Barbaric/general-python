from src.data_structures.graph.disjoint_set import DisjointSet


def test_disjoint_set():
    adj = [[0,1],[0,2],[1,3],[4,8],[5,6],[5,7]]
    size = 9
    disjoint_set = DisjointSet(size=size)
    assert disjoint_set.size == size
    
    for i,j in adj:
        disjoint_set.union(i, j)
    
    assert disjoint_set.connected(0,1)
    assert not disjoint_set.connected(2,4)
    
    
    
    