from typing import Optional
from src.data_structures.trees import TreeNode


def sum_of_root_to_leaf_binary_numbers(root: Optional[TreeNode]) -> int:

    def helper(root: Optional[TreeNode], cur_bits: list[int], ans: list[int]):

        if not root:
            return

        cur_bits.append(root.val)

        if root.left:
            helper(root.left, cur_bits, ans)
            cur_bits.pop()

        if root.right:
            helper(root.right, cur_bits, ans)
            cur_bits.pop()

        if not root.left and not root.right:
            first_bit = cur_bits[-1]
            rest = sum([2 ** (len(cur_bits) - i - 1) for i, bit in enumerate(cur_bits[:-1]) if bit == 1])
            ans.append(rest + first_bit)

    ans: list[int] = []
    helper(root, [], ans)
    return sum(ans)
