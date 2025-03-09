# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

import math
class Solution:
    def longestSquareStreak(self, nums):
       hash_map={}
       nums.sort()
       res=-1
       for num in nums:
        sqrt= math.sqrt(num)
        if sqrt in hash_map:
            hash_map[num]=hash_map[sqrt]+1
            res=max(res, hash_map[num])
        else:
            hash_map[num]=1
       return res 