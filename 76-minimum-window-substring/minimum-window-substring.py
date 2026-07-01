class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        s_count, t_count={}, {}
        for c in t:
            t_count[c]=t_count.get(c, 0)+1
        have, need = 0, len(t_count)
        res, res_len= [-1, -1], float('infinity')
        left=0
        for right in range(len(s)):
            c=s[right]
            s_count[c]=s_count.get(c, 0)+1
            if c in t_count and s_count[c]==t_count[c]:
                have+=1
            while have==need:
                if (right-left+1)<res_len:
                    res=[left, right]
                    res_len=(right-left+1)
                s_count[s[left]]-=1
                if s[left] in t_count and s_count[s[left]]<t_count[s[left]]:
                    have-=1
                left+=1
        l, r= res
        return s[l:r+1] if res_len!=float('infinity') else ""