class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur_sets, subsets=[], []
        self.helper(0, nums, cur_sets, subsets)
        return subsets 
    def helper(self, i, nums, cur_sets, subsets):
        if i >= len(nums):
            subsets.append(cur_sets.copy())
            return
        cur_sets.append(nums[i])
        self.helper(i+1, nums, cur_sets, subsets)
        cur_sets.pop()
        while i+1 < len(nums) and nums[i]==nums[i+1]:
            i+=1
        self.helper(i+1, nums, cur_sets, subsets)     