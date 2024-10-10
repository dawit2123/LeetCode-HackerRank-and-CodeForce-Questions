class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_length=[0]*len(nums)
        i=len(max_length)-1
        max_width=0
        previous_max=0
        for n in reversed(nums):
            max_length[i]=max(n, previous_max)
            previous_max=max_length[i]
            i-=1
        L=0
        for R in range(len(nums)):
            while nums[L] > max_length[R]:
                L+=1
            max_width=max(max_width, R-L)
        return max_width