class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_len=0
        unique=set()
        left=0
        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left+=1
            unique.add(s[right])
            longest_substring_len= max(longest_substring_len, right-left+1)
        return longest_substring_len