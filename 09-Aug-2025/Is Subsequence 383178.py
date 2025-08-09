# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        WL=0
        SL=0
        while WL<len(t) and SL<len(s):
            if s[SL]==t[WL]:
                SL+=1
            WL+=1
        return True if SL==len(s) else False 
