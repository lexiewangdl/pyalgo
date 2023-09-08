# 450. Delete Node in a BST
from tree_node import TreeNode


class Solution:
    def getMax(self, node) -> TreeNode:
        while node.right:
            node = node.right
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val == key:
            # if node has no child, return None
            # if node has only one child, set this child as node
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # if not has two children
            else:
                # find the largest child in left subtree
                max_left_child = self.getMax(root.left)
                # delete the largest child in tree
                root.left = self.deleteNode(root.left, max_left_child.val)
                # make curr node's left and right children attach to that child
                max_left_child.left = root.left
                max_left_child.right = root.right

                return max_left_child

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root
