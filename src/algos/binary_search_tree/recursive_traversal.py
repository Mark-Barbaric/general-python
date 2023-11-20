from src.data_structures.tree.tree_node import TreeNode
from typing import Optional

def recursive_preorder_traversal(root : Optional[TreeNode], nums : list[int]):
    if not root:
        return 

    nums.append(root.val)
    recursive_preorder_traversal(root.left)
    recursive_preorder_traversal(root.right)
    

def recursive_inorder_traversal(root : Optional[TreeNode], nums : list[int]):
    if not root:
        return
    
    recursive_inorder_traversal(root.left, nums)
    nums.append(root.val)
    recursive_inorder_traversal(root.right, nums)