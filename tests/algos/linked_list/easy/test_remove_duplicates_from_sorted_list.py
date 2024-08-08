from src.algos.linked_list.easy import delete_duplicates_from_sorted_list
from tests.test_helpers import list_to_linked_list, linked_list_to_list
from tests.test_helpers.general_helpers import are_lists_equal


def test_empty_list():
    assert not delete_duplicates_from_sorted_list(None)


def test_no_duplicates():
    l1 = [1, 2, 3]
    root = list_to_linked_list(l1)
    new_root = delete_duplicates_from_sorted_list(root)
    new_root_as_nums = linked_list_to_list(new_root)
    assert are_lists_equal(l1, new_root_as_nums)


def test_all_duplicates():
    l1 = [1, 1, 1]
    root = list_to_linked_list(l1)
    new_root = delete_duplicates_from_sorted_list(root)
    new_root_as_nums = linked_list_to_list(new_root)
    assert are_lists_equal([1], new_root_as_nums)


def test_mixture_of_duplicates():
    l1 = [1, 1, 2]
    root = list_to_linked_list(l1)
    new_root = delete_duplicates_from_sorted_list(root)
    new_root_as_nums = linked_list_to_list(new_root)
    assert are_lists_equal([1, 2], new_root_as_nums)


def test_mixture_of_duplicates_hard():
    l1 = [1, 2, 2, 3, 4, 5, 5, 5]
    root = list_to_linked_list(l1)
    new_root = delete_duplicates_from_sorted_list(root)
    new_root_as_nums = linked_list_to_list(new_root)
    assert are_lists_equal([1, 2, 3, 4, 5], new_root_as_nums)
