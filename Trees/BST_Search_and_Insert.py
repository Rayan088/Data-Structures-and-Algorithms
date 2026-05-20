"""
BST's are useful as they are ordered improving search complexity to O(log n)

In BST's we perform 3 main operations:
- Search
- Insert
- Delete

Visualisation
                            8
            3                                10
    1                6                                  14
                4         7                        13

Searching works like a binary search
At each node:
- smaller -> go left
- larger -> go right
- equal -> found

Insertion is search until you find None
Then, create a new node there
Every rescursive call returns new subtree upward
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def search(self, root, key):
        if root is None:
            return None
        
        if root.value == key:
            return f"Found: {root.value}"
        
        if root.value > key: # If root is greater go left
            return self.search(root.left, key)
        
        if root.value < key: # If root is smaller go right
            return self.search(root.right, key)
    
        return "Not found"
    
    # Search algorithm

    def insert(self, root, key):
        if root is None:
            return Node(key) # Create new node when None is found
        
        if root.value > key:
            root.left = self.insert(root.left, key) # Inserting into left subtree

        elif root.value < key:
            root.right = self.insert(root.right, key) # Inserting into right subtree

        return root # Root of updated subtree

    # Insertion algorithm

# Creating BST   
bst = Node(0)     
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(13)

# Search instance
print(bst.search(root, 13))

# Insert instance
print(bst.insert(root, 10))