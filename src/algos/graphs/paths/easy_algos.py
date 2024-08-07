def all_paths_from_source_to_target(u: int,
                                    target: int,
                                    graph: list[list[int]],
                                    visited: list[bool],
                                    cur: list[int],
                                    ans: list[list[int]]):
    if visited[u]:
        return

    visited[u] = True
    cur.append(u)

    if u == target:
        ans.append(cur.copy())

    for v in graph[u]:
        all_paths_from_source_to_target(v, target, graph, visited, cur, ans)

    visited[u] = False
    cur.pop()


def valid_path_in_bidirection_graph(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    visited = [0 for _ in range(n)]

    def dfs(u, visited, edges, target):
        if visited[u]:
            return False

        if u == target:
            return True

        visited[u] = 1

        for v in edges[u]:
            if dfs(v, visited, edges, target):
                return True

        return False

    adj = [[] for _ in range(n)]

    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    return dfs(source, visited, adj, destination)


# TODO: optimize
def find_the_town_judge(n: int, trust: list[list[int]]) -> int:

    if trust == [] and n == 1:
        return 1

    if trust == [] and n > 1:
        return -1

    adj = [[] for _ in range(n)]

    for t in trust:
        adj[t[0] - 1].append(t[1] - 1)

    possible_judges = [i for i, a in enumerate(adj) if len(a) == 0]
    judge_follow = {j: 0 for j in possible_judges}

    if not judge_follow:
        return -1

    for t in trust:
        town_person = t[1] - 1

        if judge_follow.get(town_person, -1) != -1:
            judge_follow[town_person] += 1

            if judge_follow[town_person] == n - 1:
                return town_person + 1

    return -1


def print_bidirectional_paths(u: int, graph: list[list[int]], n: int) -> list[list[int]]:

    def dfs(u: int, visited: list[int], graph: list[list[int]], cur: list[int], ans: list[list[int]]):
        if visited[u]:
            return

        visited[u] = 1
        cur.append(u)

        for v in graph[u]:
            dfs(v, visited, graph, cur, ans)

        ans.append(cur.copy())
        cur.pop()
        visited[u] = 0

    ans = []
    visited = [0 for _ in range(n)]

    for i in range(u, n):
        dfs(i, visited, graph, [], ans)

    return ans
