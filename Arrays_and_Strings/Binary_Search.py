"""
Binary Search is a search algorithm used to find a target value in a sorted array
Instead of checking every element we find the middle element and adjust L and R pointers accordingly
This significantly improves time complexity as it eliminates half the possibilities each step
In this example a target number is found by moving left, right and middle pointers"""

class Solution:
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right: #Loop while there is still a valid search range
            mid = left + ((right - left) // 2) #Calculation of mid index to avoid integer overflow
            #Mid auto adjusts every iteration of the while loop

            if arr[mid] == target:
                return True
            
            elif arr[mid] > target:
                right = mid - 1 #search to the left of the current mid value

            else:
                left = mid + 1 #Search to the right of the current mid value
        
        return False


sol = Solution()
print(sol.binary_search(arr=[-3, -2, -1, 0, 1, 2, 3], target = 2))