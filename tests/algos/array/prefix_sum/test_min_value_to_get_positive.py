from src.algos.array.prefix_sum.min_val import min_val_to_get_positive


def test_positive_array():
    nums = [1, 2, 3]
    ans = min_val_to_get_positive(nums)
    assert ans == 1


def test_negative_and_positive():
    nums = [-3, 2, -3, 4, 2]
    ans = min_val_to_get_positive(nums)
    assert ans == 5
    nums = [-2, 3, -2, 2]
    ans = min_val_to_get_positive(nums)
    assert ans == 3
