"""
A Breadth First Search (BFS) is a type of horizontal tree traversal
It visits nodes level by level

Concept:
- Take one node out
- Process it
- Put its children in
- Repeat until no nodes left

Every node enters and leaves queue once
Time Complexity: O(n)
Lists are too slow as pop() shifts everything left

Visualisation:
                              1
                  2                        3  
           4             5            6           7
"""

from collections import deque #Double ended queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return
    
    queue = deque([root]) #Queue stores nodes waiting to be explored

    while queue:
        current = queue.popleft() #Process next node

        print(current.value, end=" ")

        if current.left: #Add children on left side
            queue.append(current.left)

        if current.right: #Add children on right side
            queue.append(current.right)

#Instances
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

bfs(root)