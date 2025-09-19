# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

from math import gcd

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def lcm(a: int, b: int) -> int:
            return abs(a * b) // gcd(a, b)

        n = len(nums)
        count = 0

        for start_idx in range(n):
            current_lcm = nums[start_idx]

            for num in nums[start_idx:]:
                current_lcm = lcm(current_lcm, num)

                if current_lcm == k:
                    count += 1

                if current_lcm > k:
                    break

        return count