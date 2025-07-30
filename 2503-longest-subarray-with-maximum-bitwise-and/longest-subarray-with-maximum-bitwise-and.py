class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val= max(nums)
        count=0
        i=0
        while i<len(nums):
            if nums[i]==max_val:
                temp_count=1
                while i+1<len(nums) and nums[i]==nums[i+1]:
                    temp_count+=1
                    i+=1
                count=max(count, temp_count)
            i+=1
        return count