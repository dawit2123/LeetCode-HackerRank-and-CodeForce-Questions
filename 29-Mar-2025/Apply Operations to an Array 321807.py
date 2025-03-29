# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                res[j]=nums[i]
                j+=1
        return res
        