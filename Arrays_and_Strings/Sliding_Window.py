"""
Sliding Window is an optimisation technique used when working with subarrays or substrings
Instead of recalculating values every window, we reuse the previous windows calculation
There are 2 types of sliding window: given window size and dynamic window size
In the first example the max sum of an array is found given the window size
The second example finds the longest substring without repeating characters in a dynamic window setting"""

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
class Solution2:
    def longestSubstring(self, s):
        char_set = set()
        left = 0 #Left pointer indicating start of the window
        max_len = 0

        for right in range(len(s)): #Right pointer moves across 
            while s[right] in char_set:
                char_set.remove(s[left]) #Removing the leftmost character from the window
                left += 1 #Moving the left pointer forward
            
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

sol2 = Solution2()
print(sol2.longestSubstring(s = "abcacbb"))