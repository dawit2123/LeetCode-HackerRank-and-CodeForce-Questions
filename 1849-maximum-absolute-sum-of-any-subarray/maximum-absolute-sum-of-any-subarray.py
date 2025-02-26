class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum, min_sum=nums[0], nums[0]
        temp_max_sum=0
        for num in nums:
            temp_max_sum+=num
            if temp_max_sum<0:
                temp_max_sum=0
            else:
                max_sum=max(max_sum,temp_max_sum)
        temp_min_sum=0
        for num in nums:
            temp_min_sum+=num
            if temp_min_sum>0:
                temp_min_sum=0
            else:
                min_sum= min(min_sum, temp_min_sum)
        return max(abs(min_sum), abs(max_sum))        