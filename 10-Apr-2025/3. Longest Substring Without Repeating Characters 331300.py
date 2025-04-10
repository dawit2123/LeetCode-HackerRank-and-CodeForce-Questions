# Problem: 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        l=0
        res=0
        for r in range(len(s)):
            if s[r] in seen:
                l=max(seen[s[r]]+1, l)
            seen[s[r]]=r
            res=max(r-l+1, res)
        return res