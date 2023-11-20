from typing import Optional
from src.data_structures.tree.tree_node import TreeNode

def iterative_inorder_traversal(root : Optional[TreeNode], ans : list[int]):
    
    cur=root
    stack=[]
    
    while len(stack) or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.pop()
        ans.append(cur.val)
        cur = cur.right