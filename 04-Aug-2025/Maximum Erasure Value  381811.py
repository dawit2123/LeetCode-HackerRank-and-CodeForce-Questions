# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum=0
        temp_sum=0
        l=0
        visited=set()
        for r in range(len(nums)):
            if nums[r] not in visited:
                temp_sum+=nums[r]
                visited.add(nums[r])
                max_sum= max(max_sum, temp_sum)
            else:
                while l<r and nums[l]!=nums[r]:
                    temp_sum-=nums[l]
                    visited.remove(nums[l])
                    l+=1
                l+=1
        return max_sum