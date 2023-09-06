# 98. Validate Binary Search Tree
import math
from tree_node import TreeNode

# Solution 2: min and max
class Solution:
    def isValidBST(self, root: TreeNode, l_max=-math.inf, r_min=math.inf) -> bool:
        if not root:
            return True
        # if curr node's value is smaller than max value we have seen in left subtree
        # or greater than min value we have seen in right subtree
        if root.val <= l_max or root.val >= r_min:
            return False
        # return True only if both left and right subtrees are valid BSTs
        return self.isValidBST(root.left, l_max, root.val) and self.isValidBST(root.right, root.val, r_min)


# Solution 1: in-order traversal
class Solution:
    is_valid = True
    temp = -math.inf

    def check(self, node):
        if not node:
            return
        if not self.is_valid:
            return
        self.check(node.left)
        if node.val <= self.temp:
            self.is_valid = False
        self.temp = node.val
        self.check(node.right)
        return

    def isValidBST(self, root: TreeNode) -> bool:
        self.check(root)
        return self.is_valid
    
    