from src.algos.binary_search_tree.recursive_traversal import recursive_inorder_traversal
from src.data_structures.tree.tree_node import TreeNode

def test_inorder_traversal():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    ans = []
    recursive_inorder_traversal(root, ans)
    expected_ans = [3,5,7]
    assert sorted(ans) == sorted(expected_ans)