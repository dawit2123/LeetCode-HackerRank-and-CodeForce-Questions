# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        answer=float("inf")
        target_sum= sum(nums)-x
        left_index=current_sum=0
        for right_index, val in enumerate(nums):
            current_sum+=val
            while left_index<=right_index and current_sum>target_sum:
                current_sum-=nums[left_index]
                left_index+=1
            if current_sum==target_sum:
                answer= min(answer, len(nums)-(right_index-left_index+1))
        return -1 if answer==float("inf") else answer
                
