"""
Sorting is the process of arranging a collection of elements in a specific order
This order can be from smallest to largest or vice verca
The following example is the Bubble Sort algorithm which swaps elements until they are in the correct order
Bubble sort is inefficient for large data sets, compared to other sorting algorithms"""

class Solution:
    def bubble_sort(self, arr):
        n = len(arr) #Length of array

        for i in range(n):
            swapped = False #Setting swapped to False

            for j in range(n-i-1): #Loop through unsorted portion of list
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] #Swap elements if first index is bigger than second index
                    swapped = True #Set swapped to True

            if not swapped: #Once True, array has been sorted
                break

        return arr
    
arr = [5, 2, 9, 1, 5, 6]
sol1 = Solution()
print(sol1.bubble_sort(arr))