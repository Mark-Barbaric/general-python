def are_lists_equal(l1 : list, l2 : list) -> bool:
    assert len(l1) == len(l2) and sorted(l1) == sorted(l2)