"""
Detecting a cycle in a linked list, also known as Floyd's Algorithm expands on the idea of fast and slow pointers
We move the fast pointer by 2 steps and slow pointer by 1 step per iteration
If a cycle exists in the linked list, the pointers will eventually overlap and meet
If no cycle exists, the fast pointer will reach the end of the list without meeting the slow pointer
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    #Method which creates a node with its next pointer

    @staticmethod #Static method because it doesn't require access to instance specific data
    def detect_cycle(head):
        slow = fast = head #Setting slow and fast to head

        while fast and fast.next: #While there is a node after fast
            slow = slow.next #Move slow pointer by 1
            fast = fast.next.next #Move fast pointer by 2

            if slow == fast:
                return True
            #If overlap return True
        
        return False #If no overlap return False
    
    #Method which detects cycle
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(2)
#Initialising non repeating linked list

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = head2.next
#Initialising linked list containing a cycle

sol1 = ListNode()
cycle = sol1.detect_cycle(head)
cycle2 = sol1.detect_cycle(head2)

print(f"First Linked List: {cycle}")
print(f"Second Linked List: {cycle2}")
#Displaying results