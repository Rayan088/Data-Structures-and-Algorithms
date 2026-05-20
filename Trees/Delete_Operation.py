"""
In deletion operations, we must search, restructure the tree and preserve BST ordering
Deletion does not destroy nodes like pop() or del, but disconnects nodes from the tree structure
We are changing references

There are 3 deletion cases:
- Leaf Node
- One child
- Two children

Case 1:
Deleting a single leaf node

Visualisation:
        8
3

Just remove 3 as it contains no subtree

Case 2:
Deleting a node that has one child

Visualisation:
                8
        3
            6

We cannot simply erase 3 as subtree 6 would disconnect
Instead we return the child upward so 6 replaces 3

Case 3:
Deleting a node that has two children

Visualisation:
                8
        3               10
    1       6

We cannot simply erase 3 as both subtrees would disconnect
Intead, replace 3 with the inorder successor

Inorder successor is smallest node in right subtree
Successor is larger than everything on left and smaller than remaining right subtree
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def delete(self, root, key):

        # Base Case
        if root is None:
            return root
        
        # Search left subtree
        if key < root.value:
            root.left = self.delete(root.left, key)

        # Search right subtree
        elif key > root.value:
            root.right = self.delete(root.right, key)

        # Node found
        else:

            # Case 1 & Case 2
            # Return subtree to replace deleted node
            if root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
            
            # Case 3: 2 children
            successor = self.min_value_node(root.right) # Find smallest node in right subtree

            root.value = successor.value # Change value

            root.right = self.delete(root.right, successor.value) # Delete old succesor node

        return root

    def min_value_node(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current

    # Helper method to find smallest left subtree value

# Implementing tree
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(6)
root.right = Node(10)

"""
Visualisation:
                            8
            3                               10
    1                6 
"""