class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        num_of_hills_and_valleys=0
        left=0
        i=1
        while i<len(nums)-1 and len(nums)>0: 
            if nums[i]!=nums[i+1]:
                if (nums[left]<nums[i] and nums[i+1]<nums[i]) or (nums[left]>nums[i] and nums[i+1]>nums[i]):
                    num_of_hills_and_valleys+=1
                left=i
            i+=1
        return num_of_hills_and_valleys