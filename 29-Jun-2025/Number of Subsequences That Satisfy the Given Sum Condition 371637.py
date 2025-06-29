# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

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