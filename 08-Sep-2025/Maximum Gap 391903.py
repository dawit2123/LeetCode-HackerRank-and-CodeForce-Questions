# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        max_value=0
        for i in range(len(nums)-1):
            max_value= max(max_value, (nums[i+1]-nums[i]))
        return max_value