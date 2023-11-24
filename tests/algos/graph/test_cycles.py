from src.algos.graph.cycles import directed_graph_has_cycle
from tests.helpers import adj_to_graph

def test_directed_graph_has_cycle():
    adj = [[0,1],[1,2],[2,3],[3,0]]
    graph = adj_to_graph(adj, 4)
    assert directed_graph_has_cycle(graph)
    adj = [[0,1],[1,2],[2,0],[0,2],[3,3],[2,3]]
    graph = adj_to_graph(adj, 4)
    assert directed_graph_has_cycle(graph)
    adj = [[0,1],[1,2],[2,3]]
    graph = adj_to_graph(adj, 4)
    assert not directed_graph_has_cycle(graph)