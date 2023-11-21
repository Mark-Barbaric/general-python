from src.algos.binary_search_tree.iterative_traversal import iterative_inorder_traversal
from src.data_structures.tree.tree_node import TreeNode


def test_inorder_traversal():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    ans = []
    iterative_inorder_traversal(root, ans)
    expected_ans = [1,2,3,4,5,6,7]
    assert sorted(ans) == sorted(expected_ans)


def test_inorder_traversal2():
    root = TreeNode(5)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    ans = []
    iterative_inorder_traversal(root, ans)
    expected_ans = [5,6,7]
    assert sorted(ans) == sorted(expected_ans)