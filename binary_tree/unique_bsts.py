# 96. Unique Binary Search Trees


class Solution:
    memo = []

    def find_number_of_unique_bsts(self, left: int, right: int):
        # subtree is null tree (count as 1 unique BST)
        if left > right:
            return 1

        # subtree has only 1 node (count as 1 unique BST)
        if left == right:
            self.memo[left-1][right-1] = 1  # save to memo for reference, avoid recursion
            return self.memo[left-1][right-1]

        # subtree has more than 1 nodes,
        # if number of unique BSTs have been calculated,
        # access value and return
        if self.memo[left - 1][right - 1] != 0:
            return self.memo[left - 1][right - 1]

        res = 0  # initialize number of unique BSTs for subtree

        # loop through values from left to right, each node can be the root
        for i in range(left, right + 1):
            # number of unique BSTs for left subtree
            num_left = self.find_number_of_unique_bsts(left, i - 1)
            # number of unique BSTs for right subtree
            num_right = self.find_number_of_unique_bsts(i + 1, right)

            res += num_left * num_right

        self.memo[left - 1][right - 1] = res

        return res

    def numTrees(self, n: int) -> int:
        self.memo = [[0 for col in range(n)] for row in range(n)]  # [[0] * n] * n

        return self.find_number_of_unique_bsts(1, n)


if __name__ == "__main__":
    s = Solution()

    print("Calculating number of unique binary search trees with 5 nodes...")
    s.numTrees(5)
