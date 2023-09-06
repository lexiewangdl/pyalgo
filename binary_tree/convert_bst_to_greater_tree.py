# 538. Convert BST to Greater Tree (Medium)
from tree_node import TreeNode


class Solution:
    greater_sum = 0

    def traverse(self, node):
        if not node:
            return

        self.traverse(node.right)
        node.val = self.greater_sum = node.val + self.greater_sum
        self.traverse(node.left)

        return

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.greater_sum = 0
        self.traverse(root)
        return root
