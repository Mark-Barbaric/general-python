from src.algos.array.prefix_sum import running_sum_of_1d_array, running_sum_of_1d_array_opt


def test_running_sum():
    nums = [1, 4, 5, 6]
    ans = running_sum_of_1d_array(nums)
    assert ans == [1, 5, 10, 16]


def test_running_sum_opt():
    nums = [1, 4, 5, 6]
    ans = running_sum_of_1d_array_opt(nums)
    assert ans == [1, 5, 10, 16]
