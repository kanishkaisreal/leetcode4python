# Problem 8 - Unival  ( Universal Value Tree) tree
# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes have the same value.

# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
# ( an emppty tree is also a unival tree)
#    0
#   / \
#  1*   0
#     / \
#    1*   0*
#   / \
#  1*   1*
# 4 leaf nodes  + and last leaf. 
# https://www.youtube.com/watch?v=7HgsS8bRvjo

# def is_unival(root):
#     if root === null :  ( empty tre) 
#         return True
#     if root.left !=null and root.left.data ! = root.data:
#         return False
#     if root.right !=null and root.right.data != root.data:
#         return False
#     if is_unival(root.left) and is_unival(root.right):
#         return True 



class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def is_unival(root):
    if root is None:   # base condition 
        return True  
    if root.left is not None and root.left.data != root.data:
        return False
    if root.right is not None and root.right.data != root.data:
        return False
    if is_unival(root.left) and is_unival(root.right):  # this will take care of the condition where left and right child is null ( coz it goes to base conditon)
        return True
    return False

def count_univals(root):
    if root is None: # base condition  .. empty tree has 0 subtree 
        return 0

    total_count = count_univals(root.left) + count_univals(root.right)
    if is_unival(root):
        total_count += 1
    return total_count

def count_univals2(root):
    total_count, is_unival = helper(root)
    return total_count
 
def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)

    is_unival = True
    if not is_left_unival or not is_right_unival:
        is_unival = False
    if root.left is not None and root.left.value != root.value:
        is_unival = False
    if root.right is not None and root.right.value != root.value:
        is_unival = False
    if is_unival:
        return left_count + right_count + 1, True
    else:
        return left_count + right_count, False


root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.left.left = Node(1)
root.right.left.right = Node(1)
root.right.right = Node(1)
# tree1 looks like:
#         0
#        / \
#       1   0
#          / \
#         1   0
#        / \
#       1   1

print('number of unival tree', count_univals(root))


root = Node(3) 
root.left = Node(2)
root.right =  Node(4) 
root.right.left = Node(4)
root.right.right = Node(4)
root.right.right.right = Node(4) 
# tree2 looks like:
#         3
#        / \
#       2   4
#          / \
#         4   4
#              \
#               4

print('number of unival tree', count_univals(root))

root = Node(3)
root.left = Node(3)
root.right  = Node(3)
root.right.left = Node(3)
root.right.right = Node(3) 
root.right.right.right= Node(2)
# tree3 looks like:
#         3
#        / \
#       3   3
#          / \
#         3   3
#              \
#               2
print('number of unival tree', count_univals(root))



