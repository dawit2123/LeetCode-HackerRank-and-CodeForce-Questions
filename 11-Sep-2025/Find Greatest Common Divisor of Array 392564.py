# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num=min(nums)
        max_num= max(nums)
        for num in range(min_num, 0, -1):
            if min_num%num==0 and max_num%num==0:
                return num