from src.algos.array.sliding_window import max_ave_subarray1
import pytest


def test_empty_array():
    nums = []
    ans = max_ave_subarray1(nums, 1)
    assert ans == 0.0


def test_k_equals_len():
    nums = [1, 2, 3, 4]
    ans = max_ave_subarray1(nums, len(nums))
    assert pytest.approx(ans) == 2.5


def test_nums_with_one_item():
    nums = [-1]
    ans = max_ave_subarray1(nums, 1)
    assert ans == -1


def test_mixed_nums():
    nums = [1, 12, -5, -6, 50, 4]
    ans = max_ave_subarray1(nums, 4)
    assert pytest.approx(ans) == 12.75
