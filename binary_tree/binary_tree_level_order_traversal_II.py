# 107.

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        curr_level = [[]]

        queue = []
        queue.append(root)
        queue.append(None)

        while queue:
            node = queue.pop(0)

            if not node:
                curr_level.extend(result)
                result = curr_level
                curr_level = [[]]

                if not queue or not queue[0]:
                    return result

                queue.append(None)
                continue

            curr_level[0].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result