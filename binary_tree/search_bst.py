# 700. Search in a BST
from tree_node import TreeNode

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        # process current node
        if root.val == val:
            return root
        # process left and right subtrees
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
