class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod=(10**9)+7
        count=0
        left, right= 0 , len(nums)-1
        while left<=right:
            if nums[left]+nums[right]>target:
                right-=1
            else:
                count+=(pow(2, right-left, mod))
                left+=1
        return count%mod