def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    left = 0
    lst = []
    ans = []

    while k > 0:

        top = lst[left]
        value = top[0]
        array = top[1]
        i = left + 1

        for i in range(left + 1, len(lst)):

            new = lst[i]
            n_value = new[0]
            n_array = new[1]

            if array != n_array:
                ans.append([value, n_value])
                k -= 1

            if k == 0:
                break

        left += 1
    return ans
