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