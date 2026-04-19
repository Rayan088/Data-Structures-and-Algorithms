"""
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle
This means the last element added to the stack is the first one to be removed
Like a stack of plates, you add plates to the top and remove them from the top

Stacks support the following main operations:
- Push: Add elements to the top of the stack
- Pop: Remove the element at the top of the stock
- Peek: View the top element
- isEmpty: Checks if the stack is empty
- Size: Current number of elements in the stack
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        return self.stack

#Class instances
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(f"Stack after pushes: {stack.display()}")

print(f"Top element (peek): {stack.peek()}")

stack.pop()

print(f"Stack after pop: {stack.display()}")

stack.size()

print(f"Size of stack: {stack.size()}")