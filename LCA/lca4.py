# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def find(self, node, vals):
        if not node:
            return None

        # Preorder
        if node.val in vals:
            return node

        # Check left subtree
        left = self.find(node.left, vals)

        # Check right subtree
        right = self.find(node.right, vals)

        if left and right:
            return node

        return left if left else right

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        vals = set()
        for node in nodes:
            vals.add(node.val)

        return self.find(root, vals)
