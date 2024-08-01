def max_ones_with_flip(nums: list[int], k: int) -> int:

    left = 0
    right = 0
    ans = 0

    while right < len(nums):

        while k == 0 and nums[right] == 0:
            if nums[left] == 0:
                k += 1
            left += 1

        cur_max = right - left + 1
        ans = max(cur_max, ans)

        if nums[right] == 0:
            k -= 1

        right += 1

    return ans
