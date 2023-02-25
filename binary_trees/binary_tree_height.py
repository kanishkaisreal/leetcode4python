# Python program to find the maximum height of tree 
  
# A binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Compute the "maxHeight" of a tree -- the number of nodes  
# along the longest path from the root node down to the  
# farthest leaf node 
def findHeight(node): 
    if node is None: 
        return 0 ;  
    else : 
        # Compute the depth of each subtree 
        leftHeight = findHeight(node.left) 
        rightHeight = findHeight(node.right) 
  
        # Use the larger one 
        maxHeight= (leftHeight+1) if (leftHeight > rightHeight) else (rightHeight+1)
        return maxHeight

# Driver program to test above function 
#       1 
#     /   \ 
#    2     3 
#   /  \  
#  4    5
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
  
print ("Height of tree is %d", (findHeight(root)))