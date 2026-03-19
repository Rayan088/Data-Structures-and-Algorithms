"""
Frequency Counting is counting how many times each element appears
Instead of repeatedly scanning an array we can store counts in a hash map (dictionary)
Dictionaries is not position-based rather in the format: key -> value
It can be iterated by using .items() or .values()
"""

class Solution:
    def frequency_counting(self, array):
        dict = {}

        for element in array:
            if element in dict:
                dict[element] += 1
            else:
                dict[element] = 1

        return dict
    
sol = Solution()
print(sol.frequency_counting(["a", "b", "a", "c", "b", "a"]))


"""
A defaultdict is a normally dictionary but it automatically creates a default value when a key doesn't exist
You must have defaultdict() with int, list, set etc in the parenthesis
All values passed in will be set to a default of 0 or empty
"""

from collections import defaultdict #Importing Library

class Solution2:
    def frequency_counting2(self, nums):
        default_dict = defaultdict(int)

        for x in nums:
            default_dict[x] += 1

        return default_dict
    
sol2 = Solution2()
print(sol2.frequency_counting2([1, 2, 3, 4, 3, 2, 2, 5]))