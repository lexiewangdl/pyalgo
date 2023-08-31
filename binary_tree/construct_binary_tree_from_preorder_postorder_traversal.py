# 889 - Construct Binary Tree from Preorder and Postorder Traversal
from tree_node import TreeNode


class Solution:
    post_map = dict()

    def build(self,
              preorder: list, postorder: list,
              pre_left: int, pre_right: int,
              post_left: int, post_right: int):

        # base case
        if pre_left >= pre_right or post_left >= post_right:
            return None

        # build node
        # 首先把前序遍历结果的第一个元素或者后序遍历结果的最后一个元素确定为根节点的值
        node_val = preorder[pre_left]
        node = TreeNode(node_val)

        # find left and right boundaries for left and right subtrees
        # (1) find the index of root of left subtree in preorder (next to curr_node val)
        left_subtree_root_idx = pre_left + 1
        # (2) if no left subtree, return
        if left_subtree_root_idx == pre_right:
            return node
        # (3) find the index of root of left subtree in postorder
        left_subtree_root_idx_post = self.post_map[preorder[left_subtree_root_idx]]
        # (4) calculate the length of left subtree
        length_left_subtree = left_subtree_root_idx_post - post_left + 1

        # recurse
        node.left = self.build(preorder, postorder,
                               pre_left + 1, pre_left + 1 + length_left_subtree,
                               post_left, post_left + length_left_subtree)
        node.right = self.build(preorder, postorder,
                                pre_left + 1 + length_left_subtree, pre_right,
                                post_left + length_left_subtree, post_right - 1)

        return node

    def constructFromPrePost(self, preorder: list, postorder: list) -> TreeNode:
        length = len(preorder)

        for i in range(length):
            self.post_map[postorder[i]] = i

        return self.build(preorder, postorder, 0, length, 0, length)


if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    preorder = [1, 2, 4, 5, 3, 6, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]

    s.constructFromPrePost(preorder, postorder)
