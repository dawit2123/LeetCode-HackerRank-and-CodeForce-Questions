class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        l=0
        r=len(nums)-1
        while l<r:
            res=max(res, nums[l]+nums[r])
            l+=1
            r-=1
        return res
