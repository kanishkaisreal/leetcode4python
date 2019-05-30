
# binary tree traversal 
# reference : https://www.youtube.com/watch?v=uWL6FJhq5fM&t=787s 
# inorder traversal trick : https://www.youtube.com/watch?v=f-zmIvul-CA 


# TODO Saturday March 09, 2019: 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root:
        # preorder: root, left, right 
        print(root.data),
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        # postorder: left, right, root 
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def inorder(root):
    if root:
        # postorder: left, root, right 
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# driver code 
# 
if __name__ == "__main__":
    root = Node(45)
    root.left = Node(25)
    root.right = Node(75)
    root.left.left = Node(15)
    root.left.right = Node(35)
    print('preorder binary tree\n')
    preorder(root)
    print('postorder binary tree\n')
    postorder(root)
    print('inorder binary tree\n')
    inorder(root)       