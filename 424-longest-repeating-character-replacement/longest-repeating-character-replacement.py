class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L=0
        chars=defaultdict(int)
        res=0
        maxf=0
        for R in range(len(s)):
            chars[s[R]]+=1
            maxf=max(maxf,chars[s[R]])
            while (R-L+1) -maxf > k:
                chars[s[L]]-=1
                L+=1
            res=max(res, R-L+1)
        return res