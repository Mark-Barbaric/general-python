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


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    left = invert_tree(root.left)
    right = invert_tree(root.right)
    root.left = right
    root.right = left
    return root
