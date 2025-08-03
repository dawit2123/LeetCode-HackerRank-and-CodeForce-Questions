class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # use the dp approach starting from the end of the list to the beginning
        len_subsequence=[1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    len_subsequence[i]= max(len_subsequence[i], len_subsequence[j]+1)
        return max(len_subsequence)