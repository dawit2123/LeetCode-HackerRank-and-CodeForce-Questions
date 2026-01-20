class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result=[-1]*len(nums)
        for i in range(len(nums)):
            for j in range(nums[i]):
                if (j | j+1)==nums[i]:
                    result[i]=j
                    break
        return result