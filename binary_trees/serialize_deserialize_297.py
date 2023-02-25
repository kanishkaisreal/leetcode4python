

"""
This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

 """

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        self.vals = []

        def encode(node):
            if node:
                self.vals.append(str(node.data))
                encode(node.left)
                encode(node.right)
            else:
                self.vals.append('-1')

        encode(root)

        return ' '.join(self.vals)

    def deserialize(self, data):

        def decode(vals):
            val = next(vals)
            if val == '-1':
                return None
            node = Node(int(val))
            node.left = decode(vals)
            node.right = decode(vals)
            return node

        vals = iter(data.split())
        return decode(vals)

# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    codec = Codec()
    binary_tree_serialize = codec.serialize(root)
    binary_tree_deserialize = codec.deserialize(binary_tree_serialize)
    print('binary_tree_serialize', binary_tree_serialize)

