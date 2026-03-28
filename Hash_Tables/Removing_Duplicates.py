"""
Dictionaries are great for counting occurences because they allow you to update the count of each key
Sets are great for removing duplicates, as they automatically discard any repeated values
In this example we find the duplicates of an array
"""

class Solution:
    def find_duplicates(self, arr):
        seen = set()
        duplicates = set()

        for item in arr:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        #Adds item to appropriate set

        return duplicates
    
sol = Solution()
print(sol.find_duplicates([1, 2, 3, 3, 4, 5, 5, 5, 6, 6]))