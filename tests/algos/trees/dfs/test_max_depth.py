from src.data_structures.trees import TreeNode
from src.algos.trees.dfs.easy_algos import max_depth


def test_null_root():
    root = None
    depth = max_depth(root)
    assert depth == 0


def test_root_node():
    root = TreeNode(1)
    depth = max_depth(root)
    assert depth == 1


def test_left_max():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    depth = max_depth(root)
    assert depth == 3


def test_right_max():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(3)
    root.left.left.left.left = TreeNode(3)
    depth = max_depth(root)
    assert depth == 5
