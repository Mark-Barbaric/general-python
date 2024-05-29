from src.data_structures.tree.tree_node import TreeNode


def test_reverse_odd_levels():
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(0)
