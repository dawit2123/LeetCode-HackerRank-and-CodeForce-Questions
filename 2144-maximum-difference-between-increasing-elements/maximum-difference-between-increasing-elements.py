class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if not nums:
            return -1
        max_diff=-1
        min_num=nums[0]
        for i in range(1, len(nums)):
            max_diff= max(max_diff, nums[i]-min_num)
            min_num= min(min_num, nums[i])
        return max_diff if max_diff!=0 else -1
        