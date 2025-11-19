class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            i=nums.index(original)
            original=nums[i]*2
            nums[i],nums[-1]= nums[-1], nums[i]
            nums.pop()
        return original