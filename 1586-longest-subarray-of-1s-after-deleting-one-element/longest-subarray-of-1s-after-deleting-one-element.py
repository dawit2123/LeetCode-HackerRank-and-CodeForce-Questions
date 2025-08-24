class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        zero_index=-1
        zero_count=0
        l=0
        if 0 not in nums:
            return len(nums)-1
        for i, n in enumerate(nums):
            if nums[i]==0 and zero_count==1:
                l=zero_index+1
                zero_index=i
            elif nums[i]==0 and zero_count==0:
                zero_count=1
                zero_index=i
            count=max(i-l, count)
        return count