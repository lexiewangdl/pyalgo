# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    found_p = False
    found_q = False

    def find(self, node, p, q):
        if not node:
            return None

        # Check left subtree
        left = self.find(node.left, p, q)

        # Check right subtree
        right = self.find(node.right, p, q)

        # Check if current node is a LCA
        if left and right:
            return node

        # Post-order operation, check current node
        if node.val == p.val or node.val == q.val:
            if node.val == p.val:
                self.found_p = True
            if node.val == q.val:
                self.found_q = True
            return node

        return left if left else right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.found_p = False
        self.found_q = False

        res = self.find(root, p, q)

        if not self.found_p or not self.found_q:
            return None

        return res