class Solution:
    def check(self, nums: List[int]) -> bool:
        n= len(nums)
        if n<=1:
            return True
        inversion_count=0
        for i in range(1, n):
            if nums[i]<nums[i-1]:
                inversion_count+=1
        if nums[0]<nums[n-1]:
            inversion_count+=1
        return inversion_count<=1