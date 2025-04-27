class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        valid_sub_arrays=0
        # check for the length of the number if it's less than 3
        if len(nums)<3:
            return 0
        left=0
        for right in range(2, len(nums)):
            if ((nums[left]+nums[right])==(nums[right-1]/2)):
                valid_sub_arrays+=1
            left+=1
        return valid_sub_arrays