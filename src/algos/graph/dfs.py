def dfs_recursive(parent : int, u : int, graph : list[list[int]], visited : list[bool], ans : list[list[int]]):
    if visited[u]:
        return

    visited[u] = True
    if parent != -1:
        ans.append([parent, u])
    
    for v in graph[u]:
        dfs_recursive(u, v, graph, visited, ans)


def dfs_iterative(parent : int, u : int, graph : list[list[int]], visited : list[bool], ans : list[list[int]]):
    
    stack = [u]
    
    while len(stack):
        ...


def dfs_all_paths_from_source_to_target(u : int, target : int, graph : list[list[int]], visited : list[bool], cur : list[int], ans : list[list[int]]):
    if visited[u]:
        return
    
    visited[u] = True
    cur.append(u)
    
    if u == target:
        ans.append(cur.copy())
    
    for v in graph[u]:
        dfs_all_paths_from_source_to_target(v, target, graph, visited, cur, ans)
    
    visited[u] = False
    cur.pop()