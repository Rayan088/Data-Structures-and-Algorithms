"""
Two Pointers is a technique used to iterate through arrays or strings efficiently by using two indices instead of nested loops
Use when an array/string is sorted or problem depends on sum/distance
Two pointers (left & right) will be placed on opposite sides and move based on a condition
In this example two pointers will move from the left and right ends to find a target number
"""

class Solution():
    def twoSumII(self, numbers, target):
        left = 0 #Left pointer placed on Array position 0
        right = len(numbers) - 1 #Right pointer placed on last Array position
        while left < right:
            current_number = numbers[left] + numbers[right]
            if current_number > target:
                right -= 1 #Moving down the list
            elif current_number < target:
                left += 1 #Moving up the list
            else:
                return [left + 1, right + 1] #Returns 1-based indexing

sol = Solution()
print(sol.twoSumII([1, 3, 5, 6, 9, 11], 15))