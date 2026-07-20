"""
Time Complexity: Measures the runtime of an algorithm
We describe complexity as Big-O notation

O(1) - Constant Time
O(n) - Linear Time
O(n^2) - Quadratic Time
"""

arr = [1, 2, 3, 4, 5]

def get_first(arr):
    return arr[0]

# O(1) due to only one operation performed irregardless of array size

def print_all(arr):
    for x in arr:
        print(x)

def addition(arr):
    arr = set(arr) # Dicts have constant lookup

    for x in arr:
        if x + 1 in arr:
            print(x) 

# O(n) due to loop running for n length of array

def pairs(arr):
    for x in arr:
        for y in arr:
            print(x, y)

def addition(arr):
    for x in arr:
        if x + 1 in arr:
            print(x)

# O(n^2) due to looping through array twice

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

# O(log n) due to repeatedly halving search area

"""
Space Complexity: Measures how much memory an algorithm uses as input grows

Types of space usage:
- Input Space: Memory used by the input itself
- Auxilary Space: Extra Memory used by the algorithm
"""

arr = [1, 2, 3, 4, 5]

def sum_array(arr):
    total = 0

    for x in arr:
        total += x

# O(1) due using a fixed number of variables

def squares(arr):
    new_arr = []

    for x in arr:
        new_arr.append(x * 2)

#O(n) as memory grows with input size

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