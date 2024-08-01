from src.algos.array.sliding_window import max_ones_with_flip


def test_k_is_zero():
    nums = [0, 0, 1]
    ans = max_ones_with_flip(nums, 0)
    assert ans == 1
    nums = [1, 0, 1, 1, 1, 0, 1, 1]
    ans = max_ones_with_flip(nums, 0)
    assert ans == 3


def test_k_is_not_zero_easy():
    nums = [0, 0, 1]
    ans = max_ones_with_flip(nums, 1)
    assert ans == 2
    nums = [1, 0, 1, 0, 0, 1]
    ans = max_ones_with_flip(nums, 2)
    assert ans == 4
