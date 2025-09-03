# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        result=""
        for i in range(len(arr)):
            min_value=[arr[i], i]
            for j in range(i+1, len(arr)):
                if arr[j]<min_value[0]:
                    min_value=[arr[j], j]
            arr[i], arr[min_value[1]]= arr[min_value[1]], arr[i]
        return arr