def kthSmallest(matrix: list[list[int]], k: int) -> int:

    left, right = len(matrix) - 1, len(matrix) - 1
    up_l, up_r = left - 1, right
    left_l, left_r = left, right - 1

    ans = -1
    count = (len(matrix) * len(matrix)) - k

    while count >= 0:

        if left_l == 0 and up_l == 0:
            print(f"here: {left}, {right}")
            break

        ans = matrix[left][right]
        left_num = matrix[left_l][left_r]
        up_num = matrix[up_l][up_r]

        print(f"ans {ans}")
        print(f"left_l {left_l} : left_r {left_r}")
        print(f"up_l {up_l} : up_r {up_r}")

        if left_num > up_num:
            left = left_l
            right = left_r
            left_r -= 1

            if left_r < 0:
                left_l -= 1
                left_r = up_r - 1
        else:

            left = up_l
            right = up_r
            up_l -= 1

            if up_l < 0:
                up_r -= 1
                up_l = left_l - 1

        count -= 1

    return ans
