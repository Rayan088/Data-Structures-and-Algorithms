"""
Sliding Window is an optimisation technique used when working with subarrays or substrings
Instead of recalculating values every window, we reuse the previous windows calculation
There are 2 types of sliding window: given window size and dynamic window size
In the first example the max sum of an array is found given the window size"""

#Given Window Size
class Solution(object):
    def findMax(self, nums, k):
        current_window = 0
        maximum_sum = float("-inf") #Set to negative infinity rather than 0 because negative numbers will calculate incorrect output

        for i in range(len(nums)):
            current_window += nums[i] #Adds on i from the list one at a time

            if i + 1 >= k: #If the current iteration is greater than window size
                maximum_sum = max(maximum_sum, current_window)
                current_window -= nums[i + 1 - k] #Subtracts the leftmost number leaving the window
        
        return maximum_sum
    
sol = Solution()
print(sol.findMax(nums = [4, 2, 1, 7, 8, 1, 2, 8], k = 3))

#Dynamic Window Size