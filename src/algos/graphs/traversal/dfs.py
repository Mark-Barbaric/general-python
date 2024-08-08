def dfs_recursive(parent: int,
                  u: int,
                  graph: list[list[int]],
                  visited: list[bool],
                  ans: list[list[int]]):
    if visited[u]:
        return

    visited[u] = True
    if parent != -1:
        ans.append([parent, u])

    for v in graph[u]:
        dfs_recursive(u, v, graph, visited, ans)


def dfs_iterative(u: int,
                  graph: list[list[int]],
                  ans: list[list[int]]):
    stack = [u]
    parent = -1
    visited = [False for _ in range(len(graph))]

    while len(stack):
        top = stack.pop()
        visited[top] = True

        if parent != -1:
            ans.append([parent, top])

        for e in graph[top]:
            if not visited[e]:
                stack.append(e)

        parent = top
