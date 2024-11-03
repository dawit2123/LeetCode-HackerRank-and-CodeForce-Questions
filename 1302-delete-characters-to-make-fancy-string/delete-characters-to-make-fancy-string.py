class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy_str=s[0]
        count=1
        for i in range(1, len(s)):
            if s[i]==fancy_str[-1]:
                count+=1
                if count<3:
                    fancy_str+=s[i]
            else:
                count=1
                fancy_str+=s[i]           
        return fancy_str