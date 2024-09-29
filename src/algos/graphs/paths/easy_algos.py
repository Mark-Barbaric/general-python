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


def valid_path_in_bidirection_graph(num_nodes: int, edges: list[list[int]], source: int, destination: int) -> bool:
    visited = [0 for _ in range(num_nodes)]

    def dfs(cur_node, visited, edges, target):
        if visited[cur_node]:
            return False

        if cur_node == target:
            return True

        visited[cur_node] = 1

        for next_node in edges[cur_node]:
            if dfs(next_node, visited, edges, target):
                return True

        return False

    adj: list[list[int]] = [[] for _ in range(num_nodes)]

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    return dfs(source, visited, adj, destination)


# TODO: optimize
def find_the_town_judge(num_judges: int, trust_pairs: list[list[int]]) -> int:

    if num_judges == 1 and len(trust_pairs) == 0:
        return 1

    if num_judges > 1 and len(trust_pairs) == 0:
        return -1

    possible_judges: dict[int, int] = {j: 0 for j in range(num_judges)}
    adj: list[list] = [[] for _ in range(num_judges)]

    for trust in trust_pairs:
        town_person = trust[0] - 1
        follow = trust[1] - 1
        adj[town_person].append(follow)
        possible_judges[follow] += 1

    for trust, follow in possible_judges.items():
        if follow == num_judges - 1 and len(adj[trust]) == 0:
            return trust + 1

    return -1


def find_the_town_judge_optimized(num_judges: int, trust_pairs: list[list[int]]):
    votes = [0 for _ in range(num_judges)]

    for trust in trust_pairs:
        votes[trust[0] - 1] -= 1
        votes[trust[1] - 1] += 1

    for trust, vote in enumerate(votes):
        if vote == num_judges - 1:
            return trust + 1

    return -1
