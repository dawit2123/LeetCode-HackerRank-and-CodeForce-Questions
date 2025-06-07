# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def rec(ind , parts , prev):
            if ind == len(s):
                return parts >= 2
            for i in range(ind , len(s)):
                num = int(s[ind : i + 1])
                if prev == -10000 or num == prev - 1:
                    if rec(i + 1 , parts + 1 , num):
                        return True
            return False
        return rec(0 , 0 , -10000)