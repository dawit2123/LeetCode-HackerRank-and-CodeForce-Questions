# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map= Counter(arr1)
        result=[]
        arr2_set= set(arr2)
        for num in arr2:
            result.extend([num]*hash_map[num])
        for key in sorted(hash_map.keys()):
            if key not in arr2_set:
                result.extend([key]*hash_map[key])
        return result