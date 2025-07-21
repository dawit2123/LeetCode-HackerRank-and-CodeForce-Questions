class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        fancy_str=s[:2]
        for i in range(2, len(s)):
            if not (s[i]==fancy_str[-1] and s[i]==fancy_str[-2]):
                fancy_str+=s[i]
        return fancy_str
        
        