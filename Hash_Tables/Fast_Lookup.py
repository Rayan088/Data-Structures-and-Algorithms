"""
Hash tables are commonly used due to its fast lookup property
The time it takes to retrieve a value from a hash table is constant or O(1)
The lookup is fast because the key "Alice" hashes to a specific index, allowing quick retrievel of its value
Since the index for the key is directly computed, no iteration over the entire dictionary is needed
"""

class Solution:
    def fast_lookup(self, dictionary):
        alice_score = dictionary["Alice"]
        #Fast lookup of Alice assigned value

        return alice_score
    
    def safe_lookup(self, dictionary):
        bob_score = dictionary.get("Bob", "Not Found")
        #Get method avoids throwing an error if key doesnt exist

        return bob_score

dictionary = {"Alice": 85,
                    "Bob": 90,
                    "Charlie": 78,
                    "David": 92}

sol = Solution()
print(sol.fast_lookup(dictionary))
print(sol.safe_lookup(dictionary))