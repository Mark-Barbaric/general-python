from src.data_structures.linked_list import LinkedList


def list_to_linked_list(nums: list[int]) -> LinkedList:
    root = LinkedList(nums[0])
    head = root

    for i in range(1, len(nums)):
        new_node = LinkedList(nums[i])
        head.next = new_node
        head = head.next
    return root


def are_lists_equal(l1: list[int], l2: list[int], sort_lists=True) -> bool:
    """Checks whether two lists are equal. Use the sort_lists flag to ignore position of elements in the list.

    Args:
        l1 (list[int]): _description_
        l2 (list[int]): _description_
        sort_lists (bool, optional): _description_. Defaults to True.

    Returns:
        bool: _description_
    """
    equal_length = len(l1) == len(l2)

    if not equal_length:
        return False

    if sort_lists:
        return sorted(l1) == sorted(l2)
    else:
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False

    return True


def adj_to_graph(adj: list[int], n: int, directed=True) -> list:
    graph = [[] for _ in range(n)]

    for i, j in adj:
        graph[i].append(j)

        if not directed:
            graph[j].append(i)

    return graph
