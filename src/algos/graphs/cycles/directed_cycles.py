def directed_graph_has_cycle(graph: list[list[int]]) -> bool:

    colors = [0 for _ in range(len(graph))]

    def dfs(u: int,
            colors: list[int],
            graph: list[list[int]]) -> bool:

        if colors[u] == 2:
            return False

        colors[u] = 1

        for v in graph[u]:
            if colors[v] == 1 or dfs(v, colors, graph):
                return True

        colors[u] = 2
        return False

    return dfs(0, colors, graph)
