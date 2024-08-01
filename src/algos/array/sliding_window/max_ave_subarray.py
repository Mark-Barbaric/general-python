def max_ave_subarray1(nums: list[int], k: int) -> float:
    """_summary_

    Args:
        nums (list[int]): _description_
        k (int): _description_

    Returns:
        float: _description_
    """
    ans = 0.0

    if len(nums) == 0:
        return ans

    if k == len(nums):
        return sum(nums) / k

    cur_sum = sum(nums[: k])
    ans = cur_sum
    i = k

    while i < len(nums):
        cur_sum += (nums[i] - nums[i - k])
        ans = max(cur_sum, ans)
        i += 1

    return ans / k
