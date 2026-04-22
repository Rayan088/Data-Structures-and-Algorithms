"""
Time Complexity: Measures how the runtime of an algorithm grows with input size n
We describe complexity as Big-O notation
"""

arr = [1, 2, 3, 4, 5]

x = arr[1]
#Constant Time O(1): Always takes same time, regardless of input size

for a in arr:
    print(a)
#Linear Time O(n): Searching through n elements

for i in arr:
    for j in arr:
        print(i, j)
#Quadratic Time O(n^2): Searching through n elements multiple times in nested loops

left, right = 0, len(arr) - 1
target = 2

while left <= right:
    mid = (right - left) // 2

    if arr[mid] == target:
        print(mid)

    elif arr[mid] > target:
        right = left - 1

    else:
        left = mid + 1
#Logarithmic Time O(log n): Binary search halves the problem

"""
Space Complexity: Measures how much memory an algorithm uses as input grows
Types of space usage:
- Input Space: Memory used by the input itself
- Auxilary Space: Extra Memory used by the algorithm
"""

arr = [1, 2, 3, 4, 5]

sum = 0
for x in arr:
    sum += x
#Constant Space O(1): Uses only a fixed number of variables

new_arr = []
for x in arr:
    new_arr.append(x * 2)
#Linear Space O(n): Memory grows with input size

"""
Sometimes you trade memory for speed
Example using a hashmap:
- Faster lookups O(1)
- But uses extra space O(n)

Real world thinking:
- How fast does it grow?
- What happens at scale?
- Is memory a constraint?
- Can I trade space for time?
"""