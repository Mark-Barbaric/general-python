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

    if n == 1 and len(trust) == 0:
        return 1

    if n > 1 and len(trust) == 0:
        return -1

    possible_judges = {j: 0 for j in range(n)}
    adj = [[] for _ in range(n)]

    for t in trust:
        town_person = t[0] - 1
        follow = t[1] - 1
        adj[town_person].append(follow)
        possible_judges[follow] += 1

    for t, follow in possible_judges.items():
        if follow == n - 1 and adj[t] == []:
            return t + 1

    return -1


def find_judge_optimized(n: int, trust: list[int]):
    votes = [0] * n

    for t in trust:
        u, v = t
        votes[u-1] -= 1


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
