class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        increasing_wiggle=1
        decreasing_wiggle=1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                increasing_wiggle= max(increasing_wiggle, decreasing_wiggle+1)
            elif nums[i]<nums[i-1]:
                decreasing_wiggle= max(decreasing_wiggle, increasing_wiggle+1)
        return max(increasing_wiggle, decreasing_wiggle)
    