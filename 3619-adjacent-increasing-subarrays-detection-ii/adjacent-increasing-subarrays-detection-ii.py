class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        inc=1
        prev_inc=0
        max_inc=0
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                inc+=1
            else:
                prev_inc=inc
                inc=1
            max_inc= max(max_inc, max(inc//2, min(prev_inc, inc)))
        return max_inc
