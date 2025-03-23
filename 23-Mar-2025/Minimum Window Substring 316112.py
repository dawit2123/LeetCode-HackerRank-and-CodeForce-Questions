# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or t=="":
            return ""
        res, res_length=[-1, -1], float('inf')
        freq_t, window_s={}, {}
        for c in t:
            freq_t[c]= 1+freq_t.get(c, 0)
        
        have, need=0, len(freq_t)
        l=0
        for r in range(len(s)):
            c= s[r]
            window_s[c]= 1+window_s.get(c, 0)
            if c in freq_t and window_s[c]==freq_t[c]:
                have+=1
            while have==need:
                # update the result
                if r-l+1 < res_length:
                    res=[l,r]
                    res_length=r-l+1
                # pop the left
                window_s[s[l]]-=1
                if s[l] in freq_t and window_s[s[l]]<freq_t[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if res_length!=float("infinity") else ""
        