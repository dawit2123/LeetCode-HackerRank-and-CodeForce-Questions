# Problem: Check If It Is a Good Array - https://leetcode.com/problems/check-if-it-is-a-good-array/description/?envType=problem-list-v2&envId=number-theory

from math import gcd

class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        
        return gcd(*nums) == 1