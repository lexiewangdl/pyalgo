class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: # reach the end
            return None

        # pre-order position: check whether curr node is target node
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # post-order position
        if left and right: # both nodes found, current node is the LCA
            return root

        # p or q might be the LCA of p and q
        return left if left else right