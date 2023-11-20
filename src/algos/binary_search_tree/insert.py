from typing import Optional
from src.data_structures.tree.tree_node import TreeNode

def insert_node(root : Optional[TreeNode], val : int)->Optional[TreeNode]:
    if not root:
        return None
    
    if val < root.val:
        ...