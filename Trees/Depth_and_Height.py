"""
A tree is hierarchical, in levels
Depth and height are measurements within this hierarchy

Visualisation:
                              A
                  B                        C  
           D             E 
                      F

Degree: Number of children of a node
- Degree(A) = 2
- Degree(B) = 2
- Degree(C) = 0

Depth: The number of edges from the root to that node
Depth measures Root -> Node
It tells us how deep we have gone from the root
Calculates from the root down

- Depth(A) = 0 (A)
- Depth(B) = 1 (A -> B)
- Depth(F) = 3 (A -> B -> E -> F)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_depth(root, depth=0):

    if root is None:
        return 

    print(root.value, "depth =", depth)

    print_depth(root.left, depth + 1) #Calls left child

    print_depth(root.right, depth + 1) #Calls right child

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.left.right.left = Node("F")

print_depth(root, 0)

"""
Visualisation:
                              A
                  B                        C  
           D             E 
                      F

Height: The number of edges in the longest path from that node to a leaf
Height measures node to deepest leaf
It tells us how far downward from a node

- Height(A) = 3 (A -> B -> E -> F)
- Height(B) = 2 (B -> E -> F)
- Height(D) = 0 (D)
- Height(F) = 0 (F)

Recursive Formula: h(node) = 1 + max(h(left), h(right))
The 1 represents edge downward to child
max represents maximum height of either child node
Calculates from the bottom level up
"""

def height(root):

    if root is None:
        return -1 #-1 due to being child height
    
    left_height = height(root.left) #Calculates height of left subtree

    right_height = height(root.right) #Calculates height of right subtree

    return 1 + max(left_height, right_height) #Finds max of child subtrees and adds 1

print(f"Height: {height(root)}")