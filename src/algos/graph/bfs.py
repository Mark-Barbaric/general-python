def bfs(u : int, graph : list[list[int]], ans = list[list[int]]):
    queue = [u]
    parent = -1
    visited = [False for _ in range(len(graph))]
    
    while(len(queue)):
        top = queue.pop(0)
        visited[top] = True
        
        if parent != -1:
            ans.append([parent, top])
        
        for e in graph[top]:
            if not visited[e]:
                queue.append(e)
        
        parent = top
        