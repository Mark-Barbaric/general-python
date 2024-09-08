def trap_rain_water(heights: list[int]) -> int:
    ans = 0

    for i in range(1, len(heights)-1):
        max_l, max_r = 0, 0

        for left in range(i, -1, -1):
            max_l = max(max_l, heights[left])

        for right in range(i, len(heights)):
            max_r = max(max_r, heights[right])

        ans += min(max_l, max_r) - heights[i]

    return ans


def trap_rain_water_dp(heights: list[int]) -> int:
    ans = 0
    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    left_max[0] = heights[0]
    right_max[-1] = heights[-1]

    for i in range(1, len(heights)):
        left_max[i] = max(heights[i], left_max[i - 1])

    for i in range(len(heights) - 2, 0, -1):
        right_max[i] = max(heights[i], right_max[i+1])

    for i in range(1, len(heights) - 1):
        ans += min(left_max[i], right_max[i]) - heights[i]

    return ans
