# 116. Populating Next Right Pointers in Each Node
from tree_node import TreeNode

# My solution 2: Traversal
def traverse(self, left_parent, right_parent):
    # check for None
    if not left_parent or not right_parent:
        return
    # connect left parent to right parent
    left_parent.next = right_parent

    # process left and right children of left parent
    self.traverse(left_parent.left, left_parent.right)
    # process right child of left parent and left child of right parent
    self.traverse(left_parent.right, right_parent.left)
    # process left and right children of right parent
    self.traverse(right_parent.left, right_parent.right)

def connect(self, root: TreeNode) -> TreeNode:
    if not root:
        return root

    self.traverse(root.left, root.right)

    return root


# My solution 1: Classic BFS Traversal
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