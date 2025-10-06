class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result=nums[0]
        temp=0
        for i in range(len(nums)):
            if temp<0:
                temp=0
            temp+=nums[i]
            result=max(result, temp)
        return result