class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        for num in nums:
            if(num!=nums[l]):
                nums[l+1]=num
                l+=1
        return l+1