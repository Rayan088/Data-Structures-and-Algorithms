"""
A Binary Search Tree (BST) adds one constrait that makes searching fast
- For every node, all values in te left subtree are smaller
- All values in the right subtree are larger

Inserting a BST is naturally recursive
If the tree is empty, create a node
Otherwise, go left or right and try again
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)
    
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
    
    #Method declaring value

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    #Method to create root or call helper function

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value) #Insert if left child is empty
            else:
                self.insert_recursive(node.left, value) #Go left again
        else: #Go right
            if node.right is None:
                node.right = Node(value) #Insert if right child is empty
            else:
                self.insert_recursive(node.right, value) #Go right again
    
    #Method to decide where new node goes

root = Node(5)
root.left = Node(3)
root.right = Node(7)

bst = BinarySearchTree()
bst.insert(2)
bst.insert(6)
bst.insert(9)

"""
Visualisation
                            5
            3                               7
    2                              6                  9
"""