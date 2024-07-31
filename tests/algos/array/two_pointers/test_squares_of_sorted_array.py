from src.algos.array.two_pointers import return_squares
from tests.test_helpers import are_lists_equal


def test_empty_list():
    nums = []
    ans = return_squares(nums)
    assert ans == []


def test_only_positive1():
    nums = [0, 2, 3]
    ans = return_squares(nums)
    expected_ans = [0, 4, 9]
    assert (are_lists_equal(expected_ans, ans, sort_lists=False))


def test_only_negative():
    nums = [-5, -4, -3]
    ans = return_squares(nums)
    expected_ans = [9, 16, 25]
    assert (are_lists_equal(ans, expected_ans, sort_lists=False))
    

def test_with_negative():
    nums = [-4, -1, 0, 3, 10]
    ans = return_squares(nums)
    assert (are_lists_equal(nums, ans))
    