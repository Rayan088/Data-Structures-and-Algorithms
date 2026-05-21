"""
In binary trees every node has at most 2 children (left child, right child)
N-ary tres allows any number of children for each node

Visualisation:
                                    A
                B                   C                   D
        E       F       G                               H
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.children = [] # List of child nodes

    def dfs(self, node):
        if node is None:
            return
        
        print(node.value, end=" ")

        for child in node.children:
            self.dfs(child)
    
    # Depth First Search

    def search(self, node, target):
        if node is None:
            return
        
        if node.value == target:
            return True
        
        for child in node.children:
            if self.search(child, target):
                return True
            
        return False
    
    # Search for target value

# Creating Nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")

# Initialising children
A.children = [B, C, D]
B.children = [E, F, G]
D.children = [H]

#Calling methods
A.dfs(A)

print("\n")

print(A.search(A, "F"))