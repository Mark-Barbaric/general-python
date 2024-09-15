from typing import Optional
from src.data_structures.trees.tree_node import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_max = max_depth(root.left)
    right_max = max_depth(root.right)
    return max(left_max, right_max) + 1
