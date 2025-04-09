# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hash_map={"a":0, "b":0, "c":0}
        count=0
        left=0
        for right in range(len(s)):
            hash_map[s[right]]+=1
            while hash_map["a"]>0 and hash_map["b"]>0 and hash_map["c"]>0:
                count+=len(s)-right
                hash_map[s[left]]-=1
                left+=1
        return count
