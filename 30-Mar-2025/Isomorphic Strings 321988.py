# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map_s={}
        hash_map_t={}
        for i in range(len(s)):
            cs, ct= s[i], t[i]
            if (cs in hash_map_s and ct!= hash_map_s[cs]) or (ct in hash_map_t and cs!=hash_map_t[ct]):
                return False
            hash_map_s[cs]=ct
            hash_map_t[ct]=cs 
        return True           