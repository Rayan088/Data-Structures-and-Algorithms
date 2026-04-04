"""
Reversing the direction of a list by reversing by next pointers so that the first node becomes the last and so on
Time complexity is O(n) as we iterate through each node once
Space complexity is constant O(1) as only a constant amount of extra space is used (3 pointers)
"""

class Linked_List:
    def __init__(self, val, next=None,):
        self.val = val
        self.next = next
    
    #Method which creates a node and next pointer as none

    def __str__(self):
        return str(self.val)
    
    #Method which returns node

    def reverse_linked_list(head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next #Setting next node to current.next
            curr.next = prev #Changing the direction to the previous node
            prev = curr #Move prev one step forward and make it the current node
            curr = next_node #Move current one step forward to next node in list
        #Visualisation: After one iteration, prev on 1st element, curr on 2nd element, next_node on 3rd element
        
        return prev
    
    #Method that reverses the linked list

    @staticmethod
    def display(head):
        curr = head
        elements = []

        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements))
    
    #Method which displays linked list

head = Linked_List(1)
head.next = Linked_List(2)
head.next.next = Linked_List(3)
head.next.next.next = Linked_List(4)
#Creating the linked list and the next pointers for each element

print("Original List:")
Linked_List.display(head)
#Displays original list

head = Linked_List.reverse_linked_list(head)

print("\nReversed List:")
Linked_List.display(head)
#Displays reversed list