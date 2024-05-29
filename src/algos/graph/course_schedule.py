def can_finish_courses(num_courses: int, prerequisites: list[list[int]]):
    """_summary_

    Args:
        num_courses (int): _description_
        prerequisites (list[list[int]]): _description_

    Returns:
        _type_: _description_
    """
    colors = [0 for _ in range(num_courses)]
    graph = [[] for _ in range(num_courses)]

    for i, j in prerequisites:
        graph[j].append(i)

    def contains_cycle(u: int, colors: list[int], graph: list[list[int]]):
        if colors[u] == 2:
            return False

        colors[u] = 1

        for v in graph[u]:
            if colors[v] == 1 or contains_cycle(v, colors, graph):
                return True

        colors[u] = 2
        return False

    for i in range(num_courses):
        if colors[i] == 0 and contains_cycle(i, colors, graph):
            return False

    return True
