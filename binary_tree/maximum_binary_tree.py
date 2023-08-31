# 654. Maximum Binary Tree (M)
import math
from tree_node import TreeNode


class Solution:
    # Optimize space complexity
    def construct(self, nums: list, left: int, right: int) -> TreeNode:
        node_idx = -1
        node_val = -math.inf

        for i in range(left, right):
            if nums[i] > node_val:
                node_val = nums[i]
                node_idx = i

        if node_idx == -1:
            return None

        node = TreeNode(node_val)

        node.left = self.construct(nums, left, node_idx)
        node.right = self.construct(nums, node_idx + 1, right)

        return node

    def constructMaximumBinaryTree(self, nums: list) -> TreeNode:
        return self.construct(nums, 0, len(nums))


    # Initial solution: Divide and Conquer
    # def findMax(self, nums):
    #     if len(nums) < 1:
    #         return -1

    #     max_val, max_idx = -math.inf, -1

    #     for i in range(len(nums)):
    #         if nums[i] > max_val:
    #             max_val = nums[i]
    #             max_idx = i

    #     return max_idx

    # def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    #     root_idx = self.findMax(nums)

    #     if root_idx == -1:
    #         return None

    #     root = TreeNode(nums[root_idx])

    #     if root_idx > 0:
    #         root.left = self.constructMaximumBinaryTree(nums[:root_idx])
    #     if root_idx < len(nums) - 1:
    #         root.right = self.constructMaximumBinaryTree(nums[root_idx+1:])

    #     return root