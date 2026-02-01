class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        result=0
        result+=nums[0]
        nums_extracted=nums[1:]
        nums_extracted.sort()
        result+=(nums_extracted[0]+nums_extracted[1])
        return result