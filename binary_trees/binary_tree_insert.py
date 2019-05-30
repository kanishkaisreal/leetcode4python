class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" Inorder traversal of a binary tree"""


def inorder(temp):

    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


"""function to insert element in binary tree """


def insert(temp, data):

    q = []
    q.append(temp)

    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = Node(data)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = Node(data)
            break
        else:
            q.append(temp.right)


# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    data = 12
    insert(root, data)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)
