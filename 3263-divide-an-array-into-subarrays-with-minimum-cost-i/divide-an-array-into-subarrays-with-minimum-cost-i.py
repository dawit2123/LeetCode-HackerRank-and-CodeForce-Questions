class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first=nums[0]
        second=float('inf')
        third=float('inf')
        for i in range(1, len(nums)):
            if nums[i]<second:
                third=second
                second=nums[i]
            elif nums[i]<third:
                third=nums[i]
        return (first+second+third)