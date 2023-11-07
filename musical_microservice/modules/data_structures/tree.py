from typing import Any


class TreeNode:
    def __init__(self, key: Any):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class TreeOperations:
    @staticmethod
    def insert(root: TreeNode | None, node: TreeNode) -> TreeNode | None:
        if not root:
            return node

        # if the node already exists
        if node.key == root.key:
            return root

        # we depend on recursion to keep track of the ancestry path from root
        # to newly inserted node
        if node.key < root.key:
            root.left = TreeOperations.insert(root.left, node)
        else:
            root.right = TreeOperations.insert(root.right, node)

        # update the height of the subtree and re-balance if necessary.
        # Do this all the way back the recursion stack
        TreeOperations.update_nodes_height(root)
        return TreeOperations.balance(root)

    @staticmethod
    def search(root: TreeNode | None, key: Any) -> TreeNode | None:
        if root:
            if key > root.key:
                return TreeOperations.search(root.right, key)
            elif key < root.key:
                return TreeOperations.search(root.left, key)

        return root

    @staticmethod
    def rotate_left(z: TreeNode) -> TreeNode | None:
        y = z.right
        gc = y.left

        y.left = z
        z.right = gc

        TreeOperations.update_nodes_height(z)
        TreeOperations.update_nodes_height(y)

        return y

    @staticmethod
    def rotate_right(z: TreeNode) -> TreeNode | None:
        y = z.left
        gc = y.right

        y.right = z
        z.left = gc

        TreeOperations.update_nodes_height(z)
        TreeOperations.update_nodes_height(y)

        return y

    @staticmethod
    def get_nodes_height(node: TreeNode | None) -> int:
        if not node:
            return 0

        return node.height

    @staticmethod
    def update_nodes_height(node: TreeNode | None):
        if node:
            node.height = 1 + max(
                TreeOperations.get_nodes_height(node.left),
                TreeOperations.get_nodes_height(node.right),
            )

    @staticmethod
    def get_balance(node: TreeNode | None) -> int:
        if not node:
            return 0

        return TreeOperations.get_nodes_height(
            node.left
        ) - TreeOperations.get_nodes_height(node.right)

    @staticmethod
    def balance(root: TreeNode | None):
        balance = TreeOperations.get_balance(root)
        if balance > 1:
            if TreeOperations.get_balance(root.left) < 0:
                root.left = TreeOperations.rotate_left(root.left)
            return TreeOperations.rotate_right(root)
        elif balance < -1:
            if TreeOperations.get_balance(root.right) > 0:
                root.right = TreeOperations.rotate_right(root.right)
            return TreeOperations.rotate_left(root)
        return root

    @staticmethod
    def inorder_successor(root: TreeNode, p: TreeNode) -> TreeNode | None:
        if root:
            if root.key > p.key:
                if root.left:
                    successor = TreeOperations.inorder_successor(root.left, p)
                    if successor:
                        return successor
            else:
                return TreeOperations.inorder_successor(root.right, p)
        return root

    @staticmethod
    def delete(root: TreeNode | None, key: Any) -> TreeNode | None:
        if root:
            if key < root.key:
                root.left = TreeOperations.delete(root.left, key)
            elif key > root.key:
                root.right = TreeOperations.delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                # if root has both children, find its inorder successor and swap
                successor = TreeOperations.inorder_successor(root, root)
                TreeOperations.delete(root, successor.key)

                root.key = successor.key

        # update the height of the subtree and re-balance if necessary.
        # Do this all the way back the recursion stack
        TreeOperations.update_nodes_height(root)
        return TreeOperations.balance(root)


class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self.root = root
        self.iterands = []
        self.inorder(self.root, self.iterands)

        self.complete = len(self.iterands)
        self.index = 0

    def next(self) -> int:
        ret = self.iterands[self.index]
        self.index += 1
        return ret

    def has_next(self) -> bool:
        return self.index < self.complete

    def inorder(self, root: TreeNode | None, order: list):
        if root:
            self.inorder(root.left, order)
            order.append(root.key)
            self.inorder(root.right, order)
