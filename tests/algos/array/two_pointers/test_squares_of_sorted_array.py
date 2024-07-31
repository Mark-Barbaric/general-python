from src.algos.array.two_pointers import return_squares
from tests.test_helpers import are_lists_equal


def test_return_squares_1():
    nums = [-4, -1, 0, 3, 10]
    ans = return_squares(nums)
    assert (are_lists_equal(nums, ans))
    