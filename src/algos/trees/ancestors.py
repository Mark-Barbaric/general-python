from typing import Optional
from src.data_structures.trees import TreeNode


def max_diff_between_node_and_ancestor(root: Optional[TreeNode]) -> int:

    def traverse(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0

        root_val = root.val
        left_val = traverse(root.left)
        right_val = traverse(root.right)

    return 0
