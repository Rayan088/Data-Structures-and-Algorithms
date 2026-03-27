"""
Sorting is the process of arranging a collection of elements in a specific order
This order can be from smallest to largest or vice verca
Bubble Sort algorithm swaps elements until they are in the correct order
Bubble sort is inefficient for large data sets, compared to other sorting algorithms
Selection sort algorithm sorts an array by repeatedly picking the smallest element from the unsorted part and placing it in the correct position
Insertion sort algorithm splits list into sorted and sorted and unsorted parts and inserts elements into correct positions relative to the previous element
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

    def selection_sort(self, arr2):
        n = len(arr2) #Length of array

        for i in range(n):
            min_index = i #Assume first unsorted element is the minimum

            for j in range(i+1, n):
                if arr2[j] < arr2[min_index]: #Find the true minimum
                    min_index = j

            arr2[i], arr2[min_index] = arr2[min_index], arr2[i] #Swap found minimum with unsorted element
        return arr2
    
    def insertion_sort(self, arr3):
        indexing_length = range(1, len(arr3)) #Unsorted part of array

        for i in indexing_length:
            value_to_sort = arr3[i] #Compared value with other indexes starts at first of unsorted part

            while arr3[i-1] > value_to_sort and i > 0 : #Swap if previous is greater than current and current is in range
                arr3[i-1], arr3[i] = arr3[i], arr3[i-1]
                i -= 1 #Swap by going down the list

        return arr3
    
sol1 = Solution()

print(f"Bubble Sort: {sol1.bubble_sort([5, 2, 9, 1, 5, 6])}")
print(f"Selection Sort: {sol1.selection_sort([3, 6, 4, 1, 8, 2])}")
print(f"Insertion Sort: {sol1.insertion_sort([4, 2, 9, 1, 7, 5])}")