# 297. Serialize and Deserialize Binary Tree
from tree_node import TreeNode


# 2. Post-order solution
class Codec:
    deserialize_idx = -1
    data_list = []

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # use # to represent null nodes
        if not root:
            return "#"

        return self.serialize(root.left) + "," + self.serialize(root.right) + "," + str(root.val)

    def deserialize_helper(self):
        node_val = self.data_list[self.deserialize_idx]
        node = None

        if node_val == "#":
            self.deserialize_idx -= 1
            return node
        else:
            node = TreeNode(int(node_val))
        self.deserialize_idx -= 1

        node.right = self.deserialize_helper()
        node.left = self.deserialize_helper()

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.data_list = data.split(",")
        self.deserialize_idx = len(self.data_list) - 1

        return self.deserialize_helper()


# 1. Preorder solution
class Codec:
    data_list = []
    deserialize_idx = 0

    # Pre-order
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # use # to represent null nodes
        if not root:
            return "#"

        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize_helper(self):
        node_val = self.data_list[self.deserialize_idx]
        node = None

        if node_val == "#":
            self.deserialize_idx += 1
            return node
        else:
            node = TreeNode(int(node_val))
        self.deserialize_idx += 1

        node.left = self.deserialize_helper()
        node.right = self.deserialize_helper()

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.deserialize_idx = 0
        self.data_list = data.split(",")

        return self.deserialize_helper()
