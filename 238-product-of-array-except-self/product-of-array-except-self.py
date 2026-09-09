class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        prefix_product=postfix_product=1
        for i in range(0, len(nums)-1):
            prefix_product*=nums[i]
            result[i+1]=prefix_product
        for j in range(len(nums)-1, 0, -1):
            postfix_product*=nums[j]
            result[j-1]*=postfix_product
        return result