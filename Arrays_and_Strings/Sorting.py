"""
Sorting is the process of arranging a collection of elements in a specific order
This order can be from smallest to largest or vice verca
The following example is the Bubble Sort algorithm which swaps elements until they are in the correct order
Bubble sort is inefficient for large data sets, compared to other sorting algorithms
Selection sort algorithm sorts an array by repeatedly picking the smallest element from the unsorted part and placing it in the correct position
"""

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

    def selection_sort(self, arr):
        n = len(arr) #Length of array

        for i in range(n):
            min_index = i #Assume first unsorted element is the minimum

            for j in range(i+1, n):
                if arr[j] < arr[min_index]: #Find the true minimum
                    min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i] #Swap found minimum with unsorted element

        return arr
    
arr = [5, 2, 9, 1, 5, 6]
sol1 = Solution()

print(f"Bubble Sort: {sol1.bubble_sort(arr)}")
print(f"Selection Sort: {sol1.selection_sort(arr)}")