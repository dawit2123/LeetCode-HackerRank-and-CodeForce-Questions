# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length=0
        L=0
        for R in range(0,len(s)):
            while(s[R] in s[L:R]):
                L+=1
            longest_length=max(longest_length, R-L+1)
        return longest_length