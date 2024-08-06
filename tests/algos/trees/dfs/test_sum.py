from src.data_structures.trees import TreeNode
from src.algos.trees.dfs.sum import sum_of_root_to_leaf_binary_numbers


def test_null_root():
    root = None
    ans = sum_of_root_to_leaf_binary_numbers(root)
    assert ans == 0


def test_root_with_two_leaves():
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    ans = sum_of_root_to_leaf_binary_numbers(root)
    assert ans == 5


def test_root_with_two_levels():
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(0)
    root.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(0)
    ans = sum_of_root_to_leaf_binary_numbers(root)
    assert ans == 22


def test_root_with_uneven_levels():
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(0)
    root.right = TreeNode(0)
    root.right.left = TreeNode(1)
    ans = sum_of_root_to_leaf_binary_numbers(root)
    assert ans == 18
