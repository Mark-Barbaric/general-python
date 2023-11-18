
def kthSmallest(matrix: list[list[int]], k: int) -> int:

    l, r = len(matrix) - 1, len(matrix) - 1
    up_l, up_r = l - 1, r
    left_l, left_r = l, r - 1

    ans = -1
    count = (len(matrix) * len(matrix)) - k

    while count >= 0:

        if left_l == 0 and up_l == 0:
            print(f"here: {l}, {r}")
            break

        ans = matrix[l][r]
        left_num = matrix[left_l][left_r]
        up_num = matrix[up_l][up_r]

        print(f"ans {ans}")
        print(f"left_l {left_l} : left_r {left_r}")
        print(f"up_l {up_l} : up_r {up_r}")

        if left_num > up_num:
            l = left_l
            r = left_r
            left_r -= 1

            if left_r < 0:
                left_l -= 1
                left_r = up_r - 1
        else:
            
            l = up_l
            r = up_r
            up_l -= 1

            if up_l < 0:
                up_r -= 1
                up_l = left_l - 1

        count -= 1

    return ans