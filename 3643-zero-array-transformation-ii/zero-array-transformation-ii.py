from typing import List
from bisect import bisect_left

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(k: int) -> bool:
            difference_array = [0] * (len(nums) + 1)
            for left, right, value in queries[:k]:
                difference_array[left] += value
                difference_array[right + 1] -= value
            accumulated_sum = 0
            for original_value, change in zip(nums, difference_array):
                accumulated_sum += change
                if original_value > accumulated_sum:
                    return False
            return True
        num_queries = len(queries)
        l = bisect_left(range(num_queries + 1), True, key=check)       
        return -1 if l > num_queries else l
