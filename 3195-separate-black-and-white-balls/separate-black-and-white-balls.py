class Solution:
    def minimumSteps(self, s: str) -> int:
        result=0
        L=0
        for R in range(len(s)):
            if s[R]=="0":
                result+=(R-L)
                L+=1
        return result