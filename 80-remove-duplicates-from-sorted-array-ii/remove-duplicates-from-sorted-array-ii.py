class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L=0
        for R in range(2, len(nums)):
            if nums[L]==nums[R] and nums[R]==nums[R-1]:
                continue
            else:
                L+=1
                nums[L+1]=nums[R]
        return L+2