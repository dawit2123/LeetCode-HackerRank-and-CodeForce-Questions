# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        max_count=0
        previous_pair=None
        left=0
        for right in range(1, len(s)):
            if s[right]==s[right-1]:
                if previous_pair:
                    left= previous_pair
                previous_pair=right
            max_count= max(max_count, right-left+1)
        return max_count