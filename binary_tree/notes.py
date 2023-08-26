from tree_node import TreeNode


def traverse(root):
    if not root:
        return

    print(f"At node {root}")

    print(f"Entering node {root.left} from {root}")
    traverse(root.left)
    print(f"Leaving node {root.left} from {root}")

    print(f"Entering node {root.right} from {root}")
    traverse(root.right)
    print(f"Leaving node {root.right} from {root}")
    return


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    traverse(root)

