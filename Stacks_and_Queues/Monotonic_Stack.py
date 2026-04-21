"""
Most monotonic stack problems are versions of, for each element find the bigger/smaller in a direction
Whereas monotonic queue problems are inside a moving window of a fixed size

Monotonic increasing stack is stack values go up as you go top. E.g. [1, 2, 4, 7]
Montonic decreasing stack is stack values go down as you go top E.g. [7, 4, 2, 1]

The following examples show:
Increasing stack to remove all elements who had a smaller element later
Decreasing stack to remove all elements who had a larger element later
"""

class MonotonicStack:
    def increasing_stack(self, arr):
        stack = []

        for i in range(len(arr)):
            while stack and stack[-1] > arr[i]: #If last element is bigger than current, remove it
                stack.pop()
            stack.append(arr[i])
        return stack

    def decreasing_stack(self, arr):
        stack = []

        for i in range(len(arr)):
            while stack and stack[-1] < arr[i]: #If last element is smaller than current, remove it
                stack.pop()
            stack.append(arr[i])
        return stack
    
#Instances
sol = MonotonicStack()

arr = [2, 1, 2, 4, 3]

print(f"Increasing stack: {sol.increasing_stack(arr)}")
print(f"Decreasing stack: {sol.decreasing_stack(arr)}")