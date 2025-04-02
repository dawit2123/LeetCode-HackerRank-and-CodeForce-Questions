class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    temp= (nums[i]- nums[j])*nums[k]
                    result= max(result, temp)
        return result