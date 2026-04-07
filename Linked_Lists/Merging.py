"""
Merging two sorted linked lists uses a dummy node and a tail pointer to build a new list
We compare the current nodes of 2 linked lists and attach the smaller one to the merged list
We repeat until one of the lists are empty, when we attach the remaining nodes to the new merged list
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    #Method that creates node with value and next pointer

    def merge_two_lists(l1, l2):
        dummy = ListNode() #Starting placeholder node (dummy -> None)
        curr = dummy #Tail of linked list, as we attach nodes it moves on

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 #Append node to curr
                l1 = l1.next #Move l1 forward
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next #Move curr forward to last node

        #If a list is empty append its nodes
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next #Returns full merged list
    
    #Method that merges two linked lists

    @staticmethod
    def display(head):
        curr = head
        elements = []
        
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements))

        return elements

    #Method that displays linked list

#Initialising L1
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

#Initialising L2
l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

#Display linked list
merged = ListNode.merge_two_lists(l1, l2)
ListNode.display(merged)