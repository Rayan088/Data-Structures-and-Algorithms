"""
A deque is a double ended queue, you can remove and add from either the front or the back
- append(): adds to right (back)
- appendleft(): adds to left (front)
- pop(): removes from right (back)
- popleft(): removes from left (front)

In the following problem we find max number in window k:
- we remove elements from the front (when they go out the window)
- we remove elements from the back (when they are smaller/larger)

The deque stores elements in decreasing order, removing if a bigger one is appended
"""

from collections import deque

class Solution:
    def max_sliding_window(self, nums, k):
        result = [] #Stores max of each window
        dq = deque() #Stores indices

        for i, val in enumerate(nums):
            if dq and dq[0] < i - k + 1: #Current index in dq compared to current window start
                dq.popleft()
            #If front index is too old, remove it

            while dq and nums[dq[-1]] < val:
                dq.pop()
            #Remove indices from the back if values are smaller than current val

            dq.append(i)
            #Add current index

            if i >= k - 1:
                result.append(nums[dq[0]])
            #Add first index as it is always the maximum            

        return result

#Instances    
sol = Solution()
print(sol.max_sliding_window(nums=[1, 3, -1, -3, 5], k=2))