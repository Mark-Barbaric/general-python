from src.algos.trees.traversal import recursive_inorder_traversal
from src.algos.trees.dfs import invert_tree
from src.data_structures.trees.tree_node import TreeNode


def test_null_root():
    root = None
    new_root = invert_tree(root)
    vals = []
    recursive_inorder_traversal(new_root, vals)
    assert vals == []


def test_uneven_tree():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    new_root = invert_tree(root)
    vals = []
    recursive_inorder_traversal(new_root, vals)
    assert vals == [5, 3, 2, 1]
    

def test_full_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    new_root = invert_tree(root)
    vals = []
    recursive_inorder_traversal(new_root, vals)
    expected_vals = [3, 1, 2]
    assert vals == expected_vals
