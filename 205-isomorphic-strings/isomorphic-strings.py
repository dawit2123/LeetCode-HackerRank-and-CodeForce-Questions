class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map= {}, {}
        for i in range(len(s)):
            s1, t1= s[i], t[i]
            if (s1 in s_map and s_map[s1]!=t1) or (t1 in t_map and t_map[t1]!=s1):
                return False
            s_map[s1]=t1
            t_map[t1]=s1
        return True