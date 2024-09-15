def return_squares(l1: list[int]) -> list[int]:
    """_summary_

    Args:
        l (list[int]): _description_

    Returns:
        list[int]: _description_
    """

    if len(l1) == 0:
        return []

    i = 0
    ans = [-1 for _ in range(len(l1))]

    left = 0

    while left < len(l1) and l1[left] < 0:
        left += 1

    # iterate back
    left -= 1
    right = left + 1

    while i < len(ans):
        negative_num = "None" if left < 0 else l1[left]
        positive_num = "None" if right >= len(l1) else l1[right]

        if isinstance(negative_num, str):
            ans[i] = positive_num ** 2
            right += 1
        elif isinstance(positive_num, str):
            ans[i] = negative_num ** 2
            left -= 1
        else:
            if positive_num == 0 or int((abs(positive_num) < abs(negative_num))):
                ans[i] = positive_num ** 2
                right += 1
            else:
                ans[i] = negative_num ** 2
                left -= 1
        i += 1

    return ans
