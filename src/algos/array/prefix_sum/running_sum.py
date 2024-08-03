def running_sum_of_1d_array(nums: list[int]) -> list[int]:
    return [sum(nums[: i + 1]) for i in range(len(nums))]


def running_sum_of_1d_array_opt(nums: list[int]) -> list[int]:
    cum_sum = 0
    ans = []

    for num in nums:
        cum_sum += num
        ans.append(cum_sum)

    return ans
