class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        max_diff= float("-inf")
        for i in range(len(nums)-1):
            max_diff= max(max_diff, abs(nums[i]-nums[i+1]))
        max_diff= max(max_diff, abs(nums[0]-nums[len(nums)-1]))
        return max_diff