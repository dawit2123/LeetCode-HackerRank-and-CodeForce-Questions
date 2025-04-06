from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_index = 0 
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[max_index] < dp[i]:
                max_index = i
      
        subset_size = dp[max_index]
        current_index = max_index
        largest_subset = []
        while subset_size:
            if nums[max_index] % nums[current_index] == 0 and dp[current_index] == subset_size:
                largest_subset.append(nums[current_index])
                max_index, subset_size = current_index, subset_size - 1
            current_index -= 1
        return largest_subset