from typing import Optional
from src.data_structures.trees.tree_node import TreeNode


def reverse_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    left = reverse_tree(root.left)
    right = reverse_tree(root.right)
    root.left = right
    root.right = left
    return root


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_max = max_depth(root.left)
    right_max = max_depth(root.right)
    return max(left_max, right_max) + 1


def min_depth(root: Optional[TreeNode]) -> int:
    ...
