"""
Linked lists are a data structure where nodes are stored in a sequence with each node having a link(s)
Each node in a linked lists contains 2 parts, (Sometimes, Prev):
- Data: Data the node holds
- Next: A reference to the next node in the list
- Prev: A reference to the previous node in the list

The head is the first node of the list
The tail (optional) is the last node of the list
To access any node, you have to start from head and follow links using next until you reach your desired node or the end

Singly Linked Lists:
Each node points to the next node in the list
You can only traverse the list in one direction (head -> None)
"""

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    #Method which creates a node and its Next pointer initialised as None

    def __str__(self):
        return str(self.val)
   
    #Method which directly prints node and not its memory location
    
    @staticmethod
    def display(head):
        curr = Head #Current node is the head (first element)
        elements = []

        while curr: #While current node is pointed to next (stop at None)
            elements.append(str(curr.val))
            curr = curr.next #Increment to next node
        print(" -> ".join(elements)) #Converts into a string with -> inbetween
    
    #Method which traverses the linked list

    @staticmethod
    def search(head, val):
        curr = head
        while curr:
            if val == curr.val:
                return True
            curr = curr.next

        return False
    
    #Method which identifies if Node is in the linked list

Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
#Initalising linked list

Head.next = A
A.next = B
B.next = C
#Initialising next pointers

Head.display(Head)
print(Head.search(Head, 3))
print(Head.search(Head, 6))