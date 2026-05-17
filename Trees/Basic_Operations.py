"""
Lists ar linear, one item after another
Many real-world structures are hierarchical
- File systems
- HTML DOM
- Family trees

A tree models hierarchy naturally
A tree is made of nodes connected by edges
- The topmost node is the root
- Nodes with no children are called leaves
- Every subtree is itself a tree which makes trees a natural fit for recursion

                           A
          B                                  C
D                   E              F                    G

A is the parent node
B is a child

A is a parent of B, C
B is a parent of D, E
B and C are siblings
F and G are siblings
D, E, F, G have no children

Trees are powerful as they allow operations faster than linear structures
- Arary: O(n)
- Linked List: O(n)
- Tree: O(log n)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)
    
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.left = Node(8)
root.right.right = Node(9)

"""
Visualisation:
                            5
            3                               7
    1                4              8               9
"""