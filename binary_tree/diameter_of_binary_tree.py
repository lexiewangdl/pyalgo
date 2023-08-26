# 543. Diameter of Binary Tree
class Solution:
    res = 0

    def max_depth(self, node) -> int:
        if not node:
            return 0

        max_depth_left = self.max_depth(node.left)
        max_depth_right = self.max_depth(node.right)

        diameter = max_depth_left + max_depth_right
        self.res = diameter if diameter > self.res else self.res

        return max(max_depth_left + 1, max_depth_right + 1)

    def diameterOfBinaryTree(self, root) -> int:
        self.max_depth(root)
        return self.res
