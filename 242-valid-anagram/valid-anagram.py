from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_count, t_count= Counter(s), Counter(t)
        return s_count==t_count