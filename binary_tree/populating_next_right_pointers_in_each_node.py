# 116. Populating Next Right Pointers in Each Node
from tree_node import TreeNode

# My solution 1: BFS Traversal
def connect(root: TreeNode) -> TreeNode:
    # Initialize queue to store nodes to be visited
    q = []
    # Add root node and level change indicator
    q.append(root)
    q.append(None)

    # While there is still node to visit
    while len(q) > 0:
        curr = q.pop(0)  # pop first node in queue to process

        # Check if curr node is None (level change indicator)
        if not curr:
            if len(q) == 0 or not q[0]:
                break  # If queue is empty, break out of while loop

            # If queue is not empty, all nodes in current level have been processed
            # and all nodes in next level have been added to queue
            # Add another level change indicator
            q.append(None)

        else:
            # If curr node is not None
            curr.next = q[0]  # make curr node's next pointer point to next waiting node in queue

            # Add current node's children to queue
            # Don't add any None nodes!
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    return root