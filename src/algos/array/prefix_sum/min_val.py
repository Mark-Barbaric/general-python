def min_val_to_get_positive(nums: list[int]) -> int:
    cur_min = 0
    cum_sum = 0

    for n in nums:
        cum_sum += n
        cur_min = min(cum_sum, cur_min)

    return abs(cur_min) + 1
