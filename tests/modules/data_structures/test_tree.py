import numpy as np
from modules.data_structures.tree import TreeNode, TreeOperations

np.random.seed(0)


def test_node_constructor():
    subject = TreeNode(10)
    assert subject.key == 10
    assert subject.height == 1
    assert not subject.left and not subject.right


def test_insert():
    root = node_5 = TreeNode(5)
    assert root.height == 1

    node_3 = TreeNode(3)
    root = TreeOperations.insert(root, node_3)

    assert root == node_5, (
        f"insertion of {node_3.key} should not have caused "
        f"rotation of root node. Expected: {node_5.key}, Actual: {root.key}"
    )
    assert root.height == 2
    assert root.left == node_3
    assert not root.right
    assert node_3.height == 1
    assert not node_3.left and not node_3.right

    node_4 = TreeNode(4)
    root = TreeOperations.insert(root, node_4)

    assert root == node_4, (
        f"insertion of {node_4.key} should have caused "
        f"rotation of root node. Expected: {node_4.key}, Actual: {root.key}"
    )
    assert root.height == 2
    assert root.left == node_3
    assert node_3.height == 1
    assert not node_3.left and not node_3.right
    assert root.right == node_5
    assert node_5.height == 1
    assert not node_5.left and not node_5.right


def test_delete():
    root = node_5 = TreeNode(5)
    root = TreeOperations.insert(root, TreeNode(3))
    root = TreeOperations.insert(root, TreeNode(7))
    root = TreeOperations.insert(root, TreeNode(2))
    root = TreeOperations.insert(root, TreeNode(4))
    root = TreeOperations.insert(root, TreeNode(6))
    root = TreeOperations.insert(root, TreeNode(8))

    assert root == node_5
    assert root.height == 3

    assert root.left.key == 3
    assert root.right.key == 7
    assert root.left.height == root.right.height == 2

    assert root.left.left.key == 2
    assert root.left.right.key == 4
    assert root.right.left.key == 6
    assert root.right.right.key == 8

    root = TreeOperations.delete(root, 7)
    assert root == node_5
    assert root.height == 3
    assert root.left.height == root.right.height == 2
    assert root.right.key == 8
    assert root.right.left.key == 6
    assert not root.right.right

    root = TreeOperations.delete(root, 8)
    assert root == node_5
    assert root.height == 3
    assert root.left.height == 2 > root.right.height == 1
    assert root.right.key == 6
    assert not root.right.left and not root.right.right

    # tree re-balances
    root = TreeOperations.delete(root, 6)
    assert root != node_5
    assert root.key == 3
    assert root.right == node_5
    assert root.right.left.key == 4
    assert not root.right.right
    assert root.left.key == 2
