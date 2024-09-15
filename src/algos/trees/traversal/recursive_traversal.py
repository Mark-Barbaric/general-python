from src.data_structures.trees.tree_node import TreeNode
from typing import Optional


def recursive_preorder_traversal(root: Optional[TreeNode], nums: list[int]):
    if not root:
        return

    nums.append(root.val)
    recursive_preorder_traversal(root.left, nums)
    recursive_preorder_traversal(root.right, nums)


def recursive_inorder_traversal(root: Optional[TreeNode], nums: list[int]):
    if not root:
        return

    recursive_inorder_traversal(root.left, nums)
    nums.append(root.val)
    recursive_inorder_traversal(root.right, nums)
