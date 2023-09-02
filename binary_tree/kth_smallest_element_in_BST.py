# 230. Kth Smallest Element in a BST
from tree_node import TreeNode

class Solution:

    val = -1
    n = -1

    def add_val(self, node, k):
        if not node:
            return

        self.add_val(node.left, k)
        # in-order add val
        if self.n == k:
            self.val = node.val
            self.n += 1
            return
        self.n += 1

        self.add_val(node.right, k)

        return

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.n = 1
        self.val = -1
        self.add_val(root, k)

        return self.val