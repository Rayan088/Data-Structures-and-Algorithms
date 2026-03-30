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
   
    #Method which directly returns node and not its memory location
    
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

print("\n")

"""
Doubly Linked Lists:
Each node points to the next and previous node in the list
You can traverse the list in both directions (head <-> Node <-> None)
Inserting at beginning and end is constant time
"""

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    #Method which creates a node with next and previous pointers

    def __str__(self):
        return str(self.val)
    
    #Method which returns node 
    
    @staticmethod
    def display(head):
        curr = head
        elements = []

        while curr: #While current node is pointed to next
            elements.append(str(curr.val))
            curr = curr.next
        print(" <-> ".join(elements))
    
    #Method which traverses the list

    @staticmethod
    def insert_at_beginning(head, tail, val):
         new_node = DoublyNode(val, next=head) #Node created with its value and next pointer set to current head
         head.prev = new_node #Updating heads previous node to new node

         return new_node, tail #Returning new head and unchanged tail
    
    #Method which inserts node at beginning of linked list
    
    @staticmethod
    def insert_at_end(head, tail, val):
        new_node = DoublyNode(val, prev=head) #Node created with its value and previous pointer set to head of current last element
        tail.next = new_node #Updating tails next node to new node

        return head, new_node #Returning unchanged head (None) and new tail
    
    #Method which inserts node at end of linked list
        
head = tail = DoublyNode(1)
DoublyNode.display(head) #Displaying current linked list
head, tail = DoublyNode.insert_at_beginning(head, tail, 3)
head, new_node = DoublyNode.insert_at_end(head, tail, 7)
DoublyNode.display(head) #Displaying upadted linked list