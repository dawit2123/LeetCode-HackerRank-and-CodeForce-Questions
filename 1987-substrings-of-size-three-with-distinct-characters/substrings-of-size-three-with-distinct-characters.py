class Solution:
    def countGoodSubstrings(self, s: str) -> int:     
        if len(s)<3:
            return 0
        count=0
        for index in range(len(s)-2):
            if len(set(s[index:index+3]))==3:
                count+=1
        return count
