# 701. Insert into a Binary Search Tree
from tree_node import TreeNode


class Solution:

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # create new node to insert when empty spot found
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root
