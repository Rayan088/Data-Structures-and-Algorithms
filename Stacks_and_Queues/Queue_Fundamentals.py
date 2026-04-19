"""
A queue is a linear data structure thats follows the FIFO (First In, First Out) principle
This means that elements are added at the end and removed from the front of the queue
Like a line of people waiting to be served, the first person to join is the first one to be served

Queues support the following main operations:
- Enqueue: Add an element to the end of the queue
- Dequeue: Remove the element from the front of the queue
- Peek: View the front element
- isEmpty: Check if queue is empty
- Size: Check size of queue
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"
    
    def peek(self):
        if not self.is_empty:
            return self.queue[0]
        else:
            return "Queue is empty"
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        return self.queue

#Class instances    
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"Queue after pushes: {queue.display()}")

queue.dequeue()

print(f"Queue after pop: {queue.display()}")

print(f"Length of queue: {queue.size()}")