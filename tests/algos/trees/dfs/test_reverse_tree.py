from src.algos.trees.traversal import recursive_inorder_traversal
from src.algos.trees.dfs.easy_algos import reverse_tree
from src.data_structures.trees.tree_node import TreeNode


def test_reverse_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    new_root = reverse_tree(root)
    vals = []
    recursive_inorder_traversal(new_root, vals)
    expected_vals = [3, 1, 2]
    assert vals == expected_vals
