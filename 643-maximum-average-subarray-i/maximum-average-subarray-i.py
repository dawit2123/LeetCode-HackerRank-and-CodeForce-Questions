class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=float("-inf")
        l=0
        temp=sum(nums[l:k-1])
        for r in range(k-1, len(nums)):
            temp+=nums[r]
            res=max(res, temp/k)
            temp-=nums[r-k+1]
        return res
            