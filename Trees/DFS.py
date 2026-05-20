"""
Depth First Search is a type of tree traversal
A traversal means visiting every node

Preorder - Root -> Left -> Right
Inorder - Left -> Root -> Right
Postorder  Left -> Right -> Root
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)
    
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

"""
Visualisation:
                              1
                  2                        3  
           4             5            6           7


Preorder Traversal:
Rule: Root -> Left -> Right
"""

def preorder(root):
    if root is None:
        return
    
    print(root.value, end=" ") #prints space instead of newline

    preorder(root.left)
    preorder(root.right)

#Preorder: 1 2 4 5 3 6 7

print("Preorder: ", end="")
preorder(root)

print("\n")

"""
In BST inorder traversal gives sorted order
Inorder Traversal:
Rule: Left -> Root -> Right
"""

def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.value, end=" ")

    inorder(root.right)

#Inorder: 4 2 5 1 6 3 7

print("Inorder: ", end= "")
inorder(root)

print("\n")

"""
Postorder Traversal:
Rule: Left, Right, Root
"""

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.value, end=" ")

#Postorder: 7 3 6 1 5 2 4

print("Postorder: ", end="")
postorder(root)