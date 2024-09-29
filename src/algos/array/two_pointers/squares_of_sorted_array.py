def return_squares(numbers: list[int]) -> list[int]:
    """_summary_

    Args:
        l (list[int]): _description_

    Returns:
        list[int]: _description_
    """

    if len(numbers) == 0:
        return []

    cur_index = 0
    ans: list[int] = [-1 for _ in range(len(numbers))]

    left = 0

    while left < len(numbers) and numbers[left] < 0:
        left += 1

    # iterate back
    left -= 1
    right = left + 1

    while cur_index < len(ans):
        negative_num = None if left < 0 else numbers[left]
        positive_num = None if right >= len(numbers) else numbers[right]

        if positive_num and negative_num:
            if positive_num == 0 or (abs(positive_num) < abs(negative_num)):
                ans[cur_index] = positive_num ** 2
                right += 1
            else:
                ans[cur_index] = negative_num ** 2
                left -= 1
        else:
            if negative_num:
                ans[cur_index] = positive_num ** 2
                right += 1
            elif positive_num:
                ans[cur_index] = negative_num ** 2
                left -= 1
        cur_index += 1

    return ans
