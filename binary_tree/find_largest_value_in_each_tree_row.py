import math
from tree_node import TreeNode


def largestValues(root) -> list:
    if not root:
        return []

    level = 0
    q, res = [root, None], [root.val]

    while len(q) > 0:
        node = q.pop(0)

        if not node:
            if len(q) == 0:  # if curr node is last node popped from queue
                return res
            level += 1
            q.append(None)
            res.append(-math.inf)
        else:
            res[level] = node.val if node.val > res[level] else res[level]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    largestValues(root)
