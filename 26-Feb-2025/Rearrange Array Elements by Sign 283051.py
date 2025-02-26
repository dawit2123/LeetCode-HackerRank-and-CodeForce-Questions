# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums=[]
        negative_nums=[]
        res=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                positive_nums.append(nums[i])
            else:
                negative_nums.append(nums[i])
        for i in range(len(nums)//2):
            res.append(positive_nums[i])
            res.append(negative_nums[i])
        return res