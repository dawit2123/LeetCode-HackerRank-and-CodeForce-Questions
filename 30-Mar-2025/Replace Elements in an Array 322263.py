# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        key_map= {val: key for key, val in enumerate(nums)}
        for operation in operations:
            index= key_map[operation[0]]
            nums[index]= operation[1]
            key_map[operation[1]]=index
        return nums