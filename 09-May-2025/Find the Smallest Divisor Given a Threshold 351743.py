# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        min_number = 1
        max_number = max(nums)
        result = float('inf')
        
        while min_number <= max_number:
            mid = (min_number + max_number) // 2
            temp_sum = 0
            
            for num in nums:
                temp_sum += math.ceil(num / mid)
                    
            if temp_sum <= threshold:
                result = min(result, mid)
                max_number = mid - 1
            else:
                min_number = mid + 1
                
        return result