"""
Fast and slow pointers technique is the idea where two pointers move in different speeds
Typically the slow pointer moves by 1 step and the fast pointer moves by 2 steps per iteration

The following example is finding the middle of a linked list:
We move slow and fast pointers at different speeds until fast reaches the end of the list
Since we move the fast pointer twice as quick this will result in the slow pointer landing at the middle when the linked list comes to an end
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    #Method which creates a node and its next pointer

    @staticmethod #Static Method because it doesnt require access to instance-specific data
    def find_middle(head):
        slow = fast = head #Setting slow and fast equal to head

        while fast and fast.next: #While there is a node after fast
            slow = slow.next #Move slow pointer by 1
            fast = fast.next.next #Move fast pointer by 2

        return slow #Return middle of list
    
    #Method that finds the middle of a linked list
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
#Initialising linked list

sol1 = ListNode()
middle_node = sol1.find_middle(head)

print(f"Midlle of the list: {middle_node.val}")