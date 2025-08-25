# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur_sets, subsets=[],[]
        self.helper(0, nums, cur_sets, subsets)
        return subsets
    def helper(self, i, nums, cur_sets, subsets):
        if i>=len(nums):
            subsets.append(cur_sets.copy())
            return
        cur_sets.append(nums[i])
        self.helper(i+1, nums, cur_sets, subsets)
        cur_sets.pop()
        self.helper(i+1, nums, cur_sets, subsets)