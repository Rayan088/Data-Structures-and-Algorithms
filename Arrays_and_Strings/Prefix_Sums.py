"""
Prefix Sum is a technique where you precompure cumulative sums of an array
Instead of summing elements everytime, you build a prefix array once and reuse it
The first type is the Prefix Sum that stores the cumulative sum of elements
Range sum of an array adds numbers from L to R pointers of the original array by subtracting from the prefix array
The alternative way of the range sum stores cumulative sums while avoiding edge cases
"""

#Cumulative Sum
class Solution:
    def runningSum(self, nums):
        prefix = [0] * len(nums) #Duplicating with all 0s
        prefix[0] = nums[0] #Adding 0 to i results in the same number

        for i in range(1, len(nums)): #Start from 1 because 0 is pre-initialised
            prefix[i] = prefix[i-1] + nums[i] #Current sum = previous sum + current num

        return prefix
    
sol1 = Solution()
print(sol1.runningSum(nums=[2, 4, 1, 7, 3]))

#Range Sum
class Solution2:
    def rangeSum(self, nums2, L, R):
        range_prefix = [0] * len(nums2)
        range_prefix[0] = nums2[0]

        for i in range(1, len(nums2)):
            range_prefix[i] = range_prefix[i-1] + nums2[i]

        if L == 0:
            range_sum = range_prefix[R] #No need to subtract L if L is first element
        else:
            range_sum = range_prefix[R] - range_prefix[L-1] # Subtracting by L-1 because R includes sums before L
        
        return range_sum

sol2 = Solution2()
print(sol2.rangeSum([2, 5, 1, 7, 2], 2, 4))

#Alternative Range Sum
class Solution3:
    def rangeSumAlternative(self, nums3, L2, R2):
        range_prefixx = [0] * (len(nums3) + 1) #Index 0 stores extra 0 we avoid edge cases when L = 0

        for j in range(len(nums3)):
            range_prefixx[j+1] = range_prefixx[j] + nums3[j] #Next index is the current sum of range + current index at nums

        range_summ = range_prefixx[R2+1] - range_prefixx[L2] #Range is sum up to index R - Sum before index L

        return range_summ

sol3 = Solution3()
print(sol3.rangeSumAlternative([3, 4, 1, 8, 2, 7], 1, 4))