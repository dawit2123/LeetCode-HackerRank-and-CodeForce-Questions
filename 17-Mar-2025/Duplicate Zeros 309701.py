# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index=0
        n=len(arr)
        while index<n:
            if arr[index]==0:
                arr.insert(index+1, 0)
                index+=1    
            index+=1
        while len(arr)>n:
            arr.pop()
