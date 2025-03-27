# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr), 1, -1):
            maximum_index = arr.index(i)
            res.extend([maximum_index + 1, i])
            first = arr[:maximum_index+1][::-1]
            arr = first + arr[maximum_index+1:]
            second = arr[:i][::-1]
            arr = second + arr[i:]
        return res