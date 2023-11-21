from typing import Optional
from src.data_structures.tree.tree_node import TreeNode


def reverse_tree(root : Optional[TreeNode])->Optional[TreeNode]:
    if not root:
        return None
    
    left = reverse_tree(root.left)
    right = reverse_tree(root.right)
    root.left = right
    root.right = left
    return root
